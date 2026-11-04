# P6 evaluation handoff: inputs, commands and expected results

Updated: 5 November 2026. This is an offline evaluation package, not a new RAG implementation. Commands run from the repository root. Real data/results stay ignored and local. Schemas and project split mappings remain `v0-proposed`.

## 1. What each person supplies

| Person | Supply to P6 |
| --- | --- |
| P3 | Pinned annotation/pool commit, exact full corpus, reference QA export, corpus/usage provenance |
| Annotators | Confirmation of identities/independence and explanation of revised submissions |
| Adjudicators | Third-person decisions for disagreements, with reasons |
| P1/P2 | Saved rankings/configurations; P3 already preserves four-method top-five rankings |
| P4/P5 | Real output records, exact model/prompt/configuration, original retrieval input, contexts and timings |
| Team | Final-question eligibility/freeze decision, named batch operator, judge access/budget |
| P6 | Validated gold, scoring commands, QA/RAGAS/performance/comparison tables and instructions |

**Example:** owners run static and adaptive RAG → save answers/contexts/timings → P6 joins references offline → P6 exports comparison tables → owners review report claims.

## 2. Setup and a safe first run

Use the existing project environment. Nothing below loads a model unless `ragas --live` is supplied. Core scoring needs Python 3.10+ and Pydantic 2 (already in the project requirements).

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
export P6_PY="$PWD/.venv-p6/bin/python"
"$P6_PY" -m scripts.run_p6_evaluation --help
```

On another machine replace the `cd` path and set `P6_PY` to that environment's Python. From a clean environment install the project's `requirements-dev.txt` using `python -m pip install -r requirements-dev.txt`; a full project install can be larger than the offline scorer needs.

Run the included **synthetic** example first. Choose a fresh output name each time; commands refuse to overwrite existing directories.

```bash
"$P6_PY" -m scripts.run_p6_evaluation qa \
  --questions tests/fixtures/p6/questions.jsonl \
  --predictions tests/fixtures/p6/static.jsonl \
  --references tests/fixtures/p6/references.jsonl \
  --arm static --role development \
  --output results/p6/example-static-qa

"$P6_PY" -m scripts.run_p6_evaluation qa \
  --questions tests/fixtures/p6/questions.jsonl \
  --predictions tests/fixtures/p6/adaptive.jsonl \
  --references tests/fixtures/p6/references.jsonl \
  --arm adaptive --role development \
  --output results/p6/example-adaptive-qa
```

Expect `qa.csv`, `scores.jsonl`, `summary.json`, `run_manifest.json`. Synthetic static answerable F1=.8; adaptive F1=1. Both refuse the synthetic unanswerable question correctly. These numbers are not project findings.

## 3. Audit P3 labels and export the frozen inputs

No checkout or automatic fetch is performed. Fetch the P3 ref separately if the team says it needs refreshing; then pin the reviewed commit. The following is the inspected snapshot, not a permanent latest-commit assertion.

```bash
export P3_COMMIT=1a1dc15b824590a39c80ea11a568fbe5814a926e

"$P6_PY" -m scripts.run_p6_evaluation audit-labels \
  --ref "$P3_COMMIT" --output results/p6/annotation-audit

"$P6_PY" -m scripts.run_p6_evaluation export-p3 \
  --ref "$P3_COMMIT" --output results/p6/p3-frozen-inputs
```

Audit outputs: `agreement.json`, `agreement_by_pair.csv`, `adjudication.csv`, provenance manifest. It validates submitted sheet bodies against original templates recovered from local Git history, pool hashes, identities and record alignment. An incomplete history or missing labels stops execution; fetch the required history or obtain completed submissions rather than editing source records to pass checks.

At this commit expect 1,853 pairs, 200 questions, 89.854% raw agreement and 188 disagreements. Different revisions may differ. A/B slots are not necessarily the same two humans; inspect per-human-pair results. Method membership was disclosed on the sheets. Distinct names cannot establish independence; review that with humans, including changes from older submissions.

The export command creates `questions.jsonl`, `pairs.jsonl`, `rankings.jsonl`, `manifest.json`, `frozen_config.json` and its own run manifest. It exports existing records; it runs no retrieval model. The paired pool includes official validation and test origins; directory names do not establish final held-out eligibility.

## 4. Human adjudication and final gold

A third person who is neither original annotator fills the existing `adjudication.csv` columns:

- `adjudicator`: real name/agreed identity.
- `final_label`: exactly 0 or 1.
- `reason`: reason for the decision.

Keep all other columns unchanged. Preserve initial labels and agreement. Do not replace initial judgments with final labels to increase agreement.

Create local `results/p6/annotation-review.json` after actual review. This is a **template**, not approval. Replace nulls with true only when humans confirm them, set the supported project role, and write a real note. Do not choose `development` merely to bypass held-out controls.

```json
{
  "source_commit": "1a1dc15b824590a39c80ea11a568fbe5814a926e",
  "independence_confirmed": null,
  "usage_and_freeze_reviewed": null,
  "project_role": null,
  "review_note": ""
}
```

Set `P6_CORPUS` to the exact P3 corpus used for the frozen pool, not another chunk-size variant. The exporter checks passage IDs, paper IDs and full pooled passage text against this file.

```bash
export P6_CORPUS="$PWD/data/processed/passages.jsonl"

"$P6_PY" -m scripts.run_p6_evaluation finalize-labels \
  --ref "$P3_COMMIT" \
  --adjudication results/p6/annotation-audit/adjudication.csv \
  --review results/p6/annotation-review.json \
  --corpus "$P6_CORPUS" \
  --output results/p6/final-gold
```

Expect `final_labels.jsonl`, `final_labels_manifest.json`, `original_and_final_judgments.jsonl`, `agreement.json` and run manifest. The new label manifest has a real corpus hash and `annotation_coverage: "complete"`. This means the selected pool is labeled; `relevance_complete: false` means it is not exhaustive paper relevance. The older annotation notebook's draft manifest is not a substitute for this completed contract.

Example final label row (synthetic IDs):

```json
{"question_id":"q1","paper_id":"paper1","status":"mapped","relevance_complete":false,"relevant_passage_ids":["p3"],"judged_passage_ids":["p3","p8"]}
```

## 5. Score saved retrieval

Gold must be finalized first. If the reviewed project role is `held_out`, additionally create `results/p6/final-evaluation-review.json`:

```json
{
  "usage_and_freeze_reviewed": null,
  "review_note": "",
  "question_ids": []
}
```

You can populate the ID list without inventing approval using this local helper:

```bash
"$P6_PY" - <<'PYCODE'
import json
from pathlib import Path
questions = [json.loads(line) for line in Path('results/p6/p3-frozen-inputs/questions.jsonl').read_text().splitlines() if line]
path = Path('results/p6/final-evaluation-review.json')
with path.open('x') as f:
    json.dump({'usage_and_freeze_reviewed': None, 'review_note': '',
               'question_ids': [q['question_id'] for q in questions]}, f, indent=2)
PYCODE
```

Populate the remaining review fields only after actual review. The CLI checks the flag, note and exact scope; it cannot establish that human approval or independence really occurred. Record the frozen model/prompts/index/settings and named operator in the team's real freeze record and reference it in the note.

For a genuinely approved held-out pool:

```bash
"$P6_PY" -m scripts.run_p6_evaluation retrieval \
  --questions results/p6/p3-frozen-inputs/questions.jsonl \
  --pairs results/p6/p3-frozen-inputs/pairs.jsonl \
  --rankings results/p6/p3-frozen-inputs/rankings.jsonl \
  --labels results/p6/final-gold/final_labels.jsonl \
  --labels-manifest results/p6/final-gold/final_labels_manifest.json \
  --corpus "$P6_CORPUS" --ks 1 3 5 \
  --role held_out --review results/p6/final-evaluation-review.json \
  --output results/p6/retrieval-final
```

For a genuinely development-only pool use `--role development` and omit `--review`. The role must match the label manifest. This command expects the full pinned P3 pool/ranking files, not manually filtered subsets. Report subset studies separately under an owner-reviewed adapter.

Expect four-method `retrieval.csv`, per-question `scores.jsonl`, summary and manifest. Saved ranks/scores are verified against the original pool's byte hashes. No model rerun is required. Requesting K above saved depth fails. Recall and nDCG are pool-relative; unknown passages are not negatives. This adapter requires full judgment coverage of the frozen pool rather than guessing missing labels.

## 6. Score real QA answers

**Question file:** one row per selected question, with nonempty `question_id`, `paper_id`, `question`.

**Prediction file:** either P4's agent output with nested `answer.result`, P5's wire envelope with an explicit `question_id`, or normalized rows:

```json
{"question_id":"q1","paper_id":"paper1","prediction":"BERT base model","status":"answered"}
```

Status must be `answered`, `refused` or `error`. P5 canonical refusals and validation generation/parse errors are distinguished automatically. P4 exceptions (`error`/`answer_error`) are technical failures. If a P5 file only has `request_id`, map it to `question_id` using a verified owner-supplied mapping; never join by row number or guess ID equivalence.

**Reference file:** original exported QASPER `qa.jsonl` with `answers`, or normalized rows:

```json
{"question_id":"q1","paper_id":"paper1","references":["BERT base model","BERT-base"],"unanswerable":false}
```

For unanswerable questions use `references: []` and `unanswerable: true`. QASPER yes/no is rendered as yes/no, extractive spans are joined in source order, and answerable references take precedence over mixed unanswerable annotations. Normalization, best-reference EM/F1, abstention and failure handling are documented in the metric reference. This is a proposed project score, not an assertion of official QASPER compatibility.

Set paths to actual files, then run:

```bash
export P6_QUESTIONS="$PWD/results/p6/p3-frozen-inputs/questions.jsonl"
export P6_REFERENCES="$PWD/data/processed/qa.jsonl"
export P6_PREDICTIONS="$PWD/results/p4-final/static.jsonl"

"$P6_PY" -m scripts.run_p6_evaluation qa \
  --questions "$P6_QUESTIONS" --predictions "$P6_PREDICTIONS" \
  --references "$P6_REFERENCES" --arm static \
  --role held_out --review results/p6/final-evaluation-review.json \
  --output results/p6/static-qa-final
```

Repeat with the adaptive output and `--arm adaptive`, using a new directory. Missing predictions count as failures and zero task score when reference is valid; invalid/missing references are excluded with counts. Report answerable EM/F1 separately from unanswerable correctness. `combined_task_score` averages answerable F1 and unanswerable correctness over eligible questions; label it explicitly.

This command scores saved outputs only. To generate development outputs use the existing `scripts/run_agent_experiment.py` and `docs/P4_AGENT.md`. That runner refuses official test queries; do not bypass its guard through `--items`. Final inference remains a named-owner task with a reviewed entry point. Never send full QA reference rows to the model.

## 7. Obtain exact answer context

Preferred: P4/P5 supply an exact rendered-context export:

```json
{"question_id":"q1","paper_id":"paper1","exact_rendered":true,"contexts":["[1] passage_id: p3\n    text: The experiment used BERT."],"provenance":{"run":"actual run identifier","method":"captured from the answer prompt"}}
```

Contexts are ordered strings exactly representing the evidence shown to the answer generator, after selection/truncation. The marker and provenance are human/producer assertions; verify them against the real run. All retrieved passages or critic-read logs are insufficient.

If you have original agent records and the exact original P5 `PromptConfig`, reconstruction is available. Save that reviewed configuration as local `results/p6/prompt-config.json`. Do not silently substitute current defaults. Ask P5 for all settings (`max_passages`, `max_chars_per_passage`, `show_scores`, `include_examples`, `use_evidence_map`) and version.

```bash
"$P6_PY" -m scripts.run_p6_evaluation contexts \
  --predictions "$P6_PREDICTIONS" \
  --prompt-config results/p6/prompt-config.json \
  --expect-prompt-version p5-grounded-qa-v7 \
  --review-note 'Replace with the actual owner review and original run/config reference' \
  --output results/p6/static-contexts
```

This uses the checked-out P5 adapter, selector and renderer, rejects dropped passages and mismatched/missing saved prompt version, and emits `contexts.jsonl`. The example version must match the real run. Matching a version string cannot prove other source code was unchanged; compare original source hashes/commit before approving reconstruction. Errors/refusals need no context scoring row.

## 8. Validate and run RAGAS

First run validation on synthetic inputs. No judge calls or API credentials are needed:

```bash
"$P6_PY" -m scripts.run_p6_evaluation ragas \
  --questions tests/fixtures/p6/questions.jsonl \
  --predictions tests/fixtures/p6/static.jsonl \
  --references tests/fixtures/p6/references.jsonl \
  --contexts tests/fixtures/p6/contexts.jsonl \
  --arm static --role development \
  --output results/p6/example-ragas-validation
```

Expect null scores and `ready_not_scored` for eligible metrics; refusals are marked separately. This verifies preparation, not judge quality. Always validate real inputs the same way before a paid run.

Live scoring has optional dependencies. Use a separate Python 3.11/3.12 environment, not the school vLLM environment:

```bash
python3.12 -m venv .venv-p6-judge
.venv-p6-judge/bin/python -m pip install -r requirements-evaluation.txt
.venv-p6-judge/bin/python -m pip freeze > results/p6/judge-dependencies.txt
```

`ragas==0.2.15` is pinned to a documented API. Other dependency ranges need the resolved snapshot above. The adapter uses an OpenAI-compatible chat and embedding endpoint via LangChain. Use a backend supporting both or extend the adapter under review. A local generator service is not automatically a suitable judge/embedding backend.

Create local `results/p6/judge-config.json` with approved actual values:

```json
{
  "judge_model": "REPLACE_WITH_APPROVED_MODEL",
  "judge_revision": "REPLACE_WITH_PROVIDER_REVISION_OR_VERSION_NOTE",
  "embedding_model": "REPLACE_WITH_APPROVED_EMBEDDING_MODEL",
  "embedding_revision": "REPLACE_WITH_PROVIDER_REVISION_OR_VERSION_NOTE",
  "api_key_env": "P6_JUDGE_API_KEY",
  "timeout_seconds": 120
}
```

An optional `base_url` selects an approved compatible endpoint. No API key belongs in this JSON, notebook, command history or Git. Set `P6_JUDGE_API_KEY` through your existing secure environment mechanism. The revision strings are provenance notes; the actual model ID determines the provider request. Record any provider version limitations honestly.

First use a small, separately prepared **development-only** question/prediction/context set and `--role development`. For the approved final run:

```bash
.venv-p6-judge/bin/python -m scripts.run_p6_evaluation ragas \
  --questions "$P6_QUESTIONS" --predictions "$P6_PREDICTIONS" \
  --references "$P6_REFERENCES" \
  --contexts results/p6/static-contexts/contexts.jsonl \
  --arm static --role held_out --review results/p6/final-evaluation-review.json \
  --live --judge-config results/p6/judge-config.json \
  --cache results/p6/judge-cache \
  --output results/p6/static-ragas-final
```

Expect `ragas.csv`, per-question scores/statuses, summary, configuration and local sensitive `judge_trace.json`. Cache identity includes input, metric prompts/parameters, package version and judge configuration. Calls are sequential with explicit timeouts and no automatic API retries; failed metrics have statuses and can be rerun to a new output directory while reusing successful cached scores. Trace contains new calls only, not cached calls. Provider-supplied token usage may be available in the trace; embedding usage may not be. Do not infer a complete cost ledger when usage is absent.

Metrics: faithfulness, response relevance and **reference-based** context precision. The first valid reference in stable source order is used for context precision; QA uses best reference independently. Scores can be undefined for refusal/empty context/missing reference/judge failure. Read valid counts and status breakdowns, not just means. No overall RAGAS composite is invented.

The live backend has not been verified against a real judge in this implementation session; it requires installed optional packages, approved credentials and a development smoke test. Source: [RAGAS 0.2.15 evaluation API](https://docs.ragas.io/en/v0.2.15/getstarted/evals/).

## 9. Performance and cost

Run the reproducible synthetic example:

```bash
"$P6_PY" -m scripts.run_p6_evaluation performance \
  --predictions tests/fixtures/p6/static.jsonl --arm static \
  --latency-field client_elapsed_s --batch-seconds 6.5 \
  --hardware synthetic-example --concurrency 1 --cache-policy no-result-cache \
  --usage tests/fixtures/p6/usage.jsonl --pricing tests/fixtures/p6/pricing.json \
  --output results/p6/example-performance
```

For actual agent output use `--latency-field internal_pipeline_s`: the scorer adds `elapsed_s` and `answer_s` only where both exist. This is not HTTP latency. To report HTTP/UI speed, record `client_elapsed_s` from request dispatch to complete response. Timeouts/errors remain explicit outcomes. Report cold-start separately; fix warm-up, concurrency, hardware and cache policy before comparisons.

`--batch-seconds` is the measured wall-clock interval for exactly these records under the stated concurrency. Omit it if unavailable: throughput is null. Never substitute the sum of overlapping request times. Failures are counted separately; latency percentiles include non-error timed outcomes (including valid refusals), with sample counts. Technical-error timing is not summarized as successful response latency.

Optional usage JSONL is one row per actual call:

```json
{"component":"generator","model":"actual-model","input_tokens":1000,"output_tokens":100}
```

Use separate components for critic/judge/embedding. Pricing JSON is keyed by model, with `input_per_million`, `output_per_million`, `currency`, `date`, `source`. Unknown prices yield null cost. Local models need GPU-hours/allocation notes separately; no price is invented. Synthetic fixture prices are teaching examples only.

## 10. Matched comparisons and report handoff

Compare the two synthetic QA runs from section 2:

```bash
"$P6_PY" -m scripts.run_p6_evaluation compare \
  --left results/p6/example-static-qa/scores.jsonl \
  --right results/p6/example-adaptive-qa/scores.jsonl \
  --metrics f1 task_score --resamples 1000 --seed 42 \
  --output results/p6/example-comparison
```

Expect `ablation.csv`, summary and provenance. Differences are **right minus left** on matched finite per-question values. Bootstrap samples papers and retains their questions. Unmatched questions and valid-pair counts are reported. QA F1 excludes unanswerable rows; task score includes their correctness. For RAGAS first inspect different refusal/error/valid-score coverage; common eligible rows can be selective. For retrieval, pass the same retrieval `scores.jsonl` to both sides and add `--left-arm <method A> --right-arm <method B> --k 5`. The tool rejects ambiguous multi-arm/multi-K rows instead of comparing by position.

For final comparisons keep generator/prompt/questions/corpus/search scope/answer context budget/validation fixed and record additional calls. Static vs adaptive assesses the combined adaptive module. Separate reranking and rewriting claims require neither/reranking-only/rewriting-only/both configurations. Include larger-depth static controls to examine gains from merely reading more passages. Five UI examples satisfy a demonstration need but cannot establish stable p95.

Share these report artifacts through the team's approved external location, with access checked:

| Output | Report use |
| --- | --- |
| Initial agreement and human-pair statistics | Q4.3 |
| `retrieval.csv` and pool/coverage limitations | Q3 |
| `qa.csv`, reference policy, abstention/errors | Q4.4 |
| `ragas.csv`, judge configuration, valid counts | Q4.5 |
| `performance.csv`, usage/cost and timing policy | Q2.2/Q4.6 |
| `ablation.csv` plus controlled configuration description | Q5 |
| Per-question scores, hashes, commands and dependency snapshots | Reproducibility archive |

Do not commit real labels, model outputs, raw judge traces, credentials, corpus or indexes. Commands do not submit a report, push changes or publish results. Final numbers require the real human/runtime inputs above.

## 11. Troubleshooting and validation

- **Output already exists:** choose a new output directory; keep previous evidence.
- **Corpus/hash mismatch:** get the exact original corpus/files. Do not edit hashes to force acceptance.
- **Missing identities/labels/template history:** resolve the source with P3/annotators.
- **Review/adjudication rejected:** complete actual reviews and third-party decisions; placeholders intentionally fail.
- **QA file has request_id only:** obtain a verified question-ID mapping from the producer.
- **RAGAS missing context:** export or reconstruct the actual answer evidence, not critic context.
- **Null throughput/cost:** supply measured batch wall time/real usage and prices; null is preferable to invented values.
- **Live dependency/backend error:** use the separate judge environment and inspect configuration; deterministic scoring needs no judge.

Run verification:

```bash
"$P6_PY" -m pytest tests/test_p6_evaluation.py tests/test_p1_evaluation.py tests/test_p2_evaluation.py -q
```

The walkthrough notebook provides worked explanations and runs the synthetic examples without a judge. Reusable scoring logic lives in `src/evaluation/`, not duplicated notebook functions.

## Implementation verification on 5 November 2026

- 87 tests passed across the new P6 suite, existing P1/P2 evaluation, agent experiment runner and generation Week 6 tests.
- All five walkthrough code cells executed successfully; the saved notebook contains no executed outputs.
- Ruff checks passed on the new Python files; document links and whitespace were checked.
- The real pinned P3 annotation audit and frozen-input export completed locally. Outputs are ignored under `results/p6/annotation-audit-verified-20261105/` and `results/p6/p3-snapshot-20261105/`.
- No human adjudication, final gold export, real final QA/RAGAS scores or live judge validation is claimed. Those require the human/runtime inputs listed above.

## 12. Mapped-passage recall for static@5/@8/@10 and adaptive

The `evidence` command is separate from `retrieval`: it scores against P3's evidence mapping, not adjudicated pool relevance. It accepts the original P4 agent record (`retrieval_log`), contiguous ranked `hits`, or an explicit ordered `retrieved_passage_ids` array. Each row must have `question_id`. It checks the mapping manifest's gold/corpus hashes and all selected gold/retrieved IDs against the same-paper corpus.

Static scoring uses the saved original ranking at each requested K. Declare `--saved-depth` from the actual run configuration; it must cover all requested cutoffs. A top-five export cannot establish top-eight or top-ten results. Adaptive scoring takes the unique union of `passage_ids` across all logged rounds, matching P4's cumulative recall definition; repeated IDs across rounds count once. This is retrieval-pool recall over mapped gold IDs, not answer-visible evidence recall. `mapped_recall_first_round` is also saved for diagnosis.

Example using separately generated static top-ten and adaptive outputs:

```bash
export P6_MAPPING="$PWD/data/processed/gold_evidence_mapping_all_splits.jsonl"
export P6_MAPPING_MANIFEST="$PWD/data/processed/gold_evidence_mapping_all_splits.manifest.json"

"$P6_PY" -m scripts.run_p6_evaluation evidence \
  --questions "$P6_QUESTIONS" --records results/p4-final/static-top10.jsonl \
  --gold "$P6_MAPPING" --gold-manifest "$P6_MAPPING_MANIFEST" --corpus "$P6_CORPUS" \
  --mode static --arm static --saved-depth 10 --ks 5 8 10 \
  --role held_out --review results/p6/final-evaluation-review.json \
  --output results/p6/static-evidence

"$P6_PY" -m scripts.run_p6_evaluation evidence \
  --questions "$P6_QUESTIONS" --records results/p4-final/adaptive.jsonl \
  --gold "$P6_MAPPING" --gold-manifest "$P6_MAPPING_MANIFEST" --corpus "$P6_CORPUS" \
  --mode adaptive --arm adaptive \
  --role held_out --review results/p6/final-evaluation-review.json \
  --output results/p6/adaptive-evidence

"$P6_PY" -m scripts.run_p6_evaluation compare \
  --left results/p6/static-evidence/scores.jsonl --left-k 5 \
  --right results/p6/adaptive-evidence/scores.jsonl \
  --metrics mapped_recall --resamples 1000 --seed 42 \
  --output results/p6/adaptive-vs-static5-evidence
```

Repeat comparison with `--left-k 8` or `10` and a new output directory. For development use `--role development`, omit the review, and supply genuinely development-only assets. Mapping/gold is opened for scoring only after final inference; do not give these rows to the model. The scorer reads P3's original mapping schema directly. A normalized gold file requires a corresponding truthful mapping/corpus manifest; never reuse hashes for different bytes.

Outputs: `evidence_recall.csv`, per-question `scores.jsonl`, `summary.json`, run manifest. Missing/empty mappings are excluded, not inferred unanswerable. Missing retrieval records and retrieval errors earn zero in the primary failure-inclusive mean when gold exists. A second `successful_only_mapped_recall` and sample count matches P4's successful-run denominator. Generation-only errors do not erase successful retrieval. For exact P4 comparison select the successful-only metric and same question population; report failure counts too. `answerable` is read from an explicit boolean or derived from P3's source annotations (any answerable annotation means answerable); it is otherwise null, never inferred from mapping size.

A saved top-ten ranking can supply retrieval recall@5/@8/@10 if it is the same one-round retrieval policy with a different output truncation. It cannot supply QA/RAGAS answers for all three context depths. Those require three generation runs or correctly captured per-depth answers/contexts. For adaptive comparisons also report actual context/token/call budgets and a larger static-depth control. This scorer is paper-scoped; corpus-wide recall needs its own reviewed relevance universe.

For final-set choice and exact freeze-manifest steps, use [held-out coordination](HELD_OUT_COORDINATION.md).
