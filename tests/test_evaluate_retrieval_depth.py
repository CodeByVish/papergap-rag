"""Tests for the retrieval-depth evaluation (a plain static baseline at several top-k)."""

import pytest

from scripts import evaluate_retrieval_depth as script
from src.agent.experiments import ExperimentItem, depth_curve
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore


def hit(passage_id: str) -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=passage_id, paper_id="p", title="t", section="s",
                        chunk_number=0, text="text"),
        rank=1, source_scores={"bm25": SourceScore(rank=1, score=1.0)}, rrf_score=0.1,
    )


def ranked(*ids):
    """A retriever that returns the same ranked ids for every question, cut at top_k."""
    return lambda question, paper_id, top_k: [hit(i) for i in ids][:top_k]


def item(qid, gold):
    return ExperimentItem(qid, "q?", "p", frozenset(gold) if gold is not None else None, True)


def test_recall_grows_with_depth_and_counts_full_recall():
    items = [item("a", {"g1"}), item("b", {"g2", "g3"})]
    retriever = ranked("x", "g1", "y", "g2", "z", "g3")
    curve = depth_curve(items, retriever, [2, 4, 6])
    assert curve["questions_with_gold"] == 2
    assert curve["recall_at_k"] == {"2": pytest.approx(0.5), "4": pytest.approx(0.75), "6": 1.0}
    assert curve["full_recall_at_k"] == {"2": 1, "4": 1, "6": 2}


def test_oracle_stops_at_the_first_depth_that_has_all_gold():
    items = [item("a", {"g1"}), item("b", {"g2", "g3"}), item("c", {"never"})]
    curve = depth_curve(items, ranked("x", "g1", "y", "g2", "z", "g3"), [2, 4, 6])
    # a stops at 2; b needs 6; c never completes so it reads the deepest and keeps recall 0
    assert curve["oracle"]["mean_passages"] == pytest.approx((2 + 6 + 6) / 3)
    assert curve["oracle"]["mean_recall"] == pytest.approx((1 + 1 + 0) / 3)


def test_questions_without_gold_are_skipped_and_ks_are_validated():
    curve = depth_curve([item("a", None), item("b", set())], ranked("x"), [3, 1])
    assert curve["questions_with_gold"] == 0 and list(curve["recall_at_k"]) == ["1", "3"]
    with pytest.raises(ValueError):
        depth_curve([], ranked("x"), [])
    with pytest.raises(ValueError):
        depth_curve([], ranked("x"), [0, 5])


def test_retriever_is_asked_once_per_question_at_the_deepest_k():
    asked = []

    def retriever(question, paper_id, top_k):
        asked.append(top_k)
        return [hit("g")]

    depth_curve([item("a", {"g"}), item("b", {"g"})], retriever, [3, 8, 5])
    assert asked == [8, 8]


def test_script_refuses_depths_beyond_the_candidate_pool(capsys):
    base = ["--passages", "p.jsonl", "--dense-index-dir", "d", "--items", "i.jsonl"]
    assert script.parse_args([*base, "--ks", "5", "10"]).scoped is False
    with pytest.raises(SystemExit):
        script.parse_args([*base, "--ks", "5", "25", "--candidate-k", "20"])
    assert "candidate-k" in capsys.readouterr().err


def test_table_lists_every_depth_and_the_oracle():
    curve = depth_curve([item("a", {"g1"})], ranked("x", "g1"), [1, 2])
    text = script.format_curve(curve)
    assert "| 1 | 0.000 | 0/1 |" in text and "| 2 | 1.000 | 1/1 |" in text
    assert "oracle stop: 2.00 passages" in text
