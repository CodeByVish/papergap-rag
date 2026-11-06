"""Live-demo entry point: one free-form question in, one full agent record out.

P5's demo server answers a typed question by calling a hook and passing the
returned record to `answer_record`. This hook runs the whole agent (planner,
retrieval rounds, critic, rewriter) instead of a single retrieval, so the answer
carries the same `retrieval_round`, `gap_label` and `critic_log` as a scored run.

The critic shares P5's generator: the server owns the one vLLM engine an A40 can
hold, so nothing here loads a model.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Callable

from src.agent.critic import CriticClient, PassageView, pool_view
from src.agent.export import export_record
from src.agent.graph import build_agent_graph
from src.agent.nodes import Retriever, SectionSelector
from src.agent.schemas import AgentState

LOGGER = logging.getLogger(__name__)

#: Receives one plain-language line per agent step, with the UI step it describes
#: and the step that runs next, for a live progress view.
ProgressFn = Callable[[str, str, str], None]

#: node -> (step described, step active afterwards).
NODE_STEPS = {
    "plan_question": ("plan", "search"),
    "retrieve": ("search", "check"),
    "map_evidence": ("search", "check"),
    "critic": ("check", "check"),
    "rewrite_query": ("search", "search"),
    "finish": ("check", "write"),
}

#: `record_fn(question, paper_id, top_k, request_id=None) -> exported agent record`.
RecordFn = Callable[..., dict[str, Any]]


CRITIC_SOURCES = {
    "llm": "model",
    "rules": "rules",
    "fallback": "rules, after the model reply failed",
    "reused": "previous verdict reused, same passages",
}


def describe_step(node: str, update: dict[str, Any], pool: int) -> str | None:
    """One factual line for a finished step; None when the step has nothing to report.

    `pool` is the evidence pool's size before this step. Lines report recorded values
    only. The words after a full stop name the step that always follows.
    """
    if node == "plan_question":
        kind = getattr(update.get("question_type"), "value", update.get("question_type"))
        needs = ", ".join(update.get("required_components") or []) or "no listed components"
        return f"Planned: {kind} question, needs {needs}. Searching..."
    if node == "retrieve":
        last = (update.get("retrieval_log") or [{}])[-1]
        merged = len(update.get("retrieved_passages") or [])
        where = f" in section '{last['section']}'" if last.get("section") else ""
        fallback = " (section empty, searched everything instead)" if last.get("scope_fallback") else ""
        return (
            f"Round {last.get('round', '?')}{where}{fallback}: kept "
            f"{len(last.get('passage_ids') or [])} passages, {merged - pool} new, "
            f"{merged} in the evidence pool. Checking the evidence..."
        )
    if node == "map_evidence":
        mapping = update.get("evidence_map") or {}
        if not mapping:
            return None
        matched = sum(bool(ids) for ids in mapping.values())
        return f"Keyword match: {matched} of {len(mapping)} required components found."
    if node == "critic":
        entry = (update.get("critic_log") or [{}])[-1]
        source = CRITIC_SOURCES.get(entry.get("source"), entry.get("source"))
        shown = len(entry.get("passage_ids") or [])
        verdict = "enough" if entry.get("sufficient") else f"not enough, {entry.get('gap_label')}"
        return f"Evidence check ({source}, {shown} passages): {verdict}."
    if node == "rewrite_query":
        return f"Rewrote the search query: {update.get('rewritten_query')}"
    if node == "finish":
        return f"Stopped searching: {update.get('stop_reason')}, budget {update.get('max_rounds')} rounds."
    return None


def run_graph(graph: Any, state: AgentState, on_progress: ProgressFn) -> Any:
    """`graph.invoke`, reporting each finished step on the way."""
    final = None
    pool = 0
    for mode, chunk in graph.stream(state, stream_mode=["updates", "values"]):
        if mode == "values":
            final = chunk
            continue
        for node, update in chunk.items():
            update = update or {}
            line = describe_step(node, update, pool)
            pool = len(update.get("retrieved_passages") or []) or pool
            if line:
                on_progress(line, *NODE_STEPS[node])
    return final


def make_record_fn(
    retriever: Retriever,
    critic_client: CriticClient | None,
    *,
    max_retries: int = 2,
    section_selector: SectionSelector | None = None,
    critic_view: PassageView = pool_view,
    default_top_k: int = 5,
    on_progress: ProgressFn | None = None,
) -> RecordFn:
    """Build the server hook around `retriever(query, paper_id, top_k)`.

    P5's server calls `record_fn(question, paper_id)` without a depth, so `default_top_k` is the
    depth the demo retrieves per round (the factory reads it from `DEMO_AGENT_TOP_K`).

    `critic_view` is what the critic reads; the factory passes the server's own prompt
    view so the demo judges evidence the way the scored runs do.

    One compiled graph per `top_k`, so a request that asks for a different depth
    does not recompile on every call. A null paper ID selects corpus scope; a blank question raises
    `ValueError`, which the server reports as a client error rather than a refusal.
    """
    graphs: dict[int, Any] = {}

    def graph_for(top_k: int):
        if top_k not in graphs:
            graphs[top_k] = build_agent_graph(
                retriever,
                max_retries=max_retries,
                top_k=top_k,
                critic_client=critic_client,
                section_selector=section_selector,
                critic_view=critic_view,
            )
        return graphs[top_k]

    def record_fn(
        question: str, paper_id: str | None, top_k: int | None = None, request_id: str | None = None
    ) -> dict[str, Any]:
        started = time.perf_counter()
        state = AgentState(
            question=question,
            paper_id=paper_id,
            question_id=request_id or f"ui-{int(time.time() * 1000)}",
        )
        graph = graph_for(default_top_k if top_k is None else top_k)
        final = run_graph(graph, state, on_progress) if on_progress else graph.invoke(state)
        record = export_record(final)
        record["elapsed_s"] = time.perf_counter() - started
        # The HTTP answer record carries no critic_log, so this line is how a live run shows
        # what the critic read: per round (round, verdict source, passages shown).
        LOGGER.info(
            "agent %s: rounds=%d retrieved=%d critic=%s elapsed=%.1fs",
            record["question_id"], record["retrieval_round"], len(record["retrieved_passages"]),
            [(e["round"], e["source"], len(e.get("passage_ids", []))) for e in record["critic_log"]],
            record["elapsed_s"],
        )
        return record

    return record_fn
