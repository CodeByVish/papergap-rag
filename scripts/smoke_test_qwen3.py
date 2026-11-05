#!/usr/bin/env python
"""Load Qwen3-8B and answer one grounded question end to end.

This is the model-serving confirmation the P5 brief asks for. It answers the
question "can Qwen3-8B be loaded and used for grounded generation here?" with a
single command, and it prints the three numbers that matter for planning a real
batch: load time, generation latency, and peak VRAM.

    # The shape check that needs no GPU at all:
    python scripts/smoke_test_qwen3.py --backend mock

    # On the cluster, safest first attempt:
    python scripts/smoke_test_qwen3.py --backend transformers --show-prompt

    # The production path, once the weights are cached locally:
    python scripts/smoke_test_qwen3.py --backend vllm --model /scratch/models/Qwen3-8B

Exit codes are chosen to be usable from a job script:

    0  loaded, answered, and passed validation cleanly
    1  could not load at all (setup problem: deps, GPU, or model path)
    2  loaded, but the answer was refused or downgraded (inspect the report)

A 2 is a real result, not a crash. Qwen3-8B will occasionally refuse a question
the synthetic passage does answer - that is a prompt-tuning signal, and the point
of running this before a 6-hour batch rather than after.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.generation.generators import BackendNotAvailable, get_generator  # noqa: E402
from src.generation.pipeline import GroundedQAPipeline, PipelineConfig  # noqa: E402
from src.generation.prompts.grounded_qa import PromptConfig, build_prompt  # noqa: E402
from src.generation.schema import GenerationRequest, RetrievedPassage  # noqa: E402

#: A tiny synthetic context whose answer is unambiguous, so a refusal or a
#: fabrication is attributable to the model or the prompt rather than to the
#: synthesised evidence being genuinely insufficient.
SYNTHETIC_PASSAGES = [
    RetrievedPassage(
        passage_id="smoke_results_04",
        text=(
            "The proposed model reaches 91.2 F1 on the SQuAD 2.0 test set, which "
            "is 2.4 points above the strongest reported baseline."
        ),
        score=0.81,
        paper_id="smoke",
        section="results",
    ),
    RetrievedPassage(
        passage_id="smoke_abstract_01",
        text=(
            "We introduce a retrieval-augmented reader that is trained end to end "
            "on 120000 question-answer pairs."
        ),
        score=0.66,
        paper_id="smoke",
        section="abstract",
    ),
]

SYNTHETIC_QUESTION = "How well does the proposed model perform on the SQuAD 2.0 test set?"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--backend", default="mock",
                        choices=["mock", "transformers", "vllm"])
    parser.add_argument("--model", default=None,
                        help="HF id or local path (defaults to the backend default)")
    parser.add_argument("--max-new-tokens", type=int, default=768)
    parser.add_argument("--max-model-len", type=int, default=32768)
    parser.add_argument("--gpu-memory-utilization", type=float, default=0.85)
    parser.add_argument("--allow-cpu", action="store_true",
                        help="transformers backend: run without CUDA (very slow)")
    parser.add_argument("--show-prompt", action="store_true",
                        help="print the fully rendered prompt before generating")
    parser.add_argument("--max-chars-per-passage", type=int, default=1200)
    return parser.parse_args(argv)


def build_generator(args: argparse.Namespace):
    """Construct the requested backend, leaving model defaulting to the backend."""
    kwargs: dict = {}
    if args.model:
        kwargs["model_id"] = args.model

    if args.backend == "transformers":
        kwargs.update(
            max_new_tokens=args.max_new_tokens,
            temperature=0.0,          # greedy: the smoke test must be reproducible
            allow_cpu=args.allow_cpu,
        )
    elif args.backend == "vllm":
        kwargs.update(
            max_new_tokens=args.max_new_tokens,
            temperature=0.0,
            max_model_len=args.max_model_len,
            gpu_memory_utilization=args.gpu_memory_utilization,
        )
    return get_generator(args.backend, **kwargs)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    prompt_config = PromptConfig(max_chars_per_passage=args.max_chars_per_passage)
    request = GenerationRequest(
        question=SYNTHETIC_QUESTION,
        passages=SYNTHETIC_PASSAGES,
        retrieval_rounds=1,
        request_id="smoke-001",
    )

    if args.show_prompt:
        print("=" * 72)
        print("RENDERED PROMPT")
        print("=" * 72)
        print(build_prompt(request, prompt_config))
        print()

    generator = build_generator(args)
    print("=" * 72)
    print("LOADING")
    print("=" * 72)
    print(f"  backend : {generator.name}")
    print(f"  model   : {generator.model_id}")

    load_start = time.perf_counter()
    try:
        generator.load()
    except BackendNotAvailable as exc:
        print()
        print("CANNOT LOAD:", exc)
        return 1
    except Exception as exc:  # noqa: BLE001 - a load failure is the finding here
        print()
        print(f"CANNOT LOAD: {type(exc).__name__}: {exc}")
        return 1
    load_seconds = time.perf_counter() - load_start
    print(f"  loaded in {load_seconds:.1f}s")

    pipeline = GroundedQAPipeline(
        generator, config=PipelineConfig(prompt=prompt_config)
    )

    print()
    print("=" * 72)
    print("GENERATING")
    print("=" * 72)
    started = time.perf_counter()
    try:
        # The pipeline never raises on a bad response - it converts the failure
        # into a refusal with a report, which is the outcome this script wants to
        # print rather than a traceback.
        output = pipeline.answer(request)
    except Exception as exc:  # noqa: BLE001
        print(f"  generation failed: {type(exc).__name__}: {exc}")
        return 1
    elapsed = time.perf_counter() - started

    peak = getattr(generator, "peak_memory_gb", lambda: None)()
    print(f"  latency        : {elapsed:.2f}s")
    if peak:
        print(f"  peak VRAM      : {peak:.2f} GiB")
    if output.raw_text:
        print(f"  raw response   : {len(output.raw_text)} chars")

    print()
    print("=" * 72)
    print("VALIDATED RESULT (the frozen P6 schema)")
    print("=" * 72)
    print(json.dumps(output.result.to_wire(), indent=2, ensure_ascii=False))

    print()
    print("VALIDATION REPORT")
    print("-" * 72)
    print(f"  status         : {output.result.evidence_status.value}")
    print(f"  downgraded     : {output.report.downgraded} "
          f"({output.report.downgrade_reason or 'n/a'})")
    print(f"  violations     : {', '.join(output.report.codes()) or 'none'}")
    for violation in output.report.violations:
        print(f"    [{violation.severity.value}] {violation.code.value}: "
              f"{violation.message}")
    if output.diagnostics and output.diagnostics.drifted:
        print(f"  format drift   : {output.diagnostics.model_dump(exclude_defaults=True)}")

    generator.unload()

    print()
    if output.report.ok and not output.result.is_refusal:
        print("RESULT: loaded, answered, and passed validation. Ready for a batch.")
        return 0
    print("RESULT: loaded, but the answer was refused or downgraded - read the")
    print("        report above before committing to a full run.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
