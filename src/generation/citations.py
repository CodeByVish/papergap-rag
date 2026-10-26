"""The citation rules and the validator that enforces them.

Four rules, straight from the P5 brief:

R1  citations must reference retrieved passages
R2  each factual claim should have evidence
R3  unsupported numerical claims are prohibited
R4  insufficient evidence must produce a refusal

They are deliberately **not** enforced with equal force, and that asymmetry is
the central design decision of this module:

* R1, R3 and the un-refused half of R4 are ``ERROR``. A hallucinated citation or
  an invented number is a fabrication, the answer cannot be repaired by keeping
  it, so the validator *downgrades* the whole result to a refusal.
* R2 is ``WARNING``. Deciding whether a sentence "has evidence" needs judgement;
  a token-overlap heuristic is not good enough to throw away an otherwise
  grounded answer, so R2 findings are recorded for P6's error analysis instead.

Downgrading keeps the original in ``ValidationReport.raw_result`` and leaves
``final_result`` self-consistent: a refusal cites nothing and claims nothing.
Losing the model's fabricated citations from the *final* object is intentional -
it is exactly what stops a hallucinated citation from reaching P6's evaluator.
"""

from __future__ import annotations

from enum import Enum
from typing import Iterable, Optional, Sequence

from pydantic import BaseModel, ConfigDict, Field

from src.generation.provenance import overstated_claims
from src.generation.prompts.grounded_qa import PromptScope
from src.generation.schema import (
    SCHEMA_VERSION,
    EvidenceStatus,
    GenerationRequest,
    GenerationResult,
    RetrievedPassage,
    refusal_result,
)
from src.generation.text_utils import (
    content_tokens,
    extract_numbers,
    number_index,
    question_clauses,
    split_sentences,
    token_overlap_recall,
)


class Severity(str, Enum):
    """``ERROR`` invalidates the answer; ``WARNING`` is diagnostic only."""

    ERROR = "error"
    WARNING = "warning"


class ViolationCode(str, Enum):
    """Stable identifiers so P6 can aggregate failures across runs."""

    # R1 - citations must reference retrieved passages.
    HALLUCINATED_CITATION = "HALLUCINATED_CITATION"
    #: Retrieved, but not among the passages the prompt actually rendered. The
    #: model cited something it never read. Distinct from the above because the
    #: two need different fixes - one is a prompt-grounding failure, this one is
    #: a context-budget failure - and because only this one is detectable from
    #: the retrieved set alone.
    CITATION_NOT_IN_PROMPT = "CITATION_NOT_IN_PROMPT"

    # R2 - each factual claim should have evidence.
    UNSUPPORTED_CLAIM = "UNSUPPORTED_CLAIM"
    CLAIM_WITHOUT_EVIDENCE = "CLAIM_WITHOUT_EVIDENCE"
    CITATION_PROVENANCE_MISMATCH = "CITATION_PROVENANCE_MISMATCH"
    #: The model asserted stronger support than the text bears out.
    PROVENANCE_OVERSTATED = "PROVENANCE_OVERSTATED"

    # R3 - unsupported numerical claims are prohibited.
    UNSUPPORTED_NUMERIC_CLAIM = "UNSUPPORTED_NUMERIC_CLAIM"
    #: The number was in a passage the model was shown but not in its citation
    #: list, so the passage was added. A warning, not an error: the answer is
    #: grounded in evidence the model read; only the citation was incomplete.
    CITATION_REPAIRED_FOR_NUMBER = "CITATION_REPAIRED_FOR_NUMBER"

    # R4 - insufficient evidence must produce a refusal.
    SUFFICIENT_WITHOUT_CITATION = "SUFFICIENT_WITHOUT_CITATION"
    MISSING_REFUSAL = "MISSING_REFUSAL"
    REFUSAL_WITH_CITATIONS = "REFUSAL_WITH_CITATIONS"
    #: The question asks several things and the cited evidence covers only some
    #: of them, yet the answer is marked SUFFICIENT. A consumer reading that
    #: status would believe every part was answered.
    UNCOVERED_QUESTION_CLAUSE = "UNCOVERED_QUESTION_CLAUSE"
    #: P4 mapped a required component to passages, but the answer cites none of
    #: them. Structural counterpart to the token-overlap clause check above.
    UNCOVERED_REQUIRED_COMPONENT = "UNCOVERED_REQUIRED_COMPONENT"

    # Pipeline-level observations about how the model answered, not the content.
    GENERATION_ERROR = "GENERATION_ERROR"
    PARSE_ERROR = "PARSE_ERROR"
    PROMPT_FORMAT_DRIFT = "PROMPT_FORMAT_DRIFT"
    EXTRA_FIELDS_IGNORED = "EXTRA_FIELDS_IGNORED"

    #: Retrieval returned nothing, so the model was never called. Distinguishes
    #: "there was no context" from "the context was judged insufficient" - both
    #: surface to P6 as a refusal, and they are not the same result.
    EMPTY_CONTEXT = "EMPTY_CONTEXT"
    #: The agent's critic labelled the gap ``INSUFFICIENT_INFORMATION``, so P5
    #: refused without calling the model. Distinct from EMPTY_CONTEXT (there
    #: were passages, but the critic judged them unanswerable).
    AGENT_INSUFFICIENT = "AGENT_INSUFFICIENT"
    #: The critic said ``sufficient=False`` but did not label the gap
    #: ``INSUFFICIENT_INFORMATION``, so P5 generated from the available
    #: passages anyway. The answer is kept; this code lets P6 count "answered
    #: under critic doubt" separately from an actual refusal.
    GENERATED_WITH_INSUFFICIENT_EVIDENCE = "GENERATED_WITH_INSUFFICIENT_EVIDENCE"
    #: The pipeline filled in ``provenance`` because the model did not return
    #: any. The entries are derived, not model-authored.
    PROVENANCE_DERIVED = "PROVENANCE_DERIVED"


class ValidationConfig(BaseModel):
    """Knobs for the validator. Defaults are what P5 ships and P6 should use."""

    model_config = ConfigDict(extra="forbid")

    #: Turn an ERROR-level violation into a refusal instead of raising. This is
    #: the "soft fail + auto-downgrade" policy agreed for P5: one bad sample must
    #: not abort a 6-hour batch, and a fabrication must not reach the evaluator.
    downgrade_on_error: bool = True

    #: Rewrite refusals to the canonical text and clear their citations, so P6
    #: can detect a refusal by equality and refusal rate is comparable across
    #: prompts. Set False to inspect the model's own refusal wording.
    normalize_refusal: bool = True

    check_numeric_grounding: bool = True
    #: Repair an uncited-but-rendered number by adding the passage that contains
    #: it to ``citations``, instead of discarding the answer as an error.
    #:
    #: Week 5, record 43: the model answered "31 categories ... 2 top ..." and
    #: cited one passage, while 31 and 2 were in another passage it had been
    #: shown. The answer was correct and the omission was a citation defect, not
    #: a hallucination. Repair keeps the guarantee that every number is in a
    #: passage the model read *and* in a cited passage, while not throwing away
    #: a grounded answer. A number absent from every rendered passage is still
    #: an ERROR and still downgrades.
    repair_numeric_citations: bool = True
    check_claim_coverage: bool = True

    #: Report question clauses the cited evidence does not cover. Only runs when
    #: a :class:`~src.generation.prompts.grounded_qa.PromptScope` was supplied, because
    #: "covered" is a statement about the evidence actually shown.
    check_question_coverage: bool = True

    #: A number that also appears in the *question* is not a new factual claim by
    #: the model (e.g. re-stating "SQuAD 2.0" from "What is the F1 on SQuAD
    #: 2.0?"). Exempting it avoids flagging the question's own constants.
    allow_numbers_from_question: bool = True

    #: Minimum content-token recall between an answer sentence and a provenance
    #: claim (or cited passage text) before the sentence counts as unsupported.
    claim_coverage_threshold: float = 0.35

    #: Sentences with fewer content tokens than this are skipped by the coverage
    #: check - "In summary." carries no factual content to verify.
    min_claim_tokens: int = 3

    #: Minimum content-token recall between a question clause and the cited
    #: evidence before the clause counts as covered. Same value as the claim
    #: threshold because it answers the same question at a different granularity.
    question_clause_threshold: float = 0.35


class ValidationViolation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ViolationCode
    severity: Severity
    message: str
    #: The offending item: a passage id, a number, or a truncated sentence.
    subject: Optional[str] = None


class ValidationReport(BaseModel):
    """Audit trail for one generated answer.

    ``raw_result`` is always the generator's parsed output; ``final_result`` is
    what P6 must consume. They differ only when the validator intervened.
    """

    model_config = ConfigDict(extra="forbid")

    final_result: GenerationResult
    raw_result: Optional[GenerationResult] = None
    violations: list[ValidationViolation] = Field(default_factory=list)
    downgraded: bool = False
    downgrade_reason: Optional[str] = None
    checks_run: list[str] = Field(default_factory=list)
    schema_version: str = SCHEMA_VERSION

    @property
    def errors(self) -> list[ValidationViolation]:
        return [v for v in self.violations if v.severity is Severity.ERROR]

    @property
    def warnings(self) -> list[ValidationViolation]:
        return [v for v in self.violations if v.severity is Severity.WARNING]

    @property
    def ok(self) -> bool:
        """True when no ERROR-level rule was broken."""
        return not self.errors

    def codes(self) -> list[str]:
        """Distinct violation codes, in first-seen order."""
        seen: list[str] = []
        for violation in self.violations:
            if violation.code.value not in seen:
                seen.append(violation.code.value)
        return seen


def _dedupe(violations: Iterable[ValidationViolation]) -> list[ValidationViolation]:
    """Drop exact duplicates.

    The same hallucinated id can be reported by both the citation check and the
    provenance check; two identical lines in the report add noise, not evidence.
    """
    out: list[ValidationViolation] = []
    seen: set[tuple[str, str, str | None]] = set()
    for violation in violations:
        key = (violation.code.value, violation.severity.value, violation.subject)
        if key not in seen:
            seen.add(key)
            out.append(violation)
    return out


class CitationValidator:
    """Enforces R1-R4 over one :class:`GenerationResult`."""

    def __init__(self, config: ValidationConfig | None = None) -> None:
        self.config = config or ValidationConfig()

    # -- public API -------------------------------------------------------- #

    def validate(
        self,
        result: GenerationResult,
        request: GenerationRequest,
        extra_violations: Sequence[ValidationViolation] = (),
        scope: Optional[PromptScope] = None,
    ) -> ValidationReport:
        """Check ``result`` against the rules and downgrade it if it breaks one.

        ``extra_violations`` carries observations the validator cannot make on
        its own - prompt-format drift and ignored extra fields detected while
        parsing the model's raw text.

        ``scope`` is what the prompt actually rendered, when the caller knows.
        Without it the checks fall back to the *retrieved* set, which is the
        pre-Week-3 behaviour and is too permissive: a retriever returning more
        hits than ``PromptConfig.max_passages`` leaves passages the model never
        saw, and a citation to one of them used to sail through. Pass it. The
        pipeline always does.

        Note what is deliberately *not* here: the new checks are folded into the
        existing rule names rather than appended as new ones, so ``checks_run``
        stays a stable five entries and each name still maps to one of the four
        rules. Adding a sixth entry would be a contract change for a diagnostic
        field, which is not worth it.
        """
        retrieved = request.passage_map()
        violations: list[ValidationViolation] = list(extra_violations)
        checks: list[str] = []

        checks.append("R1_citation_reference")
        valid_citations = self._check_citation_reference(
            result, retrieved, scope, violations
        )

        checks.append("R1b_provenance_reference")
        self._check_provenance_reference(result, retrieved, scope, violations)

        checks.append("R4_evidence_status")
        self._check_evidence_status(result, request, valid_citations, violations)
        if self.config.check_question_coverage:
            self._check_question_coverage(
                result, request, scope, valid_citations, violations
            )
        # P4's evidence map is structural rather than a token heuristic, so it
        # runs even when the clause check is disabled.
        self._check_required_components(
            result, request, scope, valid_citations, violations
        )

        # Snapshot the model's own parsed output before R3, which may add a
        # passage to ``citations`` in place. ``raw_result`` is the audit trail of
        # what the model said; a repaired citation belongs only in the final
        # result, or a reviewer would think the model cited a passage it omitted.
        raw_result = result.model_copy(deep=True)

        if self.config.check_numeric_grounding:
            checks.append("R3_numeric_grounding")
            self._check_numeric_grounding(
                result, request, valid_citations, retrieved, scope, violations
            )

        if self.config.check_claim_coverage:
            checks.append("R2_claim_coverage")
            self._check_claim_coverage(
                result, retrieved, valid_citations, scope, violations
            )
            self._check_provenance_support(result, retrieved, scope, violations)

        violations = _dedupe(violations)
        final_result, downgraded, reason = self._finalize(result, violations)

        return ValidationReport(
            final_result=final_result,
            raw_result=raw_result,
            violations=violations,
            downgraded=downgraded,
            downgrade_reason=reason,
            checks_run=checks,
        )

    # -- R1 ---------------------------------------------------------------- #

    def _check_citation_reference(
        self,
        result: GenerationResult,
        retrieved: dict[str, RetrievedPassage],
        scope: Optional[PromptScope],
        violations: list[ValidationViolation],
    ) -> list[str]:
        """Every cited id must be a passage the model was actually shown.

        Two ways to fail, and they are separated rather than lumped together,
        because they have different causes and different fixes:

        * not retrieved at all -> ``HALLUCINATED_CITATION``: the model invented
          or recalled an id. A grounding failure, fixed in the prompt.
        * retrieved but outside the rendered scope -> ``CITATION_NOT_IN_PROMPT``:
          the model cited a passage that exists but was cut from its context by
          the budget. A context failure, fixed by raising ``max_passages``.

        The order of the two branches matters. Testing "not in scope" first
        would label an invented id as a budget problem, and because ``_dedupe``
        keys on ``(code, severity, subject)`` it would also emit both codes for
        the same id. Retrieved-ness is the primary question; scope is secondary.
        """
        valid: list[str] = []
        for citation in result.citations:
            if citation not in retrieved:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.HALLUCINATED_CITATION,
                        severity=Severity.ERROR,
                        message=(
                            f"citation {citation!r} is not a retrieved passage; "
                            f"the retriever returned {len(retrieved)} passage(s)"
                        ),
                        subject=citation,
                    )
                )
            elif scope is not None and citation not in scope:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.CITATION_NOT_IN_PROMPT,
                        severity=Severity.ERROR,
                        message=(
                            f"citation {citation!r} was retrieved but not rendered "
                            f"into the prompt ({len(scope.passage_ids)} of "
                            f"{len(retrieved)} passage(s) were); the model cannot "
                            "have read it"
                        ),
                        subject=citation,
                    )
                )
            else:
                valid.append(citation)
        return valid

    def _check_provenance_reference(
        self,
        result: GenerationResult,
        retrieved: dict[str, RetrievedPassage],
        scope: Optional[PromptScope],
        violations: list[ValidationViolation],
    ) -> None:
        """Provenance must point at passages the model was shown, and cohere.

        Uses the same two-branch classification as the citation check; a claim
        attributed to an unshown passage is the same defect as citing one.
        """
        attributed: set[str] = set()

        for entry in result.provenance:
            for passage_id in entry.passage_ids:
                attributed.add(passage_id)
                if passage_id not in retrieved:
                    violations.append(
                        ValidationViolation(
                            code=ViolationCode.HALLUCINATED_CITATION,
                            severity=Severity.ERROR,
                            message=(
                                f"provenance for claim {entry.claim[:80]!r} cites "
                                f"{passage_id!r}, which was not retrieved"
                            ),
                            subject=passage_id,
                        )
                    )
                elif scope is not None and passage_id not in scope:
                    violations.append(
                        ValidationViolation(
                            code=ViolationCode.CITATION_NOT_IN_PROMPT,
                            severity=Severity.ERROR,
                            message=(
                                f"provenance for claim {entry.claim[:80]!r} cites "
                                f"{passage_id!r}, which was retrieved but not "
                                "rendered into the prompt"
                            ),
                            subject=passage_id,
                        )
                    )
            if entry.passage_ids == [] and entry.support.value != "unsupported":
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.CLAIM_WITHOUT_EVIDENCE,
                        severity=Severity.WARNING,
                        message=(
                            f"claim is marked {entry.support.value!r} but names no "
                            f"passage: {entry.claim[:80]!r}"
                        ),
                        subject=entry.claim[:120],
                    )
                )

        if result.evidence_status is not EvidenceStatus.SUFFICIENT or not result.provenance:
            return

        cited = set(result.citations)
        # A SUFFICIENT answer whose provenance names an uncited passage means the
        # model grounded a claim and then forgot to cite it.
        uncited = attributed - cited
        if uncited:
            violations.append(
                ValidationViolation(
                    code=ViolationCode.CITATION_PROVENANCE_MISMATCH,
                    severity=Severity.WARNING,
                    message=(
                        "provenance names passage(s) absent from citations: "
                        + ", ".join(sorted(uncited))
                    ),
                    subject=",".join(sorted(uncited)),
                )
            )
        # The reverse: a citation no claim was attributed to.
        unclaimed = cited - attributed
        if unclaimed:
            violations.append(
                ValidationViolation(
                    code=ViolationCode.CITATION_PROVENANCE_MISMATCH,
                    severity=Severity.WARNING,
                    message=(
                        "citation(s) not referenced by any provenance claim: "
                        + ", ".join(sorted(unclaimed))
                    ),
                    subject=",".join(sorted(unclaimed)),
                )
            )

    # -- R4 ---------------------------------------------------------------- #

    def _check_evidence_status(
        self,
        result: GenerationResult,
        request: GenerationRequest,
        valid_citations: list[str],
        violations: list[ValidationViolation],
    ) -> None:
        """A SUFFICIENT answer needs evidence; an INSUFFICIENT one must not cite."""
        if result.evidence_status is EvidenceStatus.SUFFICIENT:
            if valid_citations:
                return
            if not request.passages:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.MISSING_REFUSAL,
                        severity=Severity.ERROR,
                        message=(
                            "no passages were retrieved, so no answer can be "
                            "supported; expected a refusal with "
                            "evidence_status=INSUFFICIENT"
                        ),
                    )
                )
            else:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.SUFFICIENT_WITHOUT_CITATION,
                        severity=Severity.ERROR,
                        message=(
                            "evidence_status=SUFFICIENT but no citation points at a "
                            "retrieved passage"
                        ),
                    )
                )
            return

        # Refusal path: citing passages while claiming insufficient evidence is
        # contradictory, but harmless enough to record rather than reject.
        if result.citations:
            violations.append(
                ValidationViolation(
                    code=ViolationCode.REFUSAL_WITH_CITATIONS,
                    severity=Severity.WARNING,
                    message=(
                        "refusal carries citations "
                        f"({', '.join(result.citations)}); they will be dropped"
                    ),
                    subject=",".join(result.citations),
                )
            )

    # -- R4, second half --------------------------------------------------- #

    def _check_question_coverage(
        self,
        result: GenerationResult,
        request: GenerationRequest,
        scope: Optional[PromptScope],
        valid_citations: list[str],
        violations: list[ValidationViolation],
    ) -> None:
        """Report question clauses the cited evidence does not cover.

        This is the ``b07`` gap, closed. That sample asks two things - the F1
        score and the inference latency - and the retrieved passages answer only
        the first. Every backend returned ``SUFFICIENT`` and no rule fired, so a
        consumer reading that status would reasonably believe both parts were
        answered. Nothing in R1-R4 asked "did the answer address the question",
        which is why it survived a whole week of testing.

        Kept as a ``WARNING`` rather than an ``ERROR``, and the choice is the
        same one R2 already makes: deciding whether a clause is *covered* is a
        token-overlap heuristic, and a heuristic must not be allowed to discard
        an otherwise grounded answer. The status the consumer actually reads is
        ``evidence_status``; this check exists so the shortfall is visible in
        ``citations``-adjacent audit data rather than only in the prose.

        Fires only for genuinely multi-part questions, and only when at least
        one clause is uncovered. A single-clause question is never reported: low
        recall there means the passage is marginally relevant, which the refusal
        machinery already handles and which is not the same defect.
        """
        if result.is_refusal or scope is None:
            return

        clauses = question_clauses(request.question)
        if len(clauses) < 2:
            return

        cited_text = " ".join(
            scope.text_by_id[cid]
            for cid in valid_citations
            if cid in scope.text_by_id
        )
        if not cited_text:
            return

        for clause in clauses:
            recall = token_overlap_recall(clause, cited_text)
            if recall < self.config.question_clause_threshold:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.UNCOVERED_QUESTION_CLAUSE,
                        severity=Severity.WARNING,
                        message=(
                            f"the question asks {len(clauses)} things and the cited "
                            f"evidence covers this one at recall {recall:.2f} < "
                            f"{self.config.question_clause_threshold}: {clause[:120]!r}"
                        ),
                        subject=clause[:120],
                    )
                )

    def _check_required_components(
        self,
        result: GenerationResult,
        request: GenerationRequest,
        scope: Optional[PromptScope],
        valid_citations: list[str],
        violations: list[ValidationViolation],
    ) -> None:
        """Structural counterpart to the clause heuristic, using P4's map.

        P4 maps each planner component (``result``, ``method``, ...) to the
        passage ids the agent believes support it. When the critic says the
        evidence is sufficient, every component should have at least one mapped
        passage and the answer should cite one of them.

        Kept at ``WARNING``: P4's mapper is currently a keyword mock, so a miss
        is a signal about the map, not proof that the answer is unsupported -
        the same reason ``UNCOVERED_QUESTION_CLAUSE`` does not downgrade.
        """
        if (
            result.is_refusal
            or not request.required_components
            or not request.evidence_map
        ):
            return

        cited = set(valid_citations)
        rendered = set(scope.passage_ids) if scope is not None else None
        for component in request.required_components:
            mapped = set(request.evidence_map.get(component, []))
            if not mapped:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.UNCOVERED_REQUIRED_COMPONENT,
                        severity=Severity.WARNING,
                        message=(
                            f"the agent required component {component!r} but its "
                            "evidence map contains no passage for it"
                        ),
                        subject=component,
                    )
                )
                continue

            visible = mapped & rendered if rendered is not None else mapped
            if not visible:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.UNCOVERED_REQUIRED_COMPONENT,
                        severity=Severity.WARNING,
                        message=(
                            f"component {component!r} maps to {len(mapped)} "
                            "passage(s), but none was rendered into the prompt"
                        ),
                        subject=component,
                    )
                )
            elif not (cited & visible):
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.UNCOVERED_REQUIRED_COMPONENT,
                        severity=Severity.WARNING,
                        message=(
                            f"component {component!r} maps to {sorted(visible)}, "
                            "but the answer cites none of them"
                        ),
                        subject=component,
                    )
                )

    # -- R3 ---------------------------------------------------------------- #

    @staticmethod
    def _text_of(
        passage_id: str,
        retrieved: dict[str, RetrievedPassage],
        scope: Optional[PromptScope],
    ) -> str:
        """The characters of a passage the model could actually have read.

        With a scope, that is the truncated, budgeted text the prompt rendered -
        not ``RetrievedPassage.text``. They differ whenever a passage is longer
        than ``max_chars_per_passage``, and comparing against the full text
        credits the model with numbers that sat past the cut.
        """
        if scope is not None and passage_id in scope.text_by_id:
            return scope.text_by_id[passage_id]
        passage = retrieved.get(passage_id)
        return passage.text if passage is not None else ""

    def _check_numeric_grounding(
        self,
        result: GenerationResult,
        request: GenerationRequest,
        valid_citations: list[str],
        retrieved: dict[str, RetrievedPassage],
        scope: Optional[PromptScope],
        violations: list[ValidationViolation],
    ) -> None:
        """Every number in the answer must occur in a *cited* passage.

        The diagnostic distinguishes "invented" from "present in the context but
        not cited", because the two failures need different prompt fixes.
        """
        if result.is_refusal:
            return

        # What the model saw, when that is known. Without a scope this is every
        # retrieved passage, which is the permissive reading the truncation
        # defect came from.
        visible_ids = scope.passage_ids if scope is not None else list(retrieved)
        cited_ids = [cid for cid in valid_citations if cid in retrieved]
        cited_numbers = number_index(
            " ".join(self._text_of(cid, retrieved, scope) for cid in cited_ids)
        )
        all_numbers = number_index(
            " ".join(self._text_of(pid, retrieved, scope) for pid in visible_ids)
        )
        question_numbers = (
            number_index(request.question) if self.config.allow_numbers_from_question else set()
        )

        for number in extract_numbers(result.answer):
            if number in cited_numbers or number in question_numbers:
                continue

            if number in all_numbers:
                holders = sorted(
                    pid
                    for pid in visible_ids
                    if number in number_index(self._text_of(pid, retrieved, scope))
                )

                if self.config.repair_numeric_citations:
                    # The number is in evidence the model actually read; the
                    # omission is in the citation list. Add the holder(s) and
                    # keep the answer. The final citation set still satisfies
                    # "every number is in a cited passage", and the raw result
                    # (snapshotted before this check) still shows what the model
                    # itself cited.
                    added = []
                    for holder in holders:
                        if holder not in cited_ids:
                            cited_ids.append(holder)
                            valid_citations.append(holder)
                            result.citations.append(holder)
                            added.append(holder)
                    cited_numbers |= number_index(
                        " ".join(self._text_of(pid, retrieved, scope) for pid in holders)
                    )
                    violations.append(
                        ValidationViolation(
                            code=ViolationCode.CITATION_REPAIRED_FOR_NUMBER,
                            severity=Severity.WARNING,
                            message=(
                                f"number {number} appears in rendered passage(s) "
                                f"{', '.join(holders)} but was not cited; the "
                                "passage(s) were added to citations "
                                f"({', '.join(added) or 'already present'})"
                            ),
                            subject=number,
                        )
                    )
                    continue

                message = (
                    f"number {number} appears in retrieved passage(s) "
                    f"{', '.join(holders)} but in none of the cited passages "
                    f"({', '.join(cited_ids) or 'none'})"
                )
            else:
                # "the context the model was shown", not "any retrieved passage":
                # the comparison is against the *rendered* context, so a number
                # sitting past max_chars_per_passage, or in a passage the budget
                # cut, is one the model could not have read. The old wording
                # asserted something factually untrue about that case.
                message = (
                    f"number {number} does not occur in the context the model was "
                    "shown; unsupported numerical claims are prohibited"
                )

            violations.append(
                ValidationViolation(
                    code=ViolationCode.UNSUPPORTED_NUMERIC_CLAIM,
                    severity=Severity.ERROR,
                    message=message,
                    subject=number,
                )
            )

    # -- R2 ---------------------------------------------------------------- #

    def _check_claim_coverage(
        self,
        result: GenerationResult,
        retrieved: dict[str, RetrievedPassage],
        valid_citations: list[str],
        scope: Optional[PromptScope],
        violations: list[ValidationViolation],
    ) -> None:
        """Flag answer sentences that no provenance claim or cited passage covers.

        The branch on ``result.provenance`` is why derived provenance must be
        injected *after* validation rather than before it: with provenance
        present this compares sentences against the model's own claims, and a
        derived claim *is* the sentence, so the recall would be 1.0 by
        construction and the check would never fire again.
        """
        if result.is_refusal:
            return

        if result.provenance:
            haystacks = [entry.claim for entry in result.provenance]
            source = "provenance claims"
        else:
            haystacks = [
                self._text_of(cid, retrieved, scope)
                for cid in valid_citations
                if cid in retrieved
            ]
            source = "cited passage text"

        if not haystacks:
            # No provenance and no valid citations: nothing to check against, and
            # R1/R4 have already flagged the real problem.
            return

        if not result.provenance:
            violations.append(
                ValidationViolation(
                    code=ViolationCode.CLAIM_WITHOUT_EVIDENCE,
                    severity=Severity.WARNING,
                    message=(
                        "no provenance was returned, so per-claim evidence could "
                        "not be verified; coverage was checked against cited "
                        "passage text instead"
                    ),
                )
            )

        for sentence in split_sentences(result.answer):
            if len(content_tokens(sentence)) < self.config.min_claim_tokens:
                continue
            best = max(token_overlap_recall(sentence, hay) for hay in haystacks)
            if best < self.config.claim_coverage_threshold:
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.UNSUPPORTED_CLAIM,
                        severity=Severity.WARNING,
                        message=(
                            f"no supporting evidence found in {source} "
                            f"(best token recall {best:.2f} < "
                            f"{self.config.claim_coverage_threshold}): {sentence[:160]!r}"
                        ),
                        subject=sentence[:120],
                    )
                )

    def _check_provenance_support(
        self,
        result: GenerationResult,
        retrieved: dict[str, RetrievedPassage],
        scope: Optional[PromptScope],
        violations: list[ValidationViolation],
    ) -> None:
        """Flag provenance whose asserted support the text does not bear out.

        ``provenance[].support`` is a self-report, and the one thing a
        self-report cannot do is check itself. Recomputing the label from the
        text it points at is the whole reason :mod:`src.generation.provenance` exists.

        Two details that are easy to get wrong, both found in review:

        * The comparison uses the **visible** text - the truncated, header-bearing
          block the model actually read - not ``RetrievedPassage.text``, so this
          check agrees with R2 and R3 instead of being quietly the most lenient
          of the three.
        * Each entry is scored against the passages **it names**, not against
          ``citations``. An entry correctly attributing a claim to a passage it
          forgot to cite already earns ``CITATION_PROVENANCE_MISMATCH``; scoring
          it against a different set would add a second, spurious warning.

        Entries naming no passage are skipped: those already produce
        ``CLAIM_WITHOUT_EVIDENCE``, and reporting one defect twice under two
        codes makes the aggregate counts harder to read, not more informative.
        """
        if result.is_refusal or not result.provenance:
            return

        visible_ids = scope.passage_ids if scope is not None else list(retrieved)
        visible = {
            pid: RetrievedPassage(
                passage_id=pid, text=self._text_of(pid, retrieved, scope)
            )
            for pid in visible_ids
        }

        for entry in result.provenance:
            named = [visible[pid] for pid in entry.passage_ids if pid in visible]
            if not named:
                # Already covered by the R1b reference check or by
                # CLAIM_WITHOUT_EVIDENCE; nothing to score against here.
                continue
            for _, derived in overstated_claims([entry], named):
                violations.append(
                    ValidationViolation(
                        code=ViolationCode.PROVENANCE_OVERSTATED,
                        severity=Severity.WARNING,
                        message=(
                            f"claim is marked {entry.support.value!r} but the text it "
                            f"names supports {derived.value!r}: {entry.claim[:120]!r}"
                        ),
                        subject=entry.claim[:120],
                    )
                )

    # -- outcome ----------------------------------------------------------- #

    def _finalize(
        self, result: GenerationResult, violations: list[ValidationViolation]
    ) -> tuple[GenerationResult, bool, str | None]:
        """Apply the downgrade policy and return the result P6 will see."""
        if self.config.downgrade_on_error and any(
            v.severity is Severity.ERROR for v in violations
        ):
            return refusal_result(result.retrieval_rounds), True, "error_violation"

        if self.config.normalize_refusal and result.is_refusal:
            normalized = refusal_result(result.retrieval_rounds)
            if normalized != result:
                return normalized, True, "refusal_normalised"
            return result, False, None

        return result, False, None
