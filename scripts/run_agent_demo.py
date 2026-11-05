"""Demo: run the agent on synthetic P2-shaped retrieval results.

Usage:
    python scripts/run_agent_demo.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState
from src.retrieval.schemas import RetrievedPassage

FIXTURE = ROOT / "tests" / "fixtures" / "mock_reranked_results.json"
QUESTION = "What accuracy did the model achieve?"
PAPER_ID = "mock-paper"


def load_hits() -> list[RetrievedPassage]:
    raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
    return [RetrievedPassage.model_validate(item) for item in raw["results"]]


def main() -> None:
    all_hits = load_hits()
    without_results = [h for h in all_hits if h.passage.section != "results"]

    def recovers_on_rewrite(query: str, paper_id: str, top_k: int):
        return all_hits if "results" in query.lower() else without_results

    def never_finds_results(query: str, paper_id: str, top_k: int):
        return without_results

    def returns_nothing(query: str, paper_id: str, top_k: int):
        return []

    scenarios = {
        "recovers after one retry": recovers_on_rewrite,
        "never finds results (exhausts retries)": never_finds_results,
        "empty retrieval": returns_nothing,
    }
    for name, retriever in scenarios.items():
        state = AgentState(question=QUESTION, paper_id=PAPER_ID)
        result = build_agent_graph(retriever).invoke(state)
        print(f"\n=== {name} ===")
        print(f"sufficient={result['sufficient']} rounds={result['retrieval_round']} "
              f"gap_label={result['gap_label'].value}")
        print("evidence_map:", json.dumps(result["evidence_map"]))
        for entry in result["retrieval_log"]:
            print(f"  round {entry['round']} (triggered_by={entry['triggered_by']}): "
                  f"query={entry['query']!r} -> {entry['passage_ids']}")


if __name__ == "__main__":
    main()
