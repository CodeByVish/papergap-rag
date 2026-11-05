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

#: `record_fn(question, paper_id, top_k, request_id=None) -> exported agent record`.
RecordFn = Callable[..., dict[str, Any]]


def make_record_fn(
    retriever: Retriever,
    critic_client: CriticClient | None,
    *,
    max_retries: int = 2,
    section_selector: SectionSelector | None = None,
    critic_view: PassageView = pool_view,
    default_top_k: int = 5,
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
        record = export_record(graph_for(default_top_k if top_k is None else top_k).invoke(state))
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
