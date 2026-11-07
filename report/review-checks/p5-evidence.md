# P5 report review evidence

Status: **P5 content approved by Junyu Hu on 6 November 2026; DONE FOR DRAFT - P5 scope only.**
This approval covers the items and checks listed below, including the final held-out QA and live
RAGAS scores. It does not certify the Qwen3-8B Hub revision, the final Q4.3 gold and the other
annotators' records, the Q5 ablations, or the team report. Q4.3 annotator A's own label provenance
was added on 7 November 2026 (final section).

## Run used for the P5 checks

| | |
| --- | --- |
| Slurm job | 51585, `COMPLETED`, exit 0, TC2N01 (one NVIDIA A40), 2:23:09 |
| Code | `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`; `git_dirty: false` |
| Items | `p4_held_out_items.jsonl`, 200 lines, SHA-256 `84e909e705b44c2827c5c44f53da0a56e44a766be61b1deeda7e381e2b2f9a48` |
| Corpus | `passages.jsonl`, SHA-256 `8eeef0119e322fc9253255e2c6db6cb38ec276d7ebf3669dd28a856a636aa93e` |
| Dense index | `metadata.json`, SHA-256 `a14070a74a041accb93064f893a560a5dacc94eb85391896d2f8d548222ba7ef` |
| Settings | `static adaptive static-wide`; critic `generator`; `SCOPED=1`, `OFFLINE=1`, `BGE=0`, `ANSWERS=p5`, `TOP_K=8`, `wide_k=15`; prompt `p5-grounded-qa-v7`, 8 x 1,200 characters, `max_new_tokens=1024` |
| Delivery | `p4-heldout-51585-20261106.tar.gz`, SHA-256 `96b3e0fc82314afa9527e4f0e351264c1b2163f8670414360269d62fdb6ad08f` |
| QA bundle | `p4-qa-51585-20261106.tar.gz`, SHA-256 `0b9f69920aaaa5938eeab43486fb2e6e47c948837c85ee9a700140bf7e657a04` |
| Live RAGAS bundle | `p4-ragas-live-51585-20261106.tar.gz`, SHA-256 `5dc5708a2b367267b48b8e499caed80de426da195f6c9f7a3d226c3ddba4ced7` |

Hashes of the delivered files:

| File | SHA-256 |
| --- | --- |
| `run_manifest.json` | `466e4a00d9cc9c671760cbc7e1b4e9bd9e467520d421d9cef84e15a351e34021` |
| `metrics.json` | `d7237a3a907be103c0812fba5192d869686cc18ca887de915505801d901c5cb6` |
| `metrics.md` | `1571a94014bcddbd4ccca1f95f52464285972a1cebc0b87c7b627bc54c15d950` |
| `static.jsonl` | `7b7e29428d8f410bfa5ad27a4b3830876a99e7ad408dd742a242bf5989121620` |
| `adaptive.jsonl` | `d9b10906e3220db915d337fead1d01ba489c4dd540f0d3677bafda7f4e0a3405` |
| `static-wide.jsonl` | `dedad13b0eec25bd0aa738a752231c942806f5749304a904bf7d026107ba7848` |
| Slurm log | `5a37ff8aa15ab532e42428333db647a05d4faf7d9b8778f2a717bd65bc38b613` |

## Checks by report item

- **Q1.2 (answer/refusal behavior).** The final records return the canonical refusal string
  "Insufficient evidence in the retrieved passages to answer this question." with
  `evidence_status = INSUFFICIENT` and no citations. `INSUFFICIENT` records: static 6, adaptive 9,
  static-wide 6; no record mixes a refusal with a citation. The search-scope statement and the
  example remain with P6/P4.
- **Q4.1 (generation).** `run_manifest.json` records `prompt_version = p5-grounded-qa-v7`,
  `prompt_budget = {8, 1200}`, `max_new_tokens = 1024`, and generator options
  `{dtype: bfloat16, temperature: 0.0, top_p: 0.9, enable_thinking: false, max_model_len: 32768}`.
  Package snapshot: Python 3.12.10, vLLM 0.11.0, transformers 4.57.6, torch 2.8.0. The model
  directory stores no Hub revision. The Hub cache ref
  `~/p5/hf/hub/models--Qwen--Qwen3-8B/refs/main` says `b968826d9c46dd6066d109eabc6255188de91218`,
  but that cache's snapshot is incomplete and its files could not be matched to the served model
  directory, so the revision is not claimed in the report.
- **Q4.2 (prompt rendering and output parsing).** `PromptConfig` defaults are
  `max_passages = 8` and `max_chars_per_passage = 1200`; the prompt lists the exact rendered citation
  ids and the parser performs limited repair of malformed escapes. The clipping figures in the report (73.3%, 33 of 45 development gold passages over 1,200 characters; 66.9%,
  232 of 347 held-out gold passages) were recomputed by P4 on the final 365/40 corpus; P5 did not recompute them.
- **Q4.4 (answer/refusal records and QA scores).** 200 records per arm, 0 generation errors and
  0 answer errors. P5 `evidence_status`: `SUFFICIENT` 194/191/194 and `INSUFFICIENT` 6/9/6; two
  records per arm were downgraded to refusal after a `PARSE_ERROR` (question ids
  `de830c534c...` and `cbb3c1c1e6...`).
  QA was scored with `python -m scripts.run_p6_evaluation qa` at commit `ad02d51`, using P3's
  `data/processed/qa.jsonl` (SHA-256 `1515fc586dc9070a0f548ea707892333496c8e38b3fc1c4e12eab3e07af3759e`,
  5,049 rows) and the delivered records. The held-out role gate requires a review file that is not
  in the repository, so the runs used `--role development`; the reference set is identical and the
  gate remains to be recorded.
  Results (policy `p6-qa-v0-proposed`): static EM 0.005 / F1 0.368, answered 194, refused 4,
  failed 2; adaptive EM 0.005 / F1 0.366, answered 191, refused 7, failed 2; static-wide EM 0.005 /
  F1 0.368, answered 194, refused 4, failed 2. On the 160 questions P4 did not annotate, static F1
  is 0.369 (155 answered) and adaptive F1 is 0.369 (152 answered). All 200 questions carry at least
  one answerable QASPER annotation, so the unanswerable subset is empty and
  `unanswerable_correctness` is not defined. The scorer classifies the two parse-error downgrades
  per arm as failures rather than refusals, which is why the QA refused counts are 4/7/4.
- **Q4.5 (RAGAS).** Live judge run on 6 November 2026 with `ragas==0.2.15`, judge
  `qwen-plus-2025-12-01`, embedding `qwen3.7-text-embedding` (DashScope OpenAI-compatible
  endpoint, timeout 120 s, `max_workers=1`, `max_retries=0`). Static: faithfulness 0.8918
  (n=194), response relevance 0.8542 (n=193), context precision 0.5781 (n=194). Adaptive:
  0.9069 (n=191), 0.8540 (n=189), 0.5774 (n=191). Refusals and parse-error failures are excluded;
  one static and two adaptive response-relevance scores are invalid. Paired differences over
  188-191 questions: faithfulness +0.0116 (-0.0005, 0.027), response relevance -0.0030
  (-0.0075, 0.0011), context precision -0.0025 (-0.0146, 0.0095), 2,000 resamples, seed 0.
  DashScope embeddings need `check_embedding_ctx_length=False`; the unchanged evaluator was
  called through `live-ragas-kit/run_p6_evaluation_dashscope.py`, which sets it. The repository
  was not modified.
- **Q4.6 (model/GPU record and generation timing).** Answer-only latency from `answer_s`
  (200 questions per arm, warm engine, serial): static p50/p95 10.6/23.6 s, adaptive 11.2/24.0 s,
  static-wide 10.6/22.2 s. The agent loop (`elapsed_s`) added a mean 5.6 s per adaptive question
  (p95 12.3 s). The job wall time is 2 h 23 min. These are observed serial timings, not a controlled
  throughput benchmark; model load, concurrency and cache effects are excluded.

## Method note

Counts were computed directly from the delivered JSONL records; latency percentiles use the
nearest-rank method over 200 values per arm. The report's Q4.4 prose and table now state the QA
counts and EM/F1 scores. Paired bootstrap intervals over questions or papers, and the held-out
review-file sign-off, remain to be produced.

Recheck (6 November 2026, after the live-RAGAS commit): the 200 records per arm, the
`SUFFICIENT` counts (194/191/194) and the two parse-error ids (`de830c534c…`, `cbb3c1c1e6…`)
reproduce exactly from the delivered JSONL. `answer_s` nearest-rank percentiles over all 200
records are 10.5/23.6 s (static), 11.0/24.0 s (adaptive) and 10.5/22.2 s (static-wide); the
report rounds p50 to 10.6/11.2/10.6. The p95s agree; the 0.1–0.2 s p50 difference needs the
producer's percentile convention confirmed before submission.

## Q4.3 annotator A label provenance (7 November 2026)

P5 also confirms its own part of the Q4.3 annotation record, which the 6 November approval
explicitly left out. The facts below come from the shared template and the label files on
`p3-qasper-foundation`, and from the annotator's own statement on 7 November 2026.

| | |
| --- | --- |
| Scope | annotator A, batches 01–04 |
| Questions | 80 of the 200 held-out questions |
| Labels | 747 binary labels |
| Provenance | written by the annotator from the passage text; no AI suggestion in these four batches |
| Independence | no labels or criteria exchanged with Changyan Xu before submission |
| Agreement with Xu | 739 shared pairs, 91.47%, Cohen's kappa 0.791 |
| Prior exposure | the annotator knew the 80 questions were for the final held-out evaluation; the later generation run covers all 200 |

These statements were confirmed by Junyu Hu rather than recomputed from the files: the
label counts come from `data/processed/annotation_common_v3_markdown/annotator_A/batch_01.md`
to `batch_04.md` (each headed `Annotator: HU JUNYU`), and the agreement figures from
`report/tables/agreement.tex`. The pool, the 188 disagreements, the single-reviewer
resolution and the AI-suggestion caveat for other batches are disclosed in
Section~\ref{sec:annotation} of the report and are not certified by this record.
