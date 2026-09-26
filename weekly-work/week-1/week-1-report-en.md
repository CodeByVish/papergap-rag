# Week 1 Work Report: QASPER Data Foundation

As of September $26$, $2026$

## Work Overview

This week, I completed the acquisition and quality checks for a fixed QASPER revision, unified exports of the three official splits, construction and verification of the `Passage` data foundation and two corpus scopes, and an audit of figure files and table-text coverage in the fixed release. Raw data stays local, and derived files can be reproduced using the shared instructions.

## Completed Work

### Fixed Data and Quality Checks

I used the fixed `allenai/qasper` revision `fdc9d8214fbab5dd782958601db4d678e6934a54`, corresponding to source version `0.3.0`. I verified the row counts and hashes of the raw `train`, `validation`, and `test` files against `manifest.json`. The splits contain $888$, $281$, and $416$ papers, respectively, for a total of $1{,}585$; the inspection record shows that paper IDs are disjoint across splits.

### Unified Export and Separation

I kept the three raw split files unchanged and physically combined their records in `train`, `validation`, `test` order at the derived-data layer. Each exported record retains `source_split` for provenance and evaluation-boundary tracking.

`papers.jsonl` preserves each paper's `full_text`, figure and table metadata, and other original paper fields, while removing the top-level `qas`. `qa.jsonl` stores one question per row with its complete answer annotations and evidence fields, and adds `paper_id` and `source_split`. The two files are linked by `paper_id`.

The export contains $1{,}585$ papers, $5{,}049$ questions, and $7{,}993$ answer annotations. The independent structural check passed. I also compared the projected fields for every source paper and question; all fields and values matched. The structural check handled field projection, counts, hashes, and paper links without previewing question or answer content or using it for tuning.

The mapping from official splits to project roles remains labeled `v0-proposed`. A corpus containing `test` paper text is for inference indexing only; `test` questions, answers, and evidence annotations are not used for development tuning.

### Passage Schema and Corpora

I defined and validated the eight-field `Passage`: `passage_id`, `paper_id`, `title`, `section`, `chunk_number`, `text`, `previous_passage_id`, and `next_passage_id`. The builder reads only paper `full_text`, chunks within original section boundaries, assigns stable passage IDs, and links adjacent passages only within the same section. The current working configuration uses $200$ words per chunk with $40$ words of overlap; these parameters are not an experimentally optimal or permanently frozen setting.

The $100$-`Passage` sample comes from $100$ papers and serves as an interface reproducibility artifact. Its SHA-256 is `d017b7937d2e9a54ee653c8a3a94f37afa2819d548c0f79eacc93f08832bdb42`. The complete corpus has been built, so the sample no longer represents the corpus size.

| Corpus scope | Paper source | Source papers | Unique `Passage` records | Source words (excluding overlap) | SHA-256 | Manifest purpose |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `development` | `train` + `validation` text | $1{,}169$ | $32{,}073$ | $4{,}262{,}446$ | `abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790` | `development` |
| `all-paper-text` | Paper text from all three splits | $1{,}585$ | $42{,}719$ | $5{,}659{,}921$ | `32fa43714d6be6822636fd8513af8358cfff78474d50f7c310a1b90d28a868fa` | `index_for_inference` |

The development-corpus counts and hash are the existing baseline recorded in `data/README.md`. Its manifest is not retained in the current workspace, so I do not present those values as newly measured in this report. The all-paper-text row matches the counts, purpose, and hash in the local `passages_all_paper_text.manifest.json`.

### Figure and Table Coverage Audit

I checked all $1{,}585$ papers in the fixed revision: $1{,}551$ contain figure or table records, with $11{,}364$ references in total—$6{,}492$ table references and $4{,}872$ figure references. The `figures_and_tables` records contain captions and `.png` filenames. The fixed official release contains no corresponding image files, and $0$ of the $11{,}364$ referenced images can be located locally.

`full_text` sometimes repeats individual facts from tables, but it does not provide reliable, complete table-cell data. Targeted sampling found that some table facts also appear in the body, while other answers rely only on table evidence in missing images. These samples cannot be used to estimate overall question-and-answer coverage.

### Deliverables and Reproduction Evidence

The shared guide [`data/README.md`](../../data/README.md) documents reproduction entry points for the fixed-revision download, export and independent check, `Passage` sample, and both corpus scopes. Raw data and generated JSONL and manifest files remain in Git-ignored directories; teammates can generate them locally by following the guide.

This work delivers the unified export process defined by `papers.jsonl`, `qa.jsonl`, and `qasper_export.manifest.json`, along with build and verification results for the `development` corpus, the all-paper-text inference index, and the $100$-item reproducibility sample. The manifests and SHA-256 values in this report support checks of the fixed inputs and derived outputs.

## Current Limitations

The fixed release provides figure captions and filename references but not the corresponding image files; the paper text also does not guarantee complete table contents. As a result, some figure-dependent and table-dependent evidence cannot be recovered from the current `full_text` passages, and targeted sampling cannot determine overall coverage.