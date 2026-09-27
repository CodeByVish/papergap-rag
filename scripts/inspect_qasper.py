"""Command-line entry point for offline QASPER inspection."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from src.data.qasper_inspection import (
    QasperInspectionError,
    inspect_qasper,
    write_report,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect a complete local QASPER acquisition without network access."
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        type=Path,
        help="Directory containing manifest.json and the three published JSONL splits.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Destination for the deterministic JSON inspection report.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = inspect_qasper(args.input_dir)
        write_report(report, args.output)
    except (OSError, QasperInspectionError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Inspection report: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
