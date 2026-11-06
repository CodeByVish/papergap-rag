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
| Critic | `critic.py` | LLM verdict `{sufficient, gap_label, supporting_passage_ids, missing_components, reason}`, parsed and validated deterministically (a "sufficient" verdict must cite passages it was shown, by short handle `p1`, `p2`, ... that the code maps back to passage ids) and must quote, word for word, the sentence that states the key fact, which is checked against the text the critic was shown, with a rule-based fallback. In a runner the critic reads exactly what P5's prompt renders (`--critic-view generator`, the default: `select_passages` and `visible_text` from `src/generation`, today 8 passages cut at 1,200 characters), so a "sufficient" verdict is about text the answer step will see; `--critic-view pool` shows every retrieved passage up to 3,000 characters, for diagnosis only. It judges sufficiency as "states a concrete fact the answer needs; partial counts". A retry that brings no new passage reuses the previous verdict (`source` "reused") instead of asking the model again. |
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
  `sufficient`, `retrieval_round`, `retrieval_log` and `critic_log` (with raw model replies),
  and, since the last node was added, `stop_reason` (`sufficient`, `insufficient_information` or
  `max_rounds`) with `max_rounds` (the round budget, `max_retries + 1`). A static run (`max_rounds`
  1) that is not satisfied also stops with `max_rounds`, so a rule meant for the adaptive loop
  must test `stop_reason == "max_rounds"` and `max_rounds > 1`. Both fields are additive and
  `None` in records written before this change.
- **Answer step in:** `answer_fn(record) -> dict`, P5's `make_answer_fn(pipeline)`.
  Refusal rule (agreed with P5): refuse without a model call only for
  `INSUFFICIENT_INFORMATION` or no passages; `sufficient=False` still generates and is
  kept as metadata, so both experiment arms share one generation call.

## Running

Local smoke test, rule-based critic, no generation. The pilot sample below is small and comes from the
old 200/40 build, which is fine for checking wiring but not for any result; a real run needs the 365/40
corpus and a dense index built on it (see "Corpus" below):

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

## Corpus

Every result in this repository's P4 work uses the **365/40-word development corpus**: 21,360 passages from
1,168 papers, SHA-256 `ecb1c601cdaebcd8e1e6bfeaf43f9cb4867f89e9762799ab06e7901549a9e403`. It is built with

```bash
python -m scripts.build_corpus --papers data/processed/papers.jsonl \
  --export-manifest data/processed/qasper_export.manifest.json --scope development \
  --chunk-size-words 365 --chunk-overlap-words 40 --output ... --manifest-output ...
```

The builder's own defaults are still the old 200/40 (32,073 passages), so the two flags are not optional.
Passage ids are content hashes, so ids from one corpus do not exist in the other. The runner stops when
an items file names gold passages the corpus lacks, and the dense index must be built on the same file.

## Live demo

P5's Option C server needs a hook to run the agent per typed question: `src/agent/demo.py`
(`make_record_fn`) and `scripts/demo_agent_factory.py`. The server change and the open checks are in
`docs/handoffs/P4_AGENT_DEMO_HOOK_20261030.md`. `PAPERGAP_CORPUS`, the dense index and the server's
`--passages-from` must all be the 365/40 corpus: the agent returns 365/40 passage ids, which a `/passages`
index built on the old 32,073-passage file (still named in P5's 29 Oct handoff) cannot resolve.

Checked locally on 4 November: P5's `origin/p5/demo-service` server merged with `main` in a scratch tree
(merges cleanly), the mock generator, the 40-paper development corpus and index, `fastapi` and `uvicorn`
installed outside the project. `/health` reports `"agent": true`. A question sent with
`scripts/demo_client.py` returns 200 with a cited answer, and all 3 cited passage ids resolve through
`/passages` (365/40 corpus). The log line `agent <id>: rounds=1 retrieved=10 critic=[(1, 'fallback', 8)]`
shows the critic reading the generator's 8 of 10 retrieved passages; with `DEMO_AGENT_CRITIC_VIEW=pool` it
shows 10. (that check predates the passthrough: the server then called the hook as `record_fn(question, paper_id)` and
its `--top-k` did not reach the agent; the hook is now `record_fn(question, paper_id, top_k, request_id)`
(PR #27) and the demo depth defaults to 8, PR #54). Not verified in that local check: the Qwen critic through vLLM, GPU
memory with the retrieval models beside the engine, latency with the real critic (about 7 s per question
here, mock critic), the SSH tunnel. Since then `--record-fn` and the top-k passthrough are on main (PR #27), and P5 ran the demo on
the cluster on 5 November (jobs 51185 and 51186): with the default critic view the critic reads 8 passages,
with `DEMO_AGENT_CRITIC_VIEW=pool` it reads 10 at top-k 10, and both returned an answer with citations in
about 34 s.

## Measures (`src/agent/experiments.py`)

Static = one round, rule-based critic (`max_retries=0`); adaptive = up to 2 retries.
Reported per arm: evidence recall before and after retries, average rounds, critic gap
recovery (first verdict insufficient, final sufficient), full-recall recovery, unnecessary
retries (all gold already retrieved), ineffective retries (no new gold), redundant retries
(nothing new at all), refusal rate (and correct/false refusals given answerability),
critic fallback rate and the share of verdicts reused, mean passages read, answer errors, and a paired bootstrap recall gain.

The adaptive arm can collect more passages than the static one (up to top-k x 3). To check that
a recall gain is not just extra text, add the control arm `--arms static adaptive static-wide`:
a one-round static run with `--wide-k` passages (default top-k x (max-retries + 1)). The summary
then also holds `matched_recall_gain`: per question, adaptive final recall minus static recall
over the same number of passages, with a bootstrap CI.
With the `static-wide` arm `metrics.md` also lists the plain question at depth 3, 5, 8, 10 and 15
(`static_depth_recall`, one run, no extra cost) with the adaptive arm's recall and mean passages
beneath it, and prices the refusal rule below (`refuse_if_unsatisfied`). Compare the adaptive arm with
the row of the same depth, never with top-5 alone.
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

| top-k | 3 | 5 (development default) | 8 | 10 | 15 |
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

Not enabled. The critic returns INSUFFICIENT_INFORMATION rarely (1 of 69 verdicts in job 50977), so on its
own it refuses 1 of 8 unanswerable questions. The alternative rule, "refuse if the critic is still
unsatisfied after the last round", was priced on three runs:

| run | refuses unanswerable | refuses answerable (wrongly) |
| --- | ---: | ---: |
| job 50701, original critic | 8/8 | 12/32 |
| job 50977, calibrated critic | 4/8 | 5/32 (15.6%) |
| job 51172, generator view, handles, quote check | 6/8 | 9/32 (28.1%) |

Gate, put to the team on 5 November (no objection) and fixed before any held-out run: the rule is enabled only if,
on development questions, it refuses at least 50% of the unanswerable ones and at most 5% of the
answerable ones (`PROPOSED_REFUSAL_MIN_CORRECT`, `PROPOSED_REFUSAL_MAX_FALSE`). `metrics.md` and
`metrics.json` report `meets_proposed_gate` for every run. Until it holds, refusal stays with P5's
generator, which refuses on its own evidence. Tune only on development questions; once the rule and
thresholds are frozen they must not change after the held-out labels are read.

**Decision (5 November): the gate is not met in any run, so the rule stays off.** Job 51172 refuses 6 of 8
unanswerable questions but also 9 of 32 answerable ones; the limit allows 1. P5 may add the rule as an
option that is off by default, under its own refusal code, keyed on `stop_reason == "max_rounds"` and
`max_rounds > 1` (the static arm also ends on its round budget).

What the answers run (job 51175, `ANSWERS=p5`, same items) adds, adaptive arm: the generator refuses 3 of 8
unanswerable questions on its own (the static arm refuses the same 3) and answers all 9 answerable
questions that the critic left unsatisfied. Switching the rule on would add 3 refusals of unanswerable
questions and replace those 9 answers with refusals. Whether the 9 answers are correct has not been
checked (the development items carry no gold answer text).

Critic audit, job 51172 against job 50977 (adaptive arm, verdicts with gold or unanswerable known):

| verdict / situation | job 50977 | job 51172 |
| --- | ---: | ---: |
| insufficient, all gold in view (over-strict) | 9 | 19 (8 questions; 5 before) |
| insufficient, gold not yet retrieved (correct) | 13 | 12 |
| sufficient, all gold in view (correct) | 21 | 16 |
| sufficient, gold missing (false accept) | 6 | 7 |
| insufficient, unanswerable (correct) | 8 | 12 |
| sufficient, unanswerable (false accept) | 4 | 2 |

Truncation does not explain the over-strict verdicts: the gold passage is longer than 1200 characters in 65%
of them and in 75% of the correct "sufficient" verdicts. Two verdicts fell back to the rules (one failed
quote check, one reply with an invalid `\%` escape in a LaTeX quote): 2.9% of verdicts.

## What the results support

Job 50977, 40 development questions (32 with gold), Qwen3-8B critic, adaptive against plain retrieval:

| claim | supported? | evidence |
| --- | --- | --- |
| Adaptive recovers more gold than static top-5 | Weakly | 0.740 to 0.802; paired gain +0.0625, 95% CI [0.0, 0.156]; two questions |
| Adaptive beats plain retrieval reading the same number of passages | **No** | matched gain -0.010, CI [-0.094, 0.083] at 5.7 passages |
| Adaptive beats a well-set static baseline | **No** | plain top-8 0.885, top-10 0.974, against 0.802 |
| The calibrated critic wastes fewer retries | Yes | retries 41 to 27, unnecessary 55.6% to 38.9%, model calls fewer |
| The loop reliably refuses unanswerable questions | **No** | 1 of 8 refused by the critic; the unsatisfied rule fails the gate |

Job 51172 (generator view, handles, quote check; 4 November) gives the same picture: adaptive recall 0.771 at
5.95 passages, against 0.740 for plain top-5, 0.885 for top-8 and 0.974 for top-10; the loop still does not
beat plain retrieval, and the refusal rule still fails the gate (above).

Write the results as: the critic and loop spend fewer passages and model calls than before and match
plain retrieval at equal budget, but on this slice reading more passages up front is better than retrying.
Do not write that adaptive retrieval improves recall unless a later run clears the matched-budget
comparison. Report the static baseline at depth 5, 8 (the generator takes at most 8 passages) and 10,
not at 5 alone. Dev results of 32 questions have wide intervals; the held-out set decides.

## Known limits

- **A lenient critic.** After the calibration of job 50977 the critic accepted 4 of 8 unanswerable
  questions and called 6 answerable ones sufficient with gold still missing; 8 of 26 sufficient
  verdicts cited no gold passage. How much of a question's wording a cited passage shares does not
  tell these apart (gold-citing 0.0-1.0, lookalike-citing 0.0-1.0), so no lexical guard was added.
  Instead a sufficient verdict must now quote a sentence that states the key fact and the code checks
  the quote occurs in the cited text (`quote_supported`, tolerant of punctuation, one changed word
  and "..." elisions). **Not yet run on the real model.** Watch `critic_fallback_rate` (a model that
  cannot quote falls back to the rules; above about 10% the instruction needs rewording), the number
  of unanswerable questions ending sufficient, and `unsatisfied_rate_answerable`.

- **The rewrite is not what limits recall.** Job 50701 was replayed offline (the 365/40 corpus rebuilt,
  the cluster's round-1 and round-2 retrievals reproduced exactly, the critic's recorded verdicts
  injected). Five rewrite strategies, including re-asking the plain question, land between 0.77 and
  0.82 recall at about 6 passages; the original query with top-10 and no retry reaches 0.974. The gold
  passages sit at ranks 6-10 of the plain query.

- The rule-based mapper carries no usable signal. `scripts/evaluate_planner.py` checks whether a plan is
  satisfied by gold evidence more often than by lexical lookalikes of the same paper. Compared with as many
  lookalikes as there are gold units (the fair comparison; "any of five" overstates the gap), on the 365/40
  chunks the agent actually maps: train 67.4% for gold against 69.6% for lookalikes, validation (P3's 200 held-out questions left
  out with `--exclude-ids`, n=810) 70.5% against 72.0%. On raw paragraphs gold is 54.9% against 60.9% (train, n=2,095). Per type there is some signal for
  result (81.0% against 70.7%) and comparison (72.8% against 63.6%) questions, none for factual ones (65.2%
  against 73.9%), the largest class. `evidence_map` is advisory, and the rule-based critic accepts most
  questions in round 1. Chunk level uses `--passages`; a chunk is gold if it contains a whole evidence
  paragraph or its first or last 12 words, which reproduces P3's mapping ids exactly on the 32 development
  items (45 of 45).
- Real-model status. Jobs 50550 and 50701 (40 development questions, Qwen3-8B critic) gave valid JSON
  every time but an over-strict critic: in 23 of 39 "insufficient" verdicts all gold was already retrieved,
  and it saw only 1,200 characters of each passage. Job 50977 ran the calibrated critic (whole passages,
  a defined bar for "sufficient", cited ids): that count fell to 9 and retries from 41 to 27, but leniency
  rose (see above). The generator-view alignment, short handles and the quote requirement (#34) have **not
  yet been run on the real model**; compare the next run with `runs/p4/critic-third-40`.
- Exact section names such as "Results" exist in about 20% of papers. The selector matches
  hints against each paper's own names (about 86% of papers have a result-like section).
- Reranker caches make repeat latency unrepresentative; use a fresh cache path for timings.
- Never tune on held-out labels; use development questions for prompt and parameter changes.
- **Depth.** Development tuning and jobs 50701, 50977 and 51172 were at top-k 5; the frozen held-out run
  (job 51585, 6 November, run once and scored) is at top-k 8 (`configs/p4_freeze.json`), checked once on the
  development items (job 51521).
- **The dense encoder truncates at 512 tokens.** `_INDEX_SETTINGS["max_seq_length"] = 512` in
  `src/retrieval/dense_retriever.py` is the bge-small maximum, so a longer passage is embedded from its first
  512 tokens only; BM25 reads all of it. On the 365/40 chunks 14.7% of the development passages (3,142 of
  21,360) and 14.3% of the all-paper-text passages (4,099 of 28,617) are longer, losing 84 to 88 tokens on
  average, and 14 of the 45 development gold passages (31%) are affected (about 52 tokens lost). Effect on
  recall untested; the chunking is frozen, so the report states it as a limitation.
