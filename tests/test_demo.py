"""Tests for the live-demo record hook."""

import json
import re

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
    return [METHOD, GOLD] if "result" in query.lower() else [METHOD]


class OracleChat:
    def __init__(self):
        self.calls = 0

    def chat(self, messages):
        self.calls += 1
        found = re.search(r"\[(p\d+)\] section: Results\n[^\n]*91% accuracy", messages[-1]["content"])
        if found:
            return json.dumps({"sufficient": True, "gap_label": "NONE",
                               "missing_components": [], "reason": "Result found.",
                               "supporting_passage_ids": [found.group(1)],
                               "evidence_quote": "Our model achieves 82.4 F1 and 91% accuracy"})
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

    monkeypatch.delenv("PAPERGAP_DENSE_INDEX", raising=False)
    with pytest.raises(RuntimeError, match="PAPERGAP_DENSE_INDEX"):
        f.retrieval_args()


def test_factory_reads_retrieval_settings_from_the_environment(monkeypatch):
    from scripts import demo_agent_factory as f

    monkeypatch.setenv("PAPERGAP_DENSE_INDEX", "/idx")
    monkeypatch.setenv("DEMO_AGENT_BGE", "1")
    monkeypatch.setenv("DEMO_AGENT_OFFLINE", "1")
    monkeypatch.delenv("DEMO_AGENT_SCOPED", raising=False)
    args = f.retrieval_args()
    assert str(args.dense_index_dir) == "/idx" and args.bge and args.local_files_only
    assert args.scoped and args.device == "cpu" and args.candidate_k == 20


def test_factory_finds_models_under_hf_home(monkeypatch, tmp_path):
    from scripts import demo_agent_factory as f

    monkeypatch.setenv("PAPERGAP_DENSE_INDEX", "/idx")
    monkeypatch.delenv("DEMO_AGENT_CACHE_FOLDER", raising=False)
    monkeypatch.setenv("HF_HOME", str(tmp_path))
    assert f.retrieval_args().cache_folder == tmp_path  # no hub/ subfolder: use HF_HOME itself
    (tmp_path / "hub").mkdir()
    assert f.retrieval_args().cache_folder == tmp_path / "hub"
    monkeypatch.setenv("DEMO_AGENT_CACHE_FOLDER", "/elsewhere")
    assert str(f.retrieval_args().cache_folder) == "/elsewhere"


def test_factory_names_the_missing_corpus_variable(monkeypatch):
    from scripts import demo_agent_factory as f

    monkeypatch.setenv("PAPERGAP_DENSE_INDEX", "/idx")
    monkeypatch.delenv("PAPERGAP_CORPUS", raising=False)
    with pytest.raises(RuntimeError, match="PAPERGAP_CORPUS"):
        f.factory(object())


# --- the critic reads the server's view ----------------------------------

class RecordingChat:
    def __init__(self):
        self.prompts = []

    def chat(self, messages):
        self.prompts.append(messages[-1]["content"])
        return json.dumps({"sufficient": False, "gap_label": "MISSING_RESULT",
                           "missing_components": ["reported result"], "reason": "No result."})


def test_record_fn_gives_the_critic_the_view_it_was_built_with():
    from src.agent.critic import ViewedPassage

    chat = RecordingChat()
    only_first = lambda state: [ViewedPassage(state.retrieved_passages[0].passage.passage_id,
                                              "section: Method\nonly this one")]
    make_record_fn(retriever, chat, max_retries=0, critic_view=only_first)("What F1?", "p", 5)
    assert "[p1] section: Method" in chat.prompts[0] and "[p2]" not in chat.prompts[0]


def test_record_fn_defaults_to_the_pool_view():
    chat = RecordingChat()
    make_record_fn(retriever, chat, max_retries=0)("What F1?", "p", 5)
    assert "[p1]" in chat.prompts[0]


def test_factory_critic_view_follows_the_servers_prompt_budget(monkeypatch):
    from scripts import demo_agent_factory as f
    from src.agent.critic import pool_view
    from src.agent.nodes import map_evidence, plan_question
    from src.agent.schemas import AgentState
    from src.generation.prompts.grounded_qa import PromptConfig

    state = AgentState(question="What accuracy did the model achieve?", paper_id="p",
                       retrieved_passages=[METHOD, GOLD], retrieval_round=1)
    state = state.model_copy(update=plan_question(state))
    state = state.model_copy(update=map_evidence(state))

    class Pipeline:  # P5's GroundedQAPipeline carries its prompt budget on .config.prompt
        config = type("Config", (), {"prompt": PromptConfig(max_passages=1)})()

    monkeypatch.delenv("DEMO_AGENT_CRITIC_VIEW", raising=False)
    assert len(f.critic_view_for(Pipeline())(state)) == 1
    assert len(f.critic_view_for(object())(state)) == 2  # no config: P5's default budget of 8
    monkeypatch.setenv("DEMO_AGENT_CRITIC_VIEW", "pool")
    assert f.critic_view_for(Pipeline()) is pool_view
    monkeypatch.setenv("DEMO_AGENT_CRITIC_VIEW", "bogus")
    with pytest.raises(RuntimeError, match="DEMO_AGENT_CRITIC_VIEW"):
        f.critic_view_for(Pipeline())


def test_each_answer_logs_what_the_critic_read(caplog):
    caplog.set_level("INFO", logger="src.agent.demo")
    make_record_fn(retriever, OracleChat())("What accuracy did the model achieve?", "p", 5, "req-9")
    line = next(r.getMessage() for r in caplog.records if r.name == "src.agent.demo")
    assert line.startswith("agent req-9: rounds=2 retrieved=2")
    assert "(1, 'llm', 1)" in line and "(2, 'llm', 2)" in line  # passages shown per round


def test_the_log_line_shows_the_generators_cut_on_a_wide_first_round(caplog):
    from src.agent.generator_view import make_generator_view

    many = lambda query, paper_id, top_k: [hit(f"w{i}", text=f"wide passage number {i}") for i in range(12)]
    caplog.set_level("INFO", logger="src.agent.demo")
    chat = RecordingChat()
    make_record_fn(many, chat, max_retries=0, critic_view=make_generator_view())("What F1?", "p", 12, "r")
    line = next(r.getMessage() for r in caplog.records if r.name == "src.agent.demo")
    assert "retrieved=12" in line and "(1, 'llm', 8)" in line  # 12 retrieved, 8 shown


# --- retrieval depth when the server does not pass one --------------------

def test_the_hook_uses_its_default_depth_when_called_with_question_and_paper_only(monkeypatch):
    import src.agent.demo as demo

    built = []
    real = demo.build_agent_graph
    monkeypatch.setattr(demo, "build_agent_graph",
                        lambda *a, **k: built.append(k["top_k"]) or real(*a, **k))
    record_fn = make_record_fn(retriever, None, default_top_k=10)
    record_fn("What accuracy did it get?", "p")  # how P5's server calls it
    record_fn("What accuracy did it get?", "p", 3)  # an explicit depth still wins
    assert built == [10, 3]


def test_the_default_depth_is_five():
    import src.agent.demo as demo

    built = []
    real = demo.build_agent_graph
    demo.build_agent_graph = lambda *a, **k: built.append(k["top_k"]) or real(*a, **k)
    try:
        make_record_fn(retriever, None)("What accuracy did it get?", "p")
    finally:
        demo.build_agent_graph = real
    assert built == [5]


def test_factory_reads_the_depth_from_the_environment(monkeypatch):
    from types import SimpleNamespace

    import scripts.build_indexes as build_indexes
    import scripts.run_agent_experiment as run_agent_experiment
    import src.agent.demo as demo
    from scripts import demo_agent_factory as f

    built = []
    real = demo.build_agent_graph
    monkeypatch.setattr(demo, "build_agent_graph",
                        lambda *a, **k: built.append(k["top_k"]) or real(*a, **k))
    monkeypatch.setattr(build_indexes, "load_passages", lambda path: [])
    monkeypatch.setattr(run_agent_experiment, "build_retriever", lambda args, passages: retriever)
    monkeypatch.setenv("PAPERGAP_CORPUS", "corpus.jsonl")
    monkeypatch.setenv("PAPERGAP_DENSE_INDEX", "/idx")
    monkeypatch.setenv("DEMO_AGENT_CRITIC_VIEW", "pool")
    pipeline = SimpleNamespace(generator=object())

    monkeypatch.setenv("DEMO_AGENT_TOP_K", "10")
    f.factory(pipeline)("What accuracy did it get?", "p")
    monkeypatch.delenv("DEMO_AGENT_TOP_K")
    f.factory(pipeline)("What accuracy did it get?", "p")
    assert built == [10, 8]  # explicit override or persistent demo default


def test_progress_is_reported_and_the_record_is_unchanged():
    lines = []
    plain = make_record_fn(retriever, OracleChat())("What accuracy did the model achieve?", "p", 5, "r")
    live = make_record_fn(retriever, OracleChat(), on_progress=lambda line, step, active: lines.append(line))(
        "What accuracy did the model achieve?", "p", 5, "r")
    for record in (plain, live):
        record.pop("elapsed_s")
        for entry in record["retrieval_log"]:  # Wall-clock timings differ between runs.
            entry.pop("retrieval_ms", None), entry.pop("scoped_retrieval_ms", None)
    assert live == plain
    assert any("kept" in line for line in lines) and any("Evidence check" in line for line in lines)
    assert lines[-1].startswith("Stopped searching")
