"""Run the ordered annotation-pool preparation and frozen export workflow.

Use prepare, pilot, freeze and export as separate invocations so development
verification completes before any held-out question is sampled or retrieved.
"""

import argparse
from pathlib import Path

from src.data.build_annotation_pool import DATA, HISTORY, export_pool, freeze, prepare


def main() -> None:
    """Dispatch one explicitly selected stage with fixed retrieval settings.

    Existing outputs are rejected; use a new directory for a pilot rerun.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("prepare", "pilot", "freeze", "export"))
    parser.add_argument("--data", type=Path, default=DATA)
    parser.add_argument("--history", type=Path, default=HISTORY)
    parser.add_argument("--pilot", type=Path, default=DATA / "annotation_pilot")
    parser.add_argument("--output", type=Path, default=DATA / "annotation_held_out")
    args = parser.parse_args()
    if args.stage == "prepare":
        prepare(args.data, args.history)
    elif args.stage == "pilot":
        export_pool(args.data, args.pilot, pilot=True)
    elif args.stage == "freeze":
        freeze(args.data, args.pilot)
    else:
        export_pool(args.data, args.output)
    print(f"Completed annotation stage: {args.stage}")


if __name__ == "__main__":
    main()
