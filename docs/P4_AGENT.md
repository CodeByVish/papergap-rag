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
| Critic | `critic.py` | LLM verdict `{sufficient, gap_label, missing_components, reason}`, parsed and validated deterministically, with a rule-based fallback. |
| Rewriter | `rewriter.py` | One action per gap label; adds the paper's own recurring terms and the LLM critic's missing components; never repeats an earlier query. |
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

Outputs in `--out-dir`: `static.jsonl`, `adaptive.jsonl`, `metrics.json`, `metrics.md`,
`run_manifest.json` (arguments, git commit, package versions, file hashes, critic call counts).

## Measures (`src/agent/experiments.py`)

Static = one round, rule-based critic (`max_retries=0`); adaptive = up to 2 retries.
Reported per arm: evidence recall before and after retries, average rounds, critic gap
recovery (first verdict insufficient, final sufficient), full-recall recovery, unnecessary
retries (all gold already retrieved), ineffective retries (no new gold), redundant retries
(nothing new at all), refusal rate (and correct/false refusals given answerability),
critic fallback rate, answer errors, and a paired bootstrap recall gain.
Recall needs gold evidence mapped to passage IDs (P3); without it recall is `n/a`.
Development runs use an approximation (`approximate_gold`), not P3's mapping.

## Known limits

- The rule-based mapper cannot tell evidence from lookalikes: on QASPER train a plan is
  satisfied by gold evidence 55.6% of the time and by the five closest non-evidence
  paragraphs 79.2% (`scripts/evaluate_planner.py`). `evidence_map` is advisory, and the
  rule-based critic accepts most questions in round 1.
- The Qwen critic prompt has not yet been validated on the real model.
- Exact section names such as "Results" exist in about 20% of papers. The selector matches
  hints against each paper's own names (about 86% of papers have a result-like section).
- Reranker caches make repeat latency unrepresentative; use a fresh cache path for timings.
- Never tune on held-out labels; use development questions for prompt and parameter changes.
