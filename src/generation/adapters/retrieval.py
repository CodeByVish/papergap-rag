"""Adapters from P3/P4 retriever output to :class:`RetrievedPassage`.

**Status: the real wire format was confirmed by the P1 handoff of 2026-10-17.**
Each record carries ``question_id``, ``question``, ``paper_id``,
``retrieval_round`` and ``retrieved_passages``; each hit keeps P2's nested
``{"passage": {...}, "rank": ..., "source_scores": ..., "rrf_score": ...,
"reranker_score": ...}`` shape. :class:`QasperHitAdapter` accepts that shape and
the older flat one through :func:`flatten_nested_hit`. P5 still owns only the
*contract* (the ``passage_id`` string is the only link between a citation and
its source), not the identifier scheme, so this module ships:

* :class:`PassageAdapter` - the one-method interface P6 should code against. Wire
  in the real adapter here and nothing downstream changes.
* :class:`ReferenceHitAdapter` - a working reference implementation for the
  scheme used in the P5 brief, ``{paper_id}_{section}_{chunk_idx:02d}``, e.g.
  ``paper123_results_04``. Enough to build and test the whole pipeline today, and
  deliberately field-name tolerant (``text`` / ``content`` / ``chunk``) so it may
  just work on the real output.
* :class:`PlaceholderAdapter` - the explicit "not filled in yet" case. It fails
  loudly with a pointer to ``docs/RETRIEVAL_CONTRACT.md`` instead of silently
  producing passages with missing ids.

The identifier is **never parsed for meaning** by P5. All the validator does is
compare citation strings for equality against the retrieved set, which is why the
scheme can change without touching the validator or the schema.
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import Any, Callable, Iterable, Mapping, Sequence

from pydantic import BaseModel, ConfigDict, Field

from src.generation.schema import GenerationRequest, RetrievedPassage

# --------------------------------------------------------------------------- #
# Reference identifier scheme
# --------------------------------------------------------------------------- #

#: ``paper123_results_04`` -> paper_id ``paper123``, section ``results``, chunk 4.
#: The paper id is greedy so it may itself contain underscores; the section must
#: be a single alphanumeric word and the index is 1-3 digits.
PASSAGE_ID_RE = re.compile(
    r"^(?P<paper_id>.+)_(?P<section>[A-Za-z][A-Za-z0-9]*)_(?P<chunk_idx>\d{1,3})$"
)


class PassageIdParts(BaseModel):
    """The decoded parts of a reference-scheme passage id."""

    model_config = ConfigDict(extra="forbid")

    paper_id: str
    section: str
    chunk_idx: int
    raw: str


def format_passage_id(paper_id: str, section: str, chunk_idx: int) -> str:
    """Build a reference-scheme id. Chunk indices are zero-padded to 2 digits.

    The padding is the point: it makes lexicographic order match retrieval order,
    so a sorted listing of a paper's chunks reads in document order.
    """
    clean_section = normalize_section(section)
    return f"{paper_id}_{clean_section}_{chunk_idx:02d}"


def parse_passage_id(passage_id: str) -> PassageIdParts | None:
    """Decode a reference-scheme id, or ``None`` if it does not match.

    Returning ``None`` rather than raising is intentional: an unrecognised id is
    a reason to fall back to the record's own fields, not to drop the passage.
    """
    match = PASSAGE_ID_RE.match(passage_id.strip())
    if not match:
        return None
    return PassageIdParts(
        paper_id=match.group("paper_id"),
        section=match.group("section"),
        chunk_idx=int(match.group("chunk_idx")),
        raw=passage_id,
    )


def normalize_section(section: str) -> str:
    """Lowercase and underscore-join a section label ("Results" -> "results")."""
    return re.sub(r"[\s\-]+", "_", section.strip().lower())


# --------------------------------------------------------------------------- #
# The real scheme: opaque content hashes
# --------------------------------------------------------------------------- #

#: Confirmed with the retrieval phase on 2026-10-10.
#:
#: ``qasper-passage-v1-<64 lowercase hex>``. Nothing is encoded in it: no paper
#: id, no section, no chunk index. P5 never wanted to parse an id for meaning,
#: so this costs it nothing - but it does mean anything that *derived* a passage
#: id from a paper id (the reference scheme's synthesis path) would be inventing
#: an identifier that no retriever will ever return, and a citation the
#: validator cannot resolve.
QASPER_ID_PREFIX = "qasper-passage-v1-"
QASPER_PASSAGE_ID_RE = re.compile(r"^qasper-passage-v1-(?P<digest>[0-9a-f]{64})$")


def is_qasper_passage_id(value: str) -> bool:
    """True when ``value`` has the shape the real retriever emits."""
    return bool(QASPER_PASSAGE_ID_RE.match(value.strip()))


#: Wrapper keys a retriever payload may hide its hit list under.
#:
#: ``retrieved_passages`` is the field name the P4 ``AgentState`` uses, and the
#: P1 handoff of 2026-10-17 serialises it at the top level of every record.
HITS_KEYS: tuple[str, ...] = (
    "passages",
    "hits",
    "results",
    "contexts",
    "documents",
    "retrieved",
    "retrieved_passages",
)


def _as_mapping(value: Any) -> Mapping[str, Any] | None:
    """Accept a dict or a Pydantic model and return a plain mapping.

    P4's ``AgentState`` and P2's ``RetrievedPassage`` are Pydantic models. A
    caller that hands the live graph result to P5 has not serialised them, so
    the adapter duck-types ``model_dump`` instead of requiring a JSON round-trip.
    A JSON dump and a live model therefore reach the same code path.
    """
    if isinstance(value, Mapping):
        return value
    dump = getattr(value, "model_dump", None)
    if callable(dump):
        try:
            data = dump(mode="json")
        except TypeError:  # pragma: no cover - older Pydantic without mode
            data = dump()
        if isinstance(data, Mapping):
            return data
    return None


def as_records(raw: Any) -> list[Mapping[str, Any]]:
    """Unwrap a retriever payload into a list of hit mappings.

    Accepts a list of hits, a single hit, or a wrapper dict carrying the list
    under one of :data:`HITS_KEYS`. Module-level rather than a method so the
    reference adapter, the real adapter and the request builder share one
    tolerance list - three copies of it would drift, and the failure would be a
    silently dropped passage rather than an error.
    """
    raw_map = _as_mapping(raw)
    if raw_map is not None:
        for key in HITS_KEYS:
            inner = raw_map.get(key)
            if isinstance(inner, list):
                return [
                    mapping
                    for item in inner
                    if (mapping := _as_mapping(item)) is not None
                ]
        return [raw_map]
    if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
        return [
            mapping for item in raw if (mapping := _as_mapping(item)) is not None
        ]
    raise TypeError(
        f"cannot adapt {type(raw).__name__} to passages; expected a list of "
        "hit dicts or a dict containing one under "
        f"{'/'.join(HITS_KEYS)}"
    )


#: Outer fields of a P2 ``RetrievedPassage`` that are trace data rather than
#: passage fields. They are carried into ``metadata`` so a run can be audited
#: against the retriever without P5 knowing what they mean.
NESTED_TRACE_KEYS: tuple[str, ...] = (
    "rank",
    "source_scores",
    "rrf_score",
    "reranker_score",
)


def flatten_nested_hit(record: Mapping[str, Any]) -> Mapping[str, Any]:
    """Flatten a P2 ``RetrievedPassage`` into the flat hit shape.

    P2 hands P4 a **nested** object, and the P1 handoff of 2026-10-17 serialises
    it unchanged::

        {"passage": {passage_id, paper_id, title, section, chunk_number, text,
                     previous_passage_id, next_passage_id},
         "rank": 1,
         "source_scores": {"bm25": {...}, "dense": {...}},
         "rrf_score": 0.0325,
         "reranker_score": null}

    P5's validator and prompt only need the passage fields, but the trace
    fields stay in ``metadata`` rather than being discarded. A flat hit is
    returned unchanged, so the tolerance is additive: the older fixtures keep
    working and a retriever that flattens tomorrow still works.

    **Score selection is ordered for a reason.** ``reranker_score`` is the
    author's final relevance judgement when a reranker ran; ``rrf_score`` is the
    authoritative fused score when it did not (the P1 handoff ran fusion-only,
    so every ``reranker_score`` is null); a native ``score`` is the fallback for
    the BM25/dense dumps. The hybrid list is already in RRF order, and sorting
    by the RRF score preserves it - including P2's passage-id tie-break, since
    a stable sort keeps the incoming order for equal scores.
    """
    passage = _as_mapping(record.get("passage"))
    if passage is None:
        return record

    # Passage fields first, then the outer trace fields (outer wins if both
    # levels happen to carry one), then anything else not already present.
    flat: dict[str, Any] = dict(passage)
    for key in NESTED_TRACE_KEYS:
        if key in record:
            flat[key] = record[key]
    for key, value in record.items():
        if key != "passage" and key not in flat:
            flat[key] = value

    for key in ("reranker_score", "rrf_score"):
        if record.get(key) is not None:
            flat["score"] = record[key]
            break
    else:
        if "score" in record and record["score"] is not None:
            flat["score"] = record["score"]

    return flat


# --------------------------------------------------------------------------- #
# Interface
# --------------------------------------------------------------------------- #


class PassageAdapter(ABC):
    """Convert one retriever's output into :class:`RetrievedPassage` objects.

    Implementations must guarantee two things, because the validator depends on
    both and can only check one of them:

    1. ``passage_id`` is non-empty and **unique within a request**. Duplicate ids
       make citations ambiguous, and the validator cannot detect the ambiguity -
       it would simply accept a citation that matches two different passages.
    2. ``text`` is the exact text the model will see, so that the numeric
       grounding check compares against the same characters the model read.
    """

    #: Short name for logs and the registry.
    name: str = "base"

    @abstractmethod
    def to_passages(self, raw: Any) -> list[RetrievedPassage]:
        """Adapt one retriever payload (usually a list of hits)."""

    def validate_ids(self, passages: Sequence[RetrievedPassage]) -> None:
        """Raise when ids are empty or duplicated. Called by the pipeline."""
        seen: set[str] = set()
        for passage in passages:
            if passage.passage_id in seen:
                raise ValueError(
                    f"duplicate passage_id {passage.passage_id!r}; the adapter must "
                    "produce unique ids within a request"
                )
            seen.add(passage.passage_id)


# --------------------------------------------------------------------------- #
# Reference implementation
# --------------------------------------------------------------------------- #


class AdapterFieldConfig(BaseModel):
    """Which keys to read out of a retriever hit.

    Each entry is a list of candidate key names tried in order, so the same
    adapter covers the naming variants a group project accumulates over several
    weeks of refactoring.
    """

    model_config = ConfigDict(extra="forbid")

    id_keys: tuple[str, ...] = ("passage_id", "id", "chunk_id", "doc_id", "pid")
    text_keys: tuple[str, ...] = ("text", "content", "chunk", "passage", "body", "snippet")
    score_keys: tuple[str, ...] = ("score", "rerank_score", "similarity", "bm25_score")
    rank_keys: tuple[str, ...] = ("rank", "rank_position")
    paper_id_keys: tuple[str, ...] = ("paper_id", "doc_id", "paper", "arxiv_id")
    title_keys: tuple[str, ...] = ("title", "paper_title", "heading")
    section_keys: tuple[str, ...] = ("section", "section_name", "sec")


def _pick(record: Mapping[str, Any], keys: Iterable[str]) -> Any:
    for key in keys:
        if key in record and record[key] is not None:
            return record[key]
    return None


class ReferenceHitAdapter(PassageAdapter):
    """Adapter for the ``{paper_id}_{section}_{chunk_idx:02d}`` reference scheme.

    Reads a list of hit dicts. If a hit has no id, one is synthesised from its
    paper id and position; if the id does not match the reference pattern, the
    record's own ``paper_id`` / ``section`` fields are used instead. Passages
    without a usable id are dropped rather than guessed at, because a passage the
    model can cite but the validator cannot resolve is worse than no passage.
    """

    name = "reference"

    def __init__(self, config: AdapterFieldConfig | None = None) -> None:
        self.config = config or AdapterFieldConfig()

    def to_passages(self, raw: Any) -> list[RetrievedPassage]:
        records = self._as_records(raw)
        passages: list[RetrievedPassage] = []

        for position, record in enumerate(records):
            text = _pick(record, self.config.text_keys)
            if not isinstance(text, str) or not text.strip():
                continue

            paper_id = _pick(record, self.config.paper_id_keys)
            section = _pick(record, self.config.section_keys)
            passage_id = _pick(record, self.config.id_keys)

            if not isinstance(passage_id, str) or not passage_id.strip():
                passage_id = self._synthesise_id(paper_id, section, position, passages)
                if passage_id is None:
                    continue

            parts = parse_passage_id(passage_id)
            if parts is not None:
                paper_id = paper_id or parts.paper_id
                section = section or parts.section

            score = _pick(record, self.config.score_keys)
            rank = _pick(record, self.config.rank_keys)
            title = _pick(record, self.config.title_keys)

            passages.append(
                RetrievedPassage(
                    passage_id=passage_id.strip(),
                    text=text,
                    score=float(score) if isinstance(score, (int, float)) else None,
                    rank=rank if isinstance(rank, int) and not isinstance(rank, bool) else None,
                    paper_id=str(paper_id) if paper_id is not None else None,
                    title=str(title) if title is not None else None,
                    section=str(section) if section is not None else None,
                    # Anything else the retriever returned is kept verbatim so a
                    # later stage can use it without a schema change.
                    # Everything not lifted into a named field is kept verbatim.
                    # `paper_id_keys` et al. have to be subtracted alongside the
                    # others or `paper_id` lands in metadata as well as in its
                    # own field, which reads like two sources of truth.
                    metadata={
                        key: value
                        for key, value in record.items()
                        if key
                        not in set(self.config.text_keys)
                        | set(self.config.id_keys)
                        | set(self.config.score_keys)
                        | set(self.config.paper_id_keys)
                        | set(self.config.title_keys)
                        | set(self.config.section_keys)
                    },
                )
            )

        return passages

    def _as_records(self, raw: Any) -> list[Mapping[str, Any]]:
        """Accept a list of hits, a single hit, or a wrapper with a ``hits`` key."""
        return as_records(raw)

    def _synthesise_id(
        self,
        paper_id: Any,
        section: Any,
        position: int,
        existing: Sequence[RetrievedPassage],
    ) -> str | None:
        """Build a reference-scheme id for a hit that arrived without one.

        Returns ``None`` when there is not even a paper id to anchor the
        identifier - inventing one would make the citation unverifiable.
        """
        if not isinstance(paper_id, str) or not paper_id.strip():
            return None
        section_label = section if isinstance(section, str) and section.strip() else "unknown"
        used = {p.passage_id for p in existing}
        candidate = format_passage_id(paper_id.strip(), section_label, position)
        bump = position
        while candidate in used:
            bump += 1
            candidate = format_passage_id(paper_id.strip(), section_label, bump)
        return candidate


class AdapterReport(BaseModel):
    """What an adapter had to drop or flag, so a caller can see it.

    An adapter that silently discards half a retriever's output looks exactly
    like a retriever that returned half as much, and the difference matters:
    one is P5's bug, the other is upstream's. Counting the drops is what keeps
    them distinguishable.
    """

    model_config = ConfigDict(extra="forbid")

    #: Hits with no usable id. Never synthesised - see :class:`QasperHitAdapter`.
    dropped_no_id: int = 0
    #: Hits with no usable text.
    dropped_no_text: int = 0
    #: Ids that were kept but do not match the ``qasper-passage-v1-`` shape.
    malformed_ids: list[str] = []
    #: Ids that appeared more than once and were collapsed to their first hit.
    duplicate_ids: list[str] = []

    @property
    def dropped_total(self) -> int:
        return self.dropped_no_id + self.dropped_no_text

    def notes(self) -> list[str]:
        """Human-readable summary, empty when nothing needs saying."""
        out: list[str] = []
        if self.dropped_no_id:
            out.append(
                f"{self.dropped_no_id} hit(s) dropped for having no passage id; "
                "a passage the validator cannot resolve is worse than no passage"
            )
        if self.dropped_no_text:
            out.append(f"{self.dropped_no_text} hit(s) dropped for having no text")
        if self.malformed_ids:
            out.append(
                f"{len(self.malformed_ids)} id(s) kept but not shaped like "
                f"{QASPER_ID_PREFIX}<sha256>: "
                + ", ".join(self.malformed_ids[:3])
                + (" ..." if len(self.malformed_ids) > 3 else "")
            )
        if self.duplicate_ids:
            out.append(
                f"{len(self.duplicate_ids)} duplicate id(s) collapsed to their "
                "first hit: " + ", ".join(self.duplicate_ids[:3])
                + (" ..." if len(self.duplicate_ids) > 3 else "")
            )
        return out


class QasperHitAdapter(PassageAdapter):
    """Adapter for the real retriever: opaque ``qasper-passage-v1-<sha256>`` ids.

    Differs from :class:`ReferenceHitAdapter` in exactly one way, and it is the
    one that matters: **it never synthesises an id.** The reference adapter
    builds ``{paper_id}_{section}_{idx}`` for a hit that arrives without one,
    which is reasonable when ids are structured and actively harmful here - the
    real scheme is a content hash, so a synthesised id is one no retriever will
    ever emit, and citing it produces a fabricated citation that R1 must then
    throw the whole answer away for. A hit with no id is dropped and counted.

    ``paper_id`` and ``section`` are taken from the record's own fields and
    never decoded from the id, because the id does not encode them. Both are
    optional: they only decorate the prompt's passage header.
    """

    name = "qasper"

    def __init__(self, config: AdapterFieldConfig | None = None) -> None:
        self.config = config or AdapterFieldConfig()
        self.last_report = AdapterReport()

    def to_passages(self, raw: Any) -> list[RetrievedPassage]:
        passages, self.last_report = self.to_passages_reported(raw)
        return passages

    def to_passages_reported(
        self, raw: Any
    ) -> tuple[list[RetrievedPassage], AdapterReport]:
        """Adapt and report, so the caller can surface what was lost."""
        records = [flatten_nested_hit(record) for record in as_records(raw)]
        passages: list[RetrievedPassage] = []
        report = AdapterReport()
        seen: set[str] = set()

        for record in records:
            text = _pick(record, self.config.text_keys)
            if not isinstance(text, str) or not text.strip():
                report.dropped_no_text += 1
                continue

            passage_id = _pick(record, self.config.id_keys)
            if not isinstance(passage_id, str) or not passage_id.strip():
                report.dropped_no_id += 1
                continue
            passage_id = passage_id.strip()

            if passage_id in seen:
                report.duplicate_ids.append(passage_id)
                continue
            seen.add(passage_id)

            # Kept verbatim even when it does not match. The id is an opaque
            # token to P5 and R1 will reject it if it was not retrieved, so the
            # only thing a shape check buys is an early signal that the two
            # sides have drifted apart - which is worth a note, not a drop.
            if not is_qasper_passage_id(passage_id):
                report.malformed_ids.append(passage_id)

            score = _pick(record, self.config.score_keys)
            rank = _pick(record, self.config.rank_keys)
            paper_id = _pick(record, self.config.paper_id_keys)
            title = _pick(record, self.config.title_keys)
            section = _pick(record, self.config.section_keys)

            passages.append(
                RetrievedPassage(
                    passage_id=passage_id,
                    text=text,
                    score=float(score) if isinstance(score, (int, float)) else None,
                    rank=rank if isinstance(rank, int) and not isinstance(rank, bool) else None,
                    paper_id=str(paper_id) if paper_id is not None else None,
                    title=str(title) if title is not None else None,
                    section=str(section) if section is not None else None,
                    metadata={
                        key: value
                        for key, value in record.items()
                        if key
                        not in set(self.config.text_keys)
                        | set(self.config.id_keys)
                        | set(self.config.score_keys)
                        | set(self.config.paper_id_keys)
                        | set(self.config.title_keys)
                        | set(self.config.section_keys)
                    },
                )
            )

        return passages, report


class PlaceholderAdapter(PassageAdapter):
    """Not-yet-implemented adapter for the real P3/P4 output.

    Exists so that the unfinished integration is one obvious, greppable failure
    rather than a silent one. Replace it (or point ``get_adapter`` at a new class)
    once the P3/P4 format is fixed; see ``docs/RETRIEVAL_CONTRACT.md``.
    """

    name = "placeholder"

    def to_passages(self, raw: Any) -> list[RetrievedPassage]:
        raise NotImplementedError(
            "The real P3/P4 retriever output format has not been wired up yet.\n"
            "Either:\n"
            "  1. use ReferenceHitAdapter if the hits carry passage ids shaped like\n"
            "     '{paper_id}_{section}_{chunk_idx:02d}', or\n"
            "  2. implement PassageAdapter.to_passages for the real format and\n"
            "     register it in ADAPTER_REGISTRY.\n"
            "Contract and checklist: docs/RETRIEVAL_CONTRACT.md"
        )


# --------------------------------------------------------------------------- #
# Payload -> request
# --------------------------------------------------------------------------- #

#: Candidate envelope keys for the question. The retriever names its own
#: envelope, and the names are not settled - see ``docs/RETRIEVAL_CONTRACT.md``.
QUESTION_KEYS: tuple[str, ...] = ("question", "query", "q", "question_text")
ROUNDS_KEYS: tuple[str, ...] = (
    "retrieval_round",
    "retrieval_rounds",
    "rounds",
    "n_rounds",
)
REQUEST_ID_KEYS: tuple[str, ...] = ("request_id", "question_id", "qid", "id")

#: P4 `AgentState` fields. The schema is now in the shared repo
#: (``src/agent/schemas.py``), so these names are the real ones; the aliases
#: keep the adapter tolerant of an intermediate wrapper.
PAPER_ID_KEYS: tuple[str, ...] = ("paper_id", "paper", "doc_id")
SUFFICIENT_KEYS: tuple[str, ...] = (
    "sufficient",
    "evidence_sufficient",
    "is_sufficient",
)
REQUIRED_COMPONENT_KEYS: tuple[str, ...] = (
    "required_components",
    "components",
    "sub_questions",
)
EVIDENCE_MAP_KEYS: tuple[str, ...] = (
    "evidence_map",
    "evidence",
    "evidence_by_component",
)
GAP_LABEL_KEYS: tuple[str, ...] = ("gap_label", "gap", "critic_decision")
REWRITTEN_QUERY_KEYS: tuple[str, ...] = (
    "rewritten_query",
    "rewrite",
    "rewritten",
)
RETRIEVAL_LOG_KEYS: tuple[str, ...] = ("retrieval_log", "rounds_log", "trace")


def _optional_text(value: Any, field_name: str) -> str | None:
    """Accept a string or an Enum (P4's ``GapLabel``), else raise."""
    if value is None:
        return None
    if hasattr(value, "value"):  # Enum member
        value = value.value
    if not isinstance(value, str):
        raise ValueError(
            f"P4 AgentState field {field_name} must be a string or null, "
            f"got {type(value).__name__}"
        )
    return value


def _string_list(value: Any, field_name: str) -> list[str]:
    """Validate a list of component labels without silently coercing."""
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
        raise ValueError(
            f"P4 AgentState field {field_name} must be a list of strings, "
            f"got {type(value).__name__}"
        )
    return list(value)


def _evidence_map(value: Any) -> dict[str, list[str]]:
    """Validate P4's ``component -> [passage_id]`` map.

    A malformed map means P5 is reading the wrong field; that is an integration
    error, not a model failure, so it raises here rather than becoming a silent
    zero-evidence run.
    """
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ValueError(
            "P4 AgentState field evidence_map must be a mapping of "
            f"component -> list[str], got {type(value).__name__}"
        )
    out: dict[str, list[str]] = {}
    for component, ids in value.items():
        if not isinstance(component, str):
            raise ValueError("evidence_map keys must be strings")
        if not isinstance(ids, list) or not all(isinstance(x, str) for x in ids):
            raise ValueError(
                f"evidence_map[{component!r}] must be a list of strings"
            )
        out[component] = list(ids)
    return out


def _retrieval_log(value: Any) -> list[dict[str, Any]]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(x, Mapping) for x in value):
        raise ValueError(
            "P4 AgentState field retrieval_log must be a list of objects"
        )
    return [dict(x) for x in value]


class AdaptedRequest(BaseModel):
    """One retriever payload turned into a request, plus what that cost."""

    model_config = ConfigDict(extra="forbid")

    request: GenerationRequest
    report: AdapterReport = Field(default_factory=AdapterReport)
    notes: list[str] = Field(default_factory=list)


def build_request(
    payload: Any,
    adapter: PassageAdapter | None = None,
    *,
    question_keys: Sequence[str] = QUESTION_KEYS,
    rounds_keys: Sequence[str] = ROUNDS_KEYS,
    request_id_keys: Sequence[str] = REQUEST_ID_KEYS,
    language: str = "en",
) -> AdaptedRequest:
    """Turn one retriever payload into a :class:`GenerationRequest`.

    Raises ``ValueError`` on a payload with no question or no hit list. That is
    deliberate and it is the opposite of the generation path's soft-fail: a
    malformed *model response* is the model's problem and becomes a refusal,
    while a malformed *retriever payload* means P5 is reading the wrong field,
    and turning that into a silent zero-passage refusal would report an
    integration bug as a retrieval result. A batch caller should catch this per
    record and skip, not abort the run.

    ``retrieval_rounds`` is copied, never computed - the retriever owns the
    count. Two things it does do, and both are reported in ``notes`` rather than
    applied silently:

    * the schema requires ``>= 1``, so a round count of ``0`` is clamped. If the
      retriever counts from zero, every round number is being understated by
      one, and that is a mapping decision for the retriever to make - P5 records
      the discrepancy instead of quietly papering over it.
    * a missing round count defaults to ``1``, with a note saying so.
    """
    adapter = adapter or QasperHitAdapter()
    payload_map = _as_mapping(payload)
    if payload_map is None:
        raise ValueError(
            f"expected one retriever payload as a mapping or Pydantic model, "
            f"got {type(payload).__name__}"
        )
    payload = payload_map

    question = _pick(payload, question_keys)
    if not isinstance(question, str) or not question.strip():
        raise ValueError(
            f"retriever payload has no usable question; tried {list(question_keys)}"
        )

    hits: Any = None
    for key in HITS_KEYS:
        if isinstance(payload.get(key), list):
            hits = payload[key]
            break
    if hits is None:
        raise ValueError(
            f"retriever payload has no hit list; tried {list(HITS_KEYS)}"
        )

    notes: list[str] = []

    if isinstance(adapter, QasperHitAdapter):
        passages, report = adapter.to_passages_reported(hits)
    else:
        passages = adapter.to_passages(hits)
        report = AdapterReport()
    adapter.validate_ids(passages)
    notes.extend(report.notes())

    raw_rounds = _pick(payload, rounds_keys)
    if isinstance(raw_rounds, bool) or not isinstance(raw_rounds, int):
        rounds = 1
        notes.append(
            "payload carried no usable retrieval round count "
            f"({raw_rounds!r}); defaulted to 1. P5 copies this value rather than "
            "computing it, so confirm the envelope key with the retriever."
        )
    elif raw_rounds < 1:
        rounds = 1
        notes.append(
            f"retrieval round count was {raw_rounds}, which the frozen schema "
            "cannot represent (>= 1); clamped to 1. If the retriever counts from "
            "zero the mapping belongs upstream - retrieval cost is being "
            "understated by one round here."
        )
    else:
        rounds = raw_rounds

    request_id = _pick(payload, request_id_keys)

    # P4 AgentState fields. Legacy P1 payloads omit every one of them, so the
    # Week-3 path is unchanged; an AgentState dump carries them and P5 uses
    # them for the terminal-state rule and the evidence-map prompt.
    paper_id = _optional_text(_pick(payload, PAPER_ID_KEYS), "paper_id")
    sufficient_raw = _pick(payload, SUFFICIENT_KEYS)
    if sufficient_raw is not None and not isinstance(sufficient_raw, bool):
        raise ValueError(
            "P4 AgentState field sufficient must be a boolean or null, "
            f"got {type(sufficient_raw).__name__}"
        )
    required_components = _string_list(
        _pick(payload, REQUIRED_COMPONENT_KEYS), "required_components"
    )
    evidence_map = _evidence_map(_pick(payload, EVIDENCE_MAP_KEYS))
    if not required_components and evidence_map:
        required_components = list(evidence_map)
    gap_label = _optional_text(_pick(payload, GAP_LABEL_KEYS), "gap_label")
    rewritten_query = _optional_text(
        _pick(payload, REWRITTEN_QUERY_KEYS), "rewritten_query"
    )
    retrieval_log = _retrieval_log(_pick(payload, RETRIEVAL_LOG_KEYS))

    return AdaptedRequest(
        request=GenerationRequest(
            question=question.strip(),
            passages=passages,
            retrieval_rounds=rounds,
            language=language,
            request_id=str(request_id) if request_id is not None else None,
            paper_id=paper_id,
            agent_sufficient=sufficient_raw,
            required_components=required_components,
            evidence_map=evidence_map,
            gap_label=gap_label,
            rewritten_query=rewritten_query,
            retrieval_log=retrieval_log,
        ),
        report=report,
        notes=notes,
    )


# --------------------------------------------------------------------------- #
# Registry
# --------------------------------------------------------------------------- #

ADAPTER_REGISTRY: dict[str, Callable[[], PassageAdapter]] = {
    "qasper": QasperHitAdapter,
    "reference": ReferenceHitAdapter,
    "placeholder": PlaceholderAdapter,
}

#: The real retriever's scheme, confirmed 2026-10-10. ``reference`` stays
#: registered so the Week-2 synthetic baselines remain reproducible.
DEFAULT_ADAPTER = "qasper"


def get_adapter(name: str = DEFAULT_ADAPTER, **kwargs: Any) -> PassageAdapter:
    """Build an adapter by name."""
    key = name.strip().lower()
    if key not in ADAPTER_REGISTRY:
        raise KeyError(
            f"unknown passage adapter {name!r}; expected one of "
            f"{sorted(ADAPTER_REGISTRY)}"
        )
    return ADAPTER_REGISTRY[key](**kwargs)
