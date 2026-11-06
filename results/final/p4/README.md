# P4 submission results: agent held-out run

The frozen agent configuration, run once on P3's 200 held-out questions (Slurm job 51585, 6 November 2026),
scored afterwards against P3's gold and the QASPER references. `RESULTS.md` has the findings and denominators;
`INPUTS.json` pins every input by hash; `SHA256SUMS.json` lists these files. The procedure and what was fixed
before the run are in `docs/P4_FREEZE_RECORD.md` and `configs/p4_freeze.json`.

## Layout (`held-out/`)

| Folder | Content |
| --- | --- |
| `run/` | The cluster run's own `run_manifest.json`, `metrics.json` and `metrics.md` (questions only, no gold) |
| `score-all-200/`, `score-160/` | Retrieval scores from `scripts/score_agent_records.py --role held-out` (all 200 questions; the 160 not annotated by P4), including the critic audit and the paired recall gains |
| `evidence/{static,adaptive}/` | Mapped-evidence recall by P6's `evidence` step, with per-question scores (static at K = 5, 8, 10 from the 15-passage arm) |
| `qa/{static,adaptive}/` | Token F1 and exact match by P6's `qa` step, with per-question scores |
| `compare/` | Paired static-versus-adaptive differences (P6's `compare` step), all 200 and the 160 |
| `performance/{static,adaptive,static-wide}/` | Latency percentiles, throughput and token ledgers (P6's `performance` step) |
| `usage/` | Generator token ledgers per arm, built from each record's generation statistics |
| `ragas/{static,adaptive}/`, `ragas/compare/` | Live RAGAS scores (faithfulness, response relevance, context precision) with per-question scores, run manifests, the judge configuration (no key) and the paired differences; `ragas/kit/` has the run script and the wrapper patch |
| `PIPELINE_NOTES.md` | How the P6-pipeline outputs were produced |

## What is not here

- **The per-arm answer records** (`static.jsonl`, `adaptive.jsonl`, `static-wide.jsonl`, about 19 MB with the log)
  stay outside Git. They are in the delivery archive `p4-heldout-51585-20261106.tar.gz` (SHA-256
  `96b3e0fc82314afa9527e4f0e351264c1b2163f8670414360269d62fdb6ad08f`); the hashes of each file are in `INPUTS.json`.
- **The corpus, the dense index and the model** are not duplicated; their hashes are in `INPUTS.json`.
- **The RAGAS judge traces** (2.4 MB per arm) and the rendered-contexts files are not included; their hashes are in `INPUTS.json` and the run manifests. The fifteen-passage arm was not judged.
- **The 2,500-character runs** (development job 51691, held-out job 51705) are post-hoc sensitivity analyses and are
  not part of this folder; they are added under a separate label once scored.

## Read before using the tables

- **The primary result is the 1,200-character run.** The prompt renders at most 8 passages of 1,200 characters, fixed
  before the run. Nothing was changed after the result was known; each arm ran once.
- **All 200 questions are answerable**, so abstention on unanswerable questions was not measured and
  `correct_refusal_rate` and `unanswerable correctness` are `n/a`.
- **Part of the set was read before the freeze.** P4's author annotated 40 of the 200 questions (disclosure `p4-annotated-40`
  in the freeze record), so every table is given for all 200 and for the 160 that were not annotated by P4. Other members'
  prior use of the questions has not been audited, so the 160 are not claimed to be independent.
- **Bootstrap intervals** in `score-*/` resample questions (2,000 resamples, seed 0); those in `compare/` resample papers
  (1,000 resamples, seed 42). They are not interchangeable with the paper-clustered retrieval intervals in `results/final/p2/`.
- **Role label.** The `evidence/`, `qa/`, `compare/` and `performance/` outputs were produced with `--role development`
  because the `held_out` label needs a team sign-off that has not been given. The numbers do not depend on the label; rerun
  with `--role held_out --review <file>` after sign-off. The `qa/` copies are P4's reproduction of P5's scoring; P5's
  own outputs give identical figures (static F1 0.3681, adaptive 0.3656).
- **Scoring policy.** EM and F1 use the project's proposed scorer (`p6-qa-v0-proposed`, best-matching reference), not the
  official QASPER evaluator. EM is near zero because the generator writes sentences and the references are short spans.
- **Timing** is one A40, one request at a time, warm engine, no score cache; the scorer counts the two validator-downgraded
  answers per arm as technical errors, so latency percentiles use 198 questions. Critic token use was not recorded.
- **RAGAS caveats.** The judge is a hosted LLM (`qwen-plus-2025-12-01` via DashScope), so the scores are model judgments, not human verification; the run did not store the rendered prompts, so the contexts were produced afterwards (method to be confirmed by P5); DashScope's embeddings endpoint needed a wrapper (`ragas/kit/run_p6_evaluation_dashscope.py`) that sets `check_embedding_ctx_length=False` while the evaluator itself is unmodified; refusals and failures are excluded from each denominator; the outputs carry the `development` role label.
- Manifests keep their producer paths (local paths on the producing machines); read them as historical.

## Reproduce

From the repository root, with P3's `gold_evidence_mapping_all_splits.jsonl` (commit `1a1dc15b`), the run's
`held_out_items.jsonl` and `data/processed/qa.jsonl`:

```sh
python -m scripts.score_agent_records --role held-out --freeze configs/p4_freeze.json \
  --run-dir <run>/runs/p4/held-out-200 --questions held_out_items.jsonl \
  --mapping gold_evidence_mapping_all_splits.jsonl --qa data/processed/qa.jsonl \
  --out-dir score-all-200 --label "all 200 questions"
# add --exclude-ids configs/p4_annotated_held_out_ids.jsonl for the 160
```

The `evidence`, `qa`, `compare` and `performance` steps are those of `docs/P6/EVALUATION_TEAM_HANDOFF.md`
(`python -m scripts.run_p6_evaluation <step> ...`); `static-wide.jsonl` stands in for the handout's `static-top10.jsonl`
with `--saved-depth 15 --ks 5 8 10`.
