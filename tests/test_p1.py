"""BM25 behavior and P2 callback compatibility using synthetic passages only."""

import math
from collections import Counter
from pathlib import Path

import pytest

from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import Passage, RetrievalHit, RetrievedPassage


@pytest.fixture
def passages():
    fixture = Path(__file__).parent / "fixtures/mock_passages.jsonl"
    return [
        Passage.model_validate_json(line)
        for line in fixture.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


@pytest.fixture
def retriever(passages):
    return BM25Retriever(passages)


def test_fixture_contains_multiple_papers_and_unique_ids(passages):
    counts = Counter(passage.paper_id for passage in passages)
    assert counts == {"synthetic-ir": 4, "synthetic-energy": 4}
    assert len({passage.passage_id for passage in passages}) == len(passages)


def test_normal_top_k_returns_retrieval_hits(retriever):
    results = retriever.retrieve("lexical", "synthetic-ir", top_k=2)
    assert isinstance(results, list)
    assert len(results) == 2
    assert all(isinstance(hit, RetrievalHit) for hit in results)


def test_top_k_larger_than_paper_returns_all_available(retriever):
    results = retriever.retrieve("lexical", "synthetic-ir", top_k=20)
    assert len(results) == 4


@pytest.mark.parametrize(
    ("query", "paper_id"),
    [("battery", "synthetic-ir"), ("lexical", "synthetic-energy")],
)
def test_paper_filtering_keeps_candidates_when_other_paper_matches(
    retriever, query, paper_id
):
    # The matching passage belongs to the other paper. Filtering a global top-1
    # would lose the selected paper's candidate entirely.
    results = retriever.retrieve(query, paper_id, top_k=1)
    assert len(results) == 1
    assert results[0].passage.paper_id == paper_id


def test_bm25_scores_use_only_selected_paper(passages, retriever):
    selected = [p for p in passages if p.paper_id == "synthetic-ir"]
    isolated = BM25Retriever(selected).retrieve("lexical", "synthetic-ir", 4)
    combined = retriever.retrieve("lexical", "synthetic-ir", 4)
    assert [hit.passage for hit in combined] == [hit.passage for hit in isolated]
    assert [hit.score for hit in combined] == pytest.approx(
        [hit.score for hit in isolated]
    )


def test_unknown_paper_returns_empty_list(retriever):
    assert retriever.retrieve("lexical", "unknown-paper", top_k=2) == []


@pytest.mark.parametrize("query", ["", " ", "\t\n", None, 123])
def test_invalid_query_raises_value_error(retriever, query):
    with pytest.raises(ValueError):
        retriever.retrieve(query, "synthetic-ir", top_k=2)


@pytest.mark.parametrize("paper_id", ["", " ", "\t\n", None, 123])
def test_invalid_paper_id_raises_value_error(retriever, paper_id):
    with pytest.raises(ValueError):
        retriever.retrieve("lexical", paper_id, top_k=2)


@pytest.mark.parametrize("top_k", [0, -1, -10, True, False, 1.5, "2", None])
def test_invalid_top_k_raises_value_error(retriever, top_k):
    with pytest.raises(ValueError):
        retriever.retrieve("lexical", "synthetic-ir", top_k=top_k)


def test_retrieval_preserves_stable_ids_and_all_passage_fields(passages, retriever):
    before = [passage.model_dump() for passage in passages]
    results = retriever.retrieve("lexical", "synthetic-ir", top_k=20)
    originals = {passage.passage_id: passage for passage in passages}
    assert {hit.passage.passage_id for hit in results} == {
        "synthetic-ir-001",
        "synthetic-ir-002",
        "synthetic-ir-003",
        "synthetic-ir-004",
    }
    assert all(hit.passage == originals[hit.passage.passage_id] for hit in results)
    assert [passage.model_dump() for passage in passages] == before
    assert retriever.retrieve("lexical", "synthetic-ir", 20) == results


def test_equal_scores_have_unique_continuous_one_based_ranks(retriever):
    results = retriever.retrieve("unseenquerytoken", "synthetic-ir", top_k=4)
    assert all(hit.score == 0.0 for hit in results)
    assert [hit.rank for hit in results] == [1, 2, 3, 4]


def test_scores_are_finite_floats_and_descending(retriever):
    results = retriever.retrieve("lexical", "synthetic-ir", top_k=4)
    scores = [hit.score for hit in results]
    assert all(isinstance(score, float) and math.isfinite(score) for score in scores)
    assert scores == sorted(scores, reverse=True)


def test_results_never_repeat_a_passage(retriever):
    results = retriever.retrieve("lexical lexical lexical", "synthetic-ir", 20)
    ids = [hit.passage.passage_id for hit in results]
    assert len(ids) == len(set(ids)) == 4


def test_query_term_match_ranks_above_unrelated_passages(retriever):
    results = retriever.retrieve("lexical", "synthetic-ir", 4)
    assert results[0].passage.passage_id == "synthetic-ir-001"
    assert results[0].score > results[1].score


def test_query_tokenization_ignores_case_and_punctuation(retriever):
    assert retriever.retrieve("LEXICAL!!!", "synthetic-ir", 4) == retriever.retrieve(
        "lexical", "synthetic-ir", 4
    )


@pytest.mark.parametrize(("text", "query"), [("检索", "检索"), ("Straße", "STRASSE")])
def test_unicode_terms_are_searchable(passages, text, query):
    corpus = passages[:3]
    corpus[0] = corpus[0].model_copy(update={"text": text})
    results = BM25Retriever(corpus).retrieve(query, "synthetic-ir", 3)
    assert results[0].passage.passage_id == corpus[0].passage_id
    assert results[0].score > 0.0


def test_ties_are_deterministic_across_input_order(passages, retriever):
    expected = retriever.retrieve("unseenquerytoken", "synthetic-ir", 4)
    reordered = BM25Retriever(reversed(passages)).retrieve(
        "unseenquerytoken", "synthetic-ir", 4
    )
    assert reordered == expected
    assert [hit.passage.passage_id for hit in expected] == [
        "synthetic-ir-001",
        "synthetic-ir-002",
        "synthetic-ir-003",
        "synthetic-ir-004",
    ]


def test_duplicate_input_passage_id_is_rejected(passages):
    with pytest.raises(ValueError):
        BM25Retriever([*passages, passages[0]])


def test_empty_corpus_returns_empty_list():
    assert BM25Retriever([]).retrieve("lexical", "synthetic-ir", 2) == []


def test_paper_with_no_word_tokens_returns_finite_zero_scores(passages):
    corpus = [p.model_copy(update={"text": "!!! ..."}) for p in passages[:3]]
    results = BM25Retriever(corpus).retrieve("lexical", "synthetic-ir", 3)
    assert len(results) == 3
    assert all(hit.score == 0.0 and math.isfinite(hit.score) for hit in results)
    assert [hit.rank for hit in results] == [1, 2, 3]


def test_punctuation_only_query_returns_zero_scores(retriever):
    results = retriever.retrieve("!!! ...", "synthetic-ir", 4)
    assert len(results) == 4
    assert all(hit.score == 0.0 for hit in results)


def test_bm25_callback_integrates_with_existing_hybrid(retriever):
    hybrid = HybridRetriever(retriever.retrieve, lambda *args: [], candidate_k=4)
    results = hybrid.retrieve("lexical", "synthetic-ir", top_k=2)
    sparse = retriever.retrieve("lexical", "synthetic-ir", top_k=2)
    assert len(results) == 2
    assert all(isinstance(hit, RetrievedPassage) for hit in results)
    assert [hit.passage for hit in results] == [hit.passage for hit in sparse]
    assert [hit.rank for hit in results] == [1, 2]
    for fused, original in zip(results, sparse):
        assert set(fused.source_scores) == {"bm25"}
        assert fused.source_scores["bm25"].rank == original.rank
        assert fused.source_scores["bm25"].score == original.score
