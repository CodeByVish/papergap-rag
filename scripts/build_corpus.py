"""Build and size-check the complete development QASPER passage corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from src.data.chunking import (
    ChunkingConfig,
    build_passages_from_record,
    validate_built_passages,
)
from src.data.passage_ids import PassageIdContext
from src.data.qasper_inspection import _validate_input_files
from src.data.split_policy import OFFICIAL_TO_PROJECT_ROLE, SPLIT_POLICY_VERSION

MIN_PASSAGES = 10_000
MIN_WORDS = 100_000
SOURCE_SPLITS = ("train", "validation")


def _source_words(record: dict[str, Any], built: tuple[Any, ...]) -> int:
    """Count source words once, excluding chunks' repeated overlap text."""

    indices: dict[int, set[int]] = defaultdict(set)
    for item in built:
        indices[item.coordinate.section_index].update(item.paragraph_indices)
    count = 0
    for section_index, paragraph_indices in indices.items():
        paragraphs = record["full_text"][section_index]["paragraphs"]
        count += sum(len(paragraphs[index].strip().split()) for index in paragraph_indices)
    return count


def _corpus_bytes(passages: list[Any]) -> bytes:
    lines = (
        json.dumps(
            item.passage.model_dump(mode="json"),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        for item in passages
    )
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_corpus(
    *,
    input_dir: Path,
    output: Path,
    manifest_output: Path,
    chunk_size_words: int = 200,
    chunk_overlap_words: int = 40,
) -> dict[str, Any]:
    """Verify raw input, build all development passages, and enforce rubric limits."""

    input_dir = Path(input_dir)
    output = Path(output)
    manifest_output = Path(manifest_output)
    if output == manifest_output:
        raise ValueError("corpus and manifest output paths must differ")
    if output.exists() or manifest_output.exists():
        raise FileExistsError("corpus or manifest output already exists")
    source_manifest, paths = _validate_input_files(input_dir)
    dataset = source_manifest["dataset"]
    config = ChunkingConfig(
        chunk_size_words=chunk_size_words,
        chunk_overlap_words=chunk_overlap_words,
    )
    context = PassageIdContext(
        dataset_id=dataset["id"],
        resolved_revision=dataset["resolved_revision"],
        local_parser_version=dataset["local_parser_version"],
        normalization_version=config.normalization_version,
        chunking_version=config.chunking_version,
        chunk_size_words=config.chunk_size_words,
        chunk_overlap_words=config.chunk_overlap_words,
    )
    passages: list[Any] = []
    seen_papers: set[str] = set()
    source_word_count = 0
    split_counts: dict[str, dict[str, int | str]] = {}
    for split in SOURCE_SPLITS:
        paper_count = passage_count = 0
        with paths[split].open(encoding="utf-8", newline="") as handle:
            for line_number, line in enumerate(handle, start=1):
                record = json.loads(line)
                if not isinstance(record, dict):
                    raise TypeError(f"{split} line {line_number} is not an object")
                paper_id = record.get("id")
                if paper_id in seen_papers:
                    raise ValueError(f"duplicate paper ID: {paper_id!r}")
                seen_papers.add(paper_id)
                result = build_passages_from_record(record, context=context, config=config)
                paper_count += 1
                passage_count += len(result.passages)
                source_word_count += _source_words(record, result.passages)
                passages.extend(result.passages)
        split_counts[split] = {
            "project_role": OFFICIAL_TO_PROJECT_ROLE[split],
            "source_paper_count": paper_count,
            "passage_count": passage_count,
        }
    validate_built_passages(passages)
    passage_word_count = sum(len(item.passage.text.split()) for item in passages)
    if len(passages) < MIN_PASSAGES or source_word_count < MIN_WORDS:
        raise ValueError(
            f"corpus below rubric minimum: {len(passages)} passages, "
            f"{source_word_count} source words; require {MIN_PASSAGES} and {MIN_WORDS}"
        )
    if passage_word_count < MIN_WORDS:
        raise ValueError("chunked passage word count is below rubric minimum")
    word_types = {
        token.casefold()
        for item in passages
        for token in item.passage.text.split()
    }
    corpus_bytes = _corpus_bytes(passages)
    corpus_sha256 = hashlib.sha256(corpus_bytes).hexdigest()
    source_splits = {
        entry["name"]: {"sha256": entry["sha256"], "rows": entry["rows"]}
        for entry in source_manifest["splits"]
        if entry["name"] in SOURCE_SPLITS
    }
    manifest: dict[str, Any] = {
        "manifest_schema_version": 1,
        "artifact": "development_corpus",
        "source": {
            "dataset_id": dataset["id"],
            "resolved_revision": dataset["resolved_revision"],
            "source_splits": source_splits,
            "split_policy_version": SPLIT_POLICY_VERSION,
            "split_counts": split_counts,
        },
        "chunking": {
            "source_kinds": ["full_text"],
            "normalization_version": config.normalization_version,
            "chunking_version": config.chunking_version,
            "chunk_size_words": config.chunk_size_words,
            "chunk_overlap_words": config.chunk_overlap_words,
            "word_rule": "Unicode-aware non-whitespace runs (str.split)",
            "type_rule": "casefolded non-whitespace runs from passage text",
        },
        "output": {
            "file": output.name,
            "sha256": corpus_sha256,
            "source_paper_count": sum(value["source_paper_count"] for value in split_counts.values()),
            "indexed_paper_count": len({item.passage.paper_id for item in passages}),
            "passage_count": len(passages),
            "unique_passage_count": len({item.passage.passage_id for item in passages}),
            "source_word_count": source_word_count,
            "passage_word_count": passage_word_count,
            "passage_word_type_count": len(word_types),
            "minimum_passages": MIN_PASSAGES,
            "minimum_words": MIN_WORDS,
            "rubric_minimum_met": True,
        },
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest_output.parent.mkdir(parents=True, exist_ok=True)
    tmp_output = output.with_name(f"tmp_{output.name}")
    tmp_manifest = manifest_output.with_name(f"tmp_{manifest_output.name}")
    if tmp_output.exists() or tmp_manifest.exists():
        raise FileExistsError("temporary corpus or manifest output already exists")
    try:
        tmp_output.write_bytes(corpus_bytes)
        tmp_manifest.write_bytes(manifest_bytes)
        tmp_output.replace(output)
        tmp_manifest.replace(manifest_output)
    finally:
        tmp_output.unlink(missing_ok=True)
        tmp_manifest.unlink(missing_ok=True)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    parser.add_argument("--chunk-size-words", type=int, default=200)
    parser.add_argument("--chunk-overlap-words", type=int, default=40)
    args = parser.parse_args()
    try:
        manifest = build_corpus(**vars(args))
    except (FileExistsError, OSError, ValueError, TypeError, KeyError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(json.dumps(manifest["output"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
