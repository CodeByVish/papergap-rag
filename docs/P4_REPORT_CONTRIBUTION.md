# P4 report contribution — draft for P6

## Agent: evidence-gap-driven retrieval

PaperGap's agent decides whether the passages retrieved so far are enough to answer a question and,
if not, names what is missing and searches again. This chapter describes the design, the experiments
on development questions, what they show, and what they do not show. All numbers below are
development results; **no held-out question has been run** (see "Status of the numbers").

### 1. Design

The agent is a LangGraph state machine over one paper:

```
plan_question -> retrieve -> map_evidence -> critic -> [stop | rewrite_query -> retrieve ...]
```

| Component | What it does |
| --- | --- |
| Planner | Rule-based. Assigns one of five question types (factual, method, result, comparison, limitation) and the evidence requirements an answer needs (`method`, `experiment_context`, `result`, `comparison`, `limitation`, `direct_answer`). It never predicts "unanswerable": the question text cannot show that. |
| Retrieve | P2's hybrid retriever inside the selected paper: BM25 and the pinned `BAAI/bge-small-en-v1.5` dense retriever, 20 candidates each, fused with RRF (k = 60), top 5 per round. Passages accumulate across rounds and are de-duplicated by passage id. |
| Evidence mapper | Rule-based; maps each requirement to retrieved passages by section name or keywords. Advisory only (see "Limitations": it cannot tell evidence from lookalikes). |
| Critic | `Qwen/Qwen3-8B` (thinking off, temperature 0) returns one JSON verdict: `sufficient`, one of eight gap labels, the passages it relies on, an evidence quote, what is missing, and a reason. The reply is parsed and validated by code; two bad replies fall back to a rule-based check. |
| Rewriter | One action per gap label: add the critic's own terms for the missing fact, or the gap's fixed vocabulary (method, dataset/setup, results, baselines); never repeats an earlier query. |
| Section selector | Optional. Restricts the retry to this paper's own section whose name matches the gap (for example a results section), falling back to the whole paper if that finds nothing. |
| Router | Deterministic. Stop when the critic says sufficient, says the paper cannot answer (`INSUFFICIENT_INFORMATION`), or the retry budget is spent: at most 2 retries, 3 rounds. |

Gap labels: `NONE`, `MISSING_METHOD`, `MISSING_EXPERIMENT_CONTEXT`, `MISSING_RESULT`,
`MISSING_COMPARISON`, `TERMINOLOGY_MISMATCH`, `WEAK_EVIDENCE`, `INSUFFICIENT_INFORMATION`.

**Making the critic's judgement checkable.** An LLM verdict of "sufficient" is only useful if it can be
audited, so the code does not take it on trust:

- The critic reads exactly the passages and text that P5's generator will render (8 passages, each cut
  at 1,200 characters), so "sufficient" is about evidence the answer step can use.
- It cites passages by short handle (`p1`, `p2`, ...), which the code maps back to passage ids; a
  citation to a passage it was not shown is rejected.
- A sufficient verdict must quote, word for word, the sentence that states the key fact, and the code
  checks that the quote occurs in the cited text (tolerant of punctuation, one changed word, and "..."
  elisions). A rejected reply is retried once, then the rule-based check decides.
- If a retry brings no new passage the critic would see identical input, so its previous verdict is
  reused instead of calling the model again.

The same code serves the live demo: P5's server calls `record_fn(question, paper_id)` and the agent
runs the whole loop before generation.

### 2. Experimental setup

**Corpus and gold.** The 365/40-word development corpus (365-word chunks, 40-word overlap): 21,360
passages from 1,168 papers, SHA-256 `ecb1c601cdaebcd8e1e6bfeaf43f9cb4867f89e9762799ab06e7901549a9e403`.
Gold passages come from P3's evidence-to-passage mapping (`gold-evidence-to-passage-v0-proposed`; the
mapping and the split roles remain proposals until the team confirms them).

**Development items.** 40 questions from the official QASPER train split, spread evenly over 39 papers: 32 answerable questions with gold (45 gold passages, 1.4 per question) and 8
unanswerable questions (items file SHA-256 `ff69f9a0...`). None of the 40 questions or their papers
appears in P3's frozen held-out list (`qa_for_held_out_v2`, checked on 4 November).

**Arms.** All arms use the same retriever, corpus and questions.

- *static*: one round, top 5, no critic.
- *adaptive*: the full loop above, up to 3 rounds.
- *static-wide*: one round with 15 passages; its first *k* passages are the plain-retrieval baseline at
  every depth *k*, from a single run.

**Metrics.** *Recall*: share of a question's gold passages among the distinct passages retrieved
(mean over the 32 questions with gold). *Full recall*: questions with every gold passage. *Unnecessary
retry*: a retry made when all gold was already retrieved. *Ineffective retry*: a retry that added no
gold. *Redundant retry*: a retry that added no new passage. *Matched-budget gain*: per question, the
adaptive arm's final recall minus the plain ranking's recall over the same number of passages the
adaptive arm ended with. Intervals are 95% paired bootstrap intervals (2,000 resamples) over the 32
questions.

**Compute.** One GPU per job (A40 for the first run, L40S for later ones), Qwen3-8B in bfloat16 through
vLLM 0.11.0 (transformers 4.57.6, torch 2.8.0), one engine shared by critic and answers, run by P5 on
the cluster. Retrieval ran on CPU. A complete three-arm job of 40 questions takes about 9 minutes.

**Procedure.** Every tuning decision below was made on these 40 development questions; none used
held-out questions or labels. The rule-based mapper was evaluated, not tuned, on all QASPER train
questions and on validation questions without P3's held-out list.

### 3. Results

#### 3.1 The adaptive loop against plain retrieval

Three cluster jobs on the same 40 questions: job 50701, job 50977 after the critic was recalibrated, and job
51172 after the critic was changed to read the generator's own view of the passages, cite them by handle and
quote its evidence.

| | static | adaptive, job 50701 | adaptive, job 50977 | adaptive, job 51172 | static-wide (15) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean gold recall | 0.740 | 0.802 | 0.802 | 0.771 | 0.974 |
| Questions with full recall | 22/32 | 24/32 | 24/32 | 23/32 | 30/32 |
| Mean passages read (all 40 questions) | 5.0 | 5.9 | 5.7 | 5.95 | 13.4 |
| Mean rounds | 1.00 | 2.03 | 1.68 | 1.90 | 1.00 |
| Retries | 0 | 41 | 27 | 36 | 0 |
| Unnecessary retries (of retries with gold) | n/a | 55.6% | 38.9% | 56.5% | n/a |
| Ineffective retries | n/a | 92.6% | 88.9% | 95.7% | n/a |
| Redundant retries (nothing new) | n/a | 34.1% | 22.2% | 22.2% | n/a |
| Agent time per question (s) | < 0.1 | 10.9 | 12.3 | 6.1 | < 0.1 |

- **Over static top-5**, the adaptive arm gains 0.0625 recall (95% CI 0.0 to 0.156) in jobs 50701 and
  50977, which comes from two of the 32 questions, and 0.031 (CI 0.0 to 0.094) in job 51172, one question.
- **Against the same number of plain-retrieval passages**, the matched-budget gain is −0.042 (CI −0.115
  to 0.0) in job 50701, −0.010 (CI −0.094 to 0.083) in job 50977 and −0.042 (CI −0.135 to 0.062) in job
  51172, at 5.9 passages: no gain.
- **Recalibrating the critic made the loop cheaper**: retries fell from 41 to 27 and unnecessary retries from
  55.6% to 38.9% at unchanged recall. **The generator-view change gave that back**: job 51172 has 36
  retries, 56.5% unnecessary, and slightly lower recall (0.771). Job 51172 also ran on an L40S, so its
  agent time per question is not comparable with the earlier jobs.
- The first cluster job (50550) showed the same recall change, 0.740 to 0.802, and 81 of 81 critic
  replies valid JSON, but its rewriter appended the critic's full sentences ("... not clearly described
  in the retrieved passages") to the search query; that defect was fixed before job 50701.

#### 3.2 Reading more passages beats retrying

Recall of the plain question (hybrid retrieval, no critic, no retry) at each depth:

| top-k | 3 | 5 (default) | 8 | 10 | 15 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean gold recall | 0.599 | 0.740 | 0.885 | **0.974** | 0.974 |
| Questions with full recall | 17/32 | 22/32 | 26/32 | 30/32 | 30/32 |

Six of the 32 questions have their best gold passage at ranks 6 to 10. The fusion constants hardly
matter: candidate pools of 10, 20 or 40 and RRF constants of 30, 60 or 90 move recall@5 by one or two
questions (0.74 to 0.80), so they were not tuned. An ideal stopping rule (stop at the smallest of
3/5/8/10/15 that holds all gold) would read 5.56 passages for the same 0.974, which bounds what any
critic can save over top-10; the Qwen critic is far from that bound. The cross-encoder reranker lowered
recall at every depth in P5's paired run on the same items and corpus (top-5: 0.724 against 0.740;
top-10: 0.885 against 0.974), so the final configuration uses RRF without reranking.

#### 3.3 What the critic gets wrong

Each critic verdict compared with whether all gold passages had been retrieved at that point (verdicts
asked of the model; reused verdicts excluded):

| Verdict and situation | job 50701 | job 50977 | job 51172 |
| --- | ---: | ---: | ---: |
| "Insufficient" although all gold was already retrieved (over-strict) | 23 | 9 | 19 |
| "Insufficient", gold still missing (correct) | 16 | 13 | 12 |
| "Sufficient", all gold retrieved (correct) | 16 | 21 | 16 |
| "Sufficient", gold missing (false accept) | 4 | 6 | 7 |
| "Insufficient" on an unanswerable question | 22 | 8 | 12 |
| "Sufficient" on an unanswerable question (false accept) | 0 | 4 | 2 |

Two defects explain the first job: the critic saw only the first 1,200 characters of each passage
(71% of gold passages are longer, and it lost 28% of their text on average), and its prompt asked for
"clear, detailed" coverage without defining a bar. Fixing both cut the wasted retries from 23 to 9 but
made the critic lenient: it now accepts 4 of 8 unanswerable questions, and 8 of 26 sufficient verdicts on
answerable questions cite no gold passage. Recall did not change, because one question was gained and one
lost. How much of the question's wording a cited passage shares does not separate good verdicts from
bad ones (gold-citing and lookalike-citing verdicts both range from 0.0 to 1.0), so no lexical guard was
added.

Job 51172 ran the critic on the generator's own view (8 passages of at most 1,200 characters), with
passage handles and a quote that must occur in the cited passages. It accepted fewer unanswerable
questions (2 of 8, from 4) and was stricter on answerable ones: 19 over-strict verdicts, which come from 8
questions (5 in job 50977), because every retry of an unsatisfied question is judged again. Truncation does
not explain this: the gold passage is longer than 1,200 characters in 65% of the over-strict verdicts and in
75% of the correct "sufficient" ones. Of 68 verdicts asked of the model, 2 (2.9%) fell back to the rules:
one failed the quote check and one reply contained a LaTeX `\%` that made the JSON invalid. Of the sufficient
verdicts, 12 cite a gold passage and 9 cite none. Of the 9 answerable questions the critic left
unsatisfied, 3 had the answer in view: for "Where did they get the data?", the gold passage says the
dataset was built by distant supervision from Twitter, and the critic still asked for the source.

#### 3.4 Rewriter

Replaying job 50701 offline (the cluster's round-1 and round-2 retrievals were reproduced exactly) with
five different query strategies, including asking the plain question again, gave recall between 0.77
and 0.82 at about 6 passages. The wording of the retry is not what limits recall.

#### 3.5 The rule-based evidence mapper

The mapper checks whether a plan's requirements are satisfied by a set of passages. For questions with
known gold, it accepts the gold chunks about as often as it accepts the same number of lexically
similar non-gold chunks:

| Plan accepted by | gold | as many lookalikes as gold |
| --- | ---: | ---: |
| QASPER train, 365/40 chunks (n = 2,095) | 67.4% | 69.6% |
| QASPER validation, 365/40 chunks, held-out questions excluded (n = 810) | 70.5% | 72.0% |
| QASPER train, raw paragraphs (n = 2,095) | 54.9% | 60.9% |

There is some signal for result questions (81.0% against 70.7%) and comparison questions (72.8%
against 63.6%), none for factual questions (65.2% against 73.9%), the largest class. Comparing gold with
the *five* closest lookalikes, as an earlier version of this analysis did, overstates the gap because
"any of five" is easier to satisfy than "any of one or two". The mapper is therefore advisory and the
LLM critic does the judging.

#### 3.6 Abstention

The critic returned `INSUFFICIENT_INFORMATION` rarely (1 of 67 verdicts in job 50977), so it refused 1 of
8 unanswerable questions and 0 of 32 answerable ones. The alternative rule, "refuse if the critic is
still unsatisfied after the last round", would refuse 8 of 8 unanswerable questions and 12 of 32
answerable ones with the original critic, and 4 of 8 and 5 of 32 (15.6%) with the recalibrated one. A
gate of at least 50% of unanswerable and at most 5% of answerable questions was put to the team on 5
November, with no objection. With the generator-view critic (job 51172) the rule would refuse 6 of 8
unanswerable and 9 of 32 answerable questions (28.1%), so the gate is not met in any of the three runs. The
rule is **not enabled**, and refusal stays with P5's generator.

With generated answers (job 51175, same questions), the generator refuses 3 of 8 unanswerable questions on
its own in both the static and the adaptive arm, so the loop adds nothing there. It answers, with
citations, all 9 answerable questions that the critic left unsatisfied. Switching the rule on would add 3
refusals of unanswerable questions and replace those 9 answers with refusals. Whether the 9 answers are
correct has not been checked: the development items carry no gold answer text.

#### 3.7 What the evidence supports

| Claim | Supported? | Evidence |
| --- | --- | --- |
| Adaptive recovers more gold than static top-5 | Weakly | 0.740 to 0.771 (job 51172; 0.802 in 50977); paired gain +0.031, CI [0.0, 0.094]; one question |
| Adaptive beats plain retrieval reading the same number of passages | No | matched gain −0.042, CI [−0.135, 0.062], at 5.9 passages (job 51172) |
| Adaptive beats a well-set static baseline | No | plain top-8: 0.885; top-10: 0.974; adaptive: 0.771 |
| The recalibrated critic wastes fewer retries | Only in job 50977 | retries 41 to 27 in job 50977, 36 in job 51172 with the generator view |
| The critic catches unanswerable questions better | Somewhat | 2 of 8 accepted in job 51172, 4 of 8 in job 50977; the generator refuses the same 3 of 8 in both arms |
| The loop reliably refuses unanswerable questions | No | the unsatisfied rule refuses 6 of 8 and 9 of 32 answerable: it fails the gate |

The honest summary is that the loop spends fewer passages and model calls than it first did and matches
plain retrieval at an equal budget, but on this development slice reading more passages up front is
better than retrying. We do not claim that adaptive retrieval improves recall.

### 4. Status of the numbers

| Result | Status |
| --- | --- |
| Sections 3.1 to 3.6 | Development results, jobs 50701, 50977 and 51172, reproduced offline where stated |
| Generator-view alignment, handles, quote requirement (#34) | Run on the real model in job 51172 (commit 37cb0c6) |
| Answers for the arms | Generated once (job 51175, 40 questions) and counted as answered or refused; **correctness (EM, F1, faithfulness) not yet measured** |
| Held-out run | **Not yet run**; the configuration, commit and thresholds are frozen first |
| Live demo of the full agent | Merged (P5's server option, PR #27) and run live on the cluster by P5 on 5 November: both critic views returned an answer with citations in about 34 s |

### 5. Limitations

- **Small and single-slice.** 32 questions with gold; intervals are wide (the matched-budget interval
  spans zero), and every conclusion rests on one development slice and one run per configuration.
- **Exploratory tuning.** The critic prompt, the rewriter and the depth analysis were developed on these
  same 40 questions. They are descriptions of this slice, not independent confirmation.
- **Retrieval recall is not answer quality.** Gold is P3's mapping of QASPER evidence to chunks
  (a proposal); a chunk can hold the gold paragraph and still not answer the question.
- **Recall can overstate what the generator uses.** The generator renders at most 8 passages, each cut
  at 1,200 characters, a limit set for the older 200-word chunks and frozen by P5 for the final run;
  71% of gold passages are longer. A top-10 or adaptive run can therefore retrieve gold that the
  prompt does not show.
- **The critic is imperfect in both directions** (Section 3.3). Each configuration was run once, so
  run-to-run variation of the critic was not measured.
- **The planner cannot predict unanswerable questions** and the mapper carries no usable signal
  (Section 3.5), so the system relies on one LLM verdict.
- **No dense retrieval tuning.** Retrieval used the defaults the team chose; only depth was examined.
- **Abstention is not available** (Section 3.6).

### 6. Reproducibility

- **Code:** `src/agent/` (agent, critic, rewriter, experiments), `scripts/run_agent_experiment.py` (runner),
  `scripts/cluster/run_agent_experiment.sbatch` (cluster job), `scripts/evaluate_retrieval_depth.py`
  (depth curve; `--bge` adds the reranker), `scripts/evaluate_planner.py` (mapper, `--passages` for chunks,
  `--exclude-ids` to leave out held-out questions). Details: `docs/P4_AGENT.md`.
- **Pull requests:** #29 runner fixes (worker start method), #30 rewriter, #33 critic recalibration and depth
  evaluation, #34 critic view, handles, quote check and reporting, #35 demo critic and the chunk-level mapper
  evaluation.
- **Corpus:** build with `python -m scripts.build_corpus --scope development --chunk-size-words 365
  --chunk-overlap-words 40` (the builder's own defaults are still the old 200/40, so the flags are not
  optional); the runner stops if the items' gold passages are not in the corpus it is given.
- **Cluster run:** `ARMS="static adaptive static-wide" CRITIC=generator ANSWERS=none SCOPED=1 OFFLINE=1
  OUT_DIR=... sbatch scripts/cluster/run_agent_experiment.sbatch`; each output directory holds one
  record file per arm, `metrics.md`, `metrics.json` and `run_manifest.json` (arguments, commit, package
  versions, file hashes, critic call counts, and the generator's rendering limits).
- **Environment (job 50977):** Python 3.12.10, vLLM 0.11.0, transformers 4.57.6, torch 2.8.0,
  sentence-transformers 5.7.0, faiss-cpu 1.15.1, rank-bm25 0.2.2, LangGraph 1.2.19.
