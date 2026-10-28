# Week 4 Work Report

**English** | [简体中文](week-4-report-zn-CN.md)

Status as of 2026/10/28

## Current rebuild status: Steps $2.5$–$2.7$

The independent `data/processed/qa_for_held_out_v2.jsonl` freezes $200$ questions with no intersection against the $2654$ banned IDs. From $3329$ all-splits gold-mapped questions, $1884$ are banned, leaving $1445$ eligible candidates. Seed $2026102805$, ascending IDs and Python `Random(seed).sample` were fixed before the draw. The outcome is $78$ validation/$122$ test questions across $174$ papers; no split quota or filter was applied. Isolation is at question level and permits shared papers. P1/P2 owner inventories and saved P3 development use define the accepted exclusion scope; pure functional tests, raw export, gold mapping and normal frozen evaluation are not automatic exclusions. Unrecorded external/P4–P6 use is outside the claim; later explicit development-use evidence requires a new inventory and eligibility review.

The original BM25 question list and annotation outputs are retired, with all $25$ files and hashes preserved in `historical_bm25_retirement.manifest.json`. Retirement does not declare every old question contaminated: $95$ old IDs are banned by other sources, and $13$ eligible old IDs were randomly redrawn. Old pairs, rankings, scores, labels and numbering are not reused. The older BM25 sections below describe historical outputs and commands, not the current deliverable; their former step numbering is superseded by the current Week 4 checklist.

Fresh BM25, Dense and Hybrid retrieval under the development-frozen $365/40$/paper-scoped/top-$5$ settings is complete in `data/processed/annotation_common_v2/`. Each algorithm has $1000$ native hits; $600$ ranking rows merge into $1532$ unique pairs, with $5$–$11$ per question. Common contains $975$ pairs, BM25-only $277$, Dense-only $254$ and Hybrid-only $26$. The count is the actual deduplicated union, not a fixed $1000$-record target; the design allows $5$–$15$ pairs per question. All labels remain null, and no formal `v2` Markdown export or gold-joined verification file has been produced. Both data guides document all six existing outputs, nested fields, frozen model/fusion settings, Git P3 access and local reproduction.

Step $2.7$ synchronizes the bilingual data guides and reports, evaluation protocol, requirements, execution plan, project overview, weekly tracker and local handoff/checklist. Read-only `python -m src.data.build_common_pool verify` passed again with $200$ questions, $1532$ pairs, $600$ ranking rows and $1000$ hits per method; its checks include matching inputs and all retained historical hashes. This documentation task does not rerun retrieval, resample questions or change any data. No commit or push was performed.

Step $2.8$ remains pending: export English Markdown from the saved JSONL, with $10$ batches of $20$ complete questions and variable record counts. Each question shows its real paper title and original text, then Common/BM25/Dense/Hybrid groups; two-way and three-way common pairs appear once in stable-number order, exclusive pairs follow native rank and empty groups show `None`. Preserve the stable record mapping, use level-four Passage/Relevance headings, and generate no HTML or notes field. Views disclose all algorithm sources and the annotator's name or agreed identifier; they are not algorithm-blind. Hide gold, scores, native ranks, internal IDs and other labels; initialize each `Label:` blank for binary relevance only.

Step $2.9$ remains pending: assign two different independent annotators per unique pair, requiring $2\times1532=3064$ initial judgments. Preserve each annotator's originals and labels, check completeness and validity, calculate agreement before adjudication, and retain the separate final label. `Instruction.pdf`, page $4$, Question $4$, requires at least $1000$ manually labeled records and at least $80\%$ agreement; it recommends three annotators and permits two. Pool construction alone does not meet that requirement. Every algorithm uses its original ranks joined to the common final labels, never Markdown order. Pool Recall@K covers relevant judged union members only; QASPER evidence-reference recall separately uses mapped `gold_passage_ids` with mapping/coverage limits. Unpooled passages remain unjudged. Do not tune using held-out content or results; future generator/agent configurations need their own freeze. See [the evaluation protocol](../../docs/EVALUATION.md#current-annotation-and-metric-protocol).

## Historical completion record: Step $2.4.2$

The pinned P1 $2593$, P2 $106$ and P3 $250$ selection IDs merge into $2654$ unique banned questions and $3864$ qualifying source memberships in `data/processed/qa_banned_for_held_out.jsonl`. Owner snapshots, exact statements, branch/commit/path pins, hashes, purpose decisions and generation settings are preserved in its manifest and `configs/held_out_exclusions.json`. All identities and provenance passed validation; no known eligibility records remain unresolved within the accepted scope. Unrecorded external/P4–P6 use is outside this claim. Pure functional checks and normal frozen evaluation are not automatic exclusions. Verification: $5$ targeted tests, syntax/lint, source-blob byte equality and full artifact reconstruction passed. Both data guides document reproduction and nested fields. Next: Step $2.5$, preserve/retire historical BM25 outputs and draw a new independent held-out list; no resampling, formal retrieval, commit or push was performed.

## Historical development milestone: Step $2.3$

Completed the development-only BM25/Dense/Hybrid pilot with the first $5$ persisted chunk-selection questions. The same $365/40$ corpus, original queries, complete selected-paper scope and top-$5$ produce $36$ unique pairs: $25$ common, $5$ BM25-only, $6$ Dense-only and no Hybrid-only. The selected $5$ papers contain $70$ passages. `python -m scripts.build_annotation_pool multi-pilot` exports `data/processed/annotation_pilot_multi_v2/`, preserving complete ranks/scores and gold joins in structured files, and two independent English Markdown templates with disclosed sources and blank labels. Gold/scores/internal IDs stay out of the views. BGE small revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, cosine and equal-weight RRF $20/60$ are frozen in `frozen_config.json`; feasibility was verified without held-out-driven selection. The preliminary `v1` snapshot is retained; `v2` follows an import-only lint correction and has identical pair/ranking bytes.

Targeted tests: $46$ passed. Independent persisted checks passed for input/output/current source hashes, original queries, corpus titles/text, unique union, complete per-method rank-to-record joins, post-retrieval gold association and annotation projection. Both data guides and evaluation/requirements records are updated. Earlier BM25 completion and blind-view descriptions below are historical. At pilot completion, the next task was Step $2.4$, the cross-branch actual-use audit (now completed to the scope below); formal three-system expansion, held-out eligibility recheck, new formal templates and human judgments remain pending. No commit or push was performed.

## Paper catalog for UI selection

Completed a lightweight paper catalog builder that extracts paper metadata from `data/processed/papers.jsonl` and combines it with `data/processed/passages.jsonl`, the passage corpus used by the current configuration, to produce paper and section lists for the UI to load once. The catalog includes only papers and sections that have passages; retrievable here means that passages are available for retrieval, without guaranteeing a match for every query. UI integration is not yet complete.

### Code involved

| Code path | Responsibility |
| --- | --- |
| `src/data/build_paper_catalog.py` | Provides `build_paper_catalog()`, reads papers and passages, validates unique IDs, nonempty text and paper/section references, and aggregates passage counts for each paper and section. |
| `scripts/build_paper_catalog.py` | Provides the command-line entry point, requires an explicit `--passages` argument, writes UTF-8 JSON, and refuses to overwrite an existing output. |
| `tests/data/test_paper_catalog.py` | Contains $9$ tests covering source order, merging sections with the same name, missing metadata, an empty corpus, duplicate IDs, invalid references, empty text and output protection. |

### Output and fields

The local output, `data/processed/paper_catalog.json`, contains $1{,}168$ selectable papers and $16{,}187$ paper/section-name entries, covering all $21{,}360$ passages in the selected corpus. The catalog and its source data are tracked on the P3 working branch together with their manifests.

The catalog has the top-level fields `schema_version`, `passages_file` and `papers`. The schema remains `v0-proposed`, and `passages_file` records the corpus used for this build, `data/processed/passages.jsonl`. Each paper contains `paper_id`, `title`, `authors`, `passage_count` and `sections`; each section contains `name` and `passage_count`. Field types and meanings, build commands, and local reproduction and Git-based data access workflows are documented in the [catalog section in English](../../data/README.md#dataprocessedpaper_catalogjson) in `data/README.md` and the [corresponding section in Chinese](../../data/README_zh-CN.md#dataprocessedpaper_catalogjson) in `data/README_zh-CN.md`.

Sections follow their first occurrence in the source text. Sections with the same normalized name are merged and their passage counts combined; section counts sum to the paper count. Missing or blank strings use `null`, and missing author lists use `[]`, without inferring unavailable values; the current QASPER export does not provide authors. UI retrieval must use the same corpus recorded in `passages_file`, and the catalog must be rebuilt whenever that corpus is replaced.

### Verification results

The saved catalog and passage corpus were read independently to verify unique paper IDs, consistent passage counts for every paper and section, and complete coverage of the total passage count. All $9$ new tests and all $530$ tests in the full suite passed; character, Python syntax and Ruff checks also passed. The full-suite command below explicitly uses a temporary directory inside the repository to avoid access restrictions affecting the old temporary directory:

```powershell
python -m pytest tests -q --basetemp tmp/tmp_pytest_week4_catalog --tb=short
```

## Historical BM25 annotation candidate pool and held-out question list

Completed local work-plan Steps $2.1$–$2.7$: restore historical tuning questions, run a development pilot, freeze the held-out draw, and export the formal candidate pool and blind annotation files. The formal list contains $200$ questions, each with $5$ distinct passages retrieved by paper-scoped BM25, giving $1{,}000$ unique `(question_id, passage_id)` pairs. Independent annotation templates are ready. Assigning people, collecting labels, calculating agreement and adjudicating disagreements remain pending in Step $2.8$; Step $2$ is not complete.

### Code involved

| Code path | Responsibility |
| --- | --- |
| `src/data/build_annotation_pool.py` | Restores historical questions, audits prior use, validates the pilot, selects and freezes eligible questions, retrieves pairs, joins gold references after retrieval and exports independent Markdown batches; verifies hashes and refuses replacement. |
| `scripts/build_annotation_pool.py` | Provides the ordered `prepare`, `pilot`, `freeze` and `export` CLI stages. |
| `src/data/export_evidence_mapping.py`, `scripts/export_evidence_mapping.py` | Treats the all-splits mapping as reference coverage, makes it the CLI default, and preserves the development scope and legacy argument alias. |
| `tests/data/test_annotation_pool.py` | Adds $4$ tests for blind projection and gold joining, batches and global numbering, hash and duplicate guards, prior-use exclusion and freeze protection. |
| `tests/evaluation/test_chunk_size.py` | Updates verification for the revised gold-reference semantics. |

### Question preparation and sampling boundaries

Retained `data/processed/gold_evidence_mapping_all_splits.jsonl` and its manifest as unified gold references for eligible questions across official splits. Removed the old local `data/processed/gold_evidence_mapping.jsonl` and its manifest. Reference coverage alone does not decide held-out status; independent question lists and actual use govern eligibility.

Fixed `chunk_size_words=365` and `chunk_overlap_words=40`, using `data/processed/passages_all_paper_text.jsonl`. Restored the actual $250$ tuning questions from `results/chunk_size/round4_bm25_20261028_01/questions.jsonl` without reconstructing them from a seed. A pilot used the first $5$ development questions to generate $25$ pairs and validate retrieval, deduplication, export and post-retrieval gold joining before sampling held-out questions.

The persisted local usage audit includes invalidated experiments and pilot runs. It identifies $253$ previously used question IDs, including $3$ outside the tuning list. Of the gold-mapped questions, $251$ are excluded for prior use and $1$ for having fewer than $5$ passages in its paper, leaving $3{,}077$ eligible questions. This audit establishes only recorded local use; it cannot establish the absence of unrecorded external use.

Eligibility uses identifiers, usage records and corpus metadata without previewing candidate questions, answers or evidence. Sort eligible IDs, use the predeclared seed $20261028$ with Python `Random(seed).sample` to draw $200$ without replacement, and preserve draw order. The saved draw contains $95$ train, $40$ validation and $65$ test questions. Isolation is at question level and allows shared papers with tuning questions; it does not establish paper-disjoint evaluation or designate an ordinary-testing annotation set.

Formal retrieval consumes the saved held-out list without resampling. Freeze records include input SHA-256 hashes, sampling scope, exclusions, eligible and selected IDs, retrieval settings, Git commit, dirty status, Python version and source hashes. Do not tune or develop from held-out questions, answers, evidence, human judgments or results. This freeze covers candidate-pool sampling and retrieval settings; it does not freeze unimplemented generation or agent configurations.

### Outputs and fields

| Artifact path | Contents and purpose |
| --- | --- |
| `data/processed/qa_for_choosing_chunk_size.jsonl` | The actual $250$ tuning questions, with `question_id`, `paper_id`, `question` and `source_split`. |
| `data/processed/annotation_preparation.manifest.json` | Historical input hashes, usage audit, excluded IDs, fixed settings and predeclared sampling rule. |
| `data/processed/qa_for_held_out.jsonl` | The frozen $200$ questions, with the same fields as the tuning list. |
| `data/processed/qa_for_held_out.manifest.json` | Eligibility, sampling, selected IDs, split counts, source and input fingerprints, and use boundaries. |
| `data/processed/annotation_pilot/` | The $25$ development pairs, verification records, manifest and two independent English Markdown views. |
| `data/processed/annotation_held_out/pairs.jsonl` | The $1{,}000$ formal pairs with stable global numbers for later label collection. |
| `data/processed/annotation_held_out/verification.jsonl` | Pair fields plus retrieval method, rank, score, gold IDs, evidence match and evidence paragraphs for internal verification. |
| `data/processed/annotation_held_out/manifest.json` | Question IDs, pair counts, retrieval settings, code identity, input/output hashes and freeze-manifest hash. |
| `data/processed/annotation_held_out/annotator_A/`, `data/processed/annotation_held_out/annotator_B/` | Two independent English Markdown slots, each with $10$ batches of $20$ questions / $100$ pairs, awaiting assignment to different people. |

The pair fields are `record_number`, `question_id`, `paper_id`, `passage_id`, `paper_title`, `question`, `passage` and `label`; initial labels are all `null`. Verification adds `retrieval_method`, `rank`, `score`, `gold_passage_ids`, `gold_evidence_match` and `evidence_paragraphs`. Gold is joined only after retrieval, does not affect ranking and must not be distributed to annotators. Manifest schemas remain `v0-proposed`.

Each Markdown record has a level-two heading such as `## Record 0001`, a real paper title under `Paper: Full Paper Title`, and `### Question`, `### Passage` and `### Relevance` sections. The shared header defines `0 — Not relevant` and `1 — Relevant` and includes `Annotator:`. Each record has an initially blank `Label:` for `Label: 0` or `Label: 1`. Five pairs for each question stay adjacent. Global numbers $0001$–$1000$ map back to internal IDs through JSONL.

Both views hide internal IDs, gold references, retrieval method, rank, score and the other annotator's judgments. They contain question text, passage text, the real title and a label field; no HTML or notes field is generated. Slots `annotator_A` and `annotator_B` do not yet represent assigned teammates or completed judgments.

The bilingual data guides document generation commands, complete field types and meanings, output paths and held-out boundaries. Evaluation, requirements, the shared tracker and configuration now describe question-level isolation. Run stages in this order; existing outputs are protected and must not be overwritten or resampled:

```powershell
python -m scripts.build_annotation_pool prepare
python -m scripts.build_annotation_pool pilot
python -m scripts.build_annotation_pool freeze
python -m scripts.build_annotation_pool export
```

### Verification results

Saved stage checks recorded $43$ targeted tests and $534$ full-suite tests passing, along with character, Python syntax and Ruff checks. The full-suite command was:

```powershell
python -m pytest tests -q --basetemp tmp/tmp_pytest_week4_all --tb=short
```

Independent artifact checks verified the pilot's $5$ questions / $25$ pairs and the formal pool's $200$ questions / $1{,}000$ pairs. Held-out IDs do not overlap audited prior use. Every question has exactly $5$ distinct, valid passages from the same paper, and all question–passage pairs are unique. Checks also covered passage text and real titles, gold joining, frozen input/output hashes, blind-field projection, both sets of Markdown batches and global numbering, and empty initial labels.

Candidate-pool generation and blank annotation files are complete; human labels and agreement results remain unavailable. Next, assign two different teammates independently to each record, retain their original files and labels, then collect judgments, calculate agreement and adjudicate disagreements under Step $2.8$.
