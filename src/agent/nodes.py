"""Node implementations for the LangGraph agent.

The planner, evidence mapper, critic, gap classifier and query rewriter are
still keyword-based mocks, to be replaced by real logic in later weeks (see
docs/EXECUTION_PLAN.md). Retrieval is real: `make_retrieve_node` wraps any
callable with P2's signature `retrieve(query, paper_id, top_k)`, e.g.
`HybridRetriever(...).retrieve`.

An empty retrieval result is not an error. It yields an empty evidence map, the
critic marks the evidence insufficient, and the normal retry loop applies until
the retry budget is spent.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Literal

from src.agent.schemas import AgentState, GapLabel
from src.retrieval.schemas import RetrievedPassage

MAX_RETRIES = 2  # keep in sync with configs/default.yaml: agent.max_retries
MAX_ROUNDS = MAX_RETRIES + 1  # initial retrieval + retries
DEFAULT_TOP_K = 5

Retriever = Callable[[str, str, int], list[RetrievedPassage]]

_COMPONENT_KEYWORDS: dict[str, list[str]] = {
    "result": ["result", "accuracy", "score", "performance", "f1"],
    "method": ["method", "approach", "architecture", "model"],
    "comparison": ["compare", "baseline", "versus", "outperform"],
}

_COMPONENT_TO_GAP: dict[str, GapLabel] = {
    "result": GapLabel.MISSING_RESULT,
    "method": GapLabel.MISSING_METHOD,
    "comparison": GapLabel.MISSING_COMPARISON,
}

_GAP_QUERY_HINTS: dict[GapLabel, str] = {
    GapLabel.MISSING_METHOD: "method approach architecture",
    GapLabel.MISSING_EXPERIMENT_CONTEXT: "dataset setup experimental configuration",
    GapLabel.MISSING_RESULT: "results experimental findings",
    GapLabel.MISSING_COMPARISON: "baseline comparison outperform",
    GapLabel.TERMINOLOGY_MISMATCH: "",
    GapLabel.WEAK_EVIDENCE: "additional detail",
    GapLabel.INSUFFICIENT_INFORMATION: "",
}


def plan_question(state: AgentState) -> dict:
    """Mock question planner: keyword match -> required components."""
    question_lower = state.question.lower()
    required = [
        component
        for component, keywords in _COMPONENT_KEYWORDS.items()
        if any(keyword in question_lower for keyword in keywords)
    ]
    return {"required_components": required or ["method"]}


def make_retrieve_node(
    retriever: Retriever, top_k: int = DEFAULT_TOP_K, section_selector=None
):
    """Build the retrieve node around an injected retrieval callable."""

    def retrieve_node(state: AgentState) -> dict:
        query = state.rewritten_query or state.question
        section = section_selector(state) if section_selector is not None else None
        scope = {} if section is None else {"section": section}
        started = time.perf_counter()
        hits = retriever(query, state.paper_id, top_k, **scope)
        elapsed_ms = (time.perf_counter() - started) * 1000

        merged = list(state.retrieved_passages)
        seen = {hit.passage.passage_id for hit in merged}
        for hit in hits:
            if hit.passage.passage_id not in seen:
                seen.add(hit.passage.passage_id)
                merged.append(hit)

        next_round = state.retrieval_round + 1
        log_entry = {
            "round": next_round,
            "query": query,
            "triggered_by": state.gap_label.value,
            "passage_ids": [hit.passage.passage_id for hit in hits],
            "section": section,
            "retrieval_ms": elapsed_ms,
            "retrieved_passages": [hit.model_dump(mode="json") for hit in hits],
        }
        return {
            "retrieved_passages": merged,
            "retrieval_round": next_round,
            "retrieval_log": [*state.retrieval_log, log_entry],
        }

    return retrieve_node


def map_evidence(state: AgentState) -> dict:
    """Mock evidence mapper: substring match components against passages."""
    evidence_map: dict[str, list[str]] = {}
    for component in state.required_components:
        evidence_map[component] = [
            hit.passage.passage_id
            for hit in state.retrieved_passages
            if component in hit.passage.section.lower()
            or component in hit.passage.text.lower()
        ]
    return {"evidence_map": evidence_map}


def critic(state: AgentState) -> dict:
    """Mock single critic: sufficient iff every component has evidence."""
    sufficient = all(bool(ids) for ids in state.evidence_map.values())
    update: dict = {"sufficient": sufficient}
    if sufficient:
        update["gap_label"] = GapLabel.NONE
    return update


def gap_classifier(state: AgentState) -> dict:
    """Mock gap classifier: label the first unmet required component."""
    missing = [component for component, ids in state.evidence_map.items() if not ids]
    if not missing:
        return {"gap_label": GapLabel.WEAK_EVIDENCE}
    return {"gap_label": _COMPONENT_TO_GAP.get(missing[0], GapLabel.WEAK_EVIDENCE)}


def rewrite_query(state: AgentState) -> dict:
    """Mock query rewriter: append a gap-specific search hint."""
    hint = _GAP_QUERY_HINTS.get(state.gap_label, "")
    return {"rewritten_query": f"{state.question} {hint}".strip()}


def route_after_critic(
    state: AgentState, max_rounds: int = MAX_ROUNDS
) -> Literal["retry", "stop"]:
    """Deterministic stop: sufficient evidence or retrieval budget spent."""
    if state.sufficient or state.retrieval_round >= max_rounds:
        return "stop"
    return "retry"
