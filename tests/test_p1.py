"""P1 retrieval contracts using synthetic passages and offline encoders."""

import json
import math
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import faiss
import numpy as np
import pytest

from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import (
    DEFAULT_MODEL_NAME,
    QUERY_INSTRUCTION,
    DenseRetriever,
)
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


class DenseFakeEncoder:
    """Controlled, unnormalized vectors; only FAISS performs the search."""

    model_name = "test/deterministic"
    revision = "v1"

    def __init__(self, passages):
        ir_vectors = ([0, 7, 0], [-2, 0, 0], [3, 4, 0], [-3, 4, 0])
        self.vectors = {
            passage.text: (
                ir_vectors[index] if index < 4 else [8, 0, 0]
            )
            for index, passage in enumerate(passages)
        }
        self.vectors[QUERY_INSTRUCTION + "dense ranking"] = [5, 0, 0]
        self.calls = []

    def encode(self, texts):
        self.calls.append(list(texts))
        return np.asarray([self.vectors[text] for text in texts], dtype=np.float32)


class DenseMatrixEncoder:
    """Return an explicit matrix to exercise malformed embedding handling."""

    model_name = "test/deterministic"
    revision = "v1"

    def __init__(self, matrix):
        self.matrix = matrix

    def encode(self, texts):
        return np.asarray(self.matrix)


@pytest.fixture
def dense_encoder(passages):
    return DenseFakeEncoder(passages)


@pytest.fixture
def dense_retriever(passages, dense_encoder):
    return DenseRetriever(passages, encoder=dense_encoder)


def test_dense_normal_top_k_has_expected_cosine_order(dense_retriever):
    results = dense_retriever.retrieve("dense ranking", "synthetic-ir", 2)
    assert isinstance(results, list)
    assert all(isinstance(hit, RetrievalHit) for hit in results)
    assert [hit.passage.passage_id for hit in results] == [
        "synthetic-ir-003",
        "synthetic-ir-001",
    ]
    # Both query and passage vectors have non-unit length before encoding.
    assert [hit.score for hit in results] == pytest.approx([0.6, 0.0], abs=1e-6)


def test_dense_top_k_larger_than_paper_returns_available(dense_retriever):
    results = dense_retriever.retrieve("dense ranking", "synthetic-ir", 20)
    assert len(results) == 4
    assert [hit.passage.passage_id for hit in results] == [
        "synthetic-ir-003",
        "synthetic-ir-001",
        "synthetic-ir-004",
        "synthetic-ir-002",
    ]
    assert [hit.score for hit in results] == pytest.approx(
        [0.6, 0.0, -0.6, -1.0], abs=1e-6
    )


def test_dense_paper_top_k_survives_higher_scores_in_other_paper(
    dense_retriever,
):
    other = dense_retriever.retrieve("dense ranking", "synthetic-energy", 4)
    selected = dense_retriever.retrieve("dense ranking", "synthetic-ir", 2)
    assert all(hit.score > selected[0].score for hit in other)
    assert [hit.passage.passage_id for hit in selected] == [
        "synthetic-ir-003",
        "synthetic-ir-001",
    ]
    assert all(hit.passage.paper_id == "synthetic-ir" for hit in selected)
    assert all(hit.passage.paper_id == "synthetic-energy" for hit in other)


def test_dense_paper_results_match_isolated_index(
    passages, dense_encoder, dense_retriever
):
    isolated = DenseRetriever(passages[:4], encoder=dense_encoder)
    expected = isolated.retrieve("dense ranking", "synthetic-ir", 4)
    actual = dense_retriever.retrieve("dense ranking", "synthetic-ir", 4)
    assert [hit.passage for hit in actual] == [hit.passage for hit in expected]
    assert [hit.score for hit in actual] == pytest.approx(
        [hit.score for hit in expected], abs=1e-6
    )


def test_dense_unknown_paper_does_not_encode_query(dense_retriever, dense_encoder):
    previous_calls = list(dense_encoder.calls)
    assert dense_retriever.retrieve("dense ranking", "unknown-paper", 3) == []
    assert dense_encoder.calls == previous_calls


def test_dense_empty_corpus_does_not_encode(dense_encoder, tmp_path):
    empty = DenseRetriever([], encoder=dense_encoder)
    assert empty.retrieve("dense ranking", "synthetic-ir", 2) == []
    assert dense_encoder.calls == []
    empty.save(tmp_path / "empty")
    restored = DenseRetriever.load(tmp_path / "empty", encoder=dense_encoder)
    assert restored.retrieve("dense ranking", "synthetic-ir", 2) == []
    assert dense_encoder.calls == []


@pytest.mark.parametrize("query", ["", " ", "\t\n", None, 123])
def test_dense_invalid_query_raises_value_error(dense_retriever, query):
    with pytest.raises(ValueError):
        dense_retriever.retrieve(query, "synthetic-ir", 2)


@pytest.mark.parametrize("paper_id", ["", " ", "\t\n", None, 123])
def test_dense_invalid_paper_id_raises_value_error(dense_retriever, paper_id):
    with pytest.raises(ValueError):
        dense_retriever.retrieve("dense ranking", paper_id, 2)


@pytest.mark.parametrize("top_k", [0, -1, -10, True, False, 1.5, "2", None])
def test_dense_invalid_top_k_raises_value_error(dense_retriever, top_k):
    with pytest.raises(ValueError):
        dense_retriever.retrieve("dense ranking", "synthetic-ir", top_k)


def test_dense_preserves_ids_fields_and_source_passages(passages, dense_retriever):
    before = [passage.model_dump() for passage in passages]
    originals = {passage.passage_id: passage for passage in passages}
    results = dense_retriever.retrieve("dense ranking", "synthetic-ir", 4)
    assert {hit.passage.passage_id for hit in results} == {
        passage.passage_id for passage in passages[:4]
    }
    for hit in results:
        assert hit.passage.model_dump() == originals[hit.passage.passage_id].model_dump()
    assert [passage.model_dump() for passage in passages] == before
    assert dense_retriever.retrieve("dense ranking", "synthetic-ir", 4) == results


def test_dense_ranks_scores_and_unique_results(dense_retriever):
    results = dense_retriever.retrieve("dense ranking", "synthetic-ir", 20)
    scores = [hit.score for hit in results]
    ids = [hit.passage.passage_id for hit in results]
    assert [hit.rank for hit in results] == [1, 2, 3, 4]
    assert len(ids) == len(set(ids)) == 4
    assert all(isinstance(score, float) and math.isfinite(score) for score in scores)
    assert scores == sorted(scores, reverse=True)
    assert all(-1.000001 <= score <= 1.000001 for score in scores)


def test_dense_boundary_ties_are_deterministic_across_input_order(
    passages, dense_encoder
):
    for passage in passages[:4]:
        dense_encoder.vectors[passage.text] = [7, 0, 0]
    forward = DenseRetriever(passages, encoder=dense_encoder)
    reverse = DenseRetriever(reversed(passages), encoder=dense_encoder)
    expected = forward.retrieve("dense ranking", "synthetic-ir", 2)
    assert [hit.passage.passage_id for hit in expected] == [
        "synthetic-ir-001",
        "synthetic-ir-002",
    ]
    assert [hit.rank for hit in expected] == [1, 2]
    assert [hit.score for hit in expected] == pytest.approx([1.0, 1.0])
    assert reverse.retrieve("dense ranking", "synthetic-ir", 2) == expected
    assert forward.retrieve("dense ranking", "synthetic-ir", 2) == expected


def test_dense_opaque_ids_and_mixed_input_order_keep_correct_mapping(
    passages, dense_encoder
):
    # These IDs deliberately provide no paper or position information.
    ids = ["opaque-z", "opaque-b", "opaque-q", "opaque-a"]
    changed = [
        passage.model_copy(update={"passage_id": opaque_id})
        for passage, opaque_id in zip(passages[:4], ids)
    ]
    mixed = [passages[5], changed[2], changed[0], passages[4], changed[3], changed[1]]
    retriever = DenseRetriever(mixed, encoder=dense_encoder)
    results = retriever.retrieve("dense ranking", "synthetic-ir", 4)
    assert [hit.passage.passage_id for hit in results] == [
        "opaque-q", "opaque-z", "opaque-a", "opaque-b"
    ]
    originals = {passage.passage_id: passage for passage in mixed}
    assert all(hit.passage == originals[hit.passage.passage_id] for hit in results)
    assert all(hit.passage.paper_id == "synthetic-ir" for hit in results)


@pytest.mark.parametrize("conflicting", [False, True])
def test_dense_rejects_duplicate_input_ids(passages, dense_encoder, conflicting):
    duplicate = passages[0]
    if conflicting:
        duplicate = duplicate.model_copy(
            update={"paper_id": "another-paper", "text": "Conflicting content"}
        )
    with pytest.raises(ValueError):
        DenseRetriever([*passages, duplicate], encoder=dense_encoder)


def test_dense_encodes_raw_passages_and_only_instructs_queries(
    passages, dense_encoder, dense_retriever
):
    encoded_passages = [text for call in dense_encoder.calls for text in call]
    assert Counter(encoded_passages) == Counter(passage.text for passage in passages)
    assert QUERY_INSTRUCTION == "Represent this sentence for searching relevant passages: "
    dense_retriever.retrieve("dense ranking", "synthetic-ir", 2)
    assert dense_encoder.calls[-1] == [QUERY_INSTRUCTION + "dense ranking"]


@pytest.mark.parametrize(
    "matrix",
    [
        [[1, 0, 0]],
        [[1, 0, 0]] * 3,
        [1, 0, 0],
        [[[1, 0, 0]], [[0, 1, 0]]],
        [[], []],
        [[float("nan"), 0, 0], [0, 1, 0]],
        [[float("inf"), 0, 0], [0, 1, 0]],
        [[0, 0, 0], [0, 1, 0]],
        [["invalid", 0, 0], [0, 1, 0]],
    ],
    ids=["too-few", "too-many", "flat", "3d", "empty-dimension", "nan", "inf", "zero", "text"],
)
def test_dense_rejects_invalid_passage_embeddings(passages, matrix):
    with pytest.raises(ValueError):
        DenseRetriever(passages[:2], encoder=DenseMatrixEncoder(matrix))


@pytest.mark.parametrize(
    "matrix",
    [
        [[1, 0]],
        [[1, 0, 0], [0, 1, 0]],
        [1, 0, 0],
        [[float("nan"), 0, 0]],
        [[float("inf"), 0, 0]],
        [[0, 0, 0]],
    ],
    ids=["wrong-dimension", "wrong-count", "flat", "nan", "inf", "zero"],
)
def test_dense_rejects_invalid_query_embeddings(passages, matrix):
    encoder = DenseMatrixEncoder([[1, 0, 0], [0, 1, 0]])
    retriever = DenseRetriever(passages[:2], encoder=encoder)
    encoder.matrix = matrix
    with pytest.raises(ValueError):
        retriever.retrieve("dense ranking", "synthetic-ir", 2)


def test_dense_save_writes_real_normalized_faiss_indexes_and_metadata(
    tmp_path, passages, dense_retriever
):
    directory = tmp_path / "index"
    dense_retriever.save(directory)
    metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["format_version"] == 1
    assert metadata["model_name"] == "test/deterministic"
    assert metadata["revision"] == "v1"
    assert metadata["encoder_kind"] == "injected"
    assert metadata["query_instruction"] == QUERY_INSTRUCTION
    assert metadata["embedding_dimension"] == 3
    assert metadata["normalization"] == "l2"
    assert metadata["similarity_metric"] == "cosine"
    assert metadata["index_type"] == "IndexFlatIP"
    assert metadata["max_seq_length"] == 512
    assert len(metadata["papers"]) == 2
    originals = {passage.passage_id: passage for passage in passages}
    for number, paper in enumerate(metadata["papers"]):
        index = faiss.read_index(str(directory / f"paper-{number:06d}.faiss"))
        assert isinstance(index, faiss.IndexFlatIP)
        assert index.d == 3
        assert index.ntotal == len(paper["passages"]) == 4
        vectors = index.reconstruct_n(0, index.ntotal)
        assert np.linalg.norm(vectors, axis=1) == pytest.approx(np.ones(4), abs=1e-6)
        for raw in paper["passages"]:
            assert raw == originals[raw["passage_id"]].model_dump()
            assert raw["paper_id"] == paper["paper_id"]


def test_dense_reload_preserves_results_without_reencoding_passages(
    tmp_path, passages, dense_retriever
):
    before = {
        paper_id: dense_retriever.retrieve("dense ranking", paper_id, 4)
        for paper_id in ("synthetic-ir", "synthetic-energy")
    }
    directory = tmp_path / "index"
    dense_retriever.save(directory)
    encoder = DenseFakeEncoder(passages)
    # Any attempt to encode a passage during loading or querying now fails.
    encoder.vectors = {QUERY_INSTRUCTION + "dense ranking": [5, 0, 0]}
    restored = DenseRetriever.load(directory, encoder=encoder)
    assert encoder.calls == []
    for paper_id, expected in before.items():
        actual = restored.retrieve("dense ranking", paper_id, 4)
        assert [hit.passage.model_dump() for hit in actual] == [
            hit.passage.model_dump() for hit in expected
        ]
        assert [hit.rank for hit in actual] == [hit.rank for hit in expected]
        assert [hit.score for hit in actual] == pytest.approx(
            [hit.score for hit in expected], abs=1e-6
        )
    assert encoder.calls == [[QUERY_INSTRUCTION + "dense ranking"]] * 2


@pytest.mark.parametrize(("attribute", "value"), [("model_name", "test/other"), ("revision", "v2")])
def test_dense_reload_rejects_different_encoder_identity(
    tmp_path, dense_encoder, dense_retriever, attribute, value
):
    dense_retriever.save(tmp_path)
    setattr(dense_encoder, attribute, value)
    with pytest.raises(ValueError):
        DenseRetriever.load(tmp_path, encoder=dense_encoder)


def test_dense_injected_index_cannot_load_without_explicit_encoder(
    tmp_path, dense_retriever
):
    dense_retriever.save(tmp_path)
    with pytest.raises(ValueError):
        DenseRetriever.load(tmp_path)


@pytest.mark.parametrize(
    "expected",
    [{"model_name": "test/other"}, {"revision": "v2"}, {"query_instruction": ""}],
)
def test_dense_reload_rejects_incompatible_requested_metadata(
    tmp_path, dense_encoder, dense_retriever, expected
):
    dense_retriever.save(tmp_path)
    with pytest.raises(ValueError):
        DenseRetriever.load(tmp_path, encoder=dense_encoder, **expected)


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("format_version", 99),
        ("model_name", "test/other"),
        ("revision", "v2"),
        ("encoder_kind", "unknown"),
        ("query_instruction", "wrong instruction"),
        ("embedding_dimension", 4),
        ("normalization", "none"),
        ("similarity_metric", "euclidean"),
        ("index_type", "IndexFlatL2"),
        ("max_seq_length", 1024),
    ],
)
def test_dense_reload_rejects_inconsistent_metadata(
    tmp_path, dense_encoder, dense_retriever, key, value
):
    dense_retriever.save(tmp_path)
    path = tmp_path / "metadata.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    metadata[key] = value
    path.write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError):
        DenseRetriever.load(tmp_path, encoder=dense_encoder)


@pytest.mark.parametrize("corruption", ["missing-row", "wrong-paper", "duplicate-id", "checksum"])
def test_dense_reload_rejects_invalid_row_mapping(
    tmp_path, dense_encoder, dense_retriever, corruption
):
    dense_retriever.save(tmp_path)
    path = tmp_path / "metadata.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    paper = metadata["papers"][0]
    if corruption == "missing-row":
        paper["passages"].pop()
    elif corruption == "wrong-paper":
        paper["passages"][0]["paper_id"] = "other-paper"
    elif corruption == "duplicate-id":
        paper["passages"][1]["passage_id"] = paper["passages"][0]["passage_id"]
    else:
        paper["index_sha256"] = "0" * 64
    path.write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError):
        DenseRetriever.load(tmp_path, encoder=dense_encoder)


def test_dense_callback_integrates_with_existing_hybrid(dense_retriever):
    hybrid = HybridRetriever(lambda *args: [], dense_retriever.retrieve, candidate_k=4)
    results = hybrid.retrieve("dense ranking", "synthetic-ir", 2)
    dense = dense_retriever.retrieve("dense ranking", "synthetic-ir", 2)
    assert all(isinstance(hit, RetrievedPassage) for hit in results)
    assert [hit.passage for hit in results] == [hit.passage for hit in dense]
    assert [hit.rank for hit in results] == [1, 2]
    for fused, original in zip(results, dense):
        assert set(fused.source_scores) == {"dense"}
        assert fused.source_scores["dense"].rank == original.rank
        assert fused.source_scores["dense"].score == original.score


def test_dense_and_bm25_share_passages_in_existing_hybrid(retriever, dense_retriever):
    hybrid = HybridRetriever(retriever.retrieve, dense_retriever.retrieve, candidate_k=4)
    results = hybrid.retrieve("dense ranking", "synthetic-ir", 4)
    assert len(results) == 4
    assert len({hit.passage.passage_id for hit in results}) == 4
    assert all(set(hit.source_scores) == {"bm25", "dense"} for hit in results)
    assert all(hit.passage.paper_id == "synthetic-ir" for hit in results)


def test_dense_default_sentence_transformer_wiring_and_reload(
    monkeypatch, tmp_path, passages, dense_encoder
):
    import sentence_transformers

    constructors = []
    encoding_calls = []
    models = []
    resolved_revision = "a" * 40

    class RecordingSentenceTransformer:
        def __init__(self, model_name, **kwargs):
            constructors.append((model_name, kwargs))
            self.model_card_data = SimpleNamespace(base_model_revision="main")
            self.max_seq_length = 1024
            models.append(self)

        def __getitem__(self, index):
            assert index == 0
            return SimpleNamespace(
                auto_model=SimpleNamespace(
                    config=SimpleNamespace(_commit_hash=resolved_revision)
                )
            )

        def encode(self, texts, **kwargs):
            encoding_calls.append((list(texts), kwargs))
            return dense_encoder.encode(texts)

    monkeypatch.setattr(
        sentence_transformers, "SentenceTransformer", RecordingSentenceTransformer
    )
    cache = tmp_path / "model-cache"
    retriever = DenseRetriever(
        passages,
        device="cpu",
        batch_size=2,
        cache_folder=cache,
        local_files_only=True,
    )
    expected = retriever.retrieve("dense ranking", "synthetic-ir", 4)
    assert constructors == [
        (
            "BAAI/bge-small-en-v1.5",
            {
                "revision": None,
                "device": "cpu",
                "cache_folder": str(cache),
                "local_files_only": True,
            },
        )
    ]
    assert DEFAULT_MODEL_NAME == "BAAI/bge-small-en-v1.5"
    assert models[0].max_seq_length == 512
    for _, kwargs in encoding_calls:
        assert kwargs == {
            "batch_size": 2,
            "convert_to_numpy": True,
            "normalize_embeddings": False,
            "show_progress_bar": False,
            "prompt": "",
        }
    directory = tmp_path / "index"
    retriever.save(directory)
    metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["encoder_kind"] == "sentence_transformer"
    assert metadata["model_name"] == DEFAULT_MODEL_NAME
    assert metadata["revision"] == resolved_revision
    encoding_calls.clear()
    restored = DenseRetriever.load(
        directory, cache_folder=cache, local_files_only=True, batch_size=2
    )
    assert len(constructors) == 1
    assert encoding_calls == []
    actual = restored.retrieve("dense ranking", "synthetic-ir", 4)
    assert actual == expected
    assert len(constructors) == 2
    assert constructors[1][1]["revision"] == resolved_revision
    assert [texts for texts, _ in encoding_calls] == [
        [QUERY_INSTRUCTION + "dense ranking"]
    ]


def test_dense_empty_default_path_never_loads_model(monkeypatch, tmp_path):
    import sentence_transformers

    def unexpected_model_load(*args, **kwargs):
        pytest.fail("An empty corpus must not load a SentenceTransformer model")

    monkeypatch.setattr(
        sentence_transformers, "SentenceTransformer", unexpected_model_load
    )
    empty = DenseRetriever([])
    assert empty.retrieve("dense ranking", "missing-paper", 1) == []
    empty.save(tmp_path)
    restored = DenseRetriever.load(tmp_path)
    assert restored.retrieve("dense ranking", "missing-paper", 1) == []


def test_dense_rejects_loaded_model_revision_drift(monkeypatch, passages):
    import sentence_transformers

    class WrongRevisionSentenceTransformer:
        model_card_data = SimpleNamespace(base_model_revision="main")

        def __init__(self, *args, **kwargs):
            pass

        def __getitem__(self, index):
            assert index == 0
            return SimpleNamespace(
                auto_model=SimpleNamespace(
                    config=SimpleNamespace(_commit_hash="b" * 40)
                )
            )

    monkeypatch.setattr(
        sentence_transformers, "SentenceTransformer", WrongRevisionSentenceTransformer
    )
    with pytest.raises(ValueError):
        DenseRetriever(passages, revision="a" * 40, local_files_only=True)
