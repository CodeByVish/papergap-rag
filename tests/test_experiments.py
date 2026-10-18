"""Tests for the static-vs-adaptive experiment harness."""

import json

import pytest

from src.agent.experiments import (
    ExperimentItem,
    compute_metrics,
    default_refuses,
    format_table,
    paired_recall_gain,
    run_system,
)
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore


def passage(passage_id, section="Method", text="We encode passages.") -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=passage_id, paper_id="p", title="t", section=section,
                        chunk_number=0, text=text),
        rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)},
        rrf_score=0.1,
    )


METHOD = passage("method")
GOLD = passage("gold", "Results", "Our model achieves 82.4 F1 and 91% accuracy.")
EXTRA = passage("extra", "Setup", "A held-out dataset.")


def retriever(query, paper_id, top_k):
    """Finds the gold passage only after the query is rewritten towards results."""
    return [METHOD, GOLD] if "results" in query.lower() else [METHOD]


class OracleCritic:
    """Says sufficient exactly when the gold passage is in the prompt."""

    def complete(self, prompt: str) -> str:
        if "[gold]" in prompt:
            return json.dumps({"sufficient": True, "gap_label": "NONE",
                               "missing_components": [], "reason": "Result found."})
        return json.dumps({"sufficient": False, "gap_label": "MISSING_RESULT",
                           "missing_components": ["reported result"], "reason": "No result."})


ITEMS = [
    ExperimentItem("q1", "What accuracy did the model achieve?", "p", frozenset({"gold"}), True),
    ExperimentItem("q2", "What F1 did it get?", "p", frozenset({"method"}), True),
    ExperimentItem("q3", "Who funded the study?", "p", None, False),
]


@pytest.fixture(scope="module")
def static_records():
    return run_system(ITEMS, retriever, adaptive=False)


@pytest.fixture(scope="module")
def adaptive_records():
    return run_system(ITEMS, retriever, adaptive=True, critic_client=OracleCritic())


def test_static_never_retries_or_calls_the_llm(static_records):
    assert [r["retrieval_round"] for r in static_records] == [1, 1, 1]
    assert {e["source"] for r in static_records for e in r["critic_log"]} == {"rules"}


def test_adaptive_retries_until_gold_is_found(adaptive_records):
    q1 = adaptive_records[0]
    assert q1["retrieval_round"] == 2 and q1["sufficient"] is True
    assert {p["passage"]["passage_id"] for p in q1["retrieved_passages"]} == {"method", "gold"}


def test_metrics_static(static_records):
    m = compute_metrics(static_records, ITEMS)
    assert m["questions"] == 3 and m["errors"] == 0
    assert m["mean_rounds"] == 1
    assert m["questions_with_gold"] == 2
    assert m["recall_before_retries"] == m["recall_after_retries"] == 0.5
    assert m["retries"] == 0 and m["unnecessary_retry_rate"] is None


def test_metrics_adaptive_shows_recovery_and_retry_quality(adaptive_records):
    m = compute_metrics(adaptive_records, ITEMS)
    assert m["recall_before_retries"] == 0.5 and m["recall_after_retries"] == 1.0
    assert m["full_recall_recovery_rate"] == 1.0  # q1 went 0 -> 1
    # The rewritten query surfaces the gold passage for all three questions, so each
    # starts insufficient, retries once, and ends sufficient.
    assert m["gap_detected"] == 3 and m["critic_gap_recovery_rate"] == 1.0
    assert m["retries"] == 3 and m["mean_rounds"] == 2
    assert m["critic_llm_rate"] == 1.0 and m["critic_fallback_rate"] == 0.0


def test_unnecessary_and_ineffective_retries_counted_against_gold(adaptive_records):
    # q1 and q2 have gold. q1's retry found its gold; q2's gold ("method") was already
    # complete after round 1, so its retry was both unnecessary and ineffective.
    m = compute_metrics(adaptive_records, ITEMS)
    assert m["unnecessary_retry_rate"] == pytest.approx(1 / 2)
    assert m["ineffective_retry_rate"] == pytest.approx(1 / 2)
    assert m["redundant_retry_rate"] == 0  # every retry returned a new passage


def test_redundant_retries_when_retrieval_never_changes():
    def stuck(query, paper_id, top_k):
        return [METHOD]

    records = run_system(ITEMS, stuck, adaptive=True, critic_client=OracleCritic())
    m = compute_metrics(records, ITEMS)
    assert m["mean_rounds"] == 3 and m["retries"] == 6
    assert m["redundant_retry_rate"] == 1.0
    assert m["critic_gap_recovery_rate"] == 0.0


def test_refusal_rates_use_answerability_labels():
    def nothing(query, paper_id, top_k):
        return []

    records = run_system(ITEMS, nothing, adaptive=False)
    m = compute_metrics(records, ITEMS)
    assert m["refusal_rate"] == 1.0
    assert m["correct_refusal_rate"] == 1.0  # q3 is unanswerable and refused
    assert m["false_refusal_rate"] == 1.0  # q1, q2 answerable but refused
    assert default_refuses(records[0]) is True


def test_errors_are_recorded_and_do_not_stop_the_run():
    def flaky(query, paper_id, top_k):
        if "F1" in query:
            raise RuntimeError("index offline")
        return [METHOD]

    records = run_system(ITEMS, flaky, adaptive=False)
    assert "error" in records[1] and "RuntimeError" in records[1]["error"]
    m = compute_metrics(records, ITEMS)
    assert m["questions"] == 3 and m["errors"] == 1 and m["mean_rounds"] == 1


def test_metrics_without_gold_report_none_for_recall():
    items = [ExperimentItem("q1", "What accuracy?", "p")]
    m = compute_metrics(run_system(items, retriever, adaptive=False), items)
    assert m["recall_before_retries"] is None and m["refusal_rate"] == 0.0


def test_paired_gain_and_deterministic_ci(static_records, adaptive_records):
    first = paired_recall_gain(static_records, adaptive_records, ITEMS)
    again = paired_recall_gain(static_records, adaptive_records, ITEMS)
    assert first == again
    assert first["n"] == 2 and first["mean_gain"] == pytest.approx(0.5)  # q1 +1, q2 0
    low, high = first["ci95"]
    assert low <= first["mean_gain"] <= high


def test_paired_gain_with_no_gold_is_empty():
    items = [ExperimentItem("q1", "x", "p")]
    records = run_system(items, retriever, adaptive=False)
    assert paired_recall_gain(records, records, items) == {"n": 0, "mean_gain": None, "ci95": None}


def test_metrics_can_be_recomputed_from_saved_jsonl(adaptive_records):
    reloaded = [json.loads(json.dumps(r)) for r in adaptive_records]
    assert compute_metrics(reloaded, ITEMS) == compute_metrics(adaptive_records, ITEMS)


def test_format_table(static_records, adaptive_records):
    table = format_table({
        "static": compute_metrics(static_records, ITEMS),
        "adaptive": compute_metrics(adaptive_records, ITEMS),
    })
    lines = table.splitlines()
    assert lines[0] == "| metric | static | adaptive |"
    assert any(line.startswith("| mean_rounds | 1.000 |") for line in lines)
    assert "n/a" in table
