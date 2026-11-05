# Contributing

Read the [execution plan](docs/EXECUTION_PLAN.md) and [open decisions](docs/REQUIREMENTS.md) first. Set up Python using the README. VS Code is suggested in the original plan; reusable Python modules and reproducible commands matter more than editor choice.

## Working together

1. Pull the latest default branch and create a short-lived task branch, for example `p2/rrf-fusion` or `p4/retry-budget`.
2. Keep changes within a reviewable task. Use shared schemas and mock inputs while upstream modules are unfinished.
3. Add meaningful tests for implemented behavior and run the relevant tests. Record commands and results in the PR.
4. Open a pull request. Obtain review from another member; involve affected owners for interface changes.
5. Merge only after review and update the weekly tracker with the PR or result link.

Do not commit credentials, real `.env` files, raw datasets, model weights, indexes or generated results. Keep small synthetic fixtures under `tests/fixtures/`. Put final reusable logic in `src/`, not notebooks. No license is chosen yet; the team must agree before adding one.

## Interface checkpoint

P3 owns passage IDs and passage schema. P1/P2 own retrieval results. P4 owns agent state and gap labels. P5 owns final answers. P6 coordinates configuration and experiment records. Freeze these together in Week 1; the plan's sample JSON is a proposal until that meeting.

Specify paper and section filtering, score/rank meanings, empty results, invalid paper IDs, and retry counting. Return at most `top_k` available matches; a paper may contain fewer passages. Track original ranks separately from fusion and reranker scores. Passages supplied to generation must be traceable across retrieval rounds.

## Reproducibility

Record code commit, data/split hashes, model IDs and revisions, prompts, configuration, random seeds, hardware, dependency versions and timing policy with every reported run. Once the environment works, P6 records a platform-specific resolved dependency snapshot. Do not claim that the starter ranges alone reproduce an experiment.

P6 assembles the report; every owner supplies their own reviewed section, figures and results. Assign a backup integration/release owner at the first meeting.
