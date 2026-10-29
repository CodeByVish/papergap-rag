import json
from pathlib import Path
from unittest.mock import Mock
import pytest
from streamlit.testing.v1 import AppTest
from src.ui.api_client import ApiError
from tests.test_ui_view_models import answer

APP = Path(__file__).resolve().parents[1] / 'src/ui/app.py'


def button(app, label):
    return next(b for b in app.button if b.label == label)


def setup_app(monkeypatch, tmp_path, retrieval=True, passage_text=True, payload=None):
    api = Mock()
    api.health.return_value = {'retrieval': retrieval, 'passage_text': passage_text, 'mode': 'mock'}
    api.papers.return_value = [{'paper_id': 'p', 'title': 'Synthetic paper'}]
    api.answer_question.return_value = payload or answer()
    api.answer_record.return_value = payload or answer()
    api.passages.return_value = {'passages': {'p1': {'text': 'Synthetic evidence', 'title': 'Paper'}}, 'missing': ['p2']}
    monkeypatch.setattr('src.ui.api_client.P5ApiClient', lambda config: api)
    path = tmp_path / 'records.json'
    path.write_text(json.dumps([{'question': 'Synthetic record question', 'paper_id': 'p'}]))
    monkeypatch.setenv('P5_RECORDS_PATH', str(path))
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    return app, api


def test_question_rerun_export_and_clear(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    button(app, 'New workspace').click().run()
    app.text_area[0].set_value('What improved?').run()
    button(app, 'Submit').click().run()
    assert not app.exception
    api.answer_question.assert_called_once_with('What improved?', 'p')
    assert any('Synthetic answer' in m.value for m in app.markdown)
    assert any('Passage text unavailable' in m.value for m in app.info)
    button(app, 'Refresh service').click().run()
    api.answer_question.assert_called_once()
    ids = app.multiselect[0].options
    app.multiselect[0].set_value(ids).run()
    assert not app.exception
    api.answer_question.assert_called_once()
    button(app, 'Clear workspace').click().run()
    assert not app.subheader


def test_record_mode_and_no_passage_capability(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path, retrieval=False, passage_text=False)
    app.radio[0].set_value('Demo record').run()
    button(app, 'New workspace').click().run()
    button(app, 'Submit').click().run()
    assert not app.exception
    api.answer_record.assert_called_once_with({'question': 'Synthetic record question', 'paper_id': 'p'})
    api.answer_question.assert_not_called()
    api.passages.assert_not_called()


@pytest.mark.parametrize('payload', [answer('INSUFFICIENT'), answer('INSUFFICIENT', downgraded=True), answer(violations=[{'severity': 'WARNING'}])])
def test_answer_states(monkeypatch, tmp_path, payload):
    app, api = setup_app(monkeypatch, tmp_path, payload=payload)
    button(app, 'New workspace').click().run()
    app.text_area[0].set_value('Question').run()
    button(app, 'Submit').click().run()
    assert not app.exception
    assert app.warning


def test_error_retains_prior_success(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    button(app, 'New workspace').click().run()
    app.text_area[0].set_value('Question').run()
    button(app, 'Submit').click().run()
    api.answer_question.side_effect = ApiError('outcome_unknown', 'Outcome unknown; may still be processing.')
    button(app, 'Submit').click().run()
    assert not app.exception
    assert any('Synthetic answer' in m.value for m in app.markdown)
    assert any('Outcome unknown' in m.value for m in app.error)
    state = app.session_state['workspace_state']
    assert [r['outcome'] for c in state['conversations'].values() for r in c['runs'].values()] == ['completed', 'outcome_unknown']


def test_offline(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    api.health.side_effect = ApiError('failed', 'Offline')
    button(app, 'Refresh service').click().run()
    assert not app.exception and app.error
    assert button(app, 'New workspace').disabled


def test_passage_failure_and_manual_retry(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    api.passages.side_effect = ApiError('rejected', 'Corpus unavailable', 503)
    button(app, 'New workspace').click().run()
    app.text_area[0].set_value('Question').run()
    button(app, 'Submit').click().run()
    assert not app.exception and any('answer retained' in x.value for x in app.info)
    app.checkbox[0].check().run()
    button(app, 'Submit').click().run()
    state = app.session_state['workspace_state']
    runs = list(state['conversations'][state['active_conversation_id']]['runs'].values())
    assert runs[1]['retry_of_client_run_id'] == runs[0]['client_run_id']
    assert runs[1]['message_id'] == runs[0]['message_id']


def test_two_workspaces_and_invalid_payload(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    button(app, 'New workspace').click().run()
    app.text_area[0].set_value('First workspace').run()
    button(app, 'Submit').click().run()
    button(app, 'New workspace').click().run()
    assert not app.subheader
    api.answer_question.return_value = {'bad': 'payload'}
    app.text_area[0].set_value('Second workspace').run()
    button(app, 'Submit').click().run()
    assert not app.exception and app.error
    state = app.session_state['workspace_state']
    conversations = list(state['conversations'].values())
    assert list(conversations[0]['runs'].values())[0]['outcome'] == 'completed'
    assert list(conversations[1]['runs'].values())[0]['outcome'] == 'failed'


def test_catalogue_disappears_disables_existing_workspace(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    button(app, 'New workspace').click().run()
    app.text_area[0].set_value('Question').run()
    api.papers.return_value = []
    button(app, 'Refresh service').click().run()
    assert not app.exception
    assert button(app, 'Submit').disabled and app.text_area[0].disabled
    api.answer_question.assert_not_called()
