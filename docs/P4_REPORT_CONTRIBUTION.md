# P4 report contribution — draft for P6

## Agent: evidence-gap-driven retrieval

PaperGap's agent decides whether the passages retrieved so far are enough to answer a question and,
if not, names what is missing and searches again. This chapter describes the design, the experiments
on development questions, the single frozen run on the held-out questions, what they show, and what they
do not show. Sections 3.1 to 3.7 are development results; Section 3.8 is the held-out result (see "Status of
the numbers").

### 1. Design

The agent is a LangGraph state machine over one paper:

```
plan_question -> retrieve -> map_evidence -> critic -> [stop | rewrite_query -> retrieve ...]
```

| Component | What it does |
| --- | --- |
| Planner | Rule-based. Assigns one of five question types (factual, method, result, comparison, limitation) and the evidence requirements an answer needs (`method`, `experiment_context`, `result`, `comparison`, `limitation`, `direct_answer`). It never predicts "unanswerable": the question text cannot show that. |
| Retrieve | P2's hybrid retriever inside the selected paper: BM25 and the pinned `BAAI/bge-small-en-v1.5` dense retriever, 20 candidates each, fused with RRF (k = 60), top 5 per round in the development jobs (8 in the frozen held-out run, Section 2). Passages accumulate across rounds and are de-duplicated by passage id. |
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

- *static*: one round, top 5 in the development jobs, no critic.
- *adaptive*: the full loop above, up to 3 rounds.
- *static-wide*: one round with 15 passages; its first *k* passages are the plain-retrieval baseline at
  every depth *k*, from a single run.

**Held-out run.** The held-out configuration is frozen in `configs/p4_freeze.json` (6 November, code commit
`ad02d51`): the same retriever and critic as above, but **top 8 per round** instead of 5, with answers. The
team moved the depth to 8 because plain retrieval is better there (0.885 against 0.740 at top 5 on the
development items). All tuning and jobs 50701, 50977 and 51172 were at top 5; adaptive at top 8 was run once on
the 40 development items before the freeze (job 51521: recall 0.927 against 0.885 for static, 8.55 against
7.85 passages, paired gain +0.042, 95% interval 0 to 0.115) and nothing was tuned on it. The arms are static
(top 8), adaptive and static-wide (15 passages, giving plain retrieval at 5, 8 and 10).

**Context budget.** The primary held-out run renders at most 8 passages of 1,200 characters each, the prompt
budget fixed before the run (P5's prompt v7). After that run had finished, P5 repeated the configuration with
2,500 characters per passage on the 40 development questions (job 51691) and on the same 200 held-out
questions (job 51705). The 2,500-character runs are **post-hoc sensitivity analyses**: they are not in the
freeze record, they do not replace or re-score the primary run, and they are reported separately
(Section 3.9). Everything in Sections 3.1 to 3.8 uses 1,200 characters.

**Metrics.** *Recall*: share of a question's gold passages among the distinct passages retrieved
(mean over the 32 questions with gold). *Full recall*: questions with every gold passage. *Unnecessary
retry*: a retry made when all gold was already retrieved. *Ineffective retry*: a retry that added no
gold. *Redundant retry*: a retry that added no new passage. *Matched-budget gain*: per question, the
adaptive arm's final recall minus the plain ranking's recall over the same number of passages the
adaptive arm ended with. Intervals are 95% paired bootstrap intervals (2,000 resamples) over the 32
development questions, or over the 200 held-out questions in Section 3.8.

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

| top-k | 3 | 5 (development default) | 8 | 10 | 15 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean gold recall | 0.599 | 0.740 | 0.885 | **0.974** | 0.974 |
| Questions with full recall | 17/32 | 22/32 | 26/32 | 30/32 | 30/32 |

(The held-out curve, Section 3.8, has the same shape but is flatter at the top: 0.723, 0.858, 0.897 and 0.953 at
5, 8, 10 and 15.) Six of the 32 questions have their best gold passage at ranks 6 to 10. The fusion constants hardly
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
(recomputed on the final 365/40 development corpus: 33 of the 45 gold passages, 73.3%, are longer, and 36.6% of
the gold text lies beyond the cut), and its prompt asked for
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
not by itself separate good verdicts from bad ones: the gold passage is longer than 1,200 characters in 65%
of the over-strict verdicts and in 75% of the correct "sufficient" ones. It does cost retries, however: with
the per-passage budget raised to 2,500 characters the adaptive arm needs 18 retries instead of 32 on the same
40 items (Section 3.9). Of 68 verdicts asked of the model, 2 (2.9%) fell back to the rules:
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
better than retrying. We do not claim that adaptive retrieval improves recall. The held-out run (3.8) gives
the same picture on 200 questions.

#### 3.8 Held-out result

**What was run.** The configuration frozen on 6 November (commit `ad02d51`, Section 2) was run once, by P5, on
P3's frozen list of 200 questions (174 papers, 78 validation-split and 122 test-split questions; list SHA-256
`d509010b...`), over the all-paper-text corpus (28,617 passages, 1,584 papers). Top 8 per round, no reranker,
at most 2 retries, Qwen3-8B critic reading the generator's view, three arms, answers generated by P5's
prompt v7. The run held questions only; gold was read afterwards, for scoring, with P3's evidence-to-passage
mapping. Each arm was run once and nothing was changed after the result. All 200 questions are answerable
and have mapped gold (347 gold passages, 1.74 per question). **There is no unanswerable question in the held-out
set**, so the subset the freeze record names for unanswerable questions is empty. Intervals are 95% paired
bootstrap intervals (2,000 resamples, seed 0) over the questions.

Because P4's author labelled 40 of these questions for annotation before the freeze (disclosure
`p4-annotated-40` in the freeze record), every table is given for all 200 questions **and** for the 160 that
P4 did not annotate. The two agree.

**Retrieval.** Mean gold recall and the cost of the arms:

| | static (top 8) | adaptive | static-wide (15) |
| --- | ---: | ---: | ---: |
| *All 200 questions* | | | |
| Mean gold recall | 0.858 | **0.871** | 0.953 |
| Questions with full recall | 154/200 | 157/200 | 183/200 |
| Mean passages retrieved | 7.97 | 8.28 | 13.95 |
| Mean rounds | 1.00 | 1.44 | 1.00 |
| Agent time per question (s, A40) | < 0.1 | 5.6 | < 0.1 |
| *The 160 questions P4 did not annotate* | | | |
| Mean gold recall | 0.881 | **0.897** | 0.959 |
| Questions with full recall | 127/160 | 130/160 | 148/160 |
| Mean passages retrieved | 7.98 | 8.32 | 13.97 |
| Mean rounds | 1.00 | 1.44 | 1.00 |

Plain retrieval (the question as the query, no critic, no retry) at each depth, read from the static-wide arm:

| top-k | 3 | 5 | 8 | 10 | 15 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean gold recall, 200 questions | 0.569 | 0.723 | 0.858 | 0.897 | 0.953 |
| Questions with full recall | 84/200 | 117/200 | 154/200 | 166/200 | 183/200 |
| Mean gold recall, 160 questions | 0.585 | 0.749 | 0.881 | 0.907 | 0.959 |
| Questions with full recall | 69/160 | 98/160 | 127/160 | 134/160 | 148/160 |

**Paired comparisons** (mean difference in per-question recall, 95% interval):

| Comparison | 200 questions | 160 questions |
| --- | --- | --- |
| Adaptive against static top 8 | +0.013 [0.001, 0.028] | +0.016 [0.000, 0.038] |
| Adaptive against the plain ranking at equal passages (matched budget, 8.28 and 8.32 passages) | **+0.001 [−0.014, 0.016]** | +0.009 [0.000, 0.025] |

The adaptive arm ended with higher recall than static on **4 of the 200 questions** (3 of them reaching full
recall) and with lower recall on none; the other 196 are identical. The gain over static top 8 is therefore
real but small, and its interval only just excludes zero (it reaches zero on the 160). **At equal
passages the adaptive arm does not beat the plain ranking**: on all 200 questions the gain is 0.001. Reading
more passages up front is better than retrying: plain top 10 reads 10 passages and reaches 0.897, plain top 15
reads 15 and reaches 0.953, against 0.871 for the loop at 8.3.

**The loop's cost.**

| | adaptive, held-out (200) | adaptive, depth-8 development check (job 51521, 40 items) |
| --- | ---: | ---: |
| Questions the loop retried | 45/200 (2 with one retry, 43 with two) | n/a |
| Retries | 88 | 32 |
| Unnecessary retries (all gold already retrieved) | 62.5% | 61.9% |
| Ineffective retries (added no gold) | 95.5% | 90.5% |
| Redundant retries (added no new passage) | 46.6% | 40.6% |
| Stop reason: sufficient / max rounds / insufficient information | 156 / 41 / 3 | 25 / 14 / 1 |
| Critic verdicts: from the model / rule fallback; share reused from the previous round | 95.8% / 4.2%; 17.0% reused | 93.1% / 6.9% |

The depth-8 development check predicted this well: the retry rates are close, and the gain over static was
+0.042 there against +0.013 here, both with intervals that reach or nearly reach zero. Of 88 retries, 4 added a gold
passage.

**What the critic gets wrong** (all 200 questions; verdicts asked of the model with gold known, reused
verdicts excluded; the 160-question counts are in brackets):

| Verdict and situation | Count |
| --- | ---: |
| "Insufficient" although all gold was already retrieved (over-strict) | 54 (50) |
| "Insufficient", gold still missing (correct) | 29 (18) |
| "Sufficient", all gold retrieved (correct) | 127 (103) |
| "Sufficient", gold missing (false accept) | 29 (22) |

Of 239 verdicts asked of the model, 10 (4.2%) fell back to the rules, below the 10% at which the instruction
would need rewording. Of the sufficient verdicts, 131 cite a gold passage and 21 cite none. Two thirds of the
critic's "insufficient" verdicts (54 of 83) were made with all gold already in view, and about a fifth of its
"sufficient" ones (29 of 156) were made with gold missing, as in the development runs; it was left unchanged, as
frozen.

**Abstention and answers.** The refusal rule stays off, as frozen. Its gate needs unanswerable questions, and
the held-out set has none, so the held-out result neither meets nor fails the gate on that side; the other side
is visible: the critic was unsatisfied after the last round on **22.0%** of the answerable questions (21.9% on
the 160), against the 5% the gate allows. Had the rule been on, it would have refused about one question in five
that is answerable. Generated answers were counted first:

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| Generator answered (evidence status SUFFICIENT) | 194 | 191 | 194 |
| Refused (insufficient evidence) | 6 | 9 | 6 |
| Answer downgraded by the validator (`PARSE_ERROR`) | 2 | 2 | 2 |

The generator refuses the same 6 questions in every arm. The 3 extra refusals in the adaptive arm are the 3
questions where the critic itself stopped with `INSUFFICIENT_INFORMATION`; since every held-out question is
answerable, all 3 are false refusals (1.5%), caused by the loop.

**Answer quality (overlap).** P5 scored the answers against the QASPER references with P6's scorer (`qa` step,
policy `p6-qa-v0-proposed`: normalized exact match and token F1 against the best-matching reference; not the
official QASPER evaluator), and P4 reproduced the figures independently. Exact match is 0.005 in every arm (one
question of 200), because the generator writes sentences and the references are mostly short spans, so F1 is the
usable figure:

| | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| Token F1, all 200 questions | 0.3681 | 0.3656 | 0.3676 |
| Token F1, the 160 not annotated by P4 | 0.3689 | 0.3690 | n/a |
| Answered / refused / failed (scorer) | 194 / 4 / 2 | 191 / 7 / 2 | 194 / 4 / 2 |
| Coverage (answered share), 200 / 160 | 0.970 / 0.969 | 0.955 / 0.950 | 0.970 / n/a |

The paired difference, adaptive minus static, is −0.0025 (95% interval −0.011 to 0.006; 174 papers) on the 200
questions and +0.0001 (−0.007 to 0.008; 142 papers) on the 160 (paper-level bootstrap, 1,000 resamples,
seed 42, P6's `compare` step). The scorer counts the two `PARSE_ERROR` answers per arm as failures, which is
why it reports 4, 7 and 4 refusals where the generator reports 6, 9 and 6. All 200 questions are answerable, so
the unanswerable-correctness metric is not available. The scorer's output is labelled `development` because its
`held_out` label needs a team sign-off that has not been given; the numbers do not depend on the label.
**Answer quality (LLM judge, RAGAS).** P5 scored the held-out answers of the static and adaptive arms with RAGAS 0.2.15
and a live judge (`qwen-plus-2025-12-01`, embeddings Qwen3.7 Text Embedding, `qwen3.7-text-embedding`, both through DashScope's
OpenAI-compatible endpoint), on the same records as the other scores (prediction hashes match job 51585) and the
exact rendered contexts (8 passages of at most 1,200 characters). P4 recomputed the means from the per-question scores:

| Mean (valid scores) | static | adaptive |
| --- | ---: | ---: |
| Faithfulness | 0.892 (194) | 0.907 (191) |
| Response relevance | 0.854 (193) | 0.854 (189) |
| Context precision | 0.578 (194) | 0.577 (191) |

Refused answers (4 and 7) and the two validator-downgraded answers per arm are excluded; one static and two adaptive
response-relevance scores were invalid. Paired differences, adaptive minus static, over the questions scored in both arms
(paper-level bootstrap, 1,000 resamples, seed 42, P6's `compare` step): faithfulness +0.012 [-0.001, 0.026] (191
questions); response relevance -0.003 [-0.008, 0.001] (188); context precision -0.003 [-0.015, 0.010] (191); on the 160
not annotated by P4: +0.011 [-0.003, 0.032], -0.004 [-0.009, 0.001], -0.002 [-0.014, 0.009]. No interval excludes zero:
the loop gives no measurable gain on these judge scores either. Faithfulness is scored only on answered questions, and
the adaptive arm answers three fewer. Caveats: the judge is a hosted LLM from the same model family as the generator,
its scores are model judgments and not human verification, the run did not store the rendered prompts, so the contexts were produced
afterwards (P5 to confirm the method; P6's `contexts` step rebuilds them from the records and the prompt configuration; the
contexts files are not in the delivery archive and their hashes are in the run manifests), DashScope's
embeddings endpoint needed a wrapper that sets `check_embedding_ctx_length=False` (the evaluator itself is unmodified),
and the run is labelled `development` like the other P6-pipeline outputs. Cost and time as reported by P5: about 2.5
hours and 0.63 SGD for the two arms. The fifteen-passage arm was not judged.

**What the held-out result supports.**

| Claim | Supported? | Evidence |
| --- | --- | --- |
| Adaptive recovers more gold than static top 8 | Marginally | 0.858 to 0.871, +0.013 [0.001, 0.028]; 4 questions; 160: +0.016 [0.000, 0.038] |
| Adaptive beats plain retrieval reading the same number of passages | **No** | matched gain +0.001 [−0.014, 0.016] at 8.28 passages; 160: +0.009 [0.000, 0.025] |
| Adaptive beats a well-set static baseline | **No** | plain top 10 0.897 and top 15 0.953, against 0.871 at 8.3 passages |
| The critic's retries are worth their cost | **No** | 88 retries, 95.5% ineffective, 62.5% unnecessary, 4 gained a gold passage; about 5.6 s per question |
| The loop reliably refuses unanswerable questions | **Not tested** | no unanswerable question in the set; the unsatisfied rule would refuse 22.0% of the answerable ones; the critic false-refused 3 (1.5%) |
| Adaptive gives better answers than static | **No** | token F1 0.3656 against 0.3681, −0.0025 [−0.011, 0.006]; 160: +0.0001 [−0.007, 0.008] |
| Deeper plain retrieval is better than retrying | Yes | recall 0.723 at 5, 0.858 at 8, 0.897 at 10, 0.953 at 15 |

**Reading.** On unseen questions the agent's evidence-gap loop behaves as it did on the development slice. It
finds a gold passage that plain top-8 retrieval missed on 4 of 200 questions (2%), at the price of 88 retries,
five seconds of agent time per question and 3 false refusals, and it does no better than simply reading the
same number of passages; the answers it produces score no better either (token F1 0.366 against 0.368). The extra recall that reading more passages gives (0.953 at 15) is not usable by the
generator as configured, because P5's prompt renders at most 8 passages of 1,200 characters: the 15-passage
arm shows the headroom for retrieval, not what the answer step would see. The held-out run therefore does
**not** support the claim that evidence-gap-driven retrieval improves recall; it supports the narrower claims
that the loop never lowered recall, that its critic is usable (4.2% fallback) but over-strict, and that
retrieval depth is the factor that matters.

#### 3.9 Context budget: 1,200 against 2,500 characters per passage (post-hoc sensitivity)

The generator renders at most 8 passages, each cut at a character limit. With the primary limit of 1,200
characters, 33 of the 45 development gold passages (73.3%) are cut and 36.6% of the gold text is hidden; on the
held-out questions 232 of the 347 gold passages (66.9%) are longer than 1,200 characters. At 2,500 characters
only one development gold passage (the longest, 2,509 characters) is cut. Eight passages of 2,500 characters
give prompts of 3,400 to 6,600 tokens, well inside the model's 32,768-token window.

P5 repeated the development items with the larger budget (job 51691; one run per cell, 40 questions: 32
answerable, 8 unanswerable; both the critic and the generator read the same budget):

| Metric | static 1,200 | static 2,500 | adaptive 1,200 | adaptive 2,500 |
| --- | ---: | ---: | ---: | ---: |
| Answered / refused | 36 / 4 | 37 / 3 | 36 / 4 | 37 / 3 |
| Mean citations | 1.89 | 1.73 | 1.92 | 1.81 |
| Citation gold recall | 0.694 | 0.747 | 0.726 | 0.769 |
| Citation gold precision | 0.580 | 0.619 | 0.577 | 0.613 |
| Prompt tokens (range) | 3,270-5,238 | 3,374-6,647 | 3,068-5,238 | 3,374-6,647 |
| Mean rounds | 1.000 | 1.000 | 1.800 | 1.450 |
| Retries | 0 | 0 | 32 | 18 |
| Gaps detected | 6 | 6 | 18 | 10 |

- **Better grounded citations.** Gold citation recall rises by 0.053 (static) and 0.043 (adaptive) and gold
  citation precision by 0.039 and 0.036.
- **A cheaper loop.** The adaptive arm makes 18 retries instead of 32 and detects 10 gaps instead of 18: the
  critic sees more complete text and asks for more evidence less often.
- **A small cost in refusal calibration.** Of the 8 unanswerable questions, 5 are answered at 1,200 characters
  and 6 at 2,500; the extra one ("What is the size of the Atomic dataset?") was refused at 1,200 and is
  answered at 2,500 with a sentence that does not answer it. Answerable questions stay at 31 of 32 answered.
- **The loop still adds little.** Its gain in citation gold recall over static is +0.032 at 1,200 and +0.022 at
  2,500 characters, and its gain in citation precision is about zero at both.
- **Strength of the evidence.** One run per cell on 40 questions, with no intervals; the differences are a few
  citations. Treat them as suggestive.

The same 2,500-character configuration was also run on the 200 held-out questions (job 51705). It is a
post-hoc sensitivity analysis on the questions of the primary result, started after the primary run had
finished, and it is reported next to the primary result, never instead of it. **Status: running when this was written;
no held-out 2,500 number is reported until it has been scored with the same frozen scripts.**

### 4. Status of the numbers

| Result | Status |
| --- | --- |
| Sections 3.1 to 3.6 | Development results, jobs 50701, 50977 and 51172, reproduced offline where stated |
| Generator-view alignment, handles, quote requirement (#34) | Run on the real model in job 51172 (commit 37cb0c6) |
| Answers for the arms | Generated once on the development items (job 51175, 40 questions) and once in the held-out run (job 51585, 200 questions), counted as answered or refused; held-out answers scored for EM and F1 (Section 3.8: F1 0.368 static, 0.366 adaptive); held-out answers also judged by RAGAS (faithfulness 0.892 and 0.907); **the development answers' correctness is not measured** |
| Depth-8 development check | Job 51521 (P5, 6 November, 40 development items, commit `ad02d51`): static 0.885 at 7.85 passages, adaptive 0.927 at 8.55; critic fallback 6.9%; refusal gate still not met |
| Held-out run | Frozen on 6 November (`configs/p4_freeze.json`, commit `ad02d51`) and **run once** by P5 the same day (job 51585, clean checkout, 200 questions, three arms, with answers); retrieval and answer EM/F1 scored against P3's gold and the QASPER references after the run (Section 3.8). **RAGAS scored for static and adaptive (Section 3.8): no gain from the loop** |
| Context-budget check, development | Job 51691 (P5, 6 November, the 40 development items, 1,200 against 2,500 characters per passage, one run per cell): Section 3.9. Post-hoc; not part of the freeze record |
| Context-budget sensitivity, held-out | Job 51705 (P5): the 200 held-out questions at 2,500 characters, **running, not yet scored**. Post-hoc; reported next to the 1,200-character primary result (Section 3.9), never instead of it |
| Live demo of the full agent | Merged (P5's server option, PR #27) and run live on the cluster by P5 on 5 November: both critic views returned an answer with citations in about 34 s |

### 5. Limitations

- **Small and single-slice.** The development results rest on 32 questions with gold; intervals are wide (the
  matched-budget interval spans zero), from one development slice and one run per configuration. The held-out
  run has 200 questions, but still one run per arm and one critic sample per question; run-to-run variation of
  the Qwen critic was not measured, so the small differences of Section 3.8 (a gain of 0.013) could move.
- **Exploratory tuning.** The critic prompt, the rewriter and the depth analysis were developed on these
  same 40 questions. They are descriptions of this slice, not independent confirmation.
- **Retrieval recall is not answer quality.** Gold is P3's mapping of QASPER evidence to chunks
  (a proposal); a chunk can hold the gold paragraph and still not answer the question.
- **Recall can overstate what the generator uses.** The generator renders at most 8 passages, each cut
  at 1,200 characters, a limit set for the older 200-word chunks and frozen by P5 for the primary run;
  73.3% of the development gold passages (33 of 45) and 66.9% of the held-out ones (232 of 347) are longer.
  A top-10 or adaptive run can therefore retrieve gold that the prompt does not show. A 2,500-character
  budget removes most of the clipping (Section 3.9) but was a post-hoc check, not the primary configuration.
- **The critic is imperfect in both directions** (Section 3.3). Each configuration was run once, so
  run-to-run variation of the critic was not measured.
- **The planner cannot predict unanswerable questions** and the mapper carries no usable signal
  (Section 3.5), so the system relies on one LLM verdict.
- **No dense retrieval tuning.** Retrieval used the defaults the team chose; only depth was examined.
- **Abstention is not available** (Section 3.6), and **the held-out set cannot test it**: all 200 questions are
  answerable, so the correct-refusal rate and the refusal gate could only be assessed on the development slice
  (8 unanswerable questions).
- **Answer quality is measured by overlap only.** EM and token F1 come from a proposed project scorer, not the
  official QASPER evaluator; EM is near zero because the generator writes sentences against short reference
  spans, and F1 penalizes correct paraphrases. Faithfulness comes from a hosted LLM judge (RAGAS), not from human checking, so the
  groundedness results are model judgments.
- **Part of the held-out set was read before the freeze.** P4's author annotated 40 of the 200 questions, so
  results are given for all 200 and for the 160 that were not; the figures agree. The disclosure is in the
  freeze record.
- **Retrieval beyond 8 passages is not shown to the generator.** The adaptive arm retrieves 8.3 passages on
  average and the 15-passage arm 13.9, but the prompt renders at most 8 passages, so recall above 8 is
  headroom for retrieval and not evidence the answer step used.
- **The wide arm ran with a flag outside the repository.** `--wide-k 15` was passed through a copy of the
  cluster script because the runner's default (24) exceeds the candidate pool; the recorded `static_wide_k` was
  respected and no setting was changed.
- **Development tuning at depth 5, held-out run at depth 8.** The critic, rewriter and gate decisions were
  made on top-5 runs; only one development check was made at top 8 (job 51521). The held-out figures are
  therefore from a depth the tuning did not use.
- **The dense encoder truncates long passages.** `BAAI/bge-small-en-v1.5` is built with a 512-token limit
  (`max_seq_length` in `src/retrieval/dense_retriever.py`, the model's maximum), so the vector of a longer
  passage is computed from its first 512 tokens only. With the model's own tokenizer on the 365/40 chunks,
  14.7% of the development passages (3,142 of 21,360) and 14.3% of the all-paper-text passages used for the
  held-out run (4,099 of 28,617) are longer, losing 84 to 88 tokens on average; 14 of the 45 development gold
  passages (31%) are affected, losing about 52 tokens on average. BM25 reads the full text, so the hybrid
  retriever is only partly affected. The effect on recall was not tested and the chunking is frozen, so it is
  reported, not fixed. (P2 reports 27.1% of passages above 512 tokens, probably with the reranker's
  tokenizer; this was not checked.)

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
- **Held-out run:** `configs/p4_freeze.json` (frozen 6 November, code `ad02d51`); the run's inputs were written
  by `scripts/make_held_out_items.py`, the job (51585) by P5, and the scores by `scripts/score_agent_records.py
  --role held-out`, which refuses unless the run's manifest matches the record. Commands:
  `docs/P4_FREEZE_RECORD.md`.
- **Environment (job 50977):** Python 3.12.10, vLLM 0.11.0, transformers 4.57.6, torch 2.8.0,
  sentence-transformers 5.7.0, faiss-cpu 1.15.1, rank-bm25 0.2.2, LangGraph 1.2.19.
