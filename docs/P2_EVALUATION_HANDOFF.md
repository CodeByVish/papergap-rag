# P2 four-system evaluation and annotation handoff

## Current boundary

Repository audit on 17 October: no agreed real relevance labels or frozen
held-out manifest were found in main, the fetched P1/P6 branches, or local
processed data. `configs/default.yaml` still has `held_out_manifest: null`;
P3-D004/D005 remain pending. P1's open #8 supplies label adapters and a proposed
contract, not real labels. Ask P3/P6 for:

1. Independently produced labels plus their hash/provenance/mapping manifest.
2. Agreed K values, binary relevance/partial-evidence rules and coverage policy.
3. Frozen held-out questions, corpus/split/configuration approval, and final
   annotation assignment order. P1's 100 training examples are a different set.

No quality result or optimal setting is claimed while these are missing.
Human judgments must be made independently; these tools do not fill labels.

## Run all four methods

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
python -m scripts.retrieval_ablation run \
  --questions PATH_TO_DEVELOPMENT_QUESTIONS.jsonl \
  --qa data/processed/qa.jsonl --passages data/processed/passages.jsonl \
  --dense-index-dir indexes/p2-qasper-development-mps \
  --candidate-ks 10 20 --rrf-ks 30 60 90 --top-k 10 \
  --local-files-only --output-dir results/ablation-new
```

Development questions must match train/validation inputs in QA exactly. Only
query ID, paper ID and question reach retrieval; answers and labels are not
passed. Each `cK-rR` subdirectory contains BM25, dense, RRF and RRF+BGE JSONL,
per-query latency and latency summaries. Raw P1 and nested P2 formats are kept.
All methods use the same question/corpus set. Hybrid reranks the complete union
before top-K. Model revisions are pinned as in P2_WEEK2.md. Persistent score
caching is disabled for timing; one warm-up per method/configuration is excluded,
and method order alternates. Descriptive p50/p95 are not a throughput guarantee.

Completed manifests record input/output/code hashes, model/runtime settings,
platform, dependencies and thread controls. Existing output paths are refused.
Failed/partial runs cannot be scored or pooled. A source snapshot/hash identifies
historical runs; they are not attributed to later code changes.

For held-out execution, pass `--role held_out --freeze-manifest freeze.json`.
The team-supplied manifest must contain `status: frozen`, nonempty `approved_by`,
matching `questions_sha256` and `corpus_sha256`, and `configuration` exactly equal
to the run's grid/model/runtime configuration. It must be supplied after actual
team agreement; do not generate an approval merely to satisfy the command.
Held-out questions must match official test. Never select settings from these
results. Freeze the development-selected configuration first.

## Score independent labels

```bash
python -m scripts.retrieval_ablation score \
  --run-dir results/ablation-new/c20-r60 \
  --passages data/processed/passages.jsonl \
  --labels PATH_TO_LABELS.jsonl --labels-manifest PATH_TO_LABELS_MANIFEST.json \
  --ks 1 3 5 10 --output results/metrics-new.json
```

Accepts P1's proposed per-question binary format:
`question_id`, `paper_id`, `status` (`mapped`/`unmapped`),
`relevance_complete` (boolean), `relevant_passage_ids`, and optional
`judged_passage_ids`. Without explicit judged IDs only the relevant IDs are
known judged. Completeness is a supplier's claim about exhaustive paper relevance,
not that all ten pooled pairs have labels. The label manifest requires
`labels_sha256`, `corpus_sha256`, `source`, `mapping`, `annotation_coverage`, and
`question_scope` with the exact `question_ids` and `project_role` (`development`
or `held_out`). Real files stay ignored under data/. P3/P6 must approve the
provisional metric conventions before final reporting.

The scorer validates identity, paper membership, passage metadata, ranks,
finite schema scores and hashes. It reports P@K (denominator K), truncated
MRR@K, binary nDCG@K and recall. Unknown returned judgments suppress full-ranking
scores. Incomplete relevance coverage is explicitly named pool recall/nDCG;
compressed judged-only rankings are separate. Missing/unmapped label rows are
exclusions; zero-known-relevant recall/nDCG are null. Macro results include the
number of contributing questions per metric. Error categories and missing known
positives support follow-up human error analysis. K cannot exceed saved depth.
Do not compare methods using different coverage/exclusion populations as if paired.

## Pool candidates and prepare human labels

```bash
python -m scripts.retrieval_ablation pool \
  --run-dir results/ablation-new/c20-r60 \
  --passages data/processed/passages.jsonl \
  --per-question 10 --output-dir results/pool-new
```

Optional `--gold` accepts an independent JSONL mapping question IDs to
`relevant_passage_ids`. It is used only after retrieval to include mapped gold
in the annotation pool, never to select retrieval inputs or tune held-out settings.
Selection includes explicit gold first, then rank round-robin across the four
methods; IDs are deduplicated. Final display order uses a deterministic hash.
Selection rules remain proposed for P3/P6 review. Shortfalls are recorded and
never padded; too many gold passages for capacity requires protocol review.

Send only `blinded.jsonl` to annotators. The separately named provenance file
contains retrieval method/scores/gold flags and must remain hidden during judging.

```bash
python -m scripts.prepare_p2_annotations \
  --pool-dir PATH_TO_FINAL_HELD_OUT_POOL \
  --assignment-manifest PATH_TO_P6_APPROVAL.json \
  --output-dir results/p2-annotation-new
```

The assignment approval must identify `approved_by`, matching `pool_sha256`,
`p2_first: [168,334]`, and `p2_second: [668,834]`, or P6's revised ranges that are disjoint within P2's own assignment.
Those proposed ranges amount to 334 independent judgments. Export requires a
complete held-out pool of 1,000 unique pairs. CSV label and note columns remain
blank; other annotators' labels and system scores are absent. Agreement and
adjudication belong to the shared P6 protocol, not invented P2 labels.

## Verification completed

Synthetic tests cover metric arithmetic, zero relevance, incomplete judgments,
blinding/deduplication/shortfalls, full four-method inference/scoring/pooling,
hash tampering, held-out freeze checks and blank annotation exports.

A real-model development smoke run uses three fixed training questions and
candidate sizes 10/20 at RRF 60, exporting top-10 for all four methods. Its
manifest is `results/p2-four-method-dev-20261017/run_manifest.json`. Pooling c20
created 30 unique pairs for three questions with no shortfalls, under
`results/p2-dev-blinded-pool-20261017/`. This is development tooling evidence,
not a final held-out pool or a labelled experiment. The real run preceded
latency-summary/error-category reporting additions; saved timing rows remain
available for descriptive summaries. Generated artifacts remain ignored.

## Annotation pairing clarification — 27 October

The execution-plan allocation is shared double annotation, not six globally
disjoint assignments. P2 labels 168–334 first and 668–834 second; P5 labels
668–834 first and 168–334 second. Both independently label the same 334 pairs.
"First" and "second" identify allocation batches, not access to earlier labels.
Each person must submit without seeing the other's decisions. The exporter’s
disjointness check only prevents P2 labeling one record twice. Its single approval
manifest identifies P2’s allocation on the common hashed pool, not the whole
team’s completed annotation or agreement. P6 must preserve both annotator IDs,
verify exactly two different annotators per record and compute pre-adjudication
agreement. Do not give all members globally disjoint records.

P5 refers to `docs/WEEK5_QUALITY.md` section 4, but that file is absent from both
current main and fetched P5 PR #15 (head `11b3639`); that PR explicitly excludes
handoff documents. Exact compatibility cannot yet be certified. P2’s scorer
accepts binary labels, distinguishes judged negatives from unjudged passages,
and does not treat incomplete pool coverage as exhaustive relevance.

Proposed rule for P3/P5/P6 review: label 1 when a passage directly supplies evidence
for at least one requested answer component, even if other components require
other passages; label 0 for merely topical mentions without answer evidence.
Partial evidence can therefore be retrieval-relevant without being sufficient
for generation. Keep uncertain cases in notes for independent adjudication; do
not turn unknown judgments into 0. This is a proposal pending comparison with
P5’s actual guideline, not a claim of team approval or a generated gold label.
