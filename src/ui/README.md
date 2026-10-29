# PaperGap Option C UI

The entry point is a P5 HTTP client. It does not load models, indexes, Java or
retrieval libraries. P5 operates the real service and tunnel. The former provider
UI has been replaced; its reusable provider/retrieval adapters remain available.

## Install and run

From the repository root, create/activate a Python environment:

```bash
python -m venv .venv-ui
source .venv-ui/bin/activate
python -m pip install -r requirements-ui.txt
export P5_API_BASE=http://127.0.0.1:8000
export P5_RECORDS_PATH=/absolute/local/path/to/p5-exported-states.jsonl
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

PowerShell configuration after activating the environment:

```powershell
$env:P5_API_BASE = 'http://127.0.0.1:8000'
$env:P5_RECORDS_PATH = 'C:\local\p5-exported-states.jsonl'
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

Open `http://127.0.0.1:8501`. The record file is a JSON array or JSONL of original
exported AgentState objects. Answer captures are not valid inputs. Keep real
records outside Git. Exact input-state validation belongs to P5; the UI checks
container shape and passes the selected object unchanged.

`P5_ANSWER_TIMEOUT` defaults to 120 seconds (allowed range 120–3600); connection
timeout is 5 seconds and auxiliary read timeout is 10 seconds. No POST retries.
If authentication is enabled, obtain exact header/scheme from P5 first. Set both
`P5_API_TOKEN` and `P5_AUTH_HEADER`; `P5_AUTH_SCHEME` is optional (e.g. `Bearer`
only if P5 confirms). Supported header names are Authorization, X-API-Key,
X-Auth-Token and X-Demo-Token. No token is required by default. Never commit tokens.
These are client configuration options, not a claim about P5's actual auth scheme.

## Use

1. Refresh service; inspect retrieval and passage-text capabilities.
2. Create a Free question workspace with a selected paper, or a Demo record
   workspace and select an exported state. Free input is disabled without retrieval.
3. Submit one complete independent question. Wait for the non-streaming answer.
   Workspace history is not sent to the model. A blocking request may prevent
   workspace interaction; no background processing or cancellation is promised.
4. Inspect answer/refusal, warning or validator block; expand citations and
   diagnostics. Rejected model text is clearly separated from the final answer.
5. Each submission gets a new client run ID; P5 request_id keeps its own meaning.
   To link a retry, check the manual-retry option for the last matching submission.
   Timeout/disconnect means outcome unknown, not cancellation.
6. Select five runs in the sidebar and download their JSON for reporting. Timings
   cover answer HTTP waiting/processing, not isolated inference; citations are timed
   separately. Mock/unknown timings cannot establish live querying performance.

History is session-only: max 10 workspaces and 50 attempts per workspace. Export
and clear/remove explicitly at the limit. Clear cannot cancel pending inference.
Refresh/reconnect/new browser tabs may lose history and cannot recover server runs.
Exports omit agent state and sensitive-key configuration; review downloaded text
before sharing because answer content and provenance are retained.

## Test

```bash
python -m pip install pytest
python -m pytest -q tests/test_ui_api_client.py tests/test_ui_view_models.py tests/test_ui_record_loader.py tests/test_ui_conversation_state.py tests/test_ui.py tests/test_ui_p5_smoke.py
```

The default HTTP integration test starts a localhost **synthetic** fixture. It is
not P5's mock service. The separate P5 test is skipped unless explicitly enabled:

```bash
P5_RUN_SMOKE=1 python -m pytest -q tests/test_ui_p5_smoke.py::test_actual_p5_service
```

This requires P5's actual running service and `P5_RECORDS_PATH`; missing inputs or
service failures fail the explicitly requested check. See
[the P5 handoff](../../docs/P6/P6_UI_handoff.md) for contract assumptions and E2E steps.
