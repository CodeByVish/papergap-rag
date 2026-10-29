"""Real HTTP checks: synthetic integration by default; P5 opt-in separately."""
import os
import pytest
from streamlit.testing.v1 import AppTest
from src.ui.api_client import ApiConfig, P5ApiClient
from src.ui.record_loader import load_records
from src.ui.view_models import parse_answer_record
from tests.ui_http_fixture import serve
from tests.test_ui import APP, button


def test_synthetic_http_ui_smoke(monkeypatch):
    with serve() as base:
        monkeypatch.setenv('P5_API_BASE', base)
        app = AppTest.from_file(str(APP)).run()
        button(app, 'New workspace').click().run()
        app.text_area[0].set_value('Synthetic independent question').run()
        button(app, 'Submit').click().run()
        assert not app.exception
        assert any('synthetic test answer' in x.value for x in app.markdown)
        assert any('Synthetic evidence' in x.value for x in app.text)


@pytest.mark.skipif(os.getenv('P5_RUN_SMOKE') != '1', reason='P5 service/contract unavailable; set P5_RUN_SMOKE=1 and P5_RECORDS_PATH when supplied')
def test_actual_p5_service():
    path = os.getenv('P5_RECORDS_PATH')
    assert path, 'P5_RECORDS_PATH is required for explicitly requested P5 smoke'
    client = P5ApiClient(ApiConfig.from_env())
    health = client.health()
    records = load_records(path)
    result = parse_answer_record(client.answer_record(records[0]))
    if health['passage_text'] and result['result']['citations']:
        client.passages(result['result']['citations'])
    app = AppTest.from_file(str(APP)).run()
    app.radio[0].set_value('Demo record').run()
    button(app, 'New workspace').click().run()
    button(app, 'Submit').click().run()
    assert not app.exception
    state = app.session_state['workspace_state']
    runs = [r for c in state['conversations'].values() for r in c['runs'].values()]
    assert runs and runs[0]['outcome'] == 'completed'
