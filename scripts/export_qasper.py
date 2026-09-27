"""Export fixed QASPER input splits into paper-only and question-only JSONL files."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from src.data.qasper_export import check_qasper_export, export_qasper


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--papers-output", type=Path, required=True)
    parser.add_argument("--qa-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = export_qasper(**vars(args))
        summary = check_qasper_export(
            papers_path=args.papers_output,
            qa_path=args.qa_output,
            manifest_path=args.manifest_output,
        )
    except (FileExistsError, OSError, ValueError, TypeError, KeyError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(
        json.dumps(
            {
                "papers": summary["papers"],
                "qa": summary["qa"],
                "manifest": {
                    "file": args.manifest_output.name,
                    "rows": 1,
                    "sha256": hashlib.sha256(args.manifest_output.read_bytes()).hexdigest(),
                    "split_policy_version": manifest["split_policy_version"],
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
