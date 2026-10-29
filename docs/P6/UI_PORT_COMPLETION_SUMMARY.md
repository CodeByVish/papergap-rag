# P6 UI port completion summary

Updated: 2026-10-29 (Singapore). Branch: `P6/UI-port-integration`.
Reviewed code commits: `0f5e78b` (UI) and `4584e2c` (P5 catalogue compatibility),
rebased onto main `97e33b2`, which includes P5 service `ef5f7a3`.
Status: **UI and actual P5 mock integration verified locally; P6 real-cluster E2E pending**.

## Delivered behavior

The Streamlit entry point calls P5's HTTP API. It supports paper-scoped independent
questions when retrieval is configured, and original exported-state submissions
when it is not. Final answers, warnings, refusal reasons, validator-blocked raw
answers, provenance and optional supplied agent trace are inspectable. Citation
lookup falls back to IDs without discarding the final answer.

Session/workspace/run UUIDs keep results attached to their captured submission.
Identical submissions create distinct runs; explicit manual retries retain lineage.
A timeout/disconnect is outcome_unknown, not cancellation. Display actions do not
regenerate answers. Limits are 10 workspaces and 50 attempts per workspace; clearing
is explicit and history is session-only. JSON export supports five selected runs,
separate answer/citation HTTP timing, and sensitive-key/agent-state omission.

## Actual code architecture

| File | Implemented interfaces and responsibilities |
| --- | --- |
| `src/ui/api_client.py` | ApiConfig.from_env, P5ApiClient.health/papers/answer_record/answer_question/passages, ApiError; URL/auth/timeout validation, string-paper normalization, safe transport errors, no automatic POST retry |
| `src/ui/view_models.py` | parse_answer_record, classify_answer, citation_ids, build_evidence_cards; pure validation and display mapping |
| `src/ui/record_loader.py` | load_records, record_label; JSON-array/JSONL input, malformed-file/row errors, answer-capture rejection |
| `src/ui/conversation_state.py` | new_session, create_conversation, begin_run, finish_run, attach_evidence, clear_conversation, export_runs; captured ownership and guarded terminal transitions |
| `src/ui/app.py` | refresh, submit_request, render_answer, main; capability-gated forms, workspaces/history, manual retry, diagnostics and export |
| `tests/test_ui*.py`, `tests/ui_http_fixture.py` | UI unit/AppTest, localhost synthetic HTTP integration and opt-in running-service smoke |
| `tests/test_legacy_ui_adapters.py` | Preserved reusable prompt/retrieval/provider adapter checks |

Existing retrieval/generation modules were not changed by the UI port. P5's
server is now inherited from main. No new endpoint, answer body field or shared
passage/split schema was introduced. Backend execution IDs/correlation headers
remain deferred; the current UI uses only local run routing.

## Verification evidence

The post-rebase command below ran successfully against the combined current tree:

```bash
.venv/bin/python -m pytest -q tests/test_ui_api_client.py tests/test_ui_view_models.py tests/test_ui_record_loader.py tests/test_ui_conversation_state.py tests/test_ui.py tests/test_ui_p5_smoke.py tests/test_server.py tests/test_legacy_ui_adapters.py tests/test_generation_week6.py tests/test_qwen_client.py
```

| Evidence | Result and interpretation |
| --- | --- |
| Post-rebase combined suite | **100 passed, 1 skipped**: 44 UI checks, 22 server checks, 34 existing adapter/generation/Qwen checks. External-service smoke was not opted in for this command. |
| Actual P5 mock API + P6 UI | **1 passed separately**, before rebase in an isolated combined checkout: Bearer auth, synthetic exported state, actual sockets, citation lookup and Streamlit record submission. |
| P5 socket smoke | **15/15 passed separately**, including free-form on/off and simultaneous `{200,429}`. Its retriever is a test fixture, not P2's real factory. |
| Clean lightweight environment, initial implementation | **42 passed, 1 skipped** before the two later paper-catalogue tests; no Qwen, GPU, Java, FAISS or PyTorch needed. This is historical clean-environment evidence, not the latest combined-suite count. |
| Browser walkthrough | Submitted a synthetic independent question; inspected owning run, status/timing and expanded citation. Narrow viewport wrapped the main content. |
| Rebase preservation | range-diff confirmed both P6 patches unchanged apart from commit IDs; no conflicts. |
| Documentation reconciliation | 8 Markdown files reviewed; 34 local links, 22 Bash syntax blocks, 1 embedded Python block, table shape, R01–R18/T01–T40 numbering and documented app/state function names checked. No runtime code changed in this documentation pass. |

Earlier counts such as 35 server/client tests and 43 UI unit/AppTest checks are
subsets of the combined coverage, not additive totals. The external-service test
being skipped by default does not invalidate its separately recorded mock pass.
No P6 GPU/cluster tests have been performed.

Runtime: macOS 26.6.2 arm64, Python 3.14.7. Post-rebase existing environment:
Streamlit 1.64.0, requests 2.34.2, pytest 9.1.1, OpenAI 1.109.1, Pydantic 2.13.5.
Earlier clean environment: Streamlit 1.66.1, requests 2.34.2, pytest 9.2.0,
OpenAI 2.54.0, Pydantic 2.14.1. The accompanying
[dependency snapshot](requirements-ui-macos-py314.txt) records that clean
UI environment; it excludes the full P5 server/vLLM stack and does not establish
Windows, Python 3.12 or cluster reproducibility.

## Remaining gates and limitations

- T24 passed against the actual P5 mock service with synthetic input. P5's contract,
  server, capture script, samples and cluster script are now present in this tree.
- Real-cluster cases T25–T27 and E-level portions of T32,T35,T36,T38,T40 remain
  pending P6 execution. P6 must confirm quota, runtime/weight paths, approved real
  development records, token and forwarding under its own account.
- Fresh questions require the real P2/P5 retriever factory and matching data/indexes.
  The current free-query endpoint performs one retrieval call then generation; it
  does not run P4's adaptive graph. Supplied trace is not evidence of a fresh run.
- T33's proposed header echo/mismatch extension is deferred. No ID header is sent,
  checked or echoed by the UI; there is no durable backend run recovery.
- Live long-call behavior, GPU concurrency, reconnection and full-corpus citation
  coverage are not established by local tests. Browser checking used synthetic text.
- P5 health lacks mode, so UI/export may say unknown. Preserve raw health and
  generation backend metadata externally for live-run evidence. Export does not
  synthesize missing model/code revisions or isolate inference latency.
- Unknown insufficient-result codes currently fall back to the Model refusal label.
  Inspect validation details: GENERATION_ERROR/PARSE_ERROR or a skipped model call
  must not be counted as a successful real-model generation merely because HTTP=200.
- No persistent history, streaming, cancellation, contextual multi-turn prompting,
  semantic citation-faithfulness guarantee or gold-answer scoring was implemented.

Use [the P6 E2E guide](P6_REAL_ENV_E2E_GUIDE.md) for execution and
[the handoff](P6_UI_handoff.md) for API/ownership review. Shared schemas and split
mappings remain `v0-proposed`; a reviewer must approve before merge into main.
