"""Tests for the offline QASPER inspection contract."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from src.data.qasper_inspection import (
    QasperInspectionError,
    inspect_qasper,
    write_report,
)


def _answer(**updates: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "evidence": [],
        "extractive_spans": [],
        "free_form_answer": "",
        "highlighted_evidence": [],
        "unanswerable": False,
        "yes_no": None,
    }
    payload.update(updates)
    return {
        "annotation_id": "annotation-id",
        "worker_id": "worker-id",
        "answer": payload,
    }


def _question(
    question_id: str,
    *,
    question: str = "A question",
    answers: list[Any] | None = None,
) -> dict[str, Any]:
    return {
        "question": question,
        "question_id": question_id,
        "answers": [] if answers is None else answers,
    }


def _paper(
    paper_id: str,
    *,
    full_text: list[Any] | None = None,
    qas: list[Any] | None = None,
    figures_and_tables: list[Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": paper_id,
        "title": "A title",
        "abstract": "An abstract",
        "full_text": full_text or [{"section_name": "Introduction", "paragraphs": ["paragraph"]}],
        "qas": [] if qas is None else qas,
        "figures_and_tables": [] if figures_and_tables is None else figures_and_tables,
    }


def _synthetic_records() -> dict[str, list[dict[str, Any]]]:
    train_questions: list[Any] = [
        _question("unanswerable-id", answers=[_answer(unanswerable=True)]),
        _question("yes-no-id", answers=[_answer(yes_no=True)]),
        _question(
            "extractive-id",
            answers=[
                _answer(
                    extractive_spans=["span"],
                    evidence=[" FLOAT SELECTED: Figure 1"],
                    highlighted_evidence=["", 3],
                )
            ],
        ),
        _question("free-form-id", answers=[_answer(free_form_answer="free form")]),
        _question("invalid-id", answers=[_answer()]),
        _question(
            "ambiguous-id",
            answers=[_answer(unanswerable=True, free_form_answer="also valid")],
        ),
        _question("blank-question-id", question=" ", answers=[]),
        _question(" ", question="Blank identifier", answers=[_answer()]),
        _question("duplicate-id", answers=[_answer()]),
        _question("duplicate-id", answers=[_answer()]),
        _question("wrong-answers-id", answers=None),
        "not-a-question-object",
    ]
    train_questions[10]["answers"] = None
    train = [
        _paper(
            "paper-1",
            full_text=[
                {"section_name": "Introduction", "paragraphs": ["same", " same ", "shared", ""]},
                {"section_name": "Empty", "paragraphs": []},
                {"paragraphs": None},
                "not-a-section-object",
                {"section_name": "Methods", "paragraphs": ["shared", 5]},
            ],
            qas=train_questions,
            figures_and_tables=[{"caption": "caption", "file": "figure.png"}],
        ),
        {
            "title": None,
            "abstract": 7,
            "full_text": [],
            "qas": [],
            "figures_and_tables": [],
        },
    ]
    return {
        "train": train,
        "validation": [
            _paper(
                "paper-2",
                full_text=[{"section_name": "Results", "paragraphs": ["shared"]}],
                qas=[_question("validation-question", answers=[_answer(yes_no=False)])],
            ),
            _paper(
                "paper-1",
                full_text=[{"section_name": "Results", "paragraphs": ["shared"]}],
            ),
        ],
        "test": [
            _paper(
                "paper-3",
                full_text=[{"section_name": "Results", "paragraphs": ["shared"]}],
            )
        ],
    }


def _write_fixture(root: Path) -> Path:
    input_dir = root / "tmp_qasper_input"
    input_dir.mkdir(parents=True)
    records = _synthetic_records()
    split_entries = []
    for split in ("train", "validation", "test"):
        path = input_dir / f"{split}.jsonl"
        with path.open("w", encoding="utf-8", newline="\n") as handle:
            for record in records[split]:
                handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
                handle.write("\n")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        split_entries.append(
            {
                "name": split,
                "file": f"{split}.jsonl",
                "rows": len(records[split]),
                "sha256": digest,
            }
        )
    manifest = {
        "dataset": {
            "config": "tmp-config",
            "id": "tmp/dataset",
            "requested_revision": "tmp-requested-revision",
            "resolved_revision": "tmp-resolved-revision",
            "source_dataset_version": "tmp-version",
        },
        "licenses": {"source_script": "tmp-license"},
        "manifest_schema_version": 1,
        "splits": split_entries,
    }
    (input_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return input_dir


def test_inspection_counts_anomalies_answer_types_and_leakage(tmp_path: Path) -> None:
    report = inspect_qasper(_write_fixture(tmp_path))

    assert report["global_totals"]["paper_count"] == 5
    assert report["global_totals"]["question_count"] == 13
    assert report["per_split"]["train"]["answer_types"] == {
        "extractive": 1,
        "free_form": 1,
        "invalid_or_empty": 4,
        "unanswerable": 2,
        "yes_no": 1,
    }
    assert report["ambiguous_payload"]["per_split"]["train"] == 1
    assert report["answer_types"]["global"]["extractive"] == 1
    assert report["evidence"]["global"]["evidence"]["float_selected_hits"] == 1
    assert report["evidence"]["global"]["highlighted_evidence"]["blank_items"] == 1
    assert report["duplicate_paragraphs"]["same_paper"]["duplicate_group_count"] == 2
    assert report["duplicate_paragraphs"]["cross_paper"]["involved_paper_count"] == 3
    assert report["split_overlap"]["paper_id_intersections"]["train_and_validation"] == [
        "paper-1"
    ]
    assert report["split_overlap"]["observed_paper_disjoint"] is False

    train_fields = report["field_anomalies"]["per_split"]["train"]
    assert train_fields["id"]["missing_key"]["count"] == 1
    assert train_fields["title"]["null"]["count"] == 1
    assert train_fields["abstract"]["wrong_type"]["count"] == 1
    assert train_fields["full_text"]["empty"]["count"] == 1
    assert (
        report["section_anomalies"]["global"]["zero_paragraph_chapter"]["zero"][
            "count"
        ]
        == 1
    )
    assert report["question_anomalies"]["global"]["question"]["blank"]["count"] == 1
    assert report["question_anomalies"]["global"]["question_id"]["duplicate"]["count"] == 1
    assert report["question_anomalies"]["global"]["answers"]["no_answer_annotations"]["count"] >= 1

    serialized = json.dumps(report, ensure_ascii=False, sort_keys=True)
    assert "not-a-section-object" not in serialized


def test_inspection_output_is_deterministic(tmp_path: Path) -> None:
    input_dir = _write_fixture(tmp_path)
    report_a = tmp_path / "tmp_report_a.json"
    report_b = tmp_path / "tmp_report_b.json"
    write_report(inspect_qasper(input_dir), report_a)
    write_report(inspect_qasper(input_dir), report_b)
    assert hashlib.sha256(report_a.read_bytes()).digest() == hashlib.sha256(
        report_b.read_bytes()
    ).digest()
    assert report_a.read_bytes() == report_b.read_bytes()


def test_inspection_rejects_hash_and_row_mismatches(tmp_path: Path) -> None:
    hash_input = _write_fixture(tmp_path / "tmp_hash_case")
    train_path = hash_input / "train.jsonl"
    train_path.write_text(train_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(QasperInspectionError, match="SHA-256 mismatch"):
        inspect_qasper(hash_input)

    row_input = _write_fixture(tmp_path / "tmp_row_case")
    manifest_path = row_input / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["splits"][0]["rows"] += 1
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    with pytest.raises(QasperInspectionError, match="Row-count mismatch"):
        inspect_qasper(row_input)
