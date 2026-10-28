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
from typing import Protocol, runtime_checkable

from src.agent.nodes import gap_classifier
from src.agent.schemas import AgentState, CriticOutput, GapLabel

MAX_PASSAGE_CHARS = 1200
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
  "missing_components": [short descriptions of what is missing, empty if sufficient],
  "reason": "one or two sentences"
}}

Rules:
- If sufficient is true, gap_label must be "NONE" and missing_components must be [].
- If sufficient is false, gap_label must be one of the other labels:
{label_help}"""

_USER = """\
Question: {question}
Question type: {question_type}

Evidence the answer needs:
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


def build_critic_messages(state: AgentState) -> list[dict[str, str]]:
    """Chat messages for the critic: schema and labels in system, evidence in user."""
    requirements = "\n".join(
        f"- {r.name}: {r.description}" for r in state.evidence_requirements
    ) or "- (none specified)"
    passages = "\n\n".join(
        f"[{hit.passage.passage_id}] section: {hit.passage.section}\n"
        f"{hit.passage.text[:MAX_PASSAGE_CHARS]}"
        for hit in state.retrieved_passages
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


def build_critic_prompt(state: AgentState) -> str:
    """The same messages as one string, for clients that only take a prompt."""
    return "\n\n".join(message["content"] for message in build_critic_messages(state))


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


def validate_critic_output(output: CriticOutput, state: AgentState) -> None:
    """Reject replies that are contradictory or ignore what was retrieved."""
    problems = []
    if not output.reason.strip():
        problems.append("reason is empty")
    if any(not item.strip() for item in output.missing_components):
        problems.append("missing_components contains an empty entry")
    if output.sufficient:
        if output.gap_label is not GapLabel.NONE:
            problems.append("sufficient=true requires gap_label NONE")
        if output.missing_components:
            problems.append("sufficient=true requires empty missing_components")
        if not state.retrieved_passages:
            problems.append("sufficient=true but no passages were retrieved")
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
        )
    return CriticOutput(
        sufficient=False,
        gap_label=gap_classifier(state)["gap_label"],
        missing_components=[r.description for r in unmet],
        reason="No retrieved passage matches: " + ", ".join(r.name for r in unmet) + ".",
    )


CriticClient = LLMClient | ChatClient
MAX_RAW_REPLY_CHARS = 2000


def _ask(client: CriticClient, state: AgentState) -> str:
    if isinstance(client, ChatClient):
        return client.chat(build_critic_messages(state))
    return client.complete(build_critic_prompt(state))


def make_critic_node(client: CriticClient | None = None, max_attempts: int = DEFAULT_ATTEMPTS):
    """Build the critic node. Each round's outcome is appended to `critic_log`.

    The log keeps every raw model reply (cut to MAX_RAW_REPLY_CHARS) so the first
    real traces can be inspected to validate the prompt.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    def critic_node(state: AgentState) -> dict:
        errors: list[str] = []
        raw_replies: list[str] = []
        output: CriticOutput | None = None
        source = "rules"
        if client is not None and state.retrieved_passages:
            source = "fallback"
            for _ in range(max_attempts):
                try:
                    raw = _ask(client, state)
                    raw_replies.append(raw[:MAX_RAW_REPLY_CHARS])
                    output = parse_critic_output(raw)
                    validate_critic_output(output, state)
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
            "errors": errors,
            "raw_replies": raw_replies,
        }
        return {
            "sufficient": output.sufficient,
            "gap_label": output.gap_label,
            "missing_components": output.missing_components,
            "critic_reason": output.reason,
            "critic_log": [*state.critic_log, entry],
        }

    return critic_node
