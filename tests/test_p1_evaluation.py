"""Hand-calculated synthetic relevance fixtures; no real quality claims."""

import json

import pytest

from src.retrieval.evaluation import (
    DEFAULT_SPLIT_POLICY,
    _sha256,
    evaluate_rankings,
    load_qrels,
)


@pytest.fixture
def label_files(tmp_path):
    questions = {"q1": "paper-a", "q2": "paper-b"}
    passages = {
        "a1": "paper-a",
        "a2": "paper-a",
        "a3": "paper-a",
        "a4": "paper-a",
        "b1": "paper-b",
    }
    rows = [
        {
            "question_id": "q1",
            "paper_id": "paper-a",
            "status": "mapped",
            "relevance_complete": True,
            "relevant_passage_ids": ["a1", "a3"],
        },
        {
            "question_id": "q2",
            "paper_id": "paper-b",
            "status": "mapped",
            "relevance_complete": True,
            "relevant_passage_ids": ["b1"],
        },
    ]
    manifest = {
        "format_version": 1,
        "labels_format": "jsonl",
        "corpus_sha256": "a" * 64,
        "source": "hand-calculated synthetic test fixture",
        "mapping": {"version": "synthetic-v1", "description": "explicit fixture IDs"},
        "annotation_coverage": "complete",
        "question_scope": {
            "source_split": "train",
            "project_role": "development",
            "split_policy_version": DEFAULT_SPLIT_POLICY,
            "question_ids": list(questions),
        },
    }
    return {
        "labels": tmp_path / "qrels.jsonl",
        "manifest_path": tmp_path / "qrels.manifest.json",
        "questions": questions,
        "passages": passages,
        "rows": rows,
        "manifest": manifest,
    }


def publish(files, trec_text=None):
    text = (
        trec_text
        if trec_text is not None
        else "".join(json.dumps(row) + "\n" for row in files["rows"])
    )
    files["labels"].write_text(text, encoding="utf-8")
    files["manifest"]["labels_sha256"] = _sha256(files["labels"])
    files["manifest_path"].write_text(json.dumps(files["manifest"]), encoding="utf-8")


def load(files):
    return load_qrels(
        files["labels"],
        files["manifest_path"],
        corpus_sha256="a" * 64,
        questions=files["questions"],
        passages=files["passages"],
    )


def test_hand_calculated_macro_metrics_and_cutoff(label_files):
    publish(label_files)
    report = evaluate_rankings(
        {"bm25": {"q1": ["a2", "a1", "a3"], "q2": ["b1"]}}, load(label_files), k=2
    )
    method = report["methods"]["bm25"]
    assert method["eligible_questions"] == 2
    assert method["metrics"] == pytest.approx(
        {"precision_at_k": 0.5, "recall_at_k": 0.75, "mrr_at_k": 0.75}
    )
    assert report["backend"]["status"] == "P6_pending"
    assert method["judged_coverage_at_k"] == 1


def test_empty_retrieval_with_known_relevant_is_zero(label_files):
    publish(label_files)
    method = evaluate_rankings({"dense": {"q1": [], "q2": []}}, load(label_files), k=5)[
        "methods"
    ]["dense"]
    assert method["metrics"] == {"precision_at_k": 0, "recall_at_k": 0, "mrr_at_k": 0}
    assert method["eligible_questions"] == 2
    assert method["judged_coverage_at_k"] is None


def test_distinct_exclusions_are_not_zero_scores(label_files):
    files = label_files
    states = [
        ("mapped", False),
        ("mapping_failed", False),
        ("unanswerable", True),
        ("no_relevant", True),
    ]
    files["questions"] = {f"q{i}": "paper-a" for i in range(5)}
    files["manifest"]["question_scope"]["question_ids"] = list(files["questions"])
    files["manifest"]["annotation_coverage"] = "partial"
    files["rows"] = [
        {
            "question_id": f"q{i}",
            "paper_id": "paper-a",
            "status": status,
            "relevance_complete": complete,
            "relevant_passage_ids": ["a1"] if status == "mapped" else [],
            "judged_passage_ids": ["a1", "a2"] if status == "mapped" else [],
        }
        for i, (status, complete) in enumerate(states)
    ]
    publish(files)
    result = evaluate_rankings(
        {"bm25": {qid: ["a1", "a3"] for qid in files["questions"]}}, load(files), k=2
    )["methods"]["bm25"]
    assert result["metrics"] is None
    assert result["eligible_questions"] == 0
    assert result["excluded_questions"] == {
        "incomplete_relevance": 1,
        "mapping_failed": 1,
        "unanswerable": 1,
        "no_relevant": 1,
        "missing_labels": 1,
    }
    assert result["per_question"][0]["judged_coverage_at_k"] == 0.5
    assert all(row["metrics"] is None for row in result["per_question"])


@pytest.mark.parametrize(
    "problem",
    [
        "corpus_hash",
        "label_hash",
        "unknown_qid",
        "unknown_pid",
        "cross_paper",
        "duplicate_qid",
        "duplicate_pid",
        "scope",
        "heldout",
        "policy",
        "missing_complete",
        "missing_source",
        "bad_version",
        "unproven_zero",
    ],
)
def test_invalid_labels_fail_closed(label_files, problem):
    files = label_files
    if problem == "corpus_hash":
        files["manifest"]["corpus_sha256"] = "b" * 64
    elif problem == "unknown_qid":
        files["rows"][0]["question_id"] = "unknown"
    elif problem == "unknown_pid":
        files["rows"][0]["relevant_passage_ids"] = ["unknown"]
    elif problem == "cross_paper":
        files["rows"][0]["relevant_passage_ids"] = ["b1"]
    elif problem == "duplicate_qid":
        files["rows"].append(files["rows"][0])
    elif problem == "duplicate_pid":
        files["rows"][0]["relevant_passage_ids"] = ["a1", "a1"]
    elif problem == "scope":
        files["manifest"]["question_scope"]["question_ids"] = ["q1"]
    elif problem == "heldout":
        files["manifest"]["question_scope"]["source_split"] = "test"
    elif problem == "policy":
        files["manifest"]["question_scope"]["split_policy_version"] = "other"
    elif problem == "missing_complete":
        files["rows"].pop()
    elif problem == "missing_source":
        del files["manifest"]["source"]
    elif problem == "bad_version":
        files["manifest"]["format_version"] = True
    elif problem == "unproven_zero":
        files["rows"][0].update(
            status="no_relevant", relevance_complete=False, relevant_passage_ids=[]
        )
    publish(files)
    if problem == "label_hash":
        with files["labels"].open("a") as handle:
            handle.write("\n")
    with pytest.raises(ValueError):
        load(files)


def test_trec_adapter_nonrelevant_and_positive_grades(label_files):
    files = label_files
    files["manifest"].update(
        labels_format="trec",
        assessments={
            row["question_id"]: {
                key: row[key] for key in ("paper_id", "status", "relevance_complete")
            }
            for row in files["rows"]
        },
    )
    publish(files, "q1 0 a2 0\nq1 0 a1 1\nq1 0 a3 2\nq2 0 b1 1\n")
    qrels = load(files)
    assert qrels.judgments["q1"].relevant_passage_ids == {"a1", "a3"}
    assert qrels.judgments["q1"].judged_passage_ids == {"a1", "a2", "a3"}
    result = evaluate_rankings(
        {"dense": {"q1": ["a2", "a3"], "q2": ["b1"]}}, qrels, k=2
    )
    assert result["methods"]["dense"]["metrics"]["mrr_at_k"] == 0.75


@pytest.mark.parametrize(
    "line",
    [
        "q1 0 a1 -1",
        "q1 0 a1 1.5",
        "unknown 0 a1 0",
        "q1 0 b1 0",
        "q1 0 unknown 0",
        "q1 0 a1 1\nq1 0 a1 0",
    ],
)
def test_trec_rejects_bad_or_duplicate_judgments(label_files, line):
    files = label_files
    files["manifest"].update(
        labels_format="trec",
        assessments={
            row["question_id"]: {
                key: row[key] for key in ("paper_id", "status", "relevance_complete")
            }
            for row in files["rows"]
        },
    )
    publish(files, line + "\n")
    with pytest.raises(ValueError):
        load(files)


@pytest.mark.parametrize(
    "ranking",
    [
        {"q1": [], "q2": ["b1"], "unknown": []},
        {"q1": []},
        {"q1": ["a1", "a1"], "q2": []},
        {"q1": ["b1"], "q2": []},
        {"q1": ["unknown"], "q2": []},
    ],
)
def test_rankings_preserve_scope_identity_and_unique_candidates(label_files, ranking):
    publish(label_files)
    with pytest.raises(ValueError):
        evaluate_rankings({"dense": ranking}, load(label_files), k=1)


def test_replacement_backend_receives_only_eligible_queries(label_files):
    files = label_files
    files["rows"][1].update(status="unanswerable", relevant_passage_ids=[])
    publish(files)

    class Replacement:
        name = "test-p6-contract"

        def __init__(self):
            self.calls = []

        def score(self, retrieved, relevant, *, k):
            self.calls.append((retrieved, relevant, k))
            return {"precision_at_k": 1.0, "recall_at_k": 0.5, "mrr_at_k": 1.0}

    backend = Replacement()
    result = evaluate_rankings(
        {"dense": {"q1": ["a1", "a2"], "q2": []}}, load(files), k=1, backend=backend
    )
    assert backend.calls == [(["a1"], frozenset({"a1", "a3"}), 1)]
    assert result["backend"] == {"name": "test-p6-contract", "status": "external"}
    assert result["methods"]["dense"]["eligible_questions"] == 1


def test_empty_partial_labels_never_create_quality_scores(label_files):
    files = label_files
    files["manifest"]["annotation_coverage"] = "partial"
    files["rows"] = []
    publish(files)
    report = evaluate_rankings({"dense": {"q1": ["a1"], "q2": []}}, load(files), k=1)
    assert report["status"] == "unavailable"
    assert report["evaluation_scope"]["kind"] == "none"
    method = report["methods"]["dense"]
    assert method["metrics"] is None
    assert method["excluded_questions"] == {"missing_labels": 2}
    assert method["labeled_questions"] == method["eligible_questions"] == 0


def test_manifest_rejects_duplicate_json_keys(label_files):
    files = label_files
    publish(files)
    value = files["manifest_path"].read_text()
    files["manifest_path"].write_text(
        value[:-1] + ', "format_version": 1}', encoding="utf-8"
    )
    with pytest.raises(ValueError, match="duplicate JSON key"):
        load(files)


def test_first_relevant_after_cutoff_has_zero_mrr_at_k(label_files):
    publish(label_files)
    rankings = {"dense": {"q1": ["a2", "a4", "a1"], "q2": []}}
    qrels = load(label_files)
    report = evaluate_rankings(rankings, qrels, k=2)
    assert report["status"] == "provisional"
    assert report["evaluation_scope"]["kind"] == "all"
    assert report["methods"]["dense"]["metrics"] == {
        "precision_at_k": 0,
        "recall_at_k": 0,
        "mrr_at_k": 0,
    }
    deeper = evaluate_rankings(rankings, qrels, k=3)
    assert deeper["methods"]["dense"]["per_question"][0]["metrics"][
        "mrr_at_k"
    ] == pytest.approx(1 / 3)


def test_jsonl_question_paper_id_must_match_scope(label_files):
    label_files["rows"][0]["paper_id"] = "paper-b"
    publish(label_files)
    with pytest.raises(ValueError, match="question paper mismatch"):
        load(label_files)


def test_partial_annotation_scores_only_eligible_subset(label_files):
    files = label_files
    files["rows"].pop()
    files["manifest"]["annotation_coverage"] = "partial"
    publish(files)
    report = evaluate_rankings({"dense": {"q1": ["a1"], "q2": []}}, load(files), k=1)
    assert report["status"] == "provisional"
    assert report["evaluation_scope"]["kind"] == "subset"
    assert report["evaluation_scope"]["scoped_questions"] == 2
    assert report["evaluation_scope"]["labeled_questions"] == 1
    assert report["evaluation_scope"]["eligible_questions"] == 1
    assert report["evaluation_scope"]["excluded_questions"] == 1
    assert report["methods"]["dense"]["metrics"] == {
        "precision_at_k": 1,
        "recall_at_k": 0.5,
        "mrr_at_k": 1,
    }
    assert report["methods"]["dense"]["excluded_questions"] == {"missing_labels": 1}
