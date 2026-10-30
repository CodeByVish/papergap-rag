"""Factory for P5's demo server: runs the full P4 agent per typed question.

    python -m src.generation.server --record-fn scripts.demo_agent_factory:factory ...

The server calls `factory(pipeline)` once at start-up and `record_fn(question,
paper_id, top_k, request_id)` per request. The critic reuses `pipeline.generator`,
so no second model is loaded. Retrieval models stay on the CPU unless
`DEMO_AGENT_DEVICE` says otherwise (vLLM checks free GPU memory when it loads).

Configuration (environment variables):

    DEMO_AGENT_PASSAGES      passages.jsonl                        (required)
    DEMO_AGENT_DENSE_INDEX   dense index directory                 (required)
    DEMO_AGENT_SCOPED        1 = section-scoped retries            (default 1)
    DEMO_AGENT_BGE           1 = add the BGE reranker              (default 0)
    DEMO_AGENT_SCORE_CACHE   reranker score cache (SQLite)         (optional)
    DEMO_AGENT_CACHE_FOLDER  Hugging Face hub cache                (optional)
    DEMO_AGENT_OFFLINE       1 = never touch the network           (default 0)
    DEMO_AGENT_DEVICE        device for retrieval models           (default cpu)
    DEMO_AGENT_CANDIDATE_K   candidates per retriever              (default 20)
    DEMO_AGENT_MAX_RETRIES   retry budget                          (default 2)
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

from src.agent.demo import RecordFn, make_record_fn


def _flag(name: str, default: bool) -> bool:
    return os.environ.get(name, "1" if default else "0") == "1"


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is not set; see the docstring of scripts/demo_agent_factory.py")
    return value


def retrieval_args() -> argparse.Namespace:
    """The retrieval settings `scripts.run_agent_experiment.build_retriever` reads."""
    cache = os.environ.get("DEMO_AGENT_CACHE_FOLDER")
    return argparse.Namespace(
        dense_index_dir=Path(_required("DEMO_AGENT_DENSE_INDEX")),
        scoped=_flag("DEMO_AGENT_SCOPED", True),
        bge=_flag("DEMO_AGENT_BGE", False),
        score_cache=Path(os.environ["DEMO_AGENT_SCORE_CACHE"])
        if os.environ.get("DEMO_AGENT_SCORE_CACHE") else None,
        device=os.environ.get("DEMO_AGENT_DEVICE", "cpu"),
        cache_folder=Path(cache) if cache else Path.home() / ".cache/huggingface/hub",
        local_files_only=_flag("DEMO_AGENT_OFFLINE", False),
        candidate_k=int(os.environ.get("DEMO_AGENT_CANDIDATE_K", "20")),
    )


def factory(pipeline: Any) -> RecordFn:
    from scripts.build_indexes import load_passages
    from scripts.run_agent_experiment import build_retriever
    from src.agent.qwen_client import GeneratorChatClient
    from src.agent.sections import make_section_selector

    args = retrieval_args()
    passages = load_passages(Path(_required("DEMO_AGENT_PASSAGES")))
    retriever = build_retriever(args, passages)
    return make_record_fn(
        retriever,
        GeneratorChatClient(pipeline.generator),
        max_retries=int(os.environ.get("DEMO_AGENT_MAX_RETRIES", "2")),
        section_selector=make_section_selector(passages) if args.scoped else None,
    )
