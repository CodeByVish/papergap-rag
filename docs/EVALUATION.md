# Evaluation protocol — Week 1 proposal

## Current multi-system evaluation pool

Step $2.6$ is complete: `data/processed/annotation_common_v2/` contains fresh BM25, Dense and Hybrid retrieval for the frozen $200$ questions: $1000$ native hits per method, $600$ ranking rows and $1532$ unique pairs ($5$–$11$ per question). Group counts: Common $975$, BM25-only $277$, Dense-only $254$, Hybrid-only $26$. Every pair has one null final label; all original method ranks/scores and stable record mappings are retained. Inputs, pre-run configuration/code fingerprints, corpus hashes and all $25$ historical hashes verify. No old pairs, ranks, scores, labels or numbering were reused; isolation remains question-level and shared papers are allowed. Run `python -m src.data.build_common_pool verify` for read-only checks, or `run --output tmp/tmp_annotation_common_v2` for local fresh reproduction. No held-out content/results selected parameters. New formal Markdown export and human annotation remain pending under Steps $2.8$–$2.9$.

Step $2.5$ is complete: `data/processed/qa_for_held_out_v2.jsonl` freezes $200$ distinct held-out questions with zero intersection against all $2654$ banned IDs. The predeclared seed is $2026102805$; sorted eligible IDs are sampled without replacement in Python, retaining draw order. All $3329$ valid all-splits gold mappings are candidates; $1884$ are banned, leaving $1445$ eligible IDs with at least $5$ same-paper passages. The draw contains $78$ validation and $122$ test questions across $174$ papers; these are outcomes, not split restrictions. Only IDs, usage records and corpus metadata determine eligibility. Generate with `python -m src.data.freeze_held_out freeze`, verify with `python -m src.data.freeze_held_out verify`, and use a new `--output tmp/tmp_qa_for_held_out_v2.jsonl` for local reconstruction. Both data guides document all fields and acquisition from the GitHub P3 branch.

`data/processed/historical_bm25_retirement.manifest.json` retires the original question list, manifest and `annotation_held_out/` while retaining all $25$ files in place with exact hashes. The prior usage audit confirms normal frozen BM25 evaluation, so retirement imposes no blanket exclusion; $95$ old IDs are banned through other sources and $13$ eligible old IDs were randomly redrawn. No old pairs, ranks, scores, labels or numbering transfer to the new evaluation. Legacy freeze/formal BM25 export now refuse operation. Step $2.6$ fresh three-method retrieval is complete; Steps $2.8$–$2.9$ export/human annotation remain pending. Retain question-level isolation and allow shared papers; neither this freeze nor all-splits gold coverage establishes paper isolation or frozen downstream configurations.

Week 4 Step $2.3$ is implemented through `python -m scripts.build_annotation_pool multi-pilot`, using only the first $5$ saved chunk-selection questions, the same $365/40$ corpus, original queries, paper scope and top-$5$. `configs/annotation_pilot.json` pins BGE small English v1.5 revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, L2/cosine retrieval, $512$-token truncation, and equal-weight RRF with up to $20$ candidates per source and $k=60$. These are existing implementation/default choices verified for feasibility on development data; no quality search or held-out-driven tuning was performed. The successful settings are frozen in `data/processed/annotation_pilot_multi_v2/frozen_config.json` before any future formal expansion. The manifest records input/output/code hashes, actual pair counts and complete method metadata. See both data guides for reproduction and nested fields.

Each `(question_id, passage_id)` appears once with all source ranks and scores; shared pairs include two-way and three-way overlap. Annotation views disclose algorithm sources and allow names, hide gold/scores/ranks/internal IDs and other labels, and start with blank labels. They do not constitute algorithm-blind review. Each method must be evaluated using its original top-$5$ ranks joined to the common final labels, never Markdown group order. Unpooled passages remain unjudged. Pool recall covers only relevant judged union members; QASPER evidence recall has separate mapping coverage limits.

Step $2.4.2$ saves $2654$ unique banned questions in `data/processed/qa_banned_for_held_out.jsonl`, with pinned P1/P2 inventories, all $250$ P3 selection queries and retained development provenance. Verify with `python -m src.data.build_held_out_exclusions --verify`; both data guides document reproduction and nested fields. Owner designation is authoritative unless explicitly corrected. Other use is judged by whether it informed system choices; pure functional checks, raw export, gold mapping and normal frozen evaluation do not automatically exclude questions. Failed/void runs follow the same purpose rule. The accepted scope has no known unresolved eligibility records; unrecorded external/P4–P6 use is not claimed covered. Later explicit usage evidence must extend the inventory before sampling.

The historical BM25 annotation and freeze sections below retain the original blanket local-use rule and commands as history. Step $2.5$ supersedes their question freeze and commands; formal three-system retrieval is complete under Step $2.6$; new templates remain pending under Step $2.8$. Human assignment, independent judgments and agreement/adjudication remain pending under Step $2.9$. Preserve historical numbering and artifacts; do not use held-out content/results to choose configuration. Isolation remains at question level, allowing shared papers.

## Current annotation and metric protocol

`Instruction.pdf`, page $4$, Question $4$, explicitly requires at least $1000$ manually labeled records and at least $80\%$ inter-annotator agreement; it recommends three annotators and permits two. Query–passage records, question isolation, the three-method union and source-disclosed views are project choices, not additional assignment requirements. A retrieval pool with null labels does not yet satisfy the manual-labeling requirement.

The current union contains $N=1532$ unique pairs, not a fixed quota. Each of the $200$ questions contributes $5$–$15$ possible unique pairs from three complete top-$5$ lists; the observed range is $5$–$11$. Two distinct independent annotators per pair require $2N=3064$ initial judgments. Do not count a common pair again for every algorithm. Preserve annotator identity, both original labels and the separate adjudicated final label. Calculate raw agreement over unique pairs before adjudication; report sample sizes and, for fixed annotator pairs, Cohen's kappa. Assignment, collection and agreement remain pending under Step $2.9$.

Step $2.8$ must export English Markdown from `annotation_common_v2/pairs.jsonl`, retaining stable `record_number` mappings. Use $10$ batches of $20$ questions, keeping all of a question's pairs together; batch record counts vary with the union. Each `## Question 0001` shows the real title and original query, followed by `### Common Retrieved Chunks`, `### BM25`, `### Dense` and `### Hybrid`. Common contains two-way and three-way overlap in record-number order; method sections contain only exclusive results in native-rank order; empty groups show `None`. Each unique pair appears once per annotator with `#### Passage {record_id}`, `#### Relevance {record_id}` and its actual `Retrieved by:` sources. Here `record_id` displays the existing stable record number, not a new internal ID. No formal Markdown files or gold-joined verification file have yet been generated for this version.

Views disclose algorithm sources and the annotator's name or agreed identifier through `Annotator:`; do not describe this as algorithm-blind review. Hide gold evidence, scores, native ranks, internal question/paper/passage IDs and the other person's labels. Generate no HTML or notes field. Label $1$ when a passage helps answer the question, including useful partial evidence; topic overlap alone is insufficient. Label $0$ otherwise. Start each `Label:` blank and allow only `Label: 0` or `Label: 1`. Annotators must submit independent judgments before exchanging labels or resolving disagreements. Preserve returned originals and validate missing/illegal labels, unknown records and duplicate judgments by the same person before aggregation.

For each method, join `rankings.jsonl:hits[].record_number` to the common final relevance labels and compute metrics in `hits[].rank` order. Every algorithm retrieving a pair uses the same final label; Markdown grouping never changes ranking. For query $q$, let $U_q$ be its judged union and $R_q$ its members with final label $1$. Pool-based $\mathrm{Recall}@K=|\mathrm{top}K_q\cap R_q|/|R_q|$ measures coverage of relevant judged union members only. It is not exhaustive full-paper recall. Current native lists support $K\leq5$; a wider list or a new method needs a frozen judging/coverage protocol before comparison. Labels are still null, so no manual-label metric or agreement result is available. P6 must freeze zero-relevant-query handling and averaging before scoring.

Report QASPER evidence-reference recall separately: use the question's mapped `gold_passage_ids` from `gold_evidence_mapping_all_splits.jsonl` as the reference passage set, rather than replacing manual labels with gold overlap. This reference retains only questions whose answer evidence can be uniquely located and fully covered by the corpus; empty evidence, `FLOAT SELECTED`, ambiguity and incomplete mapping are excluded. Overlap IDs may include partial evidence. Record mapping version, corpus hashes, eligible-question coverage and denominator; passage-reference recall and paragraph-evidence coverage are different measures. Unpooled passages remain unjudged for manual relevance and cannot be assigned label $0$ merely because they are absent from the union or gold list.

## Historical BM25 annotation and held-out data

`Instruction.pdf`, page $4$, Question $4$, requires at least $1{,}000$ manually labeled records and at least $80\%$ inter-annotator agreement; two annotators are allowed. The assignment does not explicitly prescribe question-level or paper-level isolation. The team's query–passage record interpretation and the user's Week 4 design use $200$ questions with $5$ distinct passages each, giving $1{,}000$ unique pairs.

The all-splits gold mapping is a reference union, not an ordinary-test designation. Coverage alone neither freezes nor invalidates held-out status. The retired BM25 pool used question-level isolation with shared papers and all official splits, excluding the saved $250$ chunk-selection questions and every additional question found in local experiment records, including invalidated runs. That historical blanket local-use rule and its audit scope are superseded by the purpose-based cross-branch inventory above.

The retired BM25 templates hid retrieval methods and used two independent slots, each with $10$ English Markdown batches of $20$ questions / $100$ records. These describe the old export only; no historical manual judgments or agreement are claimed. Current source-disclosed annotation follows the protocol above.

Calculate raw agreement before adjudication, preserve both independent judgments and separately record the final adjudicated label. If agreement is below $80\%$, report it honestly and document any fresh independent labeling; never overwrite disagreements to inflate agreement. Current assignment, collection and adjudication are Week 4 Step $2.9$, outside the completed retrieval scope.

## Retrieval metrics

P6 defines K values, relevance rules, no-relevant-document handling and macro averaging before runs. P3 maps QASPER evidence to chunk IDs and records mapping failures. Deduplicate overlapping evidence for evidence-level measures where appropriate.

A union of three top-$5$ lists is incomplete relevance coverage. Report judged coverage at K. Label pool-based scores explicitly, and do not present pool recall as exhaustive full-paper recall. Evaluate ranking within the judged pool separately from full retrieval; where available, also report QASPER evidence-based metrics with mapping limitations. Unjudged results are unknown, not automatically confirmed negatives. Any additional judging must follow a frozen, system-neutral protocol.

## Minimal experiment ladder

| ID | Configuration | Evaluation |
| --- | --- | --- |
| R1 | BM25 | Rank-aware retrieval metrics and latency |
| R2 | Dense | Same |
| R3 | Hybrid RRF | Same |
| R4 | Hybrid RRF + reranker | Same |
| G0 | Generator without retrieval | QA baseline; evidence faithfulness is not applicable |
| G1 | BM25 RAG | QA, RAGAS and latency |
| G2 | Dense RAG | Same |
| G3 | Hybrid RAG | Same |
| G4 | Static hybrid + reranker RAG | Same; primary static baseline |
| G5 | Adaptive hybrid + reranker, single critic | Same plus retries, recovery and abstention |
| Optional | Gold-evidence reference, dual critic, NLI, citation-validator ablation | Only after required runs complete |

Use the same frozen generator, answer prompt, decoding settings, question set and context budget for static/adaptive comparisons; report additional retrieval/model calls and token cost. Retain citation validation in both G4 and G5. A separate validator ablation changes only the validator. The original E/F and G/H comparisons otherwise overlap or mix factors.

Maximum two retries means **three retrieval rounds total**. Report p50/p95 latency with hardware, caching and warm-up policy. Bootstrap uncertainty over questions (or papers), not over correlated query–passage records as if independent.

## QA, citations and RAGAS

Define normalization, multiple reference-answer handling, answer-type scoring and abstention behavior before final evaluation. Report answerable/unanswerable subsets and mapping exclusions. RAGAS judge scores complement manual inspection; record evaluator version, judge model, prompt, parameters, embedding model and cost. Establish refusal handling and missing-score policy in advance.

Citation-ID validation establishes that a cited passage was supplied to the generator. It does **not** establish entailment or that numbers are supported. Evaluate citation correctness/grounding separately using manual checks and the chosen faithfulness metric. Do not claim the validator prevents all unsupported factual statements.

Tune only on eligible development questions outside the frozen held-out list; official validation provenance alone does not authorize tuning. Freeze all prompts, retrieval settings and optional variants before evaluating held-out labels. Log genuine post-freeze bug fixes and rerun affected comparisons consistently.

## Historical BM25 held-out freeze sequence

The sequence below documents the retired version. The marker blocks its `freeze` and formal `export`; use `src.data.freeze_held_out` above for current question-list reproduction.

Run `python -m scripts.build_annotation_pool prepare`, then `pilot`, `freeze`, and `export`. Commands must run from the repository root. The default paths and complete field tables are in `data/README.md`.

Preparation extracts the persisted fourth-round $250$ questions without resampling. The pilot uses only the first $5$ of these development questions with the fixed $365/40$ all-paper corpus, paper-scoped BM25 and top-$5$ retrieval. Before sampling, validate the completed pilot and input/source hashes. Eligibility uses only IDs, prior-use records, source split and per-paper passage counts; require at least $5$ retrievable passages. Do not preview candidate queries, answers or evidence.

The predeclared seed is $20261028$: sort eligible question IDs, call Python `Random(seed).sample` without replacement for $200$ IDs and preserve draw order. Persist `qa_for_held_out.jsonl` before retrieval; export uses that file without resampling. Save input hashes, exclusions, eligible/final IDs, retrieval settings, HEAD, dirty status and source hashes. Freeze is specific to this annotation-pool configuration; other final system variants still require their own settings freeze before evaluation.

Held-out questions, answers, evidence, labels and results must never drive tuning, development or prompt design. The corpus contains paper content only. Retrieval sees only the query and paper scope; gold references are associated afterward in `verification.jsonl`. Distribute only the appropriate Markdown batch, keeping verification files private. An unjudged passage remains unknown, not automatically irrelevant. Genuine post-freeze bugs require a recorded cause and consistent reruns of affected configurations, never a result-driven targeted improvement.

## Unified QA export and access boundary

`qa.jsonl` and the gold mapping physically cover all official splits. Mechanical copying, hashing, schema checks and ID-only eligibility checks do not authorize content inspection for tuning. The current pool is determined by saved question IDs and actual usage, not by official split names. The legacy `src/data/split_policy.py` guard remains available for historical split-based development runners; do not reinterpret those historical runs under the new pool policy. Track raw data, generated question lists, pair records and annotation files under `data/` on the P3 branch with provenance and manifests as required by `AGENTS.md`; keep credentials, weights and indexes outside Git. Distribute annotation views independently of the reference files.
