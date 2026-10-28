# PaperGap

[English](README.md) | [简体中文](README.zh-CN.md)

An evidence-gap-driven agentic RAG system for adaptive multi-section question answering over NLP research papers.

**Status:** P3 data preparation and chunk-size evaluation integrate P1/P2 static BM25, dense, hybrid and reranked retrieval. Fresh BM25/Dense/Hybrid runs produced the verified $200$-question/$1532$-pair common evaluation pool. The original BM25 annotation export is retired history; two source-disclosed English annotation sets are ready in `data/processed/annotation_common_v2_markdown/`; human labels remain pending. Real-model reranking, generation and UI integration remain unverified. See the [evaluation protocol](docs/EVALUATION.md) and [bilingual Week 4 report](weekly-work/week-4/week-4-report-en.md).

## Start here

- [Week-by-week execution plan](docs/EXECUTION_PLAN.md): tasks, deliverables and integration checkpoints.
- [Requirements and open decisions](docs/REQUIREMENTS.md): rubric mapping and decisions to resolve in Week 1.
- [Evaluation protocol](docs/EVALUATION.md): annotation, held-out data and experiment comparisons.
- [Contributing](CONTRIBUTING.md): setup, branches, reviews and module ownership.
- [Data and JSONL fields](data/README.md): versioned QASPER exports, all-splits gold references, and question-isolated annotation pools on the P3 branch.
- [Weekly tracker](docs/WEEKLY_TRACKER.md): update at each team meeting.
- [Chunk-size experiment](experiments/chunk_size/README.md): compare word-based chunks and export evidence and readability reviews using P1/P2 retrieval, defaulting to BM25. Select other modes through the JSON `retrieval` block; models load offline by default.

## Team

| Member | Name | Main ownership | Experiment ownership |
| --- | --- | --- | --- |
| P1 | Junlin Yin | BM25 and dense retrieval; standard retrieval API | BM25 vs dense |
| P2 | Vishakha | Hybrid fusion and reranking | Hybrid and reranking ablations |
| P3 | Jingshuai Qian | QASPER processing, chunks and passage schema | Chunking and corpus statistics |
| P4 | Ananya | LangGraph planner, critic and adaptive retrieval | Static vs adaptive RAG |
| P5 | Pending | Generation, citations and answer API | QA and grounding |
| P6 | Pending | Streamlit, evaluation infrastructure and reproducibility | RAGAS and end-to-end latency |

Everyone annotates, writes their report section, validates their module and reviews another member's work. P6 coordinates integration; each producer owns their interface and integration fixes.

## Planned pipeline

Selected paper + question → BM25 and dense retrieval → RRF → reranking → evidence critic → targeted retrieval if needed → evidence-conditioned answer or abstention → citation validation → Streamlit.

Maximum: one initial retrieval plus two retries. Optional dual critics and NLI come after the required pipeline and evaluation work.

## Local setup

Use Python 3.11 as the starter environment. Run these commands inside the cloned `papergap-rag` directory:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Windows activation: `.venv\Scripts\activate`.

The dependency files are provisional ranges, not a tested lockfile. Installation downloads libraries, not model weights or the dataset. University GPU access is available; P5 must confirm hardware and allocation details before model setup; vLLM and GPU-specific packages are deliberately separate decisions. P6 should record resolved versions after the first successful clean installation. No application launch command exists yet.

## Repository layout

```text
papergap-rag/
├── docs/             # Plan, requirements, evaluation and team tracker
├── configs/          # Proposed shared configuration
├── src/
│   ├── data/         # P3: data preparation
│   ├── retrieval/    # P1/P2: retrievers, fusion and reranking
│   ├── agent/        # P4: planning and adaptive retrieval
│   ├── generation/   # P5: generation and citation validation
│   ├── evaluation/   # P6 + experiment owners: metrics and logging
│   └── ui/           # P6: Streamlit
├── scripts/          # Reproducible command-line entry points
├── tests/            # Module and integration tests
├── data/             # Tracked QASPER data, manifests and bilingual guides
└── results/          # Shared experiment metrics, reports and reproducibility records
```

## Assignment delivery

Deadline supplied: **7 November, 23:59 SGT**. Submit one PDF with team details, the full report, and accessible links to code and datasets/results. Target code/report freeze: 6 November.

**Rubric clarification confirmed by the team:** passage chunks count toward 10,000 documents, and query–passage pairs count toward 1,000 evaluation records. Actual corpus size and annotation agreement still need verification; see [requirements](docs/REQUIREMENTS.md).
