"""Generate a lightweight catalog for a caller-selected retrieval corpus.

Run from the repository root with python -m scripts.build_paper_catalog.
Existing output paths are rejected to preserve prior data snapshots.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.data.build_paper_catalog import build_paper_catalog


def main() -> int:
    """Parse file paths, validate the complete catalog, and write UTF-8 JSON.

    Returns:
        Zero after writing a new output; invalid inputs raise before writing.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--papers", type=Path, default=Path("data/processed/papers.jsonl"))
    parser.add_argument("--passages", type=Path, required=True,
                        help="Exact passage file used by UI retrieval; recorded in the catalog.")
    parser.add_argument("--output", type=Path, default=Path("data/processed/paper_catalog.json"))
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"output already exists: {args.output}")
    catalog = build_paper_catalog(papers=args.papers, passages=args.passages)
    payload = json.dumps(catalog, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    print(json.dumps({
        "output": args.output.as_posix(),
        "paper_count": len(catalog["papers"]),
        "section_count": sum(len(paper["sections"]) for paper in catalog["papers"]),
        "passage_count": sum(paper["passage_count"] for paper in catalog["papers"]),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
