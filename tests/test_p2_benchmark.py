"""Verify development-query boundaries and paired comparison behavior."""

import json
from argparse import Namespace
from pathlib import Path

import pytest

from scripts.benchmark_p2 import (
    compare_queries,
    run_benchmark,
    select_queries,
    summarize,
)
from src.retrieval.schemas import RetrievalHit


def test_query_selection_is_train_only_deterministic_and_projects_no_labels(tmp_path):
    path = tmp_path / "qa.jsonl"
    rows = [
        {"source_split": "test", "paper_id": "a", "question": None},
        {"source_split": "validation", "paper_id": "a", "question": None},
        {"source_split": "train", "paper_id": "small", "question": None},
        {
            "source_split": "train",
            "paper_id": "b",
            "question_id": "q3",
            "question": "Third?",
            "answers": ["secret"],
        },
        {
            "source_split": "train",
            "paper_id": "a",
            "question_id": "q2",
            "question": "Second?",
            "answers": ["secret"],
        },
        {
            "source_split": "train",
            "paper_id": "a",
            "question_id": "q1",
            "question": "First?",
            "answers": ["secret"],
        },
    ]
    path.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    actual = select_queries(path, {"a": 20, "b": 30, "small": 1}, 2, 20)
    assert actual == [
        {"paper_id": "a", "question_id": "q1", "question": "First?"},
        {"paper_id": "b", "question_id": "q3", "question": "Third?"},
    ]
    with pytest.raises(ValueError, match="Only 2"):
        select_queries(path, {"a": 20, "b": 30}, 3, 20)


def test_comparison_pairs_methods_on_same_questions_and_scores_full_union():
    data = json.loads(
        (Path(__file__).parent / "fixtures/mock_retrieval_results.json").read_text()
    )
    calls = []

    def source(name):
        def retrieve(query, paper_id, top_k):
            return [RetrievalHit.model_validate(hit) for hit in data[name]][:top_k]

        return retrieve

    class Scorer:
        def score(self, query, texts):
            calls.append(len(texts))
            return list(range(len(texts)))

    query = {
        "question_id": "q1",
        "paper_id": data["paper_id"],
        "question": data["query"],
    }
    records = compare_queries(
        source("bm25"), source("dense"), Scorer(), [query], [2, 3], 1, 60
    )
    assert len(records) == 2
    for row in records:
        assert row["question_id"] == "q1"
        assert set(row["results"]) == {"rrf", "rrf_bge"}
        assert len(row["results"]["rrf"]) == len(row["results"]["rrf_bge"]) == 1
        assert row["results"]["rrf"][0]["reranker_score"] is None
        assert row["results"]["rrf_bge"][0]["reranker_score"] is not None
        assert all(value >= 0 for value in row["latency_ms"].values())
    assert (
        calls
        == [records[0]["unique_candidates"]] * 2 + [records[1]["unique_candidates"]] * 2
    )
    summaries = summarize(records, [2, 3])
    assert [row["questions"] for row in summaries] == [1, 1]
    assert [row["candidate_k_per_source"] for row in summaries] == [2, 3]


def test_existing_benchmark_output_is_preserved(tmp_path):
    output = tmp_path / "result.json"
    output.write_text("previous run", encoding="utf-8")
    with pytest.raises(FileExistsError):
        run_benchmark(Namespace(output=output))
    assert output.read_text() == "previous run"
