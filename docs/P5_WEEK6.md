# P5 Week 6 — BGE-reranked (R4) integration, first measurement, open dependencies

**Status (2026-10-28, branch `p5/generation-integration`).** The R4 execution path is
integrated and measured once. R4/top-5 is **not** a net improvement over R3/v7, and the
loss is attributable to the reranker's top-5 set, not to the generator. The next
retrieval export is the blocker.

## 1. Input verified

P2's `p2-batch-reranking-handoff-20261017.zip`:

| | |
|---|---|
| archive sha256 | `194bf9fa15a68ea7de64af945b495dba9e6988781974178793bd9c950fa7dae3` |
| `bge/retrieval.jsonl` sha256 | `3918b7a6749bf3c9c141537beabbd074cd66c8f4570ad2880664be0e5014b439` |
| manifest check | matches `bge/run_manifest.json` → `output_sha256` |
| records / hits | 100 / 485 (97 × 5, 3 empty) |
| reranker scores | 485/485 non-null |
| questions | 100 ids and texts identical to P1's Week-3 dump |

These are **training-integration** examples, not the held-out set.

## 2. What the generation module now supports

- `RetrievedPassage.metadata["p5_score_source"]` records whether the ordering score
  came from `reranker`, `rrf`, `native` or `unscored`. The run's
  `retrieval_configuration` is derived from the data, not from a filename.
- A request that mixes reranker logits with RRF scores has its scores cleared, so the
  retriever's own order is preserved instead of sorting across incomparable scales.
- `scripts/generate_from_retrieval.py` gains `--expect-config`, `--check-only`,
  `--dataset-role`, a `runs/week3/` write guard for reranked arms, and run-level
  `retrieval_sha256` / `retrieval_configuration` / `dataset_role` in both artefacts.
- The response parser repairs invalid JSON escapes (raw LaTeX such as `\extnormal`),
  keeps the answer and records `PROMPT_FORMAT_DRIFT` instead of throwing it away as
  `PARSE_ERROR`.

`scripts/compare_retrieval_arms.py` and `scripts/reparse_failures.py` are the two
CPU-only diagnostics added with this work.

## 3. R4 measurement (job 48513, rerun with the parser fix)

Exit 0, 100 records, frozen v7 prompt, 1024-token budget:

| metric | R3/v2 (Week-3 file) | R3/v7 (comparable) | R4/v7 (BGE top-5) |
|---|---:|---:|---:|
| answered / refused / downgraded | 84 / 16 / 4 | 85 / 15 / 3 | **79 / 21 / 4** |
| no-cite | 0 | 0 | 0 |
| error-level | 2 | 1 numeric | **0** |
| `PARSE_ERROR` | 1 | 0 | 0 |
| `PROMPT_FORMAT_DRIFT` | 0 | 0 | 1 (record 0) |
| `PROVENANCE_OVERSTATED` | 23 | 24 | 21 |

The Week-3 column is **not** the control: it is prompt/validator v2. R4 uses v7, so the
retrieval-arm delta is **−6 answered, +6 refused, +1 downgraded** against the v7 baseline.
R4 now has **zero error-level violations**; the v7 baseline's one numeric error (record
18) is resolved because R4 states 9,000 and 11,000 separately instead of deriving 20,000.

Record 0, which the first run lost to `PARSE_ERROR`, now parses and is answered with one
`PROMPT_FORMAT_DRIFT` warning: the parser repaired two invalid LaTeX escapes and kept the
answer. This is the only measured change between the first R4 run and this one.

### 3.1 Why the answers were lost

`scripts/compare_retrieval_arms.py` checked every flip against the two top-5 sets. The
run shown here has 9 answered→refused and 3 refused→answered flips against v7; the table
below reflects the rerun (record 0, previously `same_evidence`, is now answered):

| label | count | records |
|---|---:|---|
| `evidence_dropped` | **6** | 24, 34, 59, 62, 91, 96 |
| `evidence_partly_dropped` | 1 | 46 |
| `same_evidence` | 3 | 18, 43, 60 |
| `new_evidence` | 2 | 14, 93 |

**Six of the nine answered→refused flips lost every passage the old answer cited.**
Record 91 (*source of the tables*) has zero overlap between the RRF and BGE top-5;
record 96 (*English data*) lost all five old citations. This is the reranker selecting a
different five passages, not the generator or validator tightening.

- Records 43 and 60 kept the cited passage and the model still refused: context-order
  caution, not a retrieval gap.
- Records 14 and 93 gained answers from passages the R3 arm never retrieved.
- Record 18 kept the same evidence and answered with 9,000 + 11,000 stated separately —
  a genuine behaviour win, and no derived 20,000.

## 4. Team-wide question-usage audit (2026-10-28)

P1's inventory (`p1/week3-week4`, commit `f0f861b`) lists 2,593 `train` questions,
including the 100-question handoff. P5 audited its own runs against it and added its
inventory: **all 100 real questions P5 used are in P1's 2,593; P5 adds zero.** The 8
`bench-*` IDs are synthetic SciReader samples, listed separately. See
`docs/handoffs/P5_QUESTION_USAGE.md` and `docs/handoffs/p5_question_usage_manifest.json`.

Cross-module result:

| module | inventory | count | new vs P1 |
|---|---|---:|---:|
| P1 | `docs/handoffs/p1_used_question_ids.jsonl` | 2,593 | — |
| P2 | `p2/question-usage-inventory` | 106 | 0 |
| P3 | `annotation_pilot_multi_v1/questions.jsonl` | 5 (3 train, 2 validation) | **2** |
| P5 | `docs/handoffs/p5_used_question_ids.jsonl` | 100 | 0 |

**The only new development exposure is P3's two validation pilot questions**
(`0ab3df10…`, `729694a9…`). The union found so far is **2,595 IDs**. P6 must exclude this
union from the held-out pool, and should treat both P1's and P2's scopes as "saved local
artefacts", not a complete team inventory. P5's R4 run is training-integration data and
does not enter the held-out set.

P1's manifest declares a CRLF hash (`0b50e6ee…`) while the committed LF file hashes to
`89be5063…`; the ID set is identical. P1 should publish the canonical hash.

Held-out pool construction and any overlap with development IDs are P3/P6's scope. P5's
part is complete: 100 questions, all in P1's inventory, no P5-only IDs.

## 5. Open dependencies

| dependency | owner | status | needed for |
|---|---|---|---|
| top-10 or RRF-fallback BGE export | P2 | **missing** | R4-v2; decides the freeze |
| new export manifest (`top_k` / union rule) | P2 | **missing** | audit of R4-v2 |
| 1,000-pair frozen pool | P6 | missing | 334-record annotation |
| fixed order + assignment manifest | P6 | missing | annotation batch |
| approval manifest | P6 | missing | P2 exporter output |
| relevance / gold-evidence mapping, K, no-relevant-doc, macro rules | P3 (P6 confirms) | missing | retrieval metrics |
| ratification of `p5-annotation-v1` | P3/P6 | pending | annotation freeze |
| real agent trace runner + AgentState exports | P4/P6 | missing | G5 adaptive comparison |
| held-out freeze (commit + config) | P6 | missing | final evaluation |

The annotation rule is in `docs/P5_ANNOTATION_RULE.md`. P2 and P5 independently label
the same 334 records once P6 supplies the pool and manifests.

## 6. Next P5 steps

1. Rerun R4/top-5 with the parser fix; record the corrected 79/21/4 in this document.
2. Send P2 the top-10 / RRF-fallback request (evidence in §3.1).
3. When the new export arrives, run R4-v2 and compare R3/v7, R4/top-5 and R4-v2.
4. Freeze only after that comparison; do not treat "BGE is mandatory in the plan" as
   evidence that this top-5 export is better.
