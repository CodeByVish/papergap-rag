import json

import pytest

from scripts import batch_hybrid

pytest_plugins = ["tests.test_hybrid_cli"]


def questions(tmp_path):
    path = tmp_path / "questions.jsonl"
    path.write_text(
        "\n".join(
            json.dumps(
                {"question_id": str(i), "question": "lexical", "paper_id": paper}
            )
            for i, paper in enumerate(["synthetic-ir", "unknown", "synthetic-ir"])
        )
    )
    return path


def test_batch_reranks_union_preserves_order_and_empty(inputs, tmp_path, monkeypatch):
    corpus, directory = inputs
    calls = []

    class Scorer:
        def score(self, query, texts):
            calls.append(len(texts))
            return list(range(len(texts)))

    monkeypatch.setattr(batch_hybrid, "BGEReranker", lambda **kwargs: Scorer())
    output = tmp_path / "output"
    manifest = batch_hybrid.run_batch(
        questions=questions(tmp_path),
        passages=corpus,
        dense_index_dir=directory,
        output_dir=output,
        bge=True,
        top_k=1,
        candidate_k=4,
    )
    rows = [
        json.loads(line)
        for line in (output / "retrieval.jsonl").read_text().splitlines()
    ]
    assert [r["question_id"] for r in rows] == ["0", "1", "2"]
    assert rows[1]["retrieved_passages"] == []
    assert calls == [4, 4]
    assert rows[0]["retrieved_passages"][0]["reranker_score"] == 3.0
    assert manifest["status"] == "complete"
    assert manifest["empty_results"] == 1
    with pytest.raises(FileExistsError):
        batch_hybrid.run_batch(
            questions=questions(tmp_path),
            passages=corpus,
            dense_index_dir=directory,
            output_dir=output,
        )


def test_duplicate_questions_rejected_before_output(inputs, tmp_path):
    corpus, directory = inputs
    path = questions(tmp_path)
    path.write_text(path.read_text() + "\n" + path.read_text().splitlines()[0])
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="Duplicate"):
        batch_hybrid.run_batch(
            questions=path,
            passages=corpus,
            dense_index_dir=directory,
            output_dir=output,
        )
    assert not output.exists()


def test_failure_is_not_an_empty_result(inputs, tmp_path, monkeypatch):
    corpus, directory = inputs

    class Scorer:
        def score(self, query, texts):
            raise RuntimeError("model failed")

    monkeypatch.setattr(batch_hybrid, "BGEReranker", lambda **kwargs: Scorer())
    output = tmp_path / "output"
    with pytest.raises(RuntimeError, match="model failed"):
        batch_hybrid.run_batch(
            questions=questions(tmp_path),
            passages=corpus,
            dense_index_dir=directory,
            output_dir=output,
            bge=True,
        )
    assert json.loads((output / "run_manifest.json").read_text())["status"] == "failed"
    assert (output / "retrieval.jsonl").read_text() == ""
