"""Proposed Week 1 contract; review with P1, P3 and P4 before freezing."""

from pydantic import BaseModel, ConfigDict, Field


class Passage(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    passage_id: str = Field(min_length=1)
    paper_id: str = Field(min_length=1)
    title: str
    section: str
    chunk_number: int = Field(ge=0)
    text: str = Field(min_length=1)
    previous_passage_id: str | None = None
    next_passage_id: str | None = None


class RetrievalHit(BaseModel):
    """One P1 result. Rank is one-based; scores need not share a scale."""

    model_config = ConfigDict(extra="forbid", frozen=True)
    passage: Passage
    rank: int = Field(ge=1)
    score: float = Field(allow_inf_nan=False)


class SourceScore(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    rank: int = Field(ge=1)
    score: float = Field(allow_inf_nan=False)


class RetrievedPassage(BaseModel):
    """P2 output for P4. Reranker scores are raw logits, not probabilities."""

    model_config = ConfigDict(extra="forbid", frozen=True)
    passage: Passage
    rank: int = Field(ge=1)
    source_scores: dict[str, SourceScore]
    rrf_score: float = Field(gt=0, allow_inf_nan=False)
    reranker_score: float | None = Field(default=None, allow_inf_nan=False)
