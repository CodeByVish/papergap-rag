# P2 agent sections and score caching

`HybridRetriever.retrieve(query, paper_id, top_k=5, section=None)` now accepts
an optional exact section name. It forwards nonempty sections to both callbacks
and rejects out-of-section results. Unfiltered requests retain the existing
three-argument callback behavior. Pass section-capable P1 callbacks directly,
or wrap merged legacy callbacks in `SectionScopedRetriever(callback, passages)`.
The adapter requests the complete selected-paper ranking, filters before truncation,
and resets source ranks within the requested scope. Its corpus must match the
underlying indexes; it retains whole-paper BM25 statistics. Missing sections
return `[]`. Same-round unscoped fallback is a pending P4 change; this branch
does not implement it.

P4's `build_agent_graph(..., section_selector=callable)` optionally chooses an
exact section from the current AgentState each round. With no selector, behavior
is unchanged. The retrieval log includes passage IDs, section and elapsed time. Full passage
objects remain in the existing agent export and are not duplicated in the log.

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
python -m scripts.run_hybrid_agent \
  --passages data/processed/passages.jsonl \
  --dense-index-dir indexes/p2-qasper-development-mps \
  --query 'Which method is used?' --paper-id PAPER_ID \
  --bge --local-files-only --section 'Methods' \
  --output results/agent-new.json
```

Use actual exact section names. Omit `--section` for unrestricted retrieval.
Alternatively `--gap-sections policy.json` accepts caller-reviewed mappings such
as `{"MISSING_RESULT":"Results"}`. This mapping is valid only for a selected
paper whose actual section names are known; it is not a corpus-wide policy.
Exact names vary across papers. On the local 1,168-paper development corpus,
exact Results/Methods/Experiments occur in 19.52%/3.34%/19.95% of papers.
P4 owns the forthcoming per-paper selector matching real section names to
requirement hints. An absent match should choose unrestricted retrieval.
If scoped retrieval is empty, P4 plans an unscoped attempt in the same round
(with both attempts logged and timed), rather than spending a rewrite retry.
Unmapped labels use all sections. This is an
injection mechanism that preserves P4's planner, evidence critic and rewriter.
The CLI uses the rule-based critic fallback without an LLM client; the graph also
accepts P4's critic client. The retry budget remains at most two retries.
Install the main requirements' `langgraph>=1,<2` for the agent runner.

`BGEReranker(..., revision=PINNED_SHA).cached(path)` returns a persistent SQLite
pair scorer. Keys include full query and passage text plus pinned model revision,
sequence limit, batching, device, tokenization policy and torch/transformers
versions. No cache key relies solely on passage ID. Duplicate pairs are scored
once; changed queries, text or settings miss the cache. Invalid/failing scorer
results are not persisted. Cache counters distinguish hits from model calls;
close the cache after use. Cache files stay under ignored `.cache/`.

The agent CLI defaults to `.cache/p2/scores.sqlite`. Cached latency must not be
reported as fresh cross-encoder compute. Use a new cache path for cold comparisons.
P1/P4 should review the optional interface extensions; schemas remain proposed.

## Runner ownership and latest integration — 27 October

`scripts/run_hybrid_agent.py` stays a P2 retrieval/cache diagnostic; it does not
become a second production generation runner. P4 owns agent orchestration and
the per-paper selector/fallback. P5 owns the generator adapter and answer step;
P6 coordinates the user-facing application. This is the P2 ownership proposal,
not a claim that every affected owner has already acknowledged it.

Current main already provides `src.agent.experiments.run_system(...,
answer_fn=...)`, introduced in P4 PR #17. Use that shared seam for static/adaptive
comparisons. P5 can adapt the exported record using
`src.generation.adapters.retrieval.build_request(record).request` and its
`GroundedQAPipeline`; PR #15 must be available in the integration checkout.
The P2 diagnostic CLI still does not run Qwen or P5 generation. Real Qwen critic
and final-answer execution require P5's backend and cluster runner.

`a23aa72` is the reviewed compact-log/P4-flow correction on PR #10. It was based
on `55000fd`, but newer main commits made the old up-to-date claim stale. This
branch now merges latest main, retaining its critic client, rewriter and experiment
harness. Full passages remain in the existing export, not duplicated in each
retrieval log entry. The local exact-name counts corroborate P4's reported figures;
the claimed 86% selector coverage cannot be reproduced until that selector is shared.
