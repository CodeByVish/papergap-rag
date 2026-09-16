# PaperGap

An evidence-gap-driven agentic RAG system for adaptive multi-section question answering over NLP research papers.

**Status:** planning and repository setup. Retrieval, generation and the UI are not implemented yet.

## Start here

- [Week-by-week execution plan](docs/EXECUTION_PLAN.md): tasks, deliverables and integration checkpoints.
- [Requirements and open decisions](docs/REQUIREMENTS.md): rubric mapping and decisions to resolve in Week 1.
- [Evaluation protocol](docs/EVALUATION.md): annotation, held-out data and experiment comparisons.
- [Contributing](CONTRIBUTING.md): setup, branches, reviews and module ownership.
- [Weekly tracker](docs/WEEKLY_TRACKER.md): update at each team meeting.

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
docs/                 Plan, requirements, evaluation and team tracker
configs/              Proposed shared configuration
src/data/             P3: data preparation
src/retrieval/        P1/P2: retrievers, fusion and reranking
src/agent/            P4: planning and adaptive retrieval
src/generation/       P5: generation and citation validation
src/evaluation/       P6 + experiment owners: metrics and logging
src/ui/               P6: Streamlit
scripts/              Reproducible command-line entry points
tests/                Module and integration tests
data/                Local datasets (ignored except README)
results/              Local experiment outputs (ignored except README)
```

## Assignment delivery

Deadline supplied: **7 November, 11:59 PM SGT**. The supplied schedule is tracked for 2026; confirm the official assignment year in Blackboard. Submit one PDF with team details, the full report, and accessible links to code and datasets/results. Target code/report freeze: 6 November.

**Rubric clarification confirmed by the team:** passage chunks count toward 10,000 documents, and query–passage pairs count toward 1,000 evaluation records. Actual corpus size and annotation agreement still need verification; see [requirements](docs/REQUIREMENTS.md).
