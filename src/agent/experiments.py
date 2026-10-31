"""Static-vs-adaptive experiment harness (P4, Weeks 6-7).

Runs the agent over a fixed list of questions under different settings and
computes the P4 measures from docs/EXECUTION_PLAN.md: evidence recall before and
after retries, average retrieval rounds, gap recovery, unnecessary retries and
refusal behaviour.

Everything is computed from exported records (`src/agent/export.py`), so metrics
can be recomputed from saved JSONL without re-running the agent. Recall needs the
gold evidence mapped to passage IDs (P3's mapping); questions without it are
skipped for recall metrics only.

Systems:
    static    one retrieval round, rule-based critic, no retries (plan system F)
    adaptive  up to MAX_RETRIES retries driven by the critic (plan system G)
"""

from __future__ import annotations

import random
import time
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from typing import Any

from src.agent.critic import CriticClient
from src.agent.export import export_record
from src.agent.graph import build_agent_graph
from src.agent.nodes import DEFAULT_TOP_K, MAX_RETRIES, Retriever, SectionSelector
from src.agent.schemas import AgentState, GapLabel

AnswerFn = Callable[[dict[str, Any]], dict[str, Any]]
"""`answer_fn(record) -> answer`: P5's generation step. It receives the exported
agent record (`src/agent/export.py`, passages with text included) and returns a
JSON-safe dict, stored as `record["answer"]`. Both arms get the same function."""


@dataclass(frozen=True)
class ExperimentItem:
    """One evaluation question. `gold_passage_ids` and `answerable` may be unknown."""

    question_id: str
    question: str
    paper_id: str
    gold_passage_ids: frozenset[str] | None = None
    answerable: bool | None = None


def run_system(
    items: Iterable[ExperimentItem],
    retriever: Retriever,
    *,
    adaptive: bool,
    critic_client: CriticClient | None = None,
    max_retries: int = MAX_RETRIES,
    top_k: int = DEFAULT_TOP_K,
    answer_fn: AnswerFn | None = None,
    on_record: Callable[[dict[str, Any]], None] | None = None,
    section_selector: SectionSelector | None = None,
) -> list[dict[str, Any]]:
    """Run every item and return one exported record each.

    The static system never retries and never calls the LLM critic. A failure on
    one question is recorded as `{"question_id", "error"}` and does not stop the run.
    With `answer_fn`, each successful record also gets `answer` (or `answer_error`
    if generation raised) and `answer_s`; `elapsed_s` still times the agent alone.
    `on_record` is called with each finished record (including error records) so a
    long job can write results as it goes and survive being killed.
    `section_selector` scopes the adaptive arm's retries (src/agent/sections.py).
    """
    graph = build_agent_graph(
        retriever,
        max_retries=max_retries if adaptive else 0,
        top_k=top_k,
        critic_client=critic_client if adaptive else None,
        section_selector=section_selector if adaptive else None,
    )
    records = []
    for item in items:
        started = time.perf_counter()
        try:
            result = graph.invoke(
                AgentState(
                    question=item.question,
                    paper_id=item.paper_id,
                    question_id=item.question_id,
                )
            )
        except Exception as error:  # noqa: BLE001 - keep a long run going
            failed = {"question_id": item.question_id, "error": f"{type(error).__name__}: {error}"}
            records.append(failed)
            if on_record is not None:
                on_record(failed)
            continue
        record = export_record(result)
        record["elapsed_s"] = time.perf_counter() - started
        if answer_fn is not None:
            answer_started = time.perf_counter()
            try:
                record["answer"] = answer_fn(record)
            except Exception as error:  # noqa: BLE001 - keep a long run going
                record["answer_error"] = f"{type(error).__name__}: {error}"
            record["answer_s"] = time.perf_counter() - answer_started
        records.append(record)
        if on_record is not None:
            on_record(record)
    return records


def default_refuses(record: dict[str, Any]) -> bool:
    """Proposed refusal rule: the critic says the paper cannot answer, or nothing was found."""
    return (
        record["gap_label"] == GapLabel.INSUFFICIENT_INFORMATION.value
        or not record["retrieved_passages"]
    )


def _recall(gold: frozenset[str], found: set[str]) -> float:
    return len(gold & found) / len(gold)


def _round_passage_ids(record: dict[str, Any]) -> list[set[str]]:
    """Cumulative passage IDs after each retrieval round."""
    cumulative: set[str] = set()
    out = []
    for entry in record["retrieval_log"]:
        cumulative = cumulative | set(entry["passage_ids"])
        out.append(set(cumulative))
    return out


def _mean(values: Sequence[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def compute_metrics(
    records: Sequence[dict[str, Any]],
    items: Iterable[ExperimentItem],
    refuses: Callable[[dict[str, Any]], bool] = default_refuses,
) -> dict[str, Any]:
    """Aggregate the P4 measures for one system. Missing inputs give `None`.

    A retry is *unnecessary* when all gold evidence was already retrieved, and
    *ineffective* when it added no new gold passage (so unnecessary retries are
    also ineffective). A retry is *redundant* when it returned nothing new at all.
    """
    by_id = {item.question_id: item for item in items}
    ok = [r for r in records if "error" not in r]

    rounds = [r["retrieval_round"] for r in ok]
    first_gap = [r for r in ok if r["critic_log"] and not r["critic_log"][0]["sufficient"]]
    recovered_by_critic = [r for r in first_gap if r["sufficient"]]

    recall_before, recall_after, recovered, improvable = [], [], 0, 0
    retries = gold_retries = unnecessary = ineffective = redundant = 0
    for record in ok:
        per_round = _round_passage_ids(record)
        previous = per_round[0] if per_round else set()
        gold = by_id[record["question_id"]].gold_passage_ids
        for later in per_round[1:]:
            retries += 1
            redundant += later == previous
            if gold:
                gold_retries += 1
                unnecessary += _recall(gold, previous) == 1.0
                ineffective += (gold & later) == (gold & previous)
            previous = later
        if not gold or not per_round:
            continue
        before, after = _recall(gold, per_round[0]), _recall(gold, per_round[-1])
        recall_before.append(before)
        recall_after.append(after)
        if before < 1.0:
            improvable += 1
            recovered += after == 1.0
    with_gold = len(recall_before)

    answerable = [r for r in ok if by_id[r["question_id"]].answerable is True]
    unanswerable = [r for r in ok if by_id[r["question_id"]].answerable is False]
    critic_entries = [e for r in ok for e in r["critic_log"]]

    return {
        "questions": len(records),
        "errors": len(records) - len(ok),
        "answer_errors": sum("answer_error" in r for r in ok),
        "mean_rounds": _mean(rounds),
        "questions_with_gold": with_gold,
        "recall_before_retries": _mean(recall_before),
        "recall_after_retries": _mean(recall_after),
        "full_recall_recovery_rate": _rate(recovered, improvable),
        "gap_detected": len(first_gap),
        "critic_gap_recovery_rate": _rate(len(recovered_by_critic), len(first_gap)),
        "retries": retries,
        "unnecessary_retry_rate": _rate(unnecessary, gold_retries),
        "ineffective_retry_rate": _rate(ineffective, gold_retries),
        "redundant_retry_rate": _rate(redundant, retries),
        "refusal_rate": _rate(sum(refuses(r) for r in ok), len(ok)),
        "correct_refusal_rate": _rate(sum(refuses(r) for r in unanswerable), len(unanswerable)),
        "false_refusal_rate": _rate(sum(refuses(r) for r in answerable), len(answerable)),
        "critic_llm_rate": _rate(sum(e["source"] == "llm" for e in critic_entries), len(critic_entries)),
        "critic_fallback_rate": _rate(
            sum(e["source"] == "fallback" for e in critic_entries), len(critic_entries)
        ),
        "critic_thinking_drift_rate": _rate(
            sum(bool(e.get("thinking_drift")) for e in critic_entries), len(critic_entries)
        ),
        "mean_elapsed_s": _mean([r["elapsed_s"] for r in ok if "elapsed_s" in r]),
    }


def paired_recall_gain(
    static: Sequence[dict[str, Any]],
    adaptive: Sequence[dict[str, Any]],
    items: Iterable[ExperimentItem],
    *,
    resamples: int = 2000,
    seed: int = 0,
) -> dict[str, Any]:
    """Mean per-question final-recall gain of adaptive over static, with a bootstrap 95% CI.

    Only questions with gold evidence that ran without error in both systems count.
    """
    by_id = {item.question_id: item for item in items}
    final_static = {r["question_id"]: r for r in static if "error" not in r}
    diffs = []
    for record in adaptive:
        qid = record["question_id"]
        gold = by_id[qid].gold_passage_ids
        if "error" in record or not gold or qid not in final_static:
            continue

        def final_recall(rec: dict[str, Any], gold: frozenset[str] = gold) -> float:
            return _recall(gold, {p["passage"]["passage_id"] for p in rec["retrieved_passages"]})

        diffs.append(final_recall(record) - final_recall(final_static[qid]))
    if not diffs:
        return {"n": 0, "mean_gain": None, "ci95": None}
    rng = random.Random(seed)
    means = sorted(
        sum(rng.choices(diffs, k=len(diffs))) / len(diffs) for _ in range(resamples)
    )
    low, high = means[int(0.025 * resamples)], means[int(0.975 * resamples) - 1]
    return {"n": len(diffs), "mean_gain": sum(diffs) / len(diffs), "ci95": (low, high)}


def format_table(results: dict[str, dict[str, Any]]) -> str:
    """Markdown table: one row per metric, one column per system."""
    systems = list(results)
    metrics = list(next(iter(results.values())))

    def cell(value: Any) -> str:
        if value is None:
            return "n/a"
        return f"{value:.3f}" if isinstance(value, float) else str(value)

    lines = ["| metric | " + " | ".join(systems) + " |", "| --- |" + " ---: |" * len(systems)]
    lines += [
        f"| {metric} | " + " | ".join(cell(results[s][metric]) for s in systems) + " |"
        for metric in metrics
    ]
    return "\n".join(lines)
