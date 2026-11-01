"""Check real P1 -> P2 -> P4 integration using existing local artifacts."""

import argparse
import json
from pathlib import Path

from src.retrieval.agent_integration import run_agent_integration


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = run_agent_integration(args.artifact_root, args.output_dir)
    except (OSError, ValueError, RuntimeError, KeyError, StopIteration) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
