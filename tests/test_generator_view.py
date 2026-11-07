"""The critic reads exactly what P5's generator will read."""

import json

import pytest

from src.agent.critic import (
    CriticOutputError,
    ViewedPassage,
    build_critic_prompt,
    make_critic_node,
    parse_critic_output,
    pool_view,
    validate_critic_output,
)
from src.agent.generator_view import make_generator_view
from src.agent.nodes import map_evidence, plan_question
from src.agent.schemas import AgentState
from src.generation.prompts.grounded_qa import PromptConfig
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore


def hit(n: int, text: str = "short text for the view test") -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=f"pid-{n:02d}", paper_id="paper", title="t",
                        section="Results", chunk_number=n, text=text),
        rank=n, source_scores={"bm25": SourceScore(rank=n, score=1.0)},
        rrf_score=1.0 / (n + 1),  # pid-01 scores highest
    )


def state_with(*hits) -> AgentState:
    state = AgentState(question="What accuracy did the model achieve?", paper_id="paper",
                       retrieved_passages=list(hits), retrieval_round=1)
    state = state.model_copy(update=plan_question(state))
    return state.model_copy(update=map_evidence(state))


def reply(sufficient: bool, *cited: str) -> str:
    return json.dumps({
        "sufficient": sufficient, "gap_label": "NONE" if sufficient else "MISSING_RESULT",
        "supporting_passage_ids": list(cited), "evidence_quote": "short text for the view test",
        "missing_components": [] if sufficient else ["reported accuracy"], "reason": "r"})


class Chat:
    def __init__(self, *replies):
        self.replies, self.messages = list(replies), []

    def chat(self, messages):
        self.messages.append(messages)
        return self.replies.pop(0)


def test_view_shows_only_the_passages_the_generator_renders():
    state = state_with(*[hit(n) for n in range(1, 11)])
    shown = [v.passage_id for v in make_generator_view()(state)]
    assert len(shown) == PromptConfig().max_passages == 8
    assert shown == [f"pid-{n:02d}" for n in range(1, 9)]  # best scores; 9 and 10 are cut


def test_view_cuts_each_passage_where_the_generator_does():
    state = state_with(hit(1, "x" * 5000))
    body = make_generator_view()(state)[0].body
    assert "[...]" in body and "x" * PromptConfig().max_chars_per_passage not in body  # P5 marks the cut inside its budget
    assert "x" * 1000 in body
    assert "x" * 3000 in pool_view(state)[0].body  # the diagnostic pool view is wider


def test_view_follows_a_custom_budget():
    state = state_with(*[hit(n, "y" * 400) for n in range(1, 6)])
    view = make_generator_view(PromptConfig(max_passages=2, max_chars_per_passage=100))
    shown = view(state)
    assert [v.passage_id for v in shown] == ["pid-01", "pid-02"]
    assert "[...]" in shown[0].body and "y" * 100 not in shown[0].body
    assert "y" * 50 in shown[0].body


def test_view_of_an_empty_pool_is_empty():
    assert make_generator_view()(state_with()) == []


def test_prompt_lists_only_viewed_passages():
    state = state_with(*[hit(n) for n in range(1, 11)])
    prompt = build_critic_prompt(state, make_generator_view())
    assert "[p8]" in prompt and "[p9]" not in prompt and "pid-" not in prompt


def test_a_citation_outside_the_view_is_rejected_even_if_retrieved():
    state = state_with(*[hit(n) for n in range(1, 11)])
    shown = [v.passage_id for v in make_generator_view()(state)]
    output = parse_critic_output(reply(True, "pid-10"))  # retrieved, but never shown
    validate_critic_output(output, state)  # fine against the whole pool
    assert len(shown) == 8
    with pytest.raises(CriticOutputError, match="not among the retrieved passages"):
        validate_critic_output(output, state, shown)


def test_node_asks_the_model_about_the_view_and_rejects_unseen_citations():
    state = state_with(*[hit(n) for n in range(1, 11)])
    client = Chat(reply(True, "p9"), reply(True, "p9"))  # p9 was retrieved but not shown
    update = make_critic_node(client, view=make_generator_view())(state)
    assert update["critic_log"][0]["source"] == "fallback"
    assert update["critic_log"][0]["passage_ids"] == [f"pid-{n:02d}" for n in range(1, 9)]


def test_a_retry_that_only_adds_passages_beyond_the_view_reuses_the_verdict():
    first = state_with(*[hit(n) for n in range(1, 9)])
    client = Chat(reply(False))
    node = make_critic_node(client, view=make_generator_view())
    first = first.model_copy(update=node(first))
    bigger = first.model_copy(update={
        "retrieval_round": 2,
        "retrieved_passages": [*first.retrieved_passages, hit(9), hit(10)]})
    update = node(bigger)
    assert len(client.messages) == 1  # the model was not asked again
    assert update["critic_log"][1]["source"] == "reused"


def test_viewed_passage_is_a_plain_value():
    assert ViewedPassage("a", "b") == ViewedPassage("a", "b")
