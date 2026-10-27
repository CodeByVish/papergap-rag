# P2 status — verified 27 October 2026

Latest audited main: `fc1e76c`. P4 PRs #16/#17/#18 are merged. P1 #8, P2 #9/#10/#11,
P5 #15 and P6 #7 are still open. All three P2 branches were brought up to latest
main without rewriting history; weekly tracker conflicts were resolved by keeping
both the latest P4 status and each P2 progress entry. No teammate PR was merged.

## Decisions and verification

- **PR #10:** `a23aa72` is the P4-flow/compact-log fix P5 identified. It predates
  newer main; the branch is now synchronized. The exact-section documentation
  now explicitly limits mappings to papers with known section names. On the
  local 1,168-paper corpus, Results/Methods/Experiments occur in
  19.52%/3.34%/19.95% of papers, confirming P4's measurements. The claimed 86%
  per-paper-selector coverage remains unverified because that selector is not
  shared. P4 owns its selector and same-round unscoped fallback; neither is
  implemented by this P2 update.
- **Runner:** retain `scripts/run_hybrid_agent.py` as P2's retrieval/cache
  diagnostic. Use P4's existing `src.agent.experiments.run_system(answer_fn=...)`
  for static/adaptive orchestration; P5 owns its generation adapter. This is the
  proposed ownership split for affected owners to acknowledge, not a second runner.
- **Bridge smoke check:** combined latest main, P2 #9/#10/#11 and P5 #15 in an
  isolated local worktree. Both static/adaptive arms successfully called
  `GroundedQAPipeline(MockGenerator())` through
  `build_request(record).request` and returned the five-key P5 answer contract.
  This is a wiring check, not Qwen validation or an answer-quality result.
- **Annotation:** choose shared double annotation, as already specified by the
  execution plan. P2 and P5 independently judge the same 334 records, with
  their first/second ranges reversed. Only each individual's own batches must
  be disjoint. The final pool/order and allocation manifest still need P6 approval.
- **Relevance policy:** P5's `docs/WEEK5_QUALITY.md` is missing from shared main
  and PR #15 (`11b3639`). That PR explicitly excludes its handoff documents.
  We cannot claim compatibility without section 4. A binary partial-evidence
  proposal is recorded in P2_EVALUATION_HANDOFF.md for comparison, not approval.
- **Artifact:** verified every entry in the 531 KiB handoff ZIP checksum manifest.
  It contains 100 training integration questions, separate RRF/BGE outputs,
  485 passages per method and three empty questions. Keep BGE output separate
  from `runs/week3/`; this artifact is not a frozen held-out set. The ZIP is
  still local/ignored and must be forwarded or uploaded to an agreed destination.

## Checks completed

- #9 branch with latest main: **553 tests passed**.
- #10 branch with latest main: **556 tests passed**.
- #11 branch with latest main: **557 tests passed**.
- All three P2 branches + P5 #15 + latest main: **566 tests passed**.
- The P5 suite is not included in its PR; these counts refer to the shared suite,
  supplemented by the explicit mock bridge check above. No real Qwen run occurred.

## Can P2 continue?

Yes: interface integration, PR review/merge preparation, diagnostic development,
artifact handoff, and report methodology can proceed. P2 is not waiting for the
original BM25/dense functions or basic chunking implementation: those already work.

Final quantitative conclusions remain blocked on these shared inputs:

| Input | Owner | Why it matters |
| --- | --- | --- |
| Independently produced relevance labels / evidence-to-passage mapping and coverage manifest | P3/P6, with P5 policy input | Development tuning and fair retrieval/evidence recall metrics |
| Published section 4 guideline and agreement on partial evidence | P5/P3/P6 | Same binary meaning in annotation and scorer |
| Frozen held-out question list, corpus/config hashes and approval | P3/P6 + team | Current config still has `held_out_manifest: null`; do not manufacture approval |
| Common 1,000-pair pool order and allocation manifest | P6 | Export blinded batches and collect 2,000 independent judgments |
| Per-paper selector + same-round fallback | P4 after #10 integration | Reliable scoped retries without wasting rewrite budget |
| Real Qwen critic/generator cluster check | P4/P5 | Mock bridge success does not establish model behavior |
| Shared destination for handoff ZIP | Vishakha/team | Local filesystem path is not accessible to teammates |

The 25 October freeze target has passed according to the client date. Record the
actual freeze date once the inputs are agreed; do not backdate it. Prioritize the
required baseline, annotations and final evaluation over optional experiments.

---

# Historical status — 17 October 2026

| Work | Delivery | State |
| --- | --- | --- |
| Real P1/P3 retrieval, RRF, pinned BGE, pilot | [PR #5](https://github.com/CodeByVish/papergap-rag/pull/5) | Reviewed by Codex at owner's request and merged; 431 tests against then-current main |
| Fixed-question batch, 100-question real reranked handoff | [PR #9](https://github.com/CodeByVish/papergap-rag/pull/9) | Open; 434 tests with main |
| Agent sections, full per-round traces, persistent score caching | [PR #10](https://github.com/CodeByVish/papergap-rag/pull/10) | Open; 436 tests with main; real cold/restart-cache check passed |
| Four-method grids/metrics, blinded pools, blank human-label batches, report draft | [PR #11](https://github.com/CodeByVish/papergap-rag/pull/11) | Open; 438 tests with main; real development smoke and 30-pair pool passed |

All three follow-up branches were also combined locally on
`p2/combined-validation`: **446 tests passed**, lint passed and all 16 affected
Python files passed formatting checks. Only weekly tracker append conflicts
needed resolution; source merged cleanly. This local validation branch is not a
teammate review or an additional published PR. Follow-up PRs remain open for
review, particularly the P1/P4 optional interface and P3/P6 evaluation conventions.

The final 100-question handoff ZIP remains local and ignored:
`results/p2-batch-reranking-handoff-20261017.zip`. Its archived source is the
historical executed source; later changes are identified in the PRs above.

## Inputs still needed from P3/P6

A search of main, fetched P1/P6 branches and local processed data found proposed
protocols and adapters, but no agreed real relevance-label file or frozen held-out
manifest. The config still has `evaluation.held_out_manifest: null`.

Ask for independently produced labels and their corpus/mapping/scope manifest;
the agreed metric/partial-evidence policy; a team-approved held-out question and
configuration freeze; and P6's final assignment order. Exact input contracts and
commands are in [P2 evaluation handoff](P2_EVALUATION_HANDOFF.md).

Until these arrive, labelled development parameter selection, final held-out
candidate pooling, quality metrics/error conclusions and the quality-results
section of [the report draft](P2_REPORT_CONTRIBUTION.md) remain pending.
The proposed P2 ranges 168–334 and 668–834 total 334 independent human judgments;
they cannot be claimed complete by generating machine labels. Blank batch
exports are ready once the approved final inputs arrive.
