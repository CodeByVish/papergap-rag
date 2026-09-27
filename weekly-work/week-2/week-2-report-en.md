# Week 2 Work Report: QASPER Knowledge Base Milestone Review

**English** | [简体中文](week-2-report-zn.md)

As of September $27$, $2026$

## 1. Overview and Scope

This week I reviewed the P3 QASPER knowledge base milestone for Week $2$. Data acquisition, cleaning, section-aware chunking, `Passage` construction, the $100$-passage sample, and corpus-size measurements had already been completed in Week $1$. This report cites those results and records this week's independent checks of the retained exports, inference corpus, and data-module tests. The reproducible data foundation meets the main technical target for Week $2$; chunk-parameter selection, the final corpus freeze, and team approval of shared interfaces remain open.

This report covers the P3 data foundation and handoff status. P1 retrieval quality, later annotation, and QA results are not counted as P3 work completed this week. The [execution plan](../../docs/EXECUTION_PLAN.md) dates Week $2$ from September $21$ to $27$; the [weekly tracker](../../docs/WEEKLY_TRACKER.md) calls for a provisional corpus this week and schedules the final chunker and corpus freeze for Week $3$.

## 2. Week 2 Tasks and Existing Results

| Week 2 task | Status and evidence |
| --- | --- |
| QASPER source, structure inspection, and data export | Complete. The pinned revision, original splits, and anomaly inspection are documented in the [Week 1 English report](../week-1/week-1-report-en.md), Section $2$; separate paper and QA exports are documented in Section $3$. |
| Cleaning and section-aware chunks with titles, stable IDs, and neighbor links | Implemented. The provisional setting is $200$ words per chunk with a $40$-word overlap; cleaning and construction rules and the eight-field `Passage` model are documented in the Week 1 English report, Section $4$. |
| Corpus statistics and assignment size thresholds | Met. Section $5$ of the Week 1 English report records a `development` baseline of $32{,}073$ unique passages and $4{,}262{,}446$ source words excluding overlap, above the $10{,}000$-document and $100{,}000$-word thresholds. This scope's JSONL was not regenerated this week. |
| Data quality and split isolation | Inspection is recorded. Sections $2$, $3$, and $6$ of the Week 1 English report cover disjoint official splits, export links, and separation of paper text from QA supervision; the project-role mapping remains `v0-proposed`. |
| Reproducible inputs for teammates | Source code, field descriptions, and local generation commands are available. See Section $7$ of the Week 1 English report and the [data guide](../../data/README.md); downloaded raw data and generated JSONL files stay out of Git. |

The Week 1 report's statement that the `development` JSONL was "not retained" means only that the regenerable file and its manifest were absent from the current workspace at the time. It does not mean the pipeline or measured baseline is missing, and it does not call for uploading large data files to GitHub. Teammates can generate the needed corpus locally with the commands in that report.

## 3. Checks Run This Week

The following checks ran this week in the project's `papergap-rag` Python environment against retained artifacts and the data module. They did not modify source data or corpus files, and the test directory was removed. They do not replace the Week $3$ parameter comparison or team decisions.

| Checked item | Command entry point | Result |
| --- | --- | --- |
| Paper and QA exports and links | `python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json` | Passed: $1{,}585$ papers, $5{,}049$ questions, $7{,}993$ answer annotations; file hashes match the manifest. |
| All-paper-text inference corpus | `python -m scripts.check_corpus --corpus data/processed/passages_all_paper_text.jsonl --manifest data/processed/passages_all_paper_text.manifest.json` | Passed: independently recounted $42{,}719$ unique passages and $210{,}909$ word types, and verified SHA-256 `32fa43714d6be6822636fd8513af8358cfff78474d50f7c310a1b90d28a868fa`, record format, and nonempty text. The manifest records $5{,}659{,}921$ source words; the checker validates that this value exceeds the assignment threshold without recounting source papers. |
| P3 data-module tests | `python -m pytest tests/data -q --basetemp tmp_pytest_p3_20260927` | $273$ passed; the temporary test directory was removed. |

The `all-paper-text` corpus includes `test` paper bodies for inference indexing only. This week's checks did not use `test` questions, answers, evidence, or labels to select chunking parameters. The $32{,}073$-passage `development` figure remains the baseline recorded in the Week 1 report and `data/README.md`; the $42{,}719$ passages checked this week belong to a different corpus scope and are not presented as a new `development` build.

## 4. Current Status and Next Work

Against the weekly tracker, the P3 Week $2$ provisional knowledge base checkpoint has a reproducible implementation and size evidence. Week $3$ still requires comparing roughly $150$-, $200$-, and $250$-word chunks on development and validation data, selecting a setting using retrieval results and readability, and recording the final corpus freeze. The current $200/40$ configuration is not an experimentally selected final parameter; see the Week $3$ P3 section of the [execution plan](../../docs/EXECUTION_PLAN.md) and the "Normalization and chunking contract" in the [data guide](../../data/README.md).

The `Passage` interface, corpus scope, and official-split-to-project-role mapping remain `v0-proposed` pending team review; see `P3-D001` through `P3-D004` in the [decision log](../../docs/REQUIREMENTS.md). Later P3 work includes a paper catalogue, mapping QASPER evidence to passage IDs, the annotation candidate pool, assigned manual labels, and final report and data archiving. None of those later tasks is counted as completed Week $2$ work.
