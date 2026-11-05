"""Run the ordered annotation-pool preparation and frozen export workflow.

Use prepare, pilot, freeze and export as separate invocations so development
verification completes before any held-out question is sampled or retrieved.
"""

import argparse
import os
from pathlib import Path

from src.data.build_annotation_pool import DATA, HISTORY, export_pool, freeze, prepare
from src.data.build_multi_retriever_pilot import (
    DEFAULT_CONFIG,
    DEFAULT_OUTPUT,
    run_pilot,
)


def main() -> None:
    """Dispatch one explicitly selected stage with fixed retrieval settings.

    Existing outputs are rejected; use a new directory for a pilot rerun.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage", choices=("prepare", "pilot", "freeze", "export", "multi-pilot")
    )
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--multi-output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--data", type=Path, default=DATA)
    parser.add_argument("--history", type=Path, default=HISTORY)
    parser.add_argument("--pilot", type=Path, default=DATA / "annotation_pilot")
    parser.add_argument("--output", type=Path, default=DATA / "annotation_held_out")
    args = parser.parse_args()
    if args.stage == "multi-pilot":
        # Some SentenceTransformer processor probes omit local_files_only.
        # Set offline mode before lazy imports, then restore the caller's state.
        previous_offline = os.environ.get("HF_HUB_OFFLINE")
        os.environ["HF_HUB_OFFLINE"] = "1"
        try:
            run_pilot(args.data, args.config, args.multi_output)
        finally:
            if previous_offline is None:
                os.environ.pop("HF_HUB_OFFLINE", None)
            else:
                os.environ["HF_HUB_OFFLINE"] = previous_offline
    elif args.stage == "prepare":
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
