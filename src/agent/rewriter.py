"""Gap-driven query rewriting (P4, Week 4 gap-action table).

Each gap label maps to one retrieval action from docs/EXECUTION_PLAN.md:

| Gap                        | Action                                    |
| MISSING_METHOD             | add method/approach vocabulary            |
| MISSING_EXPERIMENT_CONTEXT | add dataset, setup and metric vocabulary  |
| MISSING_RESULT             | add results/metric vocabulary             |
| MISSING_COMPARISON         | add baseline/comparison vocabulary        |
| TERMINOLOGY_MISMATCH       | add the paper's own terms                 |
| WEAK_EVIDENCE              | add the paper's own terms and detail      |
| INSUFFICIENT_INFORMATION   | no rewrite (the loop stops and refuses)   |

The rewrite only changes the query text. Section-scoped retrieval ("Prioritize
Results") needs the retriever to accept a section and is not wired in here.
"""

from __future__ import annotations

import re
from collections import Counter

from src.agent.planner import key_terms
from src.agent.schemas import AgentState, GapLabel

MAX_PAPER_TERMS = 4
MAX_MISSING_PHRASES = 2
MAX_QUERY_WORDS = 60
_MIN_TERM_LENGTH = 4

_GAP_VOCABULARY: dict[GapLabel, str] = {
    GapLabel.MISSING_METHOD: "method approach architecture we propose",
    GapLabel.MISSING_EXPERIMENT_CONTEXT: "dataset experimental setup evaluation metrics",
    GapLabel.MISSING_RESULT: "results experimental findings accuracy score",
    GapLabel.MISSING_COMPARISON: "baseline comparison state-of-the-art outperform",
    GapLabel.WEAK_EVIDENCE: "additional detail",
}
_USES_MISSING_PHRASES = frozenset(
    {
        GapLabel.MISSING_METHOD,
        GapLabel.MISSING_EXPERIMENT_CONTEXT,
        GapLabel.MISSING_RESULT,
        GapLabel.MISSING_COMPARISON,
    }
)
_USES_PAPER_TERMS = frozenset({GapLabel.TERMINOLOGY_MISMATCH, GapLabel.WEAK_EVIDENCE})


def paper_terms(state: AgentState, limit: int = MAX_PAPER_TERMS) -> list[str]:
    """Terms that recur across retrieved passages but are absent from the question.

    Counted once per passage (document frequency), ties broken by first
    appearance, so the result is deterministic. Terms in only one passage are
    skipped when several passages exist, since they are rarely the paper's
    vocabulary for the topic.
    """
    in_question = set(key_terms(state.question))
    counts: Counter[str] = Counter()
    for hit in state.retrieved_passages:
        counts.update(
            term
            for term in key_terms(hit.passage.text)
            if len(term) >= _MIN_TERM_LENGTH
            and term not in in_question
            and not re.fullmatch(r"[\d\-]+", term)
        )
    floor = 2 if len(state.retrieved_passages) > 1 else 1
    ranked = [term for term, count in counts.most_common() if count >= floor]
    return ranked[:limit]


def _model_missing_phrases(state: AgentState) -> list[str]:
    """What the LLM critic said is missing; ignored for rule-based verdicts."""
    if not state.critic_log or state.critic_log[-1].get("source") != "llm":
        return []
    return [p.strip() for p in state.missing_components if p.strip()][:MAX_MISSING_PHRASES]


def _extend(question: str, additions: list[str]) -> str:
    seen = set(question.lower().split())
    words = question.split()
    for word in " ".join(additions).split():
        if word.lower() not in seen:
            seen.add(word.lower())
            words.append(word)
    return " ".join(words[:MAX_QUERY_WORDS])


def rewrite_query(state: AgentState) -> dict:
    """Extend the question with vocabulary aimed at the diagnosed gap.

    If the result equals a query already used this run, more of the paper's own
    terms are added so a retry never repeats an earlier search verbatim.
    """
    label = state.gap_label
    if label in (GapLabel.NONE, GapLabel.INSUFFICIENT_INFORMATION):
        return {"rewritten_query": state.question}

    base: list[str] = []
    if label in _USES_MISSING_PHRASES:
        base.extend(_model_missing_phrases(state))
    base.append(_GAP_VOCABULARY.get(label, ""))

    used = {entry["query"] for entry in state.retrieval_log}
    query = state.question
    for extra in range(0, 3 * MAX_PAPER_TERMS + 1, MAX_PAPER_TERMS):
        terms = []
        if label in _USES_PAPER_TERMS or extra:
            terms = paper_terms(state, MAX_PAPER_TERMS + extra)
        query = _extend(state.question, [*base, *terms])
        if query not in used:
            break
    return {"rewritten_query": query}
