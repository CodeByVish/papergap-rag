"""Create and verify deterministic paper and question exports for QASPER."""

from __future__ import annotations

import hashlib
import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any

from src.data.passage_ids import QASPER_DATASET_ID
from src.data.qasper_inspection import _validate_input_files
from src.data.split_policy import SPLIT_POLICY_VERSION

SPLITS = ("train", "validation", "test")
_SHA256_LENGTH = 64
_COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_PAPER_ONLY_FIELDS = ("abstract", "full_text", "figures_and_tables")


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_sha256(value: object) -> bool:
    return (
        type(value) is str
        and len(value) == _SHA256_LENGTH
        and all(character in "0123456789abcdef" for character in value)
    )


def _nonempty_identifier(value: object, *, field: str, split: str, line: int) -> str:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{split} line {line}: {field} must be a non-empty string")
    return value


def _record_bytes(records: list[dict[str, Any]]) -> bytes:
    lines = [
        json.dumps(
            record,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        for record in records
    ]
    return ("\n".join(lines) + "\n").encode("utf-8") if lines else b""


def _read_source_records(path: Path, split: str):
    with path.open("r", encoding="utf-8", newline="") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if not raw_line.strip():
                raise ValueError(f"blank source line in {split} at line {line_number}")
            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"invalid JSON in {split} at line {line_number}: {error.msg}"
                ) from error
            if not isinstance(record, dict):
                raise TypeError(f"{split} line {line_number} must be a JSON object")
            yield line_number, record


def _source_metadata(source_manifest: dict[str, Any]) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    dataset = source_manifest.get("dataset")
    if not isinstance(dataset, dict):
        raise TypeError("source manifest dataset must be an object")
    dataset_id = dataset.get("id")
    revision = dataset.get("resolved_revision")
    parser_version = dataset.get("local_parser_version")
    if type(dataset_id) is not str or dataset_id != QASPER_DATASET_ID:
        raise ValueError("source manifest dataset ID is not allenai/qasper")
    if type(revision) is not str or _COMMIT_SHA_RE.fullmatch(revision) is None:
        raise ValueError("source manifest resolved revision must be a full commit SHA")
    if type(parser_version) is not int or parser_version < 1:
        raise ValueError("source manifest local parser version must be a positive integer")

    split_entries = source_manifest.get("splits")
    if not isinstance(split_entries, list):
        raise TypeError("source manifest splits must be a list")
    by_split = {entry["name"]: entry for entry in split_entries if isinstance(entry, dict)}
    if set(by_split) != set(SPLITS):
        raise ValueError("source manifest must describe train, validation, and test")
    split_files: dict[str, dict[str, Any]] = {}
    for split in SPLITS:
        entry = by_split[split]
        if (
            type(entry.get("rows")) is not int
            or entry["rows"] < 0
            or not _is_sha256(entry.get("sha256"))
        ):
            raise ValueError(f"source manifest has an invalid {split} entry")
        split_files[split] = {"rows": entry["rows"], "sha256": entry["sha256"]}
    return (
        {
            "dataset_id": dataset_id,
            "resolved_revision": revision,
            "local_parser_version": parser_version,
        },
        split_files,
    )


def _normalized_target_paths(
    papers_output: Path,
    qa_output: Path,
    manifest_output: Path,
) -> tuple[Path, Path, Path]:
    targets = tuple(Path(path).resolve(strict=False) for path in (papers_output, qa_output, manifest_output))
    if len(set(targets)) != 3:
        raise ValueError("papers, qa, and manifest output paths must be distinct")
    if len({target.parent for target in targets}) != 1:
        raise ValueError("papers, qa, and manifest outputs must share one parent directory")
    return targets


def _output_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink()


def _publish_outputs(payloads: list[tuple[Path, bytes]]) -> None:
    """Stage and verify every output, then publish the manifest last."""

    targets = [target for target, _ in payloads]
    if any(_output_exists(target) for target in targets):
        if not _output_exists(targets[-1]) and any(
            _output_exists(target) for target in targets[:-1]
        ):
            raise FileExistsError(
                "partial QASPER export found without a manifest; inspect existing files manually"
            )
        raise FileExistsError("one or more QASPER export outputs already exist")

    parent = targets[0].parent
    parent.mkdir(parents=True, exist_ok=True)
    staged = [(target.with_name(f"tmp_{target.name}"), target, data) for target, data in payloads]
    if any(_output_exists(temp) for temp, _, _ in staged):
        raise FileExistsError("a tmp_ export file already exists; inspect it manually")
    created: list[Path] = []
    try:
        for temporary, _, data in staged:
            with temporary.open("xb") as handle:
                created.append(temporary)
                handle.write(data)
        for temporary, target, expected in staged:
            observed = temporary.read_bytes()
            if observed != expected:
                raise OSError(f"staged bytes differ for {target.name}")
        staged_manifest = json.loads(staged[-1][0].read_text(encoding="utf-8"))
        _validate_export_manifest(staged_manifest)
        for key, (_, target, _) in zip(("papers", "qa"), staged[:2], strict=True):
            entry = staged_manifest["outputs"][key]
            payload = staged[0 if key == "papers" else 1][0].read_bytes()
            if entry["file"] != target.name or entry["sha256"] != _sha256_bytes(payload):
                raise OSError(f"staged {key} bytes do not match the export manifest")
            if payload and (
                not payload.endswith(b"\n") or payload.count(b"\n") != entry["rows"]
            ):
                raise OSError(f"staged {key} row count does not match the export manifest")
        canonical_manifest = (
            json.dumps(
                staged_manifest,
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
        if staged[-1][0].read_bytes() != canonical_manifest:
            raise OSError("staged export manifest is not deterministic JSON")
        for temporary, target, _ in staged:
            os.replace(temporary, target)
            if temporary in created:
                created.remove(temporary)
    except Exception:
        for temporary in created:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
        raise


def export_qasper(
    *,
    input_dir: Path,
    papers_output: Path,
    qa_output: Path,
    manifest_output: Path,
) -> dict[str, Any]:
    """Export all official source records into separate paper and question JSONL files."""

    papers_path, qa_path, manifest_path = _normalized_target_paths(
        papers_output, qa_output, manifest_output
    )
    if any(_output_exists(path) for path in (papers_path, qa_path, manifest_path)):
        if not _output_exists(manifest_path) and any(
            _output_exists(path) for path in (papers_path, qa_path)
        ):
            raise FileExistsError(
                "partial QASPER export found without a manifest; inspect existing files manually"
            )
        raise FileExistsError("one or more QASPER export outputs already exist")

    source_manifest, source_paths = _validate_input_files(Path(input_dir))
    source, split_files = _source_metadata(source_manifest)
    source_manifest_sha256 = _sha256_file(source_paths["manifest"])
    paper_records: list[dict[str, Any]] = []
    qa_records: list[dict[str, Any]] = []
    split_counts = {
        split: {"papers": 0, "questions": 0, "answer_annotations": 0}
        for split in SPLITS
    }
    seen_paper_ids: set[str] = set()
    seen_question_ids: set[str] = set()

    for split in SPLITS:
        for line_number, raw_record in _read_source_records(source_paths[split], split):
            if "source_split" in raw_record:
                raise ValueError(
                    f"{split} line {line_number}: source paper already contains source_split"
                )
            paper_id = _nonempty_identifier(
                raw_record.get("id"), field="id", split=split, line=line_number
            )
            if paper_id in seen_paper_ids:
                raise ValueError(f"duplicate paper ID at {split} line {line_number}")
            seen_paper_ids.add(paper_id)
            qas = raw_record.get("qas")
            if not isinstance(qas, list):
                raise TypeError(f"{split} line {line_number}: qas must be a list")

            paper = {key: value for key, value in raw_record.items() if key != "qas"}
            paper["source_split"] = split
            paper_records.append(paper)
            split_counts[split]["papers"] += 1

            for question_index, question_value in enumerate(qas):
                if not isinstance(question_value, dict):
                    raise TypeError(
                        f"{split} line {line_number}: question {question_index} must be an object"
                    )
                if "paper_id" in question_value or "source_split" in question_value:
                    raise ValueError(
                        f"{split} line {line_number}: question already contains an export field"
                    )
                if any(field in question_value for field in _PAPER_ONLY_FIELDS):
                    raise ValueError(
                        f"{split} line {line_number}: question contains a paper-only field"
                    )
                question_id = _nonempty_identifier(
                    question_value.get("question_id"),
                    field="question_id",
                    split=split,
                    line=line_number,
                )
                if question_id in seen_question_ids:
                    raise ValueError(f"duplicate question ID at {split} line {line_number}")
                seen_question_ids.add(question_id)
                answers = question_value.get("answers")
                if not isinstance(answers, list):
                    raise TypeError(
                        f"{split} line {line_number}: question answers must be a list"
                    )
                qa_record = dict(question_value)
                qa_record["paper_id"] = paper_id
                qa_record["source_split"] = split
                qa_records.append(qa_record)
                split_counts[split]["questions"] += 1
                split_counts[split]["answer_annotations"] += len(answers)

    papers_bytes = _record_bytes(paper_records)
    qa_bytes = _record_bytes(qa_records)
    manifest: dict[str, Any] = {
        "manifest_schema_version": 1,
        "artifact": "qasper_papers_and_qa",
        "source": {
            **source,
            "source_manifest_sha256": source_manifest_sha256,
            "split_files": split_files,
        },
        "outputs": {
            "papers": {
                "file": papers_path.name,
                "rows": len(paper_records),
                "sha256": _sha256_bytes(papers_bytes),
            },
            "qa": {
                "file": qa_path.name,
                "rows": len(qa_records),
                "sha256": _sha256_bytes(qa_bytes),
                "answer_annotation_count": sum(
                    counts["answer_annotations"] for counts in split_counts.values()
                ),
            },
        },
        "split_counts": split_counts,
        "split_policy_version": SPLIT_POLICY_VERSION,
    }
    manifest_bytes = (
        json.dumps(
            manifest,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")
    _publish_outputs(
        [
            (papers_path, papers_bytes),
            (qa_path, qa_bytes),
            (manifest_path, manifest_bytes),
        ]
    )
    return manifest


def _load_manifest(manifest_path: Path) -> dict[str, Any]:
    try:
        value = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"could not read export manifest: {error}") from error
    if not isinstance(value, dict):
        raise TypeError("export manifest must be a JSON object")
    return value


def _validate_export_manifest(manifest: dict[str, Any]) -> None:
    if type(manifest.get("manifest_schema_version")) is not int or manifest["manifest_schema_version"] != 1:
        raise ValueError("unsupported QASPER export manifest schema")
    if manifest.get("artifact") != "qasper_papers_and_qa":
        raise ValueError("manifest is not a QASPER papers and QA export")
    if manifest.get("split_policy_version") != SPLIT_POLICY_VERSION:
        raise ValueError("QASPER export split policy version is invalid")

    source = manifest.get("source")
    if not isinstance(source, dict):
        raise TypeError("export manifest source must be an object")
    if (
        type(source.get("dataset_id")) is not str
        or source["dataset_id"] != QASPER_DATASET_ID
        or type(source.get("resolved_revision")) is not str
        or _COMMIT_SHA_RE.fullmatch(source["resolved_revision"]) is None
        or type(source.get("local_parser_version")) is not int
        or source["local_parser_version"] < 1
        or not _is_sha256(source.get("source_manifest_sha256"))
    ):
        raise ValueError("export manifest source metadata is invalid")
    split_files = source.get("split_files")
    if not isinstance(split_files, dict) or set(split_files) != set(SPLITS):
        raise ValueError("export manifest must describe all three source split files")
    for split in SPLITS:
        entry = split_files[split]
        if (
            not isinstance(entry, dict)
            or type(entry.get("rows")) is not int
            or entry["rows"] < 0
            or not _is_sha256(entry.get("sha256"))
        ):
            raise ValueError(f"export manifest source entry for {split} is invalid")

    outputs = manifest.get("outputs")
    if not isinstance(outputs, dict) or set(outputs) != {"papers", "qa"}:
        raise ValueError("export manifest outputs must contain papers and qa")
    output_files: set[str] = set()
    for name in ("papers", "qa"):
        entry = outputs[name]
        if not isinstance(entry, dict):
            raise TypeError(f"export manifest {name} output must be an object")
        file_name = entry.get("file")
        if (
            type(file_name) is not str
            or not file_name
            or Path(file_name).name != file_name
            or file_name in {".", ".."}
            or type(entry.get("rows")) is not int
            or entry["rows"] < 0
            or not _is_sha256(entry.get("sha256"))
        ):
            raise ValueError(f"export manifest {name} output metadata is invalid")
        output_files.add(file_name)
    if len(output_files) != 2:
        raise ValueError("export manifest papers and QA filenames must differ")
    if type(outputs["qa"].get("answer_annotation_count")) is not int or outputs["qa"]["answer_annotation_count"] < 0:
        raise ValueError("export manifest QA annotation count is invalid")

    split_counts = manifest.get("split_counts")
    if not isinstance(split_counts, dict) or set(split_counts) != set(SPLITS):
        raise ValueError("export manifest must contain counts for all source splits")
    for split in SPLITS:
        counts = split_counts[split]
        if not isinstance(counts, dict) or set(counts) != {
            "papers",
            "questions",
            "answer_annotations",
        }:
            raise ValueError(f"export manifest counts for {split} are invalid")
        if any(type(counts[key]) is not int or counts[key] < 0 for key in counts):
            raise ValueError(f"export manifest counts for {split} must be non-negative integers")
        if counts["papers"] != split_files[split]["rows"]:
            raise ValueError(f"export manifest paper count differs from source rows for {split}")
    if sum(split_counts[split]["papers"] for split in SPLITS) != outputs["papers"]["rows"]:
        raise ValueError("export manifest total paper count is inconsistent")
    if sum(split_counts[split]["questions"] for split in SPLITS) != outputs["qa"]["rows"]:
        raise ValueError("export manifest total question count is inconsistent")
    if sum(split_counts[split]["answer_annotations"] for split in SPLITS) != outputs["qa"]["answer_annotation_count"]:
        raise ValueError("export manifest total answer annotation count is inconsistent")


def _read_export_jsonl(path: Path, *, expected_rows: int, label: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if not raw_line.endswith("\n") or raw_line.endswith("\r\n"):
                raise ValueError(f"{label} line {line_number} must end with LF")
            if raw_line == "\n":
                raise ValueError(f"blank {label} line {line_number}")
            try:
                value = json.loads(raw_line)
            except json.JSONDecodeError as error:
                raise ValueError(f"invalid JSON in {label} line {line_number}: {error.msg}") from error
            if not isinstance(value, dict):
                raise TypeError(f"{label} line {line_number} must be a JSON object")
            records.append(value)
    if len(records) != expected_rows:
        raise ValueError(f"{label} row count differs from manifest")
    return records


def _verified_manifest_for_files(
    *, papers_path: Path, qa_path: Path | None, manifest_path: Path
) -> dict[str, Any]:
    papers_path = Path(papers_path)
    manifest_path = Path(manifest_path)
    if papers_path.parent.resolve(strict=False) != manifest_path.parent.resolve(strict=False):
        raise ValueError("papers and export manifest must share one directory")
    manifest = _load_manifest(manifest_path)
    _validate_export_manifest(manifest)
    papers_entry = manifest["outputs"]["papers"]
    if papers_path.name != papers_entry["file"]:
        raise ValueError("papers filename differs from manifest")
    if _sha256_file(papers_path) != papers_entry["sha256"]:
        raise ValueError("papers SHA-256 differs from manifest")
    if qa_path is not None:
        qa_path = Path(qa_path)
        if qa_path.parent.resolve(strict=False) != manifest_path.parent.resolve(strict=False):
            raise ValueError("papers, QA, and export manifest must share one directory")
        qa_entry = manifest["outputs"]["qa"]
        if qa_path.name != qa_entry["file"]:
            raise ValueError("QA filename differs from manifest")
        if _sha256_file(qa_path) != qa_entry["sha256"]:
            raise ValueError("QA SHA-256 differs from manifest")
    return manifest


def load_verified_papers(
    *, papers_path: Path, manifest_path: Path
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Verify and load paper-only export records without opening the QA file."""

    manifest = _verified_manifest_for_files(
        papers_path=Path(papers_path), qa_path=None, manifest_path=Path(manifest_path)
    )
    papers = _read_export_jsonl(
        Path(papers_path),
        expected_rows=manifest["outputs"]["papers"]["rows"],
        label="papers",
    )
    observed_counts = Counter()
    seen_paper_ids: set[str] = set()
    for line_number, paper in enumerate(papers, start=1):
        if "qas" in paper:
            raise ValueError(f"papers line {line_number} contains qas")
        paper_id = _nonempty_identifier(
            paper.get("id"), field="id", split="papers", line=line_number
        )
        if paper_id in seen_paper_ids:
            raise ValueError(f"duplicate paper ID in papers line {line_number}")
        seen_paper_ids.add(paper_id)
        split = paper.get("source_split")
        if split not in SPLITS:
            raise ValueError(f"invalid source_split in papers line {line_number}")
        observed_counts[split] += 1
    for split in SPLITS:
        if observed_counts[split] != manifest["split_counts"][split]["papers"]:
            raise ValueError(f"papers count differs from manifest for {split}")
    return manifest, papers


def check_qasper_export(
    *, papers_path: Path, qa_path: Path, manifest_path: Path
) -> dict[str, Any]:
    """Independently verify exported bytes, records, counts, and paper/question links."""

    manifest = _verified_manifest_for_files(
        papers_path=Path(papers_path), qa_path=Path(qa_path), manifest_path=Path(manifest_path)
    )
    papers = _read_export_jsonl(
        Path(papers_path),
        expected_rows=manifest["outputs"]["papers"]["rows"],
        label="papers",
    )
    qa_records = _read_export_jsonl(
        Path(qa_path), expected_rows=manifest["outputs"]["qa"]["rows"], label="QA"
    )
    paper_splits: dict[str, str] = {}
    paper_counts = Counter()
    for line_number, paper in enumerate(papers, start=1):
        if "qas" in paper:
            raise ValueError(f"papers line {line_number} contains qas")
        paper_id = _nonempty_identifier(
            paper.get("id"), field="id", split="papers", line=line_number
        )
        if paper_id in paper_splits:
            raise ValueError(f"duplicate paper ID in papers line {line_number}")
        split = paper.get("source_split")
        if split not in SPLITS:
            raise ValueError(f"invalid source_split in papers line {line_number}")
        paper_splits[paper_id] = split
        paper_counts[split] += 1

    question_ids: set[str] = set()
    question_counts = Counter()
    annotation_counts = Counter()
    for line_number, question in enumerate(qa_records, start=1):
        if any(field in question for field in _PAPER_ONLY_FIELDS):
            raise ValueError(f"QA line {line_number} contains a paper-only field")
        question_id = _nonempty_identifier(
            question.get("question_id"), field="question_id", split="QA", line=line_number
        )
        if question_id in question_ids:
            raise ValueError(f"duplicate question ID in QA line {line_number}")
        question_ids.add(question_id)
        paper_id = _nonempty_identifier(
            question.get("paper_id"), field="paper_id", split="QA", line=line_number
        )
        if paper_id not in paper_splits:
            raise ValueError(f"QA line {line_number} references an unknown paper")
        split = question.get("source_split")
        if split not in SPLITS or split != paper_splits[paper_id]:
            raise ValueError(f"QA source_split differs from linked paper at line {line_number}")
        answers = question.get("answers")
        if not isinstance(answers, list):
            raise TypeError(f"QA line {line_number} answers must be a list")
        question_counts[split] += 1
        annotation_counts[split] += len(answers)

    for split in SPLITS:
        expected = manifest["split_counts"][split]
        if paper_counts[split] != expected["papers"]:
            raise ValueError(f"paper count differs from manifest for {split}")
        if question_counts[split] != expected["questions"]:
            raise ValueError(f"question count differs from manifest for {split}")
        if annotation_counts[split] != expected["answer_annotations"]:
            raise ValueError(f"answer annotation count differs from manifest for {split}")

    return {
        "papers": {
            "rows": len(papers),
            "sha256": manifest["outputs"]["papers"]["sha256"],
        },
        "qa": {
            "rows": len(qa_records),
            "sha256": manifest["outputs"]["qa"]["sha256"],
            "answer_annotation_count": sum(annotation_counts.values()),
        },
        "split_counts": {
            split: {
                "papers": paper_counts[split],
                "questions": question_counts[split],
                "answer_annotations": annotation_counts[split],
            }
            for split in SPLITS
        },
    }
