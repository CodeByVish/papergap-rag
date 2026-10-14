"""Build a deterministic, schema-validated 100-passage QASPER sample."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
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
from src.data.qasper_export import load_verified_papers
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


def _build_groups(
    *,
    papers: Sequence[dict[str, Any]],
    context: PassageIdContext,
    config: ChunkingConfig,
) -> tuple[tuple[PassageGroup, ...], NormalizationReport, dict[str, int]]:
    """Build complete source-container groups from development data."""

    groups: list[PassageGroup] = []
    report = NormalizationReport()
    paper_counts: dict[str, int] = {}
    seen_paper_ids: set[str] = set()
    for split_name in SUPPORTED_SPLITS:
        records = [record for record in papers if record["source_split"] == split_name]
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


def _publish_outputs(
    output: Path, manifest_output: Path, payload: bytes, manifest: bytes
) -> None:
    """Stage both sample files and publish the manifest last without overwriting."""

    if output.resolve(strict=False) == manifest_output.resolve(strict=False):
        raise ValueError("sample and manifest output paths must differ")
    targets = (output, manifest_output)
    if any(path.exists() or path.is_symlink() for path in targets):
        raise FileExistsError("sample or manifest output already exists")
    temporary_paths = (
        output.with_name(f"tmp_{output.name}"),
        manifest_output.with_name(f"tmp_{manifest_output.name}"),
    )
    if any(path.exists() or path.is_symlink() for path in temporary_paths):
        raise FileExistsError("a temporary sample output already exists")
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest_output.parent.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    try:
        for path, content in zip(temporary_paths, (payload, manifest), strict=True):
            with path.open("xb") as handle:
                created.append(path)
                handle.write(content)
        if temporary_paths[0].read_bytes() != payload:
            raise OSError("staged sample bytes differ from generated bytes")
        if temporary_paths[1].read_bytes() != manifest:
            raise OSError("staged sample manifest bytes differ from generated bytes")
        os.replace(temporary_paths[0], output)
        created.remove(temporary_paths[0])
        os.replace(temporary_paths[1], manifest_output)
        created.remove(temporary_paths[1])
    except Exception:
        for path in created:
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass
        raise


def build_sample(
    *,
    papers: Path,
    export_manifest: Path,
    output: Path,
    manifest_output: Path,
    chunk_size_words: int = 200,
    chunk_overlap_words: int = 40,
) -> dict[str, object]:
    """Build and publish the deterministic sample and its manifest."""

    export, paper_records = load_verified_papers(
        papers_path=Path(papers), manifest_path=Path(export_manifest)
    )
    source = export["source"]
    config = ChunkingConfig(
        chunk_size_words=chunk_size_words,
        chunk_overlap_words=chunk_overlap_words,
        normalization_version=NORMALIZATION_VERSION,
        chunking_version=CHUNKING_VERSION,
    )
    context = PassageIdContext(
        dataset_id=source["dataset_id"],
        resolved_revision=source["resolved_revision"],
        local_parser_version=source["local_parser_version"],
        normalization_version=config.normalization_version,
        chunking_version=config.chunking_version,
        chunk_size_words=config.chunk_size_words,
        chunk_overlap_words=config.chunk_overlap_words,
    )
    groups, report, paper_counts = _build_groups(
        papers=paper_records,
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
            "dataset_id": source["dataset_id"],
            "resolved_revision": source["resolved_revision"],
            "local_parser_version": source["local_parser_version"],
            "export_papers_file": export["outputs"]["papers"]["file"],
            "export_papers_sha256": export["outputs"]["papers"]["sha256"],
            "source_splits": [
                {
                    "name": split_name,
                    "project_role": OFFICIAL_TO_PROJECT_ROLE[split_name],
                    "input_paper_count": paper_counts[split_name],
                    "source_sha256": export["source"]["split_files"][split_name]["sha256"],
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
    _publish_outputs(Path(output), Path(manifest_output), output_bytes, manifest_bytes)
    return manifest_payload


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build exactly 100 deterministic schema-valid QASPER passages."
    )
    parser.add_argument("--papers", required=True, type=Path)
    parser.add_argument("--export-manifest", required=True, type=Path)
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
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the sample-builder CLI."""

    args = _build_parser().parse_args(argv)
    try:
        payload = build_sample(
            papers=args.papers,
            export_manifest=args.export_manifest,
            output=args.output,
            manifest_output=args.manifest_output,
            chunk_size_words=args.chunk_size_words,
            chunk_overlap_words=args.chunk_overlap_words,
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
