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
Results") is a separate step (src/agent/sections.py).

The added vocabulary is the critic's own terms for the missing fact when it gave
any, otherwise the gap's fixed words, never both: replaying job 50701 offline, the
critic's terms alone or the fixed words alone each fetched a gold passage in round 2
that the two combined did not, and no strategy (including re-asking the plain
question) moved recall by more than 0.05. The rewrite is not what limits recall;
see docs/P4_AGENT.md.
"""

from __future__ import annotations

import re
from collections import Counter

from src.agent.planner import key_terms
from src.agent.schemas import AgentState, GapLabel

MAX_PAPER_TERMS = 4
MAX_MISSING_TERMS = 4
MAX_QUERY_WORDS = 40
_MIN_TERM_LENGTH = 5
_TERM = re.compile(r"[a-z0-9][a-z0-9\-]*")

# Words a critic uses to talk about the retrieved text rather than about the paper. Qwen
# answers in full sentences ("... is not clearly described in the retrieved passages"),
# and none of this belongs in a search query.
_CRITIC_COMMENTARY = frozenset({
    "passage", "passages", "retrieved", "retrieval", "text", "texts", "excerpt", "excerpts",
    "clearly", "explicitly", "directly", "specifically", "described", "describe", "describes",
    "description", "mention", "mentions", "mentioned", "provide", "provides", "provided",
    "specific", "detail", "details", "detailed", "explanation", "information", "lack",
    "lacks", "lacking", "missing", "absent", "present", "include", "includes", "included",
    "context", "evidence", "answer", "question", "section", "content", "relevant",
    "insufficient", "sufficient", "enough", "unclear", "complete", "fully", "generally",
    "stating", "states", "proposed", "propose", "proposes", "discuss", "discusses",
    "discussing", "show", "shows", "showing", "shown", "paper", "authors",
})

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


def _critic_terms(phrase: str):
    """Content words of `phrase`, plus two-character metric names such as "f1"."""
    content = set(key_terms(phrase))
    for word in _TERM.findall(phrase.lower()):
        if word in content or (len(word) == 2 and any(char.isdigit() for char in word)):
            yield word


def _model_missing_terms(state: AgentState) -> list[str]:
    """Content words of what the LLM critic said is missing; ignored for rule-based verdicts.

    Only terms are kept, not the critic's sentences: the sentences are commentary on the
    retrieved passages and would pull the query toward text that talks about retrieval.
    """
    if not state.critic_log or state.critic_log[-1].get("source") != "llm":
        return []
    skip = {*key_terms(state.question), *_GAP_VOCABULARY.get(state.gap_label, "").split()}
    terms: list[str] = []
    for phrase in state.missing_components:
        for term in _critic_terms(phrase):
            if term not in skip and term not in _CRITIC_COMMENTARY and term not in terms:
                terms.append(term)
    return terms[:MAX_MISSING_TERMS]


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

    The critic's terms for the missing fact are used when it gave any, otherwise the
    gap's fixed words. If the result equals a query already used this run, more of the paper's own
    terms are added so a retry never repeats an earlier search verbatim.
    """
    label = state.gap_label
    if label in (GapLabel.NONE, GapLabel.INSUFFICIENT_INFORMATION):
        return {"rewritten_query": state.question}

    base = _model_missing_terms(state) if label in _USES_MISSING_PHRASES else []
    if not base:  # the critic gave no usable terms: fall back on the gap's fixed words
        base = [_GAP_VOCABULARY.get(label, "")]

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
