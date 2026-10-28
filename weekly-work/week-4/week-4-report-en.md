# Week 4 Work Report

**English** | [简体中文](week-4-report-zn-CN.md)

Status as of 2026/10/28

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

## Annotation candidate pool and held-out question list

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
