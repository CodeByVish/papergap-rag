"""Tests for the critic's chat path and the adapter to P5's generator."""

import json

import pytest

from src.agent.critic import (
    ChatClient,
    CriticOutputError,
    build_critic_messages,
    build_critic_prompt,
    make_critic_node,
    parse_critic_output,
)
from src.agent.graph import build_agent_graph
from src.agent.qwen_client import GeneratorChatClient, looks_truncated
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore

VERDICT = {"sufficient": False, "gap_label": "MISSING_RESULT",
           "missing_components": ["reported accuracy"], "reason": "No numbers."}
GOOD = json.dumps(VERDICT)
GOOD_YES = json.dumps({"sufficient": True, "gap_label": "NONE", "missing_components": [],
                       "reason": "Result found."})


class FakeGenerator:
    """Mimics P5's `GeneratorBackend.chat`: replays replies, records every call."""

    def __init__(self, *replies):
        self.replies = list(replies)
        self.calls = []

    def chat(self, messages, *, max_new_tokens=256, temperature=0.0, top_p=0.9,
             enable_thinking=None):
        self.calls.append({"messages": messages, "max_new_tokens": max_new_tokens,
                           "temperature": temperature, "top_p": top_p,
                           "enable_thinking": enable_thinking})
        return self.replies.pop(0)


def hit(pid="p1", section="Method", text="We encode passages.") -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=pid, paper_id="paper", title="t", section=section,
                        chunk_number=0, text=text),
        rank=1, source_scores={"bm25": SourceScore(rank=1, score=1.0)}, rrf_score=0.1)


def state(*hits) -> AgentState:
    return AgentState(question="What accuracy did the model achieve?", paper_id="paper",
                      retrieved_passages=list(hits), retrieval_round=1)


# --- messages -------------------------------------------------------------

def test_messages_put_schema_and_labels_in_system_and_evidence_in_user():
    system, user = build_critic_messages(state(hit("abc", "Results", "F1 is 82.4.")))
    assert (system["role"], user["role"]) == ("system", "user")
    assert '"sufficient"' in system["content"] and "gap_label" in system["content"]
    assert all(label.value in system["content"] for label in GapLabel)
    assert "[abc] section: Results" in user["content"]
    assert user["content"].endswith("Reply with one JSON object and nothing else.")
    assert "[abc]" not in system["content"]


def test_prompt_string_is_the_two_messages_joined():
    messages = build_critic_messages(state(hit()))
    assert build_critic_prompt(state(hit())) == "\n\n".join(m["content"] for m in messages)


# --- parser ---------------------------------------------------------------

@pytest.mark.parametrize("raw", [
    GOOD,
    f"```json\n{GOOD}\n```",
    f"Sure! {GOOD} Hope that helps.",
    f"Note {{see below}} {GOOD} and {{another brace}}",
    f'{{"unrelated": 1}} {GOOD}',  # first object fails the schema, second passes
])
def test_parser_finds_the_critic_object_among_other_braces(raw):
    assert parse_critic_output(raw).gap_label is GapLabel.MISSING_RESULT


@pytest.mark.parametrize("raw", ["", "{}", '{"sufficient": tru', GOOD[:-10], "[1, 2]"])
def test_parser_still_rejects_unusable_replies(raw):
    with pytest.raises(CriticOutputError):
        parse_critic_output(raw)


# --- adapter --------------------------------------------------------------

def test_looks_truncated():
    assert looks_truncated(GOOD[:-5]) and not looks_truncated(GOOD)
    assert not looks_truncated("no braces here")


def test_adapter_is_greedy_short_budget_and_switches_thinking_off_explicitly():
    generator = FakeGenerator(GOOD)
    client = GeneratorChatClient(generator)
    assert client.chat([{"role": "user", "content": "x"}]) == GOOD
    (call,) = generator.calls
    assert (call["max_new_tokens"], call["temperature"], call["top_p"]) == (256, 0.0, 0.9)
    assert call["enable_thinking"] is False
    assert (client.calls, client.escalations) == (1, 0)


def test_adapter_retries_once_with_a_larger_budget_when_reply_is_cut_off():
    generator = FakeGenerator(GOOD[:-20], GOOD)
    client = GeneratorChatClient(generator)
    assert client.chat([{"role": "user", "content": "x"}]) == GOOD
    assert [c["max_new_tokens"] for c in generator.calls] == [256, 512]
    assert client.escalations == 1


def test_adapter_does_not_loop_when_still_truncated():
    generator = FakeGenerator(GOOD[:-20], GOOD[:-20])
    reply = GeneratorChatClient(generator).chat([{"role": "user", "content": "x"}])
    assert len(generator.calls) == 2 and looks_truncated(reply)


def test_adapter_rejects_bad_settings():
    with pytest.raises(ValueError):
        GeneratorChatClient(FakeGenerator(), max_new_tokens=0)


def test_adapter_satisfies_the_chat_client_protocol():
    assert isinstance(GeneratorChatClient(FakeGenerator()), ChatClient)


# --- critic node and graph ------------------------------------------------

def test_node_prefers_chat_over_complete():
    class Both:
        def chat(self, messages):
            self.messages = messages
            return GOOD

        def complete(self, prompt):
            raise AssertionError("complete should not be used")

    client = Both()
    update = make_critic_node(client)(state(hit()))
    assert update["critic_log"][0]["source"] == "llm"
    assert client.messages[0]["role"] == "system"


def test_node_keeps_raw_replies_for_inspection():
    update = make_critic_node(FakeChat("garbage", GOOD))(state(hit()))
    entry = update["critic_log"][0]
    assert entry["raw_replies"] == ["garbage", GOOD]
    assert entry["source"] == "llm" and len(entry["errors"]) == 1


def test_node_truncates_very_long_raw_replies():
    update = make_critic_node(FakeChat("x" * 5000, "y" * 5000))(state(hit()))
    assert [len(r) for r in update["critic_log"][0]["raw_replies"]] == [2000, 2000]


class FakeChat:
    def __init__(self, *replies):
        self.replies = list(replies)

    def chat(self, messages):
        return self.replies.pop(0)


def test_node_retries_after_truncation_then_falls_back_to_rules():
    # Both attempts are cut off even after escalation -> 4 generator calls, then rules.
    generator = FakeGenerator(*[GOOD[:-20]] * 4)
    update = make_critic_node(GeneratorChatClient(generator))(state(hit()))
    entry = update["critic_log"][0]
    assert entry["source"] == "fallback" and len(entry["errors"]) == 2
    assert len(generator.calls) == 4


def test_graph_runs_end_to_end_through_the_generator_adapter():
    generator = FakeGenerator(GOOD, GOOD_YES)
    calls = []

    def retriever(query, paper_id, top_k):
        calls.append(query)
        if len(calls) == 1:
            return [hit("m", "Method")]
        return [hit("m", "Method"), hit("r", "Results")]

    graph = build_agent_graph(retriever, critic_client=GeneratorChatClient(generator))
    result = graph.invoke(AgentState(question="What accuracy did the model achieve?",
                                     paper_id="paper"))
    assert result["sufficient"] is True and result["retrieval_round"] == 2
    assert [e["source"] for e in result["critic_log"]] == ["llm", "llm"]
    assert result["retrieval_log"][1]["triggered_by"] == "MISSING_RESULT"
