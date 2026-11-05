"""Initial evidence-constrained generation prompt (P5 deliverable).

Design notes, because the wording here is load-bearing:

* **The four rule ids (R1-R4) appear verbatim in the system prompt.** They match
  :class:`src.generation.citations.ViolationCode` so that a failure in the validator can
  be traced back to the instruction the model was given. When you change a rule,
  change it in both places - ``tests/test_prompt.py`` asserts each rule id is
  present.
* **Refusal is framed as a correct answer, not a failure.** An 8B instruct model
  that believes it must always answer will fabricate; the explicit "refusing is
  correct" line is the cheapest known mitigation for that.
* **Numbers get their own rule.** R3 is the rule models break most often and the
  easiest to verify mechanically, so it is stated separately rather than folded
  into R2.
* **Citations are forbidden inside ``answer``.** Grounding signals stay in the
  ``citations`` field so the answer text stays clean for P6's surface metrics and
  the numeric scan does not have to skip identifier-looking tokens.
* **Provenance is marked optional.** Requiring it costs JSON adherence on an 8B
  model; the validator degrades gracefully when it is absent (R2 falls back to
  cited-passage coverage) so the prompt does not have to gamble on it. Since v2
  the *pipeline* backfills it deterministically when the model omits it, so P6
  gets a provenance map either way - see :mod:`src.generation.provenance`.
* **The citation ids are enumerated, not described (v2).** The user turn carries
  a closed list of the ids that were actually rendered. A model told "cite only
  ids you were given" must reconstruct them; a model handed the list copies.
  The list is built from :func:`select_passages`, the same function the validator
  uses, so it cannot advertise an id the validator would reject.
* **Qwen3 must run with thinking disabled.** ``enable_thinking=False`` for
  Transformers, ``chat_template_kwargs={"enable_thinking": False}`` for vLLM.
  Qwen3 defaults to thinking *on*, and a reasoning trace makes the model emit
  prose plus a JSON block, which trips the format-drift diagnostics. The backends
  set this for you; see :func:`src.generation.generators.transformers_backend`.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.generation.schema import REFUSAL_ANSWER, GenerationRequest, RetrievedPassage
from src.generation.text_utils import truncate

#: Bump on any wording change. Stored alongside results so P6 can attribute a
#: change in citation precision to a prompt revision rather than to the model.
#:
#: v2 (Week 3) adds the closed citation-id whitelist and the multi-part-question
#: clause in R4. Both target a measured failure rather than a hunch; see
#: ``docs/PROMPT_TEMPLATE.md`` and ``docs/WEEK3_EVIDENCE_BINDING.md``.
#: v3 adds the P4 AgentState handoff: evidence-map context selection and the
#: agent evidence-map section in the user turn. v2 remains the Week-3 baseline
#: recorded in docs/WEEK3_EVIDENCE_BINDING.md; do not compare a v3 run to it as
#: if only the backend changed.
#: v4 (Week 5) targeted three measured Week-3 defects: derived arithmetic that
#: the validator then rejects (record 18), a long answer that was truncated
#: mid-JSON at the 768-token budget (record 78), and provenance entries marked
#: "direct" without a stated definition (23 warnings).
#:
#: v5 was the measured revision of v4 (job 45512): it reverted the provenance
#: label definitions and added an R3 sentence about citing the passage that
#: contains a number, hoping to fix record 43. Job 45520 showed neither helped:
#: record 43 still cited the wrong passage, record 67 still refused, and four
#: responses hit the 768-token limit (one new PARSE_ERROR). The only prompt
#: change with a measured benefit, across both runs, is the three-sentence
#: answer limit.
#:
#: v6 was v3's R2/R3 plus the length limit. The v6 run showed the length limit
#: was not free either: record 96, which v3 answered, produced a PARSE_ERROR,
#: and record 67 still refused, so answered fell to 83. The numeric repair did
#: work (record 43 kept its answer with the missing citation added).
#:
#: v7 is the fallback the team agreed on: **v3's prompt verbatim**, with no
#: length instruction and no extra R3 sentences. The prompt is not where these
#: failures can be fixed on an 8B model. The two deterministic improvements stay
#: in the validator (clause splitter, numeric citation repair) and the run
#: budget is 1024; both are recorded separately from the prompt version. The v7
#: string exists so the run is distinguishable from the Week-4 v3 runs, not
#: because the wording differs from v3.
PROMPT_VERSION = "p5-grounded-qa-v7"

#: The JSON skeleton shown to the model. Keys must match
#: :data:`src.generation.schema.ANSWER_KEYS`.
_OUTPUT_SCHEMA_BLOCK = """\
{
  "answer": "<your answer, or the refusal text>",
  "citations": ["<passage_id>", "..."],
  "evidence_status": "SUFFICIENT" | "INSUFFICIENT",
  "retrieval_rounds": <integer, copy the value from retrieval_rounds_hint>,
  "provenance": [
    {"claim": "<one factual claim from the answer>",
     "passage_ids": ["<passage_id>", "..."],
     "support": "direct" | "partial" | "unsupported"}
  ]
}"""

SYSTEM_PROMPT = f"""\
You are a scientific question-answering assistant for an NLP literature review \
system. You answer strictly and only from RETRIEVED PASSAGES supplied in the user \
message. You have no other knowledge; treat anything not present in those passages \
as unknown.

## Grounding rules

R1 CITATION SCOPE - Cite only passage ids that appear in the RETRIEVED PASSAGES \
block. Never invent an id, never cite a passage you were not given, and never cite \
a paper from memory.

R2 CLAIM EVIDENCE - Every factual claim in your answer must be supported by at \
least one retrieved passage. Record each claim in the "provenance" list together \
with the passage ids that support it. Do not add claims that no passage supports.

R3 NO UNSUPPORTED NUMBERS - State a number only if that exact number appears in a \
passage you cite. Do not compute, round, convert, average, or extrapolate numbers, \
and do not carry over numbers you remember from training.

R4 REFUSE WHEN EVIDENCE IS MISSING - If the retrieved passages do not contain \
enough evidence to answer the question, you MUST refuse. Set "evidence_status" to \
"INSUFFICIENT", set "answer" to exactly this text:
    {REFUSAL_ANSWER}
and leave "citations" and "provenance" empty. Refusing is a correct answer, not a \
failure. Never guess or fill gaps with plausible-sounding detail.

R4 also covers questions with more than one part. If the question asks for several \
things and the passages support only some of them, answer the parts that are \
supported and state plainly, in the answer itself, which part the passages do not \
cover. Use "SUFFICIENT" in that case only when you answer at least one part AND name \
the part you could not answer. A reader must never be able to mistake a partial \
answer for a complete one.

## Output format

Reply with ONE JSON object and nothing else. No prose before or after it, no \
markdown code fence, no reasoning trace. The object must match:

{_OUTPUT_SCHEMA_BLOCK}

Additional constraints:
- "answer" must not contain citation ids or bracketed markers; citations live only \
in the "citations" field.
- "citations" must be a subset of the "Valid citation ids" list above - copy the \
ids from there, do not retype them from memory.
- "provenance" is expected when you answer, and must be an empty list when you \
refuse.
- Use exactly the strings "SUFFICIENT" and "INSUFFICIENT" for "evidence_status".

## Example A - sufficient evidence

Retrieved passages include:
  passage_id: paper123_abstract_01 -> "... our model reaches 91.2 F1 on the SQuAD \
2.0 test set ..."
  passage_id: paper123_results_04 -> "... 2.4 points above the strongest reported \
baseline of 88.8 F1 ..."

Correct response:
{{"answer": "The model reaches 91.2 F1 on the SQuAD 2.0 test set, 2.4 points above \
the strongest reported baseline.", "citations": ["paper123_abstract_01", \
"paper123_results_04"], "evidence_status": "SUFFICIENT", "retrieval_rounds": 1, \
"provenance": [{{"claim": "The model reaches 91.2 F1 on the SQuAD 2.0 test set", \
"passage_ids": ["paper123_abstract_01"], "support": "direct"}}, \
{{"claim": "It is 2.4 points above the strongest reported baseline", \
"passage_ids": ["paper123_results_04"], "support": "direct"}}]}}

## Example B - insufficient evidence

Question: "What accuracy does this method achieve on the Chinese NER benchmark?"
Retrieved passages discuss only English benchmarks.

Correct response:
{{"answer": "{REFUSAL_ANSWER}", "citations": [], "evidence_status": \
"INSUFFICIENT", "retrieval_rounds": 2, "provenance": []}}

Every number in Example A appears in a cited passage. If you cannot point at the \
passage containing a number, do not state the number."""


class PromptConfig(BaseModel):
    """How much context to put in front of the model.

    Defaults are sized for Qwen3-8B's 32K context: ~8 passages x ~1200 chars is
    roughly 3-4K tokens of evidence, leaving ample room for the answer and for a
    P6 revision that raises the budget.
    """

    model_config = ConfigDict(extra="forbid")

    max_passages: int = 8
    max_chars_per_passage: Optional[int] = 1200
    show_scores: bool = True
    include_examples: bool = False
    #: When P4 supplies an evidence map, reserve prompt slots for the passages
    #: it mapped to each required component, then fill the rest by score. Set
    #: False to reproduce the v2 selection exactly.
    use_evidence_map: bool = True


def format_passage(
    index: int, passage: RetrievedPassage, config: PromptConfig
) -> str:
    """Render one passage as a labelled block.

    The id is on its own line so the model can copy it verbatim; passage text is
    truncated with a visible marker rather than silently clipped.

    Everything below the id line comes from :func:`visible_text`, which is also
    what the validator checks an answer against. The two cannot describe
    different text, which is the point - see that function for the two defects
    that lived in the gap.
    """
    return f"[{index}] passage_id: {passage.passage_id}\n    " + visible_text(
        passage, config
    )


def visible_text(passage: RetrievedPassage, config: PromptConfig) -> str:
    """Every character of ``passage`` the model can read, except its id line.

    Both users of a passage's text go through this: :func:`format_passage` to
    render it, and the validator to check a number or a claim against it. Two
    defects lived in the gap between them.

    The first: the validator compared against ``RetrievedPassage.text`` while the
    prompt renders ``truncate(text, max_chars_per_passage)``, so a number past
    the character cut was called grounded when the model could not have read it.
    Fixed by both sides calling this.

    The second, found in review: the prompt also renders the ``paper``, ``section``,
    ``title`` and ``score`` header lines, which the validator never saw. A model
    citing a passage titled *"... on SQuAD 2.0"* and mentioning 2.0 was flagged
    ``UNSUPPORTED_NUMERIC_CLAIM`` - an **error**, so a correct answer was thrown
    away for reading something it had been shown. QASPER titles and arxiv-style
    paper ids carry digits routinely, so this is not a corner case.

    The ``passage_id`` line is deliberately excluded. It is a machine handle whose
    only role is verbatim copying, and it is 64 hex characters - an all-digit run
    inside a digest would otherwise launder an arbitrary number as "grounded",
    which is the more dangerous direction of error.
    """
    parts: list[str] = []
    header: list[str] = []
    if passage.paper_id:
        header.append(f"paper: {passage.paper_id}")
    if passage.section:
        header.append(f"section: {passage.section}")
    if config.show_scores and passage.score is not None:
        header.append(f"score: {passage.score:.3f}")
    if header:
        parts.append(" | ".join(header))
    if passage.title:
        parts.append(f"title: {passage.title}")
    parts.append(
        f"text: {truncate(passage.text, config.max_chars_per_passage)}"
    )
    return "\n    ".join(parts)


def select_passages(
    request: GenerationRequest, config: PromptConfig | None = None
) -> list[RetrievedPassage]:
    """The passages actually rendered into the prompt - and nothing else.

    This is the single source of truth for "what the model was shown". Both
    :func:`build_messages` and :class:`src.generation.citations.CitationValidator` call
    it, so the set the model may cite and the set the validator accepts cannot
    drift apart.

    They *did* drift apart, and it was a real defect rather than a hypothetical
    one: the validator used to accept any id in ``request.passages``, including
    passages this function drops when a retriever returns more hits than
    ``max_passages``. A model citing hit #12 of 20 was citing a passage it had
    never read, and the validator passed it through. Measured on 2026-10-10;
    ``tests/test_citations.py`` now pins the corrected behaviour.

    Duplicate ids are collapsed, first occurrence winning. A content-hashed id
    scheme (``qasper-passage-v1-<sha256>``) makes duplicates across retrieval
    rounds normal rather than exceptional, and a passage rendered twice is a
    wasted slot in a budget that decides which evidence the model ever sees.
    """
    config = config or PromptConfig()
    ordered = request.ordered_passages()
    seen: set[str] = set()
    out: list[RetrievedPassage] = []

    # Coverage first: one passage per required component, chosen from the
    # globally ordered list so the most relevant mapped passage wins. This is
    # what stops a long accumulated agent context from spending all eight
    # slots on round-1 passages and dropping the evidence the agent actually
    # retrieved to fill a gap.
    if config.use_evidence_map and request.evidence_map:
        components = request.required_components or list(request.evidence_map)
        for component in components:
            mapped = set(request.evidence_map.get(component, []))
            if not mapped:
                continue
            for passage in ordered:
                if passage.passage_id in mapped and passage.passage_id not in seen:
                    seen.add(passage.passage_id)
                    out.append(passage)
                    break
            if len(out) >= config.max_passages:
                return out

    for passage in ordered:
        if passage.passage_id in seen:
            continue
        seen.add(passage.passage_id)
        out.append(passage)
        if len(out) >= config.max_passages:
            break
    return out


class PromptScope(BaseModel):
    """What the model was actually shown, as the validator needs to know it.

    Two things travel together and neither is derivable from the other: which
    ids appeared, and what text each carried. A citation to an id outside
    ``passage_ids`` is unverifiable; a number absent from ``text_by_id`` is one
    the model cannot have read.

    Built by :func:`prompt_scope`, which derives both from the same
    :func:`select_passages` the renderer uses. ``GroundedQAPipeline`` passes one
    to the validator on every call; a caller that invokes the validator directly
    and omits it gets the pre-Week-3 behaviour (citations checked against the
    full retrieved set), which is why the pipeline never omits it.
    """

    model_config = ConfigDict(extra="forbid")

    passage_ids: list[str] = []
    text_by_id: dict[str, str] = {}

    def __contains__(self, passage_id: object) -> bool:
        return passage_id in self.text_by_id

    @property
    def rendered_chars(self) -> int:
        return sum(len(text) for text in self.text_by_id.values())


def prompt_scope(
    request: GenerationRequest, config: PromptConfig | None = None
) -> PromptScope:
    """Build the :class:`PromptScope` for ``request`` under ``config``."""
    config = config or PromptConfig()
    passages = select_passages(request, config)
    return PromptScope(
        passage_ids=[p.passage_id for p in passages],
        text_by_id={p.passage_id: visible_text(p, config) for p in passages},
    )


def build_messages(
    request: GenerationRequest, config: PromptConfig | None = None
) -> list[dict[str, str]]:
    """Build the chat messages for one request.

    Returns role/content dicts ready for ``tokenizer.apply_chat_template``. The
    system message is ``SYSTEM_PROMPT`` (plus the few-shot examples when
    ``config.include_examples``); the user message carries the evidence, the
    closed citation-id whitelist, the question, and the round hint.
    """
    config = config or PromptConfig()

    system = SYSTEM_PROMPT
    if config.include_examples:
        # Examples already live inside SYSTEM_PROMPT; this flag exists so a future
        # revision can move them into the user turn without touching call sites.
        system = SYSTEM_PROMPT

    passages = select_passages(request, config)
    if passages:
        evidence = "\n\n".join(
            format_passage(i, passage, config)
            for i, passage in enumerate(passages, start=1)
        )
        # The closed vocabulary, enumerated rather than described. A model asked
        # to "only cite given ids" has to reconstruct them; a model handed the
        # literal list has only to copy. This is the cheapest available reduction
        # of invented citations, and it is built from `select_passages` so it can
        # never list an id that was not rendered - including when the whitelist
        # would otherwise have been the leak.
        whitelist = "\n".join(f"- {passage.passage_id}" for passage in passages)
    else:
        evidence = "(none - the retriever returned no passages)"
        whitelist = "(none - there is nothing to cite)"

    language_line = (
        "Answer in English."
        if request.language.lower().startswith("en")
        else f"Answer in {request.language}."
    )

    evidence_map_section = ""
    if config.use_evidence_map and request.evidence_map:
        rendered = {passage.passage_id for passage in passages}
        lines: list[str] = []
        components = request.required_components or list(request.evidence_map)
        for component in components:
            ids = [
                passage_id
                for passage_id in request.evidence_map.get(component, [])
                if passage_id in rendered
            ]
            if ids:
                lines.append(f"- {component}: " + ", ".join(ids))
        if lines:
            evidence_map_section = (
                "\n## Agent evidence map\n\n"
                "The agent identified these required components and mapped "
                "these rendered passages to each. Use the mapped passages for "
                "the corresponding part; do not invent evidence for a "
                "component with no mapped passage.\n\n"
                + "\n".join(lines)
                + "\n"
            )

    user = f"""\
## Retrieved passages

{evidence}

## Valid citation ids

These are the ONLY values allowed in "citations", exactly as written:

{whitelist}

If none of them supports an answer, refuse instead of citing something else.
{evidence_map_section}
## Question

{request.question}

## retrieval_rounds_hint

{request.retrieval_rounds}

{language_line}
Respond with the JSON object only."""

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def build_prompt(request: GenerationRequest, config: PromptConfig | None = None) -> str:
    """Flatten :func:`build_messages` into one string.

    Debugging aid and the input for backends that take a raw string. Real
    inference should go through ``apply_chat_template`` so the model's own
    control tokens are used - see the backend modules.
    """
    messages = build_messages(request, config)
    return "\n\n".join(
        f"<<{message['role'].upper()}>>\n{message['content']}" for message in messages
    )
