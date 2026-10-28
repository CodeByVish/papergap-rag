"""Build and verify the formal three-method held-out retrieval union.

Run from the repository root with ``python -m src.data.build_common_pool run``.
The runner consumes the saved question order without sampling, freezes effective
settings before indexing, and never opens gold evidence or historical rankings
for retrieval. Verification replays saved rankings without loading a model.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import time
from collections import Counter
from pathlib import Path

from src.data.build_annotation_pool import (
    DATA,
    SETTINGS,
    code_identity,
    load_corpus,
    read_jsonl,
    snapshot,
    unique_rows,
    verify_snapshot,
    write_json,
    write_jsonl,
)
from src.data.build_multi_retriever_pilot import (
    METHODS,
    build_retrievers,
    pool_rankings,
)
from src.data.freeze_held_out import OUTPUT, RETIREMENT, freeze
from src.evaluation.chunk_size_retrieval import normalize_retrieval, retriever_metadata

DEFAULT_OUTPUT = DATA / "annotation_common_v2"
PILOT = DATA / "annotation_pilot_multi_v2"
CONFIG = Path("configs/annotation_pilot.json")


def prepare() -> tuple[list[dict], list[dict], dict, dict]:
    """Validate frozen questions, history and the successful development settings.

    Returns:
        Saved questions, complete selected-paper corpus, effective settings and
        input hashes. The freeze reconstruction checks eligibility only; its
        reconstructed draw is never used as the retrieval input.
    """
    freeze(verify_only=True)
    pilot_manifest = json.loads((PILOT / "manifest.json").read_text(encoding="utf-8"))
    verify_snapshot(pilot_manifest["outputs"])
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    if config != json.loads((PILOT / "frozen_config.json").read_text(encoding="utf-8")):
        raise ValueError("configuration differs from the development freeze")
    if any(config[key] != SETTINGS[key] for key in SETTINGS):
        raise ValueError("requires 365/40 and top-five")
    retrieval = normalize_retrieval(config["retrieval"])
    if retrieval["mode"] != "hybrid":
        raise ValueError("requires the frozen hybrid configuration without reranking")
    questions = read_jsonl(OUTPUT)
    ids = set(unique_rows(questions, "question_id"))
    banned = unique_rows(
        read_jsonl(DATA / "qa_banned_for_held_out.jsonl"), "question_id"
    )
    if len(ids) != 200 or ids.intersection(banned):
        raise ValueError("requires exactly 200 unique non-banned questions")
    papers = {q["paper_id"] for q in questions}
    corpus = [p for p in load_corpus(DATA) if p["paper_id"] in papers]
    settings = {
        "schema_version": "v0-proposed",
        **SETTINGS,
        "question_count": 200,
        "question_selection": "saved held-out v2 order; no resampling",
        "scope": "paper-scoped; complete selected papers; shared papers allowed",
        "retrieval": retrieval,
        "retrievers": {
            method: retriever_metadata({**retrieval, "mode": mode})
            for method, mode in zip(METHODS, ("bm25", "dense", "hybrid"))
        },
        "record_order": "saved question order; first encounter in BM25, Dense, Hybrid native rank order",
        "label_policy": "one null final label per unique pair; human judgments pending",
        "execution": {
            "HF_HUB_OFFLINE": "1",
            "model_loading": "same offline policy as development CLI",
        },
    }
    paths = [
        CONFIG,
        PILOT / "manifest.json",
        PILOT / "frozen_config.json",
        OUTPUT,
        OUTPUT.with_suffix(".manifest.json"),
        RETIREMENT,
        *[
            DATA / name
            for name in (
                "qa_banned_for_held_out.jsonl",
                "qa_banned_for_held_out.manifest.json",
                "passages_all_paper_text.jsonl",
                "passages_all_paper_text.manifest.json",
                "papers.jsonl",
                "qa.jsonl",
                "qasper_export.manifest.json",
            )
        ],
    ]
    return questions, corpus, settings, snapshot(paths)


def validate_pool(
    questions: list[dict], corpus: list[dict], pairs: list[dict], rankings: list[dict]
) -> dict:
    """Reconstruct all pairs from persisted rankings and check exact equality.

    Args:
        questions: Frozen questions in retrieval order.
        corpus: Complete same-paper passages with canonical text and titles.
        pairs: Persisted union including labels and source ranks/scores.
        rankings: One complete top-five list per question and method.

    Returns:
        Counts of unique pairs, per-question sizes and display groups.

    Raises:
        ValueError: A ranking is missing, duplicated, invalid or inconsistent
            with the canonical pair mapping, text, ranks, scores or blank labels.
    """
    saved = {(r["question_id"], r["method"]): r["hits"] for r in rankings}
    expected = {(q["question_id"], m) for q in questions for m in METHODS}
    if len(saved) != len(rankings) or set(saved) != expected:
        raise ValueError("missing, duplicate or unknown method/question ranking")
    by_query = {(q["question"], q["paper_id"]): q["question_id"] for q in questions}
    if len(by_query) != len(questions):
        raise ValueError("ambiguous query/paper identity")

    def callback(method: str):
        """Adapt one persisted method to the existing strict pooling validator.

        Args:
            method: Named retrieval method whose native ordering is retained.

        Returns:
            Callback using only saved hits rather than executing retrieval.
        """

        def retrieve(query: str, paper_id: str, top_k: int) -> list:
            """Replay one saved top-five ranking without consulting relevance.

            Args:
                query: Canonical question text used to locate its saved ID.
                paper_id: Original retrieval scope.
                top_k: Required depth, always five in the pooling contract.

            Returns:
                Native ordered passage IDs and scores.
            """
            hits = saved[by_query[query, paper_id], method]
            if top_k != 5:
                raise ValueError("unexpected retrieval depth")
            return [(h["passage_id"], h["score"]) for h in hits]

        return retrieve

    rebuilt, native = pool_rankings(
        questions, corpus, {m: callback(m) for m in METHODS}
    )
    if rebuilt != pairs or native != rankings:
        raise ValueError("pairs/rankings differ from canonical union or native ranks")
    counts = Counter(p["question_id"] for p in pairs)
    if set(counts) != {q["question_id"] for q in questions} or any(
        not 5 <= n <= 15 for n in counts.values()
    ):
        raise ValueError("each question requires 5..15 unique pairs")
    return {
        "question_count": len(questions),
        "pair_count": len(pairs),
        "ranking_count": len(rankings),
        "hits_per_method": len(questions) * 5,
        "pair_counts_per_question": dict(counts),
        "group_counts": dict(Counter(p["display_group"] for p in pairs)),
        "pair_count_range": [min(counts.values()), max(counts.values())],
    }


def run(output: Path) -> dict:
    """Freeze inputs before fresh retrieval and save a new independent version.

    Args:
        output: Nonexistent directory; existing and partial versions are refused.

    Returns:
        Verified output counts. No Markdown or relevance metrics are generated.
    """
    if output.exists():
        raise FileExistsError(output)
    questions, corpus, settings, inputs = prepare()
    identity = code_identity()
    output.mkdir(parents=True)
    write_json(output / "frozen_config.json", settings)
    write_json(output / "run_inputs.json", {"inputs": inputs, "code": identity})
    write_jsonl(output / "questions.jsonl", questions)
    print("Inputs and configuration frozen; starting fresh retrieval.", flush=True)
    started = time.perf_counter()
    retrievers = build_retrievers(corpus, settings["retrieval"])
    print("Fresh sparse/dense indexes ready; retrieving 200 questions.", flush=True)
    pairs, rankings = pool_rankings(questions, corpus, retrievers)
    elapsed = time.perf_counter() - started
    validation = validate_pool(questions, corpus, pairs, rankings)
    verify_snapshot(inputs)
    verify_snapshot(identity["source_sha256"])
    write_jsonl(output / "pairs.jsonl", pairs)
    write_jsonl(output / "rankings.jsonl", rankings)
    retirement = json.loads(RETIREMENT.read_text(encoding="utf-8"))
    write_json(
        output / "manifest.json",
        {
            "schema_version": "v0-proposed",
            "purpose": "formal held-out v2 BM25/Dense/Hybrid common evaluation pool",
            "reason": retirement["reason"],
            "historical_retained_files": retirement["retained_files"],
            "reuse_policy": "fresh retrieval; no historical pairs, scores, ranks, labels or numbering reused",
            "settings": settings,
            "inputs": inputs,
            "code": identity,
            "indexed_paper_count": len({p["paper_id"] for p in corpus}),
            "indexed_passage_count": len(corpus),
            "validation": validation,
            "runtime": {
                "platform": platform.platform(),
                "processor": platform.processor(),
                "elapsed_seconds": elapsed,
                "timing_policy": "single CPU run; index construction and three-method retrieval together; no latency benchmark",
            },
            "usage_boundary": "no held-out-driven tuning; unpooled passages unjudged; original algorithm ranks govern metrics; human annotation pending",
            "outputs": snapshot(sorted(p for p in output.iterdir() if p.is_file())),
        },
    )
    return verify(output)


def verify(output: Path) -> dict:
    """Verify saved hashes and cross-file mappings without model inference.

    Args:
        output: Completed formal output directory.

    Returns:
        Reconstructed validation counts, after all inputs and history pass.
    """
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    verify_snapshot(manifest["inputs"])
    verify_snapshot(manifest["outputs"])
    verify_snapshot(manifest["historical_retained_files"])
    questions, corpus, settings, inputs = prepare()
    if settings != manifest["settings"] or inputs != manifest["inputs"]:
        raise ValueError("formal settings or inputs changed")
    if read_jsonl(output / "questions.jsonl") != questions:
        raise ValueError("questions differ from saved held-out list")
    if (
        json.loads((output / "frozen_config.json").read_text(encoding="utf-8"))
        != settings
    ):
        raise ValueError("formal config differs from pre-run freeze")
    provenance = json.loads((output / "run_inputs.json").read_text(encoding="utf-8"))
    if provenance != {"inputs": inputs, "code": manifest["code"]}:
        raise ValueError("pre-run provenance differs from manifest")
    validation = validate_pool(
        questions,
        corpus,
        read_jsonl(output / "pairs.jsonl"),
        read_jsonl(output / "rankings.jsonl"),
    )
    if validation != manifest["validation"]:
        raise ValueError("manifest counts differ from persisted pool")
    return validation


def main() -> None:
    """Expose fresh generation and read-only saved-pool verification.

    Only counts are printed; no held-out content or relevance is displayed.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("run", "verify"))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    # Match the development CLI: optional processor probes omit local_files_only.
    # Set this before lazy model imports and restore the caller's environment.
    previous_offline = os.environ.get("HF_HUB_OFFLINE")
    os.environ["HF_HUB_OFFLINE"] = "1"
    try:
        result = run(args.output) if args.action == "run" else verify(args.output)
    finally:
        if previous_offline is None:
            os.environ.pop("HF_HUB_OFFLINE", None)
        else:
            os.environ["HF_HUB_OFFLINE"] = previous_offline
    print(json.dumps({k: v for k, v in result.items() if not isinstance(v, dict)}))


if __name__ == "__main__":
    main()
