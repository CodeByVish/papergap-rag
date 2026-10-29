# P6 UI integration documentation

Updated: 2026-10-29 (Singapore). Branch: `P6/UI-port-integration`.
Reviewed runtime code: `4584e2c`, rebased onto `origin/main` at `97e33b2`.
P5 service/contract implementation: `ef5f7a3`, included in that main revision.

## Current status

- Design approved; UI implemented. The current branch contains both UI and P5
  service after rebase. No separate demo-service merge is needed.
- Post-rebase tests: **100 passed, 1 skipped**. The default suite's external-service
  smoke is opt-in. It previously passed separately against the actual P5 mock API.
- P6 operates its own cluster job, tunnel and laptop UI, as requested by P5's latest
  message. P5 owns service code; P1/P2 own retrieval; P4 owns agent integration.
- P6 cluster/GPU E2E remains unexecuted. Own account/runtime/data paths need
  confirmation. A real free-query retriever factory is not supplied, and the
  current free-query service path does not execute the P4 adaptive agent graph.

## Read in this order

| Document | Purpose |
| --- | --- |
| [Completion summary](UI_PORT_COMPLETION_SUMMARY.md) | Delivered behavior, exact verification evidence and remaining gates |
| [P6 real-environment E2E guide](P6_REAL_ENV_E2E_GUIDE.md) | P6 account setup, GPU job, single-hop tunnel, UI and real-environment acceptance |
| [P6 UI handoff to P5](P6_UI_handoff.md) | Usage, confirmed API compatibility, optional interface extensions and owner checklist |
| [Requirements and architecture](UI_PORT_REQUIREMENTS.md) | Current R01–R18 scope, actual modules/functions and session storage |
| [User stories and API](UI_PORT_USER_STORIES_AND_API.md) | Query/run identity, routing, lifecycle and timing/export definitions |
| [Acceptance cases](UI_PORT_ACCEPTANCE.md) | T01–T40 criteria, evidence levels and deferred checks |
| [Task specifications](UI_PORT_TASKS.md) | I0–I7 deliverables, implemented status and outstanding owner work |
| [macOS dependency snapshot](requirements-ui-macos-py314.txt) | Earlier clean UI/test environment; not a server/GPU or cross-platform lockfile |

The authoritative field-level API is [P5 UI contract](../P6_UI_CONTRACT.md),
implemented by [the server](../../src/generation/server.py). For cluster operation,
use the P6 E2E guide alongside [P5's operating manual](../DEMO_OPTION_C.md).
The P6 guide reflects the latest owner decision and single-hop tunnel method;
older P5-operated/ProxyJump descriptions elsewhere are not the selected setup.

All shared documents are in English. Passage schemas and split mappings remain
`v0-proposed`. Keep credentials, real records, corpus/index/model artifacts and
exported production results outside Git. No real-model or semantic-quality claim
follows from local mock tests.
