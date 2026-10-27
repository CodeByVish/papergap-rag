"""Expose chunk-size comparison and manual review summarization commands.

Run from the repository root with ``python -m scripts.evaluate_chunk_size``.
The default run uses a CPU BM25 baseline without downloading model weights.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.evaluation.chunk_size_reports import summarize_readability
from src.evaluation.run_chunk_size import run_comparison


def main() -> int:
    """Parse run or summarize arguments and report actionable validation errors.

    Returns zero on success and one for invalid inputs or filesystem errors.
    Generated outputs are retained locally under the requested new run ID.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument(
        "--config",
        dest="config_path",
        type=Path,
        default=Path("experiments/chunk_size/config.json"),
    )
    run.add_argument(
        "--papers",
        dest="papers_path",
        type=Path,
        default=Path("data/processed/papers.jsonl"),
    )
    run.add_argument(
        "--qa", dest="qa_path", type=Path, default=Path("data/processed/qa.jsonl")
    )
    run.add_argument(
        "--export-manifest",
        type=Path,
        default=Path("data/processed/qasper_export.manifest.json"),
    )
    run.add_argument("--output-root", type=Path, default=Path("results/chunk_size"))
    run.add_argument("--run-id", required=True)
    summarize = commands.add_parser("summarize")
    summarize.add_argument("--run-dir", type=Path, required=True)
    arguments = vars(parser.parse_args())
    command = arguments.pop("command")
    try:
        if command == "run":
            print(run_comparison(**arguments))
        else:
            summarize_readability(arguments["run_dir"])
            print(arguments["run_dir"] / "summary.json")
    except (ValueError, TypeError, KeyError, OSError, ImportError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
