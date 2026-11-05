"""Call the demo service from the laptop: health, one answer, citation text.

The demo is verified with ``curl`` in the docs, but a one-line ``python -c``
that builds a JSON body is exactly the kind of command that gets truncated by a
Windows terminal and leaves a half-open quote. This script replaces it: one
short line, no quoting, and the same checks every time.

    python scripts/demo_client.py --record runs/week3/p4_state_smoke.jsonl --token demo2026

    # free-form instead of an exported record
    python scripts/demo_client.py --question "What result is reported?" \
        --paper-id 1706.04115 --token demo2026

What it prints, in order:

* ``GET /health`` - backend, prompt version, capability flags;
* ``POST /answer`` - status, evidence status, citation count, violation codes,
  whether the agent block is present, and the wall-clock latency;
* ``POST /passages`` - the cited text, unless ``--no-passages``.

Exit codes: 0 the answer request returned 200, 1 it did not, 2 a connection
error (the tunnel is not up).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Optional


def request(
    method: str,
    url: str,
    body: Optional[dict[str, Any]] = None,
    token: Optional[str] = None,
    timeout: float = 180,
) -> tuple[int, Any]:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, json.loads(response.read().decode("utf-8") or "null")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        try:
            return exc.code, json.loads(raw)
        except json.JSONDecodeError:
            return exc.code, {"detail": raw}


def first_record(path: str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                record = json.loads(line)
                if isinstance(record, dict):
                    return record
    raise ValueError(f"{path} contains no JSON object")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Call the demo service from the laptop.")
    parser.add_argument("--base", default="http://127.0.0.1:8000")
    parser.add_argument("--token", default=None, help="bearer token, if the server requires one")
    parser.add_argument("--record", default=None, help="JSONL file; its first record is sent")
    parser.add_argument("--question", default=None, help="free-form question instead of a record")
    parser.add_argument("--paper-id", default=None, help="required with --question")
    parser.add_argument("--no-passages", action="store_true", help="skip POST /passages")
    parser.add_argument("--save", default=None, help="write the answer record to this file")
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args(argv)

    if bool(args.record) == bool(args.question):
        parser.error("pass exactly one of --record or --question")
    if args.question and not args.paper_id:
        parser.error("--question needs --paper-id (QASPER retrieval is paper-scoped)")

    base = args.base.rstrip("/")

    try:
        status, health = request("GET", base + "/health", token=args.token, timeout=10)
    except (urllib.error.URLError, OSError) as exc:
        print(f"cannot reach {base}: {exc}", file=sys.stderr)
        print("is the SSH tunnel running?", file=sys.stderr)
        return 2

    if status != 200:
        print(f"GET /health -> {status}: {health}", file=sys.stderr)
        return 2
    warmup = health.get("warmup_seconds")
    print(
        "health : "
        f"backend={health.get('backend')} prompt={health.get('prompt_version')} "
        f"papers={health.get('papers')} retrieval={health.get('retrieval')} "
        f"passage_text={health.get('passage_text')} "
        f"warmup={f'{warmup}s' if warmup is not None else 'n/a'} "
        f"uptime={health.get('uptime_seconds')}s"
    )

    if args.record:
        body: dict[str, Any] = {"record": first_record(args.record)}
    else:
        body = {"question": args.question, "paper_id": args.paper_id}

    started = time.perf_counter()
    try:
        status, answer = request("POST", base + "/answer", body, args.token, args.timeout)
    except (urllib.error.URLError, OSError) as exc:
        print(f"POST /answer failed: {exc}", file=sys.stderr)
        return 2
    elapsed = time.perf_counter() - started

    if status != 200:
        print(f"answer : {status} {json.dumps(answer, ensure_ascii=False)}", file=sys.stderr)
        return 1

    result = answer.get("result", {})
    validation = answer.get("validation", {})
    codes = [v.get("code") for v in validation.get("violations", [])]
    print(
        "answer : "
        f"200 {result.get('evidence_status')} "
        f"citations={len(result.get('citations') or [])} "
        f"downgraded={validation.get('downgraded')} codes={codes} "
        f"agent={'agent' in answer} {elapsed:.1f}s"
    )
    text = (result.get("answer") or "").replace("\n", " ")
    print(f'  "{text[:160]}{"..." if len(text) > 160 else ""}"')

    if args.save:
        Path(args.save).write_text(
            json.dumps(answer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"saved  : {args.save}")

    citations = result.get("citations") or []
    if citations and not args.no_passages:
        status, lookup = request(
            "POST", base + "/passages", {"ids": citations}, args.token, args.timeout
        )
        if status != 200:
            print(f"passages: {status} {lookup.get('detail', lookup)}")
        else:
            found = lookup.get("passages", {})
            print(f"passages: found={len(found)} missing={len(lookup.get('missing', []))}")
            for passage_id, passage in list(found.items())[:3]:
                snippet = (passage.get("text") or "").replace("\n", " ")[:140]
                print(f"  - {passage_id[:24]}... [{passage.get('section')}] {snippet}...")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
