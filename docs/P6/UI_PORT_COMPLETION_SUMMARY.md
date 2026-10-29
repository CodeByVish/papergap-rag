# P6 UI port completion summary

Date: 2026-10-29 (Singapore). Branch: `P6/UI-port-integration`.
Base: `10e52e926cc6f22395fe8fc180dd7c114950195a`.
Status: local implementation complete; actual P5 integration and real E2E pending.

## Delivered behavior

The UI now calls P5's HTTP service instead of loading retrieval/model providers.
It supports paper-scoped independent questions and original exported-state input,
six answer presentations plus inconsistent-response warnings, validator rejected
answers, provenance/trace diagnostics and citation lookup with ID-only fallback.
Each run owns its immutable submission, response, errors, timing and evidence.
Workspace/session UUIDs isolate histories; repeated queries receive different run
IDs, explicit retries retain lineage, and duplicate terminal results are ignored.
Timeout/disconnect retains an outcome-unknown attempt without retry or cancellation.
Session-only history is bounded to 10 workspaces / 50 attempts each. Selected-run
exports separate answer HTTP and citation latency and omit agent/state dumps and
sensitive-key metadata. P5 request_id is preserved as a business identifier.

## Code architecture and changes

| File | Implemented responsibilities |
| --- | --- |
| `src/ui/api_client.py` | ApiConfig/P5ApiClient/ApiError: URL/config validation, four HTTP endpoints, explicit configurable authentication, safe errors, >=120s answer read timeout and no automatic retry |
| `src/ui/view_models.py` | parse_answer_record, classify_answer, citation_ids, build_evidence_cards: response validation and pure display mapping |
| `src/ui/record_loader.py` | load_records/record_label: local JSON/JSONL inputs, actionable file/row errors, reject answer captures |
| `src/ui/conversation_state.py` | new_session/create_conversation/begin_run/finish_run/attach_evidence/clear_conversation/export_runs: identity, ownership, guarded lifecycle, retry lineage, limits and sanitized downloads |
| `src/ui/app.py` | Connection/capability controls, immutable paper workspaces, record/free forms, response/history rendering, submit_request orchestration, manual retry and export |
| `src/ui/README.md`, `requirements-ui.txt` | Actual usage, lightweight dependencies, auth/config, verification commands |
| `tests/test_ui*.py`, `tests/ui_http_fixture.py` | Unit, AppTest, actual localhost synthetic HTTP integration and opt-in P5 smoke |
| `tests/test_legacy_ui_adapters.py` | Preserved meaningful prompt/index/provider unit tests from the replaced legacy UI tests |

Actual pure-state functions consolidate the proposed complete/reject/fail/unknown
helpers into one guarded `finish_run` function. No backend schemas or existing
retrieval/generation modules changed. Correlation headers/backend run IDs remain
unsupported pending P5 agreement; client-only routing is implemented.

## Verification evidence

All commands ran from the repository root. Relevant final checks returned exit 0.
Local socket tests required sandbox permission for localhost listeners.

```bash
/private/tmp/p6-ui-clean-env/bin/python -m pip install -r requirements-ui.txt pytest
/private/tmp/p6-ui-clean-env/bin/python -m pytest -q tests/test_ui_api_client.py tests/test_ui_view_models.py tests/test_ui_record_loader.py tests/test_ui_conversation_state.py tests/test_ui.py tests/test_ui_p5_smoke.py
.venv/bin/python -m pytest -q tests/test_legacy_ui_adapters.py tests/test_generation_week6.py tests/test_qwen_client.py
```

| Check | Result |
| --- | --- |
| Clean-environment UI suite | 42 passed, 1 skipped; actual P5 smoke is the explicit skip |
| Existing adapter/generation/Qwen-client regression | 34 passed |
| Existing-environment combined UI unit/AppTest + regressions | 73 passed before the final clean-environment verification (synthetic HTTP adds one separate case) |
| Real localhost synthetic HTTP -> Streamlit -> answer -> citation | Passed; does not constitute P5 service verification |
| Browser walkthrough | Created free-query workspace, entered/submitted synthetic question, verified owning run/status/timing and expanded citation |
| Browser layout | Narrow viewport: headings/metadata wrap, answer and expandable evidence remain readable; sidebar collapses normally |
| Patch whitespace | Checked with git diff --check |

Runtime: macOS 26.6.2 arm64, Python 3.14.7. Existing environment: Streamlit 1.64.0,
requests 2.34.2, pytest 9.1.1, OpenAI 1.109.1, Pydantic 2.13.5. Clean environment:
Streamlit 1.66.1, requests 2.34.2, pytest 9.2.0, OpenAI 2.54.0, Pydantic 2.14.1.
The clean dependency snapshot is `requirements-ui-macos-py314.txt`. No model weights,
Java, FAISS, PyTorch or cluster account was needed for the clean UI test suite.
The legacy OpenAI/Pydantic dependency declarations remain for existing consumers;
the new UI does not import their generation clients.

## Acceptance coverage and remaining gates

Local tests cover transport request shapes/errors/timeouts, six display states,
invalid response handling, record files, citation fallback, rerender dispatch
counts, clear behavior, multi-workspace ownership, duplicate completion, repeat
IDs, retry lineage, limits and five-run export. These exercise the implemented
portions of T01–T23 and T28–T39. This is not a claim that every listed test level
or every real-world scenario in the design was executed.

- T24 remains pending against **P5's actual mock service**. The synthetic HTTP
  integration passes separately. P5's formal contract/server/captures/input sample
  were absent; field assumptions are enumerated in the handoff.
- T25–T27 and real-environment portions of T32,T35,T36,T38,T40 require P5.
- T33 header echo/mismatch cases are not implemented because no correlation
  extension was agreed. No such header is sent or backend execution ID fabricated.
- Real slow-call browser behavior, long production responses, reconnection and
  multi-session GPU busy behavior require P5's deployment; no async switching or
  cancellation is promised.
- Free queries and live five-query performance remain blocked when retrieval=false;
  original citation text remains conditional on passage_text=true.
- P5 field-level contract reconciliation (I1) and actual-service portion of I5
  remain open. Independent implementation proceeded using the supplied handoff.
- No actual model-quality, semantic-grounding or final held-out evaluation claim.

The downstream handoff is [P6_UI_handoff.md](P6_UI_handoff.md). It replaces the
planned filename `P5_UI_E2E_HANDOFF.md` at the user's request. It includes usage,
interface confirmations/optional changes, actual P5 smoke command and real E2E
results checklist. P5 should record pass/fail/blocked with environment revisions
and sanitized evidence. Shared schemas/split mappings remain `v0-proposed`.

Final review also added tests for a paper disappearing from the refreshed
catalogue (existing workspace submission is disabled) and invalid UTF-8 local
record files (actionable error rather than app failure). Final totals are 42 UI
passes plus 34 regression passes, with one explicit actual-P5-service skip.
No push, PR or merge has been performed; GitHub CLI is unavailable in this
workspace. The local branch and handoff are ready for review and later sharing.
