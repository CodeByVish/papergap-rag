"""Compare RRF with RRF+BGE on a deterministic training-only query pilot."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

from scripts.build_indexes import PINNED_REVISION, load_passages, revision_sha
from scripts.demo_hybrid import RERANKER_REVISION
from scripts.demo_p1 import _check_same_passages
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def select_queries(
    qa_path: Path, paper_counts: dict[str, int], count: int, minimum: int
):
    """Project only query inputs after filtering train; never return annotations."""
    if count < 1 or minimum < 1:
        raise ValueError("question count and minimum passages must be positive")
    candidates = []
    with qa_path.open(encoding="utf-8") as source:
        for line in source:
            row = json.loads(line)
            if row.get("source_split") != "train":
                continue
            if paper_counts.get(row.get("paper_id"), 0) < minimum:
                continue
            projected = {
                key: row[key] for key in ("question_id", "paper_id", "question")
            }
            if any(
                not isinstance(value, str) or not value.strip()
                for value in projected.values()
            ):
                raise ValueError("Training query inputs must be nonempty strings")
            candidates.append(projected)
    selected, seen = [], set()
    for row in sorted(
        candidates, key=lambda row: (row["paper_id"], row["question_id"])
    ):
        if row["paper_id"] not in seen:
            selected.append(row)
            seen.add(row["paper_id"])
        if len(selected) == count:
            return selected
    raise ValueError(
        f"Only {len(selected)} eligible training papers; requested {count}"
    )


def compare_queries(sparse, dense, scorer, queries, candidate_ks, top_k, rrf_k):
    """Measure complete retrieval calls; warm both paths once per configuration."""
    records = []
    for candidate_k in candidate_ks:
        source_ids = {}

        def counted(name, retrieve, collected=source_ids):
            def callback(query, paper_id, top_k):
                hits = retrieve(query, paper_id, top_k)
                collected[name] = {hit.passage.passage_id for hit in hits}
                return hits

            return callback

        kwargs = {"candidate_k": candidate_k, "rrf_k": rrf_k}
        callbacks = counted("bm25", sparse), counted("dense", dense)
        fusion = HybridRetriever(*callbacks, **kwargs)
        reranked = HybridRetriever(*callbacks, scorer=scorer, **kwargs)
        first = queries[0]
        for backend in (fusion, reranked):
            backend.retrieve(first["question"], first["paper_id"], top_k)
        for position, question in enumerate(queries):
            outputs, timings = {}, {}
            # Alternate order to reduce a consistent first/second timing bias.
            methods = [("rrf", fusion), ("rrf_bge", reranked)]
            if position % 2:
                methods.reverse()
            for name, backend in methods:
                started = time.perf_counter()
                outputs[name] = backend.retrieve(
                    question["question"], question["paper_id"], top_k
                )
                timings[name] = (time.perf_counter() - started) * 1000
            before = [hit.passage.passage_id for hit in outputs["rrf"]]
            after = [hit.passage.passage_id for hit in outputs["rrf_bge"]]
            records.append(
                {
                    **question,
                    "candidate_k_per_source": candidate_k,
                    "candidate_counts": {
                        name: len(ids) for name, ids in source_ids.items()
                    },
                    "unique_candidates": len(set().union(*source_ids.values())),
                    "latency_ms": timings,
                    "same_top1": bool(before and after and before[0] == after[0]),
                    "top_k_overlap_fraction": len(set(before) & set(after))
                    / max(1, min(len(before), len(after))),
                    "results": {
                        name: [hit.model_dump() for hit in hits]
                        for name, hits in outputs.items()
                    },
                }
            )
            print(
                f"candidate_k={candidate_k}: {position + 1}/{len(queries)} queries",
                file=sys.stderr,
                flush=True,
            )
    return records


def summarize(records, candidate_ks):
    summaries = []
    for candidate_k in candidate_ks:
        group = [row for row in records if row["candidate_k_per_source"] == candidate_k]
        summary = {
            "candidate_k_per_source": candidate_k,
            "questions": len(group),
            "mean_unique_candidates": float(
                np.mean([row["unique_candidates"] for row in group])
            ),
            "top1_changed_count": sum(not row["same_top1"] for row in group),
            "mean_top_k_overlap_fraction": float(
                np.mean([row["top_k_overlap_fraction"] for row in group])
            ),
        }
        for method in ("rrf", "rrf_bge"):
            values = [row["latency_ms"][method] for row in group]
            summary[method] = {
                "p50_ms": float(np.percentile(values, 50)),
                "p95_ms": float(np.percentile(values, 95)),
            }
        summaries.append(summary)
    return summaries


def run_benchmark(args):
    if args.output.exists():
        raise FileExistsError(
            "Choose a new output path; benchmark outputs are not overwritten"
        )
    if (
        args.questions < 1
        or args.top_k < 1
        or args.rrf_k < 1
        or any(k < 1 for k in args.candidate_ks)
    ):
        raise ValueError("Counts and RRF constant must be positive")
    if len(set(args.candidate_ks)) != len(args.candidate_ks):
        raise ValueError("candidate-ks must not contain duplicates")
    import torch

    passages = load_passages(args.passages)
    queries = select_queries(
        args.qa,
        Counter(p.paper_id for p in passages),
        args.questions,
        args.min_passages,
    )
    sparse = BM25Retriever(passages)
    dense = DenseRetriever.load(
        args.dense_index_dir,
        model_name=DEFAULT_MODEL_NAME,
        revision=args.revision,
        device=args.device,
        cache_folder=args.cache_folder,
        local_files_only=args.local_files_only,
    )
    _check_same_passages(args.dense_index_dir, passages)
    scorer = BGEReranker(
        revision=args.reranker_revision,
        device=args.device,
        cache_folder=str(args.cache_folder),
        local_files_only=args.local_files_only,
    )
    records = compare_queries(
        sparse.retrieve,
        dense.retrieve,
        scorer,
        queries,
        args.candidate_ks,
        args.top_k,
        args.rrf_k,
    )
    root = Path(__file__).resolve().parents[1]
    source_paths = [
        "scripts/benchmark_p2.py",
        "scripts/demo_hybrid.py",
        "scripts/build_indexes.py",
        "scripts/demo_p1.py",
    ]
    source_paths += [
        str(p.relative_to(root)) for p in sorted((root / "src/retrieval").glob("*.py"))
    ]
    output = {
        "purpose": "training-only integration and latency pilot; no relevance labels used",
        "limitations": "Small deterministic sample; ranking changes do not establish quality gains. p95 is descriptive for this pilot only.",
        "selection": "train only; sort paper_id then question_id; one question per paper; minimum passage count",
        "minimum_passages_per_paper": args.min_passages,
        "query_inputs": queries,
        "corpus_sha256": sha256(args.passages),
        "qa_export_sha256": sha256(args.qa),
        "index_metadata_sha256": sha256(args.dense_index_dir / "metadata.json"),
        "code_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "source_sha256": {path: sha256(root / path) for path in source_paths},
        "versions": {
            name: importlib.metadata.version(name)
            for name in (
                "numpy",
                "torch",
                "faiss-cpu",
                "transformers",
                "sentence-transformers",
                "pydantic",
                "rank-bm25",
            )
        },
        "platform": platform.platform(),
        "python": platform.python_version(),
        "torch_threads": torch.get_num_threads(),
        "device": args.device,
        "dense_model": DEFAULT_MODEL_NAME,
        "dense_revision": args.revision,
        "reranker_model": "BAAI/bge-reranker-base",
        "reranker_revision": args.reranker_revision,
        "top_k": args.top_k,
        "rrf_k": args.rrf_k,
        "timing_policy": "One complete retrieve call per method/question/configuration after one warm-up per method/configuration; alternating method order; loading/indexing excluded; BGE tokenization/scoring included.",
        "summary": summarize(records, args.candidate_ks),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as destination:
        json.dump(output, destination, indent=2, allow_nan=False)
        destination.write("\n")
    return output["summary"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--qa", type=Path, required=True)
    parser.add_argument("--dense-index-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--questions", type=int, default=6)
    parser.add_argument("--min-passages", type=int, default=20)
    parser.add_argument("--candidate-ks", type=int, nargs="+", default=[10, 20])
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--device", default="cpu")
    parser.add_argument(
        "--cache-folder", type=Path, default=Path(".cache/huggingface/hub")
    )
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--revision", type=revision_sha, default=PINNED_REVISION)
    parser.add_argument(
        "--reranker-revision", type=revision_sha, default=RERANKER_REVISION
    )
    args = parser.parse_args()
    try:
        print(json.dumps(run_benchmark(args), indent=2))
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
