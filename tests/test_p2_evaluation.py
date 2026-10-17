import json
from argparse import Namespace
from pathlib import Path

import pytest

from scripts import retrieval_ablation
from scripts.build_indexes import load_passages
from src.evaluation.pooling import pool_candidates
from src.evaluation.retrieval import binary_metrics, evaluate_rankings
from src.retrieval.bm25_retriever import BM25Retriever

pytest_plugins = ["tests.test_hybrid_cli"]


def fixture_data():
    corpus = load_passages(Path("tests/fixtures/mock_passages.jsonl"))
    paper = corpus[0].paper_id
    hits = BM25Retriever(corpus).retrieve("lexical", paper, 4)
    q = {"question_id": "q1", "paper_id": paper, "question": "lexical"}
    row = {
        **q,
        "retrieval_round": 1,
        "retrieved_passages": [h.model_dump(mode="json") for h in hits],
    }
    label = {
        "question_id": "q1",
        "paper_id": paper,
        "status": "mapped",
        "relevance_complete": True,
        "relevant_passage_ids": [hits[1].passage.passage_id],
        "judged_passage_ids": [h.passage.passage_id for h in hits],
    }
    return corpus, q, row, label


def test_binary_metric_arithmetic_and_zero_relevance():
    result = binary_metrics(["n", "r", "x"], {"r", "z"}, 3)
    assert result["precision_at_k"] == pytest.approx(1 / 3)
    assert result["recall_at_k"] == 0.5
    assert result["mrr_at_k"] == 0.5
    assert result["ndcg_at_k"] == pytest.approx(
        (1 / __import__("math").log2(3)) / (1 + 1 / __import__("math").log2(3))
    )
    assert binary_metrics([], set(), 5) == {
        "precision_at_k": 0,
        "recall_at_k": None,
        "mrr_at_k": 0,
        "ndcg_at_k": None,
    }


def test_unknown_judgments_suppress_metrics_and_incomplete_recall_is_named():
    corpus, q, row, label = fixture_data()
    catalog = {p.passage_id: p for p in corpus}
    label["relevance_complete"] = False
    label["judged_passage_ids"] = label["relevant_passage_ids"]
    report = evaluate_rankings({"rrf": [row]}, [q], [label], catalog, [3])
    result = report["methods"]["rrf"]["per_query"][0]
    assert result["full_ranking"] is None
    assert result["judged_coverage_at_k"] == pytest.approx(1 / 3)
    assert result["judged_only_compressed"]["mrr_at_k"] == 1
    label["judged_passage_ids"] = [
        h["passage"]["passage_id"] for h in row["retrieved_passages"]
    ]
    report = evaluate_rankings({"rrf": [row]}, [q], [label], catalog, [3])
    metrics = report["methods"]["rrf"]["per_query"][0]["full_ranking"]
    assert "recall_at_k" not in metrics and metrics["pool_recall_at_k"] == 1
    assert "pool_ndcg_at_k" in metrics


def test_pool_deduplicates_blinds_and_reports_shortfalls():
    _corpus, q, row, _label = fixture_data()
    pool = pool_candidates({"bm25": [row], "dense": [row]}, [q], per_question=10)
    assert len(pool["blinded"]) == len(row["retrieved_passages"])
    assert pool["shortfalls"][0]["available"] < 10
    assert all(
        set(r) == {"record_id", "question_id", "question", "paper_id", "passage"}
        for r in pool["blinded"]
    )
    assert all(set(r["sources"]) == {"bm25", "dense"} for r in pool["provenance"])
    assert pool == pool_candidates(
        {"dense": [row], "bm25": [row]}, [q], per_question=10
    )


def test_four_system_run_score_and_pool_cli_paths(inputs, tmp_path, monkeypatch):
    corpus, index = inputs
    q = {"question_id": "q1", "paper_id": "synthetic-ir", "question": "lexical"}
    questions = tmp_path / "questions.jsonl"
    questions.write_text(json.dumps(q) + "\n")
    qa = tmp_path / "qa.jsonl"
    qa.write_text(
        json.dumps({**q, "source_split": "train", "answers": ["never used"]}) + "\n"
    )

    class Scorer:
        def score(self, query, texts):
            return list(range(len(texts)))

    monkeypatch.setattr(retrieval_ablation, "BGEReranker", lambda **kw: Scorer())
    output = tmp_path / "run"
    args = Namespace(
        questions=questions,
        qa=qa,
        passages=corpus,
        dense_index_dir=index,
        output_dir=output,
        top_k=4,
        candidate_ks=[2, 4],
        rrf_ks=[60],
        role="development",
        freeze_manifest=None,
        cache_folder=tmp_path,
        local_files_only=False,
    )
    retrieval_ablation.run(args)
    manifest = json.loads((output / "run_manifest.json").read_text())
    assert manifest["status"] == "complete"
    assert not manifest["quality_evaluation_performed"]
    common = {"run_dir": output / "c4-r60", "passages": corpus}
    pool_args = Namespace(
        **common, per_question=10, gold=None, output_dir=tmp_path / "pool"
    )
    retrieval_ablation.pool(pool_args)
    assert (
        json.loads((pool_args.output_dir / "pool_manifest.json").read_text())["status"]
        == "shortfall"
    )
    p = load_passages(corpus)
    label = {
        "question_id": "q1",
        "paper_id": "synthetic-ir",
        "status": "mapped",
        "relevance_complete": True,
        "relevant_passage_ids": [p[0].passage_id],
    }
    labels = tmp_path / "labels.jsonl"
    labels.write_text(json.dumps(label) + "\n")
    labels_manifest = tmp_path / "labels.json"
    labels_manifest.write_text(
        json.dumps(
            {
                "labels_sha256": retrieval_ablation.sha(labels),
                "corpus_sha256": retrieval_ablation.sha(corpus),
                "source": "synthetic test only",
                "mapping": {"version": "test"},
                "annotation_coverage": "complete",
                "question_scope": {
                    "question_ids": ["q1"],
                    "project_role": "development",
                },
            }
        )
    )
    score_args = Namespace(
        **common,
        labels=labels,
        labels_manifest=labels_manifest,
        ks=[1, 3],
        output=tmp_path / "metrics.json",
    )
    retrieval_ablation.score(score_args)
    assert len(json.loads(score_args.output.read_text())["paired_contributions"]) == 3
    assert set(json.loads(score_args.output.read_text())["methods"]) == set(
        retrieval_ablation.METHODS
    )
    (output / "c4-r60/bm25.jsonl").write_text("changed")
    with pytest.raises(ValueError, match="hash"):
        retrieval_ablation.load_run(score_args)


def test_held_out_requires_matching_team_freeze(tmp_path):
    q = {"question_id": "q", "paper_id": "p", "question": "test"}
    qa = tmp_path / "qa.jsonl"
    qa.write_text(json.dumps({**q, "source_split": "test"}))
    with pytest.raises(ValueError, match="source split"):
        retrieval_ablation.validate_scope([q], qa, "development", None, qa, qa, {})
    with pytest.raises(ValueError, match="team-supplied"):
        retrieval_ablation.validate_scope([q], qa, "held_out", None, qa, qa, {})
    freeze = tmp_path / "freeze.json"
    freeze.write_text(
        json.dumps(
            {
                "status": "frozen",
                "approved_by": ["P3", "P6"],
                "questions_sha256": retrieval_ablation.sha(qa),
                "corpus_sha256": retrieval_ablation.sha(qa),
                "configuration": {},
            }
        )
    )
    retrieval_ablation.validate_scope([q], qa, "held_out", freeze, qa, qa, {})


def test_annotation_exports_are_blank_and_blind(tmp_path):
    import csv

    from scripts.prepare_p2_annotations import export_batch

    _corpus, q, row, _label = fixture_data()
    rows = pool_candidates({"bm25": [row]}, [q], per_question=2)["blinded"]
    path = tmp_path / "annotation.csv"
    export_batch(rows, path, 1, 2)
    with path.open() as source:
        exported = list(csv.DictReader(source))
    assert len(exported) == 2
    assert all(r["relevance"] == "" and r["notes"] == "" for r in exported)
    assert not any("score" in key or "source" in key for key in exported[0])


def test_final_annotation_cli_requires_frozen_pool_and_p6_assignment(
    tmp_path, monkeypatch
):
    import csv
    import hashlib
    import sys

    from scripts import prepare_p2_annotations

    source = tmp_path / "pool"
    source.mkdir()
    _corpus, q, row, _label = fixture_data()
    passage = row["retrieved_passages"][0]["passage"]
    records = [
        {
            "record_id": f"{i}-{j}",
            **q,
            "question_id": f"q{i}",
            "passage": {**passage, "passage_id": f"p{j}"},
        }
        for i in range(100)
        for j in range(10)
    ]
    blinded = source / "blinded.jsonl"
    blinded.write_text("\n".join(json.dumps(r) for r in records) + "\n")
    digest = hashlib.sha256(blinded.read_bytes()).hexdigest()
    manifest = source / "pool_manifest.json"
    manifest.write_text(
        json.dumps(
            {"role": "development", "status": "complete", "blinded_sha256": digest}
        )
    )
    approval = tmp_path / "approval.json"
    approval.write_text(
        json.dumps(
            {
                "approved_by": ["P6 synthetic test"],
                "pool_sha256": digest,
                "p2_first": [168, 334],
                "p2_second": [668, 834],
            }
        )
    )
    output = tmp_path / "assignment"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "annotations",
            "--pool-dir",
            str(source),
            "--output-dir",
            str(output),
            "--assignment-manifest",
            str(approval),
        ],
    )
    with pytest.raises(SystemExit):
        prepare_p2_annotations.main()
    assert not output.exists()
    manifest.write_text(
        json.dumps({"role": "held_out", "status": "complete", "blinded_sha256": digest})
    )
    prepare_p2_annotations.main()
    for name in ["first", "second"]:
        with (output / f"p2-{name}.csv").open() as f:
            exported = list(csv.DictReader(f))
        assert len(exported) == 167
        assert all(r["relevance"] == "" for r in exported)
