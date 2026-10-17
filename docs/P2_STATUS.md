# P2 status — 17 October 2026

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
