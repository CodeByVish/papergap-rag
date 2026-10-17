from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from scripts import build_corpus
from src.data.qasper_export import (
    check_qasper_export,
    export_qasper,
    load_verified_papers,
)

SPLITS = ("train", "validation", "test")


def _records() -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for split in SPLITS:
        result[split] = [
            {
                "id": f"paper-{split}",
                "title": f"Paper title {split}",
                "abstract": f"Abstract {split}",
                "full_text": [
                    {
                        "section_name": "Introduction",
                        "paragraphs": [f"Body words for {split} paper."],
                    }
                ],
                "figures_and_tables": [],
                "custom_metadata": {"kept": True},
                "qas": [
                    {
                        "question_id": f"question-{split}",
                        "question": f"Question text for {split}?",
                        "answers": [
                            {
                                "annotation_id": f"annotation-{split}",
                                "worker_id": "worker-1",
                                "answer": {
                                    "unanswerable": False,
                                    "evidence": [f"Evidence {split}"],
                                },
                            }
                        ],
                        "question_metadata": {"kept": True},
                    }
                ],
            }
        ]
    return result


def _write_source(
    root: Path, records: dict[str, list[dict[str, Any]]] | None = None
) -> Path:
    input_dir = root / "tmp_qasper_input"
    input_dir.mkdir()
    records = _records() if records is None else records
    split_entries = []
    for split in SPLITS:
        path = input_dir / f"{split}.jsonl"
        payload = "".join(
            json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n"
            for record in records[split]
        ).encode("utf-8")
        path.write_bytes(payload)
        split_entries.append(
            {
                "name": split,
                "file": path.name,
                "rows": len(records[split]),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
    source_manifest = {
        "manifest_schema_version": 1,
        "dataset": {
            "id": "allenai/qasper",
            "resolved_revision": "a" * 40,
            "local_parser_version": 1,
        },
        "splits": split_entries,
    }
    (input_dir / "manifest.json").write_text(
        json.dumps(source_manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return input_dir


def _export_paths(root: Path) -> tuple[Path, Path, Path]:
    return (
        root / "tmp_papers.jsonl",
        root / "tmp_qa.jsonl",
        root / "tmp_qasper_export.manifest.json",
    )


def _export(root: Path, input_dir: Path | None = None) -> tuple[Path, Path, Path]:
    papers, qa, manifest = _export_paths(root)
    export_qasper(
        input_dir=_write_source(root) if input_dir is None else input_dir,
        papers_output=papers,
        qa_output=qa,
        manifest_output=manifest,
    )
    return papers, qa, manifest


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_export_preserves_source_fields_and_checker_counts(tmp_path: Path) -> None:
    source = _records()
    papers_path, qa_path, manifest_path = _export(tmp_path, _write_source(tmp_path, source))

    papers = _read_jsonl(papers_path)
    qa = _read_jsonl(qa_path)
    assert [record["source_split"] for record in papers] == list(SPLITS)
    assert all("qas" not in record for record in papers)
    assert papers[0] == {
        **{key: value for key, value in source["train"][0].items() if key != "qas"},
        "source_split": "train",
    }
    assert qa[0] == {
        **source["train"][0]["qas"][0],
        "paper_id": "paper-train",
        "source_split": "train",
    }
    assert qa[0]["answers"] == source["train"][0]["qas"][0]["answers"]

    summary = check_qasper_export(
        papers_path=papers_path, qa_path=qa_path, manifest_path=manifest_path
    )
    assert summary["papers"]["rows"] == 3
    assert summary["qa"]["rows"] == 3
    assert summary["qa"]["answer_annotation_count"] == 3
    assert summary["split_counts"]["test"]["questions"] == 1
    loaded_manifest, loaded_papers = load_verified_papers(
        papers_path=papers_path, manifest_path=manifest_path
    )
    assert loaded_manifest["outputs"]["qa"]["rows"] == 3
    assert len(loaded_papers) == 3


def test_export_rejects_cross_split_duplicate_paper_id(tmp_path: Path) -> None:
    records = _records()
    records["validation"][0]["id"] = records["train"][0]["id"]
    input_dir = _write_source(tmp_path, records)
    papers, qa, manifest = _export_paths(tmp_path)

    with pytest.raises(ValueError, match="duplicate paper ID"):
        export_qasper(
            input_dir=input_dir,
            papers_output=papers,
            qa_output=qa,
            manifest_output=manifest,
        )
    assert not papers.exists()
    assert not qa.exists()
    assert not manifest.exists()


def test_export_rejects_cross_split_duplicate_question_id(tmp_path: Path) -> None:
    records = _records()
    records["validation"][0]["qas"][0]["question_id"] = records["train"][0]["qas"][0][
        "question_id"
    ]
    input_dir = _write_source(tmp_path, records)
    papers, qa, manifest = _export_paths(tmp_path)

    with pytest.raises(ValueError, match="duplicate question ID"):
        export_qasper(
            input_dir=input_dir,
            papers_output=papers,
            qa_output=qa,
            manifest_output=manifest,
        )
    assert not papers.exists()
    assert not qa.exists()
    assert not manifest.exists()


@pytest.mark.parametrize(
    ("case", "exception_type", "message"),
    [
        ("qas-not-list", TypeError, "qas must be a list"),
        ("answers-not-list", TypeError, "answers must be a list"),
        ("blank-paper-id", ValueError, "id must be a non-empty string"),
        ("blank-question-id", ValueError, "question_id must be a non-empty string"),
    ],
)
def test_export_validates_required_lists_and_ids(
    tmp_path: Path,
    case: str,
    exception_type: type[Exception],
    message: str,
) -> None:
    records = _records()
    if case == "qas-not-list":
        records["train"][0]["qas"] = None
    elif case == "answers-not-list":
        records["train"][0]["qas"][0]["answers"] = None
    elif case == "blank-paper-id":
        records["train"][0]["id"] = "  "
    else:
        records["train"][0]["qas"][0]["question_id"] = "  "
    input_dir = _write_source(tmp_path, records)
    papers, qa, manifest = _export_paths(tmp_path)

    with pytest.raises(exception_type, match=message):
        export_qasper(
            input_dir=input_dir,
            papers_output=papers,
            qa_output=qa,
            manifest_output=manifest,
        )


@pytest.mark.parametrize(
    ("record_kind", "field", "value", "message"),
    [
        ("paper", "source_split", "train", "source_split"),
        ("question", "paper_id", "paper-conflict", "export field"),
        ("question", "source_split", "train", "export field"),
        ("question", "full_text", [], "paper-only field"),
    ],
)
def test_export_rejects_reserved_field_conflicts(
    tmp_path: Path,
    record_kind: str,
    field: str,
    value: object,
    message: str,
) -> None:
    records = _records()
    target = records["train"][0]
    if record_kind == "paper":
        target[field] = value
    else:
        target["qas"][0][field] = value
    input_dir = _write_source(tmp_path, records)
    papers, qa, manifest = _export_paths(tmp_path)

    with pytest.raises(ValueError, match=message):
        export_qasper(
            input_dir=input_dir,
            papers_output=papers,
            qa_output=qa,
            manifest_output=manifest,
        )


def test_export_rejects_changed_input_hash_and_existing_output(tmp_path: Path) -> None:
    input_dir = _write_source(tmp_path)
    papers, qa, manifest = _export_paths(tmp_path)
    with (input_dir / "train.jsonl").open("ab") as handle:
        handle.write(b" ")
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        export_qasper(
            input_dir=input_dir,
            papers_output=papers,
            qa_output=qa,
            manifest_output=manifest,
        )

    papers.write_bytes(b"keep")
    with pytest.raises(FileExistsError, match="partial QASPER export"):
        export_qasper(
            input_dir=input_dir,
            papers_output=papers,
            qa_output=qa,
            manifest_output=manifest,
        )
    assert papers.read_bytes() == b"keep"
    assert not qa.exists()
    assert not manifest.exists()


def test_checker_rejects_output_hash_mismatch(tmp_path: Path) -> None:
    papers, qa, manifest = _export(tmp_path)
    with qa.open("ab") as handle:
        handle.write(b" ")

    with pytest.raises(ValueError, match="QA SHA-256 differs from manifest"):
        check_qasper_export(papers_path=papers, qa_path=qa, manifest_path=manifest)


def test_development_corpus_reads_only_train_and_validation_paper_text(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    papers_path, qa_path, export_manifest = _export(tmp_path)
    qa_path.rename(tmp_path / "tmp_unavailable_qa.jsonl")
    monkeypatch.setattr(build_corpus, "MIN_PASSAGES", 0)
    monkeypatch.setattr(build_corpus, "MIN_WORDS", 0)
    corpus_path = tmp_path / "tmp_development_passages.jsonl"
    corpus_manifest_path = tmp_path / "tmp_development_passages.manifest.json"

    manifest = build_corpus.build_corpus(
        papers=papers_path,
        export_manifest=export_manifest,
        output=corpus_path,
        manifest_output=corpus_manifest_path,
        scope="development",
        chunk_size_words=20,
        chunk_overlap_words=2,
    )

    passage_records = _read_jsonl(corpus_path)
    assert {record["paper_id"] for record in passage_records} == {
        "paper-train",
        "paper-validation",
    }
    assert all("test" not in record["text"] for record in passage_records)
    assert manifest["scope"] == "development"
    assert manifest["source"]["split_counts"]["test"]["passage_count"] == 0
