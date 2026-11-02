"""Live-demo entry point: one free-form question in, one full agent record out.

P5's demo server answers a typed question by calling a hook and passing the
returned record to `answer_record`. This hook runs the whole agent (planner,
retrieval rounds, critic, rewriter) instead of a single retrieval, so the answer
carries the same `retrieval_round`, `gap_label` and `critic_log` as a scored run.

The critic shares P5's generator: the server owns the one vLLM engine an A40 can
hold, so nothing here loads a model.
"""

from __future__ import annotations

import time
from typing import Any, Callable

from src.agent.critic import CriticClient
from src.agent.export import export_record
from src.agent.graph import build_agent_graph
from src.agent.nodes import Retriever, SectionSelector
from src.agent.schemas import AgentState

#: `record_fn(question, paper_id, top_k, request_id=None) -> exported agent record`.
RecordFn = Callable[..., dict[str, Any]]


def make_record_fn(
    retriever: Retriever,
    critic_client: CriticClient | None,
    *,
    max_retries: int = 2,
    section_selector: SectionSelector | None = None,
) -> RecordFn:
    """Build the server hook around `retriever(query, paper_id, top_k)`.

    One compiled graph per `top_k`, so a request that asks for a different depth
    does not recompile on every call. A blank question or paper raises
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
            )
        return graphs[top_k]

    def record_fn(
        question: str, paper_id: str, top_k: int = 5, request_id: str | None = None
    ) -> dict[str, Any]:
        started = time.perf_counter()
        state = AgentState(
            question=question,
            paper_id=paper_id,
            question_id=request_id or f"ui-{int(time.time() * 1000)}",
        )
        record = export_record(graph_for(top_k).invoke(state))
        record["elapsed_s"] = time.perf_counter() - started
        return record

    return record_fn
