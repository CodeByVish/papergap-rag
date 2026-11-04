"""Tests for gap-driven query rewriting."""

import pytest

from src.agent.rewriter import MAX_QUERY_WORDS, paper_terms, rewrite_query
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore

QUESTION = "What accuracy did the model achieve?"


def hit(passage_id: str, text: str) -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=passage_id, paper_id="p", title="t", section="s",
                        chunk_number=0, text=text),
        rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)},
        rrf_score=0.1,
    )


def state(label, hits=(), **fields) -> AgentState:
    return AgentState(question=QUESTION, paper_id="p", gap_label=label,
                      retrieved_passages=list(hits), **fields)


@pytest.mark.parametrize(("label", "expected"), [
    (GapLabel.MISSING_METHOD, "architecture"),
    (GapLabel.MISSING_EXPERIMENT_CONTEXT, "dataset"),
    (GapLabel.MISSING_RESULT, "results"),
    (GapLabel.MISSING_COMPARISON, "baseline"),
    (GapLabel.WEAK_EVIDENCE, "additional"),
])
def test_each_gap_adds_its_own_vocabulary(label, expected):
    query = rewrite_query(state(label))["rewritten_query"]
    assert query.startswith(QUESTION)
    assert expected in query.lower()


@pytest.mark.parametrize("label", [GapLabel.NONE, GapLabel.INSUFFICIENT_INFORMATION])
def test_no_rewrite_for_stop_labels(label):
    assert rewrite_query(state(label))["rewritten_query"] == QUESTION


def test_gaps_produce_different_queries():
    queries = {rewrite_query(state(label))["rewritten_query"] for label in (
        GapLabel.MISSING_METHOD, GapLabel.MISSING_RESULT, GapLabel.MISSING_COMPARISON)}
    assert len(queries) == 3


def test_paper_terms_use_recurring_vocabulary_not_question_words():
    hits = [hit("a", "The tagger uses a bidirectional LSTM-CRF encoder."),
            hit("b", "Our LSTM-CRF tagger was trained for ten epochs."),
            hit("c", "Unrelated sentence about weather.")]
    terms = paper_terms(state(GapLabel.TERMINOLOGY_MISMATCH, hits))
    assert terms[:2] == ["tagger", "lstm-crf"]
    assert "model" not in terms and "weather" not in terms  # once only / in question


def test_terminology_mismatch_expands_with_paper_terms():
    hits = [hit("a", "The tagger uses an LSTM-CRF encoder."),
            hit("b", "Our LSTM-CRF tagger was trained quickly.")]
    query = rewrite_query(state(GapLabel.TERMINOLOGY_MISMATCH, hits))["rewritten_query"]
    assert "tagger" in query and "lstm-crf" in query


def test_llm_missing_components_are_used_but_rule_based_ones_are_not():
    llm = state(GapLabel.MISSING_RESULT, missing_components=["reported test F1"],
                critic_log=[{"round": 1, "source": "llm"}])
    rules = state(GapLabel.MISSING_RESULT, missing_components=["Passage reporting a measured result"],
                  critic_log=[{"round": 1, "source": "rules"}])
    assert "f1" in rewrite_query(llm)["rewritten_query"].lower().split()
    assert "measured" not in rewrite_query(rules)["rewritten_query"]


def test_critic_commentary_is_kept_out_of_the_query():
    # A real Qwen3-8B reply (cluster job 50550): sentences about the passages, not terms.
    reply = ("The method of inducing the CFG is not clearly described in the retrieved passages. "
             "The passages mention grammar induction and seed rules but do not provide a "
             "detailed explanation of the specific method used to induce the CFG.")
    question = "How did they induce the CFG?"
    llm = AgentState(question=question, paper_id="p", gap_label=GapLabel.MISSING_METHOD,
                     missing_components=[reply], critic_log=[{"round": 1, "source": "llm"}])
    query = rewrite_query(llm)["rewritten_query"]
    assert query.startswith(question)
    for commentary in ("retrieved", "passages", "clearly", "described", "provide", "explanation"):
        assert commentary not in query.lower().split()
    assert "grammar" in query and "seed" in query
    assert len(query.split()) <= len(question.split()) + 4  # four critic terms, no prose, no gap words


def test_critic_terms_replace_the_fixed_gap_words_instead_of_adding_to_them():
    llm = state(GapLabel.MISSING_COMPARISON, missing_components=["names of the competing systems"],
                critic_log=[{"round": 1, "source": "llm"}])
    query = rewrite_query(llm)["rewritten_query"].lower().split()
    assert "competing" in query and "systems" in query
    for fixed in ("baseline", "comparison", "state-of-the-art", "outperform"):
        assert fixed not in query


def test_fixed_gap_words_are_the_fallback_when_the_critic_gave_no_usable_terms():
    for critic_log, missing in (([{"source": "llm"}], ["not clearly described in the passages"]),
                                ([{"source": "rules"}], ["Passage reporting a measured result"])):
        query = rewrite_query(state(GapLabel.MISSING_COMPARISON, missing_components=missing,
                                    critic_log=critic_log))["rewritten_query"].lower()
        assert "state-of-the-art" in query and "outperform" in query


def test_filler_verbs_from_the_critic_are_not_search_terms():
    # From job 50701: "... stating that the proposed model outperforms ..."
    llm = state(GapLabel.MISSING_COMPARISON, critic_log=[{"source": "llm"}],
                missing_components=["a passage stating that the proposed model outperforms baselines"])
    query = rewrite_query(llm)["rewritten_query"].lower().split()
    assert "stating" not in query and "proposed" not in query
    assert "outperforms" in query and "baselines" in query


def test_retry_never_repeats_an_earlier_query():
    hits = [hit("a", "The tagger uses an LSTM-CRF encoder with dropout regularisation."),
            hit("b", "Our LSTM-CRF tagger uses dropout regularisation and embeddings.")]
    first = rewrite_query(state(GapLabel.MISSING_RESULT, hits))["rewritten_query"]
    log = [{"query": first}]
    second = rewrite_query(state(GapLabel.MISSING_RESULT, hits, retrieval_log=log))
    assert second["rewritten_query"] != first
    assert second["rewritten_query"].startswith(first)


def test_query_is_capped_and_never_duplicates_words():
    query = rewrite_query(state(GapLabel.MISSING_RESULT,
                                missing_components=["x " * 100],
                                critic_log=[{"source": "llm"}]))["rewritten_query"]
    words = query.lower().split()
    assert len(words) <= MAX_QUERY_WORDS and len(words) == len(set(words))
