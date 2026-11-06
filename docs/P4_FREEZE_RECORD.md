# P4 freeze record and held-out procedure

Status: **frozen** on 6 November 2026 at 09:47 SGT (commit below); **run and scored** the same day (Slurm
job 51585, section "Held-out run (6 November)"). The record is `configs/p4_freeze.json`; this page explains it
and gives the order of work. The record was written before any held-out question, answer or label was read
for scoring; the labels were read only after the run, by `scripts/score_agent_records.py`.

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

## State at freezing (6 November)

The record was frozen with `code.commit` `ad02d51` (main after PR #50), the all-paper-text index built by
P5 (path and `metadata.json` SHA-256 in the record), `answers.generate` true (ANSWERS=p5, prompt v7,
8 passages x 1200 characters) and `top_k` 8. P5's development check of adaptive at depth 8 (job 51521,
decision `depth-8-dev-check`) came first; development tuning was at depth 5 (disclosure
`depth-5-tuning-8-run`). The 200-question list is used as it is: P3's written confirmation is not
attached to the record (`open_at_freezing`).

## Held-out run (6 November)

P5 ran the frozen configuration once, as Slurm job 51585 (completed, exit 0, 2 h 23 min, one A40, 10:26 to
12:49 SGT, no `RESUME`). The run's `run_manifest.json` reports code `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`
and `git_dirty` false, and the scoring script accepted it against the record (commit, corpus hash, critic
view, prompt budget, retrieval settings, arms; every arm holds exactly the 200 questions). Inputs, checked by
hash before the run: items file `84e909e7...9a48`, all-paper-text corpus `8eeef011...`, dense index
`metadata.json` `a14070a7...`. Settings as recorded: `ARMS="static adaptive static-wide"`, `CRITIC=generator`,
`SCOPED=1`, `OFFLINE=1`, `ANSWERS=p5`, `TOP_K=8`, prompt `p5-grounded-qa-v7`, 8 passages x 1200 characters.
Each arm was run once; no question was rerun.

Two things differ from what the record's text assumed, neither changes a recorded setting:

- **Wide arm depth.** The runner's default for `static-wide` is `top_k x (max_retries + 1)` = 24, which exceeds
  `candidate_k` 20 and is refused at start-up. P5 passed `--wide-k 15` (the recorded `static_wide_k`) through a
  copy of `scripts/cluster/run_agent_experiment.sbatch` kept outside the checkout (SHA-256 `937d2f01...`); the
  repository was not modified. Outputs were written outside the checkout, which is why `git_dirty` is false.
- **No unanswerable questions.** All 200 questions have mapped gold and an answerable label, so the record's
  "unanswerable questions, separately" subset is empty. The rates that need unanswerable questions
  (`correct_refusal_rate`, `unsatisfied_rate_unanswerable`) are `n/a`, and nothing can be said here about
  abstention on unanswerable questions.

Scoring (after the run, gold read only now), with P3's `gold_evidence_mapping_all_splits.jsonl` from
`origin/p3-qasper-foundation`:

```bash
python -m scripts.score_agent_records --role held-out --freeze configs/p4_freeze.json \
    --run-dir <OUT_DIR> --questions held_out_items.jsonl --mapping gold_evidence_mapping_all_splits.jsonl \
    --qa data/processed/qa.jsonl --out-dir scores/held-out-all --label "all 200 questions"
python -m scripts.score_agent_records ... --exclude-ids configs/p4_annotated_held_out_ids.jsonl \
    --out-dir scores/held-out-160 --label "the 160 questions P4 did not annotate"
```

The two score directories were scored at commit `1bfae04`, which differs from the frozen `ad02d51` only in
`configs/default.yaml` and `src/generation/server.py` (the demo server's default depth), and are kept outside
Git with the run's records. The tables are in
`docs/P4_REPORT_CONTRIBUTION.md`, Section 3.8. The result does not change any configuration: per the rule, it
drives no targeted improvement.

## Tests

`tests/test_protocol.py` covers the record checks, the guarded items script, the scoring refusals and the
audit on synthetic data. The scripts were also run on the development job 50977: the rescore matches the
cluster's `metrics.md` on all 24 shared rows, and the audit reproduces the verdict table of the report.
