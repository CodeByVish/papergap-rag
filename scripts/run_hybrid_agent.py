"""Run P4's agent with real P2 retrieval, optional sections and cached BGE."""

import argparse
import json
import os
from pathlib import Path

from scripts.build_indexes import PINNED_REVISION, load_passages
from scripts.demo_hybrid import RERANKER_REVISION
from scripts.demo_p1 import _check_same_passages
from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker
from src.retrieval.scoped import SectionScopedRetriever


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--dense-index-dir", type=Path, required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument(
        "--cache-folder", type=Path, default=Path(".cache/huggingface/hub")
    )
    parser.add_argument(
        "--score-cache", type=Path, default=Path(".cache/p2/scores.sqlite")
    )
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--bge", action="store_true")
    parser.add_argument("--section", help="Exact section for every retrieval round")
    parser.add_argument(
        "--gap-sections",
        type=Path,
        help="JSON object mapping gap labels to exact section names",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cache = None
    try:
        if args.output.exists():
            raise FileExistsError("Choose a new output path")
        if args.local_files_only:
            os.environ["HF_HUB_OFFLINE"] = os.environ["TRANSFORMERS_OFFLINE"] = "1"
        mapping = json.loads(args.gap_sections.read_text()) if args.gap_sections else {}
        if not isinstance(mapping, dict) or any(
            k not in {g.value for g in GapLabel}
            or not isinstance(v, str)
            or not v.strip()
            for k, v in mapping.items()
        ):
            raise ValueError(
                "gap-sections must map valid gap labels to nonempty section names"
            )
        passages = load_passages(args.passages)
        sparse = BM25Retriever(passages)
        dense = DenseRetriever.load(
            args.dense_index_dir,
            revision=PINNED_REVISION,
            cache_folder=args.cache_folder,
            local_files_only=args.local_files_only,
        )
        _check_same_passages(args.dense_index_dir, passages)
        if args.bge:
            cache = BGEReranker(
                revision=RERANKER_REVISION,
                cache_folder=str(args.cache_folder),
                local_files_only=args.local_files_only,
            ).cached(args.score_cache)
        backend = HybridRetriever(
            SectionScopedRetriever(sparse.retrieve, passages),
            SectionScopedRetriever(dense.retrieve, passages),
            scorer=cache,
        )
        app = build_agent_graph(
            backend.retrieve,
            section_selector=lambda state: (
                args.section or mapping.get(state.gap_label.value)
            ),
        )
        result = app.invoke(AgentState(question=args.query, paper_id=args.paper_id))
        result = AgentState.model_validate(result).model_dump(mode="json")
        result["scorer_cache"] = (
            {"hits": cache.hits, "misses": cache.misses} if cache else None
        )
        result["policy"] = (
            "P4 keyword planner/critic mocks; real retrieval; caller-supplied exact section policy"
        )
        rendered = json.dumps(result, indent=2, allow_nan=False) + "\n"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as out:
            out.write(rendered)
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))
    finally:
        if cache is not None:
            cache.close()


if __name__ == "__main__":
    main()
