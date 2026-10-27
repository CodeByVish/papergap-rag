"""Run four retrieval systems, score supplied labels, or export blinded pools."""

import argparse
import hashlib
import json
import os
import platform
import subprocess
import time
from importlib.metadata import distributions
from itertools import product
from pathlib import Path

import numpy as np

from scripts.build_indexes import PINNED_REVISION, load_passages
from scripts.demo_hybrid import RERANKER_REVISION
from scripts.demo_p1 import _check_same_passages
from src.evaluation.pooling import pool_candidates
from src.evaluation.retrieval import evaluate_rankings, question_inputs, read_jsonl
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker

METHODS = ("bm25", "dense", "rrf", "rrf_bge")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    with path.open("x", encoding="utf-8") as out:
        json.dump(value, out, indent=2, allow_nan=False)
        out.write("\n")


def write_jsonl(path, rows):
    with path.open("x", encoding="utf-8") as out:
        for row in rows:
            out.write(json.dumps(row, allow_nan=False) + "\n")


def validate_scope(
    questions, qa_path, role, freeze_path, corpus_path, questions_path, config
):
    requested = {q["question_id"]: q for q in questions}
    matched = set()
    for row in read_jsonl(qa_path):
        qid = row.get("question_id")
        if qid not in requested:
            continue
        allowed = {"train", "validation"} if role == "development" else {"test"}
        if row.get("source_split") not in allowed:
            raise ValueError(
                "Question source split is incompatible with requested role"
            )
        if (
            any(row.get(k) != requested[qid][k] for k in ("paper_id", "question"))
            or qid in matched
        ):
            raise ValueError(
                "Question identity differs from QA source or is duplicated"
            )
        matched.add(qid)
    if matched != set(requested):
        raise ValueError("Questions missing from QA source")
    if role == "held_out":
        if freeze_path is None:
            raise ValueError(
                "Held-out execution requires a team-supplied freeze manifest"
            )
        freeze = json.loads(freeze_path.read_text())
        if (
            freeze.get("status") != "frozen"
            or not freeze.get("approved_by")
            or freeze.get("questions_sha256") != sha(questions_path)
            or freeze.get("corpus_sha256") != sha(corpus_path)
            or freeze.get("configuration") != config
        ):
            raise ValueError(
                "Freeze manifest approval, hashes or configuration mismatch"
            )


def run(args):
    if args.output_dir.exists():
        raise FileExistsError("Choose a new output directory")
    for value in [args.top_k, *args.candidate_ks, *args.rrf_ks]:
        if value < 1:
            raise ValueError("All K values must be positive")
    if len(set(args.candidate_ks)) != len(args.candidate_ks) or len(
        set(args.rrf_ks)
    ) != len(args.rrf_ks):
        raise ValueError("Parameter grids must not contain duplicates")
    questions = question_inputs(args.questions)
    config = {
        "candidate_ks": args.candidate_ks,
        "rrf_ks": args.rrf_ks,
        "top_k": args.top_k,
        "dense_revision": PINNED_REVISION,
        "reranker_revision": RERANKER_REVISION,
        "device": "cpu",
        "batch_size": 8,
        "max_length": 512,
    }
    validate_scope(
        questions,
        args.qa,
        args.role,
        args.freeze_manifest,
        args.passages,
        args.questions,
        config,
    )
    if args.local_files_only:
        os.environ["HF_HUB_OFFLINE"] = os.environ["TRANSFORMERS_OFFLINE"] = "1"
    args.output_dir.mkdir(parents=True)
    manifest = {
        "status": "running",
        "role": args.role,
        "configuration": config,
        "corpus_sha256": sha(args.passages),
        "questions_sha256": sha(args.questions),
        "qa_sha256": sha(args.qa),
        "index_metadata_sha256": sha(args.dense_index_dir / "metadata.json"),
        "freeze_sha256": sha(args.freeze_manifest) if args.freeze_manifest else None,
        "code_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "source_sha256": {
            str(p): sha(p)
            for p in [
                Path(__file__),
                *Path("src/retrieval").glob("*.py"),
                *Path("src/evaluation").glob("*.py"),
            ]
        },
        "versions": {d.metadata["Name"]: d.version for d in distributions()},
        "platform": platform.platform(),
        "threads": {
            k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS")
        },
        "timing_policy": "One warm-up per method/configuration; alternating measured order per question; no persistent score cache. Load/build excluded.",
        "quality_evaluation_performed": False,
    }
    try:
        corpus = load_passages(args.passages)
        sparse = BM25Retriever(corpus)
        dense = DenseRetriever.load(
            args.dense_index_dir,
            revision=PINNED_REVISION,
            cache_folder=args.cache_folder,
            local_files_only=args.local_files_only,
        )
        _check_same_passages(args.dense_index_dir, corpus)
        scorer = BGEReranker(
            revision=RERANKER_REVISION,
            cache_folder=str(args.cache_folder),
            local_files_only=args.local_files_only,
        )
        write_jsonl(args.output_dir / "questions.jsonl", questions)
        for candidate_k, rrf_k in product(args.candidate_ks, args.rrf_ks):
            directory = args.output_dir / f"c{candidate_k}-r{rrf_k}"
            directory.mkdir()
            common = {"candidate_k": candidate_k, "rrf_k": rrf_k}
            methods = {
                "bm25": sparse.retrieve,
                "dense": dense.retrieve,
                "rrf": HybridRetriever(
                    sparse.retrieve, dense.retrieve, **common
                ).retrieve,
                "rrf_bge": HybridRetriever(
                    sparse.retrieve, dense.retrieve, scorer=scorer, **common
                ).retrieve,
            }
            first = questions[0]
            for retrieve in methods.values():
                retrieve(first["question"], first["paper_id"], args.top_k)
            outputs = {m: [] for m in METHODS}
            timings = []
            for i, q in enumerate(questions):
                order = list(METHODS) if i % 2 == 0 else list(reversed(METHODS))
                for method in order:
                    started = time.perf_counter()
                    hits = methods[method](q["question"], q["paper_id"], args.top_k)
                    elapsed = (time.perf_counter() - started) * 1000
                    outputs[method].append(
                        {
                            **q,
                            "retrieval_round": 1,
                            "retrieved_passages": [
                                h.model_dump(mode="json") for h in hits
                            ],
                        }
                    )
                    timings.append(
                        {
                            "question_id": q["question_id"],
                            "method": method,
                            "elapsed_ms": elapsed,
                        }
                    )
            for method, rows in outputs.items():
                write_jsonl(directory / f"{method}.jsonl", rows)
            write_jsonl(directory / "latency.jsonl", timings)
            write_json(
                directory / "latency_summary.json",
                {
                    m: {
                        "questions": len(questions),
                        "p50_ms": float(
                            np.percentile(
                                [r["elapsed_ms"] for r in timings if r["method"] == m],
                                50,
                            )
                        ),
                        "p95_ms": float(
                            np.percentile(
                                [r["elapsed_ms"] for r in timings if r["method"] == m],
                                95,
                            )
                        ),
                    }
                    for m in METHODS
                },
            )
        manifest["status"] = "complete"
        manifest["output_sha256"] = {
            str(p.relative_to(args.output_dir)): sha(p)
            for p in args.output_dir.rglob("*")
            if p.is_file()
        }
    except BaseException as error:
        manifest.update(status="failed", error=str(error))
        raise
    finally:
        write_json(args.output_dir / "run_manifest.json", manifest)


def load_run(args):
    root = args.run_dir.parent
    manifest = json.loads((root / "run_manifest.json").read_text())
    if (
        manifest["status"] != "complete"
        or sha(args.passages) != manifest["corpus_sha256"]
    ):
        raise ValueError("Run incomplete or corpus hash mismatch")
    for name, expected in manifest["output_sha256"].items():
        if sha(root / name) != expected:
            raise ValueError("Saved run output hash mismatch")
    questions = question_inputs(root / "questions.jsonl")
    rankings = {m: read_jsonl(args.run_dir / f"{m}.jsonl") for m in METHODS}
    catalog = {p.passage_id: p for p in load_passages(args.passages)}
    return manifest, questions, rankings, catalog


def score(args):
    manifest, questions, rankings, catalog = load_run(args)
    if any(k > manifest["configuration"]["top_k"] for k in args.ks):
        raise ValueError("Metric K exceeds saved retrieval depth")
    labels_manifest = json.loads(args.labels_manifest.read_text())
    if labels_manifest.get("annotation_coverage") not in {"partial", "complete"}:
        raise ValueError("Label annotation_coverage must be partial or complete")
    scope = labels_manifest.get("question_scope", {})
    expected = {q["question_id"] for q in questions}
    if (
        labels_manifest.get("labels_sha256") != sha(args.labels)
        or labels_manifest.get("corpus_sha256") != manifest["corpus_sha256"]
        or set(scope.get("question_ids", [])) != expected
        or scope.get("project_role") != manifest["role"]
        or not labels_manifest.get("source")
        or not labels_manifest.get("mapping")
    ):
        raise ValueError("Label provenance/hash/scope mismatch")
    labels = read_jsonl(args.labels)
    if (
        labels_manifest.get("annotation_coverage") == "complete"
        and {r["question_id"] for r in labels} != expected
    ):
        raise ValueError(
            "Label manifest claims complete coverage but records are missing"
        )
    report = evaluate_rankings(rankings, questions, labels, catalog, args.ks)
    report.update(
        labels_sha256=sha(args.labels),
        labels_manifest_sha256=sha(args.labels_manifest),
        run_manifest_sha256=sha(args.run_dir.parent / "run_manifest.json"),
        role=manifest["role"],
        configuration=manifest["configuration"],
        parameter_selection_allowed=manifest["role"] == "development",
    )
    write_json(args.output, report)


def pool(args):
    manifest, questions, rankings, catalog = load_run(args)
    evaluate_rankings(rankings, questions, [], catalog, [args.per_question])
    gold = {}
    if args.gold:
        for row in read_jsonl(args.gold):
            if row["question_id"] in gold:
                raise ValueError("Duplicate gold question")
            gold[row["question_id"]] = [
                catalog[pid] for pid in row["relevant_passage_ids"]
            ]
        if not set(gold) <= {q["question_id"] for q in questions}:
            raise ValueError("Unknown gold question")
    result = pool_candidates(
        rankings, questions, per_question=args.per_question, gold=gold
    )
    args.output_dir.mkdir(parents=True, exist_ok=False)
    write_jsonl(args.output_dir / "blinded.jsonl", result["blinded"])
    write_jsonl(
        args.output_dir / "provenance_DO_NOT_SEND_TO_ANNOTATORS.jsonl",
        result["provenance"],
    )
    write_json(
        args.output_dir / "pool_manifest.json",
        {
            "role": manifest["role"],
            "status": "shortfall" if result["shortfalls"] else "complete",
            "question_count": len(questions),
            "unique_pairs": len(result["blinded"]),
            "shortfalls": result["shortfalls"],
            "per_question": args.per_question,
            "source_run_manifest_sha256": sha(
                args.run_dir.parent / "run_manifest.json"
            ),
            "gold_sha256": sha(args.gold) if args.gold else None,
            "blinded_sha256": sha(args.output_dir / "blinded.jsonl"),
            "protocol": "v0-proposed: explicit gold first, then rank round-robin bm25/dense/rrf/rrf_bge; display ordered by content hash; no duplicate padding",
        },
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inference = commands.add_parser("run")
    for key in ("questions", "qa", "passages", "dense-index-dir", "output-dir"):
        inference.add_argument("--" + key, type=Path, required=True)
    inference.add_argument(
        "--role", choices=["development", "held_out"], default="development"
    )
    inference.add_argument("--freeze-manifest", type=Path)
    inference.add_argument("--candidate-ks", nargs="+", type=int, default=[20])
    inference.add_argument("--rrf-ks", nargs="+", type=int, default=[60])
    inference.add_argument("--top-k", type=int, default=10)
    inference.add_argument(
        "--cache-folder", type=Path, default=Path(".cache/huggingface/hub")
    )
    inference.add_argument("--local-files-only", action="store_true")
    inference.set_defaults(action=run)
    for command, action in [("score", score), ("pool", pool)]:
        sub = commands.add_parser(command)
        sub.add_argument("--run-dir", type=Path, required=True)
        sub.add_argument("--passages", type=Path, required=True)
        sub.set_defaults(action=action)
        if command == "score":
            sub.add_argument("--labels", type=Path, required=True)
            sub.add_argument("--labels-manifest", type=Path, required=True)
            sub.add_argument("--ks", nargs="+", type=int, default=[1, 3, 5, 10])
            sub.add_argument("--output", type=Path, required=True)
        else:
            sub.add_argument("--output-dir", type=Path, required=True)
            sub.add_argument("--per-question", type=int, default=10)
            sub.add_argument("--gold", type=Path)
    args = parser.parse_args()
    try:
        args.action(args)
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
