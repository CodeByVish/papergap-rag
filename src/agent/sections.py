"""Per-paper section selection for scoped retries (P4).

Section names in QASPER are free text ("Experiments ::: Results", "Baseline
Model"), so a fixed label -> section mapping such as MISSING_RESULT -> "Results"
fails for most papers (an exact "Results" section exists in only ~20% of the
development corpus). `make_section_selector` instead matches each paper's own
section names against the planner's hints for the diagnosed gap.

Rules, for the retrieval round that follows a critic verdict:
- no gap, or a gap with no section hints (terminology, weak evidence,
  insufficient information): search the whole paper;
- otherwise pick one section of this paper whose lowercase name contains a hint,
  preferring earlier hints, then document order;
- never repeat a section already searched this run, so each retry widens coverage.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from src.agent.nodes import SectionSelector
from src.agent.planner import GAP_SECTION_HINTS
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.schemas import Passage


def choose_section(
    sections: Sequence[str], hints: list[str], used: set[str]
) -> str | None:
    """Best unused section of `sections` (document order) for `hints`."""
    best: tuple[int, int] | None = None
    chosen: str | None = None
    for position, name in enumerate(sections):
        if name in used:
            continue
        lowered = name.lower()
        hint_ranks = [rank for rank, hint in enumerate(hints) if hint in lowered]
        if not hint_ranks:
            continue
        key = (min(hint_ranks), position)
        if best is None or key < best:
            best, chosen = key, name
    return chosen


def make_section_selector(passages: Iterable[Passage]) -> SectionSelector:
    """Build a `section_selector` for `build_agent_graph` from the corpus passages."""
    by_paper: dict[str, dict[str, None]] = {}
    for passage in passages:
        by_paper.setdefault(passage.paper_id, {})[passage.section] = None

    def selector(state: AgentState) -> str | None:
        if state.gap_label is GapLabel.NONE:
            return None
        hints = GAP_SECTION_HINTS.get(state.gap_label)
        if not hints:
            return None
        used = {
            entry["section"] for entry in state.retrieval_log if entry.get("section")
        }
        return choose_section(list(by_paper.get(state.paper_id, {})), hints, used)

    return selector
