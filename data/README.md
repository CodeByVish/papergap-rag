# QASPER data guide

[中文版](README_zh-CN.md)

Raw and processed data and their manifests are tracked on the P3 working branch, `p3-qasper-foundation`. This guide describes Git-based sharing, local reproduction, and the fields of each processed artifact. Run commands from the repository root in the project Python 3.11 environment after installing `requirements.txt` or `requirements-dev.txt`.

## Data versions and updates

Step $2.7$ synchronizes the rebuild documentation. The original BM25 pool and its blank templates are retired history; the `v2` question freeze and formal three-method common pool are complete; the new formal annotation export (Step $2.8$) and human judgments (Step $2.9$) remain pending. The $1532$ records are the actual deduplicated union, not a fixed target: three top-$5$ lists yield $5$–$15$ unique pairs per question ($1000$–$3000$ overall), with $5$–$11$ observed here. Two independent judgments per unique pair will require $3064$ judgments, with no extra count for shared sources.

The planned formal views disclose all `Retrieved by:` sources and the `Annotator:` name or agreed identifier; they are not algorithm-blind. Use the English question-grouped layout documented in the pilot view section, with $10$ batches of $20$ questions and variable record counts, preserving `record_number` and native algorithm ranks. No formal view output path or generation command is implemented yet; do not substitute the retired BM25 export or development `multi-pilot` command. The six existing `annotation_common_v2` outputs and their nested fields are documented below. See [the current annotation and metric protocol](../docs/EVALUATION.md#current-annotation-and-metric-protocol) for independent labeling, shared final labels and Recall@K coverage. Pool recall uses judged relevant union members; QASPER passage-reference recall uses mapped `gold_passage_ids`, subject to evidence-location and corpus-coverage filters. Neither reference makes unpooled passages manual negatives.

Week 4 Step $2.5$ is complete: the independent `qa_for_held_out_v2.jsonl` freezes $200$ eligible questions with zero banned overlap. Historical BM25 files are retired and retained with hashes; formal three-algorithm retrieval is complete as documented below; new annotation exports remain pending. Current commands and fields are below; later legacy BM25 reproduction sections describe history only.

Week 4 Step $2.4.2$ completes the scoped cross-branch exclusion inventory: P1's $2593$, P2's $106$ and P3's $250$ selection IDs merge into $2654$ unique banned questions. All qualifying overlapping sources are retained. No known eligibility records remain unresolved within this scope; unrecorded external/P4–P6 use is not claimed to be covered. Step $2.5$ reconstructs this inventory before the new freeze; add later explicit usage evidence in a new version before further sampling. Formal retrieval is now complete under Step $2.6$; historical artifact bytes are unchanged.

Week 4 Step $2.3$ adds a development-only BM25/Dense/Hybrid pilot under `data/processed/annotation_pilot_multi_v2/`: $5$ questions, $36$ unique pairs, $25$ common pairs, $5$ BM25-only pairs, $6$ Dense-only pairs and no Hybrid-only pairs. Each method has $25$ hits. Formal retrieval is complete under Step $2.6$; Step $2.5$ completes renewed held-out eligibility checks. The earlier BM25 artifacts are historical; do not distribute them as the new common pool. Obtain the pilot data with the tracked artifacts from the GitHub P3 branch. The local `annotation_pilot_multi_v1/` preliminary snapshot is retained; `v2` reran after an import-only lint correction, with identical pair/ranking bytes. Existing output directories are refused; use `--multi-output` with a new path for future runs.

Step $2.6$ now saves fresh formal BM25/Dense/Hybrid retrieval under `data/processed/annotation_common_v2/`. It consumes the persisted $200$-question freeze without resampling, validates the full banned inventory and all historical hashes, and copies the development-frozen $365/40$/paper-scoped/top-$5$ settings before indexing. Every source retains all native ranks/scores; the unique union has one null final label per pair. No historical retrieval result is reused. Gold evidence is not joined in this step. New Markdown export and human annotation remain Steps $2.8$–$2.9$.

Obtain these files and matching inputs from the GitHub P3 branch together with the other tracked data. For local reproduction use `python -m src.data.build_common_pool run --output tmp/tmp_annotation_common_v2`; an existing directory is refused. Load the pinned model from ignored `.cache/huggingface/` as in the pilot instructions below. The CLI sets `HF_HUB_OFFLINE=1` before model imports and restores it afterward. The first attempt omitted this existing development wrapper policy and failed during an optional processor probe before dense indexing completed, with no rankings or pairs produced; its three pre-run files are retained locally in `tmp/tmp_common_pool_failed_processor/`. The successful run changes no retrieval parameters. Use original algorithm ranks with common final labels, never Markdown display order. Unpooled passages remain unjudged; pool Recall@K uses relevant judged union pairs as its denominator, while gold-evidence recall has separate mapping/coverage limits. Isolation is question-level and permits shared papers; no held-out-driven tuning is allowed.

Formal validation: $200$ questions, $1000$ hits per method, $600$ ranking rows, $1532$ unique pairs and $5$–$11$ pairs per question. Common: $975$; BM25-only: $277$; Dense-only: $254$; Hybrid-only: $26$. All labels are null; no human annotation has been completed.

## `data/processed/annotation_common_v2/questions.jsonl`

Generate with `python -m src.data.build_common_pool run`; verify with `python -m src.data.build_common_pool verify`.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `paper_id` | `string` | Canonical identifiers in saved question order. |
| `question` | `string` | Original unmodified question. |
| `source_split` | `string` | Official provenance; no split filter. |

## `data/processed/annotation_common_v2/pairs.jsonl`

Generate with `python -m src.data.build_common_pool run`; verify with `python -m src.data.build_common_pool verify`.

| Field | Type | Meaning |
| --- | --- | --- |
| `record_number` | `integer` | Stable numbering within this formal version, starting at one. |
| `question_id`, `paper_id`, `passage_id` | `string` | Unique question/passage pair and paper scope. |
| `source_split`, `question`, `paper_title`, `passage` | `string` | Provenance, original query, real title and full passage text. |
| `label` | `null` | One shared final relevance label; all initially null. |
| `retrieved_by[]` | `string` | Ordered BM25/Dense/Hybrid sources. |
| `retrievals[]` | `object` | One native retrieval relation per source. |
| `retrievals[].method` | `string` | BM25, Dense or Hybrid. |
| `retrievals[].rank` | `integer` | Original one-based algorithm rank, one through five. |
| `retrievals[].score` | `number` | Finite native BM25, cosine or RRF score. |
| `display_group` | `string` | Common Retrieved Chunks for at least two sources; otherwise the sole method. |

## `data/processed/annotation_common_v2/rankings.jsonl`

Generate with `python -m src.data.build_common_pool run`; verify with `python -m src.data.build_common_pool verify`.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `method` | `string` | One row per frozen question and method. |
| `hits[]` | `object` | Exactly five distinct same-paper hits in native rank order. |
| `hits[].passage_id` | `string` | Canonical corpus passage ID. |
| `hits[].record_number` | `integer` | Foreign key to the single union pair. |
| `hits[].rank` | `integer` | Original rank, one through five. |
| `hits[].score` | `number` | Unmodified finite method score. |

## `data/processed/annotation_common_v2/frozen_config.json`

Generate with `python -m src.data.build_common_pool run`; verify with `python -m src.data.build_common_pool verify`.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed. |
| `chunk_size_words`, `chunk_overlap_words`, `top_k`, `question_count` | `integer` | $365$, $40$, $5$ and $200$. |
| `question_selection`, `scope`, `record_order`, `label_policy` | `string` | Saved questions, paper scope, stable first-encounter numbering and one null label per pair. |
| `execution.HF_HUB_OFFLINE`, `execution.model_loading` | `string` | Offline setting 1 and the same loading policy as the development CLI. |
| `retrieval` | `object` | Normalized pilot retrieval configuration; fields described in the pilot frozen-config section. |
| `retrieval.mode` | `string` | hybrid; no reranker. |
| `retrieval.candidate_k`, `retrieval.rrf_k` | `integer` | $20$ and $60$; equal-weight RRF. |
| `retrieval.dense` | `object` | revision/device/batch_size/cache_folder/local_files_only as documented for the pilot; values unchanged. |
| `retrieval.reranker` | `object` | Inactive normalized defaults; not loaded or used in this run. |
| `retrieval.reranker.revision`, `retrieval.reranker.device`, `retrieval.reranker.cache_folder` | `string` | Inactive revision, CPU and local cache path. |
| `retrieval.reranker.batch_size`, `retrieval.reranker.max_length` | `integer` | Inactive defaults $8$ and $512$. |
| `retrieval.reranker.local_files_only` | `boolean` | Inactive offline default, true. |
| `retrievers.<method>` | `object` | Complete effective metadata, including nested bm25/dense/reranker, package versions and fusion settings; same fields as the pilot manifest retrievers table. |
| `retrievers.<method>.id`, `retrievers.<method>.mode`, `retrievers.<method>.source_commit`, `retrievers.<method>.scope`, `retrievers.<method>.score`, `retrievers.<method>.tie_break` | `string` | Implementation identity, method, upstream commit, paper scope, native score semantics and tie rules. |
| `retrievers.<method>.packages.<package>` | `string` | Installed dependency versions. |
| `retrievers.<method>.persistent_score_cache`, `retrievers.<method>.bm25.enabled`, `retrievers.<method>.dense.enabled`, `retrievers.<method>.reranker.enabled` | `boolean` | Cache/component flags; no persistent score cache or reranker. |
| `retrievers.<method>.bm25.tokenizer` | `string` | Casefold plus Unicode word runs; absent for standalone Dense. |
| `retrievers.<method>.bm25.k1`, `retrievers.<method>.bm25.b`, `retrievers.<method>.bm25.epsilon` | `number` | Active BM25 parameters $1.5$, $0.75$, $0.25$. |
| `retrievers.<method>.dense.revision`, `retrievers.<method>.dense.device`, `retrievers.<method>.dense.cache_folder`, `retrievers.<method>.dense.model_name`, `retrievers.<method>.dense.tokenizer_revision`, `retrievers.<method>.dense.query_instruction`, `retrievers.<method>.dense.normalization`, `retrievers.<method>.dense.similarity_metric`, `retrievers.<method>.dense.index_type`, `retrievers.<method>.dense.truncation`, `retrievers.<method>.dense.truncation_observation` | `string` | Active dense model/encoding metadata, as specified in the pilot table. |
| `retrievers.<method>.dense.batch_size`, `retrievers.<method>.dense.max_seq_length` | `integer` | Active dense batch size $32$ and token limit $512$. |
| `retrievers.<method>.dense.local_files_only` | `boolean` | True for active Dense/Hybrid model loading. |
| `retrievers.Hybrid.candidate_k_per_source`, `retrievers.Hybrid.rrf_k`, `retrievers.Hybrid.final_top_k` | `integer` | $20$, $60$ and $5$. |
| `retrievers.Hybrid.rerank_all_fused_candidates` | `boolean` | False. |

## `data/processed/annotation_common_v2/run_inputs.json`

Generate with `python -m src.data.build_common_pool run`; verify with `python -m src.data.build_common_pool verify`.

| Field | Type | Meaning |
| --- | --- | --- |
| `inputs.<path>` | `string` | Pre-run exact-byte SHA-256 of config, pilot freeze, held-out list/manifest, bans, corpus, QA/papers and retirement. |
| `code.commit`, `code.python` | `string` | HEAD and Python version captured before retrieval. |
| `code.working_tree_status[]` | `string` | Saved Git short status, including uncommitted implementation. |
| `code.source_sha256.<path>` | `string` | Exact implementation hashes; src and script sources checked again before writing results. |

## `data/processed/annotation_common_v2/manifest.json`

Generate with `python -m src.data.build_common_pool run`; verify with `python -m src.data.build_common_pool verify`.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version`, `purpose`, `reason`, `reuse_policy`, `usage_boundary` | `string` | Proposed formal version, rebuild reason, no old-result reuse and evaluation boundaries. |
| `historical_retained_files.<path>` | `string` | All 25 retired BM25 paths and unchanged byte hashes. |
| `settings` | `object` | Exact frozen_config.json object; nested fields above. |
| `inputs.<path>`, `outputs.<path>` | `string` | Exact input/output hashes; manifest does not hash itself. |
| `code` | `object` | Same nested fields as run_inputs.json above. |
| `indexed_paper_count`, `indexed_passage_count` | `integer` | Complete selected-paper index size, equivalent under paper-scoped retrieval. |
| `validation.question_count`, `validation.pair_count`, `validation.ranking_count`, `validation.hits_per_method` | `integer` | 200 questions, actual union size, 600 ranking rows and 1000 hits per method. |
| `validation.pair_counts_per_question.<question_id>`, `validation.group_counts.<group>` | `integer` | Actual per-question and source-group unique-pair counts. |
| `validation.pair_count_range[]` | `integer` | Observed minimum and maximum, each within five to fifteen. |
| `runtime.platform`, `runtime.processor`, `runtime.timing_policy` | `string` | Host details and single-run index-plus-retrieval timing policy; not a latency benchmark. |
| `runtime.elapsed_seconds` | `number` | Index and retrieval wall time in seconds. |

## `data/processed/qa_for_held_out_v2.jsonl`

Step $2.5$ freezes this independent held-out question list for the new common evaluation. Before the first draw, `configs/held_out_sampling_v2.json` fixed seed $2026102805$, ascending candidate IDs and Python `Random(seed).sample` without replacement, preserving draw order. From $3329$ valid all-splits gold-mapped questions, $1884$ are banned and none of the remaining questions fail the minimum-$5$-passage condition, leaving $1445$ eligible IDs. The frozen $200$ unique questions have no banned intersection: $78$ validation and $122$ test, covering $174$ papers with at least $6$ passages each. These split counts are sampling outcomes, not quotas; no official-split filter is applied. Isolation is question-level and permits shared papers. No candidate question, answer, evidence or historical retrieval/label content was previewed to select the draw.

Run the following from the project Python $3.11$ environment at the repository root. Generation refuses existing outputs. The retirement command has already run; do not delete its record to rerun it. Obtain the JSONL, both manifests below, configs and their matching inputs from the GitHub P3 branch with the other tracked data; no Release is required. Locally reproduce JSONL bytes with `python -m src.data.freeze_held_out freeze --output tmp/tmp_qa_for_held_out_v2.jsonl`; its companion records that output path and the local code identity.

```powershell
python -m src.data.freeze_held_out retire
python -m src.data.freeze_held_out freeze
python -m src.data.freeze_held_out verify
```

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id` | `string` | Canonical unique question ID, in frozen draw order. |
| `paper_id` | `string` | Paper used for scoped retrieval. |
| `question` | `string` | Original QA query copied verbatim after ID sampling. |
| `source_split` | `string` | Official split provenance; no evaluation-role assignment. |

## `data/processed/qa_for_held_out_v2.manifest.json`

Generated by `python -m src.data.freeze_held_out freeze` and reconstructed by `verify` above. The freeze verifies the complete banned inventory and historical hashes before drawing; it checks the gold/corpus/QA companion hashes, fixed $365/40$ chunking, unique nonempty passages and canonical identity metadata. It preserves all eligible IDs, disjoint rejection lists and exact final IDs. Later explicit development-use evidence requires a new inventory/version; no held-out content or results may guide system choices. This question freeze does not perform Step $2.6$ retrieval or freeze future generator/agent configurations.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version`, `purpose`, `status` | `string` | Proposed schema, held-out purpose and frozen state. |
| `configuration` | `object` | Exact predeclared sampling configuration. |
| `configuration.schema_version` | `string` | `v0-proposed`. |
| `configuration.seed`, `configuration.question_count`, `configuration.minimum_passages_per_paper` | `integer` | Seed, required draw size and passage threshold. |
| `configuration.sampling_rule`, `configuration.scope`, `configuration.isolation`, `configuration.eligibility` | `string` | Ordering/draw, all-splits scope, question isolation and metadata-only filters. |
| `configuration.reason`, `configuration.usage_boundary` | `string` | Resampling reason and prohibition on held-out-driven tuning. |
| `inputs.<path>` | `string` | SHA-256 of config, retirement, banned list/manifest, gold/manifest, corpus/manifest and source exports. |
| `code.commit`, `code.python`, `code.implementation_sha256` | `string` | Generation HEAD, Python version and exact uncommitted implementation fingerprint. Verification preserves the saved HEAD. |
| `candidate_count`, `banned_question_count`, `question_count`, `paper_count` | `integer` | Gold candidate total, complete banned total, selected questions and selected papers. |
| `eligible_question_ids[]` | `string` | Sorted eligible question IDs. |
| `rejections.banned[]`, `rejections.fewer_than_minimum_passages[]` | `string` | Rejected IDs; banned takes precedence over corpus-size rejection. |
| `question_ids[]` | `string` | Final frozen IDs in draw order. |
| `source_split_counts.<split>` | `integer` | Selected split counts. |
| `selected_paper_passage_counts.<paper_id>` | `integer` | Distinct corpus passages in each selected paper. |
| `historical_redrawn_question_ids[]` | `string` | $13$ eligible historical IDs randomly drawn again, without result reuse. |
| `validation.exactly_200_unique`, `validation.banned_intersection_empty`, `validation.at_least_five_passages_per_paper` | `boolean` | Cardinality, exclusion and corpus-capacity checks. |
| `validation.canonical_question_text`, `validation.retained_history_hashes_verified`, `validation.exclusion_inventory_reconstructed` | `boolean` | Original text, unchanged history and complete banned-inventory reconstruction checks. |
| `output.path`, `output.sha256` | `string` | Versioned question-list path and exact byte hash. |
| `next_action` | `string` | Generation-time next action retained verbatim; Step $2.6$ retrieval is now complete in the independent common-pool directory. |

## `data/processed/historical_bm25_retirement.manifest.json`

Generated once by `python -m src.data.freeze_held_out retire`; `verify` validates it and all retained bytes before reconstructing the new freeze. All $25$ original files remain at `qa_for_held_out.jsonl`, its manifest and `annotation_held_out/`; their pairs, ranks, scores, labels and numbering belong exclusively to the retired BM25 version. The old `freeze` and formal BM25 `export` commands now refuse operation when this marker exists. Pilot commands remain available. Retirement is voluntary resampling for a common evaluation, not a finding that all old questions were contaminated. The Step $2.4$ usage audit found normal frozen BM25 evaluation, requiring no blanket ban; $95$ old questions are nevertheless banned by other accepted sources, leaving $105$ potentially eligible old questions before the candidate metadata filter. No new tuning-use evidence was identified.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version`, `status`, `reason` | `string` | Proposed schema, retired state and resampling rationale. |
| `retained_files.<path>` | `string` | Original SHA-256 of every retained historical file. |
| `banned_manifest_sha256` | `string` | Hash of the verified Step $2.4$ inventory manifest. |
| `usage_decision.source_id`, `usage_decision.path`, `usage_decision.sha256` | `string` | Historical-use decision identity and saved BM25 manifest hash. |
| `usage_decision.question_ids[]` | `string` | All $200$ old evaluation question IDs. |
| `usage_decision.decision`, `usage_decision.usage`, `usage_decision.reason` | `string` | No automatic exclusion for normal frozen evaluation; other sources still apply. |
| `historical_question_count` | `integer` | Original question count. |
| `historical_banned_question_ids[]`, `other_historical_question_ids[]` | `string` | Old IDs inside and outside the complete banned inventory. |
| `reuse_policy`, `replacement_questions` | `string` | No old-result reuse and canonical replacement question path. |

## `data/processed/held_out_exclusion_sources/p1_used_question_ids.jsonl`

Byte-preserving snapshot of `docs/handoffs/p1_used_question_ids.jsonl` from branch `p1/week3-week4`, commit `3bb545c967efe63197cb99a799628162f5c2b512`, containing $2593$ unique IDs. Obtain it with the other data from the GitHub P3 branch. To reproduce the snapshot locally, capture `git show <commit>:docs/handoffs/p1_used_question_ids.jsonl` through Python `subprocess.check_output` and save with `Path.write_bytes`, then compare SHA-256 with `configs/held_out_exclusions.json`. Avoid shell text redirection that changes bytes. Owner quotes and source pins are preserved in the config/manifest. Historical files named inside the inventory need not exist or parse; reducing designated IDs requires explicit owner correction.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `paper_id`, `source_split` | `string` | Delivered QA identity, checked against local QA. |
| `sources` | `array<string>` | All owner-reported usage paths, kept verbatim. |
| `usage` | `string` | Owner's usage description. |
| `usage_categories` | `array<string>` | Owner's detailed usage categories. |

## `data/processed/held_out_exclusion_sources/p2_used_question_ids.jsonl`

Byte-preserving snapshot of `docs/handoffs/p2_used_question_ids.jsonl` from branch `p2/question-usage-inventory`, commit `3b13f22fe6df29d15babea529cf2fc8f13c18f68`, containing $106$ unique IDs. Obtain from the GitHub P3 branch or reproduce through the same Python byte-preserving `git show` route using this commit/path and check the pinned SHA-256.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `paper_id`, `source_split` | `string` | Delivered QA identity. |
| `sources` | `array<string>` | All owner-reported usage paths. |
| `usage` | `string` | Owner's usage description. |

## `data/processed/qa_banned_for_held_out.jsonl`

Generate with `python -m src.data.build_held_out_exclusions`; verify existing artifacts with `python -m src.data.build_held_out_exclusions --verify`. Reproduce without replacing shared data using `python -m src.data.build_held_out_exclusions --output tmp/tmp_qa_banned_for_held_out.jsonl`: JSONL bytes match, while the manifest records the new output path and generation identity. Existing outputs are refused. The commands use tracked snapshots, QA and saved preparation/pilot manifests, without network, models, seed reconstruction or parsing historical results. Obtain JSONL, manifest, snapshots and config together from the GitHub P3 branch; no Release is needed.

All owner-designated IDs are banned. Other questions are banned when used to choose or adjust models, parameters, algorithms, prompts or evidence handling; failed/void runs follow the same purpose rule. P3 selection comparisons and three development pilots retain provenance. The old preparation's blanket $253$-ID exclusion is not reused: $3$ functional smoke IDs and the original $200$-question frozen BM25 evaluation are not automatically banned, though other qualifying sources can ban them. Raw export and gold mapping alone do not imply exclusion. Preserved functional-test evidence and decisions are in the config/manifest. The banned inventory itself is not a question freeze; the independent `v2` freeze is documented above. Isolation is question-level and permits shared papers.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `paper_id`, `question`, `source_split` | `string` | Unique ID, matching paper, unmodified original question and official split. |
| `sources` | `array<object>` | Every qualifying source, preserving overlaps. |
| `sources[].source_id`, `sources[].usage`, `sources[].exclusion_reason` | `string` | Manifest source key, purpose and exclusion rationale. |
| `sources[].original_record` | `object` | Entire delivered row, with all original metadata. |
| `sources[].original_record.question_id` | `string` | Always present; canonical QA join key. |
| `sources[].original_record.paper_id`, `.question`, `.source_split` | optional `string` | Source-supplied identity/text, checked against QA when present. |
| `sources[].original_record.sources`, `.usage_categories` | optional `array<string>` | Complete original owner paths/categories. |
| `sources[].original_record.usage` | optional `string` | Original owner usage description. |

## `data/processed/qa_banned_for_held_out.manifest.json`

Generated and verified by the same commands. Inputs use exact-byte SHA-256; owner sources additionally pin branch/commit/path. Local version records generation HEAD/branch and exact input/implementation hashes, including uncommitted files; it does not claim these files were already committed. Verification allows later HEAD changes while reconstructing rows and checking all saved hashes. Unknown IDs, identity conflicts, duplicate question IDs within a source, changed pins/counts, lost provenance and newly unresolved historical/pilot use fail before writing.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version`, `purpose`, `repository`, `scope`, `exclusion_rule` | `string` | `v0-proposed`, purpose, origin and bounded usage policy. |
| `local_source_version` | `object` | Generation version. |
| `local_source_version.branch`, `.commit` | `string` | Local P3 branch and full HEAD SHA. |
| `implementation` | `object` | Exact source identity. |
| `implementation.path`, `.sha256` | `string` | Module path and SHA-256. |
| `inputs` | `object<string,string>` | Config/QA/snapshot/preparation/pilot/evaluation paths to SHA-256. |
| `owner_inventories` | `array<object>` | Owner source pins and exact statements. |
| `owner_inventories[].source_id`, `.branch`, `.commit`, `.path`, `.snapshot`, `.sha256`, `.owner_statement` | `string` | Owner key, source identity, snapshot, hash and quote. |
| `owner_inventories[].question_count` | `integer` | Expected unique count. |
| `source_counts`, `source_split_counts` | `object<string,integer>` | Pre-union source counts and final split counts. |
| `question_count`, `provenance_count` | `integer` | Unique questions and qualifying source memberships. |
| `usage_decisions` | `array<object>` | Purpose decisions for historical P3 use/frozen evaluation. |
| `usage_decisions[].source_id`, `.path`, `.sha256`, `.decision`, `.usage`, `.reason` | `string` | Source identity/hash, decision, purpose and reason. |
| `usage_decisions[].question_ids` | `array<string>` | Persisted IDs covered by each decision. |
| `configuration` | `object` | Deterministic generation settings. |
| `configuration.join_key`, `.order`, `.sampling` | `string` | ID join, ascending ID order, no sampling. |
| `configuration.question_fields` | `array<string>` | Canonical retained fields. |
| `unresolved_records` | `array<object>` | Empty within accepted scope; unknown use blocks generation. |
| `validation` | `object<string,boolean>` | ID uniqueness, complete fields, identity, full owner/selection/provenance coverage and scoped resolution checks. |
| `output` | `object` | Final JSONL identity. |
| `output.path`, `.sha256` | `string` | Output path and SHA-256. |

## `data/processed/annotation_pilot_multi_v2/questions.jsonl`

Generate every artifact in this pilot with `python -m scripts.build_annotation_pool multi-pilot --config configs/annotation_pilot.json`. The command takes the first $5$ persisted selection questions, verifies the saved list hash against preparation, and indexes all passages of their papers from the same $365/40$ corpus. It opens no held-out question list or results. CLI model loading is offline, including optional processor probes; the prior process environment is restored afterward. Prepare the pinned weights once with:

```powershell
python -c "from huggingface_hub import snapshot_download; snapshot_download('BAAI/bge-small-en-v1.5', revision='5c38ec7c405ec4b44b94cc5a9bb96e735b38267a', cache_dir='.cache/huggingface', allow_patterns=['*.json','*.txt','*.safetensors','1_Pooling/*'], ignore_patterns=['onnx/*','openvino/*'])"
```

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `paper_id` | `string` | Original question and paper identifiers. |
| `question` | `string` | Original unmodified query. |
| `source_split` | `string` | Official split provenance; not an eligibility decision. |

## `data/processed/annotation_pilot_multi_v2/frozen_config.json`

Generated by the same `multi-pilot` command. Exact copy of `configs/annotation_pilot.json`; reuse this successful configuration before any future formal run. This is a feasibility check using existing model/default fusion settings, not a claim of optimal retrieval quality. No held-out content or results select parameters.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | `v0-proposed`. |
| `question_count`, `question_selection` | `integer`, `string` | First $5$ saved development questions in persisted order. |
| `chunk_size_words`, `chunk_overlap_words`, `top_k` | `integer` | $365$, $40$, $5$. |
| `retrieval` | `object` | Hybrid settings shared with standalone source retrievers. |
| `retrieval.mode` | `string` | `hybrid`, without reranking. |
| `retrieval.candidate_k`, `retrieval.rrf_k` | `integer` | Up to $20$ candidates per source; equal-weight RRF $1/(60+rank)$ with $k=60$. |
| `retrieval.dense` | `object` | BGE small English v1.5 inference configuration. |
| `retrieval.dense.revision` | `string` | Immutable model/tokenizer SHA `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. |
| `retrieval.dense.device`, `retrieval.dense.batch_size` | `string`, `integer` | CPU; batch size $32$. |
| `retrieval.dense.cache_folder`, `retrieval.dense.local_files_only` | `string`, `boolean` | Ignored project cache; offline loading enabled. |

Dense uses L2-normalized embeddings, cosine via FAISS `IndexFlatIP`, $512$-token truncation, the existing query instruction `Represent this sentence for searching relevant passages: `, and no passage instruction. Full passage text remains in exports. BM25 uses casefold/Unicode word tokenization with `k1=1.5`, `b=0.75`, `epsilon=0.25`. Ties use ascending passage IDs. The manifest records effective parameters and installed versions.

## `data/processed/annotation_pilot_multi_v2/pairs.jsonl`

Generated by `python -m scripts.build_annotation_pool multi-pilot`. One row per unique `(question_id, passage_id)`; $5$–$15$ rows per question. Numbers follow question order, then first discovery in BM25/Dense/Hybrid order. They belong only to this development version, not the historical formal pool. The single final relevance label will be shared by every method retrieving the pair.

| Field | Type | Meaning |
| --- | --- | --- |
| `record_number` | `integer` | Stable one-based number within this pilot. |
| `question_id`, `paper_id`, `passage_id` | `string` | Original join identifiers. |
| `source_split`, `question`, `paper_title`, `passage` | `string` | Original provenance, query, real title and full passage. |
| `label` | `null or integer` | Initially null; later binary human relevance. |
| `retrieved_by` | `array<string>` | All real sources in BM25/Dense/Hybrid order. |
| `display_group` | `string` | `Common Retrieved Chunks` for two or three sources; otherwise the unique source name. |
| `retrievals` | `array<object>` | Complete membership with original per-system rankings. |
| `retrievals[].method`, `retrievals[].rank`, `retrievals[].score` | `string`, `integer`, `number` | Algorithm, original one-based rank and native BM25/cosine/RRF score. |

## `data/processed/annotation_pilot_multi_v2/rankings.jsonl`

Generated by `python -m scripts.build_annotation_pool multi-pilot`. Three rows per question preserve each original top-$5$. Evaluate each method by these original ranks joined to common labels, never by Markdown display order. Unpooled passages have unknown relevance; pool Recall@K covers only judged relevant union members, while gold-reference recall covers mapped evidence with its mapping limitations.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id`, `method` | `string` | Query and disclosed retrieval method. |
| `hits` | `array<object>` | Five distinct valid same-paper hits in rank order. |
| `hits[].passage_id`, `hits[].record_number` | `string`, `integer` | Link to the unique pair. |
| `hits[].rank`, `hits[].score` | `integer`, `number` | Original rank and native score. |

## `data/processed/annotation_pilot_multi_v2/verification.jsonl`

Generated by `python -m scripts.build_annotation_pool multi-pilot`; never distribute it as an annotation view. Contains every `pairs.jsonl` field above, with references joined only after all rankings finish. References do not initialize human labels. Nested evidence fields have the same types and meanings as the historical `annotation_held_out/verification.jsonl` table below.

| Additional field | Type | Meaning |
| --- | --- | --- |
| `gold_passage_ids` | `array<string>` | Mapped reference passage IDs. |
| `gold_evidence_match` | `boolean` | Pair passage belongs to the mapped reference. |
| `evidence_paragraphs` | `array<object>` | Original evidence paragraphs and overlap metadata. |
| `evidence_paragraphs[].location`, `evidence_paragraphs[].text` | `string` | Source coordinate and original paragraph. |
| `evidence_paragraphs[].section_index`, `evidence_paragraphs[].paragraph_index` | `integer` | Zero-based source positions. |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | Full non-whitespace union coverage. |
| `evidence_paragraphs[].passage_matches` | `array<object>` | Reference-to-corpus overlaps. |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | Overlapping passage identifier. |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | Half-open source interval. |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | Single passage covers the full paragraph. |

## `data/processed/annotation_pilot_multi_v2/manifest.json`

Generated by `python -m scripts.build_annotation_pool multi-pilot`. Input/output SHA-256 values identify this independent version; existing outputs are refused. Shared interfaces remain `v0-proposed`. The historical BM25 freeze and record numbers are preserved.

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version`, `purpose` | `string` | Proposed schema and development-only purpose. |
| `question_ids`, `question_count`, `pair_count` | `array<string>`, `integer`, `integer` | Ordered selected IDs and actual counts. |
| `group_counts`, `pair_counts_per_question` | `object<string,integer>` | Display-group and per-query union counts. |
| `indexed_paper_count`, `indexed_passage_count` | `integer` | Complete selected-paper index scope. |
| `settings` | `object` | Every field of `frozen_config.json`, documented above. |
| `code` | `object` | Same `commit`, `python`, `working_tree_status`, `source_sha256.<path>` fields/types as the historical manifest table below. |
| `inputs.<path>`, `outputs.<path>` | `string` | Exact SHA-256 of inputs and outputs; excludes this manifest itself. |
| `retrievers` | `object` | Keys `BM25`, `Dense`, `Hybrid`; effective metadata for each method. |
| `retrievers.<method>` | `object` | Historical `retriever` metadata fields below plus active dense/fusion fields described next. |
| `retrievers.<method>.dense` | `object` | Enabled flag, all dense config fields above, model/tokenizer revision, query instruction, normalization, metric, index type, truncation and truncation observation. |
| `retrievers.<method>.dense.enabled` | `boolean` | Whether Dense is active. |
| `retrievers.<method>.dense.max_seq_length` | `integer` | $512$. |
| `retrievers.<method>.dense.model_name`, `tokenizer_revision`, `query_instruction`, `normalization`, `similarity_metric`, `index_type`, `truncation`, `truncation_observation` | `string` | These sibling fields inside `dense` describe the exact model/encoding rules; truncation frequency was not measured. |
| `retrievers.Hybrid.candidate_k_per_source`, `retrievers.Hybrid.rrf_k`, `retrievers.Hybrid.final_top_k` | `integer` | $20$, $60$, $5$. |
| `retrievers.Hybrid.rerank_all_fused_candidates` | `boolean` | False. |
| `configuration_status`, `selection_rationale`, `record_number_scope`, `validation` | `string` | Freeze status, development choice rationale, numbering boundary and completed checks. |

## `data/processed/annotation_pilot_multi_v2/annotator_A/` and `annotator_B/`

Generated by `python -m scripts.build_annotation_pool multi-pilot`. Each slot has one English Markdown batch for this $5$-question pilot. Future formal export remains pending. Views disclose algorithms and annotator identity, hide gold/scores/ranks/internal IDs/other labels, and contain no HTML or notes field. Two-way and three-way common pairs appear once, ordered by stable number; source-exclusive groups follow original algorithm rank. Each question stays within one batch of at most $20$ questions. Empty groups show `None`.

| Field | Type | Meaning |
| --- | --- | --- |
| `Annotator:` | `text` | Fill in name or agreed identifier; identities need not be anonymous. |
| `Question NNNN`, `Paper:` | `heading`, `text` | Sequential question number and real title, followed by quoted question. |
| `Common Retrieved Chunks`, `BM25`, `Dense`, `Hybrid` | `level-three headings` | One common group and three exclusive groups. |
| `Passage N`, `Relevance N` | `level-four headings` | One occurrence per unique pair and annotator. |
| `Retrieved by:` | `text` | All actual algorithm sources. |
| `Label:` | `blank, 0 or 1` | Initially blank; independently fill in only binary relevance. |

### Historical BM25 workflow

Track `data/raw/`, `data/processed/` and both guides together. GitHub Releases are not required. Preserve source license declarations, upstream revisions, generation parameters, evaluation scope and companion manifests. Git history records each published snapshot; use an exact commit to reproduce a version.

Rebuild changed outputs in a separate local staging directory, keeping canonical basenames. Regenerate dependent artifacts and manifests together, verify hashes and schemas, and document provenance, parameters, scope and changes in both guides before committing. Keep credentials, caches, model weights, indexes and personal notes outside the shared snapshot. Preserve hash-bound bytes through `.gitattributes`.

### Obtain the data

Clone the P3 working branch to a new directory:

```powershell
git clone --branch p3-qasper-foundation https://github.com/CodeByVish/papergap-rag.git
Set-Location papergap-rag
git rev-parse HEAD
```

For an exact version, check out its recorded commit in a clean checkout. The raw and processed files are under `data/` alongside their manifests. Verify hashes before use; never edit a JSONL without regenerating its manifest and dependent outputs. Use the artifact-specific commands below for local reproduction. No Release download or archive extraction is needed.

The all-splits mapping is a mechanical gold reference export. Use the saved question lists and usage audit below to determine eligibility; exporting or downloading all splits does not authorize tuning on held-out questions.

## Directory structure and build order

The tree lists canonical artifacts; the diagnostic report is optional and may be absent. `README_zh-CN.md`, `README.md` and the listed generated artifacts are tracked together.

```text
data/
├── README.md                                           # English guide / 英文指南
├── README_zh-CN.md                                     # Chinese guide / 中文指南
├── raw/                                                # Tracked source data / 纳入 Git 的源数据
│   └── qasper/
│       ├── manifest.json                               # Source metadata and hashes / 来源及哈希
│       ├── train.jsonl
│       ├── validation.jsonl
│       └── test.jsonl
└── processed/                                          # Tracked generated outputs / 纳入 Git 的生成产物
    ├── papers.jsonl
    ├── qa.jsonl
    ├── qasper_export.manifest.json
    ├── passages.jsonl
    ├── passages.manifest.json
    ├── paper_catalog.json
    ├── passages_all_paper_text.jsonl
    ├── passages_all_paper_text.manifest.json
    ├── gold_evidence_mapping_all_splits.jsonl
    ├── gold_evidence_mapping_all_splits.manifest.json
    ├── qa_for_choosing_chunk_size.jsonl
    ├── annotation_preparation.manifest.json
    ├── qa_for_held_out.jsonl
    ├── qa_for_held_out.manifest.json
    ├── qa_for_held_out_v2.jsonl
    ├── qa_for_held_out_v2.manifest.json
    ├── historical_bm25_retirement.manifest.json
    ├── annotation_pilot/
    ├── annotation_held_out/
    ├── sample_passages_100.jsonl
    ├── sample_passages_100.manifest.json
    └── qasper_inspection.json                          # Optional diagnostics / 可选诊断
```

Build order: raw acquisition → `papers.jsonl`, `qa.jsonl`, export manifest → development/all-paper-text corpora and sample → evidence mappings. Every file below has its own generation command and field table; repeated commands generate companion files together, so execute each distinct build only once.

The builders refuse existing output paths, except the optional inspector, which replaces its report. For rebuilds, use a new staging directory and pass its corresponding input/output paths throughout. The corpus and sample CLIs do not read YAML: their legacy defaults are $200/40$ words, so explicitly pass the selected $365/40$ settings. These are words, not model tokens.

Field tables use JSON types. Dotted paths and `[]` describe nested fields; `<split>` means `train`, `validation`, or `test`, and `<input>` is one of the named inputs. Source exports preserve additional original fields if present; tables describe the pinned QASPER source and current exporter, not a schema repair step.

## Raw QASPER acquisition

### Generation command

```powershell
python -m scripts.download_qasper --output-dir data/raw/qasper --revision fdc9d8214fbab5dd782958601db4d678e6934a54
```

The download maps upstream `dev` to local `validation`; `train` and `test` keep their names. Each raw JSONL line is a whole paper with `id`, `title`, `abstract`, `full_text`, `figures_and_tables`, and `qas`. `qas[]` has the question fields documented under `qa.jsonl`, without the added `paper_id` and `source_split`. The paper content fields match `papers.jsonl`, without `source_split`. Raw records are neither normalized nor chunked.

`--output-dir` is required. Existing destinations are rejected unless `--force` is supplied; `--force` replaces the whole verified acquisition with rollback, not an append/resume operation. The exact accepted directory contains only `manifest.json`, `train.jsonl`, `validation.jsonl`, and `test.jsonl`. The command needs network access to the Hugging Face Hub and official archives; QASPER is public and needs no Hugging Face token.

### Raw manifest fields

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | Manifest contract version. |
| `dataset` | `object` | Dataset ID/config, requested/resolved revision, source dataset version, local parser version. |
| `licenses` | `object` | Hub/source license declarations; retain on redistribution. |
| `repository_files` | `array<object>` | Byte counts and SHA-256 of pinned qasper.py and dataset_infos.json. |
| `splits` | `array<object>` | Split name, filename, rows, bytes, SHA-256 for each JSONL. |
| `source_verification` | `string` | Fixed verification contract identifier. |
| `source_archives` | `array<object>` | Official URLs, declared/observed bytes and hashes, required members. |
| `libraries` | `object` | Python and huggingface-hub runtime versions. |
| `output` | `object` | Encoding, newline, aggregate-hash algorithm and aggregate_sha256. |

Acquisition validates pinned `qasper.py` and `dataset_infos.json` as bytes, never executes remote code, and never uses `trust_remote_code`. Both official archives must match byte counts, SHA-256, and required members; they are not extracted to disk. Source, fingerprint, or schema changes fail closed. `--revision main` is for upstream checks, not team reproduction. The aggregate digest covers sorted JSONL relative paths and file hashes, excluding `manifest.json`. Raw JSONL uses UTF-8, LF, recursively sorted keys, and compact serialization; retain the manifest for reproduction.

## `data/processed/papers.jsonl`

One paper per row from every official split. Preserves all original top-level fields except qas and adds source_split. It is paper-only input for passage builders.

### Generation command

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `id` | `string` | Original paper identifier. |
| `title` | `string` | Original paper title. |
| `abstract` | `string` | Original abstract; retained but not currently indexed. |
| `full_text` | `array<object>` | Ordered source sections. |
| `full_text[].section_name` | `string or null` | Original section label; blank/null labels are dropped by the passage builder. |
| `full_text[].paragraphs` | `array<string>` | Original ordered paragraphs, before normalization. |
| `figures_and_tables` | `array<object>` | Original figure/table metadata; not currently indexed. |
| `figures_and_tables[].caption` | `string` | Original figure/table caption. |
| `figures_and_tables[].file` | `string` | Source figure/table file reference; not a bundled image. |
| `source_split` | `string` | Official split: train, validation, or test. |

## `data/processed/paper_catalog.json`

Lightweight metadata for loading the UI paper selector once. Build it after the selected passage corpus; the UI is not integrated yet. The command below uses `data.passages_path` in `configs/default.yaml`. Always pass the exact file used by UI retrieval through the required `--passages` option; if that corpus changes, rebuild the catalog into a new staging path and replace the local snapshot only after validation. Existing output paths are rejected.

### Generation command

```powershell
python -m scripts.build_paper_catalog --papers data/processed/papers.jsonl --passages data/processed/passages.jsonl --output data/processed/paper_catalog.json
```

Only papers and sections with passages appear. Paper IDs in the export and passage IDs in the corpus must be unique; every passage must have nonblank text and reference an exported paper and normalized source section. Papers retain export order; sections retain their first occurrence in `full_text`, with repeated normalized names merged because section filters use names. Section names follow passage normalization (LF line endings and trimmed outer whitespace). Missing/blank metadata strings become `null`, absent authors become `[]`; authors are never inferred. Here, retrievable means a passage exists, not that every query will return it.

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | Proposed catalog contract, `v0-proposed`. |
| `passages_file` | `string` | Exact `--passages` input path with forward slashes; relative paths are relative to the repository root when built there. UI retrieval must use the same corpus. |
| `papers` | `array<object>` | Selectable papers with at least one passage. |
| `papers[].paper_id` | `string` | Unique source paper ID. |
| `papers[].title` | `string or null` | Source title, or `null` when unavailable. |
| `papers[].authors` | `array<string or null>` | Available source authors; missing strings are `null`, missing author lists are empty. The current pinned QASPER export has no authors. |
| `papers[].passage_count` | `integer` | Total passage count for this paper in the selected corpus. |
| `papers[].sections` | `array<object>` | Only sections represented in the selected corpus, in source order. |
| `papers[].sections[].name` | `string or null` | Normalized source section name, or `null` when unavailable and represented by a null-section passage. The current builder drops unnamed sections. |
| `papers[].sections[].passage_count` | `integer` | Passage count for this paper and section name; section counts sum to the paper count. |

For local reproduction, first build `papers.jsonl` and the chosen passage corpus using their commands in this guide, then run the catalog command. For Git-based use, obtain the P3 snapshot as described above and retain the matching corpus with the catalog; rebuild the catalog locally if needed. The path records the selected file, not a content hash; rebuild after corpus replacement.

## `data/processed/qa.jsonl`

One original question per row, with every answer annotation. Includes every official split; paper_id and source_split are added without filtering source QA fields. Use paper_id to join papers, then evidence matching to recover passage IDs.

### Generation command

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `question_id` | `string` | Original question identifier. |
| `paper_id` | `string` | Foreign key to papers.jsonl:id. |
| `source_split` | `string` | Official provenance split; retained independently of evaluation roles. |
| `question` | `string` | Original question text. |
| `nlp_background` | `string` | Question author's NLP background. |
| `paper_read` | `string` | Source record of how much of the paper was read. |
| `question_writer` | `string` | Original question-writer identifier. |
| `search_query` | `string` | Original search query. |
| `topic_background` | `string` | Question author's topic background. |
| `answers` | `array<object>` | All alternative answer annotations; preserved independently. |
| `answers[].annotation_id` | `string` | Original annotation identifier. |
| `answers[].worker_id` | `string` | Original annotator metadata; not relevance supervision. |
| `answers[].answer` | `object` | Original answer payload. |
| `answers[].answer.evidence` | `array<string>` | Annotated evidence text, including possible FLOAT SELECTED markers. |
| `answers[].answer.extractive_spans` | `array<string>` | Extractive reference answer spans. |
| `answers[].answer.free_form_answer` | `string` | Free-form reference answer, possibly empty. |
| `answers[].answer.highlighted_evidence` | `array<string>` | Original highlighted evidence; not used for paragraph matching. |
| `answers[].answer.unanswerable` | `boolean` | Whether the question is marked unanswerable. |
| `answers[].answer.yes_no` | `boolean or null` | Yes/no reference answer, or null for another answer type. |

## `data/processed/qasper_export.manifest.json`

Generated alongside papers.jsonl and qa.jsonl, not in a separate build. Binds source and output hashes, split counts, and the proposed policy. Output filenames are basenames; keep all three export files together.

### Generation command

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | Manifest format version. |
| `artifact` | `string` | qasper_papers_and_qa. |
| `split_policy_version` | `string` | Proposed paper-disjoint split policy version. |
| `source` | `object` | Pinned upstream and export provenance. |
| `source.dataset_id` | `string` | allenai/qasper. |
| `source.resolved_revision` | `string` | Immutable full upstream commit SHA. |
| `source.local_parser_version` | `integer` | Local source parser version. |
| `source.source_manifest_sha256` | `string` | Hash of raw/qasper/manifest.json. |
| `source.split_files` | `object` | Input inventory keyed by train, validation, test. |
| `source.split_files.<split>.rows` | `integer` | Number of source paper rows. |
| `source.split_files.<split>.sha256` | `string` | Source split JSONL byte hash. |
| `split_counts` | `object` | Counts keyed by official split. |
| `split_counts.<split>.papers` | `integer` | Paper count. |
| `split_counts.<split>.questions` | `integer` | Question count. |
| `split_counts.<split>.answer_annotations` | `integer` | Answer annotation count. |
| `outputs` | `object` | Inventory of the two output JSONL files. |
| `outputs.<papers\|qa>.file` | `string` | Output basename; outputs share a directory. |
| `outputs.<papers\|qa>.rows` | `integer` | Output row count. |
| `outputs.<papers\|qa>.sha256` | `string` | Output SHA-256. |
| `outputs.qa.answer_annotation_count` | `integer` | Total answer annotations across all QA rows. |

## `data/processed/passages.jsonl`

Default development corpus used by configs/default.yaml:data.passages_path. Includes train and validation only. Current pinned 365/40 build contains 21,360 passages; manifests are authoritative for exact counts and hashes.

### Generation command

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `passage_id` | `string` | Opaque deterministic qasper-passage-v1- SHA-256 identifier. |
| `paper_id` | `string` | Source paper identifier. |
| `title` | `string` | Normalized paper title. |
| `section` | `string` | Normalized display section label; equal labels do not merge containers. |
| `chunk_number` | `integer` | Zero-based contiguous chunk index within one original source container. |
| `text` | `string` | Normalized full-text chunk; contains no QA supervision. |
| `previous_passage_id` | `string or null` | Direct predecessor in the same container; null at the start. |
| `next_passage_id` | `string or null` | Direct successor in the same container; null at the end. |

## `data/processed/passages.manifest.json`

Companion to passages.jsonl. scope=development, artifact=development_corpus, purpose=development. All official splits are recorded, including excluded test with zero emitted passages.

### Generation command

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | Manifest format version. |
| `artifact` | `string` | development_corpus or inference_corpus. |
| `purpose` | `string` | development or index_for_inference. |
| `scope` | `string` | development or all-paper-text. |
| `source` | `object` | Pinned upstream and export provenance. |
| `source.dataset_id` | `string` | allenai/qasper. |
| `source.resolved_revision` | `string` | Immutable full upstream commit SHA. |
| `source.local_parser_version` | `integer` | Local source parser version. |
| `source.export_papers_file` | `string` | Input paper-export basename. |
| `source.export_papers_sha256` | `string` | SHA-256 of exact paper-export bytes. |
| `source.source_splits` | `object` | Raw split inventory copied from export source.split_files. |
| `source.source_splits.<split>.rows` | `integer` | Original split paper count. |
| `source.source_splits.<split>.sha256` | `string` | Raw split byte hash. |
| `source.split_policy_version` | `string` | Proposed split policy version. |
| `source.split_counts` | `object` | Scope/count metadata keyed by split. |
| `source.split_counts.<split>.project_role` | `string` | development, validation, or held_out. |
| `source.split_counts.<split>.included_in_scope` | `boolean` | Whether the split was included. |
| `source.split_counts.<split>.source_paper_count` | `integer` | Paper count in the input export for this split. |
| `source.split_counts.<split>.passage_count` | `integer` | Generated passage count for this split. |
| `chunking` | `object` | Exact normalization/chunking settings. |
| `chunking.source_kinds` | `array<string>` | Currently full_text only. |
| `chunking.normalization_version` | `string` | Text-normalization implementation version. |
| `chunking.chunking_version` | `string` | Word-chunking implementation version. |
| `chunking.chunk_size_words` | `integer` | Maximum Unicode non-whitespace runs per chunk; selected value 365. |
| `chunking.chunk_overlap_words` | `integer` | Overlap in word runs; selected value 40. |
| `chunking.word_rule` | `string` | Definition of word counting. |
| `chunking.type_rule` | `string` | Casefolded word-type definition (corpus/mapping manifests). |
| `output` | `object` | Corpus inventory, counts, and rubric checks. |
| `output.file` | `string` | Corpus basename. |
| `output.sha256` | `string` | Exact corpus byte hash. |
| `output.scope` | `string` | Same scope as the top-level field. |
| `output.purpose` | `string` | Same purpose as the top-level field. |
| `output.source_paper_count` | `integer` | Input papers in the selected scope. |
| `output.indexed_paper_count` | `integer` | Papers emitting at least one passage. |
| `output.passage_count` | `integer` | Total passages. |
| `output.unique_passage_count` | `integer` | Distinct passage IDs. |
| `output.source_word_count` | `integer` | Source words counted once without chunk overlap duplication. |
| `output.passage_word_count` | `integer` | Words in emitted passages, including overlap. |
| `output.passage_word_type_count` | `integer` | Distinct casefolded passage word types. |
| `output.minimum_passages` | `integer` | Required minimum passage count. |
| `output.minimum_words` | `integer` | Required minimum word count. |
| `output.rubric_minimum_met` | `boolean` | Whether at least 10,000 passages and 100,000 words are met. |

## `data/processed/passages_all_paper_text.jsonl`

Includes train, validation, and test paper bodies for inference indexing. It contains no QA fields. Current pinned 365/40 build contains 28,617 passages; held-out paper inclusion does not permit supervision-based tuning.

### Generation command

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope all-paper-text --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages_all_paper_text.jsonl --manifest-output data/processed/passages_all_paper_text.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `passage_id` | `string` | Opaque deterministic qasper-passage-v1- SHA-256 identifier. |
| `paper_id` | `string` | Source paper identifier. |
| `title` | `string` | Normalized paper title. |
| `section` | `string` | Normalized display section label; equal labels do not merge containers. |
| `chunk_number` | `integer` | Zero-based contiguous chunk index within one original source container. |
| `text` | `string` | Normalized full-text chunk; contains no QA supervision. |
| `previous_passage_id` | `string or null` | Direct predecessor in the same container; null at the start. |
| `next_passage_id` | `string or null` | Direct successor in the same container; null at the end. |

## `data/processed/passages_all_paper_text.manifest.json`

Companion to passages_all_paper_text.jsonl. scope=all-paper-text, artifact=inference_corpus, purpose=index_for_inference. Records included paper bodies by source split; not a frozen question-pool manifest.

### Generation command

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope all-paper-text --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages_all_paper_text.jsonl --manifest-output data/processed/passages_all_paper_text.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | Manifest format version. |
| `artifact` | `string` | development_corpus or inference_corpus. |
| `purpose` | `string` | development or index_for_inference. |
| `scope` | `string` | development or all-paper-text. |
| `source` | `object` | Pinned upstream and export provenance. |
| `source.dataset_id` | `string` | allenai/qasper. |
| `source.resolved_revision` | `string` | Immutable full upstream commit SHA. |
| `source.local_parser_version` | `integer` | Local source parser version. |
| `source.export_papers_file` | `string` | Input paper-export basename. |
| `source.export_papers_sha256` | `string` | SHA-256 of exact paper-export bytes. |
| `source.source_splits` | `object` | Raw split inventory copied from export source.split_files. |
| `source.source_splits.<split>.rows` | `integer` | Original split paper count. |
| `source.source_splits.<split>.sha256` | `string` | Raw split byte hash. |
| `source.split_policy_version` | `string` | Proposed split policy version. |
| `source.split_counts` | `object` | Scope/count metadata keyed by split. |
| `source.split_counts.<split>.project_role` | `string` | development, validation, or held_out. |
| `source.split_counts.<split>.included_in_scope` | `boolean` | Whether the split was included. |
| `source.split_counts.<split>.source_paper_count` | `integer` | Paper count in the input export for this split. |
| `source.split_counts.<split>.passage_count` | `integer` | Generated passage count for this split. |
| `chunking` | `object` | Exact normalization/chunking settings. |
| `chunking.source_kinds` | `array<string>` | Currently full_text only. |
| `chunking.normalization_version` | `string` | Text-normalization implementation version. |
| `chunking.chunking_version` | `string` | Word-chunking implementation version. |
| `chunking.chunk_size_words` | `integer` | Maximum Unicode non-whitespace runs per chunk; selected value 365. |
| `chunking.chunk_overlap_words` | `integer` | Overlap in word runs; selected value 40. |
| `chunking.word_rule` | `string` | Definition of word counting. |
| `chunking.type_rule` | `string` | Casefolded word-type definition (corpus/mapping manifests). |
| `output` | `object` | Corpus inventory, counts, and rubric checks. |
| `output.file` | `string` | Corpus basename. |
| `output.sha256` | `string` | Exact corpus byte hash. |
| `output.scope` | `string` | Same scope as the top-level field. |
| `output.purpose` | `string` | Same purpose as the top-level field. |
| `output.source_paper_count` | `integer` | Input papers in the selected scope. |
| `output.indexed_paper_count` | `integer` | Papers emitting at least one passage. |
| `output.passage_count` | `integer` | Total passages. |
| `output.unique_passage_count` | `integer` | Distinct passage IDs. |
| `output.source_word_count` | `integer` | Source words counted once without chunk overlap duplication. |
| `output.passage_word_count` | `integer` | Words in emitted passages, including overlap. |
| `output.passage_word_type_count` | `integer` | Distinct casefolded passage word types. |
| `output.minimum_passages` | `integer` | Required minimum passage count. |
| `output.minimum_words` | `integer` | Required minimum word count. |
| `output.rubric_minimum_met` | `boolean` | Whether at least 10,000 passages and 100,000 words are met. |

## `data/processed/gold_evidence_mapping_all_splits.jsonl`

Full gold reference mapping across all official splits. Independent question lists and actual usage records determine evaluation roles; coverage alone neither freezes nor invalidates held-out status. The superseded development-only mapping and manifest have been removed.

### Generation command

```powershell
python -m scripts.export_evidence_mapping --scope all-splits-reference
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed. |
| `question_id` | `string` | Original question identifier. |
| `paper_id` | `string` | Source paper identifier. |
| `source_split` | `string` | Official source split. |
| `question` | `string` | Original question text. |
| `qa_metadata` | `object` | Other source QA fields; current exporter preserves them unchanged. |
| `qa_metadata.nlp_background` | `string` | Question author's NLP background. |
| `qa_metadata.paper_read` | `string` | Source record of how much of the paper was read. |
| `qa_metadata.question_writer` | `string` | Original question-writer identifier. |
| `qa_metadata.search_query` | `string` | Original search query. |
| `qa_metadata.topic_background` | `string` | Question author's topic background. |
| `annotations` | `array<object>` | Alternative answers retained separately with located evidence. |
| `annotations[].annotation_id` | `string` | Source annotation ID converted to string; answer-array index if absent. |
| `annotations[].worker_id` | `string (if present)` | Original worker metadata retained by the current exporter. |
| `annotations[].answer` | `object` | Original answer payload. |
| `annotations[].answer.evidence` | `array<string>` | Annotated evidence text, including possible FLOAT SELECTED markers. |
| `annotations[].answer.extractive_spans` | `array<string>` | Extractive reference answer spans. |
| `annotations[].answer.free_form_answer` | `string` | Free-form reference answer, possibly empty. |
| `annotations[].answer.highlighted_evidence` | `array<string>` | Original highlighted evidence; not used for paragraph matching. |
| `annotations[].answer.unanswerable` | `boolean` | Whether the question is marked unanswerable. |
| `annotations[].answer.yes_no` | `boolean or null` | Yes/no reference answer, or null for another answer type. |
| `annotations[].evidence_locations` | `array<string>` | Nonempty references to evidence_paragraphs[].location. |
| `evidence_paragraphs` | `array<object>` | Deduplicated source evidence paragraphs across answers. |
| `evidence_paragraphs[].location` | `string` | paper_id:section_index:paragraph_index reference. |
| `evidence_paragraphs[].section_index` | `integer` | Zero-based original full_text index. |
| `evidence_paragraphs[].paragraph_index` | `integer` | Zero-based original paragraphs index; blanks still count. |
| `evidence_paragraphs[].text` | `string` | Original evidence paragraph, preserving whitespace and line endings. |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | True for exported questions: matches jointly cover all non-whitespace characters. |
| `evidence_paragraphs[].passage_matches` | `array<object>` | All passages with non-whitespace overlap. |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | Exact identifier in the selected corpus. |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | Two half-open [start, end) Python character offsets in the original evidence paragraph; not bytes, tokens, or passage offsets. |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | Whether this passage alone covers all non-whitespace paragraph content. |
| `gold_passage_ids` | `array<string>` | Sorted unique IDs overlapping any annotated evidence; not manual relevance labels. |

A question is retained only if it has at least one answer and every answer has nonempty evidence uniquely located in whole full-text paragraphs, fully covered by the supplied corpus. Empty evidence, `FLOAT SELECTED`, missing paragraphs, duplicate-text ambiguity, or incomplete coverage excludes the entire question. Matching normalizes line endings and outer whitespace only; it uses no fuzzy or answer-substring matching. Compute coverage separately for alternative answers, without merging them. `gold_passage_ids` includes partial-overlap passages; an individual passage need not cover complete evidence. An unlisted passage is not automatically irrelevant. Keep questions, answers, evidence, and derived labels out of the retrieval corpus.

## `data/processed/gold_evidence_mapping_all_splits.manifest.json`

The all-splits mapping is a mechanical gold reference export. Use the saved question lists and usage audit below to determine eligibility; exporting or downloading all splits does not authorize tuning on held-out questions.

### Generation command

```powershell
python -m scripts.export_evidence_mapping --scope all-splits-reference
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed. |
| `split_policy_version` | `string` | Proposed split policy version. |
| `source_splits` | `array<string>` | Official splits selected for evidence mapping. |
| `scope` | `string` | development or all-splits-reference; absent in older development exports. |
| `evaluation_design` | `string` | Evaluation interpretation; absent in older development exports. |
| `chunking` | `object` | Exact normalization/chunking settings. |
| `chunking.source_kinds` | `array<string>` | Currently full_text only. |
| `chunking.normalization_version` | `string` | Text-normalization implementation version. |
| `chunking.chunking_version` | `string` | Word-chunking implementation version. |
| `chunking.chunk_size_words` | `integer` | Maximum Unicode non-whitespace runs per chunk; selected value 365. |
| `chunking.chunk_overlap_words` | `integer` | Overlap in word runs; selected value 40. |
| `chunking.word_rule` | `string` | Definition of word counting. |
| `chunking.type_rule` | `string` | Casefolded word-type definition (corpus/mapping manifests). |
| `inputs` | `object` | Hashes of papers, qa, export_manifest, passages, and passages_manifest. |
| `inputs.<input>.file` | `string` | Input basename. |
| `inputs.<input>.sha256` | `string` | Input byte hash. |
| `filtering_counts` | `object` | Question counts keyed by official split; zero categories can be absent. |
| `filtering_counts.<split>.total` | `integer` | Questions inspected. |
| `filtering_counts.<split>.eligible` | `integer` | Questions retained. |
| `filtering_counts.<split>.held_out_excluded` | `integer` | Questions excluded by development scope. |
| `filtering_counts.<split>.invalid_or_uncovered_answer_evidence` | `integer` | Questions rejected for missing, ambiguous, or incompletely covered evidence. |
| `mapping_rule` | `string` | Unique whole-paragraph evidence; every answer required. |
| `passage_match_rule` | `string` | Any non-whitespace overlap, with complete union coverage. |
| `offset_rule` | `string` | Zero-based half-open Python character offsets in evidence text. |
| `label_status` | `string` | Derived gold references, not human relevance labels. |
| `held_out_freeze` | `boolean` | False: not a final held-out freeze record. |
| `output` | `object` | Mapping output inventory. |
| `output.file` | `string` | Mapping JSONL basename. |
| `output.rows` | `integer` | Eligible question rows. |
| `output.sha256` | `string` | Exact mapping JSONL byte hash. |

## `data/processed/sample_passages_100.jsonl`

Deterministic dependency sample from train and validation only. Selects complete source containers by stable paper-ordered subset sum, allowing at most one container per paper and preferring more papers. Always exactly 100 passages; the pinned 365/40 sample has 100 papers and 20,017 passage words.

### Generation command

```powershell
python -m scripts.build_sample_passages --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/sample_passages_100.jsonl --manifest-output data/processed/sample_passages_100.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `passage_id` | `string` | Opaque deterministic qasper-passage-v1- SHA-256 identifier. |
| `paper_id` | `string` | Source paper identifier. |
| `title` | `string` | Normalized paper title. |
| `section` | `string` | Normalized display section label; equal labels do not merge containers. |
| `chunk_number` | `integer` | Zero-based contiguous chunk index within one original source container. |
| `text` | `string` | Normalized full-text chunk; contains no QA supervision. |
| `previous_passage_id` | `string or null` | Direct predecessor in the same container; null at the start. |
| `next_passage_id` | `string or null` | Direct successor in the same container; null at the end. |

## `data/processed/sample_passages_100.manifest.json`

Generated together with the sample. Records source hashes, normalization totals before selection, complete selected containers, and output hash. Sample neighbors remain complete because partial containers are never selected.

### Generation command

```powershell
python -m scripts.build_sample_passages --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/sample_passages_100.jsonl --manifest-output data/processed/sample_passages_100.manifest.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | Manifest format version. |
| `artifact` | `string` | sample_passages_100. |
| `source` | `object` | Pinned upstream and export provenance. |
| `source.dataset_id` | `string` | allenai/qasper. |
| `source.resolved_revision` | `string` | Immutable full upstream commit SHA. |
| `source.local_parser_version` | `integer` | Local source parser version. |
| `source.export_papers_file` | `string` | Input paper-export basename. |
| `source.export_papers_sha256` | `string` | SHA-256 of exact paper-export bytes. |
| `source.source_splits` | `array<object>` | Development source split inventory. |
| `source.source_splits[].name` | `string` | train or validation. |
| `source.source_splits[].project_role` | `string` | Proposed project role. |
| `source.source_splits[].input_paper_count` | `integer` | Input papers in the split. |
| `source.source_splits[].source_sha256` | `string` | Raw split SHA-256. |
| `normalization` | `object` | Counters across all examined development records, before sample selection. |
| `normalization.paragraphs_seen` | `integer` | Source paragraphs examined. |
| `normalization.paragraphs_emitted` | `integer` | Nonblank normalized paragraphs retained. |
| `normalization.blank_paragraphs_dropped` | `integer` | Blank paragraphs dropped. |
| `normalization.line_ending_replacements` | `integer` | CRLF/CR-to-LF replacements. |
| `normalization.outer_whitespace_trims` | `integer` | Outer-whitespace trim operations. |
| `normalization.sections_seen` | `integer` | Source sections examined. |
| `normalization.sections_emitted` | `integer` | Sections retained. |
| `normalization.blank_sections_dropped` | `integer` | Blank-name sections dropped. |
| `normalization.null_sections_dropped` | `integer` | Null-name sections dropped. |
| `normalization.empty_sections_dropped` | `integer` | Sections without usable paragraphs dropped. |
| `normalization.invalid_papers_dropped` | `integer` | Papers rejected by normalization. |
| `chunking` | `object` | Exact normalization/chunking settings. |
| `chunking.source_kinds` | `array<string>` | Currently full_text only. |
| `chunking.normalization_version` | `string` | Text-normalization implementation version. |
| `chunking.chunking_version` | `string` | Word-chunking implementation version. |
| `chunking.chunk_size_words` | `integer` | Maximum Unicode non-whitespace runs per chunk; selected value 365. |
| `chunking.chunk_overlap_words` | `integer` | Overlap in word runs; selected value 40. |
| `chunking.word_rule` | `string` | Definition of word counting. |
| `selection` | `object` | Deterministic complete-container selection metadata. |
| `selection.method` | `string` | Stable paper-ordered complete-container subset sum. |
| `selection.target_passage_count` | `integer` | Target passage count (100). |
| `selection.selected_container_count` | `integer` | Selected source-container count. |
| `selection.selected_paper_count` | `integer` | Selected distinct paper count. |
| `selection.selected_section_count` | `integer` | Selected distinct section count. |
| `selection.selected_groups` | `array<object>` | Complete selected source containers. |
| `selection.selected_groups[].source_split` | `string` | Official source split. |
| `selection.selected_groups[].project_role` | `string` | Proposed project role. |
| `selection.selected_groups[].paper_id` | `string` | Source paper identifier. |
| `selection.selected_groups[].source_kind` | `string` | full_text. |
| `selection.selected_groups[].section_index` | `integer` | Original zero-based section position. |
| `selection.selected_groups[].passage_count` | `integer` | Passages in this selected container. |
| `output` | `object` | Sample serialization and counts. |
| `output.file` | `string` | Sample basename. |
| `output.format` | `string` | jsonl. |
| `output.encoding` | `string` | utf-8. |
| `output.newline` | `string` | lf. |
| `output.passage_count` | `integer` | Total sample passages (100). |
| `output.unique_passage_count` | `integer` | Distinct passage IDs. |
| `output.unique_paper_count` | `integer` | Distinct source papers. |
| `output.passage_word_count` | `integer` | Emitted sample words, including overlap. |
| `output.sha256` | `string` | Exact sample byte hash. |

## `data/processed/qasper_inspection.json`

Optional offline diagnostic report; currently absent from the compact local layout. Checks exactly the four acquisition files, split hashes/rows, JSON parsing, and critical nested structure before reporting. Unlike other builders, it replaces an existing report. Source: src/data/qasper_inspection.py.

### Generation command

```powershell
python -m scripts.inspect_qasper --input-dir data/raw/qasper --output data/processed/qasper_inspection.json
```

### Field table

| Field name | JSON type | Meaning |
| --- | --- | --- |
| `provenance` | `object` | Pinned source metadata and input byte hashes. |
| `provenance.dataset_id` | `string` | Source dataset_id from the acquisition manifest. |
| `provenance.config` | `string` | Source config from the acquisition manifest. |
| `provenance.source_dataset_version` | `string` | Source source_dataset_version from the acquisition manifest. |
| `provenance.requested_revision` | `string` | Source requested_revision from the acquisition manifest. |
| `provenance.resolved_revision` | `string` | Source resolved_revision from the acquisition manifest. |
| `provenance.manifest_schema_version` | `integer` | Raw manifest format version. |
| `provenance.licenses` | `object` | Original source license declarations. |
| `provenance.input_files` | `object` | Input inventory keyed by split JSONL basename. |
| `provenance.input_files.<file>.bytes` | `integer` | Input byte count. |
| `provenance.input_files.<file>.rows` | `integer` | Input paper count. |
| `provenance.input_files.<file>.sha256` | `string` | Exact input byte hash. |
| `counting_definitions` | `object<string, string>` | Definitions for paper, question, annotation, paragraph, ID, and answer-type counts. |
| `per_split` | `object` | Detailed diagnostics keyed by official split. |
| `global_totals` | `object<string, integer>` | paper_count, question_count, answer_annotation_count, unique_paper_id_count, unique_question_id_count, chapter_count, paragraph_count, paragraph_string_count. |
| `field_anomalies` | `object` | Per-split and global field/category anomaly counters and example coordinates. |
| `section_anomalies` | `object` | Per-split and global field/category anomaly counters and example coordinates. |
| `question_anomalies` | `object` | Per-split and global field/category anomaly counters and example coordinates. |
| `answer_field_anomalies` | `object` | Per-split and global field/category anomaly counters and example coordinates. |
| `answer_types` | `object` | Per-split/global answer-type counts using the documented precedence. |
| `ambiguous_payload` | `object` | Per-split/global counts of ambiguous answer payloads. |
| `evidence` | `object` | Per-split/global evidence and highlighted-evidence diagnostics. |
| `duplicate_paragraphs` | `object` | same_paper and cross_paper duplicate summaries. |
| `duplicate_paragraphs.<scope>.duplicate_group_count` | `integer` | Repeated paragraph groups. |
| `duplicate_paragraphs.<scope>.involved_paragraph_count` | `integer` | Paragraph occurrences in repeated groups. |
| `duplicate_paragraphs.cross_paper.involved_paper_count` | `integer` | Distinct papers involved in cross-paper duplicates. |
| `duplicate_paragraphs.<scope>.examples` | `array<object>` | Bounded occurrence_count, paper_id_count, and locations examples. |
| `split_overlap` | `object` | Paper/question intersections and within-split duplicate IDs. |
| `split_overlap.paper_id_intersections` | `object<string, array<string>>` | Paper ID intersections for each split pair. |
| `split_overlap.question_id_intersections` | `object<string, array<string>>` | Question ID intersections for each split pair. |
| `split_overlap.within_split_duplicate_paper_ids` | `object<string, array<string>>` | Duplicate paper IDs keyed by split. |
| `split_overlap.observed_paper_disjoint` | `boolean` | True only if no within-split duplicates or cross-split paper intersections exist. |
| `open_decisions` | `array<string>` | Observed issues and decisions requiring review. |
| `per_split.<split>.paper_count` | `integer` | Paper rows. |
| `per_split.<split>.question_count` | `integer` | Questions. |
| `per_split.<split>.answer_annotation_count` | `integer` | Answer annotations. |
| `per_split.<split>.unique_paper_id_count` | `integer` | Unique nonblank paper IDs. |
| `per_split.<split>.duplicate_paper_id_count` | `integer` | Distinct duplicated paper IDs. |
| `per_split.<split>.unique_question_id_count` | `integer` | Unique nonblank question IDs. |
| `per_split.<split>.duplicate_question_id_count` | `integer` | Distinct duplicated question IDs. |
| `per_split.<split>.ambiguous_payload_count` | `integer` | Annotations with multiple valid answer payload types. |
| `per_split.<split>.duplicate_paper_id_values` | `array<string>` | Sorted duplicated paper identifiers. |
| `per_split.<split>.duplicate_question_id_values` | `array<string>` | Sorted duplicated question identifiers. |
| `per_split.<split>.question_annotation_count_stats` | `object` | min, median, max annotation counts per question. |
| `per_split.<split>.question_annotation_count_stats.<min\|median\|max>` | `number or null` | Summary count; null for no questions, median can be fractional. |
| `per_split.<split>.chapters` | `object` | Original section and paragraph statistics. |
| `per_split.<split>.chapters.chapter_count` | `integer` | Original full_text list items. |
| `per_split.<split>.chapters.paragraph_count` | `integer` | Original paragraph entries, including blanks/non-strings. |
| `per_split.<split>.chapters.paragraph_string_count` | `integer` | String-typed paragraph entries. |
| `per_split.<split>.chapters.anomalies` | `object` | Section field/category anomaly counters. |
| `per_split.<split>.field_anomalies` | `object` | Field/category anomaly counters for this split. |
| `per_split.<split>.question_anomalies` | `object` | Field/category anomaly counters for this split. |
| `per_split.<split>.answer_field_anomalies` | `object` | Field/category anomaly counters for this split. |
| `per_split.<split>.answer_types` | `object<string, integer>` | Counts of unanswerable, yes_no, extractive, free_form, invalid_or_empty. |
| `per_split.<split>.evidence` | `object` | evidence and highlighted_evidence diagnostics using the shared evidence-counter structure. |
| `<anomaly-counter>.<field>.<category>.count` | `integer` | Shared counter shape in anomaly blocks; observed category count. |
| `<anomaly-counter>.<field>.<category>.locations` | `array<object>` | At most ten stable diagnostic coordinates per category. |
| `<location>.split` | `string` | Official split at a diagnostic location. |
| `<location>.paper_id` | `string or null` | Paper identifier, or null when malformed. |
| `<location>.line_number` | `integer` | One-based JSONL source line. |
| `<location>.<section_index\|paragraph_index\|question_index\|answer_index>` | `integer (when present)` | Zero-based source-array index appropriate to the anomaly. |
| `<location>.<question_id\|field>` | `string or null (when present)` | Question identifier or affected field, when applicable. |
| `<evidence-counter>.total_items` | `integer` | All evidence items. |
| `<evidence-counter>.blank_items` | `integer` | Blank evidence strings. |
| `<evidence-counter>.non_string_items` | `integer` | Non-string evidence items. |
| `<evidence-counter>.annotations_with_items` | `integer` | Annotations containing evidence items. |
| `<evidence-counter>.float_selected_hits` | `integer` | FLOAT SELECTED prefix matches. |
| `<evidence-counter>.hit_paper_count` | `integer` | Papers containing prefix hits. |
| `<evidence-counter>.figures_and_tables_items_in_hit_papers` | `integer` | Total figure/table entries in hit papers; not inferred evidence mappings. |
| `<evidence-counter>.float_selected_prefix_forms` | `array<string>` | Observed distinct prefix forms. |
| `<evidence-counter>.anomaly_locations` | `object<string, array<object>>` | Bounded coordinates keyed by evidence anomaly category. |

`<anomaly-counter>` and `<evidence-counter>` describe reused diagnostic object shapes, not literal top-level keys; the same shapes appear in per-split and global summaries. Categories, field names, and optional coordinates depend on observations. Counting definitions and examples are generated by the inspector without question, answer, or evidence text.

## Passage ID contract

The passage ID is an opaque, deterministic identifier. Its public constructor is `make_passage_id(*, context, paper_id, source_kind, section_index, chunk_index) -> str` from `src/data/passage_ids.py`; callers must provide every argument explicitly.

The immutable context is `PassageIdContext(dataset_id, resolved_revision, local_parser_version, normalization_version, chunking_version, chunk_size_words, chunk_overlap_words)`. Production QASPER configuration uses `dataset_id="allenai/qasper"`, a full lowercase 40-character `resolved_revision`, positive integer `local_parser_version`, non-empty version strings, positive `chunk_size_words`, and `0 <= chunk_overlap_words < chunk_size_words`.

The canonical payload has exactly four top-level keys: `scheme`, `dataset`, `transform`, and `coordinate`. `dataset` contains `dataset_id`, `resolved_revision`, and `local_parser_version`; `transform` contains `normalization_version`, `chunking_version`, `chunk_size_words`, and `chunk_overlap_words`; `coordinate` contains `paper_id`, `source_kind`, `section_index`, and `chunk_index`. The implementation serializes this payload with UTF-8 `json.dumps(..., ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)` and hashes the complete bytes with SHA-256.

The final format is `qasper-passage-v1-<64 lowercase hex characters>`. `qasper-passage-v1` is `PASSAGE_ID_SCHEME_VERSION`; the digest is not truncated. Consumers must treat the value as opaque and read metadata from the `Passage` record or corpus manifest instead of parsing the ID.

P2 uses `passage_id` for duplicate removal, P5 uses it for citations, and `previous_passage_id`/`next_passage_id` use the same generated values for neighboring links. The ID function itself does not query or validate other records.

`section_index` is the zero-based position of the source container before filtering empty or unselected containers. `chunk_index` is the zero-based position emitted by the deterministic chunker within that source container. The allowed `source_kind` values are `full_text`, `abstract`, and `figure_table`; `full_text` and `figure_table` use their source-list positions, while `abstract` uses index `0`. The allowed source kinds reserve unambiguous ID coordinates; only source types approved by the team may generate passages.

The ID includes the immutable source revision, parser version, normalization version, chunking version, chunk configuration, paper ID, source kind, and source coordinates. It excludes display titles, section names, passage text, source split, output order, file paths, run time, and machine state. Therefore, `source_split` is not part of passage identity; the corpus manifest and output hash identify the complete generated collection.

Any normalization or chunking change that can alter passage bytes must increment its version string. Changes to the canonical payload, field meanings, hash method, or output prefix require a new `PASSAGE_ID_SCHEME_VERSION`; old and new IDs are not assumed compatible. The passage ID function does not generate passages, choose abstract or figure/table indexing policy, fill neighbor links, or map evidence.

For a synthetic context with `paper_id="paper-a"`, `source_kind="full_text"`, `section_index=2`, and `chunk_index=3`, the resulting ID is `qasper-passage-v1-fe1214d2ab869911e267500cd9b8903dc8e3d4d1e66bde218d0bcc938da8c6ee`.

## Passage sequence contract

The passage sequence contract is `v0-proposed` and defines the public meaning of `chunk_number` and the two neighbor fields without adding deferred provenance fields to `Passage`; the provenance-field question is tracked as `P3-D001` and remains pending team review.

`chunk_number` is equal to the `chunk_index` passed to `make_passage_id`. It is a zero-based, contiguous position within one source-container sequence, so a sequence containing $N$ passages must have exactly the positions `0..N-1`. The sequence boundary is the internal coordinate `(paper_id, source_kind, section_index)`, and numbering resets to `0` at every boundary. For `source_kind="full_text"`, every original `full_text[section_index]` is a separate sequence; `abstract` and each `figure_table` container follow the same rule if those source kinds are approved for indexing.

`previous_passage_id` and `next_passage_id` refer only to the direct predecessor and successor after ordering by `chunk_number` within the same source-container sequence. Non-null links must point to an existing passage and be mutual reverse links. A source container that is blank, invalid, or not approved produces no records; the builder must not create holes, renumber silently, or link around a missing passage. The public model does not attempt to validate these collection-level conditions because `source_kind` and `section_index` are internal construction coordinates.

At sequence boundaries, the missing neighbor is Python `None` and serializes as an explicit JSON `null`. Empty strings, missing keys, sentinel values, self-links, dangling IDs, and cross-container links are invalid representations of a missing neighbor.

The following synthetic examples illustrate the contract:

1. A three-passage sequence in one source container uses `0 -> 1 -> 2`; the first record has `previous_passage_id=null`, and the last has `next_passage_id=null`.
2. When the next `full_text` section begins, its first passage restarts at `chunk_number=0`; the last passage of the previous section and the first passage of the next section both have `null` at their respective outer boundaries.
3. A single-passage source container has `chunk_number=0`, `previous_passage_id=null`, and `next_passage_id=null`.
4. Two source containers may display the same `section` string, but their records remain separate sequences and must not link to one another; each sequence starts at `0` and uses `null` at its own boundaries.

This contract does not decide whether abstract or figure/table containers will actually be indexed, nor how `FLOAT SELECTED` evidence will map to figure/table passages. These open questions are tracked as `P3-D002` and `P3-D003`.

## Passage chunk-boundary contract

The `Passage` chunk-boundary contract is `v0-proposed`. Every passage must be produced from exactly one internal source container identified by `(paper_id, source_kind, section_index)`. The normalized `text` may contain multiple source paragraphs only when they belong to that same container and remain in their original order.

A change in `paper_id` is always a hard boundary. Different `source_kind` values are also isolated and must never be merged. For `source_kind="full_text"`, each original `full_text[section_index]` list item is a separate source container, even when adjacent list items have the same display title. If the team later approves `abstract` or `figure_table` indexing, the abstract container and every individual figure/table container remain separate boundaries as well.

The initial rule does not infer relatedness from section-title text, semantic similarity, or title hierarchy. A missing or blank title does not relax the boundary, and equal titles do not merge containers. A word chunker may combine source paragraphs in their original order within one source container, but it must not join the final text of one container to the first text of another to reach a target size. Retrieval should return multiple passages when cross-section context is needed.

This chunk boundary is stricter than the item 3 adjacency boundary, although both use the same internal coordinate. Chunking decides which source text may enter one passage; adjacency decides which already-created passages may receive direct neighbor links. Neither rule may be inferred from output-file order or the display value of `section`.

Step 5 must enforce this contract through a builder interface that accepts one source container together with its `(paper_id, source_kind, section_index)` coordinate, preserves paragraph order, and then invokes the word-level chunker. Callers must not pass a string assembled from multiple source containers. Step 7 must add collection-level negative tests using synthetic records with two papers, two sections, repeated section titles, and blank section titles to prove that no output passage crosses a hard boundary. The single-record `Passage` model only declares the text-source precondition; it cannot verify these internal coordinates.

Whether abstract or figure/table containers will actually be indexed remains a team decision. This contract also does not define `FLOAT SELECTED` evidence mapping; the mapping remains `P3-D003` pending team review.

## Normalization and chunking contract

The implementation is in `src/data/chunking.py`. The selected Week 3 configuration in `configs/default.yaml` is `normalization_version="text-normalization-v1"`, `chunking_version="word-chunking-v1"`, `chunk_words=365`, and `overlap_words=40`. These are words, not tokens. Valid Round 1–4 experiments selected this working setting for BM25; the evidence, selection rationale, and limitations are in [the experiment criteria](../experiments/chunk_size/criteria.md) and [Chinese criteria](../experiments/chunk_size/criteria_zn-CN.md). It is not a demonstrated stable optimum or a validated dense/hybrid/reranker setting. The configuration, passage schema, and split policy remain `v0-proposed` pending team confirmation.

The corpus and sample builders do not read `configs/default.yaml`; their legacy CLI defaults remain $200/40$. Always pass `--chunk-size-words 365 --chunk-overlap-words 40` as shown in the file sections above to reproduce the selected corpus. Chunk size and overlap are included in passage identity, so rebuilding changes passage IDs; consumers must rebuild dependent indexes and refresh saved passage references.

Normalization is deliberately conservative. For each source paragraph, the builder replaces CRLF and lone CR line endings with LF, removes only leading and trailing Unicode whitespace, drops paragraphs that become empty, and leaves internal whitespace, punctuation, casing, Unicode content, paragraph order, and evidence-marker text unchanged. Section names and paper titles receive the same line-ending and outer-whitespace treatment; a blank or `null` section name is dropped rather than replaced with a guessed label, and a blank paper title causes that paper to produce no passages. The returned `NormalizationReport` records paragraph and section counts, dropped blanks or `null` section names, line-ending replacements, outer-whitespace trims, and invalid-paper drops so a corpus manifest can preserve the observed transformations.

The word rule is the number of Unicode-aware non-whitespace runs matched by `\\S+`. A chunk window contains at most `chunk_size_words` runs; the next window starts `chunk_size_words - chunk_overlap_words` runs later. Chunk text is the original normalized character span from the first selected run through the last selected run, so internal whitespace and punctuation are not reconstructed or collapsed. Paragraphs are joined only with an internal LF-LF separator inside one source container, and the private build result retains the original paragraph indices touched by each chunk.

`build_passages_from_record` reads only `id`, `title`, and `full_text`. It never reads `qas`, answers, evidence, highlighted evidence, or figure/table metadata. Each original `full_text[section_index]` is processed independently, including sections with repeated display names; blank section names are dropped. Empty sections do not cause later sections to be renumbered: the original `section_index` remains in the passage ID coordinate. The current public record builder generates `full_text` passages only; abstract and figure/table sources remain deferred team decisions.

`build_passages_from_records` produces a deterministic order by `paper_id`, source kind, original section index, and chunk index. The private coordinate is `(paper_id, source_kind, section_index, chunk_index)`, while the public `Passage` remains the eight-field contract. Neighbor links are filled only within one `(paper_id, source_kind, section_index)` sequence, and `validate_built_passages` rejects duplicate IDs, empty text, missing chunk numbers, dangling links, and non-mutual or cross-container adjacency. The builder never infers boundaries from output order or display section names.

## Question-level held-out policy

The Week 4 annotation workflow uses question-level isolation across all official splits, permits shared papers, and excludes all recorded experimental questions. The legacy official-split mapping in `src/data/split_policy.py` remains `v0-proposed` for earlier chunk-size experiments; it does not select this annotation pool. Never index QA supervision; retrieval receives only paper text and the saved query. The pool freeze does not establish that downstream generator or agent settings have been frozen.

## Validation and reference snapshot

Run the following independent checks after extracting a package or rebuilding its companion files:

```powershell
python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages.jsonl --manifest data/processed/passages.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages_all_paper_text.jsonl --manifest data/processed/passages_all_paper_text.manifest.json
git check-ignore -v data/raw/qasper/manifest.json data/processed/papers.jsonl
```

The corpus checker validates the published corpus and manifest without requiring raw/export inputs. Builders enforce at least $10{,}000$ passages and $100{,}000$ source words (and sufficient emitted words). Evidence export checks its paper/QA inputs, hashes, corpus scope and configuration, then rebuilds passages to verify exact IDs/text before mapping. There is no separate evidence-mapping checker CLI; do not mistake the QA checker for an evidence-mapping validator.

The following is the pinned $365/40$ reference snapshot tracked in Git. Changed artifacts require updated companion manifests. The export contains $1{,}585$ papers, $5{,}049$ questions, and $7{,}993$ answer annotations; question counts are $2{,}593$ train, $1{,}005$ validation, and $1{,}451$ test.

| Corpus | Source papers | Indexed papers | Passages | Source words | Passage words | Casefolded word types |
| --- | --- | --- | --- | --- | --- | --- |
| Development | $1{,}169$ | $1{,}168$ | $21{,}360$ | $4{,}262{,}446$ | $4{,}469{,}326$ | $174{,}636$ |
| All paper text | $1{,}585$ | $1{,}584$ | $28{,}617$ | $5{,}659{,}921$ | $5{,}930{,}961$ | $210{,}909$ |

All-paper-text passage counts are $16{,}457$ train, $4{,}903$ validation, and $7{,}257$ test. Word counts use Unicode non-whitespace runs; source words exclude duplicated chunk overlap.

| Artifact | Expected SHA-256 |
| --- | --- |
| `passages.jsonl` | `ecb1c601cdaebcd8e1e6bfeaf43f9cb4867f89e9762799ab06e7901549a9e403` |
| `passages_all_paper_text.jsonl` | `8eeef0119e322fc9253255e2c6db6cb38ec276d7ebf3669dd28a856a636aa93e` |
| `sample_passages_100.jsonl` | `b3343a793f7428ad796bff83a79f8bd70528a89cd9d099d978fe69727ec0fa2c` |

To read raw splits locally with the optional `datasets` package:

```python
import datasets

dataset = datasets.load_dataset(
    "json",
    data_files={
        "train": "data/raw/qasper/train.jsonl",
        "validation": "data/raw/qasper/validation.jsonl",
        "test": "data/raw/qasper/test.jsonl",
    },
)
```

This is a local JSON loader, not a Hub acquisition or passage builder. Source records are still paper-level. Keep raw files, generated corpora, manifests, source archives, caches, and staging directories outside Git. Remove local outputs only when no longer needed and after satisfying experiment-retention requirements.

## Historical BM25 annotation-pool reproduction and use

This section and the original `qa_for_held_out` / `annotation_held_out` field tables below describe the retired BM25 version. Its commands are historical; the retirement marker blocks legacy freeze/formal export. Use the independent `v2` commands above for current question-list reproduction. Formal common-pool retrieval/export is pending.

The legacy `--scope all-splits-testing` spelling remains an alias for `all-splits-reference`; it no longer implies a waiver of held-out status. The optional development exporter remains available under explicit `--scope development` with separate `gold_evidence_mapping_development` basenames; that artifact is not retained in this data package. The current draw had $3{,}077$ eligible IDs after excluding $251$ gold-mapped prior-use questions and $1$ paper with fewer than $5$ passages; $2$ other audited used IDs were absent from the gold map. The selected provenance counts are $95$ train, $40$ validation and $65$ test.

Run the four commands in the order documented below: `prepare`, `pilot`, `freeze`, `export`. Inputs are the verified $365/40$ all-paper corpus, all-splits gold mapping, original exports, saved fourth-round questions and all local experiment usage records. Existing outputs are rejected. Preserve the saved historical questions and audit records with a reproducibility package; do not regenerate them from seeds. The CLI runs from the repository root and ignores YAML retrieval settings.

The seed $20261028$ and sampling rule are fixed before sampling. Do not inspect held-out content to debug, tune or change the system. The local audit excludes $253$ used IDs, including $3$ outside the $250$ selection questions; it cannot establish unrecorded external use. The verified output contains $200$ questions and $1{,}000$ unique pairs. Two blank Markdown sets supply $2{,}000$ future independent judgments; no labels or agreement have been collected yet. Keep this pool configuration unchanged throughout evaluation.

For Git-based use, obtain the P3 snapshot as described above and retain every companion manifest and the matching corpus/question lists. For local reproduction, build the original exports, all-paper corpus and all-splits references first, restore the exact historical experiment artifacts, then run the four stages into unused paths. `--data`, `--history`, `--pilot` and `--output` select locations; `--data` must preserve canonical input basenames. Archive completed inputs before any later rebuild. Distribution should include only each annotator's Markdown batches; annotators must not inspect the repository's JSONL verification files or gold references.

## `data/processed/qa_for_choosing_chunk_size.jsonl`

All $250$ saved fourth-round selection questions, in persisted order with original text; never reconstructed from a seed.

```powershell
python -m scripts.build_annotation_pool prepare
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `question_id` | `string` | Original unique question ID. |
| `paper_id` | `string` | Original paper ID; shared papers are allowed. |
| `question` | `string` | Unmodified source question text. |
| `source_split` | `string` | Official provenance, not the evaluation role. |

## `data/processed/annotation_preparation.manifest.json`

Preparation provenance and usage audit, including invalidated runs.

```powershell
python -m scripts.build_annotation_pool prepare
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed. |
| `inputs` | `object<string,string>` | Input path to exact SHA-256 digest mapping. |
| `inputs.<path>` | `string` | Hash of that input file's bytes. |
| `settings` | `object` | Frozen corpus and retrieval configuration. |
| `settings.chunk_size_words` | `integer` | $365$ words. |
| `settings.chunk_overlap_words` | `integer` | $40$ words. |
| `settings.top_k` | `integer` | Five distinct passages per question. |
| `usage_audit` | `array<object>` | Every persisted local results manifest/question list. |
| `usage_audit[].file` | `string` | Audited path. |
| `usage_audit[].sha256` | `string` | Audited file hash. |
| `usage_audit[].question_ids` | `array<string>` | Queries exposed in that run. |
| `excluded_question_ids` | `array<string>` | Union of all recorded used queries and selection queries. |
| `audit_scope` | `string` | Local persisted records only; external unrecorded use is unknown. |
| `seed` | `integer` | Predeclared 20261028. |
| `sampling_rule` | `string` | Sorted IDs, seeded simple random sampling without replacement; preserve draw order. |
| `scope` | `array<string>` | All three official splits. |
| `isolation` | `string` | Question-level; shared papers allowed. |

## `data/processed/qa_for_held_out.jsonl`

The saved $200$-question draw after the successful development pilot; formal export must use this file without resampling.

```powershell
python -m scripts.build_annotation_pool freeze
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `question_id` | `string` | Original unique question ID. |
| `paper_id` | `string` | Original paper ID; shared papers are allowed. |
| `question` | `string` | Unmodified source question text. |
| `source_split` | `string` | Official provenance, not the evaluation role. |

## `data/processed/qa_for_held_out.manifest.json`

Frozen question list and pool configuration; this does not freeze future generator, agent or prompt settings.

```powershell
python -m scripts.build_annotation_pool freeze
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed. |
| `purpose` | `string` | held-out question list. |
| `inputs` | `object<string,string>` | Input path to exact SHA-256 digest mapping. |
| `inputs.<path>` | `string` | Hash of that input file's bytes. |
| `settings` | `object` | Frozen corpus and retrieval configuration. |
| `settings.chunk_size_words` | `integer` | $365$ words. |
| `settings.chunk_overlap_words` | `integer` | $40$ words. |
| `settings.top_k` | `integer` | Five distinct passages per question. |
| `code` | `object` | Code identity, including dirty changes. |
| `code.commit` | `string` | Git HEAD at execution time. |
| `code.python` | `string` | Python runtime version. |
| `code.working_tree_status` | `array<string>` | Git short status; the run may use uncommitted code. |
| `code.source_sha256` | `object<string,string>` | Exact hashes of all src/scripts Python files. |
| `code.source_sha256.<path>` | `string` | Source-byte SHA-256, checked at export. |
| `retriever` | `object` | Metadata from the maintained P1/P2 adapter. |
| `retriever.id` | `string` | p1-p2-static-retrieval adapter. |
| `retriever.mode` | `string` | bm25. |
| `retriever.source_commit` | `string` | Upstream adapter integration commit; actual code is identified separately. |
| `retriever.packages` | `object<string,string or null>` | Active package versions. |
| `retriever.packages.<package>` | `string or null` | Installed package version, null if unavailable. |
| `retriever.scope` | `string` | Selected paper only. |
| `retriever.persistent_score_cache` | `boolean` | False; no persisted score cache. |
| `retriever.score` | `string` | Raw BM25 score. |
| `retriever.tie_break` | `string` | Stable upstream ranking tie rule. |
| `retriever.bm25` | `object` | Active sparse retriever settings. |
| `retriever.bm25.enabled` | `boolean` | True. |
| `retriever.bm25.tokenizer` | `string` | Casefold and Unicode word runs. |
| `retriever.bm25.k1` | `number` | 1.5. |
| `retriever.bm25.b` | `number` | 0.75. |
| `retriever.bm25.epsilon` | `number` | 0.25. |
| `retriever.dense` | `object` | Disabled dense component. |
| `retriever.dense.enabled` | `boolean` | False; dense retrieval is disabled. |
| `retriever.reranker` | `object` | Disabled reranker component. |
| `retriever.reranker.enabled` | `boolean` | False; reranking is disabled. |
| `seed` | `integer` | 20261028. |
| `sampling_rule` | `string` | Exact predeclared sampling procedure. |
| `scope` | `array<string>` | train, validation and test. |
| `isolation` | `string` | Question-level with shared papers allowed. |
| `eligible_question_ids` | `array<string>` | Sorted IDs before the draw; at least five passages per paper. |
| `excluded` | `object<string,string>` | Mapping of gold-mapped question IDs to exclusion reasons. |
| `excluded.<question_id>` | `string` | Prior use or fewer than five passages. |
| `prior_usage_excluded_question_ids` | `array<string>` | All used IDs, even when absent from gold references. |
| `question_ids` | `array<string>` | Exact final draw order. |
| `source_split_counts` | `object<string,integer>` | Draw counts by official split. |
| `source_split_counts.<split>` | `integer` | Number of selected queries from this split. |
| `usage_boundary` | `string` | No tuning or development based on held-out supervision/results. |

## `data/processed/annotation_pilot/pairs.jsonl`

First $5$ development questions only, $25$ pairs. JSONL is the structured source; internal IDs support joins only.

```powershell
python -m scripts.build_annotation_pool pilot
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `record_number` | `integer` | Stable global number, 1 through 1,000 for the formal pool. |
| `question_id` | `string` | Original unique question ID. |
| `paper_id` | `string` | Original paper ID; shared papers are allowed. |
| `question` | `string` | Unmodified source question text. |
| `passage_id` | `string` | Exact corpus passage ID. |
| `paper_title` | `string` | Real full paper title. |
| `passage` | `string` | Complete original retrieved passage text. |
| `label` | `null or integer` | Initially null; later human 0/1 labels must be associated by stable number and annotator. |

## `data/processed/annotation_pilot/verification.jsonl`

Private verification only; do not distribute to annotators.

```powershell
python -m scripts.build_annotation_pool pilot
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `record_number` | `integer` | Stable global number, 1 through 1,000 for the formal pool. |
| `question_id` | `string` | Original unique question ID. |
| `paper_id` | `string` | Original paper ID; shared papers are allowed. |
| `question` | `string` | Unmodified source question text. |
| `passage_id` | `string` | Exact corpus passage ID. |
| `paper_title` | `string` | Real full paper title. |
| `passage` | `string` | Complete original retrieved passage text. |
| `label` | `null or integer` | Initially null; later human 0/1 labels must be associated by stable number and annotator. |
| `retrieval_method` | `string` | bm25; verification file only. |
| `rank` | `integer` | Original one-based retrieval rank. |
| `score` | `number` | Raw retrieval score. |
| `gold_passage_ids` | `array<string>` | Reference evidence-overlapping IDs, not human labels. |
| `gold_evidence_match` | `boolean` | Whether this passage overlaps a mapped gold paragraph. |
| `evidence_paragraphs` | `array<object>` | Reference evidence, joined after retrieval. |
| `evidence_paragraphs[].location` | `string` | Original source paragraph coordinate. |
| `evidence_paragraphs[].section_index` | `integer` | Original zero-based section index. |
| `evidence_paragraphs[].paragraph_index` | `integer` | Original zero-based paragraph index. |
| `evidence_paragraphs[].text` | `string` | Reference paragraph text. |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | Full non-whitespace union coverage. |
| `evidence_paragraphs[].passage_matches` | `array<object>` | Overlapping corpus passages. |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | Exact matching corpus passage ID. |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | Half-open character interval [start,end).  |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | Whether one passage covers the full paragraph. |

## `data/processed/annotation_pilot/manifest.json`

Exact inputs, code, configuration and every output hash.

```powershell
python -m scripts.build_annotation_pool pilot
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed. |
| `purpose` | `string` | development pilot or held-out annotation pool. |
| `question_count` | `integer` | Five in pilot; 200 in formal pool. |
| `pair_count` | `integer` | 25 in pilot; 1,000 in formal pool. |
| `question_ids` | `array<string>` | Persisted query order. |
| `inputs` | `object<string,string>` | Input path to exact SHA-256 digest mapping. |
| `inputs.<path>` | `string` | Hash of that input file's bytes. |
| `settings` | `object` | Frozen corpus and retrieval configuration. |
| `settings.chunk_size_words` | `integer` | $365$ words. |
| `settings.chunk_overlap_words` | `integer` | $40$ words. |
| `settings.top_k` | `integer` | Five distinct passages per question. |
| `code` | `object` | Code identity, including dirty changes. |
| `code.commit` | `string` | Git HEAD at execution time. |
| `code.python` | `string` | Python runtime version. |
| `code.working_tree_status` | `array<string>` | Git short status; the run may use uncommitted code. |
| `code.source_sha256` | `object<string,string>` | Exact hashes of all src/scripts Python files. |
| `code.source_sha256.<path>` | `string` | Source-byte SHA-256, checked at export. |
| `retriever` | `object` | Metadata from the maintained P1/P2 adapter. |
| `retriever.id` | `string` | p1-p2-static-retrieval adapter. |
| `retriever.mode` | `string` | bm25. |
| `retriever.source_commit` | `string` | Upstream adapter integration commit; actual code is identified separately. |
| `retriever.packages` | `object<string,string or null>` | Active package versions. |
| `retriever.packages.<package>` | `string or null` | Installed package version, null if unavailable. |
| `retriever.scope` | `string` | Selected paper only. |
| `retriever.persistent_score_cache` | `boolean` | False; no persisted score cache. |
| `retriever.score` | `string` | Raw BM25 score. |
| `retriever.tie_break` | `string` | Stable upstream ranking tie rule. |
| `retriever.bm25` | `object` | Active sparse retriever settings. |
| `retriever.bm25.enabled` | `boolean` | True. |
| `retriever.bm25.tokenizer` | `string` | Casefold and Unicode word runs. |
| `retriever.bm25.k1` | `number` | 1.5. |
| `retriever.bm25.b` | `number` | 0.75. |
| `retriever.bm25.epsilon` | `number` | 0.25. |
| `retriever.dense` | `object` | Disabled dense component. |
| `retriever.dense.enabled` | `boolean` | False; dense retrieval is disabled. |
| `retriever.reranker` | `object` | Disabled reranker component. |
| `retriever.reranker.enabled` | `boolean` | False; reranking is disabled. |
| `freeze_manifest_sha256` | `string or null` | Exact held-out freeze hash; null in pilot. |
| `outputs` | `object<string,string>` | Output paths mapped to SHA-256; excludes the manifest itself. |
| `outputs.<path>` | `string` | Exact output byte hash, including blind Markdown. |
| `validation` | `string` | Completed invariant checks. |

## `data/processed/annotation_pilot/annotator_A/ and annotator_B/`

Two independent English Markdown views; each formal set has $10$ batches of $20$ questions / $100$ pairs. No HTML, notes, internal IDs, gold, retrieval method or score. Assign each record's two views to different people.

```powershell
python -m scripts.build_annotation_pool pilot
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `Annotator:` | `text` | Fill in the actual annotator identifier before collection. |
| `Record NNNN` | `heading` | Global record_number mapping; never edit. |
| `Paper:` | `text` | Real full title without internal IDs. |
| `Question / Passage` | `quoted text` | Original content; do not edit. |
| `Relevance / Label:` | `blank, 0 or 1` | Fill in only Label: 0 or Label: 1; retain all record numbers. |

## `data/processed/annotation_held_out/pairs.jsonl`

Formal $200$ questions and $1{,}000$ pairs; five records per question remain adjacent in fixed order. JSONL is the structured source; internal IDs support joins only.

```powershell
python -m scripts.build_annotation_pool export
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `record_number` | `integer` | Stable global number, 1 through 1,000 for the formal pool. |
| `question_id` | `string` | Original unique question ID. |
| `paper_id` | `string` | Original paper ID; shared papers are allowed. |
| `question` | `string` | Unmodified source question text. |
| `passage_id` | `string` | Exact corpus passage ID. |
| `paper_title` | `string` | Real full paper title. |
| `passage` | `string` | Complete original retrieved passage text. |
| `label` | `null or integer` | Initially null; later human 0/1 labels must be associated by stable number and annotator. |

## `data/processed/annotation_held_out/verification.jsonl`

Private verification only; do not distribute to annotators.

```powershell
python -m scripts.build_annotation_pool export
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `record_number` | `integer` | Stable global number, 1 through 1,000 for the formal pool. |
| `question_id` | `string` | Original unique question ID. |
| `paper_id` | `string` | Original paper ID; shared papers are allowed. |
| `question` | `string` | Unmodified source question text. |
| `passage_id` | `string` | Exact corpus passage ID. |
| `paper_title` | `string` | Real full paper title. |
| `passage` | `string` | Complete original retrieved passage text. |
| `label` | `null or integer` | Initially null; later human 0/1 labels must be associated by stable number and annotator. |
| `retrieval_method` | `string` | bm25; verification file only. |
| `rank` | `integer` | Original one-based retrieval rank. |
| `score` | `number` | Raw retrieval score. |
| `gold_passage_ids` | `array<string>` | Reference evidence-overlapping IDs, not human labels. |
| `gold_evidence_match` | `boolean` | Whether this passage overlaps a mapped gold paragraph. |
| `evidence_paragraphs` | `array<object>` | Reference evidence, joined after retrieval. |
| `evidence_paragraphs[].location` | `string` | Original source paragraph coordinate. |
| `evidence_paragraphs[].section_index` | `integer` | Original zero-based section index. |
| `evidence_paragraphs[].paragraph_index` | `integer` | Original zero-based paragraph index. |
| `evidence_paragraphs[].text` | `string` | Reference paragraph text. |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | Full non-whitespace union coverage. |
| `evidence_paragraphs[].passage_matches` | `array<object>` | Overlapping corpus passages. |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | Exact matching corpus passage ID. |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | Half-open character interval [start,end).  |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | Whether one passage covers the full paragraph. |

## `data/processed/annotation_held_out/manifest.json`

Exact inputs, code, configuration and every output hash.

```powershell
python -m scripts.build_annotation_pool export
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed. |
| `purpose` | `string` | development pilot or held-out annotation pool. |
| `question_count` | `integer` | Five in pilot; 200 in formal pool. |
| `pair_count` | `integer` | 25 in pilot; 1,000 in formal pool. |
| `question_ids` | `array<string>` | Persisted query order. |
| `inputs` | `object<string,string>` | Input path to exact SHA-256 digest mapping. |
| `inputs.<path>` | `string` | Hash of that input file's bytes. |
| `settings` | `object` | Frozen corpus and retrieval configuration. |
| `settings.chunk_size_words` | `integer` | $365$ words. |
| `settings.chunk_overlap_words` | `integer` | $40$ words. |
| `settings.top_k` | `integer` | Five distinct passages per question. |
| `code` | `object` | Code identity, including dirty changes. |
| `code.commit` | `string` | Git HEAD at execution time. |
| `code.python` | `string` | Python runtime version. |
| `code.working_tree_status` | `array<string>` | Git short status; the run may use uncommitted code. |
| `code.source_sha256` | `object<string,string>` | Exact hashes of all src/scripts Python files. |
| `code.source_sha256.<path>` | `string` | Source-byte SHA-256, checked at export. |
| `retriever` | `object` | Metadata from the maintained P1/P2 adapter. |
| `retriever.id` | `string` | p1-p2-static-retrieval adapter. |
| `retriever.mode` | `string` | bm25. |
| `retriever.source_commit` | `string` | Upstream adapter integration commit; actual code is identified separately. |
| `retriever.packages` | `object<string,string or null>` | Active package versions. |
| `retriever.packages.<package>` | `string or null` | Installed package version, null if unavailable. |
| `retriever.scope` | `string` | Selected paper only. |
| `retriever.persistent_score_cache` | `boolean` | False; no persisted score cache. |
| `retriever.score` | `string` | Raw BM25 score. |
| `retriever.tie_break` | `string` | Stable upstream ranking tie rule. |
| `retriever.bm25` | `object` | Active sparse retriever settings. |
| `retriever.bm25.enabled` | `boolean` | True. |
| `retriever.bm25.tokenizer` | `string` | Casefold and Unicode word runs. |
| `retriever.bm25.k1` | `number` | 1.5. |
| `retriever.bm25.b` | `number` | 0.75. |
| `retriever.bm25.epsilon` | `number` | 0.25. |
| `retriever.dense` | `object` | Disabled dense component. |
| `retriever.dense.enabled` | `boolean` | False; dense retrieval is disabled. |
| `retriever.reranker` | `object` | Disabled reranker component. |
| `retriever.reranker.enabled` | `boolean` | False; reranking is disabled. |
| `freeze_manifest_sha256` | `string or null` | Exact held-out freeze hash; null in pilot. |
| `outputs` | `object<string,string>` | Output paths mapped to SHA-256; excludes the manifest itself. |
| `outputs.<path>` | `string` | Exact output byte hash, including blind Markdown. |
| `validation` | `string` | Completed invariant checks. |

## `data/processed/annotation_held_out/annotator_A/ and annotator_B/`

Two independent English Markdown views; each formal set has $10$ batches of $20$ questions / $100$ pairs. No HTML, notes, internal IDs, gold, retrieval method or score. Assign each record's two views to different people.

```powershell
python -m scripts.build_annotation_pool export
```

| Field name | Type | Meaning |
| --- | --- | --- |
| `Annotator:` | `text` | Fill in the actual annotator identifier before collection. |
| `Record NNNN` | `heading` | Global record_number mapping; never edit. |
| `Paper:` | `text` | Real full title without internal IDs. |
| `Question / Passage` | `quoted text` | Original content; do not edit. |
| `Relevance / Label:` | `blank, 0 or 1` | Fill in only Label: 0 or Label: 1; retain all record numbers. |
