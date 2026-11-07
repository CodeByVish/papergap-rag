# P5 final results — job 51585

All figures come from the files in this folder unless a row says otherwise. Numbers are
rounded for reading; the JSON and CSV files carry full precision.

## 1. Records and refusal behaviour

200 questions per arm, 0 generation errors, 0 answer errors.

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| records | 200 | 200 | 200 |
| `SUFFICIENT` | 194 | 191 | 194 |
| `INSUFFICIENT` | 6 | 9 | 6 |
| records with no citation | 6 | 9 | 6 |

The refusal text is `Insufficient evidence in the retrieved passages to answer this
question.` No record pairs a refusal with a citation. Six of the `INSUFFICIENT` records
per arm are refusals produced by the generator; two per arm were downgraded to refusal
after a `PARSE_ERROR` (`de830c534c…`, `cbb3c1c1e6…`).

## 2. Retrieval loop and critic

From `held-out-200/metrics.json`.

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| mean rounds | 1.000 | 1.440 | 1.000 |
| mean passages | 7.965 | 8.280 | 13.945 |
| gaps detected | 21 | 47 | 20 |
| retries | 0 | 88 | 0 |
| critic gap recovery rate | 0.000 | 0.064 | 0.000 |
| redundant retry rate | n/a | 0.466 | n/a |
| critic reused rate | 0.000 | 0.170 | 0.000 |
| critic LLM rate | 0.000 | 0.958 | 0.000 |
| critic fallback rate | 0.000 | 0.042 | 0.000 |
| critic thinking drift | 0.000 | 0.000 | 0.000 |

The run manifest records 251 critic calls and 2 escalations. `questions_with_gold` is 0 in
every arm, so the recall and gold-recovery columns in `metrics.json` are `null`: the run
had no gold passage ids to score retrieval against. Retrieval recall is scored in
`results/final/p4/evidence/`, not here.

## 3. QA scores (`p6-qa-v0-proposed`)

Scored at `ad02d51` from these records against P3's `data/processed/qa.jsonl`.

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| answered | 194 | 191 | 194 |
| refused | 4 | 7 | 4 |
| failed | 2 | 2 | 2 |
| answer coverage | 0.970 | 0.955 | 0.970 |
| EM | 0.005 | 0.005 | 0.005 |
| F1 | 0.3681 | 0.3656 | 0.3676 |
| answered-only F1 | 0.3794 | 0.3828 | 0.3789 |

On the 160 questions P4 did not annotate, static F1 is 0.369 (155 answered) and adaptive
F1 is 0.369 (152 answered). All 200 questions carry at least one answerable QASPER
annotation, so the unanswerable subset is empty and `unanswerable_correctness` is
undefined.

The scorer counts the two parse-error downgrades per arm as failures, which is why its
refused counts (4/7/4) are two lower than the `INSUFFICIENT` counts (6/9/6).

## 4. Live RAGAS

Judge `qwen-plus-2025-12-01`, embedding `qwen3.7-text-embedding` (DashScope,
`max_workers=1`, `max_retries=0`, timeout 120 s), `ragas==0.2.15`. Refusals and
parse-error failures are excluded from each metric.

| metric | static | static-wide | adaptive |
| --- | ---: | ---: | ---: |
| faithfulness | 0.8918 (n=194) | not judged | 0.9069 (n=191) |
| response relevance | 0.8542 (n=193) | not judged | 0.8540 (n=189) |
| context precision | 0.5781 (n=194) | not judged | 0.5774 (n=191) |

Paired differences, adaptive minus static, over 188–191 questions, 2,000 resamples,
seed 0: faithfulness +0.0116 (−0.0005, 0.027); response relevance −0.0030 (−0.0075,
0.0011); context precision −0.0025 (−0.0146, 0.0095). One static and two adaptive
response-relevance rows are invalid judge scores.

## 5. Timing

Serial, warm engine, one A40. Answer-only latency from `answer_s` (nearest rank over
200 values):

| | p50 | p95 |
| --- | ---: | ---: |
| static | 10.6 s | 23.6 s |
| adaptive | 11.2 s | 24.0 s |
| static-wide | 10.6 s | 22.2 s |

The agent loop (`elapsed_s`) adds a mean 5.6 s per adaptive question (p95 12.3 s). The job
wall time is 2 h 23 min. These are observed timings, not a controlled throughput
benchmark; model load, concurrency and cache effects are excluded. A recomputation from
the delivered records gives p50 10.5/11.0/10.5 s; the 0.1–0.2 s difference is a percentile
convention question and does not change the report's rounding.

## 6. What these numbers do not cover

- The `held_out` role label: the gate needs a review file that is not in the repository,
  so QA ran with `--role development`. The reference set is identical.
- The official QASPER evaluator: the project scorer is used, so EM is near zero by design.
- Retrieval recall and groundedness: scored by P4 under `results/final/p4/`.
- The 2,500-character sensitivity run: `results/final/p4/sensitivity-2500/`.
