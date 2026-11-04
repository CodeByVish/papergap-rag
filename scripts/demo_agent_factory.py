"""Factory for P5's demo server: runs the full P4 agent per typed question.

    python -m src.generation.server --record-fn scripts.demo_agent_factory:factory ...

The server calls `factory(pipeline)` once at start-up and `record_fn(question,
paper_id, top_k, request_id)` per request. The critic reuses `pipeline.generator`,
so no second model is loaded. Retrieval models stay on the CPU unless
`DEMO_AGENT_DEVICE` says otherwise (vLLM checks free GPU memory when it loads).

Configuration (environment variables):

    PAPERGAP_CORPUS          the 365/40-word passages.jsonl         (required; the dense
                             index and the server's --passages-from must be this same file)
    PAPERGAP_DENSE_INDEX     dense index directory                 (required)
    HF_HOME                  Hugging Face home; models are read from $HF_HOME/hub
                             when that exists, else from $HF_HOME  (optional)
    DEMO_AGENT_SCOPED        1 = section-scoped retries            (default 1)
    DEMO_AGENT_BGE           1 = add the BGE reranker              (default 0)
    DEMO_AGENT_SCORE_CACHE   reranker score cache (SQLite)         (optional)
    DEMO_AGENT_CACHE_FOLDER  hub cache, overrides HF_HOME          (optional)
    DEMO_AGENT_OFFLINE       1 = never touch the network           (default 0)
    DEMO_AGENT_DEVICE        device for retrieval models           (default cpu)
    DEMO_AGENT_CANDIDATE_K   candidates per retriever              (default 20)
    DEMO_AGENT_MAX_RETRIES   retry budget                          (default 2)
    DEMO_AGENT_CRITIC_VIEW   generator = the critic reads exactly what the server's
                             prompt renders (default); pool = every retrieved passage

The BM25 term index is rebuilt in memory from PAPERGAP_CORPUS, so a BM25 index
directory (PAPERGAP_BM25_INDEX) is not read here.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

from src.agent.critic import pool_view
from src.agent.demo import RecordFn, make_record_fn


def _flag(name: str, default: bool) -> bool:
    return os.environ.get(name, "1" if default else "0") == "1"


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is not set; see the docstring of scripts/demo_agent_factory.py")
    return value


def _hub_cache() -> Path:
    explicit = os.environ.get("DEMO_AGENT_CACHE_FOLDER")
    if explicit:
        return Path(explicit)
    home = os.environ.get("HF_HOME")
    if home:
        return Path(home) / "hub" if (Path(home) / "hub").is_dir() else Path(home)
    return Path.home() / ".cache/huggingface/hub"


def retrieval_args() -> argparse.Namespace:
    """The retrieval settings `scripts.run_agent_experiment.build_retriever` reads."""
    return argparse.Namespace(
        dense_index_dir=Path(_required("PAPERGAP_DENSE_INDEX")),
        scoped=_flag("DEMO_AGENT_SCOPED", True),
        bge=_flag("DEMO_AGENT_BGE", False),
        score_cache=Path(os.environ["DEMO_AGENT_SCORE_CACHE"])
        if os.environ.get("DEMO_AGENT_SCORE_CACHE") else None,
        device=os.environ.get("DEMO_AGENT_DEVICE", "cpu"),
        cache_folder=_hub_cache(),
        local_files_only=_flag("DEMO_AGENT_OFFLINE", False),
        candidate_k=int(os.environ.get("DEMO_AGENT_CANDIDATE_K", "20")),
    )


def critic_view_for(pipeline: Any):
    """The passages and text the critic reads, from the server's own prompt budget."""
    mode = os.environ.get("DEMO_AGENT_CRITIC_VIEW", "generator")
    if mode == "pool":
        return pool_view
    if mode != "generator":
        raise RuntimeError(f"DEMO_AGENT_CRITIC_VIEW must be 'generator' or 'pool', got {mode!r}")
    from src.agent.generator_view import make_generator_view

    return make_generator_view(getattr(getattr(pipeline, "config", None), "prompt", None))


def factory(pipeline: Any) -> RecordFn:
    from scripts.build_indexes import load_passages
    from scripts.run_agent_experiment import build_retriever
    from src.agent.qwen_client import GeneratorChatClient
    from src.agent.sections import make_section_selector

    args = retrieval_args()
    passages = load_passages(Path(_required("PAPERGAP_CORPUS")))
    retriever = build_retriever(args, passages)
    return make_record_fn(
        retriever,
        GeneratorChatClient(pipeline.generator),
        max_retries=int(os.environ.get("DEMO_AGENT_MAX_RETRIES", "2")),
        section_selector=make_section_selector(passages) if args.scoped else None,
        critic_view=critic_view_for(pipeline),
    )
