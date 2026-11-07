# P5 final outputs — held-out generation run 51585

P5 owns answer generation and grounding. This folder holds the final held-out run
that produced the answers used by P4's evaluation and by the report's Q4.4 and Q4.6
items: three retrieval arms over the same 200 held-out questions, one answer record
per question per arm, plus the QA and live-RAGAS scores computed from those records.

| | |
| --- | --- |
| Slurm job | 51585, `COMPLETED`, exit 0, TC2N01 (one NVIDIA A40), 2:23:09 |
| Code | `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`, `git_dirty: false` |
| Items | `p4_held_out_items.jsonl`, 200 lines, SHA-256 `84e909e7…f9a48` |
| Corpus | `passages.jsonl`, SHA-256 `8eeef011…aa93e` |
| Dense index | `metadata.json`, SHA-256 `a14070a7…2ba7ef` |
| Arms | `static` (top-8), `static-wide` (top-15), `adaptive` (critic-driven retries, top-8) |
| Retrieval | `SCOPED=1`, `OFFLINE=1`, `BGE=0`, `ANSWERS=p5`, `candidate_k=20`, `top_k=8`, `wide_k=15`, `max_retries=2` |
| Generator | Qwen3-8B, vLLM 0.11.0, bfloat16, `temperature=0.0`, `top_p=0.9`, `enable_thinking=false`, `max_model_len=32768`, `max_new_tokens=1024` |
| Prompt | `p5-grounded-qa-v7`, 8 passages × 1,200 characters |
| Delivery archives | `p4-heldout-51585-20261106.tar.gz` SHA-256 `96b3e0fc…6ad08f`; `p4-qa-51585-20261106.tar.gz` SHA-256 `0b9f6992…7a04`; `p4-ragas-live-51585-20261106.tar.gz` SHA-256 `5dc5708a…ced7` |

`p5-evidence.md` in `report/review-checks/` is the review record for these numbers;
`docs/handoffs/P5_365-40_R4_20261102.md` describes the retrieval inputs.

## Layout

| Path | What it is |
| --- | --- |
| `held-out-200/static.jsonl`, `adaptive.jsonl`, `static-wide.jsonl` | The delivered answer records, 200 per arm. Each row holds the question, the retrieved passages, the critic trace and the `answer` object (`answer`, `citations`, `evidence_status`, `retrieval_rounds`, `provenance`). |
| `held-out-200/metrics.json`, `metrics.md` | The run's own metrics: rounds, passages, retries, critic behaviour, refusal rate, elapsed time. |
| `held-out-200/run_manifest.json` | The producer manifest: arguments, hashes, environment, package versions, git commit. |
| `qa/<arm>/` | `qa.csv`, `scores.jsonl`, `summary.json` and `run_manifest.json` from `python -m scripts.run_p6_evaluation qa` at `ad02d51`. |
| `ragas-live/<arm>-live/` | `ragas.csv`, `scores.jsonl`, `summary.json`, `judge_config.json` and `run_manifest.json` from the live DashScope judge. |
| `ragas-live/judge-config.json` | The judge and embedding model used for both judged arms. |
| `logs/p4-agent-51585.out` | The Slurm stdout of the run. |
| `INPUTS.json` | Hashes of the frozen inputs and of the three delivery archives. |
| `SHA256SUMS.json` | SHA-256 of every file in this folder. |

## Headline numbers

Per arm, 200 questions, 0 generation errors and 0 answer errors.

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| `SUFFICIENT` records | 194 | 191 | 194 |
| `INSUFFICIENT` records | 6 | 9 | 6 |
| QA answered / refused / failed | 194 / 4 / 2 | 191 / 7 / 2 | 194 / 4 / 2 |
| QA EM | 0.005 | 0.005 | 0.005 |
| QA F1 | 0.368 | 0.366 | 0.368 |
| RAGAS faithfulness | 0.8918 | 0.9069 | not judged |
| RAGAS response relevance | 0.8542 | 0.8540 | not judged |
| RAGAS context precision | 0.5781 | 0.5774 | not judged |

`RESULTS.md` gives the full tables, including the retrieval-loop and latency numbers.

## What is not here

- **The corpus and the dense index** are not duplicated; their hashes are in `INPUTS.json`.
- **The RAGAS judge traces** (`judge_trace.json`, 2.4 MB static, 0.4 MB adaptive) and the
  rendered contexts are not included; the scores and per-question rows are.
- **The judge kit** (`live-ragas-kit/run_p6_evaluation_dashscope.py`, `run_live_ragas.sh`)
  is not vendored here. It is a thin wrapper that sets
  `check_embedding_ctx_length=False` for DashScope embeddings and calls the repository's
  evaluator unchanged; the evaluator source hashes are in each `run_manifest.json`.
- **The `static-wide` arm was not judged** with RAGAS, and no arm was judged for
  faithfulness beyond the 194/191 answered records.
- **The held-out `performance/` and `evidence/` scores** live in `results/final/p4/`
  because P4's evaluation pipeline produced them from these records; they are not copied.

## Read before using these numbers

- **Refusals are split in two places.** The records carry `evidence_status`, giving
  194/191/194 `SUFFICIENT`. The QA scorer classifies the two records per arm that were
  downgraded after a `PARSE_ERROR` (ids `de830c534c…` and `cbb3c1c1e6…`) as failures rather
  than refusals, so its refused counts are 4/7/4. Both views describe the same records.
- **The refusal string** is `Insufficient evidence in the retrieved passages to answer this
  question.`; an `INSUFFICIENT` record has no citations. No record mixes a refusal with a citation.
- **Role label.** The held-out role gate needs a review file that is not in the repository,
  so the QA scoring used `--role development`. The reference set is identical; the held-out
  label remains to be recorded.
- **Scoring policy** is `p6-qa-v0-proposed`, not the official QASPER evaluator. EM is near zero
  because the generator writes sentences and the references are short spans; F1 is the usable
  figure.
- **All 200 questions are answerable** according to QASPER annotations, so the unanswerable
  subset is empty and `unanswerable_correctness` is undefined.
- **RAGAS is a live judge, not a frozen one.** The judge was `qwen-plus-2025-12-01` with
  `qwen3.7-text-embedding` at `max_workers=1`, `max_retries=0`; a rerun may not reproduce
  the same scores.
- **Latency is serial and observational.** One request at a time on one A40; it is not a
  throughput benchmark.
- **The model directory records no Hub revision.** The cache ref names
  `b968826d9c46dd6066d109eabc6255188de91218`, but that snapshot is incomplete and its files
  do not match the served directory, so no revision is claimed.
- **The 2,500-character context-budget run (job 51705)** is a post-hoc sensitivity analysis
  and is not part of this folder; it is in `results/final/p4/sensitivity-2500/`.
