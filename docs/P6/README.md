# P6 UI port integration

Status: **design approved; UI implemented and locally tested; P5 service integration pending**.
Branch: `P6/UI-port-integration`, created from local `main` on 2026-10-29.

Review in this order:

1. [Requirements and architecture](UI_PORT_REQUIREMENTS.md)
2. [User stories, multi-conversation UI and API contract](UI_PORT_USER_STORIES_AND_API.md)
3. [Acceptance criteria and test cases](UI_PORT_ACCEPTANCE.md)
4. [Task breakdown and specifications](UI_PORT_TASKS.md)

The source for this proposal is P5's `P6_demo_ui_20261029.txt` handoff supplied
by the user. Its contents describe the intended integration contract, not
evidence that the service is available in this checkout. P5's field-level
`docs/P6_UI_CONTRACT.md` must be checked before implementing parsers.

The user approved implementation after design review. See
[completion summary](UI_PORT_COMPLETION_SUMMARY.md) for actual test evidence and
[P6 handoff to P5](P6_UI_handoff.md) for usage, interface assumptions and real E2E.
The planning documents below retain their proposed contract decisions; the
completion summary distinguishes implemented behavior from pending P5 verification.

The expanded design also maps Assignment.pdf pages 2–4 to user stories, session/
conversation/message/run identities, synchronous result routing, five-query timing
export, and P5 delivery dependencies. Correlation headers are proposals requiring
P5 agreement; the existing request bodies remain unchanged.


## P6 self-operated cluster deployment update

P5's latest message authorizes the P6-owned job/tunnel/UI configuration. Read
[P6 real-environment E2E guide](P6_REAL_ENV_E2E_GUIDE.md) for verified service
compatibility, account/runtime prerequisites and the remaining fresh-retrieval /
adaptive-agent gaps. The actual P5 mock API has now been exercised locally;
earlier missing-artifact notes in the completion summary are historical.
