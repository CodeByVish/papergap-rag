"""The critic's view of the evidence, made identical to what P5's generator will read.

A critic that judges a passage cut at 3,000 characters while the answer step renders
8 passages cut at 1,200 can call the evidence sufficient on text the answer never
sees. `make_generator_view` asks P5's own code which passages the prompt renders
(`select_passages`) and how each is rendered (`visible_text`), so the two cannot
drift apart. P5 is imported only when the view is built, so the agent still works
without src/generation.
"""

from __future__ import annotations

from typing import Any

from src.agent.critic import PassageView, ViewedPassage
from src.agent.export import export_record
from src.agent.schemas import AgentState


def make_generator_view(prompt_config: Any = None) -> PassageView:
    """Build a `PassageView` from P5's prompt budget (default: the frozen `PromptConfig`)."""
    from src.generation.adapters.retrieval import build_request
    from src.generation.prompts.grounded_qa import PromptConfig, select_passages, visible_text

    config = prompt_config if prompt_config is not None else PromptConfig()

    def view(state: AgentState) -> list[ViewedPassage]:
        if not state.retrieved_passages:
            return []
        # The same record -> request path the answer step takes, on the state so far.
        request = build_request(export_record(state)).request
        return [
            ViewedPassage(passage.passage_id, visible_text(passage, config))
            for passage in select_passages(request, config)
        ]

    return view
