"""Offline structural inspection for the published QASPER acquisition."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path
from typing import Any

EXPECTED_FILES = ("manifest.json", "train.jsonl", "validation.jsonl", "test.jsonl")
SPLIT_NAMES = ("train", "validation", "test")
TOP_LEVEL_TYPES: dict[str, type] = {
    "id": str,
    "title": str,
    "abstract": str,
    "full_text": list,
    "qas": list,
    "figures_and_tables": list,
}
ANNOTATION_TYPES = {"annotation_id": str, "worker_id": str, "answer": dict}
ANSWER_TYPES = {
    "unanswerable": bool,
    "yes_no": bool,
    "extractive_spans": list,
    "free_form_answer": str,
    "evidence": list,
    "highlighted_evidence": list,
}
_FLOAT_SELECTED_RE = re.compile(r"^FLOAT SELECTED(?P<separator>[^A-Za-z0-9]*)")


class QasperInspectionError(ValueError):
    """Raised when the published acquisition cannot be inspected safely."""


class _AnomalyCounter:
    """Count anomaly categories and retain at most ten stable coordinates each."""

    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()
        self.locations: dict[str, list[dict[str, Any]]] = defaultdict(list)

    def add(self, category: str, location: Mapping[str, Any]) -> None:
        self.counts[category] += 1
        if len(self.locations[category]) < 10:
            self.locations[category].append(dict(location))

    def report(self) -> dict[str, Any]:
        categories = sorted(set(self.counts) | set(self.locations))
        return {
            category: {
                "count": self.counts.get(category, 0),
                "locations": sorted(
                    self.locations.get(category, []), key=_location_sort_key
                ),
            }
            for category in categories
        }


class _EvidenceCounter:
    """Accumulate evidence item statistics without retaining evidence text."""

    def __init__(self) -> None:
        self.total_items = 0
        self.blank_items = 0
        self.non_string_items = 0
        self.annotation_count = 0
        self.float_selected_hits = 0
        self.prefix_forms: set[str] = set()
        self.hit_papers: set[str] = set()
        self.hit_paper_figures: dict[str, int] = {}
        self.anomaly_locations: dict[str, list[dict[str, Any]]] = defaultdict(list)

    def add_location(self, category: str, location: Mapping[str, Any]) -> None:
        if len(self.anomaly_locations[category]) < 10:
            self.anomaly_locations[category].append(dict(location))

    def report(self) -> dict[str, Any]:
        return {
            "total_items": self.total_items,
            "blank_items": self.blank_items,
            "non_string_items": self.non_string_items,
            "annotations_with_items": self.annotation_count,
            "float_selected_hits": self.float_selected_hits,
            "float_selected_prefix_forms": sorted(self.prefix_forms),
            "hit_paper_count": len(self.hit_papers),
            "figures_and_tables_items_in_hit_papers": sum(
                self.hit_paper_figures.values()
            ),
            "anomaly_locations": {
                category: sorted(locations, key=_location_sort_key)
                for category, locations in sorted(self.anomaly_locations.items())
            },
        }


def _location_sort_key(location: Mapping[str, Any]) -> tuple[Any, ...]:
    """Return a stable sort key for a diagnostic coordinate."""

    return (
        str(location.get("split", "")),
        str(location.get("paper_id", "")),
        int(location.get("line_number", 0)),
        int(location.get("section_index", -1)),
        int(location.get("paragraph_index", -1)),
        int(location.get("question_index", -1)),
        int(location.get("answer_index", -1)),
        str(location.get("question_id", "")),
        str(location.get("field", "")),
    )


def _location(
    split: str,
    line_number: int,
    paper_id: object,
    **indices: int | str,
) -> dict[str, Any]:
    """Build a coordinate that never contains source text."""

    return {
        "split": split,
        "line_number": line_number,
        "paper_id": paper_id if isinstance(paper_id, str) else None,
        **indices,
    }


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_empty(value: object) -> bool:
    return (isinstance(value, str) and value == "") or (
        isinstance(value, list) and len(value) == 0
    )


def _record_field(
    record: Mapping[str, Any],
    field: str,
    expected_type: type,
    counter: _AnomalyCounter,
    location: Mapping[str, Any],
    *,
    allow_null: bool = False,
) -> object:
    """Record the four field states and return the raw value."""

    field_location = {**location, "field": field}
    if field not in record:
        counter.add("missing_key", field_location)
        return _MISSING
    value = record[field]
    if value is None:
        counter.add("null", field_location)
        return value
    if not isinstance(value, expected_type):
        counter.add("wrong_type", field_location)
        return value
    if _is_empty(value):
        counter.add("empty", field_location)
    return value


def _record_top_fields(
    record: Mapping[str, Any],
    counter_by_field: Mapping[str, _AnomalyCounter],
    location: Mapping[str, Any],
) -> None:
    for field, expected_type in TOP_LEVEL_TYPES.items():
        _record_field(record, field, expected_type, counter_by_field[field], location)


def _counter_report(counter_by_name: Mapping[str, _AnomalyCounter]) -> dict[str, Any]:
    return {name: counter.report() for name, counter in sorted(counter_by_name.items())}


def _merge_counter(target: _AnomalyCounter, source: _AnomalyCounter) -> None:
    for category, count in source.counts.items():
        target.counts[category] += count
    for category, locations in source.locations.items():
        remaining = 10 - len(target.locations[category])
        if remaining > 0:
            target.locations[category].extend(locations[:remaining])


def _new_counter_map(names: Iterable[str]) -> dict[str, _AnomalyCounter]:
    return {name: _AnomalyCounter() for name in names}


def _validate_input_files(input_dir: Path) -> tuple[dict[str, Any], dict[str, Path]]:
    if not input_dir.is_dir() or input_dir.is_symlink():
        raise QasperInspectionError(f"Input directory is not a regular directory: {input_dir}")

    entries = list(input_dir.iterdir())
    if {entry.name for entry in entries} != set(EXPECTED_FILES):
        actual = sorted(entry.name for entry in entries)
        raise QasperInspectionError(
            f"Input directory must contain exactly {list(EXPECTED_FILES)!r}; got {actual!r}"
        )
    if any(not entry.is_file() or entry.is_symlink() for entry in entries):
        raise QasperInspectionError("QASPER input files must be regular files")

    manifest_path = input_dir / "manifest.json"
    try:
        with manifest_path.open(encoding="utf-8") as handle:
            manifest = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise QasperInspectionError(f"Could not parse manifest.json: {error}") from error
    if not isinstance(manifest, dict):
        raise QasperInspectionError("manifest.json must contain a JSON object")

    split_entries = manifest.get("splits")
    if not isinstance(split_entries, list):
        raise QasperInspectionError("manifest.json must contain a splits list")
    if [entry.get("name") for entry in split_entries if isinstance(entry, dict)] != list(
        SPLIT_NAMES
    ) or len(split_entries) != len(SPLIT_NAMES):
        raise QasperInspectionError("manifest split names must be train, validation, test")

    paths: dict[str, Path] = {"manifest": manifest_path}
    for entry in split_entries:
        if not isinstance(entry, dict):
            raise QasperInspectionError("manifest split entries must be objects")
        name = entry.get("name")
        file_name = entry.get("file")
        rows = entry.get("rows")
        expected_sha256 = entry.get("sha256")
        if (
            name not in SPLIT_NAMES
            or file_name != f"{name}.jsonl"
            or not isinstance(rows, int)
            or rows < 0
            or not isinstance(expected_sha256, str)
            or len(expected_sha256) != 64
        ):
            raise QasperInspectionError(f"Invalid manifest entry for split {name!r}")
        path = input_dir / file_name
        observed_sha256 = _file_sha256(path)
        if observed_sha256 != expected_sha256:
            raise QasperInspectionError(
                f"SHA-256 mismatch for {file_name}: expected {expected_sha256}, "
                f"observed {observed_sha256}"
            )
        paths[name] = path
        actual_rows = _count_nonempty_lines(path)
        if actual_rows != rows:
            raise QasperInspectionError(
                f"Row-count mismatch for {file_name}: expected {rows}, observed {actual_rows}"
            )
    return manifest, paths


def _count_nonempty_lines(path: Path) -> int:
    count = 0
    with path.open(encoding="utf-8", newline="") as handle:
        for line in handle:
            if line.strip():
                count += 1
    return count


def _read_records(path: Path, split: str) -> list[tuple[int, dict[str, Any]]]:
    records: list[tuple[int, dict[str, Any]]] = []
    with path.open(encoding="utf-8", newline="") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if not raw_line.strip():
                continue
            try:
                value = json.loads(raw_line)
            except json.JSONDecodeError as error:
                raise QasperInspectionError(
                    f"Invalid JSON in split {split!r}, line {line_number}: {error.msg}"
                ) from error
            if not isinstance(value, dict):
                raise QasperInspectionError(
                    f"Top-level record is not an object in split {split!r}, "
                    f"line {line_number}"
                )
            records.append((line_number, value))
    return records


def _prefix_form(value: str) -> str:
    match = _FLOAT_SELECTED_RE.match(value.lstrip())
    if match is None:
        return ""
    return f"FLOAT SELECTED{match.group('separator')[:20]}"


def _inspect_evidence(
    value: object,
    field: str,
    evidence: _EvidenceCounter,
    location: Mapping[str, Any],
    *,
    paper_id: object,
    figures_and_tables_count: int,
) -> None:
    if not isinstance(value, list):
        return
    if value:
        evidence.annotation_count += 1
    for item_index, item in enumerate(value):
        evidence.total_items += 1
        item_location = {**location, "field": field, "item_index": item_index}
        if not isinstance(item, str):
            evidence.non_string_items += 1
            evidence.add_location("non_string_item", item_location)
            continue
        if item.strip() == "":
            evidence.blank_items += 1
            evidence.add_location("blank_item", item_location)
            continue
        stripped = item.lstrip()
        if stripped.startswith("FLOAT SELECTED"):
            evidence.float_selected_hits += 1
            evidence.prefix_forms.add(_prefix_form(item))
            evidence.add_location("float_selected_hit", item_location)
            if isinstance(paper_id, str) and paper_id:
                evidence.hit_papers.add(paper_id)
                evidence.hit_paper_figures[paper_id] = figures_and_tables_count


def _answer_payload_flags(payload: Mapping[str, Any]) -> tuple[str, set[str]]:
    valid: set[str] = set()
    if payload.get("unanswerable") is True:
        valid.add("unanswerable")
    if isinstance(payload.get("yes_no"), bool):
        valid.add("yes_no")
    spans = payload.get("extractive_spans")
    if isinstance(spans, list) and any(
        isinstance(span, str) and span.strip() for span in spans
    ):
        valid.add("extractive")
    free_form = payload.get("free_form_answer")
    if isinstance(free_form, str) and free_form.strip():
        valid.add("free_form")

    if payload.get("unanswerable") is True:
        answer_type = "unanswerable"
    elif isinstance(payload.get("yes_no"), bool):
        answer_type = "yes_no"
    elif "extractive" in valid:
        answer_type = "extractive"
    elif "free_form" in valid:
        answer_type = "free_form"
    else:
        answer_type = "invalid_or_empty"
    return answer_type, valid


def _sorted_intersection(values: Mapping[str, set[str]], left: str, right: str) -> list[str]:
    return sorted(values[left] & values[right])


def _stats(values: Sequence[int]) -> dict[str, int | None]:
    if not values:
        return {"min": None, "median": None, "max": None}
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        median: int | float = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    return {"min": ordered[0], "median": median, "max": ordered[-1]}


_MISSING = object()


def inspect_qasper(input_dir: Path | str) -> dict[str, Any]:
    """Inspect a complete local acquisition and return a deterministic report."""

    manifest, paths = _validate_input_files(Path(input_dir))
    per_split: dict[str, dict[str, Any]] = {}
    field_counters_global = _new_counter_map(TOP_LEVEL_TYPES)
    section_counters_global = _new_counter_map(
        (
            "chapter_item",
            "section_name",
            "paragraphs",
            "section_name_blank",
            "paragraph_blank",
            "zero_paragraph_chapter",
            "paragraph_item",
        )
    )
    question_counters_global = _new_counter_map(
        (
            "question_item",
            "question",
            "question_id",
            "answers",
            "annotation",
            "answer_payload",
        )
    )
    answer_field_counters_global = _new_counter_map(
        (*ANNOTATION_TYPES.keys(), *ANSWER_TYPES.keys())
    )
    answer_types_global: Counter[str] = Counter()
    evidence_global = {name: _EvidenceCounter() for name in ("evidence", "highlighted_evidence")}
    paper_sets: dict[str, set[str]] = {split: set() for split in SPLIT_NAMES}
    question_sets: dict[str, set[str]] = {split: set() for split in SPLIT_NAMES}
    paper_id_occurrences: dict[str, list[dict[str, Any]]] = {
        split: [] for split in SPLIT_NAMES
    }
    question_id_occurrences: dict[str, list[dict[str, Any]]] = {
        split: [] for split in SPLIT_NAMES
    }
    paragraph_occurrences: dict[str, list[tuple[str, str, dict[str, Any]]]] = defaultdict(list)

    for split in SPLIT_NAMES:
        records = _read_records(paths[split], split)
        field_counters = _new_counter_map(TOP_LEVEL_TYPES)
        section_counters = _new_counter_map(section_counters_global)
        question_counters = _new_counter_map(question_counters_global)
        answer_field_counters = _new_counter_map(answer_field_counters_global)
        answer_types: Counter[str] = Counter()
        evidence = {name: _EvidenceCounter() for name in evidence_global}
        paper_ids: Counter[str] = Counter()
        question_ids: Counter[str] = Counter()
        question_annotation_counts: list[int] = []
        question_count = 0
        answer_annotation_count = 0
        chapter_count = 0
        paragraph_count = 0
        paragraph_string_count = 0

        for line_number, record in records:
            paper_id = record.get("id")
            row_location = _location(split, line_number, paper_id)
            _record_top_fields(record, field_counters, row_location)
            for field, expected_type in TOP_LEVEL_TYPES.items():
                _record_field(
                    record,
                    field,
                    expected_type,
                    field_counters_global[field],
                    row_location,
                )

            if isinstance(paper_id, str) and paper_id:
                paper_ids[paper_id] += 1
                paper_sets[split].add(paper_id)
                paper_id_occurrences[split].append(row_location)

            figures = record.get("figures_and_tables")
            figures_count = len(figures) if isinstance(figures, list) else 0

            full_text = record.get("full_text")
            if isinstance(full_text, list):
                chapter_count += len(full_text)
                for section_index, section in enumerate(full_text):
                    section_location = {
                        **row_location,
                        "section_index": section_index,
                    }
                    if not isinstance(section, dict):
                        section_counters["chapter_item"].add(
                            "wrong_type", section_location
                        )
                        _merge_counter(section_counters_global["chapter_item"], _single_counter("wrong_type", section_location))
                        continue

                    section_name = _record_field(
                        section,
                        "section_name",
                        str,
                        section_counters["section_name"],
                        section_location,
                    )
                    paragraphs = _record_field(
                        section,
                        "paragraphs",
                        list,
                        section_counters["paragraphs"],
                        section_location,
                    )
                    _record_field(
                        section,
                        "section_name",
                        str,
                        section_counters_global["section_name"],
                        section_location,
                    )
                    _record_field(
                        section,
                        "paragraphs",
                        list,
                        section_counters_global["paragraphs"],
                        section_location,
                    )
                    if isinstance(section_name, str) and section_name.strip() == "":
                        section_counters["section_name_blank"].add(
                            "blank", section_location
                        )
                        section_counters_global["section_name_blank"].add(
                            "blank", section_location
                        )
                    if not isinstance(paragraphs, list):
                        continue
                    if not paragraphs:
                        section_counters["zero_paragraph_chapter"].add(
                            "zero", section_location
                        )
                        section_counters_global["zero_paragraph_chapter"].add(
                            "zero", section_location
                        )
                    paragraph_count += len(paragraphs)
                    for paragraph_index, paragraph in enumerate(paragraphs):
                        paragraph_location = {
                            **section_location,
                            "paragraph_index": paragraph_index,
                        }
                        if not isinstance(paragraph, str):
                            section_counters["paragraph_item"].add(
                                "wrong_type", paragraph_location
                            )
                            section_counters_global["paragraph_item"].add(
                                "wrong_type", paragraph_location
                            )
                            continue
                        paragraph_string_count += 1
                        if paragraph.strip() == "":
                            section_counters["paragraph_blank"].add(
                                "blank", paragraph_location
                            )
                            section_counters_global["paragraph_blank"].add(
                                "blank", paragraph_location
                            )
                            continue
                        if isinstance(paper_id, str) and paper_id:
                            paragraph_occurrences[paragraph.strip()].append(
                                (split, paper_id, paragraph_location)
                            )

            qas = record.get("qas")
            if not isinstance(qas, list):
                pass
            else:
                question_count += len(qas)
                for question_index, question in enumerate(qas):
                    question_location = {
                        **row_location,
                        "question_index": question_index,
                    }
                    if not isinstance(question, dict):
                        question_counters["question_item"].add(
                            "wrong_type", question_location
                        )
                        question_counters_global["question_item"].add(
                            "wrong_type", question_location
                        )
                        question_annotation_counts.append(0)
                        continue
                    question_value = _record_field(
                        question,
                        "question",
                        str,
                        question_counters["question"],
                        question_location,
                    )
                    question_id = _record_field(
                        question,
                        "question_id",
                        str,
                        question_counters["question_id"],
                        question_location,
                    )
                    question_location["question_id"] = (
                        question_id if isinstance(question_id, str) else None
                    )
                    answers = _record_field(
                        question,
                        "answers",
                        list,
                        question_counters["answers"],
                        question_location,
                    )
                    _record_field(question, "question", str, question_counters_global["question"], question_location)
                    _record_field(question, "question_id", str, question_counters_global["question_id"], question_location)
                    _record_field(question, "answers", list, question_counters_global["answers"], question_location)
                    if isinstance(question_value, str) and question_value.strip() == "":
                        question_counters["question"].add("blank", question_location)
                        question_counters_global["question"].add("blank", question_location)
                    if isinstance(question_id, str):
                        if question_id.strip() == "":
                            question_counters["question_id"].add("blank", question_location)
                            question_counters_global["question_id"].add("blank", question_location)
                        else:
                            question_ids[question_id] += 1
                            question_sets[split].add(question_id)
                            question_id_occurrences[split].append(question_location)
                    if not isinstance(answers, list):
                        question_annotation_counts.append(0)
                        question_counters["answers"].add("no_answer_annotations", question_location)
                        question_counters_global["answers"].add("no_answer_annotations", question_location)
                        continue
                    question_annotation_counts.append(len(answers))
                    if not answers:
                        question_counters["answers"].add("no_answer_annotations", question_location)
                        question_counters_global["answers"].add("no_answer_annotations", question_location)
                    answer_annotation_count += len(answers)
                    for answer_index, annotation in enumerate(answers):
                        annotation_location = {
                            **question_location,
                            "answer_index": answer_index,
                        }
                        if not isinstance(annotation, dict):
                            question_counters["annotation"].add("wrong_type", annotation_location)
                            question_counters_global["annotation"].add("wrong_type", annotation_location)
                            answer_types["invalid_or_empty"] += 1
                            answer_types_global["invalid_or_empty"] += 1
                            continue
                        annotation_answer = _record_field(
                            annotation,
                            "answer",
                            dict,
                            answer_field_counters["answer"],
                            annotation_location,
                        )
                        for field, expected_type in ANNOTATION_TYPES.items():
                            if field != "answer":
                                _record_field(annotation, field, expected_type, answer_field_counters[field], annotation_location)
                            _record_field(annotation, field, expected_type, answer_field_counters_global[field], annotation_location)
                        if not isinstance(annotation_answer, dict):
                            question_counters["answer_payload"].add("wrong_type", annotation_location)
                            question_counters_global["answer_payload"].add("wrong_type", annotation_location)
                            answer_types["invalid_or_empty"] += 1
                            answer_types_global["invalid_or_empty"] += 1
                            continue
                        for field, expected_type in ANSWER_TYPES.items():
                            _record_field(annotation_answer, field, expected_type, answer_field_counters[field], annotation_location, allow_null=field == "yes_no")
                            _record_field(annotation_answer, field, expected_type, answer_field_counters_global[field], annotation_location, allow_null=field == "yes_no")
                        answer_type, valid_payloads = _answer_payload_flags(annotation_answer)
                        answer_types[answer_type] += 1
                        answer_types_global[answer_type] += 1
                        if len(valid_payloads) > 1:
                            question_counters["answer_payload"].add("ambiguous_payload", annotation_location)
                            question_counters_global["answer_payload"].add("ambiguous_payload", annotation_location)
                        for evidence_field, evidence_counter in evidence.items():
                            evidence_value = annotation_answer.get(evidence_field)
                            _inspect_evidence(
                                evidence_value,
                                evidence_field,
                                evidence_counter,
                                annotation_location,
                                paper_id=paper_id,
                                figures_and_tables_count=figures_count,
                            )
                            _inspect_evidence(
                                evidence_value,
                                evidence_field,
                                evidence_global[evidence_field],
                                annotation_location,
                                paper_id=paper_id,
                                figures_and_tables_count=figures_count,
                            )

            if qas is None or not isinstance(qas, list):
                question_count += 0

        duplicate_paper_ids = sorted(paper_id for paper_id, count in paper_ids.items() if count > 1)
        duplicate_question_ids = sorted(qid for qid, count in question_ids.items() if count > 1)
        for paper_id in duplicate_paper_ids:
            locations = [loc for loc in paper_id_occurrences[split] if loc.get("paper_id") == paper_id]
            for duplicate_location in locations[1:]:
                field_counters["id"].add("duplicate_paper_id", duplicate_location)
                field_counters_global["id"].add("duplicate_paper_id", duplicate_location)
        for question_id in duplicate_question_ids:
            locations = [
                loc
                for loc in question_id_occurrences[split]
                if loc.get("question_id") == question_id
            ]
            for duplicate_location in locations[1:]:
                question_counters["question_id"].add("duplicate", duplicate_location)
                question_counters_global["question_id"].add("duplicate", duplicate_location)

        for counter_map in (field_counters, section_counters, question_counters, answer_field_counters):
            for counter in counter_map.values():
                for category, locations in counter.locations.items():
                    counter.locations[category] = sorted(locations, key=_location_sort_key)[:10]

        per_split[split] = {
            "paper_count": len(records),
            "question_count": question_count,
            "answer_annotation_count": answer_annotation_count,
            "unique_paper_id_count": len(paper_ids),
            "duplicate_paper_id_count": len(duplicate_paper_ids),
            "duplicate_paper_id_values": duplicate_paper_ids,
            "unique_question_id_count": len(question_ids),
            "duplicate_question_id_count": len(duplicate_question_ids),
            "duplicate_question_id_values": duplicate_question_ids,
            "question_annotation_count_stats": _stats(question_annotation_counts),
            "ambiguous_payload_count": question_counters["answer_payload"].counts.get(
                "ambiguous_payload", 0
            ),
            "chapters": {
                "chapter_count": chapter_count,
                "paragraph_count": paragraph_count,
                "paragraph_string_count": paragraph_string_count,
                "anomalies": _counter_report(section_counters),
            },
            "question_anomalies": _counter_report(question_counters),
            "answer_field_anomalies": _counter_report(answer_field_counters),
            "answer_types": dict(sorted(answer_types.items())),
            "evidence": {name: counter.report() for name, counter in evidence.items()},
            "field_anomalies": _counter_report(field_counters),
        }

    all_paper_ids = set().union(*paper_sets.values())
    all_question_ids = set().union(*question_sets.values())
    global_totals = {
        "paper_count": sum(item["paper_count"] for item in per_split.values()),
        "question_count": sum(item["question_count"] for item in per_split.values()),
        "answer_annotation_count": sum(
            item["answer_annotation_count"] for item in per_split.values()
        ),
        "unique_paper_id_count": len(all_paper_ids),
        "unique_question_id_count": len(all_question_ids),
        "chapter_count": sum(item["chapters"]["chapter_count"] for item in per_split.values()),
        "paragraph_count": sum(item["chapters"]["paragraph_count"] for item in per_split.values()),
        "paragraph_string_count": sum(
            item["chapters"]["paragraph_string_count"] for item in per_split.values()
        ),
    }

    same_paper_groups: list[list[tuple[str, str, dict[str, Any]]]] = []
    grouped_by_paper: dict[tuple[str, str], list[tuple[str, str, dict[str, Any]]]] = defaultdict(list)
    for paragraph, occurrences in paragraph_occurrences.items():
        for occurrence in occurrences:
            grouped_by_paper[(occurrence[1], paragraph)].append(occurrence)
    for group in grouped_by_paper.values():
        if len(group) > 1:
            same_paper_groups.append(group)
    cross_paper_groups = [
        occurrences
        for occurrences in paragraph_occurrences.values()
        if len({occurrence[1] for occurrence in occurrences}) > 1
    ]

    def duplicate_examples(groups: Sequence[list[tuple[str, str, dict[str, Any]]]]) -> list[dict[str, Any]]:
        examples: list[dict[str, Any]] = []
        for group in groups[:10]:
            examples.append(
                {
                    "occurrence_count": len(group),
                    "paper_id_count": len({item[1] for item in group}),
                    "locations": sorted(
                        (item[2] for item in group), key=_location_sort_key
                    )[:10],
                }
            )
        return examples

    duplicate_paragraphs = {
        "same_paper": {
            "duplicate_group_count": len(same_paper_groups),
            "involved_paragraph_count": sum(len(group) for group in same_paper_groups),
            "examples": duplicate_examples(same_paper_groups),
        },
        "cross_paper": {
            "duplicate_group_count": len(cross_paper_groups),
            "involved_paragraph_count": sum(len(group) for group in cross_paper_groups),
            "involved_paper_count": len(
                {item[1] for group in cross_paper_groups for item in group}
            ),
            "examples": duplicate_examples(cross_paper_groups),
        },
    }

    paper_id_intersections = {
            f"{left}_and_{right}": _sorted_intersection(paper_sets, left, right)
            for left, right in (("train", "validation"), ("train", "test"), ("validation", "test"))
        }
    question_id_intersections = {
            f"{left}_and_{right}": _sorted_intersection(question_sets, left, right)
            for left, right in (("train", "validation"), ("train", "test"), ("validation", "test"))
        }
    split_overlap: dict[str, Any] = {
        "paper_id_intersections": paper_id_intersections,
        "question_id_intersections": question_id_intersections,
        "within_split_duplicate_paper_ids": {
            split: per_split[split]["duplicate_paper_id_values"] for split in SPLIT_NAMES
        },
        "observed_paper_disjoint": all(
            not split_overlap_value
            for split_overlap_value in paper_id_intersections.values()
        )
        and all(
            not per_split[split]["duplicate_paper_id_values"] for split in SPLIT_NAMES
        ),
    }

    manifest_dataset = manifest.get("dataset", {})
    licenses = manifest.get("licenses", {})
    input_hashes = {
        f"{split}.jsonl": {
            "bytes": paths[split].stat().st_size,
            "sha256": _file_sha256(paths[split]),
            "rows": per_split[split]["paper_count"],
        }
        for split in SPLIT_NAMES
    }
    counting_definitions = {
        "paper_count": "Number of successfully parsed non-empty JSONL lines.",
        "question_count": "Sum of the length of each paper's qas list.",
        "answer_annotation_count": "Sum of the length of each question's answers list; fields or evidence items inside one annotation are not separate annotations.",
        "paragraph_duplicate_key": "paragraph.strip(), preserving case, internal whitespace, punctuation, and Unicode; blank paragraphs are excluded.",
        "answer_type_precedence": "unanswerable is True, then boolean yes_no, then a non-empty extractive span, then non-blank free_form_answer, otherwise invalid_or_empty.",
        "chapter_and_paragraph_counts": "chapter_count counts full_text list items; paragraph_count counts entries in list-typed paragraphs fields, including blank and non-string entries; paragraph_string_count counts string entries only.",
        "unique_id_counts": "Only non-blank string id and question_id values are included in unique-ID sets; malformed values remain in anomaly counts.",
    }
    open_decisions = [
        "Official split names are reported as observed and are not automatically mapped to development, validation, or held-out policy.",
        "FLOAT SELECTED evidence is reported as an observed string prefix; no mapping to a specific figure or table is inferred.",
        "Passage schema, section-boundary policy, and answer/evidence normalization remain Step 4 decisions.",
    ]
    if not split_overlap["observed_paper_disjoint"]:
        open_decisions.append(
            "Paper-level split disjointness is not observed; leakage must be reviewed before adopting a split policy."
        )
    if sum(
        item.get("answer_types", {}).get("invalid_or_empty", 0)
        for item in per_split.values()
    ):
        open_decisions.append(
            "Invalid or empty answer payloads were observed and are not silently repaired."
        )

    report = {
        "provenance": {
            "dataset_id": manifest_dataset.get("id"),
            "config": manifest_dataset.get("config"),
            "source_dataset_version": manifest_dataset.get("source_dataset_version"),
            "requested_revision": manifest_dataset.get("requested_revision"),
            "resolved_revision": manifest_dataset.get("resolved_revision"),
            "manifest_schema_version": manifest.get("manifest_schema_version"),
            "licenses": licenses,
            "input_files": input_hashes,
        },
        "counting_definitions": counting_definitions,
        "per_split": per_split,
        "global_totals": global_totals,
        "field_anomalies": {
            "per_split": {split: per_split[split]["field_anomalies"] for split in SPLIT_NAMES},
            "global": _counter_report(field_counters_global),
        },
        "section_anomalies": {
            "per_split": {split: per_split[split]["chapters"]["anomalies"] for split in SPLIT_NAMES},
            "global": _counter_report(section_counters_global),
        },
        "question_anomalies": {
            "per_split": {split: per_split[split]["question_anomalies"] for split in SPLIT_NAMES},
            "global": _counter_report(question_counters_global),
        },
        "answer_field_anomalies": {
            "per_split": {split: per_split[split]["answer_field_anomalies"] for split in SPLIT_NAMES},
            "global": _counter_report(answer_field_counters_global),
        },
        "answer_types": {
            "per_split": {split: per_split[split]["answer_types"] for split in SPLIT_NAMES},
            "global": dict(sorted(answer_types_global.items())),
        },
        "ambiguous_payload": {
            "per_split": {
                split: per_split[split]["ambiguous_payload_count"]
                for split in SPLIT_NAMES
            },
            "global": question_counters_global["answer_payload"].counts.get(
                "ambiguous_payload", 0
            ),
        },
        "evidence": {
            "per_split": {split: per_split[split]["evidence"] for split in SPLIT_NAMES},
            "global": {name: counter.report() for name, counter in evidence_global.items()},
        },
        "duplicate_paragraphs": duplicate_paragraphs,
        "split_overlap": split_overlap,
        "open_decisions": open_decisions,
    }
    return report


def _single_counter(category: str, location: Mapping[str, Any]) -> _AnomalyCounter:
    counter = _AnomalyCounter()
    counter.add(category, location)
    return counter


def write_report(report: Mapping[str, Any], output: Path | str) -> None:
    """Write a deterministic UTF-8/LF JSON report without machine-local fields."""

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
