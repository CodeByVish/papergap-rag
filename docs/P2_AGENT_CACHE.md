# P2 agent sections and score caching

`HybridRetriever.retrieve(query, paper_id, top_k=5, section=None)` now accepts
an optional exact section name. It forwards nonempty sections to both callbacks
and rejects out-of-section results. Unfiltered requests retain the existing
three-argument callback behavior. Pass section-capable P1 callbacks directly,
or wrap merged legacy callbacks in `SectionScopedRetriever(callback, passages)`.
The adapter requests the complete selected-paper ranking, filters before truncation,
and resets source ranks within the requested scope. Its corpus must match the
underlying indexes; it retains whole-paper BM25 statistics. Missing sections
return `[]`, with normal agent retry limits.

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
as `{"MISSING_RESULT":"Results"}`. Unmapped labels use all sections. This is an
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
