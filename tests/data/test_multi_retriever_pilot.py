"""Verify union semantics and annotation projection without model downloads.

Synthetic rankings exercise two-way and three-way overlaps, exclusive results,
and invalid backends independently of the real development smoke run.
"""

from pathlib import Path

import pytest

from src.data.build_multi_retriever_pilot import (
    METHODS,
    join_gold,
    pool_rankings,
    render_multi_batches,
)


def fixture_pool() -> tuple:
    """Construct rankings with all common/exclusive membership patterns.

    Returns:
        Questions, corpus, callbacks and gold references with private markers.
    """
    questions = [
        {
            "question_id": "secret_q",
            "paper_id": "secret_paper",
            "question": "Question?",
            "source_split": "train",
        }
    ]
    corpus = [
        {
            "passage_id": f"secret_p{i}",
            "paper_id": "secret_paper",
            "text": f"Text {i}\n### Source heading",
            "title": "Real title",
        }
        for i in range(9)
    ]
    memberships = ((0, 1, 2, 3, 4), (0, 1, 5, 6, 7), (0, 2, 5, 7, 8))

    def callback(ids: tuple) -> object:
        """Capture one ranking without exposing any evidence to retrieval.

        Args:
            ids: Synthetic passage suffixes in original rank order.

        Returns:
            Backend callback that checks the shared query contract.
        """

        def retrieve(query: str, paper_id: str, count: int) -> list:
            """Return deterministic scores for the requested paper only.

            Args:
                query: Expected original question.
                paper_id: Expected selected-paper identifier.
                count: Expected top-five depth.

            Returns:
                Five ranked synthetic hits.
            """
            assert (query, paper_id, count) == ("Question?", "secret_paper", 5)
            return [(f"secret_p{i}", float(5 - rank)) for rank, i in enumerate(ids)]

        return retrieve

    retrievers = dict(zip(METHODS, map(callback, memberships)))
    gold = {
        "secret_q": {
            **questions[0],
            "gold_passage_ids": ["secret_p0"],
            "evidence_paragraphs": [{"text": "secret_evidence"}],
        }
    }
    return questions, corpus, retrievers, gold


def test_union_preserves_all_ranks_and_separate_gold(tmp_path: Path) -> None:
    """Retain one pair per union member and hide evaluation-only fields.

    All original ranks survive grouping; the two templates remain identical
    until distinct people supply their own independent judgments.
    """
    questions, corpus, retrievers, gold = fixture_pool()
    pairs, rankings = pool_rankings(questions, corpus, retrievers)
    assert len(pairs) == 9
    assert [row["record_number"] for row in pairs] == list(range(1, 10))
    assert len(rankings) == 3
    for ranking in rankings:
        assert [hit["rank"] for hit in ranking["hits"]] == [1, 2, 3, 4, 5]
        for hit in ranking["hits"]:
            pair = pairs[hit["record_number"] - 1]
            assert pair["passage_id"] == hit["passage_id"]
            assert {
                "method": ranking["method"],
                "rank": hit["rank"],
                "score": hit["score"],
            } in pair["retrievals"]
    assert pairs[0]["retrieved_by"] == list(METHODS)
    assert pairs[1]["retrieved_by"] == ["BM25", "Dense"]
    verification = join_gold(pairs, gold)
    assert sum(r["gold_evidence_match"] for r in verification) == 1
    assert all(r["label"] is None and "gold_passage_ids" not in r for r in pairs)
    render_multi_batches(pairs, tmp_path)
    text = (tmp_path / "annotator_A/batch_01.md").read_text(encoding="utf-8")
    assert text == (tmp_path / "annotator_B/batch_01.md").read_text(encoding="utf-8")
    assert text.count("\n#### Passage ") == text.count("\nLabel: \n") == 9
    assert text.count("\n## Question ") == 1
    assert "Retrieved by: BM25, Dense, Hybrid" in text
    assert all(
        f"### {group}" in text for group in ("Common Retrieved Chunks", *METHODS)
    )
    assert "> ### Source heading" in text
    assert all(value not in text for value in ("secret_", "score", "gold_", "Notes"))


@pytest.mark.parametrize("fault", ["duplicate", "missing", "foreign", "nan"])
def test_invalid_backend_is_rejected(fault: str) -> None:
    """Reject malformed hits instead of silently padding or deduplicating.

    Args:
        fault: Backend contract violation to inject into one top-five list.
    """
    questions, corpus, retrievers, _ = fixture_pool()
    hits = retrievers["BM25"]("Question?", "secret_paper", 5)
    if fault == "duplicate":
        hits[-1] = hits[0]
    elif fault == "missing":
        hits.pop()
    elif fault == "foreign":
        corpus[0]["paper_id"] = "other_paper"
    else:
        hits[0] = (hits[0][0], float("nan"))
    retrievers["BM25"] = lambda *_: hits
    with pytest.raises(ValueError):
        pool_rankings(questions, corpus, retrievers)


def test_question_batches_and_empty_sections(tmp_path: Path) -> None:
    """Keep variable-size question unions intact across twenty-question batches.

    Fully common rankings produce explicit None entries for all exclusive groups.
    """
    questions, corpus, retrievers, _ = fixture_pool()
    retrievers = {method: retrievers["BM25"] for method in METHODS}
    questions = [{**questions[0], "question_id": f"q{i}"} for i in range(21)]
    pairs, _ = pool_rankings(questions, corpus, retrievers)
    render_multi_batches(pairs, tmp_path)
    paths = sorted((tmp_path / "annotator_A").glob("*.md"))
    first, last = [path.read_text(encoding="utf-8") for path in paths]
    assert first.count("\n## Question ") == 20
    assert first.count("\n#### Passage ") == 100
    assert "## Question 0021" in last
    assert last.count("\n#### Passage ") == 5
    assert last.count("\nNone\n") == 3
