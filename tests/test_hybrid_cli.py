"""Exercise the real FAISS/BM25/fusion path without downloading weights."""

import json

import numpy as np
import pytest

from scripts import demo_hybrid
from scripts.build_indexes import load_passages
from src.retrieval.dense_retriever import DenseRetriever


class Encoder:
    model_name = "test-hybrid"
    revision = "test-v1"

    def encode(self, texts):
        return np.array([[1.0, float("lexical" in text.lower())] for text in texts])


@pytest.fixture
def inputs(tmp_path, monkeypatch):
    from pathlib import Path

    source = Path(__file__).parent / "fixtures/mock_passages.jsonl"
    passages = load_passages(source)
    corpus = tmp_path / "passages.jsonl"
    corpus.write_text(
        "\n".join(p.model_dump_json() for p in passages), encoding="utf-8"
    )
    directory = tmp_path / "dense"
    encoder = Encoder()
    DenseRetriever(passages, encoder=encoder).save(directory)
    original_load = DenseRetriever.load
    monkeypatch.setattr(
        demo_hybrid.DenseRetriever,
        "load",
        lambda directory, **kwargs: original_load(directory, encoder=encoder),
    )
    return corpus, directory


def test_hybrid_uses_saved_index_and_preserves_source_provenance(inputs):
    corpus, directory = inputs
    result = demo_hybrid.run_hybrid(
        corpus, directory, "lexical", "synthetic-ir", top_k=2, candidate_k=3
    )
    assert result["candidate_counts"] == {"bm25": 3, "dense": 3}
    assert 3 <= result["unique_candidates"] <= 4
    assert result["retrieval_ms"] >= 0
    assert len(result["results"]) == 2
    for rank, hit in enumerate(result["results"], 1):
        assert hit["rank"] == rank
        assert hit["passage"]["paper_id"] == "synthetic-ir"
        assert hit["source_scores"]
        assert hit["reranker_score"] is None


def test_hybrid_refuses_corpus_different_from_dense_mapping(inputs):
    corpus, directory = inputs
    records = [json.loads(line) for line in corpus.read_text().splitlines()]
    records[0]["text"] = "Changed after indexing."
    corpus.write_text("\n".join(json.dumps(p) for p in records), encoding="utf-8")
    with pytest.raises(ValueError, match="do not match"):
        demo_hybrid.run_hybrid(corpus, directory, "lexical", "synthetic-ir")


def test_hybrid_reranks_all_fused_candidates_and_handles_unknown_paper(
    inputs, monkeypatch
):
    calls = []

    class Scorer:
        def score(self, query, texts):
            calls.append(len(texts))
            return list(range(len(texts)))

    monkeypatch.setattr(demo_hybrid, "BGEReranker", lambda **kwargs: Scorer())
    corpus, directory = inputs
    result = demo_hybrid.run_hybrid(
        corpus, directory, "lexical", "synthetic-ir", top_k=1, candidate_k=4, bge=True
    )
    assert calls == [4, 4]  # warm-up and measured call both score the full union
    assert result["results"][0]["reranker_score"] == 3.0
    empty = demo_hybrid.run_hybrid(corpus, directory, "lexical", "unknown", bge=True)
    assert empty["results"] == []
    assert empty["unique_candidates"] == 0
    assert calls == [4, 4]


def test_bge_forwards_cache_and_offline_policy_to_both_loaders(monkeypatch):
    import torch
    import transformers

    from src.retrieval.reranker import BGEReranker

    calls = []

    class Tokenizer:
        def __call__(self, pairs, **kwargs):
            return {"input_ids": torch.ones((len(pairs), 2), dtype=torch.long)}

    class Model:
        def to(self, device):
            return self

        def eval(self):
            return self

        def __call__(self, input_ids):
            from types import SimpleNamespace

            return SimpleNamespace(logits=torch.ones((len(input_ids), 1)))

    def loader(kind, result):
        def load(name, **kwargs):
            calls.append((kind, name, kwargs))
            return result

        return load

    monkeypatch.setattr(
        transformers.AutoTokenizer, "from_pretrained", loader("tokenizer", Tokenizer())
    )
    monkeypatch.setattr(
        transformers.AutoModelForSequenceClassification,
        "from_pretrained",
        loader("model", Model()),
    )
    scorer = BGEReranker(
        revision="a" * 40, cache_folder="local-cache", local_files_only=True
    )
    assert scorer.score("question", ["first", "second"]) == [1.0, 1.0]
    assert scorer.score("question", ["third"]) == [1.0]
    assert [call[0] for call in calls] == ["tokenizer", "model"]
    assert all(
        call[2]
        == {"revision": "a" * 40, "cache_dir": "local-cache", "local_files_only": True}
        for call in calls
    )
