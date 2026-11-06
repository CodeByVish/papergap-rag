# P4 held-out results

Configuration frozen on 6 November 2026 (`configs/p4_freeze.json`, code `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`)
and run once by P5 (job 51585, clean checkout, one NVIDIA A40): top 8 per round, BM25 and bge-small RRF without
reranking, at most 2 retries, Qwen3-8B critic reading the generator's view, prompt `p5-grounded-qa-v7` with 8 passages
of at most 1,200 characters, answers from the same generator in every arm. Three arms on the same 200 questions:
**static** (top 8, no critic), **adaptive** (the evidence-gap loop) and **static-wide** (15 passages, no critic; its
first k passages are plain retrieval at depth k). Every table is given for all 200 questions and for the 160 that
P4 did not annotate. Read `README.md` first for the limits.

## 1. Mapped-evidence recall

Mean share of a question's gold passages among the retrieved ones (`score-all-200/`, `score-160/`, `evidence/`):

| | static (8) | adaptive | static-wide (15) |
| --- | ---: | ---: | ---: |
| All 200: mean recall | 0.858 | **0.871** | 0.953 |
| All 200: complete evidence | 154 | 157 | 183 |
| All 200: mean passages | 7.97 | 8.28 | 13.95 |
| 160 not annotated: mean recall | 0.881 | **0.897** | 0.959 |
| 160 not annotated: complete evidence | 127 | 130 | 148 |

Plain retrieval by depth (from the 15-passage arm), 200 questions: 0.569 (3), 0.723 (5), 0.858 (8), 0.897 (10),
0.953 (15); 160 questions: 0.585, 0.749, 0.881, 0.907, 0.959.

Paired differences in per-question recall (95% bootstrap interval over questions, 2,000 resamples, seed 0):

| Comparison | 200 questions | 160 questions |
| --- | --- | --- |
| Adaptive minus static top 8 | +0.0133 [0.0008, 0.0283] | +0.0156 [0.0000, 0.0375] |
| Adaptive minus plain retrieval at the same passages (matched budget) | **+0.0008 [-0.0142, 0.0158]** | +0.0094 [0.0000, 0.0250] |

The loop raised recall on 4 of 200 questions (three reached complete evidence), lowered it on none. At equal
passages it does not beat the plain ranking.

## 2. Cost of the loop (adaptive arm)

45 of 200 questions were retried (88 retries). Of the retries, 95.5% added no gold passage, 62.5% were made when
all gold was already retrieved, 46.6% added no new passage. Stop reasons: sufficient 156, max rounds 41,
insufficient information 3. Critic verdicts: 95.8% from the model, 4.2% rule fallback (10 of 239 asked of the model);
17.0% reused from the previous round. Critic audit (200 questions; 160 in brackets): "insufficient" with all gold in
view 54 (50); "insufficient", gold missing 29 (18); "sufficient", all gold retrieved 127 (103); "sufficient", gold
missing 29 (22).

## 3. Abstention and answer counts

All 200 questions are answerable, so there is no correct-refusal rate. The critic was unsatisfied after its last round
on 22.0% of the questions (21.9% on the 160), against the 5% the (disabled) refusal gate allows. The generator
refused 6 questions in every arm; the critic's `INSUFFICIENT_INFORMATION` stop added 3 more in the adaptive arm (9),
all false refusals (1.5%). Two answers per arm were downgraded after a `PARSE_ERROR`.

## 4. Answer quality (overlap only)

`qa/`, `compare/` (project scorer `p6-qa-v0-proposed`; best-matching QASPER reference):

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| Token F1, 200 questions | 0.3681 | 0.3656 | 0.3676 (P5) |
| Token F1, 160 questions | 0.3689 | 0.3690 | n/a |
| Exact match, 200 | 0.005 | 0.005 | 0.005 (P5) |
| Answered / refused / failed (scorer) | 194 / 4 / 2 | 191 / 7 / 2 | 194 / 4 / 2 (P5) |

Adaptive minus static (paper-level bootstrap, 1,000 resamples, seed 42): F1 -0.0025 [-0.0109, 0.0056] on the 200
(174 papers); +0.0001 [-0.0074, 0.0080] on the 160 (142 papers). No answer-quality gain from the loop. Faithfulness
and the other RAG metrics are not available (RAGAS not run).

## 5. Performance

`performance/` (one A40, serial requests, per-arm wall time measured by the runner; latency = agent time plus
generation time per question, n = 198 after the scorer's technical errors):

| Arm | Wall time (s) | Questions/s | p50 (s) | p95 (s) | Prompt tokens | Output tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| static | 2,519 | 0.079 | 10.1 | 21.5 | 934,334 | 73,586 |
| adaptive | 3,583 | 0.055 | 16.4 | 31.5 | 928,803 | 74,598 |
| static-wide | 2,456 | 0.081 | 10.1 | 21.2 | 934,460 | 73,573 |

Tokens are the generator's. The critic's tokens were not recorded (251 critic calls, 2 escalations), so the adaptive
arm's totals are lower bounds. Retrieval takes about 0.04 s per question; the agent loop adds a mean 5.6 s. Cost is
empty: the model is local, no price was supplied. Static-wide's prompt is the same size as static's, which fits the
generator rendering at most 8 passages.

## 6. Readings and limits

- The held-out run does not support the claim that evidence-gap-driven retrieval improves recall or answers: the gain over
  static top 8 is small, there is none over reading the same number of passages, and F1 is unchanged. Retrieval depth is
  the factor that matters.
- Clipping: 232 of the 347 held-out gold passages (66.9%) exceed 1,200 characters. Part of the loop's wasted retries
  comes from the clipped view the critic reads (development check, job 51691); this was not tested on the held-out
  primary run.
- A 2,500-character budget was run afterwards as post-hoc sensitivity analyses (development job 51691, held-out job
  51705). They are not included here and never replace the primary result.
- Each arm ran once; run-to-run variation of the critic was not measured.
