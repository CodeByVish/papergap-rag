"""Generator interface and the lenient response parser.

Every backend returns **raw text**, never a validated object. Parsing happens in
exactly one place (:func:`parse_response`) so that the mock and Qwen3 paths are
held to the same standard: if the mock can produce something the parser accepts
or rejects, so can the real model, and the tests cover both through one code path.

The parser is forgiving on purpose. An 8B instruct model will wrap JSON in a
markdown fence, prepend "Sure! Here is the answer:", or rename ``citations`` to
``references``. None of those are grounding failures, so the parser recovers and
records the deviation in :class:`ParseDiagnostics`; the pipeline turns that record
into ``PROMPT_FORMAT_DRIFT`` / ``EXTRA_FIELDS_IGNORED`` warnings. What the parser
will *not* do is invent missing content - a response with no answer field raises
:class:`ResponseParseError` and the pipeline refuses.
"""

from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod
from typing import Any, ClassVar, Iterator, Mapping, Optional, Sequence

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from src.generation.prompts.grounded_qa import PromptConfig
from src.generation.schema import EvidenceStatus, GenerationRequest, GenerationResult


class BackendNotAvailable(RuntimeError):
    """Raised when a backend cannot run here: missing package or no GPU.

    The message always carries the exact install command or the reason, because
    whoever hits this is usually on a login node trying to find out why the model
    will not load. Every backend also raises this from ``load()`` rather than at
    import time, so that importing the module - and running the CPU-only test
    suite - never depends on torch being present.
    """


class ResponseParseError(ValueError):
    """Raised when no JSON object in the text yields a valid result."""

    def __init__(self, reason: str, raw_text: str, candidates_tried: int = 0) -> None:
        super().__init__(reason)
        self.reason = reason
        self.raw_text = raw_text
        self.candidates_tried = candidates_tried

    @property
    def excerpt(self) -> str:
        text = self.raw_text.strip()
        return text[:400] + (" [...]" if len(text) > 400 else "")


class ParseDiagnostics(BaseModel):
    """Non-fatal deviations observed while parsing one response.

    Purely observational - nothing here changes the parsed result. It exists so
    that a prompt that is quietly degrading (models increasingly padding the JSON
    with prose) shows up as a rising warning count in P6's error analysis rather
    than as an unexplained drop in citation precision.
    """

    model_config = ConfigDict(extra="forbid")

    had_code_fence: bool = False
    had_thinking_block: bool = False
    unclosed_thinking_block: bool = False
    leading_text_chars: int = 0
    trailing_text_chars: int = 0
    candidate_index: int = 0
    extra_fields: list[str] = Field(default_factory=list)
    coerced: list[str] = Field(default_factory=list)

    @property
    def drifted(self) -> bool:
        """True when the model did not emit a bare, exact JSON object."""
        return bool(
            self.had_code_fence
            or self.had_thinking_block
            or self.leading_text_chars
            or self.trailing_text_chars
            or self.extra_fields
            or self.coerced
        )


class GenerationStats(BaseModel):
    """What the most recent generation call actually cost.

    This exists because the Week-2 brief asks for inference latency and GPU
    memory data, and ``generate_batch`` otherwise returns raw text and nothing
    else. Everything here is optional, and that is deliberate: a backend that
    cannot measure a quantity must leave it ``None`` rather than report a
    plausible-looking ``0``. A fabricated zero silently deflates every average
    computed over it and is indistinguishable from a real measurement, which is
    the failure mode this project has already been bitten by once (see
    ``docs/GPU_FEASIBILITY.md`` §2 on the 30.5 GiB peak that was a bug, not a
    measurement).

    ``tokens_per_second`` is completion-only. Prefill throughput on a short
    prompt is a different number, dominated by a fixed cost, and mixing the two
    is how a benchmark reports a rate no reader can reproduce.
    """

    model_config = ConfigDict(extra="forbid")

    #: 1 for the single-request path (both real backends route
    #: ``_generate_text`` through ``generate_batch([request])``).
    batch_size: int = 1
    #: Real prompt tokens, not the padded tensor width.
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    #: Wall-clock inside the backend's own generate call, excluding the
    #: pipeline's parse and validate work.
    batch_seconds: Optional[float] = None

    @property
    def tokens_per_second(self) -> Optional[float]:
        if not self.completion_tokens or not self.batch_seconds:
            return None
        return self.completion_tokens / self.batch_seconds


# --------------------------------------------------------------------------- #
# Aliases the parser accepts for the canonical field names
# --------------------------------------------------------------------------- #

_FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "answer": ("answer", "response", "output", "text", "final_answer"),
    "citations": ("citations", "cited_passages", "references", "sources", "evidence_ids"),
    "evidence_status": ("evidence_status", "status", "evidence", "sufficiency"),
    "retrieval_rounds": ("retrieval_rounds", "rounds", "retrieval_round"),
    "provenance": ("provenance", "claims", "claim_evidence", "supporting_claims"),
}

#: Tag names used by the reasoning models this project might serve. Qwen3 uses
#: ``think``; the others are cheap insurance so a backend swap does not silently
#: start feeding a reasoning trace into the parser.
_THINK_TAGS = ("think", "thinking", "reasoning", "analysis")
_TAG_ALTERNATION = "|".join(_THINK_TAGS)
_OPEN_TAG_RE = re.compile(r"<(" + _TAG_ALTERNATION + r")>", re.IGNORECASE)
_CLOSE_TAG_RE = re.compile(r"</(" + _TAG_ALTERNATION + r")>", re.IGNORECASE)
_CLOSED_BLOCK_RE = re.compile(
    r"<(" + _TAG_ALTERNATION + r")>.*?</\1>", re.DOTALL | re.IGNORECASE
)


def _strip_thinking(text: str, diagnostics: ParseDiagnostics, limit: int) -> str:
    """Remove a Qwen3-style reasoning block from the response.

    Three cases, and the middle one is the one that actually happens:

    1. A matched ``<think>...</think>`` pair - strip the whole block.
    2. **A bare closing tag with no opening tag.** Qwen3's chat template puts the
       opening tag at the *end of the prompt*, so when thinking is on, the text
       generated by the model is just the reasoning followed by ``</think>``. A
       parser that looks for a matched pair misses every real occurrence, so
       everything up to the closing tag is treated as reasoning.
    3. An opening tag that is never closed - generation hit the token limit
       mid-reasoning. The text is left intact so the brace scanner can still find
       a JSON object if one is present; the truncation is recorded instead.

    All three set :attr:`ParseDiagnostics.had_thinking_block`, because Qwen3 is
    supposed to run with ``enable_thinking=False``: seeing any of them means the
    switch did not take effect.

    ``limit`` is the offset where the first JSON object begins, and only the text
    before it is searched for tags. Reasoning always precedes the answer, so this
    does not lose real traces - but it does stop an answer that legitimately
    *quotes* a reasoning tag (``"The <thinking> step is described in the paper."``)
    from being chopped in half.
    """
    region = text[:limit]
    open_match = _OPEN_TAG_RE.search(region)
    close_matches = list(_CLOSE_TAG_RE.finditer(region))

    if open_match and any(m.start() > open_match.start() for m in close_matches):
        diagnostics.had_thinking_block = True
        return _CLOSED_BLOCK_RE.sub("", text, count=1)

    if close_matches:
        diagnostics.had_thinking_block = True
        return text[close_matches[0].end() :]

    if open_match:
        diagnostics.had_thinking_block = True
        diagnostics.unclosed_thinking_block = True

    return text


def _first_json_start(text: str) -> int:
    """Offset of the first balanced top-level object, or ``len(text)`` if none."""
    for start, _end, _candidate in _iter_json_candidates(text):
        return start
    return len(text)


def _iter_json_candidates(text: str) -> Iterator[tuple[int, int, str]]:
    """Yield ``(start, end, substring)`` for every balanced top-level object.

    A brace counter that ignores braces inside JSON strings. Prose before the
    JSON can contain a stray ``{`` (``Here is the JSON {as requested}:``), which
    would make a naive "first ``{`` to last ``}``" slice invalid - so candidates
    are yielded in order and the caller tries each one.
    """
    depth = 0
    start: int | None = None
    in_string = False
    escaped = False

    for index, char in enumerate(text):
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == "{":
            if depth == 0:
                start = index
            depth += 1
            continue

        if depth > 0:
            if char == '"':
                in_string = True
            elif char == "}":
                depth -= 1
                if depth == 0 and start is not None:
                    yield start, index + 1, text[start : index + 1]
                    start = None


def _normalize_payload(
    payload: dict[str, Any], diagnostics: ParseDiagnostics
) -> dict[str, Any]:
    """Map tolerated aliases onto canonical field names.

    Unknown keys are dropped (the schema is ``extra="ignore"``) but their names
    are recorded so a model that insists on adding ``"reasoning"`` or
    ``"confidence"`` is visible in the report rather than silently ignored.
    """
    known: set[str] = set()
    normalized: dict[str, Any] = {}

    for canonical, aliases in _FIELD_ALIASES.items():
        known.update(aliases)
        if canonical in payload:
            normalized[canonical] = payload[canonical]
            continue
        for alias in aliases:
            if alias in payload:
                normalized[canonical] = payload[alias]
                if alias != canonical:
                    diagnostics.coerced.append(f"{alias}->{canonical}")
                break

    diagnostics.extra_fields.extend(
        sorted(key for key in payload if key not in known)
    )

    if "evidence_status" not in normalized:
        # Refusing by default is the safe failure: an undeclared status must not
        # be read as a licence to answer. If the model really meant SUFFICIENT it
        # will have said so, and the validator would reject the answer anyway for
        # the missing declaration.
        normalized["evidence_status"] = EvidenceStatus.INSUFFICIENT.value
        diagnostics.coerced.append("<missing>->evidence_status:INSUFFICIENT")
    elif isinstance(normalized["evidence_status"], str):
        raw = normalized["evidence_status"]
        try:
            resolved = EvidenceStatus(raw)
        except ValueError:
            resolved = EvidenceStatus.INSUFFICIENT
        if resolved.value != raw:
            diagnostics.coerced.append(f"evidence_status:{raw}->{resolved.value}")
        normalized["evidence_status"] = resolved.value

    if "retrieval_rounds" in normalized and isinstance(
        normalized["retrieval_rounds"], str
    ):
        raw_rounds = normalized["retrieval_rounds"].strip()
        if raw_rounds.isdigit():
            normalized["retrieval_rounds"] = int(raw_rounds)
            diagnostics.coerced.append("retrieval_rounds:str->int")

    if "provenance" in normalized and isinstance(normalized["provenance"], str):
        # A model that emits provenance as a prose sentence loses the structure
        # but should not lose the answer.
        normalized["provenance"] = []
        diagnostics.coerced.append("provenance:str->[]")

    return normalized


def parse_response(text: str) -> tuple[GenerationResult, ParseDiagnostics]:
    """Extract a :class:`GenerationResult` from a model response.

    Raises :class:`ResponseParseError` when no candidate object parses *and*
    validates. The error carries the last validation failure so a batch run can
    report *why* responses were unparseable instead of just how many.
    """
    diagnostics = ParseDiagnostics()
    cleaned = _strip_thinking(text, diagnostics, limit=_first_json_start(text))
    if "```" in cleaned:
        diagnostics.had_code_fence = True

    last_error = "no JSON object found in the response"
    tried = 0

    for index, (start, end, candidate) in enumerate(_iter_json_candidates(cleaned)):
        tried = index + 1
        try:
            payload = json.loads(candidate)
        except json.JSONDecodeError as exc:
            last_error = f"invalid JSON at candidate {index}: {exc.msg}"
            continue

        if not isinstance(payload, dict):
            last_error = f"candidate {index} is a {type(payload).__name__}, not an object"
            continue

        normalized = _normalize_payload(payload, diagnostics)
        try:
            result = GenerationResult.model_validate(normalized)
        except ValidationError as exc:
            first = exc.errors()[0]
            location = ".".join(str(part) for part in first["loc"]) or "<root>"
            last_error = f"schema validation failed at {location}: {first['msg']}"
            continue

        diagnostics.candidate_index = index
        diagnostics.leading_text_chars = len(cleaned[:start].strip())
        diagnostics.trailing_text_chars = len(cleaned[end:].strip())
        return result, diagnostics

    raise ResponseParseError(last_error, text, candidates_tried=tried)


# --------------------------------------------------------------------------- #
# Backend interface
# --------------------------------------------------------------------------- #


class GeneratorBackend(ABC):
    """Common interface for the mock, Transformers and vLLM generators.

    Loading is lazy and idempotent: constructing a backend never touches the GPU,
    so the mock path and the test suite can import every module on a CPU-only
    machine. Call :meth:`load` explicitly when you want to control *when* the
    weights land in VRAM, or use the backend as a context manager.
    """

    #: Short identifier used by :func:`src.generation.generators.get_generator`.
    name: ClassVar[str] = "base"

    #: True when the backend can serve a batch more efficiently than a loop.
    supports_batch: ClassVar[bool] = False

    def __init__(self, model_id: str, **options: Any) -> None:
        self.model_id = model_id
        self.options = options
        self._loaded = False
        #: How much evidence this backend puts in front of the model. Declared
        #: here rather than in each backend so every backend has one uniformly,
        #: and so :class:`~src.generation.pipeline.GroundedQAPipeline` can make its own
        #: config authoritative by assigning to it - see the pipeline's
        #: ``__init__`` for why that matters to citation validation.
        self.prompt_config: PromptConfig = PromptConfig()
        #: Cost of the most recent generation, or ``None`` when the backend
        #: cannot measure it (the mock has no tokenizer). "last" is load-bearing:
        #: it is overwritten by every call, so it describes this call and not a
        #: run - for anything aggregated over a batch, read it per call.
        self.last_generation_stats: Optional[GenerationStats] = None

    # -- lifecycle --------------------------------------------------------- #

    def load(self) -> None:
        """Acquire the model. Public entry point; idempotent.

        The ``_loaded`` flag is set here and nowhere else, so loading happens
        once however it was reached. Subclasses override :meth:`_load`, not this
        method.

        The indirection is load-bearing. When each backend set the flag inside
        its own ``load``, a caller that invoked ``load()`` directly - which
        ``scripts/smoke_test_qwen3.py`` does - left ``_loaded`` False, and the
        next :meth:`generate` called ``load()`` a *second* time. Two backends,
        two ways to fail: Transformers held two copies of the weights, so
        15.26 GiB became a 30.5 GiB peak, and vLLM tried to start a second
        engine beside the first, which cannot work because the first still owns
        the VRAM and the second fails its own memory check.
        """
        if self._loaded:
            return
        self._load()
        self._loaded = True

    def _load(self) -> None:
        """Acquire the model. Backends override; the default is a no-op."""

    def unload(self) -> None:
        """Release the model and mark the backend unloaded.

        Subclasses override this to free their own resources and **must** call
        ``super().unload()``. Resetting the flag is not bookkeeping: if it stayed
        set, a later :meth:`generate` would skip ``load()`` and hand a released
        model to ``_generate_text``, which surfaces as an AttributeError deep
        inside a batch rather than as an obvious "not loaded" error.

        The stats are cleared for the same reason. They describe a call made by
        a model that no longer exists, and a record written after an unload
        would otherwise attribute a previous phase's token counts to a request
        that was never generated.
        """
        self._loaded = False
        self.last_generation_stats = None

    def _ensure_loaded(self) -> None:
        self.load()

    def __enter__(self) -> "GeneratorBackend":
        self._ensure_loaded()
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.unload()

    # -- generation -------------------------------------------------------- #

    @abstractmethod
    def _generate_text(self, request: GenerationRequest) -> str:
        """Produce the raw response text for one request."""

    def generate(self, request: GenerationRequest) -> str:
        """Raw response text. Always unparsed - see :func:`parse_response`."""
        self._ensure_loaded()
        return self._generate_text(request)

    def generate_batch(self, requests: Sequence[GenerationRequest]) -> list[str]:
        """Raw responses for many requests, in input order.

        The default is a sequential loop. Subclasses override when the serving
        stack offers real batching.
        """
        return [self.generate(request) for request in requests]

    # -- schema-agnostic chat ---------------------------------------------- #
    #
    # P5's ``generate`` path owns the grounded-QA prompt. A caller that needs
    # the same loaded model for a *different* prompt - P4's evidence critic is
    # the motivating case - must not build a second engine: one 8B model already
    # fills a 45 GiB card, and a second load costs a whole job slot. ``chat``
    # is the supported way in. It returns raw text and never parses; the caller
    # owns its own schema and validation.

    def chat(
        self,
        messages: Sequence[Mapping[str, str]],
        *,
        max_new_tokens: int = 256,
        temperature: float = 0.0,
        top_p: float = 0.9,
        enable_thinking: Optional[bool] = None,
    ) -> str:
        """Raw text for one arbitrary chat conversation.

        Parameters
        ----------
        messages:
            ``[{"role": "system"|"user", "content": "..."}]``. The backend
            applies the model's own chat template; do not hand-format control
            tokens.
        max_new_tokens:
            Completion budget. The default is sized for a short JSON reply, not
            for a grounded answer with provenance (P5's ``generate`` uses 768).
        temperature, top_p:
            Sampling. The default is greedy and reproducible, which is what a
            classifier-style critic should use.
        enable_thinking:
            ``None`` uses the backend's configured value (Qwen3 defaults to
            thinking *on*, and both backends configure it *off*). Pass ``True``
            only if you deliberately want a reasoning trace.

        Returns
        -------
        str
            Raw response text, never parsed or validated. Use the same
            brace-scanner + Pydantic validation discipline as
            :func:`parse_response` on your own schema.
        """
        return self.chat_batch(
            [messages],
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            enable_thinking=enable_thinking,
        )[0]

    def chat_batch(
        self,
        conversations: Sequence[Sequence[Mapping[str, str]]],
        *,
        max_new_tokens: int = 256,
        temperature: float = 0.0,
        top_p: float = 0.9,
        enable_thinking: Optional[bool] = None,
    ) -> list[str]:
        """Raw responses for many arbitrary conversations, in input order.

        The default raises rather than silently looping: a backend that cannot
        honour the per-call sampling settings would otherwise make a critic's
        temperature-0 guarantee quietly false. The mock, Transformers and vLLM
        backends implement it.
        """
        raise NotImplementedError(
            f"{type(self).__name__} does not implement chat(); use the mock, "
            "transformers or vllm backend"
        )

    # -- introspection ----------------------------------------------------- #

    def info(self) -> dict[str, Any]:
        """Metadata for the run log, so a result file is self-describing.

        :attr:`GroundedQAPipeline <src.generation.pipeline.GroundedQAPipeline>` embeds
        this on every return path, so anything added here lands in every answers
        record and every batch file with no plumbing at all. That is why the
        token counts live here rather than in a parallel structure: the cost of
        an answer travels with the answer.

        One trap for a consumer. On the empty-context short-circuit the model is
        never called, so ``last_generation_stats`` still describes the
        *previous* request. Detect that case structurally - ``raw_text`` and
        ``diagnostics`` are both ``None`` - rather than trusting the stats.
        """
        return {
            "backend": self.name,
            "model_id": self.model_id,
            "loaded": self._loaded,
            "options": self.options,
            "last_generation_stats": (
                self.last_generation_stats.model_dump(mode="json")
                if self.last_generation_stats is not None
                else None
            ),
        }

    def __repr__(self) -> str:
        return f"<{type(self).__name__} model_id={self.model_id!r} loaded={self._loaded}>"
