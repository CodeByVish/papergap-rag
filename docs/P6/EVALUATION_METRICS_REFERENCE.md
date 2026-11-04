# Evaluation metric reference

Companion to [the execution plan](EVALUATION_EXECUTION_PLAN.md). These are proposed scoring policies; confirm them before final evaluation. Shared schemas and split mappings remain `v0-proposed`.

## 4. Metric definitions and calculation

### 4.1 Retrieval: Q3

For question q, let R be the set of known relevant passage IDs in the declared evaluation universe, L the unique ranked IDs, and r_i the binary relevance of rank i. Validate duplicate IDs as errors rather than silently changing ranks. Proposed primary cutoff: K=5 to match the reported native top-five pool. Use K=1 and 3 as secondary measures; K=10 requires saved depth and adequate judgments. Freeze these choices before final scoring.

| Metric | Per-question calculation | Meaning |
| --- | --- | --- |
| Precision@K | sum(r_i, i=1..K) / K | Relevant hits among K requested positions |
| Recall@K | number of relevant IDs in top K / size(R) | Fraction of declared relevant set recovered |
| MRR@K | 1 / first relevant rank within K; otherwise 0 | How early the first useful passage occurs |
| DCG@K | sum(r_i / log2(i+1), i=1..K) | Relevance weighted toward early ranks |
| nDCG@K | DCG@K / ideal DCG@K | Ranking quality relative to an ideal ranking |
| Judged coverage@K | judged returned hits / returned hits, up to K | Fraction of actual retrieved hits with judgments |

For binary labels, ideal DCG sums 1/log2(i+1) through min(K, size(R)). Average each metric over eligible questions, not over pairs. Report each metric's denominator and exclusions. A short ranking still has Precision@K denominator K; missing positions earn no relevance credit. Report returned depth separately. Empty rankings have coverage undefined, not perfect coverage.

**Example:** K=3, ranking [A,B,C], relevant set {A,C,D}: Precision=2/3, Recall=2/3, MRR=1, DCG=1+1/log2(4)=1.5, ideal DCG=1+1/log2(3)+1/log2(4)=2.13093; nDCG≈0.704.

**Incomplete labels:** unjudged hits are unknown. Suppress original-ranking quality scores at a cutoff containing unknown hits; report coverage. A separate judged-only compressed ranking can be reported with its changed task clearly labeled. Recall against the common pool is **pool-relative recall**, not exhaustive paper/corpus recall. Even fully judged returned top K does not prove complete relevance coverage for recall or ideal-ranking denominators. With no relevant labeled passages, report recall/nDCG undefined; report precision and MRR only if judgments support them. Mapping failures and missing labels are exclusions with counts, not negatives. P3 owns evidence-to-passage mapping; score evidence recall separately and document duplicate/overlap treatment.

Reuse `src/evaluation/retrieval.py` and `scripts/retrieval_ablation.py` where compatible. Their contracts require explicit completeness declarations. The current evaluator validates paper-scoped labels; corpus-wide evaluation needs owner-reviewed changes and its own relevance universe. Do not silently apply paper-scoped gold to corpus search.

### 4.2 Annotation agreement: Q4.3

Join independent judgments by canonical (question_id, passage_id). Require valid 0/1 labels, two distinct identified humans per record, no duplicate assignments and preserved originals. Missing judgments prevent a complete-dataset agreement claim. A provisional complete-case result must disclose missing counts.

- Raw agreement = number of pairs with equal initial labels / number of doubly labeled pairs.
- For a fixed human pair, observed agreement p_o is raw agreement. If A's positive rate is p_A and B's is p_B, expected agreement p_e = p_A*p_B + (1-p_A)*(1-p_B).
- Cohen's kappa = (p_o-p_e)/(1-p_e). If p_e=1, kappa is undefined.

Example: 90/100 labels agree; both humans mark 50% positive. p_o=.90, p_e=.50, kappa=.80. The rubric's 80% threshold concerns raw agreement, not kappa=.80.

Report overall raw agreement and agreement/kappa per actual fixed human pair with sample sizes and class counts. A/B spreadsheet slots do not establish fixed human identities. Compute agreement before a third person adjudicates disagreements. Preserve disagreement records. If agreement falls below 80%, document it and any guideline clarification/fresh independent labeling; never replace initial labels with adjudicated labels to claim independent agreement.

### 4.3 QA quality: Q4.4

Proposed deterministic normalization: lowercase, remove ASCII punctuation, remove English articles a/an/the, collapse whitespace. Pin implementation and examples; do not remove numbers, units or negation. Freeze how QASPER extractive spans are joined and how free-form, yes/no and unanswerable references are rendered with P3/P5.

- **Exact Match:** 1 if normalized prediction equals a valid normalized reference; otherwise 0.
- **Token F1:** use multiset token overlap c; precision=c/prediction_token_count and recall=c/reference_token_count; F1=2PR/(P+R). No overlap gives 0. Two empty normalized strings score 1; only one empty scores 0. References must first pass validation so missing annotations are not rewarded as empty answers.
- **Multiple references:** take maximum EM and maximum F1 over valid references separately, then macro-average by question. Preserve references individually, rather than concatenating different annotators' answers.
- **ROUGE-L, secondary:** with token longest common subsequence length l, P=l/prediction_length, R=l/reference_length and F1=2PR/(P+R). Pin tokenizer, stemming and multi-reference handling; use max reference F1 under this proposal. This is lexical overlap, not factual correctness. BERTScore is optional, not needed alongside every alternative metric in the handout.

Example: prediction “BERT model”, reference “BERT base model”: overlap=2, P=1, R=2/3, token F1=.8; EM=0.

Use structured abstention status, not substring matching of refusal prose. Proposed policy: on gold-unanswerable questions, abstention scores 1 and an attempted answer 0 in an explicitly named unanswerable correctness score. On answerable questions, abstention scores 0 for QA. Report answerable EM/F1 and unanswerable correctness separately; a combined task score must state its composition and is not an official QASPER score without compatibility verification. Keep technical failure distinct from abstention. Report failure rate; include failures as zero in a primary all-eligible-question QA summary and show completed-only scores separately. Report answer coverage and quality among answered questions so refusal cannot inflate quality invisibly.

### 4.4 Answer-level RAG evaluation: Q4.5

RAGAS is a library implementing metrics, not one aggregate score. Pin the installed version, metric class/API, judge and embedding revisions, prompts, decoding, seed where supported and timeout policy. Backend access is currently unresolved; do not assume a hosted budget. A separate capable judge is preferable; if the generator also judges its answers, disclose that limitation and manually inspect a prespecified development sample.

| Metric | Inputs | Calculation concept |
| --- | --- | --- |
| Faithfulness | Final answer and actual rendered evidence | Judge decomposes answer into claims; supported claims / total extracted claims |
| Answer/response relevancy | Question, answer, judge and embeddings | Generate questions from the answer and average cosine similarity with the original question; exact noncommittal handling depends on pinned implementation |
| Reference-based context precision | Question, ordered rendered contexts, reference | Judge labels each context useful (v_i); weighted precision = sum(Precision@i * v_i) / sum(v_i), subject to implementation's zero-denominator policy |

Context precision rewards placing useful evidence early; it is not simply the proportion of relevant sentences. Do not substitute this judge-based score for human-labeled retrieval Precision@K. Explicitly choose reference-based context precision to satisfy the handout's context relevance/precision alternative; do not claim to have run a separate context-relevance metric. Optional context recall measures reference information supported by context and is distinct from passage Recall@K.

Score the exact ordered/truncated context the answer generator received, not every passage seen during retries. Preserve rendered text/hash and source IDs. G0 has no retrieval context, so context precision and evidence faithfulness are not applicable. Refusals, empty contexts, no extracted claims, malformed judge output and timeouts get explicit status codes. Do not force undefined values to 1 or silently drop failures. Average eligible finite scores with valid/attempted counts and refusal/failure rates; show paired common-eligible comparisons if arms have different coverage. Choose and freeze one reference-selection policy for a metric requiring one reference (for example, the first valid reference in stable source order); preserve all references for QA scoring.

The conceptual definitions above follow the official [faithfulness documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/), [response relevancy documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/) and [context precision documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/). Installed-version behavior must be verified in the development smoke test.

### 4.5 Performance and diagnostic metrics: Q2.2/Q4.6/Q5

- End-to-end client latency = monotonic time from request dispatch to complete validated response; include network/server time, exclude offline RAGAS scoring. Log server retrieval, reranking, critic, generation and validation times separately where available. UI rendering and citation fetch times are separate measurements. Stage times need not sum to wall time if operations overlap.
- p50/p95 = 50th/95th percentiles of request latencies; pin percentile implementation. Report sample count, completed-request latency and timeout/error counts. A client timeout is not a successful completion or proof the server stopped.
- Throughput = completed requests / measured wall-clock batch interval. Also report successful requests/second and concurrency; do not calculate concurrent throughput as 1/mean latency.
- Hosted cost = input tokens*input price + output tokens*output price, summing generator, critic, embedding and judge calls separately. Store currency, price units/date and source. Local compute has no assumed API price; report GPU-hours and any known allocation cost, not “free”.
- Scalability: measure concurrency 1 first; optionally 2/4 if capacity allows, same workload/settings, with throughput, p95 and errors. Without those runs, provide a qualified discussion, not a measured scaling claim.
- Report retry/round distribution (maximum three retrieval rounds), model-call counts, token usage, refusal and technical-error rates. Define adaptive recovery as initial failure followed by final success under the same prespecified criterion; count only cases with both states scored and report the denominator. Do not call any answer-text change a recovery.
- Citation-ID validity = valid supplied-context citation IDs / cited IDs, with no-citation cases separate. This checks identity, not entailment. Semantic support needs manual checks or a separately specified evaluator.

Record hardware, precision, service concurrency, caches and warm-up. Proposed primary timing: warm model/index, no answer-result cache, fixed concurrency 1, same contexts/budgets; report setup/cold start separately. The five UI examples demonstrate usability but are too few to establish stable p95.

