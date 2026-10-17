"""Offline checks for P1 section filters, caller queries and BM25 snapshots."""

import json
import math
from functools import partial

import numpy as np
import pytest

from src.retrieval import bm25_retriever as bm25_module
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import QUERY_INSTRUCTION, DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import Passage, RetrievalHit


class SectionEncoder:
    """Controlled vectors expose wrong filtering and stale rewritten queries."""

    model_name = "test/section-vectors"
    revision = "v1"

    def __init__(self):
        self.calls = []

    def encode(self, texts):
        self.calls.append(list(texts))
        vectors = []
        for text in texts:
            if text.startswith(QUERY_INSTRUCTION):
                query = text.removeprefix(QUERY_INSTRUCTION)
                vectors.append([0, 1, 0] if query == "gamma" else [1, 0, 0])
            elif text.startswith("alpha"):
                vectors.append([1, 0, 0])
            elif text.startswith("beta"):
                vectors.append([0.8, 0.6, 0])
            elif text.startswith("gamma"):
                vectors.append([0, 1, 0])
            else:
                vectors.append([0, 0, 1])
        return np.asarray(vectors, dtype=np.float32)


@pytest.fixture
def section_passages():
    records = [
        ("a-results", "paper-a", "Results", "alpha alpha alpha alpha"),
        ("a-method-b", "paper-a", "Methods", "beta method second"),
        ("a-method-a", "paper-a", "Methods", "beta method first"),
        ("a-method-c", "paper-a", "Methods", "gamma method third"),
        ("a-background", "paper-a", "Introduction", "delta background"),
        ("a-extra", "paper-a", "Introduction", "zeta background"),
        ("b-method", "paper-b", "Methods", "alpha foreign paper"),
    ]
    return [
        Passage(
            passage_id=passage_id,
            paper_id=paper_id,
            title=f"Title for {paper_id}",
            section=section,
            chunk_number=number,
            text=text,
            previous_passage_id=records[number - 1][0] if 0 < number < 6 else None,
            next_passage_id=records[number + 1][0] if number < 5 else None,
        )
        for number, (passage_id, paper_id, section, text) in enumerate(records)
    ]


@pytest.fixture(params=["bm25", "dense"])
def section_retriever(request, section_passages):
    if request.param == "bm25":
        return BM25Retriever(section_passages)
    return DenseRetriever(section_passages, encoder=SectionEncoder())


def test_section_filter_precedes_top_k_and_breaks_boundary_ties(section_retriever):
    unfiltered = section_retriever.retrieve("alpha", "paper-a", 1)
    assert unfiltered[0].passage.passage_id == "a-results"
    filtered = section_retriever.retrieve("alpha", "paper-a", 2, section="Methods")
    assert [hit.passage.passage_id for hit in filtered] == [
        "a-method-a",
        "a-method-b",
    ]
    assert [hit.rank for hit in filtered] == [1, 2]
    assert all(isinstance(hit, RetrievalHit) for hit in filtered)
    assert all(hit.passage.paper_id == "paper-a" for hit in filtered)
    scores = [hit.score for hit in filtered]
    assert all(math.isfinite(score) for score in scores)
    assert scores == sorted(scores, reverse=True)
    assert filtered == section_retriever.retrieve(
        "alpha", "paper-a", 2, section="Methods"
    )


def test_section_filter_preserves_whole_paper_scores_and_original_passages(
    section_retriever, section_passages
):
    whole = section_retriever.retrieve("beta", "paper-a", 20)
    expected = [hit for hit in whole if hit.passage.section == "Methods"]
    filtered = section_retriever.retrieve("beta", "paper-a", 20, section="Methods")
    assert len(filtered) == 3
    assert [hit.passage for hit in filtered] == [hit.passage for hit in expected]
    assert [hit.score for hit in filtered] == pytest.approx(
        [hit.score for hit in expected]
    )
    assert [hit.rank for hit in filtered] == [1, 2, 3]
    originals = {p.passage_id: p.model_dump() for p in section_passages}
    assert all(
        hit.passage.model_dump() == originals[hit.passage.passage_id]
        for hit in filtered
    )
    assert len({hit.passage.passage_id for hit in filtered}) == len(filtered)


@pytest.mark.parametrize("section", ["unknown", "methods", " Methods "])
def test_section_match_is_exact_and_unknown_returns_empty(section_retriever, section):
    assert section_retriever.retrieve("alpha", "paper-a", 2, section=section) == []
    assert section_retriever.retrieve("alpha", "absent", 2, section=section) == []


@pytest.mark.parametrize("section", ["", " ", "\t\n", 123, True, []])
def test_invalid_section_rejected_even_for_unknown_paper(section_retriever, section):
    with pytest.raises(ValueError, match="section"):
        section_retriever.retrieve("alpha", "absent", 2, section=section)


def test_three_argument_call_and_none_section_are_identical(section_retriever):
    assert section_retriever.retrieve("alpha", "paper-a", 2) == (
        section_retriever.retrieve("alpha", "paper-a", 2, section=None)
    )
    with pytest.raises(TypeError):
        section_retriever.retrieve("alpha", "paper-a", 2, "Methods")


def test_rewritten_query_from_caller_changes_ranking(section_retriever):
    first = section_retriever.retrieve("beta", "paper-a", 1, section="Methods")
    rewritten = section_retriever.retrieve("gamma", "paper-a", 1, section="Methods")
    assert first[0].passage.passage_id == "a-method-a"
    assert rewritten[0].passage.passage_id == "a-method-c"
    assert section_retriever.retrieve("beta", "paper-a", 1, section="Methods") == first


def test_existing_hybrid_accepts_unmodified_three_argument_callbacks(section_passages):
    sparse = BM25Retriever(section_passages)
    dense = DenseRetriever(section_passages, encoder=SectionEncoder())
    hybrid = HybridRetriever(sparse.retrieve, dense.retrieve, candidate_k=6)
    hits = hybrid.retrieve("alpha", "paper-a", 3)
    assert len(hits) == 3
    assert [hit.rank for hit in hits] == [1, 2, 3]
    assert all(hit.passage.paper_id == "paper-a" for hit in hits)
    assert all(set(hit.source_scores) == {"bm25", "dense"} for hit in hits)


def test_bm25_json_roundtrip_restores_fields_and_rebuilds_terms(
    section_passages, tmp_path, monkeypatch
):
    original = BM25Retriever(section_passages)
    directory = tmp_path / "bm25"
    original.save(directory)
    metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["index_type"] == "BM25Okapi"
    assert metadata["tokenization"] == "unicode-word-regex-casefold-v1"
    assert metadata["rank_bm25_version"]
    assert (metadata["k1"], metadata["b"], metadata["epsilon"]) == (1.5, 0.75, 0.25)
    saved = {
        p["passage_id"]: p for paper in metadata["papers"] for p in paper["passages"]
    }
    assert saved == {p.passage_id: p.model_dump() for p in section_passages}
    assert [path.name for path in directory.iterdir()] == ["metadata.json"]

    tokenize = bm25_module._tokenize
    tokenized_texts = []

    def record_tokenize(text):
        tokenized_texts.append(text)
        return tokenize(text)

    monkeypatch.setattr(bm25_module, "_tokenize", record_tokenize)
    loaded = BM25Retriever.load(directory)
    assert sorted(tokenized_texts) == sorted(p.text for p in section_passages)
    for paper_id in ("paper-a", "paper-b"):
        for query in ("alpha", "beta", "gamma", "unmatched"):
            for section in (None, "Methods", "missing"):
                assert loaded.retrieve(query, paper_id, 20, section=section) == (
                    original.retrieve(query, paper_id, 20, section=section)
                )


def test_bm25_empty_snapshot_and_nonempty_output_protection(tmp_path):
    directory = tmp_path / "bm25"
    directory.mkdir()
    BM25Retriever([]).save(directory)
    assert BM25Retriever.load(directory).retrieve("alpha", "missing", 2) == []
    content = (directory / "metadata.json").read_bytes()
    with pytest.raises(ValueError, match="new or empty"):
        BM25Retriever([]).save(directory)
    assert (directory / "metadata.json").read_bytes() == content
    with pytest.raises(ValueError, match="new or empty"):
        BM25Retriever([]).save(directory / "metadata.json")


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("format_version", 2),
        ("format_version", True),
        ("index_type", "BM25Plus"),
        ("tokenization", "lowercase"),
        ("token_pattern", "[a-z]+"),
        ("k1", 2.0),
        ("b", 1.0),
        ("epsilon", 0.0),
        ("rank_bm25_version", "incompatible"),
        ("papers", None),
    ],
)
def test_bm25_load_rejects_incompatible_metadata(
    section_passages, tmp_path, key, value
):
    BM25Retriever(section_passages).save(tmp_path)
    path = tmp_path / "metadata.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    metadata[key] = value
    path.write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError, match=key):
        BM25Retriever.load(tmp_path)


@pytest.mark.parametrize(
    "corruption",
    [
        "duplicate_paper",
        "duplicate_passage",
        "wrong_paper",
        "unordered_rows",
        "empty_mapping",
        "missing_field",
        "extra_field",
        "invalid_paper_id",
        "not_object",
    ],
)
def test_bm25_load_rejects_invalid_passage_mapping(
    section_passages, tmp_path, corruption
):
    BM25Retriever(section_passages).save(tmp_path)
    path = tmp_path / "metadata.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    paper = metadata["papers"][0]
    if corruption == "duplicate_paper":
        metadata["papers"].append(paper)
    elif corruption == "duplicate_passage":
        paper["passages"].append(paper["passages"][0])
    elif corruption == "wrong_paper":
        paper["passages"][0]["paper_id"] = "another-paper"
    elif corruption == "unordered_rows":
        paper["passages"].reverse()
    elif corruption == "empty_mapping":
        paper["passages"] = []
    elif corruption == "missing_field":
        del paper["passages"][0]["text"]
    elif corruption == "extra_field":
        paper["passages"][0]["score"] = 1.0
    elif corruption == "invalid_paper_id":
        paper["paper_id"] = " "
    else:
        metadata = []
    path.write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError):
        BM25Retriever.load(tmp_path)


def test_dense_saved_embeddings_reused_for_section_and_rewritten_queries(
    section_passages, tmp_path
):
    original = DenseRetriever(section_passages, encoder=SectionEncoder())
    original.save(tmp_path)
    encoder = SectionEncoder()
    loaded = DenseRetriever.load(tmp_path, encoder=encoder)
    assert encoder.calls == []
    for query in ("beta", "gamma"):
        restored = loaded.retrieve(query, "paper-a", 2, section="Methods")
        expected = original.retrieve(query, "paper-a", 2, section="Methods")
        assert [hit.passage for hit in restored] == [hit.passage for hit in expected]
        assert [hit.rank for hit in restored] == [hit.rank for hit in expected]
        assert [hit.score for hit in restored] == pytest.approx(
            [hit.score for hit in expected]
        )
    assert encoder.calls == [
        [QUERY_INSTRUCTION + "beta"],
        [QUERY_INSTRUCTION + "gamma"],
    ]


def test_existing_hybrid_accepts_section_bound_callbacks_and_candidate_limit(
    section_passages,
):
    sparse = BM25Retriever(section_passages)
    dense = DenseRetriever(section_passages, encoder=SectionEncoder())
    hybrid = HybridRetriever(
        partial(sparse.retrieve, section="Methods"),
        partial(dense.retrieve, section="Methods"),
        candidate_k=2,
    )
    # There are three eligible passages, while P2 requests two per backend.
    assert len(sparse.retrieve("alpha", "paper-a", 20, section="Methods")) == 3
    assert len(dense.retrieve("alpha", "paper-a", 20, section="Methods")) == 3
    single = hybrid.retrieve("alpha", "paper-a", top_k=1)
    expanded = hybrid.retrieve("alpha", "paper-a", top_k=20)
    assert len(single) == 1
    assert single == expanded[:1]
    assert [hit.passage.passage_id for hit in expanded] == [
        "a-method-a",
        "a-method-b",
    ]
    assert [hit.rank for hit in expanded] == [1, 2]
    for hit in expanded:
        assert hit.passage.paper_id == "paper-a"
        assert hit.passage.section == "Methods"
        assert set(hit.source_scores) == {"bm25", "dense"}
        assert hit.source_scores["bm25"].rank == hit.rank
        assert hit.source_scores["dense"].rank == hit.rank


def test_section_bound_hybrids_keep_interleaved_calls_independent(section_passages):
    sparse = BM25Retriever(section_passages)
    dense = DenseRetriever(section_passages, encoder=SectionEncoder())
    # Each callback fixes its own keyword; all hybrids share the same indexes.
    hybrids = {
        section: HybridRetriever(
            partial(sparse.retrieve, section=section),
            partial(dense.retrieve, section=section),
            candidate_k=6,
        )
        for section in ("Methods", "Results", None, "unknown")
    }
    original = hybrids["Methods"].retrieve("beta", "paper-a", top_k=3)
    assert [hit.passage.passage_id for hit in original] == [
        "a-method-a",
        "a-method-b",
        "a-method-c",
    ]
    results = hybrids["Results"].retrieve("alpha", "paper-a", top_k=3)
    assert [hit.passage.passage_id for hit in results] == ["a-results"]
    other_paper = hybrids["Methods"].retrieve("alpha", "paper-b", top_k=3)
    assert [hit.passage.passage_id for hit in other_paper] == ["b-method"]
    rewritten = hybrids["Methods"].retrieve("gamma", "paper-a", top_k=1)
    assert rewritten[0].passage.passage_id == "a-method-c"
    assert hybrids["Results"].retrieve("gamma", "paper-b", top_k=3) == []
    unfiltered = hybrids[None].retrieve("alpha", "paper-a", top_k=1)
    assert unfiltered[0].passage.passage_id == "a-results"
    default_hybrid = HybridRetriever(sparse.retrieve, dense.retrieve, candidate_k=6)
    assert unfiltered == default_hybrid.retrieve("alpha", "paper-a", top_k=1)
    assert hybrids["unknown"].retrieve("beta", "paper-a", top_k=3) == []
    assert hybrids["Methods"].retrieve("gamma", "absent", top_k=3) == []
    assert hybrids["Methods"].retrieve("beta", "paper-a", top_k=3) == original
    assert hybrids["Results"].retrieve("alpha", "paper-a", top_k=3) == results
