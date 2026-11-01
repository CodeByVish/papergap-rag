"""Tests for the rule-based question planner and requirement-driven evidence mapper."""

import pytest

from src.agent.nodes import gap_classifier, map_evidence, plan_question
from src.agent.planner import build_plan, classify_question, key_terms
from src.agent.schemas import AgentState, GapLabel, QuestionType
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore

# Manually written examples: (question, expected type).
EXAMPLES = [
    ("What accuracy did the model achieve on the test set?", QuestionType.RESULT),
    ("What F1 score does the proposed system obtain?", QuestionType.RESULT),
    ("How well does it perform on low-resource languages?", QuestionType.RESULT),
    ("How accurate is their predictive model?", QuestionType.RESULT),
    ("How did they induce the CFG?", QuestionType.METHOD),
    ("What architecture is used for the encoder?", QuestionType.METHOD),
    ("Does the approach use pretrained embeddings?", QuestionType.METHOD),
    ("How does the system compare to the BiLSTM baseline?", QuestionType.COMPARISON),
    ("Does it outperform previous state-of-the-art models?", QuestionType.COMPARISON),
    ("What are the limitations of this work?", QuestionType.LIMITATION),
    ("In which cases does the parser fail?", QuestionType.LIMITATION),
    ("Which languages are covered?", QuestionType.FACTUAL),
    ("What model was used by the top team?", QuestionType.FACTUAL),
    ("How big is the dataset for this challenge?", QuestionType.FACTUAL),
    ("Who annotated the corpus?", QuestionType.FACTUAL),
]


@pytest.mark.parametrize(("question", "expected"), EXAMPLES)
def test_classify_question(question, expected):
    assert classify_question(question) is expected


def test_cues_match_whole_words_only():
    # "vs" must not fire inside "canvas"; "fail" not inside "failsafe".
    assert classify_question("Which canvas size is used?") is QuestionType.FACTUAL
    assert classify_question("Is there a failsafe mode?") is QuestionType.FACTUAL


def test_comparison_needs_result_and_comparison_evidence():
    plan = build_plan("How does the system compare to the baseline?")
    assert [r.name for r in plan.requirements] == ["result", "comparison"]


def test_baseline_only_question_needs_no_result():
    plan = build_plan("What was the baseline?")
    assert plan.question_type is QuestionType.COMPARISON
    assert [r.name for r in plan.requirements] == ["comparison"]


def test_explicit_comparison_with_baseline_still_needs_result():
    plan = build_plan("How does it compare to the baseline?")
    assert [r.name for r in plan.requirements] == ["result", "comparison"]


def test_setup_question_adds_experiment_context():
    plan = build_plan("What accuracy is reached on which dataset?")
    assert [r.name for r in plan.requirements] == ["result", "experiment_context"]
    assert plan.requirements[1].gap_if_missing is GapLabel.MISSING_EXPERIMENT_CONTEXT


def test_factual_requirement_uses_question_key_terms():
    plan = build_plan("Which languages are covered by the study?")
    (requirement,) = plan.requirements
    assert requirement.name == "direct_answer"
    # Stems, matched as word prefixes, so "language" and "covers" also count.
    assert requirement.keywords == ["languag", "cover", "study"]
    assert requirement.gap_if_missing is GapLabel.TERMINOLOGY_MISMATCH


def test_planner_never_predicts_unanswerable():
    assert all(
        build_plan(question).question_type is not QuestionType.UNANSWERABLE
        for question, _ in EXAMPLES
    )


def test_every_requirement_maps_to_an_actionable_gap_label():
    for question, _ in EXAMPLES:
        for requirement in build_plan(question).requirements:
            assert requirement.gap_if_missing is not GapLabel.NONE


def test_stemmed_factual_keywords_match_inflected_text():
    hits = [_hit("a", "Intro", "The corpus covers three languages and one dialect.")]
    state = _planned_state("Which languages are covered by the study?", hits)
    # "languag" and "cover" both appear as prefixes; "study" does not.
    assert map_evidence(state)["evidence_map"] == {"direct_answer": ["a"]}


def test_key_terms_drop_stopwords_and_duplicates():
    assert key_terms("What is the size of the dataset and the dataset split?") == [
        "size", "dataset", "split",
    ]


@pytest.mark.parametrize("question", ["", "   "])
def test_empty_question_rejected(question):
    with pytest.raises(ValueError):
        build_plan(question)


def test_plan_question_node_fills_state_fields():
    state = AgentState(question="What accuracy did the model achieve?", paper_id="p")
    update = plan_question(state)
    assert update["question_type"] is QuestionType.RESULT
    assert update["required_components"] == ["result"]
    assert [r.name for r in update["evidence_requirements"]] == ["result"]


def _hit(passage_id: str, section: str, text: str) -> RetrievedPassage:
    return RetrievedPassage(
        passage=Passage(
            passage_id=passage_id,
            paper_id="p",
            title="t",
            section=section,
            chunk_number=0,
            text=text,
        ),
        rank=1,
        source_scores={"bm25": SourceScore(rank=1, score=1.0)},
        rrf_score=0.1,
    )


def _planned_state(question: str, hits: list[RetrievedPassage]) -> AgentState:
    state = AgentState(question=question, paper_id="p", retrieved_passages=hits)
    return state.model_copy(update=plan_question(state))


def test_mapper_accepts_matching_section_name():
    hits = [_hit("a", "Results", "Numbers are in the table.")]
    state = _planned_state("What accuracy was achieved?", hits)
    assert map_evidence(state)["evidence_map"] == {"result": ["a"]}


def test_mapper_accepts_text_with_enough_distinct_keywords():
    hits = [_hit("a", "Experiments", "The model achieves 91% accuracy and 88 F1.")]
    state = _planned_state("What accuracy was achieved?", hits)
    assert map_evidence(state)["evidence_map"] == {"result": ["a"]}


def test_mapper_rejects_single_incidental_keyword():
    hits = [_hit("a", "Setup", "We report token F1 on the held-out set.")]
    state = _planned_state("What accuracy was achieved?", hits)
    assert map_evidence(state)["evidence_map"] == {"result": []}


def test_mapper_keeps_requirements_separate():
    hits = [_hit("a", "Results", "Accuracy is 82 and F1 is 80.")]
    state = _planned_state("How does the system compare to the baseline?", hits)
    evidence = map_evidence(state)["evidence_map"]
    assert evidence["result"] == ["a"]
    assert evidence["comparison"] == []


def test_gap_classifier_uses_first_unmet_requirement():
    hits = [_hit("a", "Results", "Accuracy is 82 and F1 is 80.")]
    state = _planned_state("How does the system compare to the baseline?", hits)
    state = state.model_copy(update=map_evidence(state))
    assert gap_classifier(state) == {"gap_label": GapLabel.MISSING_COMPARISON}


def test_gap_classifier_defaults_to_weak_evidence_when_nothing_unmet():
    state = _planned_state("What accuracy was achieved?", [_hit("a", "Results", "x")])
    state = state.model_copy(update=map_evidence(state))
    assert gap_classifier(state) == {"gap_label": GapLabel.WEAK_EVIDENCE}
