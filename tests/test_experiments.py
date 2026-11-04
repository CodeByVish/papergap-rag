"""Tests for the static-vs-adaptive experiment harness."""

import json
import re

import pytest

from src.agent.experiments import (
    ExperimentItem,
    compute_metrics,
    default_refuses,
    depth_recall,
    format_baseline_section,
    format_table,
    matched_recall_gain,
    paired_recall_gain,
    refusal_rule_check,
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
    """Finds the gold passage only after the query is rewritten towards results (the critic's "reported result")."""
    return [METHOD, GOLD] if "result" in query.lower() else [METHOD]


class OracleCritic:
    """Says sufficient exactly when the gold passage is in the prompt."""

    def complete(self, prompt: str) -> str:
        found = re.search(r"\[(p\d+)\] section: Results\n[^\n]*91% accuracy", prompt)
        if found:
            return json.dumps({"sufficient": True, "gap_label": "NONE",
                               "missing_components": [], "reason": "Result found.",
                               "supporting_passage_ids": [found.group(1)],
                               "evidence_quote": "Our model achieves 82.4 F1 and 91% accuracy"})
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
    assert m["critic_reused_rate"] == 0.0


def test_unsatisfied_rates_price_the_refuse_if_unsatisfied_rule(adaptive_records):
    m = compute_metrics(adaptive_records, ITEMS)
    # every adaptive question ends sufficient here, so that rule would refuse nothing
    assert m["unsatisfied_rate_answerable"] == 0.0
    assert m["unsatisfied_rate_unanswerable"] == 0.0


def test_unsatisfied_rates_split_by_answerability():
    def record(qid, sufficient):
        return {"question_id": qid, "paper_id": "p", "question": "?", "retrieval_round": 3,
                "sufficient": sufficient, "gap_label": "MISSING_RESULT", "elapsed_s": 1.0,
                "retrieval_log": [], "retrieved_passages": [{}], "critic_log": []}

    items = [ExperimentItem("a", "?", "p", frozenset({"g"}), True),
             ExperimentItem("b", "?", "p", frozenset({"g"}), True),
             ExperimentItem("c", "?", "p", None, False)]
    m = compute_metrics([record("a", True), record("b", False), record("c", False)], items)
    assert m["unsatisfied_rate_answerable"] == 0.5 and m["unsatisfied_rate_unanswerable"] == 1.0


def test_reused_verdicts_are_counted_apart_from_model_calls():
    entry = lambda source: {"round": 1, "source": source, "sufficient": False,
                            "gap_label": "MISSING_RESULT", "errors": [], "raw_replies": []}
    record = {"question_id": "q1", "paper_id": "p", "question": "?", "retrieval_round": 3,
              "sufficient": False, "gap_label": "MISSING_RESULT", "elapsed_s": 1.0,
              "retrieval_log": [], "retrieved_passages": [],
              "critic_log": [entry("llm"), entry("reused"), entry("reused")]}
    items = [ExperimentItem(question_id="q1", question="?", paper_id="p")]
    m = compute_metrics([record], items)
    assert m["critic_reused_rate"] == pytest.approx(2 / 3)
    assert m["critic_llm_rate"] == 1.0  # of the calls that asked the model


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


def wide_retriever(query, paper_id, top_k):
    """Ranks the gold passage last of three, so only a wide static run reaches it."""
    return [METHOD, EXTRA, GOLD][:top_k]


def test_matched_gain_credits_only_what_extra_passages_cannot_explain(adaptive_records):
    # Adaptive ends with [method, gold] for q1: two passages. Static top-2 of the wide
    # ranking is [method, extra], which misses gold, so the retry still earns its gain.
    wide = run_system(ITEMS, wide_retriever, adaptive=False, top_k=3)
    result = matched_recall_gain(wide, adaptive_records, ITEMS)
    assert result["n"] == 2 and result["mean_budget"] == pytest.approx(2.0)
    assert result["mean_gain"] == pytest.approx(0.5)  # q1 +1, q2 0

    # Once the static run ranks gold within the same budget, there is nothing left to credit.
    wide_all = run_system(ITEMS, lambda q, p, k: [METHOD, GOLD], adaptive=False)
    assert matched_recall_gain(wide_all, adaptive_records, ITEMS)["mean_gain"] == pytest.approx(0.0)


def test_matched_gain_with_no_gold_is_empty():
    items = [ExperimentItem("q1", "x", "p")]
    records = run_system(items, retriever, adaptive=False)
    result = matched_recall_gain(records, records, items)
    assert result["n"] == 0 and result["mean_gain"] is None and result["mean_budget"] is None


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


def test_answer_fn_gets_the_exported_record_and_runs_for_both_arms():
    seen = []

    def answer_fn(record):
        seen.append((record["question_id"], len(record["retrieved_passages"])))
        return {"answer": f"for {record['question_id']}", "refused": False}

    static = run_system(ITEMS, retriever, adaptive=False, answer_fn=answer_fn)
    adaptive = run_system(ITEMS, retriever, adaptive=True, critic_client=OracleCritic(),
                          answer_fn=answer_fn)
    assert [r["answer"]["answer"] for r in static] == ["for q1", "for q2", "for q3"]
    assert all("answer_s" in r and "answer_error" not in r for r in adaptive)
    # Same question ids in both arms; the adaptive arm handed over more passages for q1.
    assert [qid for qid, _ in seen[:3]] == [qid for qid, _ in seen[3:]]
    assert seen[3][1] > seen[0][1]
    json.dumps(adaptive)  # records stay JSON-safe with answers attached


def test_answer_errors_are_recorded_and_counted_without_stopping_the_run():
    def flaky(record):
        if record["question_id"] == "q2":
            raise RuntimeError("model OOM")
        return {"answer": "ok"}

    records = run_system(ITEMS, retriever, adaptive=False, answer_fn=flaky)
    assert "RuntimeError" in records[1]["answer_error"] and "answer" not in records[1]
    assert records[0]["answer"] == {"answer": "ok"} and records[2]["answer"] == {"answer": "ok"}
    assert compute_metrics(records, ITEMS)["answer_errors"] == 1


def test_without_answer_fn_records_have_no_answer_keys(static_records):
    assert all("answer" not in r and "answer_s" not in r for r in static_records)


def test_on_record_sees_every_record_in_order_including_errors():
    def flaky(query, paper_id, top_k):
        if "F1" in query:
            raise RuntimeError("index offline")
        return [METHOD]

    seen = []
    records = run_system(ITEMS, flaky, adaptive=False, on_record=seen.append)
    assert [r["question_id"] for r in seen] == ["q1", "q2", "q3"]
    assert seen == records and "error" in seen[1]


# --- the static baseline at every depth, and the refusal rule's price -------

def ranked_record(qid, *ids):
    return {"question_id": qid, "retrieved_passages": [{"passage": {"passage_id": i}} for i in ids]}


def test_depth_recall_cuts_one_ranking_at_every_depth():
    items = [ExperimentItem("a", "?", "p", frozenset({"g1"}), True),
             ExperimentItem("b", "?", "p", frozenset({"g2", "g3"}), True),
             ExperimentItem("c", "?", "p", None, False)]
    records = [ranked_record("a", "x", "g1", "y", "z", "w", "v"),
               ranked_record("b", "g2", "x", "y", "g3", "z", "w"),
               ranked_record("c", "x", "y")]
    out = depth_recall(records, items, ks=[1, 2, 4, 6, 10])
    assert out["questions_with_gold"] == 2
    assert out["recall_at_k"] == {"1": 0.25, "2": 0.75, "4": 1.0, "6": 1.0}  # no ranking reaches 10
    assert out["full_recall_at_k"] == {"1": 0, "2": 1, "4": 2, "6": 2}


def test_depth_recall_lets_a_short_paper_contribute_all_it_has():
    items = [ExperimentItem("a", "?", "p", frozenset({"g"}), True),
             ExperimentItem("b", "?", "p", frozenset({"h"}), True)]
    records = [ranked_record("a", "g", "x"), ranked_record("b", "x", "y", "z", "w", "h")]
    assert depth_recall(records, items, ks=[2, 5])["recall_at_k"] == {"2": 0.5, "5": 1.0}


def test_refusal_rule_check_applies_the_proposed_gate():
    ok = refusal_rule_check({"unsatisfied_rate_unanswerable": 0.6, "unsatisfied_rate_answerable": 0.03})
    assert ok["meets_proposed_gate"] is True
    too_many_false = refusal_rule_check({"unsatisfied_rate_unanswerable": 1.0,
                                         "unsatisfied_rate_answerable": 0.375})
    assert too_many_false["meets_proposed_gate"] is False
    too_few_caught = refusal_rule_check({"unsatisfied_rate_unanswerable": 0.25,
                                         "unsatisfied_rate_answerable": 0.0})
    assert too_few_caught["meets_proposed_gate"] is False
    assert refusal_rule_check({"unsatisfied_rate_unanswerable": None,
                               "unsatisfied_rate_answerable": 0.0})["meets_proposed_gate"] is False


def test_baseline_section_lists_depths_adaptive_and_the_refusal_check():
    summary = {
        "metrics": {"adaptive": {"mean_passages": 5.5, "recall_after_retries": 0.8}},
        "static_depth_recall": {"questions_with_gold": 10, "recall_at_k": {"5": 0.7, "10": 0.9},
                                "full_recall_at_k": {"5": 6, "10": 9}},
        "refuse_if_unsatisfied": {"correct_refusal_rate": 0.5, "false_refusal_rate": 0.1,
                                  "meets_proposed_gate": False},
    }
    text = format_baseline_section(summary)
    assert "| 5 | 0.700 | 6/10 |" in text and "| 10 | 0.900 | 9/10 |" in text
    assert "adaptive, 5.50 passages on average | 0.800" in text
    assert "not enabled" in text and "meets the proposed gate" in text and "False" in text
    assert format_baseline_section({"metrics": {}}) == ""
