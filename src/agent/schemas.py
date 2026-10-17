"""Agent-state and gap-label schemas for the PaperGap LangGraph agent (P4).

Proposed for team review (see docs/EXECUTION_PLAN.md); not yet frozen. Retrieval
results use P2's `RetrievedPassage` (src/retrieval/schemas.py) unchanged.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from src.retrieval.schemas import RetrievedPassage


class GapLabel(str, Enum):
    """Evidence-gap categories, from the Week 4 gap-action table."""

    NONE = "NONE"
    MISSING_METHOD = "MISSING_METHOD"
    MISSING_EXPERIMENT_CONTEXT = "MISSING_EXPERIMENT_CONTEXT"
    MISSING_RESULT = "MISSING_RESULT"
    MISSING_COMPARISON = "MISSING_COMPARISON"
    TERMINOLOGY_MISMATCH = "TERMINOLOGY_MISMATCH"
    WEAK_EVIDENCE = "WEAK_EVIDENCE"
    INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"


class CriticOutput(BaseModel):
    """Output of the single evidence critic (Week 3 sample shape)."""

    sufficient: bool
    gap_label: GapLabel
    missing_components: list[str] = Field(default_factory=list)
    reason: str


class AgentState(BaseModel):
    """Shared state threaded through every node in the LangGraph agent.

    `retrieved_passages` accumulates across rounds, de-duplicated by the opaque
    `passage_id`. `retrieval_log` has one entry per retrieval round
    (`round`, `query`, `triggered_by`, `passage_ids`) so passages stay traceable.
    """

    question: str
    paper_id: str
    required_components: list[str] = Field(default_factory=list)
    retrieved_passages: list[RetrievedPassage] = Field(default_factory=list)
    evidence_map: dict[str, list[str]] = Field(default_factory=dict)
    gap_label: GapLabel = GapLabel.NONE
    rewritten_query: str | None = None
    retrieval_round: int = 0
    sufficient: bool = False
    retrieval_log: list[dict[str, Any]] = Field(default_factory=list)
