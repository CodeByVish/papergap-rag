"""Run reproducible, development-only comparisons of word-based chunk sizes.

The runner reuses P3's verified exports and chunker. Its local paper-filtered
BM25 baseline can be replaced through an explicit retriever factory in Python;
it does not require a generator, model service or held-out tuning data.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
import platform
import random
import re
import subprocess
import time
from collections import Counter
from collections.abc import Callable
from dataclasses import asdict
from pathlib import Path
from typing import Any

from src.data.chunking import (
    ChunkingConfig,
    build_passages_from_record,
    validate_built_passages,
)
from src.data.passage_ids import PassageIdContext
from src.data.qasper_export import check_qasper_export, load_verified_papers
from src.data.split_policy import (
    SPLIT_POLICY_VERSION,
    assert_data_use_allowed,
    project_role_for_official_split,
)
from src.evaluation.chunk_size_metrics import (
    evaluate_question,
    locate_annotations,
    passage_spans,
    source_paragraphs,
)
from src.evaluation.chunk_size_reports import (
    evidence_section,
    readability_report,
    write_json,
)

ROOT = Path(__file__).resolve().parents[2]
DEFAULTS = {
    "overlap_words": 40,
    "top_k": 5,
    "question_sample_count": 50,
    "readability_sample_count": 10,
    "question_seed": 42,
    "readability_seed": 43,
}
Retriever = Callable[[str, str, int], list[tuple[str, float]]]
RetrieverFactory = Callable[[list[dict[str, Any]]], Retriever]


def load_config(path: Path) -> dict[str, Any]:
    """Validate experiment settings without silently accepting misspelled keys.

    The original candidates-only configuration remains supported using explicit
    defaults. All sizes are words; top_k is fixed to five by the metric contract.
    """
    supplied = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(supplied, dict) or set(supplied) - {"candidates", *DEFAULTS}:
        raise ValueError("configuration must be an object with known keys")
    config = {**DEFAULTS, **supplied}
    candidates = config.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("candidates must be a nonempty list")
    if any(type(size) is not int or size <= 0 for size in candidates):
        raise ValueError("candidates must contain positive integers")
    if len(set(candidates)) != len(candidates):
        raise ValueError("candidates must be unique")
    for key in DEFAULTS:
        if type(config[key]) is not int or config[key] < 0:
            raise ValueError(f"{key} must be a nonnegative integer")
    if config["top_k"] != 5:
        raise ValueError(
            "top_k must be 5 for Evidence Hit@5 and complete evidence rate@5"
        )
    if not config["question_sample_count"] or not config["readability_sample_count"]:
        raise ValueError("sample counts must be positive")
    for size in candidates:
        ChunkingConfig(
            chunk_size_words=size, chunk_overlap_words=config["overlap_words"]
        )
    return config


def file_hash(path: Path) -> str:
    """Hash an input file without loading a complete corpus into memory.

    Hashes identify the exact UTF-8 export and configuration bytes used by a run.
    """
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def local_bm25(passages: list[dict[str, Any]]) -> Retriever:
    """Build a paper-filtered rank-bm25 baseline with deterministic score ties.

    Tokens are casefolded Unicode word runs. Each paper has its own BM25 index;
    model parameters follow rank-bm25 defaults and are recorded in the manifest.
    """
    from rank_bm25 import BM25Okapi

    groups: dict[str, list[dict[str, Any]]] = {}
    for passage in passages:
        groups.setdefault(passage["paper_id"], []).append(passage)
    indexes = {}
    for paper_id, items in groups.items():
        items.sort(key=lambda item: item["passage_id"])
        tokens = [re.findall(r"\w+", item["text"].casefold()) for item in items]
        # A punctuation-only paper cannot produce a nonempty lexical vocabulary.
        indexes[paper_id] = (items, BM25Okapi(tokens) if any(tokens) else None)

    def retrieve(query: str, paper_id: str, top_k: int) -> list[tuple[str, float]]:
        """Return up to top_k scored IDs from the selected paper.

        Empty lexical vocabularies return deterministic zero-score rankings.
        """
        items, index = indexes[paper_id]
        scores = (
            index.get_scores(re.findall(r"\w+", query.casefold()))
            if index
            else [0.0] * len(items)
        )
        ranked = sorted(
            zip(items, scores), key=lambda pair: (-pair[1], pair[0]["passage_id"])
        )
        return [(item["passage_id"], float(score)) for item, score in ranked[:top_k]]

    return retrieve


def select_questions(
    questions: list[dict[str, Any]],
    papers: dict[str, dict[str, Any]],
    paragraphs: dict[str, dict[str, dict[str, Any]]],
    common_papers: set[str],
    config: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, int], dict[str, list[dict[str, Any]]]]:
    """Filter before seeded sampling and retain annotation groups for scoring.

    Every input question receives exactly one filtering outcome. Paper and QA
    split consistency has already been checked by the verified export loader.
    """
    counts: Counter[str] = Counter()
    eligible = []
    annotations = {}
    for question in sorted(questions, key=lambda item: item["question_id"]):
        if question["source_split"] == "test":
            counts["held_out"] += 1
            continue
        role = project_role_for_official_split(question["source_split"])
        for asset in ("question", "answer", "label"):
            assert_data_use_allowed(
                project_role=role,
                asset=asset,
                purpose="chunk_selection",
                evaluation_frozen=False,
            )
        paper_id = question["paper_id"]
        if paper_id not in papers or paper_id not in common_papers:
            counts["paper_not_in_every_corpus"] += 1
            continue
        located = locate_annotations(question, paragraphs[paper_id])
        if not any(annotation["usable"] for annotation in located):
            counts["no_usable_text_evidence"] += 1
            continue
        annotations[question["question_id"]] = located
        eligible.append(question)
        counts["eligible"] += 1
    if not eligible:
        raise ValueError("no eligible development/validation questions")
    sample = random.Random(config["question_seed"]).sample(
        eligible,
        min(config["question_sample_count"], len(eligible)),
    )
    counts["total"] = len(questions)
    return sample, dict(counts), annotations


def build_candidate(
    papers: dict[str, dict[str, Any]],
    source: dict[str, Any],
    size: int,
    overlap: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Build one candidate corpus with shared IDs and private source provenance.

    Size and overlap are word counts and enter both the chunker and ID context.
    The returned config records the validated normalization and chunk versions.
    """
    config = ChunkingConfig(chunk_size_words=size, chunk_overlap_words=overlap)
    context = PassageIdContext(
        dataset_id=source["dataset_id"],
        resolved_revision=source["resolved_revision"],
        local_parser_version=source["local_parser_version"],
        **asdict(config),
    )
    passages = []
    for paper_id in sorted(papers):
        paper = papers[paper_id]
        built = build_passages_from_record(
            paper, context=context, config=config
        ).passages
        validate_built_passages(built)
        spans = passage_spans(paper, built, config)
        passages.extend(
            {
                **item.passage.model_dump(),
                "spans": spans[item.passage.passage_id],
            }
            for item in built
        )
    return passages, asdict(config)


def retrieve_question(
    retrieve: Retriever,
    question: dict[str, Any],
    by_id: dict[str, dict[str, Any]],
    top_k: int,
) -> tuple[list[dict[str, Any]], float]:
    """Time retrieval and resolve scored IDs against this candidate's corpus.

    Reject duplicate, unknown, wrong-paper or over-limit matches and nonfinite
    scores before they can influence a metric or appear in a saved report.
    """
    started = time.perf_counter()
    matches = retrieve(question["question"], question["paper_id"], top_k)
    seconds = time.perf_counter() - started
    if len(matches) > top_k or len({pid for pid, _ in matches}) != len(matches):
        raise ValueError("retriever returned too many or duplicate passages")
    retrieved = []
    for passage_id, score in matches:
        if (
            passage_id not in by_id
            or by_id[passage_id]["paper_id"] != question["paper_id"]
        ):
            raise ValueError(
                "retriever returned an unknown ID or a passage from another paper"
            )
        if not math.isfinite(score):
            raise ValueError("retrieval scores must be finite")
        retrieved.append({**by_id[passage_id], "score": float(score)})
    return retrieved, seconds


def run_comparison(
    *,
    config_path: Path,
    papers_path: Path,
    qa_path: Path,
    export_manifest: Path,
    output_root: Path,
    run_id: str,
    retriever_factory: RetrieverFactory | None = None,
    retriever_metadata: dict[str, Any] | None = None,
) -> Path:
    """Build candidate corpora and publish one new comparison directory.

    A custom retriever factory receives the full candidate corpus and returns
    ``(query, paper_id, top_k) -> [(passage_id, score)]``. It must provide explicit
    reproducibility metadata. Outputs never overwrite an existing run.
    """
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", run_id):
        raise ValueError("run_id must be a simple directory name")
    run_dir = output_root / run_id
    if run_dir.exists():
        raise FileExistsError(f"run already exists: {run_dir}")
    config = load_config(config_path)
    if retriever_factory is not None and not retriever_metadata:
        raise ValueError("custom retrievers require explicit metadata")
    factory = retriever_factory or local_bm25
    check_qasper_export(
        papers_path=papers_path, qa_path=qa_path, manifest_path=export_manifest
    )
    export, records = load_verified_papers(
        papers_path=papers_path, manifest_path=export_manifest
    )
    papers = {
        paper["id"]: paper for paper in records if paper["source_split"] != "test"
    }
    paragraphs = {
        paper_id: source_paragraphs(paper) for paper_id, paper in papers.items()
    }
    corpora = {}
    chunk_configs = {}
    build_seconds = {}
    for size in config["candidates"]:
        started = time.perf_counter()
        corpora[size], chunk_configs[str(size)] = build_candidate(
            papers,
            export["source"],
            size,
            config["overlap_words"],
        )
        build_seconds[str(size)] = time.perf_counter() - started
    common_papers = set.intersection(
        *({item["paper_id"] for item in corpus} for corpus in corpora.values())
    )
    questions = [
        json.loads(line) for line in qa_path.read_text(encoding="utf-8").splitlines()
    ]
    selected, filtering, annotations = select_questions(
        questions,
        papers,
        paragraphs,
        common_papers,
        config,
    )
    locations = [
        paragraph
        for paper_id in sorted(common_papers)
        for paragraph in paragraphs[paper_id].values()
    ]
    samples = random.Random(config["readability_seed"]).sample(
        locations,
        min(config["readability_sample_count"], len(locations)),
    )
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    status = subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=ROOT, text=True
    )
    metadata = retriever_metadata or {
        "id": "experiment-local-paper-bm25-v1",
        "package": "rank-bm25",
        "version": importlib.metadata.version("rank-bm25"),
        "model_revision": None,
        "tokenizer": "casefold + Unicode word runs",
        "scope": "selected paper",
        "k1": 1.5,
        "b": 0.75,
        "epsilon": 0.25,
        "tie_break": "passage_id ascending",
    }
    manifest = {
        "schema_version": "v0-proposed",
        "run_id": run_id,
        "config": config,
        "code_commit": commit,
        "working_tree_dirty": bool(status),
        "working_tree_status": status.splitlines(),
        "split_policy_version": SPLIT_POLICY_VERSION,
        "source": export["source"],
        "source_splits": ["train", "validation"],
        "inputs": {
            name: {"path": str(path.resolve()), "sha256": file_hash(path)}
            for name, path in {
                "config": config_path,
                "papers": papers_path,
                "qa": qa_path,
                "export_manifest": export_manifest,
            }.items()
        },
        "retriever": metadata,
        "chunking": chunk_configs,
        "question_ids": [question["question_id"] for question in selected],
        "question_sample_count_requested": config["question_sample_count"],
        "question_sample_count_actual": len(selected),
        "filtering_counts": filtering,
        "readability_samples": [
            {
                key: sample[key]
                for key in ("location", "paper_id", "section_index", "paragraph_index")
            }
            | {"character_span": [0, len(sample["text"])]}
            for sample in samples
        ],
        "readability_sample_count_actual": len(samples),
        "readability_passage_ids": {},
        "dependencies": sorted(
            f"{dist.metadata['Name']}=={dist.version}"
            for dist in importlib.metadata.distributions()
        ),
        "hardware": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        },
        "python": platform.python_version(),
        "prompts": None,
        "generator": None,
        "timing_policy": "perf_counter wall seconds; per-query excludes index build and report rendering",
        "build_seconds": build_seconds,
    }
    summary: dict[str, Any] = {
        "schema_version": "v0-proposed",
        "run_id": run_id,
        "sizes": {},
    }
    # Reserve the ID only after validation and sampling. An interrupted run stays
    # visible and cannot be mistaken for a completed comparison without a manifest.
    run_dir.mkdir(parents=True, exist_ok=False)
    for size, corpus in corpora.items():
        directory = run_dir / f"chunk_size_{size}"
        directory.mkdir()
        index_started = time.perf_counter()
        retrieve = factory(corpus)
        index_seconds = time.perf_counter() - index_started
        by_id = {item["passage_id"]: item for item in corpus}
        reports = ["# Evidence Review\n"]
        results = []
        for question in selected:
            retrieved, seconds = retrieve_question(
                retrieve,
                question,
                by_id,
                config["top_k"],
            )
            located = annotations[question["question_id"]]
            paper_paragraphs = paragraphs[question["paper_id"]]
            metrics = evaluate_question(located, paper_paragraphs, retrieved)
            reports.append(
                evidence_section(
                    question, located, paper_paragraphs, retrieved, metrics
                )
            )
            results.append(
                {
                    "question_id": question["question_id"],
                    **metrics,
                    "retrieval_seconds": seconds,
                    "retrieved": [
                        {"passage_id": item["passage_id"], "score": item["score"]}
                        for item in retrieved
                    ],
                }
            )
        (directory / "evidence_review.md").write_text(
            "\n".join(reports), encoding="utf-8"
        )
        review, review_ids = readability_report(samples, papers, corpus)
        (directory / "readability.md").write_text(review, encoding="utf-8")
        manifest["readability_passage_ids"][str(size)] = review_ids
        count = len(results)
        hits = sum(result["evidence_hit_at_5"] for result in results)
        complete = sum(result["complete_evidence_at_5"] for result in results)
        words = sum(result["total_retrieved_words"] for result in results)
        corpus_bytes = "\n".join(
            json.dumps(item, sort_keys=True, ensure_ascii=False) for item in corpus
        ).encode("utf-8")
        summary["sizes"][str(size)] = {
            "evidence_hit_at_5": {
                "value": hits / count,
                "numerator": hits,
                "denominator": count,
            },
            "complete_evidence_rate_at_5": {
                "value": complete / count,
                "numerator": complete,
                "denominator": count,
            },
            "retrieved_word_count": {
                "value": words / count,
                "numerator": words,
                "denominator": count,
            },
            "readability_pass_rate": {
                "value": None,
                "numerator": 0,
                "denominator": len(review_ids),
                "pending": len(review_ids),
            },
            "corpus_passage_count": len(corpus),
            "corpus_sha256": hashlib.sha256(corpus_bytes).hexdigest(),
            "index_seconds": index_seconds,
            "questions": results,
        }
    write_json(run_dir / "summary.json", summary)
    write_json(run_dir / "manifest.json", manifest)
    return run_dir
