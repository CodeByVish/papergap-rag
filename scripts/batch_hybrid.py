"""Export hybrid retrieval for a fixed questions JSONL, loading models once."""

import argparse
import hashlib
import json
import os
import platform
import subprocess
import time
from importlib.metadata import distributions
from pathlib import Path

from scripts.build_indexes import PINNED_REVISION, load_passages, revision_sha
from scripts.demo_hybrid import RERANKER_REVISION
from scripts.demo_p1 import _check_same_passages
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker


def read_questions(path):
    rows = []
    seen = set()
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), 1
    ):
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"Line {line_number}: question must be an object")  # noqa: TRY004
        for key in ("question_id", "question", "paper_id"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f"Line {line_number}: nonempty {key} required")
        if row["question_id"] in seen:
            raise ValueError(f"Duplicate question_id: {row['question_id']}")
        seen.add(row["question_id"])
        rows.append({key: row[key] for key in ("question_id", "question", "paper_id")})
    if not rows:
        raise ValueError("Questions file is empty")
    return rows


def run_batch(
    *,
    questions,
    passages,
    dense_index_dir,
    output_dir,
    bge=False,
    top_k=5,
    candidate_k=20,
    rrf_k=60,
    device="cpu",
    cache_folder=None,
    local_files_only=False,
    revision=PINNED_REVISION,
    reranker_revision=RERANKER_REVISION,
):
    rows = read_questions(questions)
    for value in (top_k, candidate_k, rrf_k):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError("top_k, candidate_k and rrf_k must be positive integers")
    if local_files_only:
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
    output_dir.mkdir(parents=True, exist_ok=False)
    manifest = {
        "status": "running",
        "question_count": len(rows),
        "config": {
            "top_k": top_k,
            "candidate_k_per_source": candidate_k,
            "rrf_k": rrf_k,
            "device": device,
            "dense_model": DEFAULT_MODEL_NAME,
            "dense_revision": revision,
            "reranker_model": "BAAI/bge-reranker-base" if bge else None,
            "reranker_revision": reranker_revision if bge else None,
            "batch_size": 8,
            "max_length": 512,
            "local_files_only": local_files_only,
        },
        "input_sha256": {
            str(p): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (questions, passages, dense_index_dir / "metadata.json")
        },
        "source_sha256": {
            str(p): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [Path(__file__), *Path("src/retrieval").glob("*.py")]
        },
        "dependencies": {d.metadata["Name"]: d.version for d in distributions()},
        "threads": {
            key: os.environ.get(key) for key in ("OMP_NUM_THREADS", "MKL_NUM_THREADS")
        },
        "python": platform.python_version(),
        "platform": platform.platform(),
        "timing_policy": "One call per question; no warm-up; model/index loading excluded except lazy first-use loading.",
    }
    try:
        manifest["code_commit"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
        manifest["working_tree"] = subprocess.check_output(
            ["git", "status", "--short"], text=True
        )
        corpus = load_passages(passages)
        sparse = BM25Retriever(corpus)
        dense = DenseRetriever.load(
            dense_index_dir,
            model_name=DEFAULT_MODEL_NAME,
            revision=revision,
            device=device,
            cache_folder=cache_folder,
            local_files_only=local_files_only,
        )
        _check_same_passages(dense_index_dir, corpus)
        scorer = (
            BGEReranker(
                revision=reranker_revision,
                device=device,
                cache_folder=str(cache_folder) if cache_folder else None,
                local_files_only=local_files_only,
            )
            if bge
            else None
        )
        backend = HybridRetriever(
            sparse.retrieve,
            dense.retrieve,
            scorer=scorer,
            candidate_k=candidate_k,
            rrf_k=rrf_k,
        )
        empty = 0
        with (
            (output_dir / "retrieval.jsonl").open("x", encoding="utf-8") as out,
            (output_dir / "latency.jsonl").open("x", encoding="utf-8") as timing,
        ):
            for row in rows:
                start = time.perf_counter()
                hits = backend.retrieve(row["question"], row["paper_id"], top_k=top_k)
                elapsed = (time.perf_counter() - start) * 1000
                empty += not hits
                out.write(
                    json.dumps(
                        dict(
                            row,
                            retrieval_round=1,
                            retrieved_passages=[
                                h.model_dump(mode="json") for h in hits
                            ],
                        )
                    )
                    + "\n"
                )
                timing.write(
                    json.dumps(
                        {"question_id": row["question_id"], "elapsed_ms": elapsed}
                    )
                    + "\n"
                )
        manifest.update(status="complete", empty_results=empty)
        manifest["output_sha256"] = hashlib.sha256(
            (output_dir / "retrieval.jsonl").read_bytes()
        ).hexdigest()
    except BaseException as error:
        manifest.update(status="failed", error=str(error))
        raise
    finally:
        (output_dir / "run_manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("questions", "passages", "dense-index-dir", "output-dir"):
        parser.add_argument("--" + name, type=Path, required=True)
    for name, default in (("top-k", 5), ("candidate-k", 20), ("rrf-k", 60)):
        parser.add_argument("--" + name, type=int, default=default)
    parser.add_argument("--bge", action="store_true")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--cache-folder", type=Path)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--revision", type=revision_sha, default=PINNED_REVISION)
    parser.add_argument(
        "--reranker-revision", type=revision_sha, default=RERANKER_REVISION
    )
    args = parser.parse_args()
    try:
        print(json.dumps(run_batch(**vars(args)), indent=2))
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
