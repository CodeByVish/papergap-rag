"""Run from repo root: python -m scripts.demo_p2 [--bge]."""

import argparse
import json
from pathlib import Path

from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker
from src.retrieval.schemas import RetrievalHit


class MockScorer:
    """Fixed synthetic scores to exercise wiring, never an evaluation result."""

    def score(self, query, texts):
        return [3.0 if "82.4" in text else -1.0 for text in texts]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bge", action="store_true", help="Download/load real BGE weights"
    )
    parser.add_argument("--revision", help="Optional Hugging Face model commit")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    fixture = (
        Path(__file__).resolve().parents[1]
        / "tests/fixtures/mock_retrieval_results.json"
    )
    data = json.loads(fixture.read_text())

    def source(name):
        def retrieve(query, paper_id, top_k):
            return [
                RetrievalHit.model_validate(hit)
                for hit in data[name]
                if hit["passage"]["paper_id"] == paper_id
            ][:top_k]

        return retrieve

    scorer = BGEReranker(revision=args.revision) if args.bge else MockScorer()
    backend = HybridRetriever(source("bm25"), source("dense"), scorer=scorer)
    output = {
        "synthetic_passages": True,
        "scorer": "bge" if args.bge else "mock",
        "query": data["query"],
        "paper_id": data["paper_id"],
        "results": [
            hit.model_dump()
            for hit in backend.retrieve(data["query"], data["paper_id"], top_k=3)
        ],
    }
    rendered = json.dumps(output, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
