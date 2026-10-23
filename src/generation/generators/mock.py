"""Mock generator - a dependency-free stand-in for Qwen3-8B.

This is the P5 "mock generated-answer JSON" deliverable, and it is built to be
useful rather than merely present. Two properties make it worth more than a
hard-coded fixture:

* **It emits raw text, not objects.** The mock goes through exactly the same
  parse-then-validate path as Qwen3 would, so running the pipeline on the mock
  exercises :func:`src.generation.generators.base.parse_response`, the validator and the
  downgrade logic. A structural bug in any of them fails on a CPU-only machine.
* **Its grounded answers are grounded by construction.** The ``grounded``
  scenario copies whole sentences out of the retrieved passages, so every number
  it states provably occurs in a passage it cites. It is a *known-good* baseline:
  if the mock is downgraded, the bug is in P5, not in the model.

The remaining scenarios are deliberate rule breaks, one per failure mode the
validator claims to catch. Together they are the negative half of the P5 test
matrix, and they double as the "what does a violation look like" reference for
P6's error analysis.

The mock does not pretend to reason: it copies sentences. Do not read anything
into its answer quality.
"""

from __future__ import annotations

import json
from enum import Enum
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict

from src.generation.generators.base import GeneratorBackend
from src.generation.schema import (
    REFUSAL_ANSWER,
    EvidenceStatus,
    GenerationRequest,
    Support,
)
from src.generation.text_utils import split_sentences

CLOSE_THINKING_TAG = "</think>"

#: Numbers checked in order when the ``unsupported_number`` scenario needs a
#: value that is guaranteed absent from the retrieved passages. Common enough to
#: look plausible in a results sentence, distinctive enough not to collide.
_NUMBER_CANDIDATES = ("47.3", "97.31", "1234567", "8.88", "63.7", "31415")


class MockScenario(str, Enum):
    """One behaviour per row of the P5 test matrix."""

    # -- expected to pass validation cleanly ---------------------------------
    GROUNDED = "grounded"
    FENCED = "fenced"
    THINKING = "thinking"

    # -- legitimate refusal --------------------------------------------------
    REFUSAL = "refusal"

    # -- rule breaks that must trigger a downgrade ---------------------------
    HALLUCINATED_CITATION = "hallucinated_citation"
    UNSUPPORTED_NUMBER = "unsupported_number"
    SUFFICIENT_WITHOUT_CITATION = "sufficient_without_citation"
    INVALID_JSON = "invalid_json"
    MISSING_FIELD = "missing_field"

    # -- rule breaks that must stay WARNING-level ----------------------------
    PARTIAL = "partial"
    NO_PROVENANCE = "no_provenance"


#: Order used when ``scenario=None``. Deterministic, so a batch run is
#: reproducible and a failure can be traced back to a specific request index.
DEFAULT_CYCLE: tuple[MockScenario, ...] = (
    MockScenario.GROUNDED,
    MockScenario.REFUSAL,
    MockScenario.PARTIAL,
    MockScenario.HALLUCINATED_CITATION,
    MockScenario.UNSUPPORTED_NUMBER,
    MockScenario.NO_PROVENANCE,
    MockScenario.SUFFICIENT_WITHOUT_CITATION,
    MockScenario.FENCED,
    MockScenario.INVALID_JSON,
    MockScenario.MISSING_FIELD,
)


class MockConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    #: How many passages to base the answer on. Kept small so the mock answer
    #: stays readable in the example JSON.
    max_claims: int = 3

    #: Indent the emitted JSON. Off by default so the mock looks like a real
    #: model response; the example artefacts turn it on for readability.
    pretty: bool = False

    #: Canned reply for :meth:`MockGenerator.chat`. The mock has no prompt
    #: understanding, so this is an echo-free fixed string. A caller testing its
    #: own schema (P4's critic, for example) should set this to a valid reply
    #: for that schema.
    chat_response: str = '{"response": "mock chat response"}'


def _first_sentence(text: str) -> str:
    """First sentence of a passage, or the whole thing if splitting fails."""
    sentences = split_sentences(text)
    return sentences[0] if sentences else text.strip()


class MockGenerator(GeneratorBackend):
    """A generator that returns valid structured responses, with knobs to break them.

    Parameters
    ----------
    scenario:
        A specific :class:`MockScenario`, or ``None`` to cycle deterministically
        through :data:`DEFAULT_CYCLE` across successive calls.
    config:
        :class:`MockConfig`; ``max_claims`` and ``pretty``.

    Examples
    --------
    >>> generator = MockGenerator(MockScenario.GROUNDED)
    >>> text = generator.generate(request)          # doctest: +SKIP
    >>> result, diagnostics = parse_response(text)  # doctest: +SKIP
    """

    name: ClassVar[str] = "mock"
    supports_batch: ClassVar[bool] = True

    def __init__(
        self,
        scenario: MockScenario | None = None,
        config: MockConfig | None = None,
        model_id: str = "mock-generator",
        **options: Any,
    ) -> None:
        super().__init__(model_id=model_id, **options)
        self.scenario = MockScenario(scenario) if scenario is not None else None
        self.config = config or MockConfig()
        self._calls = 0

    # -- GeneratorBackend -------------------------------------------------- #

    def _generate_text(self, request: GenerationRequest) -> str:
        scenario = self._pick_scenario()
        payload = self._build_payload(scenario, request)
        return self._render(scenario, payload, request)

    def generate_batch(self, requests: Any) -> list[str]:
        """Sequential by design: the cycle must advance one request at a time."""
        return [self.generate(request) for request in requests]

    def chat_batch(
        self,
        conversations: Any,
        *,
        max_new_tokens: int = 256,
        temperature: float = 0.0,
        top_p: float = 0.9,
        enable_thinking: Any = None,
    ) -> list[str]:
        """The same canned reply for every conversation.

        Kept deliberately dumb: a mock that pretends to understand a critic
        prompt would let a caller's parsing bug pass locally and fail on the
        cluster. Set ``MockConfig.chat_response`` to a valid reply for *your*
        schema when you want an end-to-end shape check.
        """
        self._ensure_loaded()
        return [self.config.chat_response for _ in conversations]

    def info(self) -> dict[str, Any]:
        info = super().info()
        info["scenario"] = self.scenario.value if self.scenario else "cycle"
        info["max_claims"] = self.config.max_claims
        return info

    # -- internals --------------------------------------------------------- #

    def _pick_scenario(self) -> MockScenario:
        self._calls += 1
        if self.scenario is not None:
            return self.scenario
        return DEFAULT_CYCLE[(self._calls - 1) % len(DEFAULT_CYCLE)]

    def _build_payload(
        self, scenario: MockScenario, request: GenerationRequest
    ) -> dict[str, Any]:
        """The JSON payload for a scenario, before rendering to text."""
        # Refusal is the only sane behaviour with no evidence, and it takes
        # precedence over the scenario - EXCEPT for the malformed-output
        # scenarios, which must keep breaking so the parse path stays covered.
        malformed = {
            MockScenario.INVALID_JSON,
            MockScenario.MISSING_FIELD,
        }
        if not request.passages and scenario not in malformed:
            return self._refusal_payload(request)

        if scenario is MockScenario.REFUSAL:
            return self._refusal_payload(request)

        payload = self._grounded_payload(request)

        if scenario is MockScenario.PARTIAL:
            # An extra sentence with no passage behind it. No numbers, so only
            # R2 can catch it - which is exactly the WARNING-level case.
            payload["answer"] = (
                payload["answer"]
                + " This finding is consistent with the broader direction of the "
                "field and strengthens the overall argument."
            )
        elif scenario is MockScenario.NO_PROVENANCE:
            payload["provenance"] = []
        elif scenario is MockScenario.SUFFICIENT_WITHOUT_CITATION:
            payload["citations"] = []
        elif scenario is MockScenario.HALLUCINATED_CITATION:
            payload["citations"] = payload["citations"] + [
                self._invent_passage_id(request)
            ]
        elif scenario is MockScenario.UNSUPPORTED_NUMBER:
            payload["answer"] = (
                payload["answer"]
                + f" This corresponds to an improvement of {self._absent_number(request)}"
                " percent over prior work."
            )
        elif scenario is MockScenario.MISSING_FIELD:
            payload.pop("answer", None)

        return payload

    def _grounded_payload(self, request: GenerationRequest) -> dict[str, Any]:
        """A grounded answer, assembled verbatim from the retrieved passages."""
        passages = request.ordered_passages()[: max(1, self.config.max_claims)]
        claims: list[str] = []
        provenance: list[dict[str, Any]] = []

        for passage in passages:
            claim = _first_sentence(passage.text)
            if not claim:
                continue
            claims.append(claim)
            provenance.append(
                {
                    "claim": claim,
                    "passage_ids": [passage.passage_id],
                    "support": Support.DIRECT.value,
                }
            )

        if not claims:
            # Passages existed but carried no usable sentence.
            return self._refusal_payload(request)

        return {
            "answer": " ".join(claims),
            "citations": [entry["passage_ids"][0] for entry in provenance],
            "evidence_status": EvidenceStatus.SUFFICIENT.value,
            "retrieval_rounds": request.retrieval_rounds,
            "provenance": provenance,
        }

    def _refusal_payload(self, request: GenerationRequest) -> dict[str, Any]:
        return {
            "answer": REFUSAL_ANSWER,
            "citations": [],
            "evidence_status": EvidenceStatus.INSUFFICIENT.value,
            "retrieval_rounds": request.retrieval_rounds,
            "provenance": [],
        }

    def _invent_passage_id(self, request: GenerationRequest) -> str:
        """A plausible-looking id that was definitely not retrieved."""
        retrieved = set(request.passage_ids)
        stem = "paper999"
        if request.passages and request.passages[0].paper_id:
            stem = request.passages[0].paper_id
        candidate = f"{stem}_appendix_99"
        suffix = 0
        while candidate in retrieved:
            suffix += 1
            candidate = f"{stem}_appendix_99_{suffix}"
        return candidate

    def _absent_number(self, request: GenerationRequest) -> str:
        """A plausible statistic that appears in none of the passages."""
        haystack = " ".join(p.text for p in request.passages)
        for candidate in _NUMBER_CANDIDATES:
            if candidate not in haystack:
                return candidate
        return _NUMBER_CANDIDATES[0]

    def _render(
        self,
        scenario: MockScenario,
        payload: dict[str, Any],
        request: GenerationRequest,
    ) -> str:
        """Turn a payload into the raw text a real model might have emitted."""
        indent = 2 if self.config.pretty else None
        body = json.dumps(payload, indent=indent, ensure_ascii=False)

        if scenario is MockScenario.INVALID_JSON:
            # Truncated mid-string, plus a chatty preamble: the two ways a real
            # response usually fails to parse.
            return (
                "Sure! Here is the answer.\n\n"
                '{"answer": "The proposed method achieves a substantial '
                'improvement over the baseline, reaching 9'
            )

        if scenario is MockScenario.FENCED:
            return f"```json\n{body}\n```"

        if scenario is MockScenario.THINKING:
            # The realistic shape of a Qwen3 response when enable_thinking did
            # not take effect: the chat template places the OPENING tag at the end
            # of the prompt, so only the CLOSING tag comes back - preceded by the
            # reasoning trace and followed by the answer.
            return (
                "The user wants a grounded answer. I should check which passages "
                "contain the relevant result before citing anything.\n\n"
                + CLOSE_THINKING_TAG
                + "\n\n"
                + body
            )

        return body
