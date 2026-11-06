# P2 approved-label retrieval results

Scored using evaluation code at `ceeaca8` and the exact P3-confirmed PR #50
label commit `f70bf95593a6b9f705674770b8c3e833ca76290c`. P3 confirmation was
provided by Vishakha in the project conversation; the review files at that commit
retain their original assumption wording. PR #50 was open at execution time.
Frozen pool/rankings source: `1a1dc15b824590a39c80ea11a568fbe5814a926e`.
Corpus SHA-256: `8eeef0119e322fc9253255e2c6db6cb38ec276d7ebf3669dd28a856a636aa93e`.
All input hash, scope and corpus-text checks in P6's scorer passed.

200 questions from 174 papers; 1,853 judged pairs, 820 relevant pairs.
Every returned passage is judged. Precision and MRR average over 200 questions;
pool recall and pool nDCG average over 199, excluding the one question with no
positive pool label. Recall and nDCG are relative to the judged union of saved
rankings, not exhaustive full-paper relevance. All metrics below are proportions.

| Method | K | Precision | Pool recall | MRR | Pool nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| BM25 | 1 | 0.6000 | 0.1822 | 0.6000 | 0.6030 |
| BM25 | 3 | 0.5317 | 0.4336 | 0.7183 | 0.6010 |
| BM25 | 5 | 0.4820 | 0.6067 | 0.7296 | 0.6355 |
| Dense | 1 | 0.6850 | 0.2281 | 0.6850 | 0.6884 |
| Dense | 3 | 0.5767 | 0.4726 | 0.7842 | 0.6681 |
| Dense | 5 | 0.5270 | 0.6976 | 0.7992 | 0.7188 |
| Hybrid RRF | 1 | 0.7000 | 0.2176 | 0.7000 | 0.7035 |
| Hybrid RRF | 3 | 0.5933 | 0.4915 | 0.7908 | 0.6833 |
| Hybrid RRF | 5 | 0.5390 | 0.7137 | 0.8043 | 0.7313 |
| Hybrid RRF followed by BGE reranking | 1 | 0.5950 | 0.1748 | 0.5950 | 0.5980 |
| Hybrid RRF followed by BGE reranking | 3 | 0.5400 | 0.4234 | 0.6900 | 0.6031 |
| Hybrid RRF followed by BGE reranking | 5 | 0.5090 | 0.6587 | 0.7175 | 0.6632 |

## Paired comparisons at K=5

Differences are right minus left on the same questions. Intervals are 95%
paper-cluster bootstrap intervals (1,000 resamples, seed 42). They describe
sampling uncertainty conditional on these labels, not annotation bias.

| Comparison | Metric | Difference | 95% interval |
| --- | --- | ---: | --- |
| dense-vs-bm25 | precision_at_k | +0.0450 | [+0.0171, +0.0728] |
| dense-vs-bm25 | pool_recall_at_k | +0.0909 | [+0.0419, +0.1421] |
| dense-vs-bm25 | mrr_at_k | +0.0696 | [+0.0168, +0.1222] |
| dense-vs-bm25 | pool_ndcg_at_k | +0.0833 | [+0.0366, +0.1314] |
| rrf-vs-bm25 | precision_at_k | +0.0570 | [+0.0354, +0.0788] |
| rrf-vs-bm25 | pool_recall_at_k | +0.1070 | [+0.0663, +0.1471] |
| rrf-vs-bm25 | mrr_at_k | +0.0747 | [+0.0398, +0.1112] |
| rrf-vs-bm25 | pool_ndcg_at_k | +0.0958 | [+0.0640, +0.1273] |
| rrf-vs-dense | precision_at_k | +0.0120 | [-0.0063, +0.0318] |
| rrf-vs-dense | pool_recall_at_k | +0.0161 | [-0.0139, +0.0462] |
| rrf-vs-dense | mrr_at_k | +0.0052 | [-0.0330, +0.0434] |
| rrf-vs-dense | pool_ndcg_at_k | +0.0125 | [-0.0154, +0.0409] |
| bge-vs-rrf | precision_at_k | -0.0300 | [-0.0555, -0.0051] |
| bge-vs-rrf | pool_recall_at_k | -0.0550 | [-0.1037, -0.0098] |
| bge-vs-rrf | mrr_at_k | -0.0868 | [-0.1377, -0.0350] |
| bge-vs-rrf | pool_ndcg_at_k | -0.0682 | [-0.1123, -0.0256] |

RRF leads all four metrics at K=1, 3 and 5. At K=5, adding BGE changes
precision by -3.00 percentage points, pool recall by -5.50 points, MRR by
-0.0868 and pool nDCG by -0.0682. These results support retaining BGE as an
ablation rather than claiming it improved this dataset. The earlier development
choice of RRF-only top-8 remains separate: this saved top-five pool cannot
establish top-eight metrics, and these scores must not be used to retune it.
No models were rerun and no new latency or generation-quality result is claimed.

## Label limitations to retain in the report

Method identities were visible during annotation. A08–10 originated as Codex
suggestions subsequently confirmed by P2. The final manifest discloses that
Changyan resolved 188 disagreements, had annotated 73 of those pairs, and
confirmed 66 AI-prefilled labels unchanged without written notes. Resolution
sources are 102 human_reviewed and 86 human_spot_checked; most records have no
written reason. This is disclosed resolution, not independent third-person
adjudication. Agreement of 89.85% describes the specified revised source files;
it must not replace the original pre-review agreement or imply unaided labels.

## Reproduction

Extract `questions.jsonl`, `pairs.jsonl`, `rankings.jsonl` from
`1a1dc15b:data/processed/annotation_common_v3/` and the three label/review files
from `f70bf95:data/gold/p6/final/` into `results/p2-final-retrieval/inputs/`.
Use the corpus whose hash is recorded above. With `INPUT` and `CORPUS` set:

```sh
python -m scripts.run_p6_evaluation retrieval \
  --questions "$INPUT/questions.jsonl" --pairs "$INPUT/pairs.jsonl" \
  --rankings "$INPUT/rankings.jsonl" --labels "$INPUT/final_labels.jsonl" \
  --labels-manifest "$INPUT/final_labels_manifest.json" --corpus "$CORPUS" \
  --ks 1 3 5 --role held_out --review "$INPUT/retrieval-review.json" \
  --output results/p2-retrieval-reproduction
```

Use the `compare` subcommand on the resulting `scores.jsonl` with `--k 5`,
`--left-arm` and `--right-arm`, metrics `precision_at_k pool_recall_at_k mrr_at_k
pool_ndcg_at_k`, `--resamples 1000 --seed 42`. Each output directory must be new.
The local handoff ZIP contains all CSVs, per-question scores, run manifests,
checksums and exact input label/pool snapshots. It excludes corpus/model files.
