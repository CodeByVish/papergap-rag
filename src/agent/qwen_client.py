"""Adapter from P5's generator backends to the critic's `ChatClient` (P4).

P5 owns model serving: `get_generator("vllm")` (src/generation/generators on
P5's branch) loads Qwen3-8B in-process, and its `chat()` returns raw text. The
cluster job that runs the agent must pass that same generator in rather than load
a second engine (one A40 fits one 8B model).

    generator = get_generator("vllm", model_id=...)
    client = GeneratorChatClient(generator)
    graph = build_agent_graph(retriever, critic_client=client)

Thinking is switched off explicitly on every call: Qwen3 defaults to a reasoning
trace that would consume the token budget before the JSON. The backend returns
text only, with no finish reason, so a reply cut off by the token limit is
detected from its unbalanced braces and asked for once more with a larger
budget. Any other bad reply is left to the critic's own retry.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Protocol

DEFAULT_MAX_NEW_TOKENS = 256
DEFAULT_TOP_P = 0.9
ESCALATION_FACTOR = 2


class ChatGenerator(Protocol):
    """The part of P5's `GeneratorBackend` the critic uses."""

    def chat(
        self,
        messages: Sequence[Mapping[str, str]],
        *,
        max_new_tokens: int = ...,
        temperature: float = ...,
        top_p: float = ...,
        enable_thinking: bool | None = ...,
    ) -> str: ...


def looks_truncated(text: str) -> bool:
    """True when a JSON object was opened but never closed (cut off mid-reply)."""
    return text.count("{") > text.count("}")


class GeneratorChatClient:
    """Greedy, short-budget critic calls through a shared generator."""

    def __init__(
        self,
        generator: ChatGenerator,
        *,
        max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
        temperature: float = 0.0,
        top_p: float = DEFAULT_TOP_P,
        enable_thinking: bool = False,
        escalation_factor: int = ESCALATION_FACTOR,
    ) -> None:
        if max_new_tokens < 1 or escalation_factor < 1:
            raise ValueError("max_new_tokens and escalation_factor must be positive")
        self.generator = generator
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.enable_thinking = enable_thinking
        self.escalation_factor = escalation_factor
        self.calls = 0
        self.escalations = 0

    def _chat(self, messages: list[dict[str, str]], budget: int) -> str:
        self.calls += 1
        return self.generator.chat(
            messages,
            max_new_tokens=budget,
            temperature=self.temperature,
            top_p=self.top_p,
            enable_thinking=self.enable_thinking,
        )

    def chat(self, messages: list[dict[str, str]]) -> str:
        reply = self._chat(messages, self.max_new_tokens)
        if looks_truncated(reply) and self.escalation_factor > 1:
            self.escalations += 1
            reply = self._chat(messages, self.max_new_tokens * self.escalation_factor)
        return reply
