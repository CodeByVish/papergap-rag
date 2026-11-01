"""Run the static and adaptive agent arms on real retrieval and write the records.

One process owns one generator (a single A40 fits one Qwen3-8B), shared by the
adaptive arm's critic and by P5's answer step:

    python -m scripts.run_agent_experiment \\
        --passages data/processed/passages.jsonl \\
        --dense-index-dir indexes/p2-qasper-development \\
        --from-qa data/processed/qa.jsonl --split validation --limit 100 \\
        --critic generator --generator vllm --model-id "$P5_ROOT/models/Qwen3-8B" \\
        --answers p5 --out-dir runs/p4/dev-001

Outputs in --out-dir: static.jsonl, adaptive.jsonl (one export record per question,
written as each finishes, so a killed job can `--resume`), metrics.json, metrics.md
and run_manifest.json. Without `--critic generator` the adaptive arm uses the
rule-based critic; without `--answers p5` no generation runs. The test split is
refused. See docs/P4_AGENT.md and scripts/cluster/run_agent_experiment.sbatch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time
from collections.abc import Callable, Sequence
from importlib import metadata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent.experiments import (
    AnswerFn,
    ExperimentItem,
    compute_metrics,
    format_table,
    paired_recall_gain,
    run_system,
)

ARMS = ("static", "adaptive")
# P5's frozen generation settings (their message of 2026-10-29); the backend default is 768.
FROZEN_PROMPT_VERSION = "p5-grounded-qa-v7"
FROZEN_MAX_NEW_TOKENS = 1024
ALLOWED_SPLITS = ("train", "validation")
PACKAGES = (
    "torch", "vllm", "transformers", "sentence-transformers", "faiss-cpu",
    "rank-bm25", "langgraph", "pydantic",
)


# --------------------------------------------------------------------------- #
# Items
# --------------------------------------------------------------------------- #

def load_items_jsonl(path: Path) -> list[ExperimentItem]:
    """Read items: {question_id, question, paper_id, gold_passage_ids?, answerable?}."""
    items, seen = [], set()
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        for key in ("question_id", "question", "paper_id"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f"{path}:{number}: {key} must be a nonempty string")
        if row["question_id"] in seen:
            raise ValueError(f"{path}:{number}: duplicate question_id {row['question_id']}")
        seen.add(row["question_id"])
        gold = row.get("gold_passage_ids")
        answerable = row.get("answerable")
        if answerable is not None and not isinstance(answerable, bool):
            raise ValueError(f"{path}:{number}: answerable must be true, false or absent")
        items.append(
            ExperimentItem(
                question_id=row["question_id"],
                question=row["question"],
                paper_id=row["paper_id"],
                gold_passage_ids=frozenset(gold) if gold else None,
                answerable=answerable,
            )
        )
    if not items:
        raise ValueError(f"{path}: no items")
    return items


def load_qa_items(qa_path: Path, passages: Sequence[Any], split: str, limit: int | None
                  ) -> list[ExperimentItem]:
    """Development items from qa.jsonl: one split, papers present in `passages`.

    Gold passages are the approximation from scripts/smoke_agent_real.py, not P3's
    evidence mapping. Selection is deterministic and spread across papers.
    """
    if split not in ALLOWED_SPLITS:
        raise ValueError(f"split must be one of {ALLOWED_SPLITS}; the test split is refused")
    from scripts.smoke_agent_real import approximate_gold

    by_paper: dict[str, list[Any]] = {}
    for passage in passages:
        by_paper.setdefault(passage.paper_id, []).append(passage)
    items = []
    with qa_path.open(encoding="utf-8") as source:
        for line in source:
            row = json.loads(line)
            if row["source_split"] != split or row["paper_id"] not in by_paper:
                continue
            answers = [a["answer"] for a in row["answers"]]
            answerable = not all(a["unanswerable"] for a in answers)
            evidence = [e for a in answers for e in a["evidence"]]
            gold = approximate_gold(evidence, by_paper[row["paper_id"]]) if answerable else None
            items.append(
                ExperimentItem(row["question_id"], row["question"], row["paper_id"],
                               gold or None, answerable)
            )
    items.sort(key=lambda item: (item.paper_id, item.question_id))
    if limit is not None and limit < len(items):
        step = len(items) / limit
        items = [items[int(i * step)] for i in range(limit)]
    if not items:
        raise ValueError(f"no {split} questions found for the papers in the passages file")
    return items


# --------------------------------------------------------------------------- #
# Running and resuming
# --------------------------------------------------------------------------- #

def read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def is_complete(record: dict[str, Any], expect_answers: bool) -> bool:
    """A record to keep on resume: no agent error, and no failed or missing answer."""
    if "error" in record:
        return False
    return not expect_answers or "answer" in record


def run_arm(
    name: str,
    items: Sequence[ExperimentItem],
    retriever: Callable[..., Any],
    out_dir: Path,
    *,
    adaptive: bool,
    critic_client: Any = None,
    answer_fn: AnswerFn | None = None,
    max_retries: int = 2,
    top_k: int = 5,
    section_selector: Callable[..., Any] | None = None,
    resume: bool = False,
    log: Callable[[str], None] = print,
) -> list[dict[str, Any]]:
    """Run one arm, appending each record to <out_dir>/<name>.jsonl as it finishes."""
    path = out_dir / f"{name}.jsonl"
    kept: list[dict[str, Any]] = []
    if path.exists():
        if not resume:
            raise FileExistsError(f"{path} exists; pass --resume to continue it")
        kept = [r for r in read_records(path) if is_complete(r, answer_fn is not None)]
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in kept),
                        encoding="utf-8")
    done = {r["question_id"] for r in kept}
    todo = [item for item in items if item.question_id not in done]
    log(f"[{name}] {len(kept)} done, {len(todo)} to run")
    started = time.perf_counter()
    finished = len(kept)

    with path.open("a", encoding="utf-8") as out:
        def write(record: dict[str, Any]) -> None:
            nonlocal finished
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            finished += 1
            if finished % 10 == 0 or finished == len(items):
                log(f"[{name}] {finished}/{len(items)}  {time.perf_counter() - started:.0f}s")

        fresh = run_system(
            todo, retriever, adaptive=adaptive, critic_client=critic_client,
            max_retries=max_retries, top_k=top_k, answer_fn=answer_fn, on_record=write,
            section_selector=section_selector,
        ) if todo else []
    by_id = {r["question_id"]: r for r in [*kept, *fresh]}
    return [by_id[item.question_id] for item in items if item.question_id in by_id]


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def environment() -> dict[str, Any]:
    versions = {}
    for package in PACKAGES:
        try:
            versions[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            versions[package] = None
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                                text=True, check=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                                    capture_output=True, text=True, check=True).stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        commit, dirty = None, None
    return {"python": platform.python_version(), "platform": platform.platform(),
            "git_commit": commit, "git_dirty": dirty, "packages": versions}


def summarise(arm_records: dict[str, list[dict[str, Any]]], items: Sequence[ExperimentItem]
              ) -> dict[str, Any]:
    results = {arm: compute_metrics(records, items) for arm, records in arm_records.items()}
    summary: dict[str, Any] = {"metrics": results}
    if set(arm_records) == set(ARMS):
        summary["paired_recall_gain"] = paired_recall_gain(
            arm_records["static"], arm_records["adaptive"], items)
    return summary


def write_outputs(out_dir: Path, summary: dict[str, Any], manifest: dict[str, Any]) -> None:
    (out_dir / "metrics.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (out_dir / "metrics.md").write_text(format_table(summary["metrics"]) + "\n", encoding="utf-8")
    (out_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Wiring (lazy imports: this file must import on a machine without the GPU stack)
# --------------------------------------------------------------------------- #

def build_retriever(args: argparse.Namespace, passages: list[Any]):
    from scripts.build_indexes import PINNED_REVISION
    from scripts.demo_hybrid import RERANKER_REVISION
    from scripts.demo_p1 import _check_same_passages
    from src.retrieval.bm25_retriever import BM25Retriever
    from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
    from src.retrieval.hybrid_retriever import HybridRetriever
    from src.retrieval.reranker import BGEReranker
    from src.retrieval.scoped import SectionScopedRetriever

    _check_same_passages(args.dense_index_dir, passages)
    sparse = BM25Retriever(passages).retrieve
    dense = DenseRetriever.load(
        args.dense_index_dir, model_name=DEFAULT_MODEL_NAME, revision=PINNED_REVISION,
        device=args.device, cache_folder=args.cache_folder, local_files_only=args.local_files_only,
    ).retrieve
    if args.scoped:
        sparse, dense = SectionScopedRetriever(sparse, passages), SectionScopedRetriever(dense, passages)
    scorer = None
    if args.bge:
        scorer = BGEReranker(revision=RERANKER_REVISION, device=args.device,
                             cache_folder=str(args.cache_folder),
                             local_files_only=args.local_files_only)
        if args.score_cache:
            scorer = scorer.cached(args.score_cache)
    return HybridRetriever(sparse, dense, scorer=scorer, candidate_k=args.candidate_k).retrieve


def prompt_version() -> str:
    from src.generation import PROMPT_VERSION

    return PROMPT_VERSION


def build_generation(args: argparse.Namespace):
    """(generator, critic_client, answer_fn); all None when neither is requested."""
    if args.critic != "generator" and args.answers != "p5":
        return None, None, None
    try:
        from src.generation import PROMPT_VERSION, GroundedQAPipeline, make_answer_fn
        from src.generation.generators import get_generator
    except ImportError as error:
        raise SystemExit(
            f"P5's generation package is not importable ({error}); run from a checkout "
            "that contains src/generation (on main)."
        ) from error
    from src.agent.qwen_client import GeneratorChatClient

    if args.answers == "p5" and PROMPT_VERSION != args.expect_prompt_version:
        raise SystemExit(
            f"P5 prompt is {PROMPT_VERSION!r}, expected {args.expect_prompt_version!r}; "
            "update the checkout or pass --expect-prompt-version deliberately"
        )
    kwargs = {"model_id": args.model_id} if args.model_id else {}
    if args.generator != "mock":
        kwargs["max_new_tokens"] = args.max_new_tokens
    generator = get_generator(args.generator, **kwargs)
    critic = GeneratorChatClient(generator) if args.critic == "generator" else None
    answer = make_answer_fn(GroundedQAPipeline(generator)) if args.answers == "p5" else None
    return generator, critic, answer


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("--passages", type=Path, required=True)
    p.add_argument("--dense-index-dir", type=Path, required=True)
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--items", type=Path, help="JSONL of question items")
    source.add_argument("--from-qa", type=Path, help="qa.jsonl (development splits only)")
    p.add_argument("--split", default="validation", help="with --from-qa: train or validation")
    p.add_argument("--limit", type=int, help="with --from-qa: number of questions")
    p.add_argument("--out-dir", type=Path, required=True)
    p.add_argument("--arms", nargs="+", choices=ARMS, default=list(ARMS))
    p.add_argument("--critic", choices=["rules", "generator"], default="rules")
    p.add_argument("--answers", choices=["none", "p5"], default="none")
    p.add_argument("--generator", default="vllm", help="P5 backend: vllm, transformers, mock")
    p.add_argument("--model-id", help="model path or hub id for the generator")
    p.add_argument("--max-new-tokens", type=int, default=FROZEN_MAX_NEW_TOKENS,
                   help="answer token budget (P5's frozen v7 value; the backend default is 768)")
    p.add_argument("--expect-prompt-version", default=FROZEN_PROMPT_VERSION,
                   help="refuse to run answers if P5's PROMPT_VERSION differs")
    p.add_argument("--scoped", action="store_true", help="per-paper section-scoped retries")
    p.add_argument("--bge", action="store_true", help="add the BGE reranker")
    p.add_argument("--score-cache", type=Path, help="persistent reranker score cache (SQLite)")
    p.add_argument("--candidate-k", type=int, default=20)
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--max-retries", type=int, default=2)
    p.add_argument("--device", default="cpu", help="device for the retrieval models")
    p.add_argument("--cache-folder", type=Path, default=ROOT / ".cache/huggingface/hub")
    p.add_argument("--local-files-only", action="store_true")
    p.add_argument("--resume", action="store_true", help="continue a killed run in --out-dir")
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    from scripts.build_indexes import load_passages

    if args.out_dir.exists() and any(args.out_dir.iterdir()) and not args.resume:
        raise SystemExit(f"{args.out_dir} is not empty; choose a new --out-dir or pass --resume")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    passages = load_passages(args.passages)
    items = (load_items_jsonl(args.items) if args.items
             else load_qa_items(args.from_qa, passages, args.split, args.limit))
    print(f"{len(passages)} passages, {len(items)} questions, "
          f"{sum(1 for i in items if i.gold_passage_ids)} with gold passages")

    # Engine first: vLLM checks free GPU memory at load, so resident retrieval models
    # (--device cuda) would make it fail. The default retrieval device is the CPU.
    generator, critic, answer_fn = build_generation(args)
    retriever = build_retriever(args, passages)
    retriever(items[0].question, items[0].paper_id, args.top_k)  # warm up before timing
    selector = None
    if args.scoped:
        from src.agent.sections import make_section_selector
        selector = make_section_selector(passages)

    started = time.time()
    arm_records = {}
    for arm in args.arms:
        arm_records[arm] = run_arm(
            arm, items, retriever, args.out_dir, adaptive=arm == "adaptive",
            critic_client=critic, answer_fn=answer_fn, max_retries=args.max_retries,
            top_k=args.top_k, section_selector=selector, resume=args.resume)

    summary = summarise(arm_records, items)
    manifest = {
        "args": {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        "started": started, "finished": time.time(),
        "questions": len(items),
        "passages_sha256": sha256_of(args.passages),
        "items_sha256": sha256_of(args.items) if args.items else None,
        "critic_client": ({"calls": critic.calls, "escalations": critic.escalations}
                          if critic is not None else None),
        "generator": generator.info() if generator is not None and hasattr(generator, "info") else None,
        "prompt_version": prompt_version() if answer_fn is not None else None,
        "environment": environment(),
    }
    write_outputs(args.out_dir, summary, manifest)
    print("\n" + format_table(summary["metrics"]))
    print(f"\nwrote {args.out_dir}")


if __name__ == "__main__":
    main()
