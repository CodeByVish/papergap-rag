#!/usr/bin/env python
"""Re-parse recorded parse failures with today's parser - no model, no GPU.

When parsing fails, the answers artefact still stores the first
:data:`src.generation.pipeline.RAW_TEXT_EXCERPT_CHARS` characters of the raw response as
``generation.raw_text_excerpt``. After a parser fix, that excerpt is enough to
check whether the record would now parse. It is **not** enough to replace the
recorded run: a response longer than the excerpt is truncated, so a failure here
can be the excerpt rather than the parser.

    python scripts/reparse_failures.py \\
        --answers runs/week6/answers-vllm-bge-reranked-cluster.jsonl

Exit codes:

    0  every failure record was replayed, whether it recovered or not
    1  the answers file could not be read
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.generation.generators.base import ResponseParseError, parse_response  # noqa: E402


def cut(text: str, limit: int) -> str:
    collapsed = " ".join(text.split())
    return collapsed if len(collapsed) <= limit else collapsed[: limit - 3] + "..."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--answers", type=Path, required=True)
    parser.add_argument(
        "--code",
        default="PARSE_ERROR",
        help="violation code marking a record to replay (default: PARSE_ERROR)",
    )
    parser.add_argument("--max-answer-chars", type=int, default=300)
    args = parser.parse_args(argv)

    try:
        records = [
            json.loads(line)
            for line in args.answers.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[fatal] cannot read {args.answers}: {type(exc).__name__}: {exc}")
        return 1

    failures = [
        record
        for record in records
        if any(
            violation.get("code") == args.code
            for violation in record.get("validation", {}).get("violations", [])
        )
    ]
    if not failures:
        print(f"no {args.code} record in {args.answers}")
        return 0

    recovered = 0
    for record in failures:
        text = (record.get("generation") or {}).get("raw_text_excerpt") or ""
        print()
        print(f"[{record.get('index')}] {record.get('question')}")
        print(f"  excerpt chars: {len(text)}")
        try:
            result, diagnostics = parse_response(text)
        except ResponseParseError as exc:
            print(f"  still fails: {exc.reason}")
            continue

        recovered += 1
        print(
            f"  RECOVERED status={result.evidence_status.value} "
            f"repairs={diagnostics.invalid_escape_repairs}"
        )
        print(f"  answer: {cut(result.answer, args.max_answer_chars)}")

    print()
    print(
        f"{recovered}/{len(failures)} {args.code} record(s) re-parse with "
        "today's parser"
    )
    print(
        "This is a diagnostic, not a rewritten run: raw_text_excerpt is "
        "truncated at 2000 characters."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
