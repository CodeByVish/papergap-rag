# P4 freeze record and held-out procedure

Status: **draft**. The record is `configs/p4_freeze.json`; this page explains it and gives the
order of work. Nothing here has touched a held-out question, answer or label.

## Why

`docs/EVALUATION.md`: *before reading any held-out question, record the final Git commit and
configuration, then freeze the chunker, prompts, retrieval settings, model settings and evaluation
protocol; read held-out answers and labels only afterwards, for scoring.* A genuine bug found after the
freeze is fixed only with its cause recorded and every affected comparison rerun (`P3-D006`). A held-out
result never drives a targeted improvement.

The record is the sealed envelope: what will be run, on what, how it will be reported, and what the
author already knew. The scripts below enforce the order.

## What the record holds

| Part | Content |
| --- | --- |
| `code`, `frozen_at` | the main commit the run is made at, and when the record was frozen |
| `corpus` | the development corpus (21,360 passages) and the all-paper-text corpus the run needs (28,617 passages, 1,584 papers, SHA-256 `8eeef011...`, byte-identical to P3's pinned build) |
| `dense_index` | the pinned `bge-small-en-v1.5` revision and, once built, the index path and the SHA-256 of its `metadata.json` |
| `questions` | P3's frozen list: 200 questions, 174 papers, SHA-256 `d509010b...` (the hash in P3's own manifest) |
| `retrieval`, `agent` | candidate pool 20, RRF 60, top 8, no reranker, section-scoped retries, at most 2 retries, Qwen3-8B critic reading the generator's view (8 passages x 1200 characters), refusal rule off |
| `arms`, `baseline_depths` | static, adaptive, and the 15-passage run from which the plain ranking at depth 3, 5, 8, 10 and 15 is read |
| `metrics`, `reporting` | what is reported whatever the outcome, and the subsets |
| `disclosures` | what the author already knew (below) |
| `decisions` | what was decided before the freeze: the refusal rule stays off, the critic is final |

## Disclosure: 40 of the 200 questions were read while annotating

P4's author labelled annotator B's batches 09 and 10 on 4 November and so read 40 held-out questions
and their retrieved passages (ids in `configs/p4_annotated_held_out_ids.jsonl`). Every later change was
driven by the development jobs, but nobody can prove that about their own reasoning, so the report gives
the results on all 200 questions **and** on the 160 not annotated by P4. Other team members read the
questions in the same way while annotating; the rule forbids tuning on them.

## Order of work

1. **Final configuration: done.** Job 51172 (critic with the generator view, handles and quote check),
   read with `python -m scripts.audit_critic --run-dir ... --items items.jsonl`, is the configuration
   that is frozen; the refusal rule stays off (decision `refusal-rule-off`). Merge the
   `stop_reason` change and note the merge commit; the freeze commit must include it.
2. **Build the held-out index** over the all-paper-text corpus (CPU is enough, or on the cluster):

   ```bash
   python -m scripts.build_indexes --passages passages_all_paper_text.jsonl \
       --output-dir indexes/p4-all-paper-text --device cpu --local-files-only
   sha256sum indexes/p4-all-paper-text/metadata.json
   ```

3. **Freeze.** Fill `code.commit`, `dense_index.path`, `dense_index.metadata_sha256`, `frozen_at`,
   resolve `answers.generate`, set `status` to `frozen`, and commit. That commit is the
   freeze. `freeze_problems` in `src/agent/protocol.py` lists whatever is still missing.
4. **Write the run's input** (refuses unless step 3 is done and the list matches the recorded hash):

   ```bash
   python -m scripts.make_held_out_items --questions qa_for_held_out_v2.jsonl \
       --freeze configs/p4_freeze.json --out runs/p4/held_out_items.jsonl
   ```

   The file holds `question_id`, `question` and `paper_id` only.
5. **P5 runs the job** at the frozen commit, with the corpus, index and items above
   (`PASSAGES`, `DENSE_INDEX`, `ITEMS`, `ARMS="static adaptive static-wide"`, `ANSWERS` as recorded,
   `SCOPED=1`, `OFFLINE=1`, `TOP_K=8`). The run has no gold.
6. **Score after the run**, when the gold may be read. Refused unless the run's manifest matches the
   record (commit, corpus hash, critic view, prompt budget, retrieval settings, arms) and every arm holds
   exactly the 200 questions:

   ```bash
   python -m scripts.score_agent_records --role held-out --freeze configs/p4_freeze.json \
       --run-dir runs/p4/held-out --questions runs/p4/held_out_items.jsonl \
       --mapping gold_evidence_mapping_all_splits.jsonl --qa data/processed/qa.jsonl \
       --out-dir scores/held-out-all --label "all 200 questions"
   python -m scripts.score_agent_records ... --exclude-ids configs/p4_annotated_held_out_ids.jsonl \
       --out-dir scores/held-out-160 --label "the 160 questions P4 did not annotate"
   ```

7. **Report** every table the record lists, with the covered questions stated, including any in which
   the adaptive arm does not beat the plain ranking.

## Still to settle before step 3

- whether the run also generates answers (needs P5's compute and a decision on the 8-passage,
  1200-character budget, which P5 keeps frozen);
- P3's confirmation, with P6, that the agent's held-out run uses this 200-question list (the plan names
  100 questions; 200 fits one job).

## Tests

`tests/test_protocol.py` covers the record checks, the guarded items script, the scoring refusals and the
audit on synthetic data. The scripts were also run on the development job 50977: the rescore matches the
cluster's `metrics.md` on all 24 shared rows, and the audit reproduces the verdict table of the report.
