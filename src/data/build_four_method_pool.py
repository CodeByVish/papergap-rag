"""Extend the maintained common-pool CLI with a separately frozen fourth method.

The pilot reads only saved development questions. Formal retrieval preserves
held-out v2 order and refuses any change to the original three native rankings.
Both modes reuse the existing retrievers, pooling validator and Markdown path.
"""

from __future__ import annotations

import json
import platform
import time
from pathlib import Path

from src.data.build_annotation_pool import (
    DATA,
    code_identity,
    load_corpus,
    read_jsonl,
    snapshot,
    unique_rows,
    verify_snapshot,
    write_json,
    write_jsonl,
)
from src.data.build_common_pool import DEFAULT_OUTPUT as HISTORY
from src.data.build_common_pool import prepare, validate_pool
from src.data.build_common_pool import verify as verify_history
from src.data.build_multi_retriever_pilot import (
    FOUR_METHODS,
    build_retrievers,
    pool_rankings,
)
from src.evaluation.chunk_size_retrieval import normalize_retrieval, retriever_metadata

CONFIG = Path("configs/annotation_four.json")
PILOT = DATA / "annotation_pilot_four_v3"
OUTPUT = DATA / "annotation_common_v3"
MODES = ("bm25", "dense", "hybrid", "hybrid_rerank")


def configuration() -> dict:
    """Validate the new settings against the unchanged original retrieval freeze.

    Returns:
        Effective normalized settings with immutable model revisions and
        explicit inference, candidate, scoring and tie-breaking contracts.
    """
    raw = json.loads(CONFIG.read_text(encoding="utf-8"))
    original = normalize_retrieval(
        json.loads(Path("configs/annotation_pilot.json").read_text(encoding="utf-8"))[
            "retrieval"
        ]
    )
    retrieval = normalize_retrieval(raw["retrieval"])
    if retrieval["mode"] != "hybrid_rerank" or any(
        retrieval[k] != original[k] for k in ("dense", "candidate_k", "rrf_k")
    ):
        raise ValueError("the original three methods must remain unchanged")
    return {
        "schema_version": "v0-proposed",
        "chunk_size_words": 365,
        "chunk_overlap_words": 40,
        "top_k": 5,
        "methods": list(FOUR_METHODS),
        "retrieval": retrieval,
        "scope": "original query; complete same-paper corpus; shared papers allowed",
        "candidate_policy": "union of BM25 top-20 and Dense top-20; score every fused candidate before final top-five",
        "record_order": "saved question order; first encounter in frozen method/native rank order",
        "reranker_inference": {
            "model_name": "BAAI/bge-reranker-base",
            "padding": True,
            "truncation": "longest_first query-passage pair at 512 tokens",
            "score": "raw float32 relevance logit; eval and inference_mode",
            "tie_break": "logit descending; RRF descending; passage_id ascending",
        },
        "retrievers": {
            method: retriever_metadata({**retrieval, "mode": mode})
            for method, mode in zip(FOUR_METHODS, MODES)
        },
        "execution": {"HF_HUB_OFFLINE": "1", "persistent_score_cache": False},
    }


def compare_history(rankings: list[dict]) -> dict:
    """Require identical original native IDs and ranks before any export.

    Args:
        rankings: Newly executed four-method results, including native scores.

    Returns:
        Auditable comparison counts; score equality is also reported.

    Raises:
        ValueError: Any original method's IDs, order or ranks changed.
    """
    historical = {
        (r["question_id"], r["method"]): r["hits"]
        for r in read_jsonl(HISTORY / "rankings.jsonl")
    }
    checked = scores_equal = 0
    for row in rankings:
        if row["method"] == FOUR_METHODS[-1]:
            continue
        method = "Hybrid" if row["method"] == "Hybrid RRF" else row["method"]
        old = historical[row["question_id"], method]
        if [(h["passage_id"], h["rank"]) for h in row["hits"]] != [
            (h["passage_id"], h["rank"]) for h in old
        ]:
            raise ValueError(
                "original native IDs/ranks differ from v2; investigate before export"
            )
        checked += 1
        scores_equal += int(
            [h["score"] for h in row["hits"]] == [h["score"] for h in old]
        )
    if checked != 600:
        raise ValueError("requires 600 original-method rankings")
    return {
        "rankings_compared": checked,
        "identical_id_rank_lists": checked,
        "identical_score_lists": scores_equal,
    }


def inputs_for_run(pilot: bool) -> tuple[list, list, dict, dict, dict]:
    """Prepare development-only inputs or verified frozen formal inputs.

    Args:
        pilot: Select the first five persisted development queries only.

    Returns:
        Questions, full paper corpus, settings, input hashes and retained hashes.
    """
    settings = configuration()
    if pilot:
        path = DATA / "qa_for_choosing_chunk_size.jsonl"
        preparation = json.loads(
            (DATA / "annotation_preparation.manifest.json").read_text(encoding="utf-8")
        )
        verify_snapshot({path.as_posix(): preparation["inputs"][path.as_posix()]})
        saved = read_jsonl(path)
        if len(unique_rows(saved, "question_id")) != 250:
            raise ValueError("requires 250 saved development questions")
        questions = saved[:5]
        papers = {q["paper_id"] for q in questions}
        corpus = [p for p in load_corpus(DATA) if p["paper_id"] in papers]
        inputs = snapshot(
            [
                CONFIG,
                path,
                DATA / "annotation_preparation.manifest.json",
                DATA / "passages_all_paper_text.jsonl",
                DATA / "passages_all_paper_text.manifest.json",
            ]
        )
        history = {}
    else:
        verify_history(HISTORY)
        questions, corpus, _, inputs = prepare()
        pilot_manifest = json.loads(
            (PILOT / "manifest.json").read_text(encoding="utf-8")
        )
        verify_snapshot(pilot_manifest["inputs"])
        verify_snapshot(pilot_manifest["outputs"])
        if pilot_manifest["settings"] != settings:
            raise ValueError("settings differ from successful development freeze")
        inputs.update(
            snapshot([CONFIG, PILOT / "manifest.json", PILOT / "frozen_config.json"])
        )
        history = snapshot(
            sorted(
                [
                    *HISTORY.rglob("*.*"),
                    *(DATA / "annotation_common_v2_markdown").rglob("*.*"),
                ]
            )
        )
        old_manifest = json.loads(
            (HISTORY / "manifest.json").read_text(encoding="utf-8")
        )
        history.update(old_manifest["historical_retained_files"])
    return questions, corpus, settings, inputs, history


def run(output: Path, *, pilot: bool = False) -> dict:
    """Freeze provenance before executing fresh retrieval and persist its union.

    Args:
        output: New version directory; existing partial outputs are refused.
        pilot: Run development feasibility without opening held-out content.

    Returns:
        Validated counts with no question, evidence or passage text displayed.
    """
    if output.exists():
        raise FileExistsError(output)
    questions, corpus, settings, inputs, history = inputs_for_run(pilot)
    identity = code_identity()
    output.mkdir(parents=True)
    write_json(output / "frozen_config.json", settings)
    write_json(
        output / "run_inputs.json",
        {"inputs": inputs, "code": identity, "history": history},
    )
    write_jsonl(output / "questions.jsonl", questions)
    print(
        f"Configuration frozen; indexing {len(corpus)} passages for {len(questions)} questions.",
        flush=True,
    )
    started = time.perf_counter()
    retrievers = build_retrievers(corpus, settings["retrieval"])
    pairs, rankings = pool_rankings(questions, corpus, retrievers, FOUR_METHODS)
    counts = validate_pool(questions, corpus, pairs, rankings, FOUR_METHODS)
    comparison = {} if pilot else compare_history(rankings)
    verify_snapshot(inputs)
    verify_snapshot(history)
    verify_snapshot(identity["source_sha256"])
    write_jsonl(output / "pairs.jsonl", pairs)
    write_jsonl(output / "rankings.jsonl", rankings)
    write_json(
        output / "manifest.json",
        {
            "schema_version": "v0-proposed",
            "pilot": pilot,
            "purpose": "development feasibility only"
            if pilot
            else "formal four-method held-out common pool",
            "reason": "add full RRF-candidate BGE reranking before human annotation; retain v2 history",
            "settings": settings,
            "inputs": inputs,
            "code": identity,
            "historical_retained_files": history,
            "historical_comparison": comparison,
            "validation": counts,
            "indexed_passage_count": len(corpus),
            "indexed_paper_count": len({p["paper_id"] for p in corpus}),
            "runtime": {
                "platform": platform.platform(),
                "elapsed_seconds": time.perf_counter() - started,
                "policy": "single CPU run including indexing and all four methods; no latency benchmark",
            },
            "usage_boundary": "no held-out tuning; no resampling; null labels; unpooled passages unjudged; metrics use native ranks",
            "outputs": snapshot(sorted(p for p in output.iterdir() if p.is_file())),
        },
    )
    return verify(output)


def verify(output: Path) -> dict:
    """Replay canonical union and check frozen inputs, outputs and history.

    Args:
        output: Completed four-method pilot or formal directory.

    Returns:
        Reconstructed counts after configuration and native-rank checks pass.
    """
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    for key in ("inputs", "outputs", "historical_retained_files"):
        verify_snapshot(manifest[key])
    questions, corpus, settings, inputs, history = inputs_for_run(manifest["pilot"])
    if (
        settings != manifest["settings"]
        or inputs != manifest["inputs"]
        or history != manifest["historical_retained_files"]
    ):
        raise ValueError("frozen configuration, inputs or history changed")
    if (
        json.loads((output / "frozen_config.json").read_text(encoding="utf-8"))
        != settings
    ):
        raise ValueError("pre-run configuration differs")
    if (
        json.loads((output / "run_inputs.json").read_text(encoding="utf-8"))
        != {"inputs": inputs, "code": manifest["code"], "history": history}
        or read_jsonl(output / "questions.jsonl") != questions
    ):
        raise ValueError("pre-run provenance or saved questions differ")
    rankings = read_jsonl(output / "rankings.jsonl")
    counts = validate_pool(
        questions, corpus, read_jsonl(output / "pairs.jsonl"), rankings, FOUR_METHODS
    )
    comparison = {} if manifest["pilot"] else compare_history(rankings)
    if (
        counts != manifest["validation"]
        or comparison != manifest["historical_comparison"]
    ):
        raise ValueError("saved counts or historical comparison differ")
    return counts


def dispatch(action: str, output: Path) -> dict:
    """Route the maintained common-pool CLI to independent four-method versions.

    Args:
        action: Pilot feasibility, formal run or read-only verification.
        output: Explicit new version path or the original CLI default sentinel.

    Returns:
        Verified counts for the requested operation.
    """
    if output == HISTORY:
        output = PILOT if action == "pilot" else OUTPUT
    return (
        verify(output) if action == "verify" else run(output, pilot=action == "pilot")
    )
