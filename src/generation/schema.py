"""Wire-level data contracts for P5 generation and grounding.

`GenerationResult` is the **frozen P6 handoff schema**. It serialises to exactly
the five keys agreed for P5:

    answer, citations, evidence_status, retrieval_rounds, provenance

Two deliberate asymmetries to keep in mind when editing this module:

* Parsing is *lenient* (``extra="ignore"``) but serialisation is *exact*. A
  generator that emits an extra chatty field should not poison a whole batch,
  yet P6 must be able to rely on the key set. ``tests/test_schema.py`` pins the
  output key set so a careless field addition fails CI instead of silently
  breaking P6's parser.
* ``evidence_status`` / ``support`` accept a few common spelling variants from
  the model (``"sufficient"``, ``"Sufficient"``) and normalise to the enum. The
  parse layer in :mod:`src.generation.generators.base` records any such coercion as a
  diagnostic so prompt drift stays visible.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

# NOTE: Pydantic model *fields* below use `Optional[X]` rather than the `X | None`
# shorthand. `from __future__ import annotations` makes the shorthand safe in
# ordinary signatures, but Pydantic resolves field annotations at class-creation
# time and `str | None` is a runtime TypeError before Python 3.10. The university
# cluster and this workstation both run older interpreters, so `Optional` it is.

SCHEMA_VERSION = "p5-answer-v1"

#: The exact key set P6 may depend on, in canonical order.
ANSWER_KEYS: tuple[str, ...] = (
    "answer",
    "citations",
    "evidence_status",
    "retrieval_rounds",
    "provenance",
)

#: Canonical refusal text. The validator rewrites any refusal to this exact
#: string so that P6 can detect refusals with a single equality check, and so
#: that refusal rate is comparable across prompts and models.
REFUSAL_ANSWER = "Insufficient evidence in the retrieved passages to answer this question."


class EvidenceStatus(str, Enum):
    """Whether the retrieved passages were enough to answer the question."""

    SUFFICIENT = "SUFFICIENT"
    INSUFFICIENT = "INSUFFICIENT"

    @classmethod
    def _missing_(cls, value: object) -> "EvidenceStatus | None":
        if isinstance(value, str):
            key = value.strip().upper().replace("-", "_").replace(" ", "_")
            aliases = {
                "SUFFICIENT": cls.SUFFICIENT,
                "SUPPORTED": cls.SUFFICIENT,
                "ANSWERED": cls.SUFFICIENT,
                "OK": cls.SUFFICIENT,
                "INSUFFICIENT": cls.INSUFFICIENT,
                "UNSUPPORTED": cls.INSUFFICIENT,
                "INADEQUATE": cls.INSUFFICIENT,
                "REFUSED": cls.INSUFFICIENT,
                "NOT_ENOUGH_EVIDENCE": cls.INSUFFICIENT,
            }
            return aliases.get(key)
        return None


class Support(str, Enum):
    """How well a passage supports a claim, as asserted by the generator."""

    DIRECT = "direct"
    PARTIAL = "partial"
    UNSUPPORTED = "unsupported"

    @classmethod
    def _missing_(cls, value: object) -> "Support | None":
        if isinstance(value, str):
            key = value.strip().lower().replace("-", "_").replace(" ", "_")
            aliases = {
                "direct": cls.DIRECT,
                "full": cls.DIRECT,
                "explicit": cls.DIRECT,
                "yes": cls.DIRECT,
                "true": cls.DIRECT,
                "partial": cls.PARTIAL,
                "implied": cls.PARTIAL,
                "weak": cls.PARTIAL,
                "unsupported": cls.UNSUPPORTED,
                "none": cls.UNSUPPORTED,
                "no": cls.UNSUPPORTED,
                "false": cls.UNSUPPORTED,
            }
            return aliases.get(key)
        return None


class RetrievedPassage(BaseModel):
    """One passage handed to the generator by the P3/P4 retriever.

    ``passage_id`` is the only required link between a citation and its source.
    The identifier *scheme* is owned by P3/P4 and adapted in
    :mod:`src.generation.adapters.retrieval`; P5 never parses it, it only compares it
    for equality.

    ``extra="allow"`` lets the adapter carry P3/P4-specific fields (rerank
    scores, offsets, DOIs, ...) straight through without P5 knowing about them.
    """

    model_config = ConfigDict(extra="allow")

    passage_id: str
    text: str
    score: Optional[float] = None
    #: One-based rank from the round that produced this passage. P2 treats rank
    #: as authoritative within a round; P4 accumulates passages across rounds,
    #: so rank is a tie-breaker rather than a global ordering key here.
    rank: Optional[int] = None
    paper_id: Optional[str] = None
    title: Optional[str] = None
    section: Optional[str] = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("passage_id")
    @classmethod
    def _non_empty_id(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("passage_id must not be empty")
        return value.strip()


class ProvenanceEntry(BaseModel):
    """One factual claim in the answer plus the passages claimed to support it.

    This is P5's *audit trail*. It is filled in by the generator when it follows
    the prompt, and cross-checked against ``citations`` by the validator. It is
    diagnostic data: after a downgrade to a refusal the model's provenance is
    preserved only inside ``ValidationReport.raw_result``, because a refusal
    makes no claims and must not look as though it does.
    """

    model_config = ConfigDict(extra="ignore")

    claim: str
    passage_ids: list[str] = Field(default_factory=list)
    support: Support = Support.DIRECT

    @field_validator("passage_ids", mode="before")
    @classmethod
    def _coerce_ids(cls, value: Any) -> Any:
        """Accept ``["a"]``, ``"a"``, ``[{"passage_id": "a"}]`` and friends."""
        if value is None:
            return []
        if isinstance(value, str):
            return [value]
        if isinstance(value, list):
            out: list[str] = []
            for item in value:
                if isinstance(item, str):
                    out.append(item)
                elif isinstance(item, dict):
                    for key in ("passage_id", "id", "citation", "source"):
                        if isinstance(item.get(key), str):
                            out.append(item[key])
                            break
            return out
        return value


class GenerationResult(BaseModel):
    """The frozen final-answer schema handed to P6.

    Invariants enforced *after* validation (see
    :class:`src.generation.citations.CitationValidator`):

    * ``evidence_status == INSUFFICIENT`` implies ``citations == []``,
      ``provenance == []`` and ``answer == REFUSAL_ANSWER``.
    * ``evidence_status == SUFFICIENT`` implies ``citations`` is non-empty and
      every id in it was actually retrieved.

    Use :func:`to_wire` rather than ``model_dump`` when writing JSON: it pins the
    key order and drops nothing silently.
    """

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    answer: str
    citations: list[str] = Field(default_factory=list)
    evidence_status: EvidenceStatus = EvidenceStatus.INSUFFICIENT
    retrieval_rounds: int = Field(default=1, ge=1)
    provenance: list[ProvenanceEntry] = Field(default_factory=list)

    @field_validator("citations", mode="before")
    @classmethod
    def _coerce_citations(cls, value: Any) -> Any:
        if value is None:
            return []
        if isinstance(value, str):
            return [value]
        if isinstance(value, list):
            out: list[str] = []
            for item in value:
                if isinstance(item, str):
                    out.append(item.strip())
                elif isinstance(item, dict):
                    for key in ("passage_id", "id", "citation", "source"):
                        if isinstance(item.get(key), str):
                            out.append(item[key].strip())
                            break
            # De-duplicate while preserving order; a repeated citation carries no
            # extra information and would otherwise skew citation-count metrics.
            seen: set[str] = set()
            return [c for c in out if c and not (c in seen or seen.add(c))]
        return value

    @property
    def is_refusal(self) -> bool:
        """True when the result is a refusal. Derived, never serialised."""
        return self.evidence_status is EvidenceStatus.INSUFFICIENT

    @property
    def cited_passage_ids(self) -> list[str]:
        """Citations in order of first appearance."""
        return list(self.citations)

    def to_wire(self) -> dict[str, Any]:
        """Serialise to the frozen P6 schema (exactly ``ANSWER_KEYS``)."""
        dumped = self.model_dump(mode="json")
        return {key: dumped[key] for key in ANSWER_KEYS}


class GenerationRequest(BaseModel):
    """Everything the generator is allowed to see for one question.

    Note what is *absent*: no gold answer, no reference citation set. Grounding
    is enforced downstream by the validator, not by hiding information.
    """

    model_config = ConfigDict(extra="forbid")

    question: str
    passages: list[RetrievedPassage] = Field(default_factory=list)
    retrieval_rounds: int = Field(default=1, ge=1)
    language: str = "en"
    request_id: Optional[str] = None

    # -- P4 AgentState handoff (all optional; legacy payloads omit them) ---- #
    #: Paper scope, carried for the audit trail and P6 display.
    paper_id: Optional[str] = None
    #: The agent critic's terminal decision. ``None`` means the payload did not
    #: come from the agent loop (the P1 handoff), so P5 keeps its Week-3 path.
    agent_sufficient: Optional[bool] = None
    #: Components the planner requires (``result``, ``method``, ...). Used to
    #: prioritise the prompt's context and to check structural coverage.
    required_components: list[str] = Field(default_factory=list)
    #: P4's component -> passage-id map. A component with no ids is an evidence
    #: gap the critic should have caught.
    evidence_map: dict[str, list[str]] = Field(default_factory=dict)
    #: Trace fields carried through to the answer record for P6.
    gap_label: Optional[str] = None
    rewritten_query: Optional[str] = None
    retrieval_log: list[dict[str, Any]] = Field(default_factory=list)

    @property
    def passage_ids(self) -> list[str]:
        return [p.passage_id for p in self.passages]

    def passage_map(self) -> dict[str, RetrievedPassage]:
        return {p.passage_id: p for p in self.passages}

    def ordered_passages(self) -> list[RetrievedPassage]:
        """Best first: global score, with the retriever's rank as tie-breaker.

        P2 says rank is authoritative *within a round*. P4 accumulates passages
        across up to three rounds, so a rank of 1 exists once per round and
        cannot order the union. The retriever score is the only signal on a
        common scale across those rounds (RRF for fusion-only, raw reranker
        logits when a reranker ran), so it is the primary key; rank then breaks
        ties, matching P2's own tie-break rule. When scores are absent, the
        incoming order - which is rank order - is preserved.
        """
        if self.passages and all(p.score is not None for p in self.passages):
            return sorted(
                self.passages,
                key=lambda p: (
                    -(p.score if p.score is not None else 0.0),
                    p.rank if p.rank is not None else 0,
                    p.passage_id,
                ),
            )
        return list(self.passages)

    def input_fingerprint(self) -> dict[str, Any]:
        """The request fields that define the sample's *inputs*.

        The Week-4 agent fields are additive and default to empty for the
        Week-2/3 benchmark samples. Hashing them when unset would make an
        unchanged sample set report a different fingerprint, which is exactly
        the false alarm the fingerprint exists to prevent. Fields present with a
        non-default value stay in the hash.
        """
        data = self.model_dump(mode="json")
        for key in (
            "paper_id",
            "agent_sufficient",
            "required_components",
            "evidence_map",
            "gap_label",
            "rewritten_query",
            "retrieval_log",
        ):
            if data.get(key) in (None, [], {}):
                data.pop(key, None)
        for passage in data.get("passages", []):
            if passage.get("rank") is None:
                passage.pop("rank", None)
        return data

    def agent_trace(self) -> Optional[dict[str, Any]]:
        """The P4 fields worth carrying in the answer record, or ``None``.

        The frozen five-key answer is unchanged; this is an additive block on
        the *record wrapper* for P6's Week-4 display (rewritten query, critic
        decision, evidence map).
        """
        if (
            self.agent_sufficient is None
            and not self.required_components
            and not self.evidence_map
            and self.gap_label is None
            and self.rewritten_query is None
            and not self.retrieval_log
        ):
            return None
        return {
            "paper_id": self.paper_id,
            "sufficient": self.agent_sufficient,
            "gap_label": self.gap_label,
            "rewritten_query": self.rewritten_query,
            "required_components": list(self.required_components),
            "evidence_map": {k: list(v) for k, v in self.evidence_map.items()},
            "retrieval_log": list(self.retrieval_log),
        }


def refusal_result(retrieval_rounds: int = 1) -> GenerationResult:
    """A well-formed refusal, used for empty-context and downgrade paths."""
    return GenerationResult(
        answer=REFUSAL_ANSWER,
        citations=[],
        evidence_status=EvidenceStatus.INSUFFICIENT,
        retrieval_rounds=max(1, retrieval_rounds),
        provenance=[],
    )
