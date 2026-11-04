# P4: adaptive retrieval agent

Owner: Ananya. Code in `src/agent/`; schemas stay `v0-proposed`.

## Flow

```text
plan_question -> retrieve -> map_evidence -> critic -> [sufficient | budget spent
                                                        | INSUFFICIENT_INFORMATION] -> END
                    ^                                  \-> rewrite_query -> (back to retrieve)
```

At most 2 retries (3 rounds). Stopping is deterministic: `route_after_critic` ends the
run when the evidence is sufficient, the retry budget is spent, or the critic says the
paper cannot answer (`INSUFFICIENT_INFORMATION`). Every round is logged.

| Step | File | What it does |
| --- | --- | --- |
| Planner | `planner.py` | Rule-based: question type (factual, method, result, comparison, limitation) and structured evidence requirements. Never predicts `unanswerable`; the question text cannot show it. |
| Retrieve | `nodes.py` | Calls the injected `retrieve(query, paper_id, top_k)`; merges and dedupes passages by opaque `passage_id`. With a `section_selector` it scopes the search and, if that finds nothing, repeats the round over the whole paper. |
| Evidence mapper | `nodes.py` | Maps each requirement to passages by section hint or keywords. **Weak and advisory**, see below. |
| Critic | `critic.py` | LLM verdict `{sufficient, gap_label, supporting_passage_ids, missing_components, reason}`, parsed and validated deterministically (a "sufficient" verdict must cite passages it was shown, by short handle `p1`, `p2`, ... that the code maps back to passage ids), with a rule-based fallback. In a runner the critic reads exactly what P5's prompt renders (`--critic-view generator`, the default: `select_passages` and `visible_text` from `src/generation`, today 8 passages cut at 1,200 characters), so a "sufficient" verdict is about text the answer step will see; `--critic-view pool` shows every retrieved passage up to 3,000 characters, for diagnosis only. It judges sufficiency as "states a concrete fact the answer needs; partial counts". A retry that brings no new passage reuses the previous verdict (`source` "reused") instead of asking the model again. |
| Rewriter | `rewriter.py` | One action per gap label. Adds the critic's own content terms for the missing fact (its commentary on the passages is dropped) or, if it gave none, the gap's fixed words, never both; the paper's own recurring terms are added only to avoid repeating an earlier query. Capped at 40 words. |
| Section selector | `sections.py` | Optional. Picks this paper's own section whose name matches the gap's hints; never repeats a section. |

Gap labels: `MISSING_METHOD`, `MISSING_EXPERIMENT_CONTEXT`, `MISSING_RESULT`,
`MISSING_COMPARISON`, `TERMINOLOGY_MISMATCH`, `WEAK_EVIDENCE`, `INSUFFICIENT_INFORMATION`
(plus `NONE`). Only the first four scope a retry to a section.

## Interfaces

- **Retriever in:** any `retrieve(query, paper_id, top_k) -> list[RetrievedPassage]` (P2's
  `HybridRetriever.retrieve`); a `section=` keyword is added only when a selector is given.
- **Critic client in:** `ChatClient.chat(messages)` (preferred) or `LLMClient.complete(prompt)`.
  `GeneratorChatClient(generator)` adapts P5's backend: greedy, `top_p=0.9`, 256 tokens,
  thinking off, one retry with 512 tokens if the reply is cut off.
- **Record out:** `export_record(state)` / `to_jsonl_line(state)` in `export.py`: the full
  terminal state, `retrieved_passages` with text, `question_id`, `evidence_map`, `gap_label`,
  `sufficient`, `retrieval_round`, `retrieval_log` and `critic_log` (with raw model replies).
- **Answer step in:** `answer_fn(record) -> dict`, P5's `make_answer_fn(pipeline)`.
  Refusal rule (agreed with P5): refuse without a model call only for
  `INSUFFICIENT_INFORMATION` or no passages; `sufficient=False` still generates and is
  kept as metadata, so both experiment arms share one generation call.

## Running

Local, rule-based critic, no generation (needs the P2 corpus and index, see `P2_WEEK2.md`):

```bash
OMP_NUM_THREADS=1 python -m scripts.run_agent_experiment \
  --passages data/processed/p2-training-pilot-passages.jsonl \
  --dense-index-dir indexes/p2-training-pilot \
  --from-qa data/processed/qa.jsonl --split train --limit 20 \
  --out-dir results/p4-local-001
```

`OMP_NUM_THREADS=1` avoids the FAISS and PyTorch duplicate-OpenMP crash seen on macOS.
The test split is refused. Cluster, with the Qwen3-8B critic and P5's answers
(`--critic generator --generator vllm --model-id ... --answers p5`):
`sbatch scripts/cluster/run_agent_experiment.sbatch`. The job installs nothing; its
preflight lists missing packages. One engine is shared by critic and answers (one A40
fits one 8B model). Records are written per question; add `RESUME=1` to continue.

Cluster environment (from P5, who validated the pins): `python312`, `vllm==0.11.0`,
`transformers>=4.51.0,<5`. The cap matters, because vLLM 0.11 fails at model load under
transformers 5. Add the retrieval packages in one command with the cap restated and read the
`--dry-run` list first (it must not touch torch or install transformers 5):

```bash
"$VLLM_PY" -m pip install --dry-run "faiss-cpu==1.15.1" "sentence-transformers==5.7.0" \
  "rank-bm25==0.2.2" "transformers>=4.51.0,<5"
```

The runner uses P5's frozen settings: prompt `p5-grounded-qa-v7` (the run stops if the checkout
differs, `--expect-prompt-version`) and `--max-new-tokens 1024`. It loads the vLLM engine
before the retrieval models and keeps those on the CPU, because vLLM checks free GPU memory
at load. The corpus and dense index are not on the cluster yet; copy them from P1's outputs.
`prompt_version` is recorded in `run_manifest.json`.

Outputs in `--out-dir`: `static.jsonl`, `adaptive.jsonl`, `metrics.json`, `metrics.md`,
`run_manifest.json` (arguments, git commit, package versions, file hashes, critic call counts).

## Live demo

P5's Option C server needs a hook to run the agent per typed question: `src/agent/demo.py`
(`make_record_fn`) and `scripts/demo_agent_factory.py`. The server change and the open checks are in
`docs/handoffs/P4_AGENT_DEMO_HOOK_20261030.md`.

## Measures (`src/agent/experiments.py`)

Static = one round, rule-based critic (`max_retries=0`); adaptive = up to 2 retries.
Reported per arm: evidence recall before and after retries, average rounds, critic gap
recovery (first verdict insufficient, final sufficient), full-recall recovery, unnecessary
retries (all gold already retrieved), ineffective retries (no new gold), redundant retries
(nothing new at all), refusal rate (and correct/false refusals given answerability),
critic fallback rate and the share of verdicts reused, answer errors, and a paired bootstrap recall gain.

The adaptive arm can collect more passages than the static one (up to top-k x 3). To check that
a recall gain is not just extra text, add the control arm `--arms static adaptive static-wide`:
a one-round static run with `--wide-k` passages (default top-k x (max-retries + 1)). The summary
then also holds `matched_recall_gain`: per question, adaptive final recall minus static recall
over the same number of passages, with a bootstrap CI.
Recall needs gold evidence mapped to passage IDs (P3); without it recall is `n/a`.
`--from-qa` runs use an approximation (`approximate_gold`). For gold from P3's mapping
(`gold-evidence-to-passage-v0-proposed`) build an items file and pass it with `--items`:

```bash
python -m scripts.make_dev_items --mapping gold_evidence_mapping_all_splits.jsonl \
    --passages passages.jsonl --qa qa.jsonl --split train --answerable 32 --unanswerable 8 \
    --out items.jsonl
```

The mapping's gold IDs exist only in the **365/40-word corpus** that P3 selected on 28 October
(21,360 development passages). None of them occur in the 200/40-word corpus of 17 October
(32,073 passages), so the script stops when the IDs do not match `--passages`. The index the
agent searches must be built on the same 365/40 corpus. The test split is refused.

## Retrieval depth: the static baseline to beat

Recall of plain retrieval (the question as the query, hybrid RRF with the shipped defaults, no
reranker, no critic, no retry) on the 32 development items with P3 gold, measured offline on the
rebuilt 365/40 corpus and reproducible with `scripts/evaluate_retrieval_depth.py`:

| top-k | 3 | 5 (shipped default) | 8 | 10 | 15 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mean gold recall | 0.599 | 0.740 | 0.885 | **0.974** | 0.974 |
| questions with full recall | 17/32 | 22/32 | 26/32 | 30/32 | 30/32 |

- The adaptive loop of job 50701 reached 0.802 reading about 6 passages. Plain top-10 reaches 0.974, so
  the loop has to be compared with a static baseline at depth 8-10, not 5. Add the control arm with
  `--arms static adaptive static-wide --wide-k 10`.
- `candidate_k` 10/20/40 and `rrf_k` 30/60/90 move recall@5 between 0.74 and 0.80 (one or two
  questions), so they were not tuned. Depth is what matters: 6 of 32 questions have their best gold
  passage at rank 6-10.
- An ideal stopping rule (stop at the smallest of 3/5/8/10/15 that holds all gold) reads 5.56
  passages for the same 0.974. That is the most an adaptive loop can save over static top-10; the
  Qwen critic is far from it.
- The reranker is not covered here (its weights were not available offline). On the cluster, rerun
  with `--bge` to see whether reranking moves gold into the top 5.
- **Generation budget (P5, frozen v7).** `PromptConfig` uses `max_passages=8` and
  `max_chars_per_passage=1200`, sized for the old 200/40 chunks. With 365/40 chunks a top-10 run
  would lose its last two passages, and every passage is cut at 1200 characters (71% of the gold
  passages are longer, 28% of their text on average). Raise both with P5 before an answer-quality run.

## Abstention

The critic returned INSUFFICIENT_INFORMATION for 2 of 81 verdicts, so only 1 of 8 unanswerable
questions was refused (and 1 of 32 answerable ones). On job 50701 the alternative rule "refuse if the
critic is still unsatisfied after the last round" would refuse all 8 unanswerable questions but also
12 of 32 answerable ones (37.5%), because the critic was over-strict. It is not enabled.
Every question the critic called sufficient was answerable, so the rule becomes usable once
`unsatisfied_rate_answerable` (reported per run beside `unsatisfied_rate_unanswerable`) falls
well below that; decide after the next run of the calibrated critic.

## Known limits

- **The rewrite is not what limits recall.** Job 50701 was replayed offline (the 365/40 corpus rebuilt,
  the cluster's round-1 and round-2 retrievals reproduced exactly, the critic's recorded verdicts
  injected). Five rewrite strategies, including re-asking the plain question, land between 0.77 and
  0.82 recall at about 6 passages; the original query with top-10 and no retry reaches 0.974. The gold
  passages sit at ranks 6-10 of the plain query.

- The rule-based mapper cannot tell evidence from lookalikes: on QASPER train a plan is
  satisfied by gold evidence 55.6% of the time and by the five closest non-evidence
  paragraphs 79.2% (`scripts/evaluate_planner.py`). `evidence_map` is advisory, and the
  rule-based critic accepts most questions in round 1.
- The first two real critic runs (jobs 50550 and 50701, 40 development questions) gave valid JSON every
  time, but the critic was over-strict: in 23 of its 39 "insufficient" verdicts all gold passages were
  already retrieved, and it saw only the first 1,200 characters of each passage, cutting 28% of the
  text of the gold passages. The calibrated prompt, the 3,000-character view and the cited-passage
  check were written for that and have **not yet been run on the real model**; compare them with
  `runs/p4/critic-second-40` on the same items before relying on them.
- Exact section names such as "Results" exist in about 20% of papers. The selector matches
  hints against each paper's own names (about 86% of papers have a result-like section).
- Reranker caches make repeat latency unrepresentative; use a fresh cache path for timings.
- Never tune on held-out labels; use development questions for prompt and parameter changes.
