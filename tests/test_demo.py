"""Tests for the live-demo record hook."""

import json

import pytest

from src.agent.demo import make_record_fn
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore


def hit(passage_id, section="Method", text="We encode passages."):
    return RetrievedPassage(
        passage=Passage(passage_id=passage_id, paper_id="p", title="t", section=section,
                        chunk_number=0, text=text),
        rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)},
        rrf_score=0.1,
    )


METHOD = hit("method")
GOLD = hit("gold", "Results", "Our model achieves 82.4 F1 and 91% accuracy.")


def retriever(query, paper_id, top_k):
    return [METHOD, GOLD] if "results" in query.lower() else [METHOD]


class OracleChat:
    def __init__(self):
        self.calls = 0

    def chat(self, messages):
        self.calls += 1
        if "[gold]" in messages[-1]["content"]:
            return json.dumps({"sufficient": True, "gap_label": "NONE",
                               "missing_components": [], "reason": "Result found."})
        return json.dumps({"sufficient": False, "gap_label": "MISSING_RESULT",
                           "missing_components": ["reported result"], "reason": "No result."})


def test_returns_a_full_exported_record():
    record_fn = make_record_fn(retriever, OracleChat())
    record = record_fn("What accuracy did the model achieve?", "p", 5, "req-1")
    assert record["question_id"] == "req-1" and record["paper_id"] == "p"
    assert record["retrieval_round"] == 2 and record["sufficient"] is True
    assert [e["source"] for e in record["critic_log"]] == ["llm", "llm"]
    assert {h["passage"]["passage_id"] for h in record["retrieved_passages"]} == {"method", "gold"}
    assert record["elapsed_s"] >= 0
    json.dumps(record)  # JSON-safe, as the server needs


def test_generates_a_request_id_when_none_is_given():
    record = make_record_fn(retriever, None)("What accuracy did it get?", "p")
    assert record["question_id"].startswith("ui-")


def test_without_a_critic_client_the_rules_decide():
    record = make_record_fn(retriever, None)("What accuracy did the model achieve?", "p")
    assert all(e["source"] == "rules" for e in record["critic_log"])


def test_max_retries_zero_stops_after_one_round():
    record = make_record_fn(retriever, OracleChat(), max_retries=0)(
        "What accuracy did the model achieve?", "p")
    assert record["retrieval_round"] == 1


def test_blank_question_is_a_value_error_for_the_server_to_report_as_400():
    with pytest.raises(ValueError):
        make_record_fn(retriever, None)("   ", "p")


def test_graph_is_compiled_once_per_top_k(monkeypatch):
    import src.agent.demo as demo

    built = []
    real = demo.build_agent_graph
    monkeypatch.setattr(demo, "build_agent_graph",
                        lambda *a, **k: built.append(k["top_k"]) or real(*a, **k))
    record_fn = make_record_fn(retriever, None)
    for top_k in (5, 5, 3):
        record_fn("What accuracy did it get?", "p", top_k)
    assert built == [5, 3]


# --- factory configuration ------------------------------------------------

def test_factory_names_the_missing_environment_variable(monkeypatch):
    from scripts import demo_agent_factory as f

    monkeypatch.delenv("DEMO_AGENT_DENSE_INDEX", raising=False)
    with pytest.raises(RuntimeError, match="DEMO_AGENT_DENSE_INDEX"):
        f.retrieval_args()


def test_factory_reads_retrieval_settings_from_the_environment(monkeypatch):
    from scripts import demo_agent_factory as f

    monkeypatch.setenv("DEMO_AGENT_DENSE_INDEX", "/idx")
    monkeypatch.setenv("DEMO_AGENT_BGE", "1")
    monkeypatch.setenv("DEMO_AGENT_OFFLINE", "1")
    monkeypatch.delenv("DEMO_AGENT_SCOPED", raising=False)
    args = f.retrieval_args()
    assert str(args.dense_index_dir) == "/idx" and args.bge and args.local_files_only
    assert args.scoped and args.device == "cpu" and args.candidate_k == 20
