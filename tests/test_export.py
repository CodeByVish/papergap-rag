"""Tests for the agent -> P5/P6 handoff record."""

import json

from src.agent.export import export_record, to_jsonl_line
from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore

TEXT = "Our model achieves 82.4 F1."


def _hit() -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id="p1", paper_id="paper", title="t", section="Results",
                        chunk_number=0, text=TEXT),
        rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)},
        rrf_score=0.1,
    )


def _run(question_id="q-7") -> dict:
    graph = build_agent_graph(lambda query, paper_id, top_k: [_hit()])
    return graph.invoke(
        AgentState(question="What accuracy was achieved?", paper_id="paper",
                   question_id=question_id)
    )


def test_question_id_passes_through_the_graph():
    assert _run()["question_id"] == "q-7"
    assert _run(question_id=None)["question_id"] is None


def test_record_is_json_serialisable_and_includes_passage_text():
    record = export_record(_run())
    json.dumps(record)  # raises if anything is not JSON-safe
    assert record["question_id"] == "q-7"
    assert record["retrieved_passages"][0]["passage"]["text"] == TEXT
    assert record["gap_label"] == "NONE"  # enum exported as its value
    assert record["question_type"] == "result"
    assert record["evidence_map"] == {"result": ["p1"]}
    assert record["retrieval_round"] == 1
    assert record["retrieval_log"][0]["passage_ids"] == ["p1"]
    assert record["critic_log"][0]["source"] == "rules"


def test_jsonl_line_round_trips_to_agent_state():
    line = to_jsonl_line(_run())
    assert "\n" not in line
    restored = AgentState.model_validate(json.loads(line))
    assert restored.question_id == "q-7"
    assert restored.retrieved_passages[0].passage.passage_id == "p1"


def test_export_accepts_an_agent_state_directly():
    state = AgentState(question="q", paper_id="p")
    assert export_record(state)["retrieved_passages"] == []
