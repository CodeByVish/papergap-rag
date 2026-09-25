"""Build a deterministic, schema-validated 100-passage QASPER sample."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.data.chunking import (
    CHUNKING_VERSION,
    NORMALIZATION_VERSION,
    BuiltPassage,
    ChunkingConfig,
    NormalizationReport,
    build_passages_from_records,
    validate_built_passages,
)
from src.data.passage_ids import PassageIdContext
from src.data.qasper import QASPER_DATASET_ID
from src.data.split_policy import OFFICIAL_TO_PROJECT_ROLE

TARGET_PASSAGE_COUNT = 100
SUPPORTED_SPLITS = ("train", "validation")


@dataclass(frozen=True, slots=True)
class PassageGroup:
    """All chunks from one source container."""

    source_split: str
    project_role: str
    paper_id: str
    source_kind: str
    section_index: int
    passages: tuple[BuiltPassage, ...]

    @property
    def sort_key(self) -> tuple[str, str, str, int]:
        """Return the stable selection and output order key."""

        return (
            self.source_split,
            self.paper_id,
            self.source_kind,
            self.section_index,
        )


def _load_json_object(path: Path) -> dict[str, Any]:
    """Read one UTF-8 JSON object."""

    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return value


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    """Read non-empty JSON object lines in source order."""

    records: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                raise ValueError(f"blank line in {path} at line {line_number}")
            value = json.loads(line)
            if not isinstance(value, dict):
                raise TypeError(f"non-object record in {path} at line {line_number}")
            records.append(value)
    return records


def _manifest_value(manifest: Mapping[str, object], *keys: str) -> object:
    """Read a required nested manifest value."""

    value: object = manifest
    for key in keys:
        if not isinstance(value, Mapping) or key not in value:
            raise ValueError(f"manifest is missing {'.'.join(keys)}")
        value = value[key]
    return value


def _split_file(manifest: Mapping[str, object], split_name: str) -> str:
    """Return one split filename from the acquisition manifest list."""

    splits = manifest.get("splits")
    if not isinstance(splits, list):
        raise TypeError("manifest splits must be a list")
    for entry in splits:
        if not isinstance(entry, Mapping):
            raise TypeError("manifest split entries must be objects")
        if entry.get("name") == split_name:
            file_name = entry.get("file")
            if type(file_name) is not str:
                raise ValueError(f"manifest split file for {split_name} must be a string")
            return file_name
    raise ValueError(f"manifest is missing split {split_name}")


def _source_manifest(manifest: Mapping[str, object]) -> tuple[str, str, int]:
    """Return the dataset ID, resolved revision, and parser version."""

    dataset_id = _manifest_value(manifest, "dataset", "id")
    resolved_revision = _manifest_value(manifest, "dataset", "resolved_revision")
    parser_version = _manifest_value(manifest, "dataset", "local_parser_version")
    if type(dataset_id) is not str or dataset_id != QASPER_DATASET_ID:
        raise ValueError("manifest dataset ID is not allenai/qasper")
    if type(resolved_revision) is not str:
        raise ValueError("manifest resolved revision must be a string")
    if type(parser_version) is not int:
        raise ValueError("manifest local parser version must be an integer")
    return dataset_id, resolved_revision, parser_version


def _build_groups(
    *,
    input_dir: Path,
    manifest: Mapping[str, object],
    context: PassageIdContext,
    config: ChunkingConfig,
) -> tuple[tuple[PassageGroup, ...], NormalizationReport, dict[str, int]]:
    """Build complete source-container groups from development data."""

    groups: list[PassageGroup] = []
    report = NormalizationReport()
    paper_counts: dict[str, int] = {}
    seen_paper_ids: set[str] = set()
    for split_name in SUPPORTED_SPLITS:
        split_file = _split_file(manifest, split_name)
        records = _read_jsonl(input_dir / split_file)
        result = build_passages_from_records(
            records,
            context=context,
            config=config,
        )
        report = report.merged(result.report)
        split_paper_ids = {item.coordinate.paper_id for item in result.passages}
        for paper_id in split_paper_ids:
            if paper_id in seen_paper_ids:
                raise ValueError(f"paper ID overlaps selected source splits: {paper_id}")
            seen_paper_ids.add(paper_id)
        paper_counts[split_name] = len(records)
        grouped: dict[tuple[str, str, int], list[BuiltPassage]] = defaultdict(list)
        for item in result.passages:
            key = (
                item.coordinate.paper_id,
                item.coordinate.source_kind,
                item.coordinate.section_index,
            )
            grouped[key].append(item)
        project_role = OFFICIAL_TO_PROJECT_ROLE[split_name]  # type: ignore[index]
        for (paper_id, source_kind, section_index), items in grouped.items():
            sequence = tuple(sorted(items, key=lambda item: item.coordinate.chunk_index))
            groups.append(
                PassageGroup(
                    source_split=split_name,
                    project_role=project_role,
                    paper_id=paper_id,
                    source_kind=source_kind,
                    section_index=section_index,
                    passages=sequence,
                )
            )
    groups.sort(key=lambda group: group.sort_key)
    return tuple(groups), report, paper_counts


def _prefer_path(candidate: tuple[PassageGroup, ...], current: tuple[PassageGroup, ...]) -> bool:
    """Prefer more papers, then the lexicographically earlier stable path."""

    if len(candidate) != len(current):
        return len(candidate) > len(current)
    return tuple(group.sort_key for group in candidate) < tuple(
        group.sort_key for group in current
    )


def select_groups(
    groups: Sequence[PassageGroup],
    *,
    target_count: int = TARGET_PASSAGE_COUNT,
) -> tuple[PassageGroup, ...]:
    """Select complete source containers summing exactly to the target count.

    Dynamic programming processes papers in stable order and allows at most one
    source container per paper. This prevents one long paper from supplying the
    whole sample while preserving complete within-container adjacency links.
    """

    if type(target_count) is not int or target_count <= 0:
        raise ValueError("target_count must be a positive integer")
    by_paper: dict[str, list[PassageGroup]] = defaultdict(list)
    for group in sorted(groups, key=lambda item: item.sort_key):
        if 0 < len(group.passages) <= target_count:
            by_paper[group.paper_id].append(group)

    states: dict[int, tuple[PassageGroup, ...]] = {0: ()}
    for paper_id in sorted(by_paper):
        previous = dict(states)
        options = sorted(by_paper[paper_id], key=lambda group: group.sort_key)
        for total, path in previous.items():
            for group in options:
                new_total = total + len(group.passages)
                if new_total > target_count:
                    continue
                candidate = path + (group,)
                current = states.get(new_total)
                if current is None or _prefer_path(candidate, current):
                    states[new_total] = candidate

    selected = states.get(target_count)
    if selected is None:
        raise ValueError(
            f"could not select complete source containers totaling {target_count} passages"
        )
    selected = tuple(sorted(selected, key=lambda group: group.sort_key))
    selected_count = sum(len(group.passages) for group in selected)
    if selected_count != target_count:
        raise AssertionError("sample selection count changed unexpectedly")
    if len({group.paper_id for group in selected}) < 2:
        raise ValueError("sample must contain passages from multiple papers")
    return selected


def _selected_passages(groups: Sequence[PassageGroup]) -> tuple[BuiltPassage, ...]:
    """Flatten complete selected groups in stable source order."""

    return tuple(item for group in groups for item in group.passages)


def _report_dict(report: NormalizationReport) -> dict[str, int]:
    """Serialize the fixed normalization report fields."""

    return {
        field: getattr(report, field)
        for field in (
            "paragraphs_seen",
            "paragraphs_emitted",
            "blank_paragraphs_dropped",
            "line_ending_replacements",
            "outer_whitespace_trims",
            "sections_seen",
            "sections_emitted",
            "blank_sections_dropped",
            "null_sections_dropped",
            "empty_sections_dropped",
            "invalid_papers_dropped",
        )
    }


def _passage_bytes(passages: Iterable[BuiltPassage]) -> bytes:
    """Serialize passages with stable JSONL formatting."""

    lines = [
        json.dumps(
            item.passage.model_dump(mode="json"),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        for item in passages
    ]
    return ("\n".join(lines) + "\n").encode("utf-8")


def _write_bytes_safely(destination: Path, payload: bytes, *, force: bool) -> None:
    """Publish one generated file through a temporary sibling file."""

    if destination.exists() and not force:
        raise FileExistsError(f"output already exists: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f"tmp_{destination.name}")
    if temporary.exists():
        temporary.unlink()
    temporary.write_bytes(payload)
    temporary.replace(destination)


def build_sample(
    *,
    input_dir: Path,
    output: Path,
    manifest_output: Path,
    chunk_size_words: int = 200,
    chunk_overlap_words: int = 40,
    force: bool = False,
) -> dict[str, object]:
    """Build and publish the deterministic sample and its manifest."""

    input_dir = Path(input_dir)
    manifest = _load_json_object(input_dir / "manifest.json")
    dataset_id, resolved_revision, parser_version = _source_manifest(manifest)
    config = ChunkingConfig(
        chunk_size_words=chunk_size_words,
        chunk_overlap_words=chunk_overlap_words,
        normalization_version=NORMALIZATION_VERSION,
        chunking_version=CHUNKING_VERSION,
    )
    context = PassageIdContext(
        dataset_id=dataset_id,
        resolved_revision=resolved_revision,
        local_parser_version=parser_version,
        normalization_version=config.normalization_version,
        chunking_version=config.chunking_version,
        chunk_size_words=config.chunk_size_words,
        chunk_overlap_words=config.chunk_overlap_words,
    )
    groups, report, paper_counts = _build_groups(
        input_dir=input_dir,
        manifest=manifest,
        context=context,
        config=config,
    )
    selected_groups = select_groups(groups)
    passages = _selected_passages(selected_groups)
    if len(passages) != TARGET_PASSAGE_COUNT:
        raise AssertionError("sample does not contain exactly 100 passages")
    validate_built_passages(passages)
    output_bytes = _passage_bytes(passages)
    output_sha256 = hashlib.sha256(output_bytes).hexdigest()
    _write_bytes_safely(Path(output), output_bytes, force=force)

    selected_papers = sorted({group.paper_id for group in selected_groups})
    selected_sections = sorted(
        {
            (group.source_split, group.paper_id, group.section_index)
            for group in selected_groups
        }
    )
    manifest_payload: dict[str, object] = {
        "manifest_schema_version": 1,
        "artifact": "sample_passages_100",
        "source": {
            "dataset_id": dataset_id,
            "resolved_revision": resolved_revision,
            "local_parser_version": parser_version,
            "source_splits": [
                {
                    "name": split_name,
                    "project_role": OFFICIAL_TO_PROJECT_ROLE[split_name],
                    "input_paper_count": paper_counts[split_name],
                }
                for split_name in SUPPORTED_SPLITS
            ],
        },
        "normalization": _report_dict(report),
        "chunking": {
            "normalization_version": config.normalization_version,
            "chunking_version": config.chunking_version,
            "chunk_size_words": config.chunk_size_words,
            "chunk_overlap_words": config.chunk_overlap_words,
            "source_kinds": ["full_text"],
            "word_rule": "Unicode-aware non-whitespace runs matched by \\S+",
        },
        "selection": {
            "method": "stable complete-source-container subset sum by paper",
            "target_passage_count": TARGET_PASSAGE_COUNT,
            "selected_container_count": len(selected_groups),
            "selected_paper_count": len(selected_papers),
            "selected_section_count": len(selected_sections),
            "selected_groups": [
                {
                    "source_split": group.source_split,
                    "project_role": group.project_role,
                    "paper_id": group.paper_id,
                    "source_kind": group.source_kind,
                    "section_index": group.section_index,
                    "passage_count": len(group.passages),
                }
                for group in selected_groups
            ],
        },
        "output": {
            "file": Path(output).name,
            "format": "jsonl",
            "encoding": "utf-8",
            "newline": "lf",
            "passage_count": len(passages),
            "unique_passage_count": len({item.passage.passage_id for item in passages}),
            "unique_paper_count": len(selected_papers),
            "passage_word_count": sum(len(item.passage.text.split()) for item in passages),
            "sha256": output_sha256,
        },
    }
    manifest_bytes = (
        json.dumps(
            manifest_payload,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")
    _write_bytes_safely(Path(manifest_output), manifest_bytes, force=force)
    return manifest_payload


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build exactly 100 deterministic schema-valid QASPER passages."
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        type=Path,
        help="Directory containing the verified QASPER JSONL files and manifest.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Destination JSONL path for the 100-passage sample.",
    )
    parser.add_argument(
        "--manifest-output",
        required=True,
        type=Path,
        help="Destination JSON manifest path for the generated sample.",
    )
    parser.add_argument("--chunk-size-words", type=int, default=200)
    parser.add_argument("--chunk-overlap-words", type=int, default=40)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing generated outputs after successful construction.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the sample-builder CLI."""

    args = _build_parser().parse_args(argv)
    try:
        payload = build_sample(
            input_dir=args.input_dir,
            output=args.output,
            manifest_output=args.manifest_output,
            chunk_size_words=args.chunk_size_words,
            chunk_overlap_words=args.chunk_overlap_words,
            force=args.force,
        )
    except (FileExistsError, OSError, ValueError, TypeError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    output = payload["output"]
    if not isinstance(output, Mapping):
        raise TypeError("manifest output section is not a mapping")
    print(f"Output: {args.output}")
    print(f"Passages: {output['passage_count']}")
    print(f"Papers: {output['unique_paper_count']}")
    print(f"SHA-256: {output['sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
