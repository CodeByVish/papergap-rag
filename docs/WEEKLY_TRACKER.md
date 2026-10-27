# Weekly tracker

Update this file after the weekly meeting. Link to concrete issues, PRs, artifacts or run IDs.

| Week | Dates | Exit checkpoint | Status |
| --- | --- | --- | --- |
| 1 | 14–20 Sep | Rubric interpretation, owners, compute, interfaces and split policy | Not recorded |
| 2 | 21–27 Sep | Provisional corpus, independent retrieval, pilot candidates | Not recorded |
| 3 | 28 Sep–4 Oct | Retrieval baselines, annotation pilot, final chunker/corpus freeze | Not recorded |
| 4 | 5–11 Oct | One complete query in Streamlit | Not recorded |
| 5 | 12–18 Oct | Frozen held-out pool and annotation guidelines | Not recorded |
| 6 | 19–25 Oct | 2,000 blind judgments, agreement, adjudication, system freeze | Not recorded |
| 7 | 26 Oct–1 Nov | Final comparisons and analysis | Not recorded |
| 8 | 2–6 Nov | Clean setup, report PDF and links verified | Not recorded |
| Submission | 7 Nov | Blackboard submission before 11:59 PM SGT | Not recorded |

## Meeting actions

| Task / issue | Owner | Due | Required input | Reviewable output | Blocking? | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Confirm rubric document/record units | Team | Week 1 | Instructor clarification | Both interpretations confirmed; see REQUIREMENTS.md | No | Confirmed 16 Sep |
| Confirm compute and evaluator access | P5/P6 | Week 1 | GPU access and judge backend | Feasibility note | Yes: inference setup | Open |
| Fill remaining names and backup owner | Team | Week 1 | Member agreement | Updated README | No | Open |

## P2 Week 1 progress

Fusion, deduplication, proposed schemas, mock handoff and BGE CPU smoke test are implemented on `p2/week1-fusion-reranking`. See [P2 handoff](P2_WEEK1.md). 17 tests passed. Interface agreement with P1/P3/P4 remains pending; this does not mark the whole team checkpoint complete.

## P1 Week 1 / Week 2 progress

This records P1's independent retrieval work; it does not mark the team's Week 1 or Week 2 exit checkpoints complete.

| Deliverable | Status | Evidence / remaining dependency |
| --- | --- | --- |
| Shared retrieval interface | Implemented | BM25 and dense return the existing `RetrievalHit` schema with original `Passage` fields and IDs. |
| BM25 retrieval | Implemented and tested on synthetic data | Per-paper indexes, parameter validation, stable IDs, filtering and deterministic ranks; `src/retrieval/bm25_retriever.py`, `tests/test_p1.py`. |
| BGE dense retrieval and FAISS | Implemented and tested on synthetic data | Query-only instruction, L2 normalization, per-paper `IndexFlatIP`, finite scores and deterministic top-K; `src/retrieval/dense_retriever.py`. |
| FAISS mapping and persistence | Implemented and tested | Explicit row-to-Passage mappings, save/load without re-encoding passages, model/encoding metadata and consistency checks. |
| P2 callback compatibility | Verified by regression tests | Both retrievers can be used by the existing `HybridRetriever`; P2 algorithms remain unchanged. |
| Real BGE model smoke check | Verified on synthetic passages | `BAAI/bge-small-en-v1.5`, revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, CPU; separate from fake-encoder unit tests. |
| Reproducible build and sample-query commands | Verified on synthetic data | `scripts/build_indexes.py` and `scripts/demo_p1.py` ran successfully with the pinned real BGE model from the local cache; see the verification evidence below. |
| Preliminary synthetic latency | Measured | One warm-up followed by one timed `retrieve` per retriever: BM25 0.088 ms; dense 7.636 ms. This is a local smoke measurement on 8 synthetic passages, not a real-corpus benchmark. |
| P3 corpus integration | Blocked on P3 data | P3 real corpus integration is still pending. The available fixture has 2 synthetic papers and 8 passages. |
| Real-corpus latency | Blocked on P3 data | Synthetic timing cannot establish real-corpus performance. |
| Week 3 retrieval evaluation | Planned for Week 3 | Precision@K, Recall@K, MRR and formal retrieval failure analysis have not been performed. |

### P1 verification evidence

Interpreter: `E:\Miniconda\py311\envs\papergap\python.exe`, Python 3.11.16. Both test commands below used this interpreter with `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`:

| Command | Passed | Failed | Skipped | Reported duration |
| --- | ---: | ---: | ---: | ---: |
| `python -B -m pytest tests/test_p1.py -v` | 122 | 0 | 0 | 5.68 s |
| `python -B -m pytest -q` | 139 | 0 | 0 | 5.72 s |

All 112 pre-existing P1 cases remain; 10 command-line cases were added. The full suite includes the 17 P2 cases. Dense unit tests use deterministic fake encoders and real FAISS; they do not require downloading or running the real embedding model.

The separate real-model check ran the exact build and demo commands in the [README](../README.md#p1-retrieval-week-1--week-2), with `--local-files-only`, CPU and revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. The build produced indexes for 2 synthetic papers / 8 passages with 384-dimensional embeddings under `indexes/p1-week2-synthetic`. The demo loaded these indexes, queried `synthetic-ir` with `Which method uses sparse term matching for passage retrieval?` and `top_k=3`, and returned:

| Rank | Passage ID | BM25 score | Dense cosine score |
| --- | --- | ---: | ---: |
| 1 | `synthetic-ir-001` | 4.270201 | 0.865788 |
| 2 | `synthetic-ir-002` | 0.000000 | 0.706013 |
| 3 | `synthetic-ir-003` | 0.000000 | 0.621847 |

The demo used `time.perf_counter` for one measured `retrieve` after one warm-up per retriever: BM25 **0.088 ms**, dense **7.636 ms**. Dense timing includes query encoding; both timings exclude model loading, passage encoding and index construction. These single-query synthetic measurements do not establish performance on P3's real corpus.

Local ignored artifacts are `results/p1-week2-build.json` and `results/p1-week2-demo.txt`; rerun the README commands to regenerate the outputs. P3 real corpus integration is still pending. No real-corpus retrieval metrics or Week 3 evaluation have been completed.

## P2 real-data integration — 14 October 2026

P1 #4 and P3 #2 are merged. Vishakha's P2 integration now connects their real
QASPER passage pipeline and pinned BGE/FAISS index to RRF and optional BGE
reranking. The corpus check reproduced 32,073 passages / 1,168 indexed papers
and the expected hash. A complete 384-dimensional dense index was built on Metal.

The training-only pilot compares 10/20 candidates per retriever at final top-5
on six fixed training papers. See [P2 commands and measured results](P2_WEEK2.md).
No held-out question content or answer annotations were used for this comparison.
The local native-runtime repair permits the full suite to run without exclusions.
This resolves the earlier real-corpus integration dependency, but does not establish
retrieval quality or mark the team's weekly exit checkpoint complete. Passage/split
contracts and the final evaluation protocol still need affected-owner agreement.

## P4 agent progress — updated 23 October 2026

Owner: Ananya. Merged: [#6](https://github.com/CodeByVish/papergap-rag/pull/6) LangGraph loop on the P2 retrieval API, [#12](https://github.com/CodeByVish/papergap-rag/pull/12) planner and evidence mapper, [#13](https://github.com/CodeByVish/papergap-rag/pull/13) critic, `question_id` and export record, [#14](https://github.com/CodeByVish/papergap-rag/pull/14) gap-driven query rewriter, [#16](https://github.com/CodeByVish/papergap-rag/pull/16) chat-based critic client for P5's Qwen generator, [#17](https://github.com/CodeByVish/papergap-rag/pull/17) static-vs-adaptive experiment harness and real-retrieval smoke test. 130 agent tests pass with fake retrievers and fake LLM clients. The agent has run end to end on real P1/P2 retrieval (10 training questions, no LLM); it has **not** yet run with real Qwen.

| Component | Status | Notes |
| --- | --- | --- |
| Loop and stopping | Implemented | Plan, retrieve, map, critic, rewrite; at most 2 retries (3 rounds); stops early on `INSUFFICIENT_INFORMATION`; every round logged. |
| Planner | Rule-based | Five question types and structured evidence requirements. `unanswerable` is never predicted from the question text. |
| Evidence mapper | Rule-based, weak | `scripts/evaluate_planner.py` on QASPER train (2,593 questions): the plan is satisfied by gold evidence 55.6% of the time but by the five closest non-evidence paragraphs 79.2% (validation: 58.8% vs 79.5%). It cannot separate real evidence from lookalikes, so `evidence_map` is advisory. |
| Critic | Implemented; Qwen prompt unvalidated | System/user prompt, tolerant JSON scan, deterministic validation, rule-based fallback, and `GeneratorChatClient` for P5's shared generator (greedy, thinking off, one larger-budget retry on truncation). `critic_log` records `llm`/`rules`/`fallback` and the raw replies per round. |
| Query rewriter | Implemented | One action per gap label; reuses the paper's own terms and the LLM critic's missing components; never repeats an earlier query. Section-scoped retries wait for P2's PR #10. |
| Experiment harness | Implemented | `src/agent/experiments.py`: static (no retries) vs adaptive arms; evidence recall before/after retries, rounds, gap recovery, unnecessary/ineffective/redundant retries, refusals, paired bootstrap gain. Optional `answer_fn(record) -> dict` runs P5's generation identically on both arms. Needs P3's gold-evidence-to-passage mapping for recall. |
| Real-retrieval smoke test | Run once | `scripts/smoke_agent_real.py` on 6 pilot training papers with the rule-based critic: it accepted 7 of 10 questions in round 1 although only about 25% of approximate gold passages were retrieved, so adaptive retries made no difference. This motivates the Qwen critic; it is not a result. |
| Handoff to P5/P6 | Implemented | `AgentState.question_id`; `src/agent/export.py` writes one JSON record per question including passage text. |

Agreed with P5: refuse without a model call only for `INSUFFICIENT_INFORMATION` or no retrieved passages; every other state generates and keeps `sufficient` as metadata, so both arms share one generation call.

Open items: first run of the critic on real Qwen on the cluster (needs a cluster runner and P5's generator; raw replies are logged so the prompt can be inspected); P2's PR #10 (section-scoped retrieval) before the per-paper section selector can be proposed; P3's gold-evidence mapping for recall metrics; real-data traces on development examples; agent freeze by 25 October. Passage and state schemas remain `v0-proposed`.

## P2 agent/filter/cache increment — 17 October 2026

PR #5 is merged. Added optional exact-section forwarding with a legacy P1
adapter, caller-selected per-round agent sections, compact per-round ID traces
and persistent content/config-keyed reranker scoring. The new real-agent CLI
passed a pinned CPU section-scoped three-round check: first process eight unique
pair misses/four hits; second process zero misses/12 hits. The branch is rebased onto P4's current planner/critic/rewriter; full passages
remain in the export, not the retrieval log. All 436 tests pass; lint and changed-file formatting pass.
See [interface and cache commands](P2_AGENT_CACHE.md). P1/P4 interface review is
pending; this does not freeze proposed shared schemas or evaluation policy.
