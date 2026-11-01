"""Tests for the evidence critic, driven by a fake LLM client."""

import json

import pytest

from src.agent.critic import (
    CriticOutputError,
    build_critic_prompt,
    make_critic_node,
    parse_critic_output,
    rule_based_critic,
    validate_critic_output,
)
from src.agent.graph import build_agent_graph
from src.agent.nodes import map_evidence, plan_question
from src.agent.schemas import AgentState, CriticOutput, GapLabel, QuestionType
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore

QUESTION = "What accuracy did the model achieve?"


class FakeLLM:
    """Replays canned replies; an Exception instance is raised instead."""

    def __init__(self, *replies):
        self.replies = list(replies)
        self.prompts = []

    def complete(self, prompt: str) -> str:
        self.prompts.append(prompt)
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply


def reply(**fields) -> str:
    base = {"sufficient": False, "gap_label": "MISSING_RESULT",
            "missing_components": ["reported accuracy"], "reason": "No numbers."}
    return json.dumps({**base, **fields})


GOOD_YES = reply(sufficient=True, gap_label="NONE", missing_components=[],
                 reason="Table gives 82.4 F1.")


def hit(passage_id="p1", section="Method", text="We encode passages.") -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=passage_id, paper_id="paper", title="t",
                        section=section, chunk_number=0, text=text),
        rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)},
        rrf_score=0.1,
    )


def state_with(*hits, question=QUESTION) -> AgentState:
    state = AgentState(question=question, paper_id="paper", retrieved_passages=list(hits))
    state = state.model_copy(update=plan_question(state))
    state = state.model_copy(update={"retrieval_round": 1})
    return state.model_copy(update=map_evidence(state))


# --- prompt ---------------------------------------------------------------

def test_prompt_contains_question_passages_requirements_and_labels():
    prompt = build_critic_prompt(state_with(hit("abc", "Results", "F1 is 82.4.")))
    assert QUESTION in prompt
    assert "[abc] section: Results" in prompt and "F1 is 82.4." in prompt
    assert "- result:" in prompt
    assert QuestionType.RESULT.value in prompt
    for label in GapLabel:
        assert label.value in prompt


def test_prompt_truncates_long_passages_and_handles_no_passages():
    long_text = "x" * 5000
    assert "x" * 1300 not in build_critic_prompt(state_with(hit(text=long_text)))
    assert "no passages were retrieved" in build_critic_prompt(state_with())


# --- parsing --------------------------------------------------------------

def test_parse_plain_fenced_and_prose_wrapped_json():
    for raw in (GOOD_YES, f"```json\n{GOOD_YES}\n```", f"Sure! Here it is: {GOOD_YES} Done."):
        assert parse_critic_output(raw).sufficient is True


@pytest.mark.parametrize("raw", [
    "", "no json here", "{not json}", "[1, 2]",
    reply(gap_label="MADE_UP"),
    json.dumps({"sufficient": True}),
    json.dumps({"sufficient": "maybe", "gap_label": "NONE", "reason": "x"}),
])
def test_parse_rejects_unusable_replies(raw):
    with pytest.raises(CriticOutputError):
        parse_critic_output(raw)


# --- validation -----------------------------------------------------------

def output(**fields) -> CriticOutput:
    return parse_critic_output(reply(**fields))


@pytest.mark.parametrize("fields", [
    {"sufficient": True, "gap_label": "MISSING_RESULT", "missing_components": []},
    {"sufficient": True, "gap_label": "NONE", "missing_components": ["something"]},
    {"sufficient": False, "gap_label": "NONE"},
    {"reason": "   "},
    {"missing_components": ["ok", " "]},
])
def test_validate_rejects_contradictions(fields):
    with pytest.raises(CriticOutputError):
        validate_critic_output(output(**fields), state_with(hit()))


def test_validate_rejects_sufficient_without_any_passage():
    good = output(sufficient=True, gap_label="NONE", missing_components=[])
    with pytest.raises(CriticOutputError, match="no passages"):
        validate_critic_output(good, state_with())
    validate_critic_output(good, state_with(hit()))  # accepted with passages


def test_validate_accepts_consistent_negative_verdict():
    validate_critic_output(output(), state_with(hit()))


# --- rule-based fallback --------------------------------------------------

def test_rule_based_critic_flags_unmet_requirement_with_its_gap_label():
    verdict = rule_based_critic(state_with(hit(section="Method", text="We encode.")))
    assert verdict.sufficient is False
    assert verdict.gap_label is GapLabel.MISSING_RESULT
    assert verdict.missing_components and verdict.reason


def test_rule_based_critic_accepts_when_every_requirement_is_mapped():
    verdict = rule_based_critic(state_with(hit(section="Results", text="F1 82.4.")))
    assert (verdict.sufficient, verdict.gap_label) == (True, GapLabel.NONE)


# --- node behaviour -------------------------------------------------------

def test_node_uses_llm_verdict_when_valid():
    client = FakeLLM(reply())
    update = make_critic_node(client)(state_with(hit()))
    assert update["sufficient"] is False
    assert update["gap_label"] is GapLabel.MISSING_RESULT
    assert update["missing_components"] == ["reported accuracy"]
    assert update["critic_reason"] == "No numbers."
    assert update["critic_log"][0] == {"round": 1, "source": "llm", "sufficient": False,
                                       "gap_label": "MISSING_RESULT", "errors": [],
                                       "raw_replies": [reply()], "thinking_drift": False}


def test_node_llm_can_override_rule_based_mapper():
    state = state_with(hit(section="Method", text="We encode."))
    assert rule_based_critic(state).sufficient is False
    update = make_critic_node(FakeLLM(GOOD_YES))(state)
    assert update["sufficient"] is True and update["gap_label"] is GapLabel.NONE


def test_node_retries_once_then_accepts():
    client = FakeLLM("garbage", reply())
    update = make_critic_node(client)(state_with(hit()))
    assert len(client.prompts) == 2
    entry = update["critic_log"][0]
    assert entry["source"] == "llm" and len(entry["errors"]) == 1


def test_node_falls_back_to_rules_after_repeated_bad_replies():
    client = FakeLLM("garbage", reply(sufficient=True))  # 2nd is contradictory
    update = make_critic_node(client)(state_with(hit(section="Method", text="We encode.")))
    entry = update["critic_log"][0]
    assert entry["source"] == "fallback" and len(entry["errors"]) == 2
    assert update["sufficient"] is False  # rule-based verdict


def test_node_flags_a_reasoning_trace_in_the_reply():
    client = FakeLLM("<think>hmm</think>" + GOOD_YES)
    entry = make_critic_node(client)(state_with(hit()))["critic_log"][0]
    assert entry["thinking_drift"] is True


def test_node_reports_no_drift_for_a_clean_reply():
    entry = make_critic_node(FakeLLM(GOOD_YES))(state_with(hit()))["critic_log"][0]
    assert entry["thinking_drift"] is False


def test_node_falls_back_when_client_raises():
    client = FakeLLM(TimeoutError("endpoint down"), RuntimeError("still down"))
    update = make_critic_node(client)(state_with(hit()))
    entry = update["critic_log"][0]
    assert entry["source"] == "fallback"
    assert "TimeoutError" in entry["errors"][0]


def test_node_skips_llm_when_nothing_was_retrieved():
    client = FakeLLM()
    update = make_critic_node(client)(state_with())
    assert client.prompts == []
    assert update["sufficient"] is False
    assert update["critic_log"][0]["source"] == "rules"


def test_node_without_client_uses_rules():
    update = make_critic_node(None)(state_with(hit(section="Results", text="F1 82.4.")))
    assert update["sufficient"] is True
    assert update["critic_log"][0]["source"] == "rules"


def test_node_rejects_zero_attempts():
    with pytest.raises(ValueError):
        make_critic_node(FakeLLM(), max_attempts=0)


# --- inside the graph -----------------------------------------------------

def test_graph_retries_on_llm_gap_then_stops_when_sufficient():
    method_hit = hit("m", "Method", "We encode passages.")
    results_hit = hit("r", "Results", "Our model achieves 82.4 F1.")
    calls = []

    def retriever(query, paper_id, top_k):
        calls.append(query)
        return [method_hit] if len(calls) == 1 else [method_hit, results_hit]

    client = FakeLLM(reply(), GOOD_YES)
    result = build_agent_graph(retriever, critic_client=client).invoke(
        AgentState(question=QUESTION, paper_id="paper")
    )
    assert result["sufficient"] is True and result["retrieval_round"] == 2
    assert [e["source"] for e in result["critic_log"]] == ["llm", "llm"]
    assert result["retrieval_log"][1]["triggered_by"] == "MISSING_RESULT"
    assert "results" in calls[1].lower()


def test_graph_stops_immediately_on_insufficient_information():
    client = FakeLLM(reply(gap_label="INSUFFICIENT_INFORMATION",
                           reason="The paper never discusses this."))
    result = build_agent_graph(lambda q, p, k: [hit()], critic_client=client).invoke(
        AgentState(question=QUESTION, paper_id="paper")
    )
    assert result["retrieval_round"] == 1
    assert result["sufficient"] is False
    assert result["gap_label"] is GapLabel.INSUFFICIENT_INFORMATION


def test_graph_without_client_matches_previous_rule_based_behaviour():
    result = build_agent_graph(lambda q, p, k: [hit()]).invoke(
        AgentState(question=QUESTION, paper_id="paper")
    )
    assert result["retrieval_round"] == 3 and result["sufficient"] is False
    assert {e["source"] for e in result["critic_log"]} == {"rules"}
