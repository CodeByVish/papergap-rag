#!/usr/bin/env python
"""Answer questions from a real retriever dump - the Week-3 end-to-end path.

This is the script that takes P5 off Mock. It reads what the retrieval phase
actually emits, adapts it, generates, validates and writes the frozen five-key
records. Everything downstream of the adapter is the code that already existed;
what is new is that the evidence now comes from a file instead of from hand-
written fixtures.

    # CPU only, seconds, no model weights - the shape check:
    python scripts/generate_from_retrieval.py \\
        --retrieval tests/fixtures/retrieval_sample.jsonl \\
        --backend mock --out runs/week3/answers-mock.jsonl

    # The real model, on the cluster:
    python scripts/generate_from_retrieval.py \\
        --retrieval "$P5_ROOT/data/p2_retrieval.jsonl" \\
        --backend vllm --model "$P5_ROOT/models/Qwen3-8B" \\
        --out runs/week3/answers-vllm.jsonl

Input is either JSON Lines (one retriever payload per line) or a JSON array of
payloads. Each payload is one question: the question text, the hits, and the
retrieval round count. Envelope key names are matched against alias lists
because the retriever's envelope is not settled yet - see
``docs/RETRIEVAL_CONTRACT.md`` §2.

Two outputs, and they answer different questions:

* ``--out`` (JSONL) - the answers, one record per question, exactly what P6
  consumes. Written through ``run_batch_to_jsonl``, so it is append-and-flush
  per record and resumable by index after a wall-clock kill.
* ``--notes-out`` (JSON) - what the *adapter* had to drop or flag, per payload,
  plus the run summary. Answers say what the model did; this says whether the
  evidence it was given was complete. An adapter that silently discards half a
  dump produces a run that looks like a retrieval failure.

Exit codes, chosen for use from a job script:

    0  ran; both artefacts written. Refusals and downgrades are results, not
       failures - a refusal on an unanswerable question is the correct outcome.
    1  could not start: unreadable input, no payloads, missing model path, or a
       backend that cannot load here. A setup problem, never a result.
    2  started, but nothing was produced. The harness is broken, not the model.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.generation.adapters import get_adapter  # noqa: E402
from src.generation.adapters.retrieval import DEFAULT_ADAPTER, build_request  # noqa: E402
from src.generation.generators import (  # noqa: E402
    BackendNotAvailable,
    MockConfig,
    MockGenerator,
    MockScenario,
    get_generator,
)
from src.generation.pipeline import (  # noqa: E402
    GroundedQAPipeline,
    PipelineConfig,
    load_jsonl,
    run_batch_to_jsonl,
)
from src.generation.prompts.grounded_qa import PROMPT_VERSION, PromptConfig  # noqa: E402
from src.generation.schema import SCHEMA_VERSION, GenerationRequest  # noqa: E402

DEFAULT_OUT = ROOT / "runs" / "week3" / "answers.jsonl"


def load_payloads(
    path: str | Path, echo: Any = print
) -> list[Any]:
    """Read one retriever dump: JSON Lines, or a JSON array.

    **The whole dump is read into memory**, deliberately. Deciding between the
    two formats means trying the whole-file parse first, which needs the whole
    file; and a retrieval dump is one payload per *question*, so even a few
    thousand is tens of megabytes. The answers artefact is the one that streams,
    because that is the one written by a job that can be killed at the
    wall-clock limit.

    A malformed **line** is skipped and counted, not fatal. That matches what
    ``pipeline.load_jsonl`` does for the answers file and for the same reason: a
    dump produced by a retriever that was killed mid-write has a partial last
    line, and aborting on it would throw away every good question before it.
    A malformed **file** still raises, because then the format itself is wrong
    and there is nothing to salvage.
    """
    text = Path(path).read_text(encoding="utf-8")

    # Whole-file first, line-by-line second. Trying the whole file first is what
    # makes a pretty-printed JSON array work; trying it second is what a JSONL
    # file needs. Deciding from the first character instead would break on
    # either, and `json.JSONDecodeError` is the honest signal that a
    # multi-record text is not one document.
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        out: list[Any] = []
        skipped = 0
        for line in text.splitlines():
            if not line.strip():
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                skipped += 1
        if skipped:
            echo(
                f"[warn] {skipped} unparseable line(s) in {path} were skipped; "
                "a dump written by a killed retriever ends in a partial line"
            )
        return out

    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        # One object is either a single payload or a wrapper carrying several
        # under a list key. Accepting both is worth it: a one-question dump is
        # how a new format gets checked before a whole batch is run.
        for key in ("payloads", "records", "responses", "data"):
            if isinstance(payload.get(key), list):
                return payload[key]
        return [payload]
    raise ValueError(
        f"expected an object, an array, or JSON Lines; got {type(payload).__name__}"
    )


def adapt_payloads(
    payloads: list[Any], adapter_name: str
) -> tuple[list[GenerationRequest], list[dict[str, Any]], list[str]]:
    """Adapt every payload, keeping going when one is malformed.

    A bad payload is an integration bug rather than a model failure, so it is
    never turned into a refusal - that would report it as a retrieval result.
    It is recorded and skipped, and the run carries on, because the alternative
    is losing a whole six-hour job to one malformed line.
    """
    adapter = get_adapter(adapter_name)
    requests: list[GenerationRequest] = []
    notes: list[dict[str, Any]] = []
    errors: list[str] = []

    for position, payload in enumerate(payloads):
        try:
            adapted = build_request(payload, adapter)
        except (ValueError, TypeError) as exc:
            errors.append(f"payload {position}: {type(exc).__name__}: {exc}")
            continue

        requests.append(adapted.request)
        if adapted.notes or adapted.report.dropped_total:
            notes.append(
                {
                    "payload_index": position,
                    "request_id": adapted.request.request_id,
                    "question": adapted.request.question,
                    "passages": len(adapted.request.passages),
                    "notes": adapted.notes,
                }
            )

    return requests, notes, errors


def request_fingerprints(requests: Sequence[GenerationRequest]) -> list[str]:
    """Per-request hashes of the adapted request set, for resume safety.

    ``run_batch_to_jsonl`` resumes by record index and trusts that the request
    list has not changed between runs. That holds for a resubmitted job - the
    same command over the same dump - but not for a *different* dump pointed at
    the same ``--out``, where the file may already hold more records than the new
    request list has. The result is a run that answers nothing and exits 0.

    **One hash per request, not one for the list**, so that the guard can test
    for a prefix rather than an exact match. ``--limit 2`` followed by a full run
    is a normal way to check a new dump before committing to it, and the record
    indices still line up; a single list hash would refuse that while adding no
    safety.

    Hashing the requests rather than the file is deliberate: it is semantic, so
    reformatting the dump does not trip it, but changing the questions, the
    passages or their order does. Same idea as ``samples_sha256`` in
    ``scripts/benchmark_qwen3.py``.
    """
    return [
        hashlib.sha256(
            json.dumps(
                r.model_dump(mode="json"), sort_keys=True, ensure_ascii=False
            ).encode("utf-8")
        ).hexdigest()
        for r in requests
    ]


def _is_prefix_mismatch(previous: Sequence[str], current: Sequence[str]) -> bool:
    """True when one list is not a prefix of the other.

    Either direction counts as compatible. The previous list is shorter when the
    last run used ``--limit``; it is longer when a full run is followed by a
    limited one, which has nothing left to do but is not an error.
    """
    shorter, longer = (
        (previous, current) if len(previous) <= len(current) else (current, previous)
    )
    return list(shorter) != list(longer[: len(shorter)])


def build_generator(args: argparse.Namespace):
    """Construct the backend named on the command line.

    Duplicated in ``smoke_test_qwen3.py`` and ``benchmark_qwen3.py`` rather than
    shared: ``scripts/`` is deliberately not a package, so importing one script
    from another would need a path hack in every caller. The flag names are kept
    identical across all three instead, which is what actually matters to
    somebody typing the command.
    """
    if args.backend == "mock":
        scenario = (
            None
            if args.mock_scenario == "cycle"
            else MockScenario(args.mock_scenario)
        )
        return MockGenerator(scenario, MockConfig())

    if not args.model:
        raise BackendNotAvailable(
            f"--model is required for the {args.backend} backend "
            "(e.g. --model \"$P5_ROOT/models/Qwen3-8B\")"
        )

    kwargs: dict[str, Any] = {
        "max_new_tokens": args.max_new_tokens,
    }
    if args.backend == "vllm":
        kwargs.update(
            max_model_len=args.max_model_len,
            gpu_memory_utilization=args.gpu_memory_utilization,
        )
    else:
        kwargs.update(allow_cpu=args.allow_cpu, max_model_len=args.max_model_len)

    return get_generator(args.backend, model_id=args.model, **kwargs)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--retrieval",
        type=Path,
        required=True,
        help="retriever dump: JSON Lines or a JSON array of payloads",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--notes-out", type=Path, default=None)
    parser.add_argument(
        "--adapter",
        default=DEFAULT_ADAPTER,
        help=f"passage adapter name (default: {DEFAULT_ADAPTER})",
    )
    parser.add_argument(
        "--backend", default="mock", choices=["mock", "transformers", "vllm"]
    )
    parser.add_argument("--model", default=None)
    parser.add_argument(
        "--mock-scenario",
        default="grounded",
        choices=["cycle"] + [s.value for s in MockScenario],
        help="which mock behaviour to emit (default: grounded, the positive control)",
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="answer only the first N payloads"
    )
    parser.add_argument("--tag", default="local")
    parser.add_argument("--max-passages", type=int, default=PromptConfig().max_passages)
    parser.add_argument(
        "--max-chars-per-passage",
        type=int,
        default=PromptConfig().max_chars_per_passage,
    )
    parser.add_argument("--max-new-tokens", type=int, default=768)
    parser.add_argument("--max-model-len", type=int, default=32768)
    parser.add_argument("--gpu-memory-utilization", type=float, default=0.85)
    parser.add_argument(
        "--allow-cpu",
        action="store_true",
        help="let the Transformers backend run on CPU (shape checks only)",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="ignore an existing --out file instead of continuing it",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        payloads = load_payloads(args.retrieval)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"[fatal] cannot read {args.retrieval}: {type(exc).__name__}: {exc}")
        return 1

    if args.limit < 0:
        print(f"[fatal] --limit must not be negative, got {args.limit}")
        return 1
    if args.limit:
        payloads = payloads[: args.limit]
    if not payloads:
        print(f"[fatal] {args.retrieval} holds no payloads")
        return 1

    requests, notes, errors = adapt_payloads(payloads, args.adapter)
    for error in errors:
        print(f"[skip] {error}")
    if not requests:
        print("[fatal] no payload could be adapted; check the adapter against the dump")
        return 1

    prompt_config = PromptConfig(
        max_passages=args.max_passages,
        max_chars_per_passage=args.max_chars_per_passage or None,
    )

    try:
        generator = build_generator(args)
    except (BackendNotAvailable, KeyError) as exc:
        print(f"[fatal] {type(exc).__name__}: {exc}")
        return 1

    pipeline = GroundedQAPipeline(
        generator, config=PipelineConfig(prompt=prompt_config)
    )

    fingerprints = request_fingerprints(requests)
    #: Sits beside the answers file rather than inside it: the records must stay
    #: exactly the frozen five-key shape plus the audit trail, and a run-level
    #: fact has no business in a per-question record.
    meta_path = args.out.parent / (args.out.name + ".meta.json")

    if not args.no_resume and args.out.exists() and meta_path.exists():
        try:
            previous = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous = {}
        stored = previous.get("request_fingerprints")
        if stored is not None and _is_prefix_mismatch(stored, fingerprints):
            print(
                f"[fatal] {args.out} was produced from a DIFFERENT request set "
                f"({len(stored)} request(s) then, {len(fingerprints)} now; the "
                "records match by index only if one is a prefix of the other)."
            )
            print(
                "        Resuming would match records against the wrong questions "
                "and silently answer nothing.\n"
                "        Use a different --out, or pass --no-resume to overwrite."
            )
            return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    run_batch_to_jsonl(
        pipeline,
        requests,
        args.out,
        resume=not args.no_resume,
    )

    meta_path.write_text(
        json.dumps(
            {
                "request_fingerprints": fingerprints,
                "requests": len(requests),
                "retrieval": str(args.retrieval),
                "adapter": args.adapter,
                "backend": args.backend,
                "tag": args.tag,
                "note": (
                    "Guards resume: re-running against this --out with a "
                    "different request set is refused rather than silently "
                    "answering nothing."
                ),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    records = load_jsonl(args.out)

    counts: Counter[str] = Counter()
    for record in records:
        for violation in record.get("validation", {}).get("violations", []):
            counts[violation["code"]] += 1

    # Keyed to the answers file it describes. Naming it by backend and tag alone
    # meant two runs writing one directory overwrote each other's notes - and
    # the notes are the only record of what the adapter dropped, which is
    # exactly the information that must not vanish.
    notes_path = args.notes_out or args.out.with_name(
        args.out.stem + ".notes.json"
    )
    notes_path.parent.mkdir(parents=True, exist_ok=True)
    notes_path.write_text(
        json.dumps(
            {
                "schema_version": SCHEMA_VERSION,
                "prompt_version": PROMPT_VERSION,
                "generated_by": "scripts/generate_from_retrieval.py",
                "retrieval": str(args.retrieval),
                "adapter": args.adapter,
                "backend": args.backend,
                "tag": args.tag,
                "payloads_read": len(payloads),
                "requests_adapted": len(requests),
                "payload_errors": errors,
                "adaptation_notes": notes,
                "violation_counts": dict(sorted(counts.items())),
                "note": (
                    "One entry per payload whose adaptation was not lossless. "
                    "Empty means every hit became a citable passage. This file "
                    "describes the *input*; the answers file describes the output."
                ),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    answered = sum(
        1
        for r in records
        if r["result"]["evidence_status"] == "SUFFICIENT"
    )
    print()
    print(f"payloads read       {len(payloads)}")
    print(f"requests adapted    {len(requests)}  ({len(errors)} payload error(s))")
    print(f"answered            {answered}")
    print(f"refused             {len(records) - answered}")
    print(f"adaptation notes    {len(notes)}")
    print(f"violations          {dict(sorted(counts.items())) or '-'}")
    print()
    print(f"wrote {args.out}")
    print(f"wrote {notes_path}")
    return 0 if records else 2


if __name__ == "__main__":
    raise SystemExit(main())
