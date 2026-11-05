"""Exercise multi-system pooling on saved development questions only.

Reuse the public retrieval contracts without changing shared interfaces or the
historical BM25 freeze. Gold joins happen after all three rankings are complete.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from collections.abc import Callable
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
from src.evaluation.chunk_size_retrieval import (
    normalize_retrieval,
    project_passages,
    retriever_metadata,
    scored_ids,
)

METHODS = ("BM25", "Dense", "Hybrid")
FOUR_METHODS = ("BM25", "Dense", "Hybrid RRF", "Hybrid RRF followed by BGE reranking")
DEFAULT_CONFIG = Path("configs/annotation_pilot.json")
DEFAULT_OUTPUT = DATA / "annotation_pilot_multi_v2"
Retrieve = Callable[[str, str, int], list[tuple[str, float]]]


def build_retrievers(corpus: list[dict], settings: dict) -> dict[str, Retrieve]:
    """Share sparse/dense indexes, optionally adding full-candidate BGE scoring.

    Args:
        corpus: All passages belonging to the selected development papers.
        settings: Validated hybrid configuration with an immutable model revision.

    Returns:
        Named callbacks returning ordered passage IDs and native scores.
    """
    from src.retrieval.bm25_retriever import BM25Retriever
    from src.retrieval.dense_retriever import DenseRetriever
    from src.retrieval.hybrid_retriever import HybridRetriever

    passages = project_passages(corpus)
    sparse = BM25Retriever(passages)
    dense = DenseRetriever(passages, **settings["dense"])
    hybrid = HybridRetriever(
        sparse.retrieve,
        dense.retrieve,
        candidate_k=settings["candidate_k"],
        rrf_k=settings["rrf_k"],
    )

    def callback(backend: object) -> Retrieve:
        """Adapt a backend while retaining its native rank order.

        Args:
            backend: Existing P1/P2 retriever instance.

        Returns:
            Query callback with no access to evidence or labels.
        """

        def retrieve(query: str, paper_id: str, top_k: int) -> list:
            """Score the original query within one paper.

            Args:
                query: Unmodified development question.
                paper_id: Paper scope shared by all systems.
                top_k: Number of requested results.

            Returns:
                Ranked passage identifiers and finite scores.
            """
            return scored_ids(backend.retrieve(query, paper_id, top_k))

        return retrieve

    if settings["mode"] == "hybrid_rerank":
        from src.retrieval.reranker import BGEReranker

        reranked = HybridRetriever(
            sparse.retrieve,
            dense.retrieve,
            scorer=BGEReranker(**settings["reranker"]),
            candidate_k=settings["candidate_k"],
            rrf_k=settings["rrf_k"],
        )
        return dict(zip(FOUR_METHODS, map(callback, (sparse, dense, hybrid, reranked))))
    return dict(zip(METHODS, map(callback, (sparse, dense, hybrid))))


def pool_rankings(
    questions: list[dict],
    corpus: list[dict],
    retrievers: dict[str, Retrieve],
    methods: tuple[str, ...] = METHODS,
) -> tuple[list[dict], list[dict]]:
    """Validate complete top-five lists and union by question/passage pair.

    Args:
        questions: Unique development questions in persisted order.
        corpus: Same corpus used by every retriever, without evidence fields.
        retrievers: Exactly the callbacks named in methods.
        methods: Ordered three- or four-method contract; defines numbering.

    Returns:
        Pair records with all source ranks/scores, and complete ranking records.

    Raises:
        ValueError: A backend returns duplicate, missing, foreign or invalid hits.
    """
    unique_rows(questions, "question_id")
    passages = unique_rows(corpus, "passage_id")
    if methods not in (METHODS, FOUR_METHODS) or set(retrievers) != set(methods):
        raise ValueError("retrievers must match the three- or four-method contract")
    pairs, rankings = [], []
    for question in questions:
        union = {}
        for method in methods:
            hits = retrievers[method](question["question"], question["paper_id"], 5)
            if len(hits) != 5 or len({pid for pid, _ in hits}) != 5:
                raise ValueError("each method must return five distinct passages")
            ranked = []
            for rank, (pid, score) in enumerate(hits, 1):
                if (
                    pid not in passages
                    or passages[pid]["paper_id"] != question["paper_id"]
                    or not math.isfinite(score)
                ):
                    raise ValueError("invalid passage scope or score")
                if pid not in union:
                    passage = passages[pid]
                    title = passage["title"]
                    if not isinstance(title, str) or not title.strip():
                        raise ValueError("a real paper title is required")
                    union[pid] = {
                        "record_number": len(pairs) + len(union) + 1,
                        "question_id": question["question_id"],
                        "paper_id": question["paper_id"],
                        "source_split": question["source_split"],
                        "question": question["question"],
                        "paper_title": title,
                        "passage_id": pid,
                        "passage": passage["text"],
                        "label": None,
                        "retrieved_by": [],
                        "retrievals": [],
                    }
                row = union[pid]
                row["retrieved_by"].append(method)
                row["retrievals"].append(
                    {"method": method, "rank": rank, "score": float(score)}
                )
                ranked.append(
                    {
                        "passage_id": pid,
                        "record_number": row["record_number"],
                        "rank": rank,
                        "score": float(score),
                    }
                )
            rankings.append(
                {
                    "question_id": question["question_id"],
                    "method": method,
                    "hits": ranked,
                }
            )
        for row in union.values():
            row["display_group"] = (
                "Common Retrieved Chunks"
                if len(row["retrieved_by"]) > 1
                else row["retrieved_by"][0]
            )
        pairs.extend(union.values())
    return pairs, rankings


def join_gold(pairs: list[dict], gold: dict[str, dict]) -> list[dict]:
    """Attach reference evidence only after retrieval has completed.

    Args:
        pairs: Unique retrieved pairs with initially empty human labels.
        gold: Reference mapping for the selected development questions only.

    Returns:
        Separate verification rows; input pairs remain unchanged.
    """
    verification = []
    for row in pairs:
        reference = gold[row["question_id"]]
        if any(row[key] != reference[key] for key in ("paper_id", "question")):
            raise ValueError("query and gold reference disagree")
        verification.append(
            {
                **row,
                "gold_passage_ids": reference["gold_passage_ids"],
                "gold_evidence_match": row["passage_id"]
                in reference["gold_passage_ids"],
                "evidence_paragraphs": reference["evidence_paragraphs"],
            }
        )
    return verification


def render_multi_batches(
    rows: list[dict], output: Path, methods: tuple[str, ...] = METHODS
) -> None:
    """Export algorithm-disclosed views, grouping twenty questions per batch.

    Args:
        rows: Unique pair records with complete source attribution.
        output: New run directory; slot subdirectories must not already exist.
        methods: Frozen method order used for exclusive display groups.

    Gold, scores, ranks and internal IDs never enter this projection. Common
    pairs use stable record order; exclusive pairs use their source rank.
    """
    questions = {}
    for row in rows:
        questions.setdefault(row["question_id"], []).append(row)
    groups = list(questions.values())
    for slot in ("A", "B"):
        directory = output / f"annotator_{slot}"
        directory.mkdir()
        for start in range(0, len(groups), 20):
            lines = [
                "# Passage relevance annotation",
                "",
                "Annotator: ",
                "",
                "Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.",
                "",
                "0 — Not relevant",
                "",
                "1 — Relevant",
                "",
                "Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.",
                "",
            ]
            for number, question_rows in enumerate(
                groups[start : start + 20], start + 1
            ):
                first = question_rows[0]
                title = " ".join(first["paper_title"].splitlines())
                lines.extend(
                    [
                        f"## Question {number:04d}",
                        "",
                        f"Paper: {title}",
                        "",
                        *["> " + line for line in first["question"].splitlines()],
                        "",
                    ]
                )
                for group in ("Common Retrieved Chunks", *methods):
                    selected = [r for r in question_rows if r["display_group"] == group]
                    selected.sort(
                        key=lambda r: (
                            r["record_number"]
                            if group == "Common Retrieved Chunks"
                            else r["retrievals"][0]["rank"]
                        )
                    )
                    lines.extend([f"### {group}", ""])
                    if not selected:
                        lines.extend(["None", ""])
                    for row in selected:
                        number_id = row["record_number"]
                        lines.extend(
                            [
                                f"#### Passage {number_id}",
                                "",
                                "Retrieved by: " + ", ".join(row["retrieved_by"]),
                                "",
                                *["> " + line for line in row["passage"].splitlines()],
                                "",
                                f"#### Relevance {number_id}",
                                "",
                                "Label: ",
                                "",
                            ]
                        )
            with (directory / f"batch_{start // 20 + 1:02d}.md").open(
                "x", encoding="utf-8", newline="\n"
            ) as handle:
                handle.write("\n".join(lines))


def run_pilot(data: Path, config_path: Path, output: Path) -> None:
    """Run a development-only smoke test and persist a configuration freeze.

    Args:
        data: Existing processed data, including saved selection questions.
        config_path: Explicit configuration saved before the run.
        output: Independent version directory; existing output is refused.

    Only complete papers containing the first saved selection questions are
    indexed. This is equivalent to full-corpus paper-scoped retrieval. No
    held-out question list, query, label or result is opened by this runner.
    """
    if output.exists():
        raise FileExistsError(output)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if any(config[key] != SETTINGS[key] for key in SETTINGS):
        raise ValueError("pilot requires 365/40 and top-five")
    if (
        config["question_selection"]
        != "first saved development questions in persisted order"
    ):
        raise ValueError("unsupported development selection rule")
    count = config["question_count"]
    if type(count) is not int or not 1 <= count <= 10:
        raise ValueError("pilot question_count must be an integer in 1..10")
    settings = normalize_retrieval(config["retrieval"])
    if settings["mode"] != "hybrid":
        raise ValueError("pilot requires hybrid without reranking")
    saved = read_jsonl(data / "qa_for_choosing_chunk_size.jsonl")
    preparation = json.loads(
        (data / "annotation_preparation.manifest.json").read_text(encoding="utf-8")
    )
    development_path = (data / "qa_for_choosing_chunk_size.jsonl").as_posix()
    verify_snapshot({development_path: preparation["inputs"][development_path]})
    if len(unique_rows(saved, "question_id")) != 250:
        raise ValueError("expected the saved 250 development questions")
    questions = saved[:count]
    paper_ids = {q["paper_id"] for q in questions}
    corpus = [row for row in load_corpus(data) if row["paper_id"] in paper_ids]
    inputs = snapshot(
        [
            config_path,
            *[
                data / name
                for name in (
                    "qa_for_choosing_chunk_size.jsonl",
                    "annotation_preparation.manifest.json",
                    "passages_all_paper_text.jsonl",
                    "passages_all_paper_text.manifest.json",
                    "gold_evidence_mapping_all_splits.jsonl",
                    "gold_evidence_mapping_all_splits.manifest.json",
                    "papers.jsonl",
                    "qa.jsonl",
                    "qasper_export.manifest.json",
                )
            ],
        ]
    )
    pairs, rankings = pool_rankings(
        questions, corpus, build_retrievers(corpus, settings)
    )
    selected_ids = {q["question_id"] for q in questions}
    gold = unique_rows(
        [
            row
            for row in read_jsonl(data / "gold_evidence_mapping_all_splits.jsonl")
            if row["question_id"] in selected_ids
        ],
        "question_id",
    )
    verification = join_gold(pairs, gold)
    # Freeze the exact successful configuration before any future formal run.
    output.mkdir(parents=True)
    write_json(output / "frozen_config.json", config)
    write_jsonl(output / "questions.jsonl", questions)
    write_jsonl(output / "pairs.jsonl", pairs)
    write_jsonl(output / "rankings.jsonl", rankings)
    write_jsonl(output / "verification.jsonl", verification)
    render_multi_batches(pairs, output)
    write_json(
        output / "manifest.json",
        {
            "schema_version": "v0-proposed",
            "purpose": "development multi-retriever pilot; not held-out evaluation",
            "question_ids": [q["question_id"] for q in questions],
            "question_count": len(questions),
            "pair_count": len(pairs),
            "group_counts": dict(Counter(r["display_group"] for r in pairs)),
            "pair_counts_per_question": dict(Counter(r["question_id"] for r in pairs)),
            "indexed_paper_count": len(paper_ids),
            "indexed_passage_count": len(corpus),
            "settings": config,
            "code": code_identity(),
            "inputs": inputs,
            "retrievers": {
                method: retriever_metadata({**settings, "mode": mode})
                for method, mode in zip(METHODS, ("bm25", "dense", "hybrid"))
            },
            "configuration_status": "frozen for future expansion; no held-out-driven selection",
            "selection_rationale": "reuse existing pinned BGE/cosine and default RRF 20/60; feasibility smoke test, no quality-based parameter search",
            "record_number_scope": "this development pilot only; no historical formal record numbers modified",
            "outputs": snapshot(sorted(p for p in output.rglob("*") if p.is_file())),
            "validation": "five distinct valid same-paper hits per method; unique union; complete source ranks/scores; gold joined after retrieval; labels null; algorithm-disclosed Markdown without gold/scores/internal IDs",
        },
    )
