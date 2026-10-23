"""Rule-based question planner (P4, Week 2).

`build_plan(question)` classifies a question into a `QuestionType` and returns
the structured evidence requirements an answer needs. It is deterministic and
needs no model, so it can run in tests and as the fallback if an LLM planner is
added later behind the same function signature.

The question text alone cannot show that a question is unanswerable, so the
planner never returns `QuestionType.UNANSWERABLE`; the critic reports that case
through `GapLabel.INSUFFICIENT_INFORMATION` once retrieval is exhausted.
"""

from __future__ import annotations

import re

from pydantic import BaseModel, Field

from src.agent.schemas import EvidenceRequirement, GapLabel, QuestionType


class Plan(BaseModel):
    question_type: QuestionType
    requirements: list[EvidenceRequirement] = Field(min_length=1)


# Checked in order; the first match wins. Comparison and limitation cues are the
# most specific, result cues come before method because "what accuracy did the
# model achieve" mentions "model" but asks for a number.
_TYPE_CUES: list[tuple[QuestionType, tuple[str, ...]]] = [
    (
        QuestionType.COMPARISON,
        (
            "compare", "compared", "comparison", "versus", "vs", "outperform",
            "outperforms", "better than", "worse than", "baseline", "baselines",
            "differ from", "difference between", "improve over",
            "improvement over", "state-of-the-art", "state of the art",
        ),
    ),
    (
        QuestionType.LIMITATION,
        (
            "limitation", "limitations", "drawback", "weakness", "shortcoming",
            "downside", "fail", "fails", "future work",
        ),
    ),
    (
        QuestionType.RESULT,
        (
            "accuracy", "f1", "f-score", "bleu", "rouge", "perplexity", "auc",
            "precision", "recall", "score", "performance", "result", "results",
            "how well", "how much", "achieve", "achieved", "metric",
        ),
    ),
    (
        QuestionType.METHOD,
        (
            "method", "approach", "architecture", "technique", "algorithm",
            "propose", "proposed", "trained", "implement", "implemented",
            "how do", "how does", "how did", "how is", "how are", "how was",
            "how were",
        ),
    ),
]

# Comparison questions that only name the baseline or prior systems ("What was the
# baseline?") need a description of it, not a measured result.
_DESCRIPTIVE_COMPARISON_CUES = (
    "baseline", "baselines", "state-of-the-art", "state of the art",
)

# Extra requirement added to any question that asks about the experimental setup.
_SETUP_CUES = (
    "dataset", "datasets", "corpus", "hyperparameter", "hyperparameters",
    "setup", "setting", "settings", "learning rate", "batch size", "split",
    "annotator", "annotators", "evaluate on", "evaluated on", "trained on",
)

_STOPWORDS = frozenset({
    "a", "an", "the", "of", "in", "on", "for", "to", "is", "are", "was", "were",
    "be", "been", "do", "does", "did", "what", "which", "who", "whom", "whose",
    "when", "where", "why", "how", "that", "this", "these", "those", "it", "its",
    "they", "their", "them", "with", "by", "as", "at", "from", "and", "or", "not",
    "can", "could", "would", "should", "will", "have", "has", "had", "than",
    "there", "paper", "authors", "author", "used", "use", "using",
    "also", "such", "only", "other", "some", "any", "each", "many", "much", "few",
    "more", "most", "very", "both", "over", "into", "then", "about", "between",
    "during", "after", "before", "under", "again", "further", "here", "while",
    "through", "above", "below", "just", "now", "same", "own", "too", "but", "all",
    "one", "two", "may", "might", "must", "shall", "being", "else",
    "however", "thus", "therefore", "since", "because", "although", "whether",
    "show", "shown", "shows", "given", "based", "make", "made", "like", "well",
    "first", "second", "new", "different", "several", "various", "often",
    "relate", "related", "within", "without", "across", "around", "per",
})

_METHOD = EvidenceRequirement(
    name="method",
    description="Passage describing the proposed method, model or procedure.",
    section_hints=["method", "approach", "model", "architecture", "system"],
    keywords=[
        "we propose", "we present", "we introduce", "we develop", "we use",
        "we apply", "we employ", "we adopt", "we train", "we build",
        "our model", "our approach", "our method", "our system", "architecture",
        "algorithm", "based on", "consists of", "pipeline", "encoder",
        "classifier", "network",
    ],
    min_keyword_matches=2,
    gap_if_missing=GapLabel.MISSING_METHOD,
)
_EXPERIMENT_CONTEXT = EvidenceRequirement(
    name="experiment_context",
    description="Passage describing the dataset, setup or training configuration.",
    section_hints=[
        "setup", "setting", "dataset", "data", "corpus", "implementation",
        "training", "experiment", "evaluation",
    ],
    keywords=[
        "dataset", "corpus", "hyperparameter", "learning rate", "batch size",
        "split", "setup", "implementation details", "annotated", "collected",
        "training set", "test set", "we use", "we used", "trained on",
        "pre-trained", "fine-tun",
    ],
    min_keyword_matches=2,
    gap_if_missing=GapLabel.MISSING_EXPERIMENT_CONTEXT,
)
_RESULT = EvidenceRequirement(
    name="result",
    description="Passage reporting a measured result or metric value.",
    section_hints=["result", "evaluation", "findings", "experiment", "performance"],
    keywords=[
        "accuracy", "f1", "f-score", "f-measure", "bleu", "rouge", "perplexity",
        "precision", "recall", "score", "achieve", "obtain", "outperform",
        "improve", "performance", "%", "points",
    ],
    min_keyword_matches=2,
    gap_if_missing=GapLabel.MISSING_RESULT,
)
_COMPARISON = EvidenceRequirement(
    name="comparison",
    description="Passage comparing the system with baselines or prior work.",
    section_hints=["comparison", "baseline", "related work", "compared"],
    keywords=[
        "baseline", "compare", "comparison", "outperform", "versus",
        "state-of-the-art", "state of the art", "improve", "better than",
        "previous work", "prior work", "existing",
    ],
    min_keyword_matches=2,
    gap_if_missing=GapLabel.MISSING_COMPARISON,
)
_LIMITATION = EvidenceRequirement(
    name="limitation",
    description="Passage stating a limitation, failure case or future work.",
    section_hints=["limitation", "discussion", "conclusion", "error analysis", "future"],
    keywords=[
        "limitation", "fail", "failure", "drawback", "weakness", "future work",
        "however", "unable", "cannot",
    ],
    min_keyword_matches=2,
    gap_if_missing=GapLabel.WEAK_EVIDENCE,
)

_REQUIREMENTS_BY_TYPE: dict[QuestionType, list[EvidenceRequirement]] = {
    QuestionType.METHOD: [_METHOD],
    QuestionType.RESULT: [_RESULT],
    QuestionType.COMPARISON: [_RESULT, _COMPARISON],
    QuestionType.LIMITATION: [_LIMITATION],
}


def _contains_cue(text: str, cues: tuple[str, ...]) -> bool:
    return any(re.search(rf"(?<!\w){re.escape(cue)}(?!\w)", text) for cue in cues)


def _only_descriptive_cues(question: str) -> bool:
    """True when a comparison question has only baseline/state-of-the-art cues."""
    text = question.lower()
    comparison_cues = dict(_TYPE_CUES)[QuestionType.COMPARISON]
    matched = [cue for cue in comparison_cues if _contains_cue(text, (cue,))]
    return all(cue in _DESCRIPTIVE_COMPARISON_CUES for cue in matched)


def classify_question(question: str) -> QuestionType:
    """Return the first question type whose cue words appear in `question`."""
    text = question.lower()
    for question_type, cues in _TYPE_CUES:
        if _contains_cue(text, cues):
            return question_type
    return QuestionType.FACTUAL


def key_terms(question: str) -> list[str]:
    """Content words of the question, in order and without duplicates."""
    terms: list[str] = []
    for word in re.findall(r"[a-z0-9][a-z0-9\-]*", question.lower()):
        if len(word) >= 3 and word not in _STOPWORDS and word not in terms:
            terms.append(word)
    return terms


def _stem(word: str) -> str:
    """Crude suffix stripping so "datasets" matches "dataset" under prefix match."""
    for suffix in ("ing", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def _direct_answer_requirement(question: str) -> EvidenceRequirement:
    stems = list(dict.fromkeys(_stem(term) for term in key_terms(question)))
    return EvidenceRequirement(
        name="direct_answer",
        description="Passage that mentions the key terms of the question.",
        keywords=stems,
        min_keyword_matches=min(2, max(len(stems), 1)),
        gap_if_missing=GapLabel.TERMINOLOGY_MISMATCH,
    )


def build_plan(question: str) -> Plan:
    """Classify `question` and list the evidence an answer must be built on."""
    if not question.strip():
        raise ValueError("question must be a nonempty string")
    question_type = classify_question(question)
    if question_type is QuestionType.FACTUAL:
        requirements = [_direct_answer_requirement(question)]
    elif question_type is QuestionType.COMPARISON and _only_descriptive_cues(question):
        requirements = [_COMPARISON]
    else:
        requirements = list(_REQUIREMENTS_BY_TYPE[question_type])
    if _contains_cue(question.lower(), _SETUP_CUES) and all(
        r.name != _EXPERIMENT_CONTEXT.name for r in requirements
    ):
        requirements.append(_EXPERIMENT_CONTEXT)
    return Plan(question_type=question_type, requirements=requirements)
