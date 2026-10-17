"""Independently verify QASPER paper and question exports."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from src.data.qasper_export import check_qasper_export


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--papers", type=Path, required=True)
    parser.add_argument("--qa", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        summary = check_qasper_export(
            papers_path=args.papers,
            qa_path=args.qa,
            manifest_path=args.manifest,
        )
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
