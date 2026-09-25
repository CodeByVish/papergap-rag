"""Command-line entry point for reproducible QASPER acquisition."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from src.data.qasper import (
    DEFAULT_QASPER_REVISION,
    QasperAcquisitionResult,
    acquire_qasper,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download and verify a reproducible local QASPER acquisition."
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="Destination directory for the published QASPER files.",
    )
    parser.add_argument(
        "--revision",
        default=DEFAULT_QASPER_REVISION,
        help="Hub revision to resolve (default: the pinned commit SHA).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing destination after staging succeeds.",
    )
    return parser


def _format_split_rows(result: QasperAcquisitionResult) -> str:
    return ", ".join(
        f"{split_name}={row_count}" for split_name, row_count in result.split_rows
    )


def _print_success(result: QasperAcquisitionResult) -> None:
    print(f"Output directory: {result.output_dir}")
    print(f"Resolved revision: {result.resolved_revision}")
    print(f"Split rows: {_format_split_rows(result)}")
    print(f"Aggregate SHA-256: {result.aggregate_sha256}")


def main(argv: Sequence[str] | None = None) -> int:
    """Parse CLI arguments, run acquisition, and print a safe summary."""

    args = _build_parser().parse_args(argv)
    try:
        result = acquire_qasper(
            output_dir=args.output_dir,
            revision=args.revision,
            force=args.force,
        )
    except FileExistsError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    _print_success(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
