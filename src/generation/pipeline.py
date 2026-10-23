"""End-to-end grounded QA: request -> raw text -> parsed result -> validated result.

The pipeline is the only place that knows the *order* of operations, and the order
is what implements the P5 policy:

1. **No evidence, no call.** A request with zero retrieved passages short-circuits
   to a refusal. This is not an optimisation - asking a model to answer with an
   empty context is the single most reliable way to elicit a hallucination, so the
   call is never made. It also means a retrieval bug costs nothing in GPU time.
2. **Generate, then parse.** Backends return raw text; parsing is centralised.
3. **Validate, then downgrade.** Fabrications are replaced by a refusal (see
   :mod:`src.generation.citations`), never raised as exceptions, so one bad sample cannot
   abort a batch that has hours left to run.
4. **Record everything.** :class:`PipelineOutput` carries the raw text, the parse
   diagnostics and the full violation list, so P6 can analyse *why* a sample
   failed without re-running generation.

:func:`run_batch_to_jsonl` adds the one piece of operational care the confirmed
quota demands: results are appended and flushed per item, so a job killed at the
6-hour wall-clock limit keeps everything it had already produced and can resume.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Iterable, Optional, Sequence

from pydantic import BaseModel, ConfigDict, Field

from src.generation.citations import (
    CitationValidator,
    Severity,
    ValidationConfig,
    ValidationReport,
    ValidationViolation,
    ViolationCode,
)
from src.generation.generators.base import (
    BackendNotAvailable,
    GeneratorBackend,
    ParseDiagnostics,
    ResponseParseError,
    parse_response,
)
from src.generation.prompts.grounded_qa import (
    PROMPT_VERSION,
    PromptConfig,
    PromptScope,
    prompt_scope,
    select_passages,
)
from src.generation.provenance import map_claims_to_passages
from src.generation.schema import (
    SCHEMA_VERSION,
    GenerationRequest,
    GenerationResult,
    refusal_result,
)

#: Number of leading characters of the raw response kept in a batch record.
#: Enough to see a truncation or a chatty preamble; not enough to bloat a file
#: with a whole reasoning trace.
RAW_TEXT_EXCERPT_CHARS = 2000


#: P4's gap label for "the passages cannot answer this question at all". It is
#: the only label that makes P5 refuse without calling the model. Every other
#: label (MISSING_METHOD, WEAK_EVIDENCE, ...) describes a gap the model may still
#: answer around, so generation proceeds and the label travels as metadata.
INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"


def _is_insufficient_information(label: Optional[str]) -> bool:
    """Case- and whitespace-tolerant comparison against the one refusal label.

    P4's ``GapLabel`` serialises as an uppercase enum value, but the handoff has
    already been through JSON once by the time P5 sees it. Normalising here means
    a lowercased dump cannot silently turn a refusal into an answer.
    """
    return (label or "").strip().upper() == INSUFFICIENT_INFORMATION


class PipelineConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    prompt: PromptConfig = Field(default_factory=PromptConfig)
    validation: ValidationConfig = Field(default_factory=ValidationConfig)
    prompt_version: str = PROMPT_VERSION
    schema_version: str = SCHEMA_VERSION


class PipelineOutput(BaseModel):
    """One answered question, with everything needed to audit it later."""

    model_config = ConfigDict(extra="forbid")

    #: What P6 must consume.
    result: GenerationResult
    #: The audit trail: violations, whether and why a downgrade happened.
    report: ValidationReport
    #: The generator's raw response, or None when no call was made.
    raw_text: Optional[str] = None
    diagnostics: Optional[ParseDiagnostics] = None
    backend: dict[str, Any] = Field(default_factory=dict)

    @property
    def downgraded(self) -> bool:
        return self.report.downgraded

    @property
    def is_refusal(self) -> bool:
        return self.result.is_refusal

    def to_wire(self, include_raw_text: bool = True) -> dict[str, Any]:
        """JSON-ready record: ``{"result": ..., "validation": ..., "generation": ...}``.

        The ``result`` sub-object is exactly the frozen P6 schema (five keys). The
        other two are context for error analysis and may be ignored by a consumer
        that only wants answers.
        """
        generation: dict[str, Any] = {
            "backend": self.backend,
            "prompt_version": PROMPT_VERSION,
        }
        if self.diagnostics is not None:
            generation["diagnostics"] = self.diagnostics.model_dump(mode="json")
        if include_raw_text and self.raw_text is not None:
            generation["raw_text_excerpt"] = self.raw_text[:RAW_TEXT_EXCERPT_CHARS]
            generation["raw_text_chars"] = len(self.raw_text)

        return {
            "result": self.result.to_wire(),
            "validation": self.report.model_dump(mode="json"),
            "generation": generation,
        }


def failure_report(
    request: GenerationRequest,
    code: ViolationCode,
    message: str,
) -> ValidationReport:
    """Build the report for a sample where generation or parsing failed.

    There is no ``raw_result`` because nothing valid was ever parsed; the
    ``final_result`` is a refusal, matching the policy that P6 only ever sees
    either an answer that passed validation or a refusal.
    """
    return ValidationReport(
        final_result=refusal_result(request.retrieval_rounds),
        raw_result=None,
        violations=[ValidationViolation(code=code, severity=Severity.ERROR, message=message)],
        downgraded=True,
        downgrade_reason=code.value,
        checks_run=["<none: no valid response to check>"],
    )


def diagnostics_violations(diagnostics: ParseDiagnostics) -> list[ValidationViolation]:
    """Turn parse observations into WARNING-level violations.

    These never change the answer. They exist so that prompt drift is visible in
    aggregate: a slow rise in ``PROMPT_FORMAT_DRIFT`` across a run is the early
    warning that a model update or a template edit is degrading JSON adherence,
    and it is far cheaper to notice that here than to explain a citation-precision
    drop in the final report.
    """
    violations: list[ValidationViolation] = []

    if diagnostics.extra_fields:
        violations.append(
            ValidationViolation(
                code=ViolationCode.EXTRA_FIELDS_IGNORED,
                severity=Severity.WARNING,
                message=(
                    "response contained fields outside the schema, which were "
                    "ignored: " + ", ".join(diagnostics.extra_fields)
                ),
                subject=",".join(diagnostics.extra_fields),
            )
        )

    drift: list[str] = []
    if diagnostics.had_thinking_block:
        detail = "thinking block present"
        if diagnostics.unclosed_thinking_block:
            detail += " (unclosed - generation was truncated)"
        drift.append(detail + "; enable_thinking is not taking effect")
    if diagnostics.had_code_fence:
        drift.append("JSON wrapped in a markdown fence")
    if diagnostics.leading_text_chars:
        drift.append(f"{diagnostics.leading_text_chars} chars of prose before the JSON")
    if diagnostics.trailing_text_chars:
        drift.append(f"{diagnostics.trailing_text_chars} chars of prose after the JSON")
    if diagnostics.coerced:
        drift.append("coerced fields: " + ", ".join(diagnostics.coerced))
    if diagnostics.candidate_index > 0:
        drift.append(f"JSON found at candidate {diagnostics.candidate_index}")

    if drift:
        violations.append(
            ValidationViolation(
                code=ViolationCode.PROMPT_FORMAT_DRIFT,
                severity=Severity.WARNING,
                message="; ".join(drift),
            )
        )

    return violations


class GroundedQAPipeline:
    """Generate, parse and validate grounded answers.

    Examples
    --------
    >>> from src.generation.generators import MockGenerator, MockScenario
    >>> pipeline = GroundedQAPipeline(MockGenerator(MockScenario.GROUNDED))
    >>> output = pipeline.answer(request)   # doctest: +SKIP
    >>> output.result.to_wire()             # doctest: +SKIP
    """

    def __init__(
        self,
        generator: GeneratorBackend,
        validator: CitationValidator | None = None,
        config: PipelineConfig | None = None,
    ) -> None:
        self.generator = generator
        self.config = config or PipelineConfig()
        self.validator = validator or CitationValidator(self.config.validation)

        # The pipeline owns the prompt budget, and it has to be *the* budget the
        # backend renders with. Backends each carry their own PromptConfig -
        # they default to the same values, so leaving them disagreeing is silent
        # until someone sets `max_passages` on one and not the other. Then the
        # citation-scope check compares the model's citations against a context
        # that was never rendered, and it fails as an ERROR: a correct answer
        # discarded. That is worse than the defect the check exists to close, so
        # the pipeline's config wins, always.
        if getattr(generator, "prompt_config", None) is not None:
            generator.prompt_config = self.config.prompt

    # -- single ------------------------------------------------------------ #

    def answer(self, request: GenerationRequest) -> PipelineOutput:
        """Answer one question.

        Raises
        ------
        BackendNotAvailable
            The backend cannot run here (missing package, no GPU). This is a
            configuration problem, not a data problem, so it is never converted
            into a refusal - it would hide the real cause.
        """
        scope = prompt_scope(request, self.config.prompt)

        # Rule 4, enforced structurally: an empty context gets a refusal without
        # ever reaching the model. Retrying is the retriever's job, not this
        # one's - by the time a request arrives with no passages, the upstream
        # loop has already exhausted its attempts, so this is the terminal
        # state and not a signal to try again.
        if not request.passages:
            report = self.validator.validate(
                refusal_result(request.retrieval_rounds),
                request,
                extra_violations=[
                    ValidationViolation(
                        code=ViolationCode.EMPTY_CONTEXT,
                        severity=Severity.WARNING,
                        message=(
                            "no passages were retrieved, so the model was never "
                            "called; the refusal is the terminal state of the "
                            "retrieval loop, not a judgement about evidence"
                        ),
                    )
                ],
                scope=scope,
            )
            return PipelineOutput(
                result=report.final_result,
                report=report,
                raw_text=None,
                diagnostics=None,
                backend=self.generator.info(),
            )

        # P4's refusal rule, confirmed 2026-10-20. Refuse only when the critic
        # names INSUFFICIENT_INFORMATION: that label means the passages cannot
        # answer the question at all. `sufficient=False` on its own is metadata,
        # not a refusal signal. The static baseline stops at round 1 with
        # `max_retries=0`, so treating insufficient as a refusal would make the
        # baseline measure the critic rather than the answer; both arms must use
        # the same generation call.
        if _is_insufficient_information(request.gap_label):
            report = self.validator.validate(
                refusal_result(request.retrieval_rounds),
                request,
                extra_violations=[
                    ValidationViolation(
                        code=ViolationCode.AGENT_INSUFFICIENT,
                        severity=Severity.WARNING,
                        message=(
                            "the agent's critic labelled the gap "
                            "INSUFFICIENT_INFORMATION, so P5 refused without "
                            "calling the model"
                        ),
                    )
                ],
                scope=scope,
            )
            return PipelineOutput(
                result=report.final_result,
                report=report,
                raw_text=None,
                diagnostics=None,
                backend=self.generator.info(),
            )

        extra_violations: list[ValidationViolation] = []
        if request.agent_sufficient is False:
            # Keep the answer, but make the disagreement visible. P6 can count
            # "answered under critic doubt" without mistaking it for a refusal.
            extra_violations.append(
                ValidationViolation(
                    code=ViolationCode.GENERATED_WITH_INSUFFICIENT_EVIDENCE,
                    severity=Severity.WARNING,
                    message=(
                        "the agent's critic judged the evidence insufficient, "
                        "but the gap was not INSUFFICIENT_INFORMATION, so P5 "
                        "generated from the available passages; the answer is kept"
                    ),
                )
            )

        raw_text = self.generator.generate(request)
        return self._parse_validate(
            raw_text, request, scope, extra_violations=extra_violations
        )

    # -- batch ------------------------------------------------------------- #

    def answer_batch(
        self, requests: Sequence[GenerationRequest], continue_on_error: bool = True
    ) -> list[PipelineOutput]:
        """Answer many questions in order.

        With ``continue_on_error`` (the default) a backend failure on one request
        is recorded as a ``GENERATION_ERROR`` refusal and the batch proceeds.
        Turn it off to surface the first exception - useful when debugging on a
        new cluster, where the failure is systematic and you want the traceback.
        """
        return [self.answer_safe(request, continue_on_error) for request in requests]

    def answer_safe(
        self, request: GenerationRequest, continue_on_error: bool = True
    ) -> PipelineOutput:
        """Like :meth:`answer`, but converts backend errors into refusals."""
        try:
            return self.answer(request)
        except BackendNotAvailable:
            # Configuration failures must surface, not become a refusal that
            # looks like the model's judgement.
            raise
        except Exception as exc:  # noqa: BLE001 - deliberate batch-level catch
            if not continue_on_error:
                raise
            report = failure_report(
                request,
                ViolationCode.GENERATION_ERROR,
                f"{type(exc).__name__}: {exc}",
            )
            return PipelineOutput(
                result=report.final_result,
                report=report,
                raw_text=None,
                diagnostics=None,
                backend=self.generator.info(),
            )

    # -- internals --------------------------------------------------------- #

    def _parse_validate(
        self,
        raw_text: str,
        request: GenerationRequest,
        scope: PromptScope,
        extra_violations: Sequence[ValidationViolation] = (),
    ) -> PipelineOutput:
        try:
            result, diagnostics = parse_response(raw_text)
        except ResponseParseError as exc:
            report = failure_report(
                request,
                ViolationCode.PARSE_ERROR,
                f"{exc.reason} (candidates tried: {exc.candidates_tried})",
            )
            return PipelineOutput(
                result=report.final_result,
                report=report,
                raw_text=raw_text,
                diagnostics=None,
                backend=self.generator.info(),
            )

        report = self.validator.validate(
            result,
            request,
            extra_violations=list(extra_violations)
            + diagnostics_violations(diagnostics),
            scope=scope,
        )
        report = self._derive_provenance(report, request, scope)
        return PipelineOutput(
            result=report.final_result,
            report=report,
            raw_text=raw_text,
            diagnostics=diagnostics,
            backend=self.generator.info(),
        )

    def _derive_provenance(
        self,
        report: ValidationReport,
        request: GenerationRequest,
        scope: PromptScope,
    ) -> ValidationReport:
        """Map claims to cited passages when the model returned no provenance.

        The frozen contract makes ``provenance`` optional, and an 8B model that
        has already spent its JSON budget on the answer often omits it. Making
        the field mandatory in the prompt would trade JSON adherence for a
        feature the pipeline can produce deterministically instead - so it does.

        **Runs after validation, never before**, and both reasons are
        load-bearing:

        1. :meth:`CitationValidator._check_claim_coverage` changes what it
           compares against when ``provenance`` is non-empty. A derived claim is
           the answer sentence itself, so injecting earlier would make R2 score
           every sentence against itself - recall 1.0, check permanently silent.
           A capability regression disguised as a feature.
        2. ``ValidationReport.raw_result`` is the model's own parsed output.
           Enriching before it is snapshotted would make the audit trail assert
           the model said something it never said.

        Only the final object is touched, and only for answers that survived
        validation: a refusal makes no claims and must not appear to.
        """
        final = report.final_result
        if final.is_refusal or final.provenance:
            return report

        cited_ids = set(final.citations)
        cited = [
            passage
            for passage in select_passages(request, self.config.prompt)
            if passage.passage_id in cited_ids
        ]
        derived = map_claims_to_passages(final.answer, cited)
        if not derived:
            return report

        violations = list(report.violations) + [
            ValidationViolation(
                code=ViolationCode.PROVENANCE_DERIVED,
                severity=Severity.WARNING,
                message=(
                    "the model returned no provenance; "
                    f"{len(derived)} claim(s) were mapped to cited passages "
                    "deterministically by src.generation.provenance"
                ),
            )
        ]
        # `cited` is drawn from the cited set, so the filled-in map can only ever
        # name passages the model also cited - which is the invariant that keeps
        # a derived map from tripping CITATION_PROVENANCE_MISMATCH.
        return report.model_copy(
            update={
                "final_result": final.model_copy(update={"provenance": derived}),
                "violations": violations,
            }
        )


def resume_state(path: str | Path) -> tuple[int, int]:
    """Return ``(next_index, corrupt_lines)`` for an existing batch file.

    Resuming is done by **record index, not by line count**. Counting lines gets
    the answer wrong in the exact situation resume exists for: a job killed during
    a write leaves a partial final line, which a line count treats as a finished
    record and thereby *skips a question* on the next run. Reading the ``index``
    the record already carries cannot drift.

    Also repairs the file in place: an unterminated trailing line is truncated, so
    the next append cannot be glued onto a partial record and produce one
    unparseable line out of two good ones. A kill during write is the expected
    cause, so this is not data loss - the dropped bytes were never a record.
    """
    path = Path(path)
    if not path.exists():
        return 0, 0

    raw = path.read_bytes()
    if not raw:
        return 0, 0

    if not raw.endswith(b"\n"):
        cut = raw.rfind(b"\n") + 1  # 0 when the file is a single partial line
        raw = raw[:cut]
        path.write_bytes(raw)

    next_index = 0
    corrupt = 0
    for line in raw.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            corrupt += 1
            continue
        index = record.get("index")
        next_index = max(next_index, index + 1) if isinstance(index, int) else next_index + 1

    return next_index, corrupt


def run_batch_to_jsonl(
    pipeline: GroundedQAPipeline,
    requests: Sequence[GenerationRequest],
    out_path: str | Path,
    *,
    resume: bool = True,
    include_raw_text: bool = True,
    progress_every: int = 1,
    on_record: Optional[Callable[[int, GenerationRequest, "PipelineOutput"], None]] = None,
    echo: Any = print,
) -> Path:
    """Run a batch and append one JSON record per question to ``out_path``.

    Written for the confirmed quota - 1 GPU, 2 concurrent jobs, 6 hours per job:

    * **Append + flush per record.** A job killed at the wall-clock limit keeps
      every completed answer. Nothing is buffered in memory until the end.
    * **Resume by record index.** Re-running with the same ``out_path`` picks up
      after the last indexed record (see :func:`resume_state`), so a killed job
      continues instead of restarting and burning another queue slot.
    * **One record per line.** A truncated final line is repaired on resume.

    ``on_record`` is called with ``(index, request, output)`` immediately after
    each record is flushed. It exists so a caller can take a timestamp or a
    sample of device memory *per sample* without reimplementing the writer above
    - which is what the benchmark in ``scripts/benchmark_qwen3.py`` needs, since
    per-sample latency is the quantity the Week-2 brief asks for. A hook that
    raises is reported and swallowed: it is instrumentation, and instrumentation
    must never be the reason a six-hour batch stops.

    Returns the path written. Keep one file per run configuration: resume trusts
    the indices in the file, so mixing two different request lists in one file
    would silently skip questions.
    """
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    done = 0
    if resume:
        done, corrupt = resume_state(path)
        if corrupt:
            echo(f"[resume] warning: {corrupt} unparseable line(s) in {path}; ignored")
        if done:
            echo(f"[resume] resuming at index {done} of {len(requests)}")

    remaining = list(requests)[done:]
    if not remaining:
        echo(f"[done] nothing to do; {path} already covers all {len(requests)} record(s)")
        return path

    with path.open("a", encoding="utf-8") as handle:
        for offset, request in enumerate(remaining):
            index = done + offset
            output = pipeline.answer_safe(request)
            record = {
                "index": index,
                "request_id": request.request_id,
                "question": request.question,
                **output.to_wire(include_raw_text=include_raw_text),
            }
            # Additive P6 display block: the frozen five keys are untouched.
            agent = request.agent_trace()
            if agent is not None:
                record["agent"] = agent
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            handle.flush()

            if on_record is not None:
                try:
                    on_record(index, request, output)
                except Exception as exc:  # noqa: BLE001 - instrumentation must not stop a batch
                    echo(
                        f"[warn] on_record raised on index {index}: "
                        f"{type(exc).__name__}: {exc}"
                    )

            if progress_every and (offset + 1) % progress_every == 0:
                status = "refusal" if output.is_refusal else "answered"
                flags = ",".join(output.report.codes()) or "-"
                echo(
                    f"[{index + 1}/{len(requests)}] {status} "
                    f"citations={len(output.result.citations)} flags={flags}"
                )

    return path


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Read a batch file back, skipping a truncated trailing line.

    A job killed by the 6-hour limit during a write leaves a partial final line;
    that is expected, so it is dropped silently rather than raising and hiding the
    thousands of good records before it.
    """
    records: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def summarise(outputs: Iterable[PipelineOutput]) -> dict[str, Any]:
    """Aggregate counts for a completed batch.

    Deliberately counts *mechanism* (how often each rule fired, how often a
    downgrade happened) rather than quality. Quality needs P6's gold reference
    sets; this is the operational dashboard you want while a job is running.
    """
    outputs = list(outputs)
    total = len(outputs)
    code_counts: dict[str, int] = {}
    for output in outputs:
        for violation in output.report.violations:
            code_counts[violation.code.value] = code_counts.get(violation.code.value, 0) + 1

    refusals = sum(1 for o in outputs if o.is_refusal)
    downgraded = sum(1 for o in outputs if o.downgraded)
    return {
        "total": total,
        "refusals": refusals,
        "refusal_rate": round(refusals / total, 4) if total else 0.0,
        "downgraded": downgraded,
        "downgrade_rate": round(downgraded / total, 4) if total else 0.0,
        "answered_with_citations": sum(
            1 for o in outputs if not o.is_refusal and o.result.citations
        ),
        "violation_counts": dict(sorted(code_counts.items())),
    }
