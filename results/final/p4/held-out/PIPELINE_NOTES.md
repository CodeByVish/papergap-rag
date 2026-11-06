# P6 pipeline outputs for held-out job 51585 (P4 runs 3 and 7)

Produced on 6 November 2026 with `scripts/run_p6_evaluation.py` (main, PR #49) from
`/Users/ananyaredhu/Documents/p4-heldout-51585-20261106.tar.gz`.

## Inputs
- Questions: `export-p3 --ref 1a1dc15b824590a39c80ea11a568fbe5814a926e` (200 ids, identical to P4's
  items file).
- Gold mapping and corpus: P3 commit `1a1dc15b` (`gold_evidence_mapping_all_splits.jsonl`, hashes
  checked against its manifest by the tool; corpus SHA-256 `8eeef011...`).
- Records: the run's `static.jsonl` and `adaptive.jsonl`. `static-wide.jsonl` (15 deep) stands in for the
  handout's `static-top10.jsonl` (`--saved-depth 15 --ks 5 8 10`).

## Role label
These were run with `--role development`, so their `run_manifest.json` says "development" although the
questions are the held-out ones. `--role held_out` needs a review file with
`usage_and_freeze_reviewed: true` (team sign-off), which nobody has given yet. The numbers do not depend on
the role; rerun with `--role held_out --review <file>` once the team signs off.

## Evidence recall (run 3)
Mapped gold recall, 200 questions: static 0.7233 / 0.8577 / 0.8972 at K = 5 / 8 / 10 (mean passages 5.0 /
7.965 / 9.87); adaptive 0.8710 (8.28 passages). Equal to P4's own scorer (`score_agent_records`).

## Performance (run 7)
- Latency = `elapsed_s + answer_s` per question. The tool counts the 2 questions per arm that the validator
  downgraded for `PARSE_ERROR` as technical errors, so n = 198 per arm (p50/p95 differ slightly from P5's
  200-question nearest-rank figures, 10.6/23.6 s for static).
- `--batch-seconds` is the runner's own wall-clock per arm from the Slurm log: static 2519 s, adaptive
  3583 s, static-wide 2456 s (sum 8558 s, equal to the manifest's started-to-finished time; the Slurm job
  took 8589 s, so about 31 s lie outside the arm timers). Concurrency 1.
- Hardware: one NVIDIA A40 (node TC2N01), vLLM 0.11.0, Qwen3-8B bfloat16, retrieval on CPU.
- Cost is null: no price was supplied (local model, no API charges).
- Tokens (generator only, from `generation.backend.last_generation_stats` in each record):
  static 934,334 in / 73,586 out; adaptive 928,803 / 74,598; static-wide 934,460 / 73,573. The critic's
  tokens were not recorded (251 critic calls, 2 escalations, in the manifest), so the adaptive arm's
  total tokens are understated. Static-wide has the same prompt size as static, which fits the
  generator rendering at most 8 passages.
