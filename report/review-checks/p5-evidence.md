# P5 report review evidence

Status: **P5 content approved by Junyu Hu on 6 November 2026; DONE FOR DRAFT - P5 scope only.**
This approval covers the items and checks listed below. It does not certify final EM/F1 or RAGAS
scores, the Qwen3-8B Hub revision, the Q4.3 annotation record, the Q5 ablations, or the team report.

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
  ids and the parser performs limited repair of malformed escapes. The 71% clipping figure is P4's
  development analysis and was not recomputed here.
- **Q4.4 (answer/refusal records).** 200 records per arm, 0 generation errors and 0 answer errors.
  `evidence_status = SUFFICIENT`: static 194, adaptive 191, static-wide 194; `INSUFFICIENT`: 6, 9, 6.
  Two records per arm were downgraded to refusal after a `PARSE_ERROR` (question ids
  `de830c534c...` and `cbb3c1c1e6...`). The scorer policy is `p6-qa-v0-proposed` in
  `src/evaluation/qa.py`; EM/F1 cannot be computed from the held-out items because they carry no
  reference answers.
- **Q4.5 (RAGAS).** `requirements-evaluation.txt` pins `ragas==0.2.15`; no live-judge run was made,
  so the RAGAS table stays reserved.
- **Q4.6 (model/GPU record and generation timing).** Answer-only latency from `answer_s`
  (200 questions per arm, warm engine, serial): static p50/p95 10.6/23.6 s, adaptive 11.2/24.0 s,
  static-wide 10.6/22.2 s. The agent loop (`elapsed_s`) added a mean 5.6 s per adaptive question
  (p95 12.3 s). The job wall time is 2 h 23 min. These are observed serial timings, not a controlled
  throughput benchmark; model load, concurrency and cache effects are excluded.

## Method note

Counts were computed directly from the delivered JSONL records; latency percentiles use the
nearest-rank method over 200 values per arm. The report's Q4.4 prose now states the counts, and the
EM/F1 table remains marked pending.
