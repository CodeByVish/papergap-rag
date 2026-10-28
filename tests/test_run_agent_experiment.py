"""Tests for the experiment runner: items, resume, outputs and the P5 import guard."""

import json
import sys

import pytest

from scripts import run_agent_experiment as runner
from src.agent.experiments import ExperimentItem
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore


def passage(pid, section="Method", text="We encode passages.", paper="paper") -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(passage_id=pid, paper_id=paper, title="t", section=section,
                        chunk_number=0, text=text),
        rank=1, source_scores={"bm25": SourceScore(rank=1, score=1.0)}, rrf_score=0.1)


METHOD, GOLD = passage("method"), passage("gold", "Results", "Our model achieves 91% accuracy.")
ITEMS = [
    ExperimentItem("q1", "What accuracy did the model achieve?", "paper", frozenset({"gold"}), True),
    ExperimentItem("q2", "Who funded the study?", "paper", None, False),
]


def retriever(query, paper_id, top_k):
    return [METHOD, GOLD] if "results" in query.lower() else [METHOD]


def answer_fn(record):
    return {"request_id": record["question_id"], "result": {"answer": "x"}}


def read(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


# --- items ----------------------------------------------------------------

def test_load_items_jsonl(tmp_path):
    path = tmp_path / "items.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in [
        {"question_id": "a", "question": "q?", "paper_id": "p", "gold_passage_ids": ["x", "y"],
         "answerable": True},
        {"question_id": "b", "question": "q2?", "paper_id": "p"},
    ]) + "\n")
    first, second = runner.load_items_jsonl(path)
    assert first.gold_passage_ids == frozenset({"x", "y"}) and first.answerable is True
    assert second.gold_passage_ids is None and second.answerable is None


@pytest.mark.parametrize("rows", [
    [{"question_id": "a", "question": "q", "paper_id": "p"},
     {"question_id": "a", "question": "q", "paper_id": "p"}],  # duplicate id
    [{"question_id": "a", "question": " ", "paper_id": "p"}],
    [{"question_id": "a", "question": "q", "paper_id": "p", "answerable": "yes"}],
    [],
])
def test_load_items_jsonl_rejects_bad_files(tmp_path, rows):
    path = tmp_path / "items.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows))
    with pytest.raises(ValueError):
        runner.load_items_jsonl(path)


def test_load_qa_items_refuses_test_split(tmp_path):
    with pytest.raises(ValueError, match="test split"):
        runner.load_qa_items(tmp_path / "qa.jsonl", [], "test", None)


def test_load_qa_items_selects_one_split_spreads_and_marks_unanswerable(tmp_path):
    pytest.importorskip("faiss")  # the module imports the retrieval stack
    passages = [Passage(passage_id=f"p{i}", paper_id="paper", title="t", section="Results",
                        chunk_number=i, text=f"Our model reaches {80 + i} percent accuracy "
                                             "on the evaluation set of this paper.")
                for i in range(3)]
    rows = []
    for i in range(6):
        rows.append({"question_id": f"q{i}", "paper_id": "paper", "source_split": "validation",
                     "question": f"question {i}?", "answers": [{"answer": {
                         "evidence": [passages[i % 3].text], "unanswerable": i == 5}}]})
    rows.append({"question_id": "other", "paper_id": "paper", "source_split": "train",
                 "question": "train q?", "answers": [{"answer": {"evidence": [], "unanswerable": True}}]})
    rows.append({"question_id": "elsewhere", "paper_id": "absent", "source_split": "validation",
                 "question": "q?", "answers": [{"answer": {"evidence": [], "unanswerable": True}}]})
    qa = tmp_path / "qa.jsonl"
    qa.write_text("\n".join(json.dumps(r) for r in rows))

    items = runner.load_qa_items(qa, passages, "validation", None)
    assert [i.question_id for i in items] == [f"q{i}" for i in range(6)]
    assert items[0].gold_passage_ids == frozenset({"p0"}) and items[0].answerable is True
    assert items[5].answerable is False and items[5].gold_passage_ids is None
    assert [i.question_id for i in runner.load_qa_items(qa, passages, "validation", 3)] == ["q0", "q2", "q4"]


# --- arms, writing and resume --------------------------------------------

def test_run_arm_writes_one_line_per_question_as_it_goes(tmp_path):
    records = runner.run_arm("static", ITEMS, retriever, tmp_path, adaptive=False,
                             answer_fn=answer_fn, log=lambda _: None)
    written = read(tmp_path / "static.jsonl")
    assert [r["question_id"] for r in written] == ["q1", "q2"] == [r["question_id"] for r in records]
    assert all("answer" in r and r["retrieval_round"] == 1 for r in written)


def test_run_arm_refuses_to_overwrite_without_resume(tmp_path):
    runner.run_arm("static", ITEMS, retriever, tmp_path, adaptive=False, log=lambda _: None)
    with pytest.raises(FileExistsError, match="--resume"):
        runner.run_arm("static", ITEMS, retriever, tmp_path, adaptive=False, log=lambda _: None)


def test_resume_skips_finished_questions_and_retries_failed_ones(tmp_path):
    calls = []
    offline = {"down": True}

    def flaky(query, paper_id, top_k):
        calls.append(query)
        if "funded" in query and offline["down"]:
            raise RuntimeError("index offline")
        return [METHOD]

    first = runner.run_arm("static", ITEMS, flaky, tmp_path, adaptive=False, log=lambda _: None)
    assert "error" in first[1]  # q2 failed
    calls.clear()
    offline["down"] = False
    second = runner.run_arm("static", ITEMS, flaky, tmp_path, adaptive=False, resume=True,
                            log=lambda _: None)
    assert calls == ["Who funded the study?"]  # q1 was kept, only q2 re-run
    assert [r["question_id"] for r in second] == ["q1", "q2"] and "error" not in second[1]
    assert [r["question_id"] for r in read(tmp_path / "static.jsonl")] == ["q1", "q2"]


def test_resume_reruns_questions_whose_answer_failed(tmp_path):
    state = {"fail": True}

    def flaky_answer(record):
        if state["fail"] and record["question_id"] == "q1":
            raise RuntimeError("model OOM")
        return {"ok": True}

    runner.run_arm("static", ITEMS, retriever, tmp_path, adaptive=False,
                   answer_fn=flaky_answer, log=lambda _: None)
    state["fail"] = False
    records = runner.run_arm("static", ITEMS, retriever, tmp_path, adaptive=False,
                             answer_fn=flaky_answer, resume=True, log=lambda _: None)
    assert all(r["answer"] == {"ok": True} for r in records)


def test_adaptive_arm_uses_the_section_selector(tmp_path):
    seen = []

    def scoped(query, paper_id, top_k, **scope):
        seen.append(scope)
        return [METHOD, GOLD] if scope.get("section") == "Results" else [METHOD]

    def selector(state):
        return "Results" if state.gap_label.value == "MISSING_RESULT" else None

    records = runner.run_arm("adaptive", ITEMS[:1], scoped, tmp_path, adaptive=True,
                             section_selector=selector, log=lambda _: None)
    assert {"section": "Results"} in seen
    assert records[0]["retrieval_log"][-1]["section"] == "Results"


# --- summary and outputs --------------------------------------------------

def test_summary_and_outputs(tmp_path):
    arms = {arm: runner.run_arm(arm, ITEMS, retriever, tmp_path, adaptive=arm == "adaptive",
                                answer_fn=answer_fn, log=lambda _: None)
            for arm in runner.ARMS}
    summary = runner.summarise(arms, ITEMS)
    assert set(summary["metrics"]) == {"static", "adaptive"}
    assert summary["paired_recall_gain"]["n"] == 1
    assert summary["metrics"]["static"]["recall_after_retries"] == 0.0
    assert summary["metrics"]["adaptive"]["recall_after_retries"] == 1.0

    runner.write_outputs(tmp_path, summary, {"note": "x"})
    assert json.loads((tmp_path / "metrics.json").read_text())["metrics"]["static"]["questions"] == 2
    assert (tmp_path / "metrics.md").read_text().startswith("| metric | static | adaptive |")
    assert json.loads((tmp_path / "run_manifest.json").read_text()) == {"note": "x"}


def test_single_arm_summary_has_no_paired_gain():
    records = [{"question_id": "q1", "retrieval_round": 1, "critic_log": [], "sufficient": False,
                "retrieved_passages": [], "gap_label": "NONE", "retrieval_log": []}]
    assert "paired_recall_gain" not in runner.summarise({"static": records}, ITEMS[:1])


def test_environment_records_versions_and_commit():
    env = runner.environment()
    assert env["python"] and "pydantic" in env["packages"] and "git_commit" in env


# --- generation wiring ----------------------------------------------------

def args(**overrides):
    base = runner.parse_args(["--passages", "p", "--dense-index-dir", "d", "--items", "i",
                              "--out-dir", "o"])
    for key, value in overrides.items():
        setattr(base, key, value)
    return base


def test_no_generation_stack_needed_for_the_rule_based_run():
    assert runner.build_generation(args()) == (None, None, None)


def test_missing_p5_package_gives_a_clear_error(monkeypatch):
    monkeypatch.setitem(sys.modules, "src.generation", None)  # import raises ImportError
    with pytest.raises(SystemExit, match="PR #15"):
        runner.build_generation(args(critic="generator"))


def test_parse_args_defaults_and_choices():
    parsed = args()
    assert (parsed.arms, parsed.critic, parsed.answers, parsed.max_retries) == (
        ["static", "adaptive"], "rules", "none", 2)
    with pytest.raises(SystemExit):
        runner.parse_args(["--passages", "p", "--dense-index-dir", "d", "--out-dir", "o"])  # no items
