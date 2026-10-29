"""Prompt templates for P5."""

from src.generation.prompts.grounded_qa import (
    PROMPT_VERSION,
    SYSTEM_PROMPT,
    PromptConfig,
    build_messages,
    build_prompt,
    format_passage,
)

__all__ = [
    "PROMPT_VERSION",
    "SYSTEM_PROMPT",
    "PromptConfig",
    "build_messages",
    "build_prompt",
    "format_passage",
]
