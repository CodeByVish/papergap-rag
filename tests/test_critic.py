"""Tests for the evidence critic, driven by a fake LLM client."""

import json

import pytest

from src.agent.critic import (
    ViewedPassage,
    MAX_PASSAGE_CHARS,
    CriticOutputError,
    normalise_handle,
    quote_supported,
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


def yes(*passage_ids: str, quote: str = "We encode passages with a bi-LSTM encoder") -> str:
    return reply(sufficient=True, gap_label="NONE", missing_components=[],
                 reason="Table gives 82.4 F1.", supporting_passage_ids=list(passage_ids),
                 evidence_quote=quote)


GOOD_YES = yes("p1")


def hit(passage_id="p1", section="Method", text="We encode passages with a bi-LSTM encoder.") -> RetrievedPassage:
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
    assert "[p1] section: Results" in prompt and "F1 is 82.4." in prompt
    assert "abc" not in prompt  # the critic is shown handles, not passage ids
    assert "- result:" in prompt
    assert QuestionType.RESULT.value in prompt
    for label in GapLabel:
        assert label.value in prompt


def test_prompt_truncates_long_passages_and_handles_no_passages():
    long_text = "x" * (MAX_PASSAGE_CHARS + 500)
    prompt = build_critic_prompt(state_with(hit(text=long_text)))
    assert "x" * MAX_PASSAGE_CHARS in prompt and "x" * (MAX_PASSAGE_CHARS + 1) not in prompt
    assert "no passages were retrieved" in build_critic_prompt(state_with())


def test_prompt_shows_a_whole_365_word_chunk():
    chunk = " ".join(["word"] * 365)  # about 1,800 chars, past the old 1,200 cap
    assert chunk in build_critic_prompt(state_with(hit(text=chunk)))


def test_prompt_defines_sufficiency_and_asks_for_supporting_ids():
    prompt = build_critic_prompt(state_with(hit()))
    assert "supporting_passage_ids" in prompt
    assert "partial but concrete answer counts" in prompt
    assert "heuristic" in prompt  # requirements are hints, not the bar


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
    good = output(sufficient=True, gap_label="NONE", missing_components=[],
                  supporting_passage_ids=["p1"])
    with pytest.raises(CriticOutputError, match="no passages"):
        validate_critic_output(good, state_with())
    validate_critic_output(good, state_with(hit()))  # accepted with passages


def test_validate_accepts_consistent_negative_verdict():
    validate_critic_output(output(), state_with(hit()))


def test_validate_requires_sufficient_verdicts_to_cite_a_retrieved_passage():
    state = state_with(hit("p1"), hit("p2"))
    uncited = output(sufficient=True, gap_label="NONE", missing_components=[])
    with pytest.raises(CriticOutputError, match="requires supporting_passage_ids"):
        validate_critic_output(uncited, state)
    invented = output(sufficient=True, gap_label="NONE", missing_components=[],
                      supporting_passage_ids=["p9"])
    with pytest.raises(CriticOutputError, match="not among the retrieved passages"):
        validate_critic_output(invented, state)
    cited = output(sufficient=True, gap_label="NONE", missing_components=[],
                   supporting_passage_ids=["p2"])
    validate_critic_output(cited, state)


def test_validate_rejects_invented_ids_in_a_negative_verdict_too():
    with pytest.raises(CriticOutputError, match="not among the retrieved passages"):
        validate_critic_output(output(supporting_passage_ids=["p9"]), state_with(hit("p1")))
    validate_critic_output(output(supporting_passage_ids=["p1"]), state_with(hit("p1")))


# --- rule-based fallback --------------------------------------------------

def test_rule_based_critic_flags_unmet_requirement_with_its_gap_label():
    verdict = rule_based_critic(state_with(hit(section="Method", text="We encode.")))
    assert verdict.sufficient is False
    assert verdict.gap_label is GapLabel.MISSING_RESULT
    assert verdict.missing_components and verdict.reason


def test_rule_based_critic_accepts_when_every_requirement_is_mapped():
    verdict = rule_based_critic(state_with(hit(section="Results", text="F1 82.4.")))
    assert (verdict.sufficient, verdict.gap_label) == (True, GapLabel.NONE)
    assert verdict.supporting_passage_ids == ["p1"]


# --- node behaviour -------------------------------------------------------

def test_node_uses_llm_verdict_when_valid():
    client = FakeLLM(reply())
    update = make_critic_node(client)(state_with(hit()))
    assert update["sufficient"] is False
    assert update["gap_label"] is GapLabel.MISSING_RESULT
    assert update["missing_components"] == ["reported accuracy"]
    assert update["critic_reason"] == "No numbers."
    assert update["critic_log"][0] == {
        "round": 1, "source": "llm", "sufficient": False, "gap_label": "MISSING_RESULT",
        "passage_ids": ["p1"], "supporting_passage_ids": [], "evidence_quote": "",
        "missing_components": ["reported accuracy"], "reason": "No numbers.",
        "errors": [], "raw_replies": [reply()], "thinking_drift": False}


def test_node_llm_can_override_rule_based_mapper():
    state = state_with(hit(section="Method"))
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


# --- a sufficient verdict must quote its evidence --------------------------

QUOTED = "We encode passages with a bi-LSTM encoder"


@pytest.mark.parametrize(("quote", "text", "ok"), [
    (QUOTED, "Intro. We encode passages with a bi-LSTM encoder. Next.", True),
    ("we ENCODE passages with a bi-lstm encoder", "We encode passages with a bi-LSTM encoder.", True),
    ("We encode passages ... a bi-LSTM encoder", "We encode passages with a bi-LSTM encoder.", True),
    ("We encode every passage with a CNN encoder", "We encode passages with a bi-LSTM encoder.", False),
    ("encode passages", "We encode passages with a bi-LSTM encoder.", False),  # too short to check
    ("", "We encode passages with a bi-LSTM encoder.", False),
])
def test_quote_must_come_from_the_text(quote, text, ok):
    assert quote_supported(quote, [text]) is ok


def test_a_sufficient_verdict_without_a_quote_is_rejected_and_retried():
    state = state_with(hit("a"))
    client = FakeLLM(yes("p1", quote=""), yes("p1"))
    update = make_critic_node(client)(state)
    entry = update["critic_log"][0]
    assert entry["source"] == "llm" and len(client.prompts) == 2
    assert "requires evidence_quote" in entry["errors"][0]
    assert entry["evidence_quote"] == QUOTED


def test_an_invented_quote_falls_back_to_the_rules():
    state = state_with(hit("a"))
    fake = yes("p1", quote="The model reaches ninety percent accuracy on the test set")
    update = make_critic_node(FakeLLM(fake, fake))(state)
    entry = update["critic_log"][0]
    assert entry["source"] == "fallback"
    assert "does not occur in the cited passages" in entry["errors"][0]


def test_the_quote_must_come_from_a_cited_passage_not_just_any_shown_one():
    state = state_with(hit("a", text="We encode passages with a bi-LSTM encoder."),
                       hit("b", text="Our model achieves 82.4 F1 on the dev set."))
    fake = yes("p2")  # cites the second passage but quotes the first
    update = make_critic_node(FakeLLM(fake, fake))(state)
    assert update["critic_log"][0]["source"] == "fallback"


def test_the_quote_is_checked_against_the_text_the_critic_was_shown():
    body_cut = lambda state: [ViewedPassage("a", "We encode passages")]  # the rest was cut
    state = state_with(hit("a"))
    update = make_critic_node(FakeLLM(GOOD_YES, GOOD_YES), view=body_cut)(state)
    assert update["critic_log"][0]["source"] == "fallback"


def test_the_prompt_asks_for_a_quote_and_says_topic_alone_does_not_count():
    prompt = build_critic_prompt(state_with(hit()))
    assert "evidence_quote" in prompt and "word for word" in prompt
    assert "only about the same topic does not count" in prompt


# --- citing passages by short handle --------------------------------------

def test_handles_are_resolved_to_the_real_passage_ids():
    state = state_with(hit("long-id-aaa"), hit("long-id-bbb"))
    update = make_critic_node(FakeLLM(yes("p2")))(state)
    entry = update["critic_log"][0]
    assert entry["source"] == "llm" and entry["supporting_passage_ids"] == ["long-id-bbb"]
    assert entry["raw_replies"] == [yes("p2")]  # the log keeps what the model wrote


@pytest.mark.parametrize("spelling", ["p2", "P2", "[p2]", " p 2 ", "2"])
def test_handles_are_read_leniently(spelling):
    assert normalise_handle(spelling) == "p2"
    state = state_with(hit("a"), hit("b"))
    update = make_critic_node(FakeLLM(yes(spelling)))(state)
    assert update["critic_log"][0]["supporting_passage_ids"] == ["b"]


def test_an_unknown_handle_or_a_raw_id_is_rejected():
    state = state_with(hit("a"), hit("b"))
    for cited in ("p3", "a"):  # only p1 and p2 were shown; "a" is an id, not a handle
        update = make_critic_node(FakeLLM(yes(cited), yes(cited)))(state)
        assert update["critic_log"][0]["source"] == "fallback"
        assert "not among the retrieved passages" in update["critic_log"][0]["errors"][0]


def test_citing_the_same_passage_twice_counts_once():
    state = state_with(hit("a"), hit("b"))
    update = make_critic_node(FakeLLM(yes("p1", "P1")))(state)
    assert update["critic_log"][0]["supporting_passage_ids"] == ["a"]


# --- reusing a verdict when a retry brings nothing new ---------------------

def test_node_reuses_the_verdict_when_the_passages_did_not_change():
    client = FakeLLM(reply())
    node = make_critic_node(client)
    first = state_with(hit("p1"))
    first = first.model_copy(update=node(first))
    second = first.model_copy(update={"retrieval_round": 2})
    update = node(second)
    assert len(client.prompts) == 1  # no second model call
    assert update["sufficient"] is False and update["gap_label"] is GapLabel.MISSING_RESULT
    assert update["missing_components"] == ["reported accuracy"]
    assert update["critic_reason"] == "No numbers."
    entry = update["critic_log"][1]
    assert (entry["round"], entry["source"], entry["raw_replies"]) == (2, "reused", [])
    assert entry["passage_ids"] == ["p1"]


def test_node_asks_again_when_a_retry_added_a_passage():
    client = FakeLLM(reply(), yes("p2"))
    node = make_critic_node(client)
    first = state_with(hit("p1"))
    first = first.model_copy(update=node(first))
    second = first.model_copy(update={
        "retrieval_round": 2,
        "retrieved_passages": [*first.retrieved_passages, hit("p2")]})
    update = node(second)
    assert len(client.prompts) == 2
    assert update["critic_log"][1]["source"] == "llm" and update["sufficient"] is True


def test_node_does_not_reuse_a_rules_or_fallback_verdict():
    node = make_critic_node(FakeLLM("garbage", "garbage", reply()))
    first = state_with(hit("p1"))
    first = first.model_copy(update=node(first))
    assert first.critic_log[0]["source"] == "fallback"
    update = node(first.model_copy(update={"retrieval_round": 2}))
    assert update["critic_log"][1]["source"] == "llm"


def test_graph_skips_the_model_on_a_retry_that_finds_nothing_new():
    client = FakeLLM(reply())
    result = build_agent_graph(lambda q, p, k: [hit()], critic_client=client).invoke(
        AgentState(question=QUESTION, paper_id="paper")
    )
    assert result["retrieval_round"] == 3 and result["sufficient"] is False
    assert len(client.prompts) == 1
    assert [e["source"] for e in result["critic_log"]] == ["llm", "reused", "reused"]


# --- inside the graph -----------------------------------------------------

def test_graph_retries_on_llm_gap_then_stops_when_sufficient():
    method_hit = hit("m", "Method", "We encode passages with a bi-LSTM encoder.")
    results_hit = hit("r", "Results", "Our model achieves 82.4 F1.")
    calls = []

    def retriever(query, paper_id, top_k):
        calls.append(query)
        return [method_hit] if len(calls) == 1 else [method_hit, results_hit]

    client = FakeLLM(reply(), yes("p2", quote="Our model achieves 82.4 F1"))  # p2 is the Results passage, id "r"
    result = build_agent_graph(retriever, critic_client=client).invoke(
        AgentState(question=QUESTION, paper_id="paper")
    )
    assert result["sufficient"] is True and result["retrieval_round"] == 2
    assert [e["source"] for e in result["critic_log"]] == ["llm", "llm"]
    assert result["retrieval_log"][1]["triggered_by"] == "MISSING_RESULT"
    assert "reported" in calls[1].lower()  # the critic's own term, not the fixed gap words


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
