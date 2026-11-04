"""Evidence critic (P4, Week 3).

The critic decides whether the passages retrieved so far are enough to answer the
question and, if not, names the gap. It asks an LLM through the `LLMClient`
protocol, then parses and validates the reply deterministically. When there is no
client, nothing was retrieved, or the model's reply is unusable, it falls back to
`rule_based_critic`, which only checks whether every evidence requirement has a
mapped passage.

Measured on QASPER train (scripts/evaluate_planner.py), that rule-based check
accepts lookalike passages more often than the annotated evidence, so it is a
safety net, not a sufficiency judge.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from src.agent.nodes import gap_classifier
from src.agent.schemas import AgentState, CriticOutput, GapLabel

MAX_PASSAGE_CHARS = 3000  # 99.9% of the 365/40-word dev chunks (median 1,272 chars) fit whole
DEFAULT_ATTEMPTS = 2


class LLMClient(Protocol):
    """Anything that turns a prompt into the model's text reply."""

    def complete(self, prompt: str) -> str: ...


@runtime_checkable
class ChatClient(Protocol):
    """A client that takes `[{"role": ..., "content": ...}]` chat messages.

    Preferred when available: the system/user split is how Qwen3 is meant to be
    prompted. A client with both methods is used through `chat`.
    """

    def chat(self, messages: list[dict[str, str]]) -> str: ...


@dataclass(frozen=True)
class ViewedPassage:
    """One passage as the critic reads it: its id and exactly the text shown for it."""

    passage_id: str
    body: str


PassageView = Callable[[AgentState], list[ViewedPassage]]
"""Which passages, and how much of each, the critic is shown for a state."""


def pool_view(state: AgentState) -> list[ViewedPassage]:
    """Every retrieved passage in retrieval order, each cut at MAX_PASSAGE_CHARS."""
    return [
        ViewedPassage(
            hit.passage.passage_id,
            f"section: {hit.passage.section}\n{hit.passage.text[:MAX_PASSAGE_CHARS]}",
        )
        for hit in state.retrieved_passages
    ]


class CriticOutputError(ValueError):
    """The model reply could not be parsed or failed deterministic validation."""


_SYSTEM = """\
You are an evidence critic for a question-answering system over one research paper.
Decide whether the retrieved passages contain enough evidence to answer the question.
Judge only from the passages you are given; do not use outside knowledge.

Reply with one JSON object and nothing else, in exactly this shape:
{{
  "sufficient": true or false,
  "gap_label": one of {labels},
  "supporting_passage_ids": [ids of the passages that state the facts the answer needs, exactly as shown in square brackets; empty if none do],
  "missing_components": [the specific facts that appear in none of the passages, empty if sufficient],
  "reason": "one or two sentences"
}}

What "sufficient" means:
- The passages together state the concrete facts needed to answer the question (a name, a number, a dataset, a baseline, a step of the method, a stated limitation).
- A partial but concrete answer counts. Do not mark the evidence insufficient because a passage is short, is not exhaustive, or words things differently from the question.
- Mark it insufficient only when you can name a specific fact the answer needs that no passage states.

Rules:
- If sufficient is true, gap_label must be "NONE", missing_components must be [] and supporting_passage_ids must list at least one passage.
- If sufficient is false, gap_label must be one of the other labels:
{label_help}
- Write each missing component as a short noun phrase for the missing fact (for example "names of the baseline systems"), never as a remark about the passages such as "not clearly described"."""

_USER = """\
Question: {question}
Question type: {question_type}

Hints about the kind of evidence the answer probably needs (a heuristic from the question wording; judge the question itself):
{requirements}

Retrieved passages:
{passages}

Reply with one JSON object and nothing else."""

_LABEL_HELP = {
    GapLabel.MISSING_METHOD: "the method or approach is not described",
    GapLabel.MISSING_EXPERIMENT_CONTEXT: "dataset, setup or metrics are not described",
    GapLabel.MISSING_RESULT: "no reported result or number",
    GapLabel.MISSING_COMPARISON: "no baseline or comparison is given",
    GapLabel.TERMINOLOGY_MISMATCH: "passages seem related but use different terms",
    GapLabel.WEAK_EVIDENCE: "related passages exist but do not settle the question",
    GapLabel.INSUFFICIENT_INFORMATION: "the paper does not appear to answer this",
}


def build_critic_messages(
    state: AgentState, view: PassageView = pool_view
) -> list[dict[str, str]]:
    """Chat messages for the critic: schema and labels in system, evidence in user.

    `view` decides which passages are shown and how much of each; the default shows
    the whole pool, a runner that answers with P5 passes the generator's own view.
    """
    requirements = "\n".join(
        f"- {r.name}: {r.description}" for r in state.evidence_requirements
    ) or "- (none specified)"
    passages = "\n\n".join(
        f"[{shown.passage_id}] {shown.body}" for shown in view(state)
    ) or "(no passages were retrieved)"
    return [
        {
            "role": "system",
            "content": _SYSTEM.format(
                labels=", ".join(f'"{label.value}"' for label in GapLabel),
                label_help="\n".join(f"  {k.value}: {v}" for k, v in _LABEL_HELP.items()),
            ),
        },
        {
            "role": "user",
            "content": _USER.format(
                question=state.question,
                question_type=state.question_type.value if state.question_type else "unknown",
                requirements=requirements,
                passages=passages,
            ),
        },
    ]


def build_critic_prompt(state: AgentState, view: PassageView = pool_view) -> str:
    """The same messages as one string, for clients that only take a prompt."""
    return "\n\n".join(
        message["content"] for message in build_critic_messages(state, view)
    )


def parse_critic_output(raw: str) -> CriticOutput:
    """Parse a model reply into `CriticOutput`.

    Scans for JSON objects instead of trusting the first and last brace, so prose,
    code fences and stray braces around the object are tolerated; the first object
    that matches the schema wins.
    """
    decoder = json.JSONDecoder()
    last_error = "reply contains no JSON object"
    for index, char in enumerate(raw):
        if char != "{":
            continue
        try:
            data, _ = decoder.raw_decode(raw, index)
        except json.JSONDecodeError as error:
            last_error = f"invalid JSON: {error}"
            continue
        if not isinstance(data, dict):
            continue
        try:
            return CriticOutput.model_validate(data)
        except ValueError as error:  # pydantic.ValidationError subclasses ValueError
            last_error = f"schema violation: {error}"
    raise CriticOutputError(last_error)


def validate_critic_output(
    output: CriticOutput, state: AgentState, passage_ids: Sequence[str] | None = None
) -> None:
    """Reject replies that are contradictory or ignore what was shown.

    `passage_ids` are the passages the critic was shown (default: everything retrieved).
    """
    problems = []
    shown = (
        [hit.passage.passage_id for hit in state.retrieved_passages]
        if passage_ids is None
        else list(passage_ids)
    )
    known = set(shown)
    unknown = [i for i in output.supporting_passage_ids if i not in known]
    if unknown:
        problems.append(f"supporting_passage_ids not among the retrieved passages: {unknown}")
    if not output.reason.strip():
        problems.append("reason is empty")
    if any(not item.strip() for item in output.missing_components):
        problems.append("missing_components contains an empty entry")
    if output.sufficient:
        if output.gap_label is not GapLabel.NONE:
            problems.append("sufficient=true requires gap_label NONE")
        if output.missing_components:
            problems.append("sufficient=true requires empty missing_components")
        if not shown:
            problems.append("sufficient=true but no passages were retrieved")
        elif not output.supporting_passage_ids:
            problems.append("sufficient=true requires supporting_passage_ids")
    elif output.gap_label is GapLabel.NONE:
        problems.append("sufficient=false requires a gap_label other than NONE")
    if problems:
        raise CriticOutputError("; ".join(problems))


def rule_based_critic(state: AgentState) -> CriticOutput:
    """Sufficient iff every evidence requirement has at least one mapped passage."""
    unmet = [r for r in state.evidence_requirements if not state.evidence_map.get(r.name)]
    if not unmet:
        return CriticOutput(
            sufficient=True,
            gap_label=GapLabel.NONE,
            missing_components=[],
            reason="Every required evidence component has a matching passage.",
            supporting_passage_ids=list(
                dict.fromkeys(i for ids in state.evidence_map.values() for i in ids)
            ),
        )
    return CriticOutput(
        sufficient=False,
        gap_label=gap_classifier(state)["gap_label"],
        missing_components=[r.description for r in unmet],
        reason="No retrieved passage matches: " + ", ".join(r.name for r in unmet) + ".",
    )


CriticClient = LLMClient | ChatClient
MAX_RAW_REPLY_CHARS = 2000
THINKING_MARKERS = ("<think>", "</think>")


def _ask(client: CriticClient, state: AgentState, view: PassageView) -> str:
    if isinstance(client, ChatClient):
        return client.chat(build_critic_messages(state, view))
    return client.complete(build_critic_prompt(state, view))


def make_critic_node(
    client: CriticClient | None = None,
    max_attempts: int = DEFAULT_ATTEMPTS,
    view: PassageView = pool_view,
):
    """Build the critic node. Each round's outcome is appended to `critic_log`.

    The log keeps every raw model reply (cut to MAX_RAW_REPLY_CHARS) so the first
    real traces can be inspected to validate the prompt. A round that shows the model
    exactly the passages of its previous verdict reuses that verdict (`source`
    "reused"). `view` is what the model is shown; cited ids must come from it.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    def critic_node(state: AgentState) -> dict:
        viewed = view(state)
        passage_ids = [shown.passage_id for shown in viewed]
        previous = state.critic_log[-1] if state.critic_log else None
        if (
            previous is not None
            and previous["source"] in ("llm", "reused")
            and previous["passage_ids"] == passage_ids
        ):
            # A retry that found nothing new hands the model the same input, so it
            # would repeat its verdict; skip the call and say so in the log.
            entry = {**previous, "round": state.retrieval_round, "source": "reused",
                     "errors": [], "raw_replies": [], "thinking_drift": False}
            return {
                "sufficient": previous["sufficient"],
                "gap_label": GapLabel(previous["gap_label"]),
                "missing_components": previous["missing_components"],
                "critic_reason": previous["reason"],
                "critic_log": [*state.critic_log, entry],
            }

        errors: list[str] = []
        raw_replies: list[str] = []
        output: CriticOutput | None = None
        source = "rules"
        if client is not None and viewed:
            source = "fallback"
            for _ in range(max_attempts):
                try:
                    raw = _ask(client, state, view)
                    raw_replies.append(raw[:MAX_RAW_REPLY_CHARS])
                    output = parse_critic_output(raw)
                    validate_critic_output(output, state, passage_ids)
                    source = "llm"
                    break
                except Exception as error:  # noqa: BLE001 - any client/reply failure retries
                    errors.append(f"{type(error).__name__}: {error}")
                    output = None
        if output is None:
            output = rule_based_critic(state)

        entry = {
            "round": state.retrieval_round,
            "source": source,
            "sufficient": output.sufficient,
            "gap_label": output.gap_label.value,
            "passage_ids": passage_ids,
            "supporting_passage_ids": output.supporting_passage_ids,
            "missing_components": output.missing_components,
            "reason": output.reason,
            "errors": errors,
            "raw_replies": raw_replies,
            # Qwen3 with thinking off should never emit these; if the backend silently
            # dropped enable_thinking=False the replies would carry a reasoning trace.
            "thinking_drift": any(m in r for r in raw_replies for m in THINKING_MARKERS),
        }
        return {
            "sufficient": output.sufficient,
            "gap_label": output.gap_label,
            "missing_components": output.missing_components,
            "critic_reason": output.reason,
            "critic_log": [*state.critic_log, entry],
        }

    return critic_node
