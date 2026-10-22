"""Node implementations for the LangGraph agent.

The planner (src/agent/planner.py), evidence mapper and gap classifier are
rule-based; the critic lives in src/agent/critic.py and the query rewriter in
src/agent/rewriter.py. Retrieval is real: `make_retrieve_node` wraps any
callable with P2's signature `retrieve(query, paper_id, top_k)`, e.g.
`HybridRetriever(...).retrieve`.

An empty retrieval result is not an error. It yields an empty evidence map, the
critic marks the evidence insufficient, and the normal retry loop applies until
the retry budget is spent.
"""

from __future__ import annotations

import re
import time
from collections.abc import Callable
from typing import Literal

from src.agent.planner import build_plan
from src.agent.schemas import AgentState, EvidenceRequirement, GapLabel
from src.retrieval.schemas import RetrievedPassage

MAX_RETRIES = 2  # keep in sync with configs/default.yaml: agent.max_retries
MAX_ROUNDS = MAX_RETRIES + 1  # initial retrieval + retries
DEFAULT_TOP_K = 5

Retriever = Callable[[str, str, int], list[RetrievedPassage]]


def plan_question(state: AgentState) -> dict:
    """Classify the question and derive its structured evidence requirements."""
    plan = build_plan(state.question)
    return {
        "question_type": plan.question_type,
        "evidence_requirements": plan.requirements,
        "required_components": [r.name for r in plan.requirements],
    }


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
        }
        return {
            "retrieved_passages": merged,
            "retrieval_round": next_round,
            "retrieval_log": [*state.retrieval_log, log_entry],
        }

    return retrieve_node


def _satisfies(requirement: EvidenceRequirement, hit: RetrievedPassage) -> bool:
    section = hit.passage.section.lower()
    if any(hint in section for hint in requirement.section_hints):
        return True
    text = hit.passage.text.lower()
    matched = {
        keyword
        for keyword in requirement.keywords
        if re.search(rf"(?<!\w){re.escape(keyword)}", text)
    }
    return len(matched) >= requirement.min_keyword_matches


def map_evidence(state: AgentState) -> dict:
    """Map each requirement to the retrieved passages that satisfy it."""
    return {
        "evidence_map": {
            requirement.name: [
                hit.passage.passage_id
                for hit in state.retrieved_passages
                if _satisfies(requirement, hit)
            ]
            for requirement in state.evidence_requirements
        }
    }


def gap_classifier(state: AgentState) -> dict:
    """Label the first unmet requirement with its `gap_if_missing` label."""
    for requirement in state.evidence_requirements:
        if not state.evidence_map.get(requirement.name):
            return {"gap_label": requirement.gap_if_missing}
    return {"gap_label": GapLabel.WEAK_EVIDENCE}


def route_after_critic(
    state: AgentState, max_rounds: int = MAX_ROUNDS
) -> Literal["retry", "stop"]:
    """Deterministic stop: sufficient, out of budget, or the paper cannot answer."""
    if (
        state.sufficient
        or state.gap_label is GapLabel.INSUFFICIENT_INFORMATION
        or state.retrieval_round >= max_rounds
    ):
        return "stop"
    return "retry"
