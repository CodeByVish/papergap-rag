# PaperGap: Week-by-Week Execution Plan

> Working plan based on the supplied schedule. Names: P1 = Junlin Yin, P2 = Vishakha, P4 = Ananya; P3/P5/P6 pending. Dates follow the supplied September–November schedule (2026 tracking year; confirm in Blackboard).
>
> The team confirmed instructor acceptance of passage documents and query–passage evaluation records on 16 September 2026. See [requirements and decisions](REQUIREMENTS.md). The following clarifications take precedence over draft examples below:
>
> - Run the annotation pilot on development records in Week 3; Week 5 is a readiness check before full annotation.
> - Week 2 corpus is provisional. Freeze chunking and final passage IDs in Week 3 before final evidence mapping/annotation.
> - Use the distinct retrieval and generation comparisons in [the evaluation protocol](EVALUATION.md), replacing the overlapping experiment ladder below.
> - Report Cohen's kappa per fixed annotator pair and raw agreement before adjudication. Budget adjudication beyond the 2,000 initial judgments.
> - Citation validation checks passage IDs; semantic support needs separate evaluation. At budget exhaustion, abstain if evidence remains insufficient.
> - P6 coordinates; each module owner supplies tested integration and report material. Confirm GPU and RAGAS backend access in Week 1.
> - A maximum of two retries is a maximum of three retrieval rounds. Final schemas and model revisions remain Week 1 decisions.
> - Confirm any required group-number filename with Blackboard; it was not specified in the supplied assignment instructions.


This schedule uses the controlled scope you selected:

### Mandatory components

* QASPER knowledge base with at least 10,000 passage documents
* BM25 sparse retrieval
* BGE dense retrieval with FAISS
* Reciprocal Rank Fusion
* BGE cross-encoder reranking
* LangGraph planner and evidence-gap critic
* Typed gap diagnosis and targeted retrieval retries
* Deterministic stopping with a maximum of two retries
* Qwen3-8B evidence-conditioned generation
* Programmatic citation validation
* Simplified provenance trace
* Streamlit interface
* 1,000 manually labelled query–passage records
* Retrieval, QA and RAGAS evaluation

### Optional experiments

* Dual-perspective critic
* DeBERTa NLI faithfulness checker

### Removed from the required scope

* Learned stopping classifier
* External BEIR evaluation
* Complex interactive graph visualisation

## Final role allocation

| Person | Primary ownership                                                 |
| ------ | ----------------------------------------------------------------- |
| P1     | Sparse and dense retrieval                                        |
| P2     | Hybrid fusion and reranking                                       |
| P3     | QASPER data and knowledge-base construction                       |
| P4     | LangGraph planning, criticism and adaptive retrieval              |
| P5     | Qwen generation, citations and grounding                          |
| P6     | Streamlit, evaluation infrastructure, testing and reproducibility |

All six members also complete:

* approximately 333 annotation judgments;
* one report section;
* unit tests for their module;
* one module-specific experiment;
* code review for another person.

---

# Development rules for everyone

## Where the work happens

* Use **VS Code** for all production Python code.
* Use Jupyter notebooks only for initial exploration or visual analysis.
* Move any final logic out of notebooks and into reusable Python files.
* Push work to individual Git branches.
* Merge through pull requests after another member reviews the changes.
* Never commit model weights, raw dataset dumps, FAISS indexes or secrets.

## Suggested branch names

```text
p1-retrieval
p2-fusion-reranking
p3-knowledge-base
p4-agent
p5-generation
p6-ui-evaluation
```

## Critical rule

Nobody should directly code against another person’s unfinished module. Everyone develops against shared schemas and mock files first.

For example, P4 should be able to build the agent using `mock_retrieval_results.json` even before P1 and P2 complete retrieval.

---

# Week 1: Foundation and interface contracts

**14–20 September**

## Shared objectives

By the end of this week, all six members must agree on:

* project scope;
* repository structure;
* dataset splits;
* JSON schemas;
* Python environment;
* coding conventions;
* branch and pull-request workflow;
* evaluation rules;
* mandatory versus optional features.

This is the most important dependency-control week.

## P1 — Sparse and dense retrieval

### Tasks

* Study the basic operation of BM25, embeddings and FAISS.
* Create the retrieval module structure:

```text
src/retrieval/
├── bm25_retriever.py
├── dense_retriever.py
├── schemas.py
└── utils.py
```

* Define a common retriever function:

```python
retrieve(
    query: str,
    paper_id: str,
    top_k: int
) -> list[RetrievedPassage]
```

* Agree with P2 on the `RetrievedPassage` schema.
* Build temporary BM25 and dense retrieval using 100 mock passages supplied by P3.
* Write one basic test showing that retrieval returns the expected number of results.

### Technology

* Python
* `rank_bm25`
* Sentence Transformers
* FAISS
* Pydantic
* pytest

### Must be ready with

* Retrieval interface
* BM25 proof of concept
* FAISS proof of concept
* Mock retrieval output
* Schema shared with P2 and P4

---

## P2 — Hybrid fusion and reranking

### Tasks

* Study Reciprocal Rank Fusion and cross-encoder reranking.
* Define the expected BM25 and dense result format with P1.
* Create:

```text
src/retrieval/
├── hybrid_retriever.py
├── reranker.py
└── fusion.py
```

* Implement RRF using mock BM25 and dense rankings.
* Implement duplicate removal using `passage_id`.
* Load `BAAI/bge-reranker-base` on a small set of mock passages.
* Establish what final retrieval output P4 will receive.

### Technology

* Python
* PyTorch
* Hugging Face Transformers
* BGE reranker
* Pydantic
* pytest

### Must be ready with

* Working RRF on mock results
* Reranker proof of concept
* Final retrieval-output schema
* Mock reranked results for P4

---

## P3 — Knowledge base

### Tasks

* Create the reproducible QASPER download script.
* Explore QASPER’s fields, paper structure, sections, questions and evidence.
* Confirm which official split fields are available.
* Define the development, validation and held-out split policy with P5/P6.
* Extract 100 sample passages immediately for the other members.
* Define the passage-document schema:

```json
{
  "passage_id": "paper123_results_04",
  "paper_id": "paper123",
  "title": "Paper title",
  "section": "Results",
  "chunk_number": 4,
  "text": "Passage text",
  "previous_passage_id": "paper123_results_03",
  "next_passage_id": "paper123_results_05"
}
```

### Technology

* Python
* Hugging Face `datasets`
* pandas
* JSONL
* Pydantic

### Must be ready with

* `download_qasper.py`
* Dataset field summary
* 100 clean sample passages
* Frozen passage schema
* Preliminary split strategy

---

## P4 — Agentic reasoning

### Tasks

* Study LangGraph nodes, state, conditional edges and retry loops.
* Define the agent state:

```python
class AgentState:
    question: str
    paper_id: str
    required_components: list
    retrieved_passages: list
    evidence_map: dict
    gap_label: str
    rewritten_query: str
    retrieval_round: int
    sufficient: bool
```

* Create mock implementations for:

  * question planner;
  * evidence mapper;
  * single critic;
  * gap classifier;
  * query rewriter;
  * deterministic stopping condition.

* Build a LangGraph skeleton that runs with P2’s mock retrieval results.

* Confirm gap labels with the entire team.

### Technology

* Python
* LangGraph
* Pydantic
* Qwen-compatible structured prompts
* pytest

### Must be ready with

* LangGraph skeleton
* Agent-state schema
* Gap-label definitions
* Mock agent execution trace
* Expected retrieval callback format for P1/P2

---

## P5 — Generation and grounding

### Tasks

* Confirm university GPU access and available GPU memory.
* Test whether Qwen3-8B can be loaded using Transformers or vLLM.
* Define the final answer schema:

```json
{
  "answer": "Generated answer",
  "citations": ["paper123_results_04"],
  "evidence_status": "SUFFICIENT",
  "retrieval_rounds": 2,
  "provenance": []
}
```

* Create a mock generator that returns valid structured responses.
* Design the initial evidence-constrained generation prompt.
* Define citation rules:

  * citations must reference retrieved passages;
  * each factual claim should have evidence;
  * unsupported numerical claims are prohibited;
  * insufficient evidence must produce a refusal.

### Technology

* Qwen3-8B
* vLLM or Hugging Face Transformers
* PyTorch
* Pydantic
* pytest

### Must be ready with

* Confirmed model-serving method
* Mock generated-answer JSON
* Initial prompt template
* Final-response schema for P6
* GPU feasibility note

---

## P6 — UI, evaluation and reproducibility

### Tasks

* Create the initial Streamlit application using mock data.

* Add:

  * paper selector;
  * question input;
  * Analyze button;
  * answer panel;
  * citations panel;
  * evidence-status display;
  * retrieval-trace placeholder.

* Create the project configuration file:

```text
configs/default.yaml
```

* Establish experiment-result formats with P1, P2 and P5.
* Create the initial pytest and logging structure.
* Prepare a shared experiment registry.

### Technology

* Streamlit
* Python
* YAML
* JSONL/CSV
* pytest
* GitHub Actions, if practical

### Must be ready with

* Working mock Streamlit interface
* Configuration file
* Experiment-result schema
* Basic integration test
* README skeleton

---

## Week 1 team checkpoint

The following must be frozen before Week 2:

* Passage schema
* Retrieval-result schema
* Agent-state schema
* Final-answer schema
* Dataset split policy
* Gap-label list
* Repository structure
* Mandatory and optional features

Changes after this point require agreement from affected module owners.

---

# Week 2: Knowledge base and independent retrieval

**21–27 September**

## P1

* Build the full BM25 indexing pipeline.
* Build the full dense-embedding pipeline.
* Store embeddings in FAISS.
* Build and test the FAISS-to-passage-ID mapping.
* Implement paper-level filtering so the system searches only the selected paper.
* Measure preliminary retrieval latency.
* Add tests for:

  * valid top-K;
  * paper filtering;
  * stable passage IDs;
  * missing paper IDs.

### Ready by end of week

* Working BM25 retriever
* Working dense retriever
* Saved index-building scripts
* BM25 and dense results on sample questions

## P2

* Complete RRF fusion.
* Complete candidate deduplication.
* Complete BGE reranking.
* Test various candidate sizes, such as:

```text
BM25 top 20 + dense top 20
→ RRF fused candidates
→ reranked top 5 or top 8
```

* Ensure all rank and score fields are retained for later analysis.
* Develop against P1’s mock results first, then actual results once available.

### Ready by end of week

* Working hybrid retriever
* Working reranker
* Reranked output following the agreed schema
* Preliminary latency figures

## P3

* Complete QASPER cleaning.

* Implement section-aware chunking.

* Start with approximately:

  * 200 words per chunk;
  * 40-word overlap;
  * no merging across unrelated sections.

* Preserve section titles and neighbouring-passage references.

* Generate corpus statistics.

* Verify:

  * at least 10,000 chunks;
  * at least 100,000 words;
  * no duplicate IDs;
  * no empty chunks;
  * no train/held-out leakage.

### Ready by end of week

* `passages.jsonl`
* At least 10,000 passage documents
* Corpus-statistics file
* Data-quality report
* Frozen dataset splits

## P4

* Implement the question planner using mock retrieval.

* Define common question types:

  * factual;
  * method;
  * result;
  * comparison;
  * limitation;
  * unanswerable.

* Generate structured evidence requirements for each question.

* Implement basic evidence-map creation.

* Build tests using manually written examples.

### Ready by end of week

* Working planner
* Structured evidence components
* Basic evidence mapper
* Planner tests

## P5

* Complete Qwen3-8B model-serving setup.
* Run generation on 5–10 mock examples only.
* Implement structured-output parsing.
* Add fallback handling when the model produces invalid JSON.
* Build the citation validator against mock retrieved-passage IDs.
* Log model latency and GPU memory usage.

### Ready by end of week

* Qwen inference script
* Valid structured answers
* Citation-validation function
* Initial GPU and latency observations

## P6

* Connect the Streamlit application to mock backend functions.
* Add expandable citation cards.
* Add loading and error states.
* Build experiment logging utilities.
* Create tests that verify UI-facing responses match the schema.
* Begin the annotation guideline with P3 and P5.

### Ready by end of week

* Polished mock UI
* Experiment logger
* Initial annotation guideline
* UI/backend contract tests

---

# Week 3: Baseline retrieval evaluation

**28 September–4 October**

## P1

* Integrate BM25 and dense retrieval with P3’s complete corpus.
* Generate results for the development questions.
* Calculate baseline Precision@K, Recall@K and MRR with P6/P5’s metric functions.
* Investigate retrieval failures:

  * exact terminology missed by dense retrieval;
  * paraphrases missed by BM25;
  * incorrect paper filtering;
  * section mismatch.

### Deliverables

* BM25 baseline results
* Dense baseline results
* Retrieval error examples
* Retrieval module documentation

## P2

* Integrate actual P1 results into RRF.
* Run hybrid and hybrid-plus-reranker experiments.
* Tune top-K and RRF parameters using development/validation data only.
* Do not touch the held-out test results for tuning.
* Add retrieval-stage timing instrumentation.

### Deliverables

* Hybrid baseline
* Hybrid-plus-reranker baseline
* Selected top-K and fusion configuration
* Retrieval ablation table draft

## P3

* Perform chunk-quality inspection on a sample.

* Compare reasonable chunk settings, such as:

  * 150 words;
  * 200 words;
  * 250 words.

* Select the final setting using development retrieval results and readability.

* Freeze the knowledge base after selection.

* Document the entire data pipeline in the README.

### Deliverables

* Final frozen knowledge base
* Chunking analysis
* Corpus-statistics table
* Data-preparation documentation

## P4

* Connect the planner and evidence mapper to P2’s retrieval API.
* Implement the mandatory single evidence critic.
* Critic output must include:

```json
{
  "sufficient": false,
  "gap_label": "MISSING_RESULT",
  "missing_components": ["reported F1 score"],
  "reason": "The retrieved passages explain the method but contain no result."
}
```

* Implement deterministic validation of critic outputs.
* Begin query-reformulation rules.

### Deliverables

* Real retrieval-to-agent integration
* Working single critic
* Typed gap diagnosis
* Agent traces on development examples

## P5

* Connect generation to actual retrieved passages.
* Improve evidence-constrained prompts.
* Ensure the model cannot cite passages that were not retrieved.
* Implement simplified provenance mapping.
* Test answerable and unanswerable questions.

### Deliverables

* First evidence-grounded Qwen answers
* Citation validator
* Provenance JSON
* Initial refusal behaviour

## P6

* Implement retrieval metrics:

  * Precision@K;
  * Recall@K;
  * MRR;
  * nDCG.

* Verify metric calculations using a tiny manually checked example.

* Add retrieval latency recording.

* Connect the UI to a stub that follows the real backend signature.

### Deliverables

* Verified retrieval-metric functions
* Latency logger
* Retrieval-results CSV format
* UI ready for real backend connection

---

# Week 4: Complete the adaptive agent

**5–11 October**

## P1

* Expose BM25 and dense retrieval through stable callable functions.
* Support query rewriting and paper/section filters.
* Cache embeddings.
* Resolve any index or ID-mapping failures.
* Freeze the independent retriever interfaces.

## P2

* Expose a single hybrid-retrieval function to P4.
* Support optional section filters passed by the agent.
* Finish reranker caching.
* Freeze the final retrieval configuration.
* Provide P4 with retrieval latency and trace fields.

## P3

* Construct paper metadata used by the UI:

  * paper ID;
  * title;
  * authors where available;
  * available section names.

* Produce a lightweight paper catalogue.

* Begin constructing the annotation candidate-pool script.

* Ensure gold QASPER evidence can be mapped to chunk IDs.

## P4

* Finish the LangGraph adaptive loop:

```text
Plan question
→ Retrieve
→ Map evidence
→ Critique
→ Diagnose gap
→ Reformulate
→ Retrieve again
→ Stop or generate
```

* Implement gap-specific actions:

| Gap                        | Action                                   |
| -------------------------- | ---------------------------------------- |
| Missing method             | Prioritize Method/Approach               |
| Missing experiment context | Search dataset, setup and metrics        |
| Missing result             | Prioritize Results                       |
| Missing comparison         | Add missing model/baseline name          |
| Terminology mismatch       | Expand query using paper terminology     |
| Weak evidence              | Reformulate or change retrieval emphasis |
| Insufficient information   | Stop and refuse                          |

* Enforce a maximum of two retries.
* Log every retrieval round.
* Implement deterministic stopping.

## P5

* Connect generation to P4’s evidence map.

* Generate only after evidence is sufficient or the retry budget is exhausted.

* Complete:

  * answer generation;
  * passage citations;
  * citation validation;
  * provenance mapping;
  * insufficient-evidence response.

* Prevent unsupported numerical claims where possible.

## P6

* Connect Streamlit to an end-to-end mock or development backend.

* Display:

  * selected paper;
  * answer;
  * citations;
  * supported and missing evidence;
  * number of retrieval rounds;
  * rewritten queries;
  * final critic decision.

* Add integration tests using fixed examples.

## Week 4 integration checkpoint

By 11 October, the team must demonstrate at least one complete query:

```text
Select paper
→ Ask question
→ Retrieve evidence
→ Critique evidence
→ Retry if required
→ Generate answer
→ Validate citations
→ Display in Streamlit
```

The output quality may still be imperfect, but the entire pipeline must execute.

---

# Week 5: System refinement and annotation pilot

**12–18 October**

## P1

* Finalize BM25 and dense retrieval reliability.
* Run retrieval error analysis.
* Document why sparse and dense retrieval behave differently.
* Provide frozen retrieval outputs for annotation-pool construction.

## P2

* Finalize hybrid and reranking configuration.

* Produce pooled candidate passages for P3/P5.

* Compare:

  * BM25;
  * dense;
  * hybrid;
  * hybrid plus reranker.

* Freeze retrieval parameters before manual evaluation begins.

## P3

* Select 100 held-out QASPER questions.
* Stratify across question and answerability types where practical.
* Generate ten candidate passages per question from pooled retrieval systems.
* Include gold QASPER evidence where it can be mapped correctly.
* Remove duplicates.
* Export exactly 1,000 annotation records.

## P4

* Refine critic prompts on development examples.
* Check whether the critic incorrectly accepts incomplete evidence.
* Implement the optional dual-perspective critic on a limited development sample.
* Do not allow dual-critic work to delay the mandatory single critic.

## P5

* Refine the generation prompt.

* Check:

  * citation validity;
  * answer conciseness;
  * numerical grounding;
  * refusal behaviour;
  * malformed output handling.

* Help P6/P3 finalize the annotation relevance guidelines.

## P6

* Finalize the annotation sheet or form.
* Run a 30–50-record annotation pilot involving all six members.
* Calculate preliminary percentage agreement and Cohen’s kappa.
* Coordinate a discussion about disagreements.
* Update annotation instructions before full annotation.

## Week 5 freeze

After the annotation pool is created:

* Do not change the 100 held-out questions.
* Do not tune retrieval parameters using their final labels.
* Keep the held-out records separate from development experiments.
* Record the Git commit and configuration used to create the pool.

---

# Week 6: Manual annotation and system freeze

**19–25 October**

## Shared annotation work

Each of the 1,000 records receives two independent judgments.

| Member | First-label batch | Second-label batch |
| ------ | ----------------: | -----------------: |
| P1     |             1–167 |            501–667 |
| P2     |           168–334 |            668–834 |
| P3     |           335–500 |          835–1,000 |
| P4     |           501–667 |              1–167 |
| P5     |           668–834 |            168–334 |
| P6     |         835–1,000 |            335–500 |

Each member completes approximately 333 judgments.

Annotators must not see the other person’s answer before submitting their own.

## P1

* Complete assigned annotations.
* Freeze BM25 and dense code.
* Prepare retrieval reproducibility commands.
* Fix only genuine bugs—not tune against held-out labels.

## P2

* Complete assigned annotations.
* Freeze RRF and reranking code.
* Prepare retrieval ablation execution scripts.
* Record final model names and parameters.

## P3

* Complete assigned annotations.
* Validate that all 1,000 records have valid question and passage IDs.
* Archive corpus statistics and data-preparation configuration.
* Assist P6 with annotation completeness checks.

## P4

* Complete assigned annotations.
* Freeze the mandatory single-critic agent.
* Run optional dual critic only if the core agent is stable.
* Prepare static versus adaptive RAG experiments.

## P5

* Complete assigned annotations.
* Freeze Qwen model, prompt, temperature and output schema.
* Freeze citation-validation behaviour.
* Implement optional NLI checker only if required work is complete.

## P6

* Complete assigned annotations.
* Monitor annotation completeness.
* Calculate pre-adjudication agreement.
* Randomly assign disagreements to a third annotator.
* Preserve original labels before adjudication.
* Create the final gold-label file.
* Freeze the UI and experiment configuration.

## Week 6 completion criteria

* 1,000 records
* 2,000 independent judgments
* Raw percentage agreement reported
* Cohen’s kappa reported
* At least 80% raw inter-annotator agreement
* Disagreements adjudicated separately
* Original and final labels preserved

---

# Week 7: Final experiments and analysis

**26 October–1 November**

## P1

Run and document:

* BM25 retrieval
* Dense retrieval
* Precision@K
* Recall@K
* MRR
* nDCG
* latency
* error analysis

## P2

Run and document:

* Hybrid retrieval
* Hybrid plus reranker
* fusion contribution
* reranking contribution
* top-K behaviour
* latency added by reranking

## P3

Prepare:

* knowledge-base statistics;
* dataset split table;
* chunking methodology;
* annotation-pool construction explanation;
* data-quality and leakage checks;
* data files for the external cloud folder.

## P4

Run and compare:

* static hybrid RAG without critic;
* single-critic evidence-gap RAG;
* optional dual-critic RAG, if complete.

Measure:

* evidence recall before and after retries;
* average retrieval rounds;
* successful gap recovery;
* unnecessary retries;
* refusal behaviour.

## P5

Run and document:

* Exact Match;
* token F1;
* ROUGE-L;
* evidence F1;
* citation validity rate;
* unanswerable accuracy;
* optional NLI results.

Ensure Qwen3-8B and the same frozen prompt/configuration are used across reported comparisons.

## P6

Run and document:

* RAGAS Faithfulness;
* RAGAS Answer Relevance;
* optional Context Precision and Context Recall;
* end-to-end latency;
* p50 and p95 latency;
* GPU-seconds per query where measurable;
* integration tests;
* UI demonstration cases.

P6 also combines all experiment outputs into standardized tables.

## Required experiment ladder

| ID          | System                                 |
| ----------- | -------------------------------------- |
| A           | Generator without retrieval            |
| B           | BM25 RAG                               |
| C           | Dense RAG                              |
| D           | Hybrid RAG                             |
| E           | Hybrid plus reranker                   |
| F           | Static hybrid-plus-reranker RAG        |
| G           | Single-critic evidence-gap PaperGap    |
| H           | Single critic plus citation validation |
| Optional I  | Dual-perspective critic                |
| Optional J  | NLI faithfulness gate                  |
| Upper bound | Gold QASPER evidence supplied directly |

Not every experiment needs every retrieval metric. Retrieval configurations use rank-aware metrics; complete RAG configurations use QA and RAGAS metrics.

---

# Week 8: Report, demonstration and submission preparation

**2–6 November**

## P1

* Write sparse and dense retrieval sections.
* Add implementation details and retrieval results.
* Verify retrieval commands in the README.
* Review P2’s retrieval claims.

## P2

* Write hybrid fusion and reranking sections.
* Add ablation and error-analysis results.
* Review P1’s retrieval code and results.
* Confirm that all retrieval tables are reproducible.

## P3

* Write QASPER, cleaning, chunking and corpus-statistics sections.
* Add the dataset schema and split explanation.
* Verify all dataset/result cloud links.
* Review the annotation-data files.

## P4

* Write planner, evidence critic, gap diagnosis and retry-loop sections.
* Add agent architecture diagram and adaptive-retrieval results.
* Explain deterministic stopping.
* Clearly label the dual critic as optional if it was not completed.

## P5

* Write generation, citation validation and provenance sections.
* Add QA and grounding results.
* Explain Qwen3-8B deployment and GPU usage.
* Document optional NLI only if it was actually evaluated.

## P6

* Complete the Streamlit UI.

* Assemble the full report.

* Add:

  * team details;
  * contribution statement;
  * architecture diagrams;
  * evaluation tables;
  * limitations;
  * ethics;
  * external links;
  * final appendix.

* Run the repository from a clean environment.

* Verify all report links.

* Check formatting and PDF export.

## 6 November: code and report freeze

After this date:

* no model changes;
* no parameter tuning;
* no dataset changes;
* no major UI redesign;
* only factual, formatting or link corrections.

## 7 November: submission

Before 11:59 PM SGT:

* export one final PDF;
* use the required group-number filename;
* verify GitHub access;
* verify dataset/results cloud links;
* verify the PDF opens correctly;
* confirm team details and matriculation numbers;
* submit through Blackboard early enough to handle upload problems.

---

# Dependency-control matrix

| Producer          | Must provide                 | Consumer   | Deadline |
| ----------------- | ---------------------------- | ---------- | -------- |
| P3                | 100 sample passages          | P1, P2, P4 | Week 1   |
| P1                | Mock BM25/dense results      | P2         | Week 1   |
| P2                | Mock fused/reranked results  | P4         | Week 1   |
| P4                | Mock evidence map            | P5         | Week 1   |
| P5                | Mock final-answer JSON       | P6         | Week 1   |
| P6                | Config and experiment schema | Everyone   | Week 1   |
| P3                | Full frozen corpus           | P1         | Week 2   |
| P1                | Real sparse/dense API        | P2         | Week 2   |
| P2                | Real hybrid/reranker API     | P4         | Week 3   |
| P4                | Real agent output            | P5         | Week 4   |
| P5                | Real final-answer response   | P6         | Week 4   |
| P1/P2             | Frozen candidate results     | P3/P6      | Week 5   |
| All               | Manual labels                | P6         | Week 6   |
| All module owners | Final result tables          | P6         | Week 7   |

## If a dependency is late

* The consumer continues using the agreed mock JSON.
* The producer must not change the schema without notifying affected owners.
* Integration issues are logged as GitHub issues.
* P6 maintains a dependency tracker.
* No member waits without progressing on tests, documentation, mock integration or experiments.
* Missing optional features never block the mandatory pipeline.

---

# Weekly team meeting structure

Hold one fixed meeting each week, approximately 45–60 minutes.

Each person answers:

1. What did I complete?
2. What exact file, branch or result can the team inspect?
3. What will I complete next?
4. What dependency do I need?
5. Is any interface changing?
6. Is any mandatory component at risk?

End every meeting with written actions containing:

```text
Task
Owner
Deadline
Required input
Expected output
Blocking or non-blocking
```

## Additional short technical syncs

* P1 and P2: retrieval sync twice weekly.
* P4 and P5: agent-generation sync twice weekly.
* P3 sends data changes to P1/P2 immediately.
* P6 attends one retrieval and one agent-generation sync weekly for integration visibility.

This arrangement gives everyone substantial, individually demonstrable work while preventing the project from becoming a chain where one delayed member stops the entire group.
