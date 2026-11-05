"""Deterministic claim -> passage provenance mapping.

The frozen P6 contract carries a ``provenance`` list: one entry per factual
claim, naming the passages that support it. Until Week 3 that list was whatever
the model chose to emit, which made it a *self-report* - usable as a hint, and
useless as evidence, because an 8B model that invents a claim will just as
happily declare it supported.

This module makes the mapping reproducible. It splits the answer into sentences,
scores each one against the candidate passages with the same content-token
recall the validator uses, and derives a :class:`~src.generation.schema.Support` label
from the score. Two consequences matter:

* **A grounded answer comes back with a provenance map** whenever it contains at
  least one checkable sentence (three or more content tokens). If the model
  omitted it, :class:`~src.generation.pipeline.GroundedQAPipeline` fills it in from here
  and records ``PROVENANCE_DERIVED``. P6 gets a map either way.
* **A model's overstatement becomes visible.** :func:`overstated_claims` reports
  entries whose asserted ``support`` the overlap does not bear out, which is
  exactly the case a self-reported field cannot catch on its own.

Two deliberate limits, both inherited from :mod:`src.generation.text_utils`:

* The score is content-token recall, not entailment. It catches a claim with no
  textual foothold in its passage; it cannot catch a claim that reuses the
  passage's words to say something the passage does not. That is the optional
  NLI experiment in the brief, not this module.
* The mapping is *not* a validator and never downgrades anything. It runs after
  every rule check, on results that already passed, and only enriches them.
"""

from __future__ import annotations

from typing import Sequence

from pydantic import BaseModel, ConfigDict

from src.generation.schema import ProvenanceEntry, RetrievedPassage, Support
from src.generation.text_utils import content_tokens, split_sentences, token_overlap_recall


class ProvenanceConfig(BaseModel):
    """Thresholds for turning an overlap score into a support label.

    The bands are deliberately coarse. Two cut points on a recall score cannot
    distinguish "direct" from "partial" the way a reader would, so the labels are
    treated downstream as a rough ordering, never as a verified fact.
    """

    model_config = ConfigDict(extra="forbid")

    #: Recall at or above this is reported as ``direct``.
    direct_threshold: float = 0.60
    #: Recall at or above this (but below ``direct_threshold``) is ``partial``.
    #: Matches ``ValidationConfig.claim_coverage_threshold``'s default so a claim
    #: the coverage check accepts is not simultaneously called unsupported here.
    partial_threshold: float = 0.35
    #: Sentences with fewer content tokens than this carry no checkable claim and
    #: are skipped, as in the R2 coverage check.
    min_claim_tokens: int = 3
    #: Cap on passages named per claim. A sentence matching six passages equally
    #: is usually a generic opening, and naming all six buries the signal.
    max_passages_per_claim: int = 2


def score_claim(claim: str, passages: Sequence[RetrievedPassage]) -> list[tuple[str, float]]:
    """``[(passage_id, recall)]`` for one claim, best first.

    Ties break on the passage's position in ``passages``, so the output depends
    only on the inputs and not on dict ordering - a provenance map that shuffles
    between runs would be untestable.
    """
    scored = [
        (index, passage.passage_id, token_overlap_recall(claim, passage.text))
        for index, passage in enumerate(passages)
    ]
    scored.sort(key=lambda item: (-item[2], item[0]))
    return [(passage_id, score) for _, passage_id, score in scored]


def map_claims_to_passages(
    answer: str,
    passages: Sequence[RetrievedPassage],
    config: ProvenanceConfig | None = None,
) -> list[ProvenanceEntry]:
    """Map each factual sentence of ``answer`` to the passages that support it.

    ``passages`` should be the *cited* passages, not every retrieved one: the
    provenance map exists to explain the citations, and restricting it there
    guarantees the result satisfies ``provenance ⊆ citations``, so a derived map
    can never introduce the mismatch the validator warns about.

    Returns one entry per checkable sentence, in answer order. A sentence with
    no passage above ``partial_threshold`` is kept with ``support=unsupported``
    and no passage ids - dropping it would silently understate how much of the
    answer is ungrounded.
    """
    config = config or ProvenanceConfig()
    if not answer.strip() or not passages:
        return []

    entries: list[ProvenanceEntry] = []
    for sentence in split_sentences(answer):
        if len(content_tokens(sentence)) < config.min_claim_tokens:
            continue

        ranked = score_claim(sentence, passages)
        if not ranked:
            continue
        best = ranked[0][1]

        if best >= config.direct_threshold:
            support = Support.DIRECT
            ids = [
                passage_id
                for passage_id, score in ranked
                if score >= config.direct_threshold
            ][: config.max_passages_per_claim]
        elif best >= config.partial_threshold:
            support = Support.PARTIAL
            ids = [ranked[0][0]]
        else:
            support = Support.UNSUPPORTED
            ids = []

        entries.append(
            ProvenanceEntry(claim=sentence, passage_ids=ids, support=support)
        )

    return entries


def overstated_claims(
    entries: Sequence[ProvenanceEntry],
    passages: Sequence[RetrievedPassage],
    config: ProvenanceConfig | None = None,
) -> list[tuple[ProvenanceEntry, Support]]:
    """Model-asserted entries whose claimed support the text does not bear out.

    Returns ``(entry, derived_support)`` for every entry that claims a stronger
    label than the overlap supports. The reverse direction is not reported: a
    model that under-claims is being cautious, which is not a defect.

    This is the check a self-reported field cannot perform on itself, and the
    reason ``provenance[].support`` is still documented to P6 as a hint rather
    than a verified fact - what changed in Week 3 is that the *disagreement* is
    now visible in the audit trail.
    """
    config = config or ProvenanceConfig()
    if not passages:
        return []

    order = {Support.UNSUPPORTED: 0, Support.PARTIAL: 1, Support.DIRECT: 2}
    out: list[tuple[ProvenanceEntry, Support]] = []

    for entry in entries:
        ranked = score_claim(entry.claim, passages)
        best = ranked[0][1] if ranked else 0.0
        if best >= config.direct_threshold:
            derived = Support.DIRECT
        elif best >= config.partial_threshold:
            derived = Support.PARTIAL
        else:
            derived = Support.UNSUPPORTED

        if order[entry.support] > order[derived]:
            out.append((entry, derived))

    return out
