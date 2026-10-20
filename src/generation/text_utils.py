"""Text helpers shared by the prompt template, the mock generator and the validator.

Two facts about this module matter for how much you should trust the citation
validator:

1. **Number extraction is symmetric.** The same regex and the same canonicaliser
   run over the answer *and* over the retrieved passages. If the canonicaliser
   refuses to treat something as a number on one side (``T5``, ``v1.2``, a
   ``paper123_results_04`` identifier) it refuses on the other side too, so the
   check never becomes accidentally permissive for a whole class of tokens.
2. **The heuristics here are conservative, not clever.** Sentence splitting is
   regex-based and the claim-coverage check is a content-token recall. They exist
   to catch *unsupported* claims, so a false positive costs a warning line and a
   false negative costs nothing. No downstream decision may treat a
   ``WARNING``-level finding as proof that the answer is wrong.
"""

from __future__ import annotations

import re
import unicodedata
from decimal import Decimal, InvalidOperation

# --------------------------------------------------------------------------- #
# Numbers
# --------------------------------------------------------------------------- #

#: Matches a number that is *not* glued to an identifier.
#:
#: The lookbehind rejects ``T5``, ``paper123`` and the inner digits of ``v1.2``;
#: the lookahead only rejects a following digit so that unit suffixes still
#: count (``3.5x``, ``5G``, ``12%``). Both sides of every comparison go through
#: this pattern, so identifier-like tokens are excluded consistently.
NUMBER_RE = re.compile(r"(?<![A-Za-z0-9_.])(\d+(?:,\d{3})*(?:\.\d+)?)(?![0-9])")


def canonical_number(raw: str) -> str:
    """Reduce a numeric literal to a comparable form.

    ``"1,234.50"`` -> ``"1234.5"``; ``"2.0"`` -> ``"2"``. Integral values lose
    their decimal part, so ``2.0`` and ``2`` compare equal - they are the same
    quantity, and distinguishing them would only create false positives. Falls
    back to the comma-stripped literal if the value cannot be parsed.
    """
    cleaned = raw.replace(",", "").strip()
    try:
        value = Decimal(cleaned)
    except InvalidOperation:
        return cleaned
    if value == value.to_integral_value():
        return str(int(value))
    # `normalize()` would produce exponent notation for round numbers, so format
    # back to plain decimal notation explicitly.
    return format(value.normalize(), "f")


def extract_numbers(text: str) -> list[str]:
    """Canonical numbers in order of first appearance, de-duplicated."""
    seen: set[str] = set()
    out: list[str] = []
    for match in NUMBER_RE.finditer(text):
        value = canonical_number(match.group(1))
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def number_index(text: str) -> set[str]:
    """The set of canonical numbers occurring in ``text``."""
    return {canonical_number(m.group(1)) for m in NUMBER_RE.finditer(text)}


# --------------------------------------------------------------------------- #
# Normalisation
# --------------------------------------------------------------------------- #

_QUOTE_MAP = {
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
    "«": '"',
    "»": '"',
    "′": "'",
    "″": '"',
}
_DASH_RE = re.compile("[‐-―−]")


def normalize_for_match(text: str) -> str:
    """Aggressively flatten text so substring/overlap comparisons behave.

    NFKC folds full-width forms, smart quotes and dashes are mapped to ASCII,
    and whitespace is collapsed. Used for claim-coverage and number-context
    checks, never for anything user-visible.
    """
    folded = unicodedata.normalize("NFKC", text)
    folded = folded.translate(str.maketrans(_QUOTE_MAP))
    folded = _DASH_RE.sub("-", folded)
    return re.sub(r"\s+", " ", folded).strip().lower()


# --------------------------------------------------------------------------- #
# Sentences and tokens
# --------------------------------------------------------------------------- #

#: Abbreviations protected from the sentence splitter. ``et al.`` style endings
#: are extremely common in the paper text this project retrieves, so splitting
#: them produces junk "sentences" that then trip the coverage check.
_ABBREVIATIONS = (
    "e.g.", "i.e.", "cf.", "et al.", "etc.", "vs.", "fig.", "figs.",
    "eq.", "eqs.", "sec.", "secs.", "tab.", "tabs.", "ref.", "refs.",
    "no.", "nos.", "approx.", "ca.", "al.", "resp.", "w.r.t.",
)

#: Stands in for the dot of a protected abbreviation while splitting. A NUL byte
#: cannot occur in normalised text, so unlike a space it can never be confused
#: with real content and can be restored losslessly.
_ABBREV_SENTINEL = "\x00"

_ABBREV_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(a) for a in _ABBREVIATIONS) + r")",
    re.IGNORECASE,
)

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
_LIST_MARKER_RE = re.compile("^\\s*(?:[-*•–—]|\\d{1,2}[.)])\\s+")


def split_sentences(text: str) -> list[str]:
    """Split into sentences, treating each line of a list as its own sentence.

    Abbreviated dots are masked before splitting and restored afterwards, so
    ``"Zhang et al. report 91.2 F1."`` stays one sentence instead of becoming
    two fragments.

    Known limitation: no dependency parse, so a sentence containing an
    unlisted abbreviation may be over-split. Every consumer of this function
    treats over-splitting as extra scrutiny, not as evidence of error.
    """

    def _mask(match: re.Match[str]) -> str:
        return match.group(0)[:-1] + _ABBREV_SENTINEL

    protected = _ABBREV_RE.sub(_mask, text)

    out: list[str] = []
    for raw_line in protected.splitlines():
        # Strip the list marker *before* splitting on sentence enders. Otherwise
        # "1. Third point" splits into "1." and "Third point", leaving a junk
        # "1." fragment that the coverage check would then try to verify.
        line = _LIST_MARKER_RE.sub("", raw_line).strip()
        if not line:
            continue
        for chunk in _SENTENCE_SPLIT_RE.split(line):
            chunk = chunk.replace(_ABBREV_SENTINEL, ".").strip()
            if chunk:
                out.append(chunk)
    return out


#: Deliberately small: this is a coverage heuristic, not an IR pipeline. A larger
#: list would mostly change the denominator, not the verdict.
STOPWORDS = frozenset(
    """
    a an the and or but if then than that this these those of in on at to for from by
    with without into over under about as is are was were be been being am do does did
    doing have has had having it its it's their there here we our you your they them
    he she his her i me my mine not no nor so such only own same too very can could
    will would shall should may might must also more most much many few some any all
    both each other others another between during before after above below up down out
    off again further once because while where when why how what which who whom whose
    however therefore thus hence moreover furthermore additionally specifically
    """.split()
)

_WORD_RE = re.compile(r"[a-z][a-z0-9'-]*")

#: Sibilant plurals take ``-es``: ``reaches`` -> ``reach``, not ``reache``. Getting
#: this wrong is not cosmetic - it would make "reaches" and "reach" look like
#: different words, and the coverage check compares near-paraphrases of the same
#: claim.
_PLURAL_ES_RE = re.compile(r"(?:ch|sh|ss|x|z)es$")


def _singularize(word: str) -> str:
    """Fold the common English plurals. Deliberately shallow, and applied
    identically to both sides of every comparison, so an irregular form degrades
    to a consistent non-word rather than to a spurious mismatch."""
    if len(word) <= 4:
        return word
    if _PLURAL_ES_RE.search(word):
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def content_tokens(text: str) -> set[str]:
    """Lowercase content words for overlap scoring.

    Numbers and stopwords are dropped and plurals are folded. This is
    intentionally shallow - the check it feeds compares *claim* text against
    *answer* text, which are near-paraphrases of each other, so heavy
    normalisation would hurt more than help.
    """
    tokens: set[str] = set()
    for raw in _WORD_RE.findall(normalize_for_match(text)):
        if raw in STOPWORDS or len(raw) < 3:
            continue
        tokens.add(_singularize(raw))
    return tokens


def token_overlap_recall(needle: str, haystack: str) -> float:
    """Fraction of ``needle``'s content tokens present in ``haystack``.

    Returns ``1.0`` when ``needle`` has no content tokens at all, so that short
    connective sentences ("In summary.") never register as unsupported claims.
    """
    needle_tokens = content_tokens(needle)
    if not needle_tokens:
        return 1.0
    return len(needle_tokens & content_tokens(haystack)) / len(needle_tokens)


# --------------------------------------------------------------------------- #
# Question clauses
# --------------------------------------------------------------------------- #

#: Coordinators that join two separately-answerable requests. Only these split a
#: question: "in order to" joins one request, "and" between two nouns does not.
_CLAUSE_SPLIT_RE = re.compile(
    r"\s*(?:;|,\s*and\s+|\s+and\s+|\s+or\s+)\s*", re.IGNORECASE
)

#: Minimum content tokens a fragment must carry to count as its own clause.
#:
#: Two, not three, and the difference is measured rather than guessed. At three,
#: ``b07``'s second request - ``"what is its inference latency"`` - reduces to
#: ``{inference, latency}`` and is discarded as a modifier, which is precisely
#: the case the clause check exists to catch. At two it survives, while a true
#: modifier like ``"and by how much"`` reduces to no content tokens at all and
#: is still correctly absorbed into the clause it follows.
MIN_CLAUSE_TOKENS = 2

#: A fragment that opens with an interrogative is a request in its own right
#: however few content words it carries.
#:
#: Content-token count alone is the wrong test for a short question: ``"and how
#: many parameters does it have"`` reduces to the single token ``{parameter}``
#: because ``how``, ``many`` and ``have`` are all stopwords, so a genuine second
#: request would be swallowed and the check would silently do nothing. Modifiers
#: survive this test because they are prepositional - ``"by how much"``,
#: ``"to what extent"``, ``"for which model"`` - and none of them *starts* with
#: the interrogative.
_INTERROGATIVE_START_RE = re.compile(
    r"^(?:how|what|which|who|whom|whose|where|when|why"
    r"|does|do|did|is|are|was|were|can|could|should|would|will)\b",
    re.IGNORECASE,
)


def question_clauses(question: str) -> list[str]:
    """Split a question into the separate things it asks for.

    Conservative by construction. This feeds a check that reports a *missing*
    answer, so a spurious clause costs a false warning on a good answer - the
    expensive direction. A fragment is only promoted to its own clause when it
    either carries at least :data:`MIN_CLAUSE_TOKENS` content tokens or opens
    with an interrogative. That keeps ``"..., and by how much?"`` attached to the
    clause it belongs to while still separating ``"...have, and on how many ...
    trained?"``.

    Returns ``[question]`` unchanged when the question asks one thing, and the
    caller can treat a single-element result as "not a multi-part question".
    """
    stripped = question.strip().rstrip("?.").strip()
    if not stripped:
        return []

    parts = [part.strip() for part in _CLAUSE_SPLIT_RE.split(stripped)]
    clauses = [
        part
        for part in parts
        if len(content_tokens(part)) >= MIN_CLAUSE_TOKENS
        or _INTERROGATIVE_START_RE.match(part)
    ]
    return clauses or [stripped]


def truncate(text: str, max_chars: int | None, marker: str = " [...]") -> str:
    """Character-budget truncation with an explicit, greppable marker.

    The marker is deliberately visible: if a numeric claim is missing from the
    evidence only because the passage was truncated, P6 should be able to spot
    it in the transcript rather than conclude the model hallucinated.
    """
    if max_chars is None or max_chars <= 0 or len(text) <= max_chars:
        return text
    keep = max(0, max_chars - len(marker))
    return text[:keep].rstrip() + marker
