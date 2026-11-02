"""Tests for per-paper section selection and the same-round scope fallback."""

import json

import pytest

from src.agent.graph import build_agent_graph
from src.agent.nodes import make_retrieve_node
from src.agent.schemas import AgentState, GapLabel
from src.agent.sections import choose_section, make_section_selector
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore


def passage(pid, section, text, paper="paper") -> Passage:
    return Passage(passage_id=pid, paper_id=paper, title="t", section=section,
                   chunk_number=0, text=text)


PASSAGES = [
    passage("i1", "Introduction", "We study tagging with a bidirectional model."),
    passage("m1", "Baseline Model", "The tagger uses an encoder and a linear layer."),
    passage("e1", "Experiments", "Training uses a held-out dataset split."),
    passage("r1", "Experiments ::: Results", "The tagger reaches 91.2 accuracy and 88 F1."),
    passage("r2", "Experiments ::: Results", "Accuracy improves with more data."),
    passage("c1", "Conclusion", "We presented a tagger."),
    passage("o1", "Introduction", "Other paper text about tagging.", paper="other"),
]


# --- choose_section -------------------------------------------------------

def test_prefers_earlier_hint_then_document_order():
    hints = ["result", "evaluation", "experiment"]
    assert choose_section(["Experiments", "Results"], hints, set()) == "Results"
    assert choose_section(["Evaluation", "Experiments"], hints, set()) == "Evaluation"
    assert choose_section(["Results A", "Results B"], hints, set()) == "Results A"


def test_skips_used_sections_and_returns_none_when_nothing_matches():
    hints = ["result"]
    assert choose_section(["Results", "Results ::: Extra"], hints, {"Results"}) == "Results ::: Extra"
    assert choose_section(["Results"], hints, {"Results"}) is None
    assert choose_section(["Introduction"], hints, set()) is None
    assert choose_section([], hints, set()) is None


# --- selector -------------------------------------------------------------

def state(label, paper="paper", log=()) -> AgentState:
    return AgentState(question="q", paper_id=paper, gap_label=label, retrieval_log=list(log))


@pytest.fixture(scope="module")
def selector():
    return make_section_selector(PASSAGES)


@pytest.mark.parametrize(("label", "expected"), [
    (GapLabel.MISSING_RESULT, "Experiments ::: Results"),
    (GapLabel.MISSING_METHOD, "Baseline Model"),
    (GapLabel.MISSING_EXPERIMENT_CONTEXT, "Experiments"),  # first "experiment" section
])
def test_selector_matches_this_papers_own_section_names(selector, label, expected):
    assert selector(state(label)) == expected


@pytest.mark.parametrize("label", [
    GapLabel.NONE, GapLabel.TERMINOLOGY_MISMATCH, GapLabel.WEAK_EVIDENCE,
    GapLabel.INSUFFICIENT_INFORMATION,
])
def test_selector_does_not_scope_labels_without_hints(selector, label):
    assert selector(state(label)) is None


def test_selector_unknown_paper_and_paper_without_matching_section(selector):
    assert selector(state(GapLabel.MISSING_RESULT, paper="nope")) is None
    # The other paper has only an Introduction, so no section matches.
    assert selector(state(GapLabel.MISSING_RESULT, paper="other")) is None


def test_selector_never_repeats_a_searched_section(selector):
    log = [{"section": "Experiments ::: Results"}]
    # Next best section for results is "Experiments" (a later hint).
    assert selector(state(GapLabel.MISSING_RESULT, log=log)) == "Experiments"
    log.append({"section": "Experiments"})
    assert selector(state(GapLabel.MISSING_RESULT, log=log)) is None


# --- retrieve node fallback -----------------------------------------------

def hit(pid="x") -> RetrievedPassage:
    return RetrievedPassage(
        passage=passage(pid, "Experiments", "text"), rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)}, rrf_score=0.1)


def test_empty_scoped_result_falls_back_to_whole_paper_in_same_round():
    calls = []

    def retriever(query, paper_id, top_k, **scope):
        calls.append(scope)
        return [] if scope else [hit()]

    node = make_retrieve_node(retriever, 5, lambda s: "Results")
    update = node(AgentState(question="q", paper_id="paper"))
    assert calls == [{"section": "Results"}, {}]
    assert update["retrieval_round"] == 1  # one round, not two
    entry = update["retrieval_log"][0]
    assert entry["section"] == "Results" and entry["scope_fallback"] is True
    assert entry["passage_ids"] == ["x"]
    # Both attempts are timed: the scoped one alone, then scoped + unscoped together.
    assert 0 <= entry["scoped_retrieval_ms"] <= entry["retrieval_ms"]


def test_nonempty_scoped_result_does_not_fall_back():
    calls = []

    def retriever(query, paper_id, top_k, **scope):
        calls.append(scope)
        return [hit()]

    node = make_retrieve_node(retriever, 5, lambda s: "Results")
    entry = node(AgentState(question="q", paper_id="paper"))["retrieval_log"][0]
    assert calls == [{"section": "Results"}] and entry["scope_fallback"] is False
    assert entry["scoped_retrieval_ms"] == pytest.approx(entry["retrieval_ms"], abs=5)


def test_unscoped_empty_result_is_not_a_fallback():
    node = make_retrieve_node(lambda q, p, k: [], 5)
    entry = node(AgentState(question="q", paper_id="paper"))["retrieval_log"][0]
    assert entry["section"] is None and entry["scope_fallback"] is False
    assert entry["scoped_retrieval_ms"] is None


# --- end to end with P2's scoped hybrid retriever -------------------------

class CriticClient:
    """Reports a missing result until a results passage has been retrieved."""

    def complete(self, prompt: str) -> str:
        found = "[r1]" in prompt or "[r2]" in prompt
        return json.dumps({
            "sufficient": found,
            "gap_label": "NONE" if found else "MISSING_RESULT",
            "missing_components": [] if found else ["reported accuracy"],
            "reason": "Results found." if found else "No numbers yet.",
        })


def test_graph_retries_into_the_papers_results_section():
    from src.retrieval.scoped import SectionScopedRetriever

    sparse = BM25Retriever(PASSAGES)
    scoped = SectionScopedRetriever(sparse.retrieve, PASSAGES)
    hybrid = HybridRetriever(scoped, scoped)
    graph = build_agent_graph(
        hybrid.retrieve, critic_client=CriticClient(),
        section_selector=make_section_selector(PASSAGES), top_k=1,
    )
    result = graph.invoke(AgentState(question="Which encoder layer design is used?",
                                     paper_id="paper"))
    first, second = result["retrieval_log"]
    assert first["section"] is None
    assert second["section"] == "Experiments ::: Results"
    assert second["triggered_by"] == "MISSING_RESULT"
    assert set(second["passage_ids"]) <= {"r1", "r2"} and second["passage_ids"]
    assert result["sufficient"] is True and result["retrieval_round"] == 2
