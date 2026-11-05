"""Verified P3 inputs and reproducible, train-only P1 retrieval experiments.

This adapter consumes files; it never imports or changes the P3 implementation.
QA annotations are discarded at the input boundary, without inspecting labels.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from importlib.metadata import version
from itertools import pairwise
from pathlib import Path

import numpy as np

from scripts.build_indexes import PINNED_REVISION, load_passages
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever, Encoder
from src.retrieval.schemas import Passage, RetrievalHit

SPLIT_POLICY = "qasper-official-paper-disjoint-v0-proposed"
SPLIT_ROLES = {"train": "development", "validation": "validation", "test": "held_out"}


def file_sha256(path: Path) -> str:
    with Path(path).open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as error:
        raise ValueError(f"{path}: cannot read JSON ({error})") from error
    _require(isinstance(value, dict), f"{path}: expected a JSON object")
    return value


def _rows(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except ValueError as error:
                raise ValueError(f"{path}:{line_number}: invalid JSON") from error
            _require(isinstance(row, dict), f"{path}:{line_number}: expected an object")
            yield row


def _clean_string(value, label: str) -> str:
    _require(isinstance(value, str) and bool(value.strip()), f"{label}: empty string")
    _require(value == value.strip(), f"{label}: leading or trailing whitespace")
    return value


def _check_file(path: Path, entry: dict) -> str:
    _require(path.name == entry["file"], f"{path}: filename differs from manifest")
    observed = file_sha256(path)
    _require(observed == entry["sha256"], f"{path}: SHA-256 differs from manifest")
    return observed


@dataclass(frozen=True)
class DevelopmentQuestion:
    question_id: str
    paper_id: str
    query: str


@dataclass
class ExperimentInputs:
    passages: list[Passage]
    questions: list[DevelopmentQuestion]
    provenance: dict


def load_experiment_inputs(
    passages_path: str | Path,
    corpus_manifest_path: str | Path,
    qa_path: str | Path,
    export_manifest_path: str | Path,
) -> ExperimentInputs:
    """Check provenance and project only train queries, never answers/evidence.

    The paper-only export is resolved beside its manifest to check split links.
    Other QA splits are counted mechanically but their text is never selected.
    """
    paths = [
        Path(p)
        for p in (passages_path, corpus_manifest_path, qa_path, export_manifest_path)
    ]
    passages_path, corpus_manifest_path, qa_path, export_manifest_path = paths
    try:
        corpus = _object(corpus_manifest_path)
        export = _object(export_manifest_path)
        _require(
            type(corpus["manifest_schema_version"]) is int
            and corpus["manifest_schema_version"] == 1,
            "unsupported corpus manifest",
        )
        _require(
            type(export["manifest_schema_version"]) is int
            and export["manifest_schema_version"] == 1,
            "unsupported export manifest",
        )
        chunking = corpus["chunking"]
        _require(isinstance(chunking, dict), "chunking must be an object")
        _require(
            chunking["source_kinds"] == ["full_text"], "unsupported chunk source kinds"
        )
        for key in ("normalization_version", "chunking_version"):
            _clean_string(chunking[key], f"chunking {key}")
        size, overlap = chunking["chunk_size_words"], chunking["chunk_overlap_words"]
        _require(
            type(size) is int
            and size > 0
            and type(overlap) is int
            and 0 <= overlap < size,
            "invalid chunking size or overlap",
        )
        _require(
            export["artifact"] == "qasper_papers_and_qa", "invalid export artifact"
        )
        _require(
            corpus["artifact"] == "development_corpus"
            and corpus["scope"] == corpus["purpose"] == "development"
            and corpus["output"]["scope"]
            == corpus["output"]["purpose"]
            == "development",
            "only the complete development corpus is supported (train + validation)",
        )
        source = corpus["source"]
        _require(
            source["split_policy_version"]
            == export["split_policy_version"]
            == SPLIT_POLICY,
            "unsupported split policy; review the development convention first",
        )
        for key in ("dataset_id", "resolved_revision", "local_parser_version"):
            _require(source[key] == export["source"][key], f"source {key} differs")
        _require(source["dataset_id"] == "allenai/qasper", "expected allenai/qasper")
        _require(
            type(source["local_parser_version"]) is int
            and source["local_parser_version"] > 0,
            "invalid source parser version",
        )
        _require(
            bool(re.fullmatch(r"[0-9a-f]{40}", source["resolved_revision"])),
            "source revision must be an immutable SHA",
        )
        _require(
            source["source_splits"] == export["source"]["split_files"],
            "source split provenance differs",
        )
        for entries in (
            source["source_splits"],
            source["split_counts"],
            export["split_counts"],
        ):
            _require(
                isinstance(entries, dict) and set(entries) == set(SPLIT_ROLES),
                "manifest must describe exactly train, validation, and test",
            )
        for split, entry in source["source_splits"].items():
            _require(
                type(entry["rows"]) is int
                and entry["rows"] >= 0
                and bool(re.fullmatch(r"[0-9a-f]{64}", entry["sha256"])),
                f"invalid source split fingerprint for {split}",
            )
        papers_entry = export["outputs"]["papers"]
        _require(
            Path(papers_entry["file"]).name == papers_entry["file"]
            and papers_entry["file"] not in ("", ".", ".."),
            "papers filename must be a basename",
        )
        papers_path = export_manifest_path.parent / papers_entry["file"]
        _require(
            source["export_papers_file"] == papers_entry["file"]
            and source["export_papers_sha256"] == papers_entry["sha256"],
            "corpus was built from a different paper export",
        )
        fingerprints = {
            "passages": _check_file(passages_path, corpus["output"]),
            "papers": _check_file(papers_path, papers_entry),
            "qa": _check_file(qa_path, export["outputs"]["qa"]),
            "corpus_manifest": file_sha256(corpus_manifest_path),
            "export_manifest": file_sha256(export_manifest_path),
        }
        paper_splits = {}
        paper_counts = Counter()
        for row in _rows(papers_path):
            paper_id = _clean_string(row["id"], "paper id")
            split = row["source_split"]
            _require(split in SPLIT_ROLES, "invalid paper source_split")
            _require(paper_id not in paper_splits, "duplicate or cross-split paper id")
            paper_splits[paper_id] = split
            paper_counts[split] += 1
        _require(len(paper_splits) == papers_entry["rows"], "paper count differs")

        passages = load_passages(passages_path)
        passage_counts = Counter()
        by_id = {}
        for passage in passages:
            _clean_string(passage.passage_id, "passage id")
            _clean_string(passage.paper_id, "passage paper id")
            _require(bool(passage.text.strip()), "passage text is empty")
            split = paper_splits.get(passage.paper_id)
            _require(
                split in ("train", "validation"),
                "passage references unknown or held-out paper",
            )
            passage_counts[split] += 1
            by_id[passage.passage_id] = passage
        for passage in passages:
            for field, reverse in (
                ("previous_passage_id", "next_passage_id"),
                ("next_passage_id", "previous_passage_id"),
            ):
                neighbor_id = getattr(passage, field)
                if neighbor_id is None:
                    continue
                neighbor = by_id.get(neighbor_id)
                _require(
                    neighbor is not None
                    and neighbor.paper_id == passage.paper_id
                    and getattr(neighbor, reverse) == passage.passage_id,
                    "invalid or cross-paper Passage neighbor mapping",
                )
        output = corpus["output"]
        _require(
            len(passages) == output["passage_count"] == output["unique_passage_count"],
            "passage count differs from manifest",
        )
        _require(
            len({p.paper_id for p in passages}) == output["indexed_paper_count"],
            "indexed paper count differs from manifest",
        )
        _require(
            output["source_paper_count"]
            == paper_counts["train"] + paper_counts["validation"],
            "source paper count differs from manifest",
        )
        question_counts = Counter()
        questions = []
        seen_questions = set()
        for row in _rows(qa_path):
            question_id = _clean_string(row["question_id"], "question id")
            paper_id = _clean_string(row["paper_id"], "question paper id")
            split = row["source_split"]
            _require(
                split in SPLIT_ROLES and paper_splits.get(paper_id) == split,
                "QA source_split differs from linked paper",
            )
            _require(question_id not in seen_questions, "duplicate question id")
            seen_questions.add(question_id)
            question_counts[split] += 1
            if split == "train":
                query = row["question"]
                _require(
                    isinstance(query, str) and bool(query.strip()), "empty train query"
                )
                questions.append(DevelopmentQuestion(question_id, paper_id, query))
            # Never access question/answers/evidence for non-train records.
        _require(
            len(seen_questions) == export["outputs"]["qa"]["rows"],
            "QA row count differs",
        )
        for split, role in SPLIT_ROLES.items():
            expected = export["split_counts"][split]
            scope_entry = source["split_counts"][split]
            _require(
                paper_counts[split]
                == expected["papers"]
                == scope_entry["source_paper_count"]
                == source["source_splits"][split]["rows"],
                f"{split} paper count differs",
            )
            _require(
                question_counts[split] == expected["questions"],
                f"{split} question count differs",
            )
            _require(
                scope_entry["included_in_scope"] is (split != "test")
                and scope_entry["project_role"] == role,
                f"{split} corpus scope differs",
            )
            _require(
                passage_counts[split] == scope_entry["passage_count"],
                f"{split} passage count differs",
            )
        _require(bool(questions), "no train development questions found")
        questions.sort(key=lambda question: question.question_id)
    except (KeyError, TypeError) as error:
        raise ValueError(f"invalid P3 input or manifest structure: {error}") from error
    return ExperimentInputs(
        passages,
        questions,
        {
            "sha256": fingerprints,
            "paths": {
                "passages": str(passages_path.resolve()),
                "corpus_manifest": str(corpus_manifest_path.resolve()),
                "qa": str(qa_path.resolve()),
                "export_manifest": str(export_manifest_path.resolve()),
                "papers": str(papers_path.resolve()),
            },
            "dataset": export["source"],
            "chunking": chunking,
            "scope": "development",
            "split_policy_version": SPLIT_POLICY,
            "question_split": "train",
            "project_role": "development",
            "split_policy_status": "proposed; train-only development convention",
            "corpus_counts": output,
            "available_train_questions": len(questions),
            "question_order": "question_id ascending",
            "annotations_used": False,
        },
    )


def _same_passages(saved: list[dict], passages: list[Passage], label: str) -> None:
    parsed = [Passage.model_validate(value) for value in saved]
    _require(
        len(parsed) == len(passages)
        and {p.passage_id: p for p in parsed} == {p.passage_id: p for p in passages},
        f"{label} index Passage mapping differs from complete input corpus",
    )


def _check_hits(
    hits: list[RetrievalHit],
    question: DevelopmentQuestion,
    top_k: int,
    by_id: dict[str, Passage],
    expected_count: int,
) -> None:
    _require(
        isinstance(hits, list) and len(hits) == min(top_k, expected_count),
        "retriever returned an unexpected number of passages",
    )
    seen = set()
    previous_score = math.inf
    for rank, hit in enumerate(hits, 1):
        _require(
            isinstance(hit, RetrievalHit) and hit.rank == rank,
            "retriever returned invalid ranks or result types",
        )
        passage = hit.passage
        _require(
            passage.paper_id == question.paper_id
            and by_id.get(passage.passage_id) == passage
            and passage.passage_id not in seen,
            "retriever returned an invalid Passage mapping",
        )
        _require(
            math.isfinite(hit.score) and hit.score <= previous_score,
            "invalid retrieval scores",
        )
        previous_score = hit.score
        seen.add(passage.passage_id)


def _write_json(path: Path, value: dict) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def run_experiment(
    *,
    passages_path: str | Path,
    corpus_manifest_path: str | Path,
    qa_path: str | Path,
    export_manifest_path: str | Path,
    p3_commit: str,
    dense_index_dir: str | Path,
    output_dir: str | Path,
    top_k: int = 5,
    limit: int | None = None,
    bm25_index_dir: str | Path | None = None,
    p1_commit: str | None = None,
    revision: str = PINNED_REVISION,
    device: str = "cpu",
    cache_folder: str | Path | None = None,
    local_files_only: bool = False,
    encoder: Encoder | None = None,
) -> dict:
    """Run both backends on verified train queries with retrieve-only timings."""
    _require(type(top_k) is int and top_k > 0, "top_k must be a positive integer")
    _require(
        limit is None or (type(limit) is int and limit > 0), "limit must be positive"
    )
    _require(
        bool(re.fullmatch(r"[0-9a-f]{40}", p3_commit)), "p3_commit must be a full SHA"
    )
    output_dir = Path(output_dir)
    _require(
        not output_dir.exists()
        or (output_dir.is_dir() and not any(output_dir.iterdir())),
        "output directory must be new or empty",
    )
    inputs = load_experiment_inputs(
        passages_path, corpus_manifest_path, qa_path, export_manifest_path
    )
    dense_index_dir = Path(dense_index_dir)
    dense = DenseRetriever.load(
        dense_index_dir,
        encoder=encoder,
        model_name=DEFAULT_MODEL_NAME if encoder is None else encoder.model_name,
        revision=revision if encoder is None else encoder.revision,
        device=device,
        cache_folder=cache_folder,
        local_files_only=local_files_only,
    )
    dense_metadata = _object(dense_index_dir / "metadata.json")
    _same_passages(
        [p for paper in dense_metadata["papers"] for p in paper["passages"]],
        inputs.passages,
        "Dense",
    )
    questions = inputs.questions[:limit]
    by_id = {p.passage_id: p for p in inputs.passages}
    paper_counts = Counter(p.paper_id for p in inputs.passages)
    if p1_commit is None:
        p1_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=Path(__file__).resolve().parents[2],
            text=True,
        ).strip()
    _require(
        bool(re.fullmatch(r"[0-9a-f]{40}", p1_commit)), "p1_commit must be a full SHA"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    if bm25_index_dir is None:
        bm25_index_dir = output_dir / "bm25-index"
    bm25_index_dir = Path(bm25_index_dir)
    if not bm25_index_dir.exists() or (
        bm25_index_dir.is_dir() and not any(bm25_index_dir.iterdir())
    ):
        BM25Retriever(inputs.passages).save(bm25_index_dir)
    bm25 = BM25Retriever.load(bm25_index_dir)
    bm25_metadata = _object(bm25_index_dir / "metadata.json")
    _same_passages(
        [p for paper in bm25_metadata["papers"] for p in paper["passages"]],
        inputs.passages,
        "BM25",
    )
    repository = Path(__file__).resolve().parents[2]
    dirty = bool(
        subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=repository, text=True
        ).strip()
    )
    source_files = [
        "scripts/run_p1_experiment.py",
        "scripts/build_indexes.py",
        "src/retrieval/experiment.py",
        "src/retrieval/bm25_retriever.py",
        "src/retrieval/dense_retriever.py",
        "src/retrieval/schemas.py",
    ]
    import torch

    config = {
        "format_version": 1,
        "status": "running",
        "p1_commit": p1_commit,
        "p1_dirty": dirty,
        "p1_source_sha256": {
            name: file_sha256(repository / name) for name in source_files
        },
        "p3_commit": p3_commit,
        "inputs": inputs.provenance,
        "top_k": top_k,
        "filters": {"paper_id": "question.paper_id", "section": None},
        "limit": limit,
        "question_count": len(questions),
        "methods": ["bm25", "dense"],
        "dense_index_dir": str(dense_index_dir.resolve()),
        "bm25_index_dir": str(bm25_index_dir.resolve()),
        "dense_metadata_sha256": file_sha256(dense_index_dir / "metadata.json"),
        "bm25_metadata_sha256": file_sha256(bm25_index_dir / "metadata.json"),
        "dense": {
            key: dense_metadata[key]
            for key in (
                "model_name",
                "revision",
                "encoder_kind",
                "query_instruction",
                "embedding_dimension",
                "normalization",
                "similarity_metric",
                "index_type",
            )
        },
        "environment": {
            "python": sys.executable,
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "processor": platform.processor(),
            "logical_cpu_count": os.cpu_count(),
            "device": device,
            "torch_threads": torch.get_num_threads(),
            "torch_interop_threads": torch.get_num_interop_threads(),
            "packages": {
                name: version(name)
                for name in (
                    "numpy",
                    "faiss-cpu",
                    "sentence-transformers",
                    "transformers",
                    "huggingface-hub",
                    "rank-bm25",
                    "pydantic",
                    "torch",
                )
            },
        },
        "timing": {
            "clock": "time.perf_counter",
            "unit": "ms",
            "scope": "retrieve only; Dense includes query encoding",
            "excluded": [
                "index construction",
                "index loading",
                "model loading",
                "warmup",
            ],
            "warmup_queries_per_method": 1,
            "measured_calls_per_question_per_method": 1,
            "population": "all selected train queries, including zero-hit queries",
            "interpretation": "initial latency observations; not a formal benchmark",
        },
        "quality_evaluation": {
            "performed": False,
            "reason": "No gold passage-ID mapping or P6 metric implementation supplied",
        },
        "quality_metrics": None,
        "outputs": {"results": "results.jsonl", "queries": "queries.jsonl"},
    }
    _write_json(output_dir / "run.json", config)
    # Warm up a question from an indexed paper, even when the first query has no passages.
    warmup = next((q for q in questions if q.paper_id in paper_counts), None)
    config["timing"]["warmup_queries_per_method"] = int(warmup is not None)
    methods = {"bm25": bm25, "dense": dense}
    if warmup is not None:
        for retriever in methods.values():
            retriever.retrieve(warmup.query, warmup.paper_id, top_k)
    result_counts = Counter()
    missing_questions = 0
    latencies = {method: [] for method in methods}
    with (
        (output_dir / "results.jsonl").open("w", encoding="utf-8") as result_file,
        (output_dir / "queries.jsonl").open("w", encoding="utf-8") as query_file,
    ):
        for number, question in enumerate(questions, 1):
            expected_count = paper_counts[question.paper_id]
            missing_questions += int(expected_count == 0)
            for method, retriever in methods.items():
                started = time.perf_counter()
                hits = retriever.retrieve(question.query, question.paper_id, top_k)
                elapsed_ms = (time.perf_counter() - started) * 1000
                _check_hits(hits, question, top_k, by_id, expected_count)
                latencies[method].append(elapsed_ms)
                common = {
                    "question_id": question.question_id,
                    "paper_id": question.paper_id,
                    "query": question.query,
                    "method": method,
                    "config": "run.json",
                }
                query_file.write(
                    json.dumps(
                        {
                            **common,
                            "hit_count": len(hits),
                            "status": "ok" if hits else "paper_without_passages",
                            "latency_ms": elapsed_ms,
                        },
                        ensure_ascii=False,
                        allow_nan=False,
                    )
                    + "\n"
                )
                for hit in hits:
                    result_file.write(
                        json.dumps(
                            {
                                **common,
                                "rank": hit.rank,
                                "passage_id": hit.passage.passage_id,
                                "score": hit.score,
                            },
                            ensure_ascii=False,
                            allow_nan=False,
                        )
                        + "\n"
                    )
                result_counts[method] += len(hits)
            if number % 100 == 0:
                print(
                    f"Retrieved {number}/{len(questions)} train questions",
                    file=sys.stderr,
                    flush=True,
                )
    config["status"] = "complete"
    config["summary"] = {
        "result_rows": dict(result_counts),
        "query_rows": len(questions) * len(methods),
        "questions_without_passages": missing_questions,
        "latency_mean_ms": {
            name: sum(values) / len(values) for name, values in latencies.items()
        },
        "latency_p50_ms": {
            name: float(np.percentile(values, 50)) for name, values in latencies.items()
        },
        "latency_p95_ms": {
            name: float(np.percentile(values, 95)) for name, values in latencies.items()
        },
    }
    config["output_sha256"] = {
        name: file_sha256(output_dir / name)
        for name in ("results.jsonl", "queries.jsonl")
    }
    _write_json(output_dir / "run.json", config)
    return config


# This exact exporter called retrieve(query, paper_id, top_k), without section.
# Older artifacts omitted filters; never infer a different exporter's policy.
_PAPER_ONLY_EXPORTER = (
    "ab31e5b3004ede59e845209d6ec0c2952f84f0e27b6a670edeaae2fe342ad626"
)


def audit_saved_run(run_dir: Path, inputs: ExperimentInputs) -> tuple[dict, dict, list]:
    """Validate saved rankings against the original train query/corpus snapshots.

    No retriever, index or encoder is constructed. Invalid identities, hashes,
    ranks or scores fail closed; count/status discrepancies remain in the report
    and prevent subsequent scoring. Returns audit, rankings and per-query counts.
    """
    run_dir = Path(run_dir)
    config = _object(run_dir / "run.json")
    try:
        _require(
            type(config["format_version"]) is int and config["format_version"] == 1,
            "unsupported run format",
        )
        _require(isinstance(config["status"], str), "invalid run status")
        _require(
            config["inputs"]["sha256"] == inputs.provenance["sha256"],
            "run inputs differ from verified corpus/QA snapshots",
        )
        for field in ("question_split", "project_role", "split_policy_version"):
            _require(
                config["inputs"][field] == inputs.provenance[field],
                f"run {field} differs from verified development scope",
            )
        filters = config.get("filters")
        filter_evidence = "explicit run metadata"
        if filters is None:
            _require(
                config["p1_source_sha256"]["src/retrieval/experiment.py"]
                == _PAPER_ONLY_EXPORTER,
                "legacy run has unknown filtering policy; verify its exporter",
            )
            filters = {"paper_id": "question.paper_id", "section": None}
            filter_evidence = (
                "verified legacy exporter SHA-256 (three-argument retrieve)"
            )
        _require(
            isinstance(filters, dict)
            and set(filters) == {"paper_id", "section"}
            and filters["paper_id"] == "question.paper_id",
            "unsupported filtering policy",
        )
        section = filters["section"]
        if section is not None:
            _clean_string(section, "section filter")
        top_k, limit = config["top_k"], config["limit"]
        _require(type(top_k) is int and top_k > 0, "invalid run top_k")
        _require(
            limit is None or (type(limit) is int and limit > 0), "invalid run limit"
        )
        questions = inputs.questions[:limit]
        _require(
            config["question_count"] == len(questions), "run question count differs"
        )
        methods = config["methods"]
        _require(methods == ["bm25", "dense"], "unsupported run methods")
        for key, filename in (
            ("results", "results.jsonl"),
            ("queries", "queries.jsonl"),
        ):
            _require(config["outputs"][key] == filename, "unsupported output filename")
            _require(
                file_sha256(run_dir / filename) == config["output_sha256"][filename],
                f"{filename}: SHA-256 differs from run",
            )
    except (KeyError, TypeError) as error:
        raise ValueError(f"invalid run metadata: {error}") from error

    by_question = {q.question_id: q for q in questions}
    by_passage = {p.passage_id: p for p in inputs.passages}
    paper_counts = Counter(p.paper_id for p in inputs.passages)
    eligible_counts = Counter(
        p.paper_id for p in inputs.passages if section is None or p.section == section
    )
    logs = {method: {} for method in methods}
    hits = {method: {qid: [] for qid in by_question} for method in methods}

    def identity(row: dict):
        method, qid = row.get("method"), row.get("question_id")
        _require(isinstance(method, str) and method in logs, "unknown result method")
        _require(
            isinstance(qid, str) and qid in by_question,
            "unknown/non-development question_id in saved output",
        )
        question = by_question[qid]
        _require(
            row.get("paper_id") == question.paper_id
            and row.get("query") == question.query
            and row.get("config") == "run.json",
            f"{method}/{qid}: identity differs",
        )
        return method, qid

    for row in _rows(run_dir / "queries.jsonl"):
        method, qid = identity(row)
        _require(qid not in logs[method], f"{method}/{qid}: duplicate query log")
        _require(
            type(row.get("hit_count")) is int and row["hit_count"] >= 0,
            "invalid logged hit_count",
        )
        latency = row.get("latency_ms")
        _require(
            type(latency) in (int, float) and math.isfinite(latency) and latency >= 0,
            "invalid latency_ms",
        )
        _require(isinstance(row.get("status"), str), "invalid query status")
        logs[method][qid] = row
    for row in _rows(run_dir / "results.jsonl"):
        method, qid = identity(row)
        pid = row.get("passage_id")
        _require(isinstance(pid, str) and pid in by_passage, "unknown passage_id")
        passage = by_passage[pid]
        _require(passage.paper_id == by_question[qid].paper_id, "cross-paper result")
        _require(section is None or passage.section == section, "cross-section result")
        _require(
            type(row.get("rank")) is int and 1 <= row["rank"] <= top_k,
            "invalid result rank",
        )
        score = row.get("score")
        _require(type(score) in (int, float) and math.isfinite(score), "invalid score")
        hits[method][qid].append(row)

    issues, counts, method_reports = [], [], {}
    rankings = {method: {} for method in methods}
    for method in methods:
        distribution = Counter()
        for question in questions:
            qid, paper_id = question.question_id, question.paper_id
            rows = sorted(hits[method][qid], key=lambda row: row["rank"])
            pids = [row["passage_id"] for row in rows]
            _require(len(set(pids)) == len(pids), f"{method}/{qid}: duplicate passage")
            _require(
                [row["rank"] for row in rows] == list(range(1, len(rows) + 1)),
                f"{method}/{qid}: duplicate or non-continuous rank",
            )
            _require(
                all(a["score"] >= b["score"] for a, b in pairwise(rows)),
                f"{method}/{qid}: scores not descending",
            )
            expected = min(top_k, eligible_counts[paper_id])
            log = logs[method].get(qid)
            problems = []
            if log is None:
                problems.append("missing_query_log")
            else:
                if log["hit_count"] != len(rows):
                    problems.append("logged_hit_count_mismatch")
                expected_status = (
                    "ok"
                    if expected
                    else "paper_without_passages"
                    if not paper_counts[paper_id]
                    else "no_eligible_passages"
                )
                if log["status"] != expected_status:
                    problems.append("unexpected_query_status")
            if len(rows) != expected:
                problems.append("expected_return_count_mismatch")
            if problems:
                issues.append(
                    {"method": method, "question_id": qid, "issues": problems}
                )
            reason = (
                "paper_without_passages"
                if not paper_counts[paper_id]
                else "no_eligible_passages"
                if not eligible_counts[paper_id]
                else "eligible_passages_below_k"
                if expected < top_k
                else "full_k"
            )
            counts.append(
                {
                    "method": method,
                    "question_id": qid,
                    "paper_id": paper_id,
                    "paper_passage_count": paper_counts[paper_id],
                    "eligible_passage_count": eligible_counts[paper_id],
                    "expected_count": expected,
                    "actual_count": len(rows),
                    "logged_count": None if log is None else log["hit_count"],
                    "reason": reason,
                    "issues": problems,
                }
            )
            distribution[len(rows)] += 1
            rankings[method][qid] = pids
        latency_values = [row["latency_ms"] for row in logs[method].values()]
        current_counts = [row for row in counts if row["method"] == method]
        method_reports[method] = {
            "query_log_rows": len(logs[method]),
            "unique_question_ids": len(logs[method]),
            "result_rows": sum(row["actual_count"] for row in current_counts),
            "expected_result_rows": sum(
                row["expected_count"] for row in current_counts
            ),
            "maximum_slots": len(questions) * top_k,
            "legitimate_missing_slots": sum(
                top_k - row["expected_count"] for row in current_counts
            ),
            "return_count_distribution": {
                str(n): distribution[n] for n in range(top_k + 1)
            },
            "status_counts": dict(
                Counter(row["status"] for row in logs[method].values())
            ),
            "short_queries": [
                row for row in current_counts if row["expected_count"] < top_k
            ],
            "latency_ms": (
                {
                    "count": len(latency_values),
                    "mean": float(np.mean(latency_values)),
                    "min": min(latency_values),
                    "max": max(latency_values),
                    **{
                        f"p{n}": float(np.percentile(latency_values, n))
                        for n in (50, 95, 99)
                    },
                }
                if latency_values
                else None
            ),
        }
    if config["status"] != "complete":
        issues.append(
            {"issues": ["run_not_complete"], "recorded_status": config["status"]}
        )
    summary = config.get("summary", {})
    if summary.get("result_rows") != {
        m: r["result_rows"] for m, r in method_reports.items()
    }:
        issues.append({"issues": ["run_result_summary_mismatch"]})
    if summary.get("query_rows") != sum(len(rows) for rows in logs.values()):
        issues.append({"issues": ["run_query_summary_mismatch"]})
    report = {
        "status": "valid" if not issues else "invalid",
        "source_run": str(run_dir.resolve()),
        "source_run_sha256": file_sha256(run_dir / "run.json"),
        "input_sha256": inputs.provenance["sha256"],
        "output_sha256": config["output_sha256"],
        "recorded_run_status": config["status"],
        "top_k": top_k,
        "filters": filters,
        "filter_evidence": filter_evidence,
        "section_check": "not applicable (no requested section)"
        if section is None
        else "exact match",
        "question_count": len(questions),
        "methods": method_reports,
        "issues": issues,
        "checked": [
            "hashes",
            "train question coverage",
            "identity",
            "unique query logs",
            "unique passages and ranks",
            "finite descending scores",
            "paper/section membership",
            "min(K, eligible passage count)",
            "query status",
            "run completion and counts",
        ],
        "latency_note": "Recomputed from original logs; no new retrieval/timing run.",
    }
    return report, rankings, counts


def evaluate_saved_experiment(
    *,
    run_dir: Path,
    output_dir: Path,
    passages_path: Path | None = None,
    corpus_manifest_path: Path | None = None,
    qa_path: Path | None = None,
    export_manifest_path: Path | None = None,
    labels_path: Path | None = None,
    labels_manifest_path: Path | None = None,
    evaluation_k: int | None = None,
) -> dict:
    """Audit and optionally score existing outputs, preserving the source run."""
    from src.retrieval.evaluation import evaluate_rankings, load_qrels

    run_dir, output_dir = Path(run_dir).resolve(), Path(output_dir).resolve()
    _require(
        not output_dir.is_relative_to(run_dir), "output must be outside the source run"
    )
    _require(
        not output_dir.exists()
        or (output_dir.is_dir() and not any(output_dir.iterdir())),
        "output directory must be new or empty",
    )
    _require(
        (labels_path is None) == (labels_manifest_path is None),
        "provide both labels and labels manifest",
    )
    config = _object(run_dir / "run.json")
    overrides = {
        "passages": passages_path,
        "corpus_manifest": corpus_manifest_path,
        "qa": qa_path,
        "export_manifest": export_manifest_path,
    }
    try:
        paths = {
            key + "_path": value or Path(config["inputs"]["paths"][key])
            for key, value in overrides.items()
        }
    except (KeyError, TypeError) as error:
        raise ValueError(f"run input paths are missing: {error}") from error
    inputs = load_experiment_inputs(**paths)
    audit, rankings, counts = audit_saved_run(run_dir, inputs)
    k = audit["top_k"] if evaluation_k is None else evaluation_k
    _require(
        type(k) is int and 0 < k <= audit["top_k"],
        "evaluation K must be positive and no deeper than saved retrieval K",
    )
    if audit["status"] != "valid":
        quality = {
            "status": "unavailable",
            "metrics": None,
            "reason": "invalid retrieval artifacts; inspect audit issues",
        }
    elif labels_path is None:
        quality = {
            "status": "unavailable",
            "metrics": None,
            "k": k,
            "evaluated_questions": 0,
            "scope_questions": audit["question_count"],
            "excluded": {"missing_labels": audit["question_count"]},
            "reason": "No independently supplied gold passage-ID labels/manifest.",
            "protocol_status": "provisional; pending P6 alignment",
        }
    else:
        selected = inputs.questions[: config["limit"]]
        labels = load_qrels(
            labels_path,
            labels_manifest_path,
            corpus_sha256=inputs.provenance["sha256"]["passages"],
            questions={q.question_id: q.paper_id for q in selected},
            passages={p.passage_id: p.paper_id for p in inputs.passages},
            split_policy_version=SPLIT_POLICY,
        )
        quality = evaluate_rankings(rankings, labels, k=k)
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in (("audit.json", audit), ("evaluation.json", quality)):
        _write_json(output_dir / name, payload)
    with (output_dir / "counts.jsonl").open("w", encoding="utf-8") as handle:
        for row in counts:
            handle.write(json.dumps(row, allow_nan=False) + "\n")
    provenance = {
        "source_run_sha256": audit["source_run_sha256"],
        "retrieval_repeated": False,
        "source_outputs_modified": False,
        "python": sys.executable,
        "python_version": platform.python_version(),
        "evaluator_source_sha256": {
            str(p): file_sha256(Path(__file__).resolve().parents[2] / p)
            for p in (
                Path("src/retrieval/experiment.py"),
                Path("src/retrieval/evaluation.py"),
                Path("scripts/run_p1_experiment.py"),
            )
        },
        "labels_sha256": None
        if labels_path is None
        else file_sha256(Path(labels_path)),
        "labels_manifest_sha256": (
            None
            if labels_manifest_path is None
            else file_sha256(Path(labels_manifest_path))
        ),
    }
    _write_json(output_dir / "provenance.json", provenance)
    return {
        "status": audit["status"],
        "question_count": audit["question_count"],
        "output_dir": str(output_dir),
        "evaluation_status": quality["status"],
        "result_rows": {
            method: entry["result_rows"] for method, entry in audit["methods"].items()
        },
    }
