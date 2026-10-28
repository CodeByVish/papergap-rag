# P5 annotation rule — binary relevance and partial evidence

Version `p5-annotation-v1` (2026-10-28). P5 final; pending ratification by P3/P6. Extracted from P5 `docs/WEEK5_QUALITY.md` §4 so the shared repo has a citable copy; the section numbers are kept so the references inside the text resolve.

## 4. The annotation rule: binary relevance and partial evidence

**Status: P5 final, `p5-annotation-v1`, 2026-10-28. Pending ratification by P3/P6**
(`docs/EVALUATION.md` in the shared repo assigns the partial-evidence definition to P3/P5/P6).
This section replaces the earlier discussion draft with a rule that can be applied to one
`(question, passage)` pair without consulting any other passage or any other annotator.

P2 asked for this before building the 334-record batch, and it is also what P6 needs before
fixing K, the no-relevant-document rule and macro averaging. If P3 or P6 change a decision here,
change the version string and rerun any affected agreement measurement — a guideline revision
after labels exist is a new annotation round, not an edit.

### 4.1 The label

One binary label per `(question, passage)` pair:

- **1 — relevant:** the passage contains at least one piece of information that is *necessary*
  to determine the correct answer to the question.
- **0 — not relevant:** the passage could be removed without changing what the correct answer
  is, or how it is justified.

The test is **necessity**, not topicality. "Same paper", "mentions the entity", "is the kind of
section where the answer usually lives" and "contains the question's words" are all 0 unless the
passage also carries a fact the answer depends on.

Relevance is to **determining the answer**, not to agreeing with the gold answer text. Two cases
follow from that and are easy to get backwards:

- A passage that establishes a **negative** answer is 1. For *"Do they report results on English
  only?"*, a passage listing English, German and Chinese is necessary to answer "no", so it is 1.
- A passage that **contradicts** the gold answer without supplying the correct fact is 0. It is
  not evidence for the answer, even though it is on topic.

### 4.2 Partial evidence — the rule P2 asked for

A passage that supplies **one required component** of a multi-part question, but not all of them,
is **1**. The annotator sets `partial = 1` and records the component in `component`.

| question | passage contains | label | partial | component |
|---|---|---:|---:|---|
| *How many parameters does X have, and on how many pairs was it trained?* | parameter count only | 1 | 1 | `parameters` |
| same | training-pair count only | 1 | 1 | `training_pairs` |
| same | both | 1 | 0 | — |
| same | neither | 0 | 0 | — |

`partial = 1` also covers a passage that supplies a **necessary intermediate fact** without the
final answer. The Week-3 record 18 is the canonical example: the question asks the dataset size,
and the passages state 9,000 training and 11,000 validation questions. That passage is **1,
partial = 1** for relevance — a reader needs it to determine 20,000 — even though P5's validator
refuses to *state* 20,000 under R3. See §4.3; the two labels answer different questions.

**There is no 0.5 and no "maybe".** Partial is a property of a relevant passage, not a third
label. A passage that supplies no necessary component is 0 even if it is nearly relevant.

### 4.3 Relevance is not P5's `support` label

These are two different judgments and neither may be used to fill in the other:

| | annotation relevance (§4) | P5 `provenance[].support` |
|---|---|---|
| question it answers | is this passage needed to answer? | does this passage state the claim the generator made? |
| values | 0 / 1 (+ `partial`) | `direct` / `partial` / `unsupported` |
| who assigns it | annotator, blinded | generator, checked by the validator |
| record 18 | 1 (partial) — needed to derive 20,000 | `unsupported` for the claim "20,000" — not stated |

A passage can be annotation-relevant and still not license the generator to state a derived
number. Conversely, a passage can state a claim (`direct`) that is not needed for the answer
(annotation 0). The annotation file records **only** the relevance label; it is not a grounding
score and must not be reported as one.

### 4.4 Unanswerable questions

If the question cannot be answered from the paper — or from the judged pool, when the pool is the
unit — every passage is **0**, and the question row carries `answerable = 0`.

The reason is the definition, not a convention: no passage can be *necessary* to determine an
answer that does not exist. Do not import outside knowledge, and do not mark "the closest
passage" as 1 to avoid an empty row.

This has a consequence P6 must handle before runs: a question with no relevant passage has no
recall denominator. The no-relevant-document rule (exclude from macro recall, or score 0, and
report the count either way) must be fixed in advance. The annotation must not manufacture a
positive to dodge the decision.

### 4.5 Boundaries that decide close cases

| case | label | why |
|---|---:|---|
| states the answer directly | 1 | necessary by definition |
| states one of two required facts | 1 (partial) | §4.2 |
| establishes that the answer is "no" / "not reported" | 1 | negative evidence is evidence |
| defines a term the answer depends on, and the question asks for the definition | 1 | the definition is the answer |
| merely uses a term the question asks about | 0 | no information about it |
| same paper/entity, no fact bearing on the question | 0 | topical, not necessary |
| repeats the question's wording | 0 | **lexical overlap is not relevance** |
| related work, motivation, or limitations unrelated to the asked quantity | 0 | context, not evidence |
| contradicts the gold answer, supplies no correct fact | 0 | §4.1 |
| near-duplicate of another judged passage | judge independently | the file must be readable one row at a time |
| visible text is truncated and the needed fact may lie beyond the cut | 0 unless a necessary fact is already visible; note `truncated` | P5 only ever sees the stored text |
| still ambiguous after all of the above | 0, with a note | a false 1 inflates every system's recall; a false 0 is visible in adjudication |

### 4.6 What the annotator sees and records

Input is the question text plus **one** passage. Nothing else: no retrieval system, score, rank,
paper title, section, gold answer, or the other annotator's label. The row order is fixed by the
P6 manifest; do not re-sort or skip rows.

Columns: `record_id`, `question_id`, `passage_id`, `label` (0/1), `partial` (0/1), `component`
(empty unless partial), `answerable` (per question), `notes` (free text; use it for `truncated`
and for the one-line reason on a hard 0).

Agreement is measured **before adjudication**: raw agreement overall and per fixed pair, plus
Cohen's kappa per pair with its sample size. A third member who was not in the pair adjudicates
disagreements. Never revise a label to raise agreement; disagreements are the data the guideline
is judged on.

### 4.7 Why P5 needs this exact rule

The same distinction drives two validator signals, and reading them with the wrong definition
makes a correct generator look broken:

- **`UNCOVERED_QUESTION_CLAUSE`** fires when an answer addresses one component of a multi-part
  question. Under §4.2 that answer is *partly correct*; the warning is a completeness signal
  for P6, not an error and not a refusal.
- **`PROVENANCE_OVERSTATED`** compares a claim against the passage it cites. A partial passage
  can legitimately be cited for a partial claim, and the warning is mostly a content-token
  recall artefact (§2.5), not a relevance judgment.

If the guideline instead scored "supports one component" as 0, P5's behaviour would look wrong
on exactly the questions the pool is built to test, and the two systems would be optimising
against different definitions of the same word.

### 4.8 Scope of these labels

The 100-question P2 handoff of 2026-10-28 is **training-integration** data (`dataset_role` in the
run metadata), not the held-out pool. Labels produced on it are for guideline calibration and
pipeline checks; they must not be reported as held-out evaluation results.
`evaluation.held_out_manifest` remains null until P6 freezes the question/configuration set.

For the frozen pool, P2 and P5 independently label the **same 334 records** (not disjoint
ranges), with a third member adjudicating disagreements per §4.6; the remaining records go to
the other fixed pairs. This assignment is recorded here because it is the one P2 asked to have
stated rather than assumed.

---

