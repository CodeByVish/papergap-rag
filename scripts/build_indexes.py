"""Build P1 indexes: python -m scripts.build_indexes --help."""

import argparse
import json
import re
from pathlib import Path

from pydantic import ValidationError

from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.schemas import Passage

PINNED_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"


def revision_sha(value: str) -> str:
    """Keep build and reload on an immutable model version."""
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise argparse.ArgumentTypeError("revision must be a 40-character commit SHA")
    return value


def load_passages(path: str | Path) -> list[Passage]:
    """Read UTF-8 JSONL, ignoring blank lines and reporting bad record locations."""
    path = Path(path)
    passages = []
    seen_ids: dict[str, int] = {}
    try:
        source = path.open(encoding="utf-8-sig")
    except OSError as error:
        raise ValueError(f"{path}: cannot read Passage JSONL ({error.strerror})") from error
    with source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                passage = Passage.model_validate_json(line)
            except ValidationError as error:
                detail = error.errors(include_url=False, include_input=False)[0]
                field = ".".join(str(part) for part in detail["loc"]) or "JSON"
                raise ValueError(
                    f"{path}:{line_number}: invalid Passage {field}: {detail['msg']}"
                ) from error
            if passage.passage_id in seen_ids:
                raise ValueError(
                    f"{path}:{line_number}: duplicate passage_id {passage.passage_id!r} "
                    f"(first seen on line {seen_ids[passage.passage_id]})"
                )
            seen_ids[passage.passage_id] = line_number
            passages.append(passage)
    if not passages:
        raise ValueError(f"{path}: no passages found")
    return passages


def build_indexes(
    passages_path: str | Path,
    output_dir: str | Path,
    *,
    model_name: str = DEFAULT_MODEL_NAME,
    revision: str = PINNED_REVISION,
    device: str = "cpu",
    cache_folder: str | Path | None = None,
    local_files_only: bool = False,
) -> dict:
    """Validate BM25 construction and persist Dense using existing retrievers."""
    if model_name != DEFAULT_MODEL_NAME:
        raise ValueError(f"This P1 implementation supports only {DEFAULT_MODEL_NAME}")
    passages = load_passages(passages_path)
    output_dir = Path(output_dir)
    # Reject accidental reuse before spending time encoding the corpus.
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise ValueError(f"{output_dir}: output directory must be new or empty")
    BM25Retriever(passages)
    dense = DenseRetriever(
        passages,
        revision=revision,
        device=device,
        cache_folder=cache_folder,
        local_files_only=local_files_only,
    )
    dense.save(output_dir)
    metadata = json.loads((output_dir / "metadata.json").read_text(encoding="utf-8"))
    return {
        "passages_path": str(Path(passages_path).resolve()),
        "passage_count": len(passages),
        "paper_count": len({passage.paper_id for passage in passages}),
        "bm25_index": "built in memory; rebuild from the same JSONL when querying",
        "model_name": metadata["model_name"],
        "revision": metadata["revision"],
        "embedding_dimension": metadata["embedding_dimension"],
        "output_dir": str(output_dir.resolve()),
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--passages", type=Path, required=True, help="Passage JSONL input"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="New or empty Dense index directory",
    )
    parser.add_argument(
        "--model-name", choices=[DEFAULT_MODEL_NAME], default=DEFAULT_MODEL_NAME
    )
    parser.add_argument("--revision", type=revision_sha, default=PINNED_REVISION)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--cache-folder", type=Path)
    parser.add_argument(
        "--local-files-only", action="store_true", help="Use cached model files only"
    )
    args = parser.parse_args(argv)
    try:
        summary = build_indexes(
            args.passages,
            args.output_dir,
            model_name=args.model_name,
            revision=args.revision,
            device=args.device,
            cache_folder=args.cache_folder,
            local_files_only=args.local_files_only,
        )
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
