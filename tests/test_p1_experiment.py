"""Offline experiment integration: controlled encoder, actual persisted FAISS."""

import json
from collections import Counter

import numpy as np
import pytest

from scripts import run_p1_experiment
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import QUERY_INSTRUCTION, DenseRetriever
from src.retrieval.experiment import (
    SPLIT_POLICY,
    audit_saved_run,
    evaluate_saved_experiment,
    file_sha256,
    load_experiment_inputs,
    run_experiment,
)
from src.retrieval.schemas import Passage


class FakeEncoder:
    model_name = "test/p1-experiment"
    revision = "test-v1"

    def __init__(self):
        self.calls = []

    def encode(self, texts):
        self.calls.extend(texts)
        return np.asarray([[1.0, float("lexical" in text)] for text in texts])


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def write_jsonl(path, values):
    path.write_text(
        "".join(json.dumps(value) + "\n" for value in values), encoding="utf-8"
    )


@pytest.fixture
def experiment_files(tmp_path):
    passages = [
        Passage(
            passage_id=f"opaque-{paper}-{number}",
            paper_id=paper,
            title="Title",
            section="Methods",
            chunk_number=number,
            text=text,
        )
        for paper in ("train-paper", "validation-paper")
        for number, text in enumerate(("lexical matching", "dense vectors"))
    ]
    papers = [
        {"id": paper, "source_split": split}
        for paper, split in (
            ("train-paper", "train"),
            ("empty-paper", "train"),
            ("validation-paper", "validation"),
            ("test-paper", "test"),
        )
    ]
    qa = [
        {
            "question_id": "q2",
            "paper_id": "empty-paper",
            "source_split": "train",
            "question": "Missing paper?",
            "answers": ["LABEL MUST NOT APPEAR"],
        },
        {
            "question_id": "q1",
            "paper_id": "train-paper",
            "source_split": "train",
            "question": "lexical method?",
            "answers": ["LABEL MUST NOT APPEAR"],
        },
        {
            "question_id": "v1",
            "paper_id": "validation-paper",
            "source_split": "validation",
            "question": {"not": "for reading"},
            "answers": ["VALIDATION SECRET"],
        },
        {
            "question_id": "t1",
            "paper_id": "test-paper",
            "source_split": "test",
            "question": {"not": "for reading"},
            "answers": ["HELDOUT SECRET"],
        },
    ]
    for filename, values in (
        ("passages.jsonl", [p.model_dump() for p in passages]),
        ("papers.jsonl", papers),
        ("qa.jsonl", qa),
    ):
        write_jsonl(tmp_path / filename, values)
    source = {
        "dataset_id": "allenai/qasper",
        "resolved_revision": "a" * 40,
        "local_parser_version": 1,
        "split_files": {
            split: {
                "rows": sum(p["source_split"] == split for p in papers),
                "sha256": "d" * 64,
            }
            for split in ("train", "validation", "test")
        },
    }
    export = {
        "manifest_schema_version": 1,
        "artifact": "qasper_papers_and_qa",
        "source": source,
        "split_policy_version": SPLIT_POLICY,
        "outputs": {
            key: {
                "file": f"{key}.jsonl",
                "sha256": file_sha256(tmp_path / f"{key}.jsonl"),
                "rows": len(values),
            }
            for key, values in (("papers", papers), ("qa", qa))
        },
        "split_counts": {
            split: {
                "papers": sum(p["source_split"] == split for p in papers),
                "questions": sum(q["source_split"] == split for q in qa),
            }
            for split in ("train", "validation", "test")
        },
    }
    corpus = {
        "manifest_schema_version": 1,
        "artifact": "development_corpus",
        "scope": "development",
        "purpose": "development",
        "source": {
            "dataset_id": source["dataset_id"],
            "resolved_revision": source["resolved_revision"],
            "local_parser_version": 1,
            "source_splits": source["split_files"],
            "export_papers_file": "papers.jsonl",
            "export_papers_sha256": export["outputs"]["papers"]["sha256"],
            "split_policy_version": SPLIT_POLICY,
            "split_counts": {
                split: {
                    "project_role": role,
                    "included_in_scope": split != "test",
                    "source_paper_count": export["split_counts"][split]["papers"],
                    "passage_count": 0 if split == "test" else 2,
                }
                for split, role in (
                    ("train", "development"),
                    ("validation", "validation"),
                    ("test", "held_out"),
                )
            },
        },
        "chunking": {
            "chunk_size_words": 200,
            "chunk_overlap_words": 40,
            "normalization_version": "text-normalization-v1",
            "chunking_version": "word-chunking-v1",
            "source_kinds": ["full_text"],
        },
        "output": {
            "file": "passages.jsonl",
            "sha256": file_sha256(tmp_path / "passages.jsonl"),
            "scope": "development",
            "purpose": "development",
            "passage_count": 4,
            "unique_passage_count": 4,
            "indexed_paper_count": 2,
            "source_paper_count": 3,
        },
    }
    write_json(tmp_path / "export.manifest.json", export)
    write_json(tmp_path / "corpus.manifest.json", corpus)
    dense_dir = tmp_path / "dense"
    DenseRetriever(passages, encoder=FakeEncoder()).save(dense_dir)
    return {
        "paths": {
            "passages_path": tmp_path / "passages.jsonl",
            "corpus_manifest_path": tmp_path / "corpus.manifest.json",
            "qa_path": tmp_path / "qa.jsonl",
            "export_manifest_path": tmp_path / "export.manifest.json",
        },
        "passages": passages,
        "export": export,
        "corpus": corpus,
        "qa": qa,
        "dense": dense_dir,
        "root": tmp_path,
    }


def test_loader_projects_train_only_and_preserves_passages(experiment_files):
    files = experiment_files
    loaded = load_experiment_inputs(**files["paths"])
    assert loaded.passages == files["passages"]
    assert [q.question_id for q in loaded.questions] == ["q1", "q2"]
    assert all(
        set(vars(q)) == {"question_id", "paper_id", "query"} for q in loaded.questions
    )
    assert loaded.provenance["annotations_used"] is False
    assert loaded.provenance["available_train_questions"] == 2


@pytest.mark.parametrize(
    "problem",
    [
        "hash",
        "count",
        "scope",
        "qa_split",
        "heldout_passage",
        "blank_text",
        "duplicate_id",
        "bad_chunking",
        "missing_chunking",
        "boolean_schema",
    ],
)
def test_loader_rejects_corrupt_or_leaking_inputs(experiment_files, problem):
    files = experiment_files
    if problem == "hash":
        files["paths"]["passages_path"].write_text("tampered", encoding="utf-8")
    elif problem == "count":
        files["corpus"]["output"]["passage_count"] += 1
    elif problem == "scope":
        files["corpus"]["scope"] = "all-paper-text"
    elif problem == "bad_chunking":
        files["corpus"]["chunking"]["chunk_overlap_words"] = 200
    elif problem == "missing_chunking":
        del files["corpus"]["chunking"]
    elif problem == "boolean_schema":
        files["corpus"]["manifest_schema_version"] = True
    elif problem == "qa_split":
        files["qa"][0]["source_split"] = "test"
        write_jsonl(files["paths"]["qa_path"], files["qa"])
        files["export"]["outputs"]["qa"]["sha256"] = file_sha256(
            files["paths"]["qa_path"]
        )
    else:
        rows = [p.model_dump() for p in files["passages"]]
        if problem == "heldout_passage":
            rows[0]["paper_id"] = "test-paper"
        elif problem == "blank_text":
            rows[0]["text"] = "   "
        else:
            rows[0]["passage_id"] = rows[1]["passage_id"]
        write_jsonl(files["paths"]["passages_path"], rows)
        files["corpus"]["output"]["sha256"] = file_sha256(
            files["paths"]["passages_path"]
        )
    write_json(files["paths"]["corpus_manifest_path"], files["corpus"])
    write_json(files["paths"]["export_manifest_path"], files["export"])
    with pytest.raises(ValueError):
        load_experiment_inputs(**files["paths"])


def test_run_persists_results_zero_hits_and_full_index_mapping(experiment_files):
    files = experiment_files
    encoder = FakeEncoder()
    arguments = {
        **files["paths"],
        "p3_commit": "b" * 40,
        "p1_commit": "c" * 40,
        "dense_index_dir": files["dense"],
        "output_dir": files["root"] / "run",
        "top_k": 1,
        "encoder": encoder,
        "local_files_only": True,
    }
    report = run_experiment(**arguments)
    assert report["status"] == "complete"
    assert report["summary"]["result_rows"] == {"bm25": 1, "dense": 1}
    assert report["summary"]["questions_without_passages"] == 1
    for method in ("bm25", "dense"):
        assert (
            0
            <= report["summary"]["latency_p50_ms"][method]
            <= report["summary"]["latency_p95_ms"][method]
        )
    assert report["quality_metrics"] is None
    assert report["p1_source_sha256"]["src/retrieval/experiment.py"]
    output = arguments["output_dir"]
    results = [
        json.loads(line) for line in (output / "results.jsonl").read_text().splitlines()
    ]
    queries = [
        json.loads(line) for line in (output / "queries.jsonl").read_text().splitlines()
    ]
    assert len(results) == 2 and len(queries) == 4
    assert all(row["paper_id"] == "train-paper" and row["rank"] == 1 for row in results)
    assert all(
        row["passage_id"]
        in {p.passage_id for p in files["passages"] if p.paper_id == "train-paper"}
        for row in results
    )
    assert all(row["config"] == "run.json" for row in results + queries)
    assert Counter(row["status"] for row in queries) == {
        "ok": 2,
        "paper_without_passages": 2,
    }
    assert all(row["latency_ms"] >= 0 for row in queries)
    assert encoder.calls == [QUERY_INSTRUCTION + "lexical method?"] * 2
    rendered = "".join(path.read_text() for path in output.glob("*.json*"))
    assert "SECRET" not in rendered and "LABEL MUST" not in rendered
    # Both persisted backends reload, and the deterministic ranking survives.
    arguments["bm25_index_dir"] = output / "bm25-index"
    arguments["output_dir"] = files["root"] / "reloaded-run"
    second = run_experiment(**arguments)
    assert (
        second["output_sha256"]["results.jsonl"]
        == report["output_sha256"]["results.jsonl"]
    )


def test_run_rejects_dense_mapping_with_different_full_fields(experiment_files):
    files = experiment_files
    wrong_dir = files["root"] / "wrong-dense"
    changed = [p.model_copy(update={"title": "changed"}) for p in files["passages"]]
    DenseRetriever(changed, encoder=FakeEncoder()).save(wrong_dir)
    with pytest.raises(ValueError, match="Passage mapping differs"):
        run_experiment(
            **files["paths"],
            p3_commit="b" * 40,
            dense_index_dir=wrong_dir,
            output_dir=files["root"] / "out",
            encoder=FakeEncoder(),
        )
    assert not (files["root"] / "out").exists()


def test_cli_runs_offline_with_real_faiss_and_limits_queries_only(
    experiment_files, monkeypatch, capsys
):
    files = experiment_files
    monkeypatch.setattr(
        run_p1_experiment,
        "run_experiment",
        lambda **kwargs: run_experiment(**kwargs, encoder=FakeEncoder()),
    )
    output = files["root"] / "cli"
    arguments = []
    for key, path in files["paths"].items():
        arguments.extend(
            ["--" + key.removesuffix("_path").replace("_", "-"), str(path)]
        )
    arguments += [
        "--p3-commit",
        "b" * 40,
        "--p1-commit",
        "c" * 40,
        "--dense-index-dir",
        str(files["dense"]),
        "--output-dir",
        str(output),
        "--limit",
        "1",
        "--top-k",
        "1",
        "--local-files-only",
    ]
    run_p1_experiment.main(arguments)
    printed = json.loads(capsys.readouterr().out)
    assert printed["question_count"] == 1
    config = json.loads((output / "run.json").read_text())
    assert config["inputs"]["corpus_counts"]["passage_count"] == 4
    assert config["inputs"]["available_train_questions"] == 2
    with pytest.raises(SystemExit) as error:
        run_p1_experiment.main(arguments)
    assert error.value.code == 2
    assert "new or empty" in capsys.readouterr().err


@pytest.fixture
def saved_experiment(experiment_files):
    """Create one historical run; subsequent audit tests must only read it."""
    files = experiment_files
    directory = files["root"] / "saved-run"
    run_experiment(
        **files["paths"],
        p3_commit="b" * 40,
        p1_commit="c" * 40,
        dense_index_dir=files["dense"],
        output_dir=directory,
        top_k=5,
        encoder=FakeEncoder(),
        local_files_only=True,
    )
    return {
        "files": files,
        "directory": directory,
        "inputs": load_experiment_inputs(**files["paths"]),
    }


def saved_rows(directory, name):
    return [
        json.loads(line)
        for line in (directory / name).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def rewrite_saved_rows(directory, name, rows):
    """Refresh the recorded hash so tests exercise semantic validation."""
    write_jsonl(directory / name, rows)
    config = json.loads((directory / "run.json").read_text(encoding="utf-8"))
    config["output_sha256"][name] = file_sha256(directory / name)
    write_json(directory / "run.json", config)


def source_snapshot(directory):
    return {
        str(path.relative_to(directory)): path.read_bytes()
        for path in directory.rglob("*")
        if path.is_file()
    }


def forbid_retrieval(monkeypatch):
    def fail(*args, **kwargs):
        raise AssertionError(
            "Saved-run evaluation must not execute retrieval or encoding"
        )

    for retriever in (BM25Retriever, DenseRetriever):
        for operation in ("__init__", "load", "retrieve"):
            monkeypatch.setattr(retriever, operation, fail)
    monkeypatch.setattr(FakeEncoder, "encode", fail)
    monkeypatch.setattr(run_p1_experiment, "run_experiment", fail)


def test_saved_audit_accepts_min_k_and_empty_paper_without_retrieval(
    saved_experiment, monkeypatch
):
    saved = saved_experiment
    before = source_snapshot(saved["directory"])
    forbid_retrieval(monkeypatch)
    audit, rankings, counts = audit_saved_run(saved["directory"], saved["inputs"])
    assert audit["status"] == "valid" and audit["issues"] == []
    assert audit["filters"] == {"paper_id": "question.paper_id", "section": None}
    for method in ("bm25", "dense"):
        report = audit["methods"][method]
        assert report["return_count_distribution"] == {
            "0": 1,
            "1": 0,
            "2": 1,
            "3": 0,
            "4": 0,
            "5": 0,
        }
        assert report["expected_result_rows"] == report["result_rows"] == 2
        assert report["maximum_slots"] == 10
        assert report["legitimate_missing_slots"] == 8
        assert rankings[method]["q2"] == []
        assert len(rankings[method]["q1"]) == 2
        short = {row["question_id"]: row for row in report["short_queries"]}
        assert short["q1"]["reason"] == "eligible_passages_below_k"
        assert short["q1"]["actual_count"] == short["q1"]["expected_count"] == 2
        assert short["q2"]["reason"] == "paper_without_passages"
        assert short["q2"]["actual_count"] == short["q2"]["expected_count"] == 0
    assert len(counts) == 4
    assert source_snapshot(saved["directory"]) == before


def test_evaluate_without_labels_records_unavailable_and_preserves_source(
    saved_experiment, monkeypatch
):
    saved = saved_experiment
    output = saved["files"]["root"] / "evaluation"
    before = source_snapshot(saved["directory"])
    forbid_retrieval(monkeypatch)
    report = evaluate_saved_experiment(
        run_dir=saved["directory"], output_dir=output, evaluation_k=2
    )
    assert report["status"] == "valid"
    assert report["evaluation_status"] == "unavailable"
    quality = json.loads((output / "evaluation.json").read_text(encoding="utf-8"))
    assert quality["metrics"] is None and quality["evaluated_questions"] == 0
    assert quality["k"] == 2 and quality["excluded"] == {"missing_labels": 2}
    assert len(saved_rows(output, "counts.jsonl")) == 4
    provenance = json.loads((output / "provenance.json").read_text(encoding="utf-8"))
    assert provenance["retrieval_repeated"] is False
    assert provenance["source_outputs_modified"] is False
    assert source_snapshot(saved["directory"]) == before


def test_evaluate_cli_reuses_saved_outputs_without_encoder_or_retrievers(
    saved_experiment, monkeypatch, capsys
):
    saved = saved_experiment
    output = saved["files"]["root"] / "cli-evaluation"
    before = source_snapshot(saved["directory"])
    forbid_retrieval(monkeypatch)
    run_p1_experiment.main(
        [
            "evaluate",
            "--run-dir",
            str(saved["directory"]),
            "--output-dir",
            str(output),
            "--evaluation-k",
            "1",
        ]
    )
    report = json.loads(capsys.readouterr().out)
    assert report["status"] == "valid"
    assert report["evaluation_status"] == "unavailable"
    assert report["question_count"] == 2
    assert report["result_rows"] == {"bm25": 2, "dense": 2}
    assert source_snapshot(saved["directory"]) == before


@pytest.mark.parametrize("known_exporter", [True, False])
def test_saved_audit_only_accepts_verified_legacy_filter_policy(
    saved_experiment, known_exporter
):
    saved = saved_experiment
    config_path = saved["directory"] / "run.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    del config["filters"]
    config["p1_source_sha256"]["src/retrieval/experiment.py"] = (
        "ab31e5b3004ede59e845209d6ec0c2952f84f0e27b6a670edeaae2fe342ad626"
        if known_exporter
        else "f" * 64
    )
    write_json(config_path, config)
    if not known_exporter:
        with pytest.raises(ValueError, match="unknown filtering policy"):
            audit_saved_run(saved["directory"], saved["inputs"])
    else:
        audit, _, _ = audit_saved_run(saved["directory"], saved["inputs"])
        assert audit["status"] == "valid"
        assert audit["filters"]["section"] is None
        assert "verified legacy exporter" in audit["filter_evidence"]


def test_saved_audit_rejects_unverified_output_hash(saved_experiment):
    saved = saved_experiment
    path = saved["directory"] / "results.jsonl"
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="SHA-256 differs from run"):
        audit_saved_run(saved["directory"], saved["inputs"])


@pytest.mark.parametrize(
    ("problem", "message"),
    [
        ("duplicate_query", "duplicate query log"),
        ("duplicate_passage", "duplicate passage"),
        ("unknown_passage", "unknown passage_id"),
        ("cross_paper", "cross-paper result"),
        ("cross_section", "cross-section result"),
        ("nonfinite_score", "invalid score"),
        ("nonfinite_latency", "invalid latency_ms"),
        ("invalid_rank", "invalid result rank"),
        ("duplicate_rank", "duplicate or non-continuous rank"),
        ("increasing_scores", "scores not descending"),
        ("non_train_question", "unknown/non-development question_id"),
    ],
)
def test_saved_audit_rejects_semantic_corruption_after_hash_refresh(
    saved_experiment, problem, message
):
    saved = saved_experiment
    directory = saved["directory"]
    filename = (
        "queries.jsonl"
        if problem in {"duplicate_query", "nonfinite_latency"}
        else "results.jsonl"
    )
    rows = saved_rows(directory, filename)
    if problem == "duplicate_query":
        rows.append(dict(rows[0]))
    elif problem == "duplicate_passage":
        rows[1]["passage_id"] = rows[0]["passage_id"]
    elif problem == "unknown_passage":
        rows[0]["passage_id"] = "missing-passage"
    elif problem == "cross_paper":
        rows[0]["passage_id"] = "opaque-validation-paper-0"
    elif problem == "cross_section":
        config = json.loads((directory / "run.json").read_text(encoding="utf-8"))
        config["filters"]["section"] = "Results"
        write_json(directory / "run.json", config)
    elif problem == "nonfinite_score":
        rows[0]["score"] = float("nan")
    elif problem == "nonfinite_latency":
        rows[0]["latency_ms"] = float("inf")
    elif problem == "invalid_rank":
        rows[0]["rank"] = True
    elif problem == "duplicate_rank":
        rows[1]["rank"] = rows[0]["rank"]
    elif problem == "increasing_scores":
        rows[0]["score"], rows[1]["score"] = 0.0, 1.0
    else:
        rows[0]["question_id"] = "t1"
    rewrite_saved_rows(directory, filename, rows)
    with pytest.raises(ValueError, match=message):
        audit_saved_run(directory, saved["inputs"])


@pytest.mark.parametrize(
    ("problem", "issue"),
    [
        ("missing_query", "missing_query_log"),
        ("missing_result", "expected_return_count_mismatch"),
        ("count_mismatch", "logged_hit_count_mismatch"),
    ],
)
def test_saved_audit_reports_incomplete_artifacts_and_prevents_scoring(
    saved_experiment, problem, issue
):
    saved = saved_experiment
    filename = "results.jsonl" if problem == "missing_result" else "queries.jsonl"
    rows = saved_rows(saved["directory"], filename)
    if problem == "missing_result":
        del rows[1]  # Keep rank 1 intact: the failure is missing count, not rank order.
    elif problem == "missing_query":
        del rows[0]
    else:
        rows[0]["hit_count"] = 1
    rewrite_saved_rows(saved["directory"], filename, rows)
    output = saved["files"]["root"] / "invalid-evaluation"
    report = evaluate_saved_experiment(run_dir=saved["directory"], output_dir=output)
    audit = json.loads((output / "audit.json").read_text(encoding="utf-8"))
    observed = {name for entry in audit["issues"] for name in entry["issues"]}
    assert report["status"] == "invalid" and issue in observed
    quality = json.loads((output / "evaluation.json").read_text(encoding="utf-8"))
    assert quality["status"] == "unavailable" and quality["metrics"] is None
    assert "invalid retrieval artifacts" in quality["reason"]


@pytest.mark.parametrize("evaluation_k", [0, -1, 6, True])
def test_saved_evaluation_rejects_k_outside_saved_depth(saved_experiment, evaluation_k):
    saved = saved_experiment
    output = saved["files"]["root"] / "bad-k"
    before = source_snapshot(saved["directory"])
    with pytest.raises(ValueError, match="no deeper than saved retrieval K"):
        evaluate_saved_experiment(
            run_dir=saved["directory"], output_dir=output, evaluation_k=evaluation_k
        )
    assert not output.exists()
    assert source_snapshot(saved["directory"]) == before


def test_saved_evaluation_refuses_existing_output_and_source_directory(
    saved_experiment,
):
    saved = saved_experiment
    output = saved["files"]["root"] / "existing-evaluation"
    output.mkdir()
    sentinel = output / "keep.txt"
    sentinel.write_text("Existing evaluation must survive", encoding="utf-8")
    before = source_snapshot(saved["directory"])
    with pytest.raises(ValueError, match="new or empty"):
        evaluate_saved_experiment(run_dir=saved["directory"], output_dir=output)
    assert sentinel.read_text(encoding="utf-8") == "Existing evaluation must survive"
    for destination in (saved["directory"], saved["directory"] / "nested"):
        with pytest.raises(ValueError, match="outside the source run"):
            evaluate_saved_experiment(
                run_dir=saved["directory"], output_dir=destination
            )
    assert source_snapshot(saved["directory"]) == before


def test_saved_evaluation_accepts_explicit_paths_after_artifact_relocation(
    saved_experiment, monkeypatch
):
    saved = saved_experiment
    directory = saved["directory"]
    config = json.loads((directory / "run.json").read_text(encoding="utf-8"))
    config["inputs"]["paths"] = {
        key: str(saved["files"]["root"] / "unavailable" / key)
        for key in config["inputs"]["paths"]
    }
    write_json(directory / "run.json", config)
    forbid_retrieval(monkeypatch)
    report = evaluate_saved_experiment(
        run_dir=directory,
        output_dir=saved["files"]["root"] / "relocated-evaluation",
        **saved["files"]["paths"],
    )
    assert report["status"] == "valid"


def test_labeled_evaluate_cli_scores_handwritten_synthetic_subset_only(
    saved_experiment, monkeypatch, capsys
):
    saved = saved_experiment
    root = saved["files"]["root"]
    labels = root / "handwritten-synthetic-qrels.jsonl"
    manifest_path = root / "handwritten-synthetic-qrels.manifest.json"
    # These relevance decisions are handwritten for the synthetic passages above.
    # Never select labels by copying a retriever's output or use real-data labels.
    write_jsonl(
        labels,
        [
            {
                "question_id": "q1",
                "paper_id": "train-paper",
                "status": "mapped",
                "relevance_complete": True,
                "relevant_passage_ids": ["opaque-train-paper-0"],
            },
            {
                "question_id": "q2",
                "paper_id": "empty-paper",
                "status": "mapping_failed",
                "relevance_complete": False,
                "relevant_passage_ids": [],
            },
        ],
    )
    write_json(
        manifest_path,
        {
            "format_version": 1,
            "labels_format": "jsonl",
            "labels_sha256": file_sha256(labels),
            "corpus_sha256": file_sha256(saved["files"]["paths"]["passages_path"]),
            "source": "Handwritten synthetic test judgments, independent of rankings",
            "mapping": {
                "version": "handwritten-synthetic-v1",
                "description": "Fixed fixture passage IDs; empty-paper mapping fails",
            },
            "annotation_coverage": "complete",
            "question_scope": {
                "source_split": "train",
                "project_role": "development",
                "split_policy_version": SPLIT_POLICY,
                "question_ids": ["q1", "q2"],
            },
        },
    )
    before = source_snapshot(saved["directory"])
    output = root / "labeled-cli-evaluation"
    forbid_retrieval(monkeypatch)
    run_p1_experiment.main(
        [
            "evaluate",
            "--run-dir",
            str(saved["directory"]),
            "--output-dir",
            str(output),
            "--evaluation-k",
            "5",
            "--labels",
            str(labels),
            "--labels-manifest",
            str(manifest_path),
        ]
    )
    printed = json.loads(capsys.readouterr().out)
    assert printed["status"] == "valid"
    assert printed["evaluation_status"] == "provisional"
    quality = json.loads((output / "evaluation.json").read_text(encoding="utf-8"))
    assert quality["status"] == "provisional"
    scope = quality["evaluation_scope"]
    assert scope["kind"] == "subset"
    assert scope["scoped_questions"] == scope["labeled_questions"] == 2
    assert scope["eligible_questions"] == scope["excluded_questions"] == 1
    for method in ("bm25", "dense"):
        result = quality["methods"][method]
        assert result["eligible_questions"] == 1
        assert result["excluded_questions"] == {"mapping_failed": 1}
        # One known relevant first hit / K=5; the excluded query is not a zero.
        assert result["metrics"] == pytest.approx(
            {"precision_at_k": 0.2, "recall_at_k": 1.0, "mrr_at_k": 1.0}
        )
        per_question = {row["question_id"]: row for row in result["per_question"]}
        assert per_question["q1"]["metrics"] == result["metrics"]
        assert per_question["q1"]["returned_at_k"] == 2
        assert per_question["q2"]["metrics"] is None
        assert per_question["q2"]["exclusion_reason"] == "mapping_failed"
        assert per_question["q2"]["returned_at_k"] == 0
    assert quality["labels"]["labels_sha256"] == file_sha256(labels)
    assert source_snapshot(saved["directory"]) == before
