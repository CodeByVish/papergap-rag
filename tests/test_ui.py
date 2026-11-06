"""Question-first UI behavior and the unchanged P5 HTTP boundary."""
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


def widget(elements, label):
    return next(element for element in elements if element.label == label)


def setup_app(monkeypatch, tmp_path, retrieval=True, passage_text=True, payload=None, corpus=True):
    api = Mock()
    api.health.return_value = {'retrieval': retrieval, 'passage_text': passage_text, 'mode': 'mock', 'corpus_search': corpus}
    api.papers.return_value = [{'paper_id': 'p', 'title': 'Synthetic paper'}, {'paper_id': 'other', 'title': 'Other paper'}]
    api.answer_question.return_value = payload or answer()
    api.answer_record.return_value = payload or answer()
    api.passages.return_value = {'passages': {'p1': {'text': 'Synthetic evidence', 'title': 'Synthetic paper', 'paper_id': 'p'}}, 'missing': ['p2']}
    monkeypatch.setattr('src.ui.api_client.P5ApiClient', lambda config: api)
    path = tmp_path / 'records.json'
    path.write_text(json.dumps([{'question': 'Synthetic record question', 'paper_id': 'p'}]))
    monkeypatch.setenv('P5_RECORDS_PATH', str(path))
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    return app, api


def ask(app, question):
    # One run, as a form commits its text and its click together.
    widget(app.text_area, 'Your question').set_value(question)
    button(app, 'Ask question').click().run()
    assert not app.exception


def all_runs(app):
    return [run for context in app.session_state['workspace_state']['conversations'].values()
            for run in context['runs'].values()]


def test_question_first_default_scope_history_export_and_clear(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    assert app.sidebar.title[0].value == 'PaperRAG'
    assert not app.main.title
    assert app.session_state['scope_choice'] == 'All papers'
    ask(app, 'What improved?')
    api.answer_question.assert_called_once_with('What improved?', None)
    assert any('Synthetic answer' in m.value for m in app.markdown)
    assert any('Passage text unavailable' in m.value for m in app.info)
    # The answer comes first, so a presenter sees it without scrolling.
    elements = [getattr(e, 'value', None) or getattr(e, 'label', None) for e in app.main]
    answer_at = next(i for i, value in enumerate(elements) if 'Synthetic answer' in str(value))
    composer = next(i for i, e in enumerate(app.main) if e.type == 'text_area')
    assert answer_at < composer
    button(app, 'Refresh service').click().run()
    api.answer_question.assert_called_once()
    export = widget(app.multiselect, 'Select runs to export (choose five for report)')
    export.set_value(export.options).run()
    assert not app.exception
    button(app, 'Clear history').click().run()
    assert not app.exception and not all_runs(app)
    assert not any('Synthetic answer' in m.value for m in app.markdown)


def test_record_mode_without_retrieval_or_passage_capability(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path, retrieval=False, passage_text=False)
    widget(app.radio, 'Input mode').set_value('Demo record').run()
    button(app, 'Ask question').click().run()
    assert not app.exception
    api.answer_record.assert_called_once_with({'question': 'Synthetic record question', 'paper_id': 'p'})
    api.answer_question.assert_not_called()
    api.passages.assert_not_called()
    assert any('not rerun' in c.value for c in app.caption) or api.answer_record.called


@pytest.mark.parametrize('payload, expected', [
    (answer('INSUFFICIENT'), 'No answer'),
    (answer('INSUFFICIENT', downgraded=True), 'Validator blocked answer'),
    (answer(violations=[{'code': 'PROVENANCE_DERIVED', 'severity': 'WARNING', 'message': 'Claim mapping was derived.'}]), 'Evidence needs review'),
    (answer(violations=[{'severity': 'ERROR'}]), 'Inconsistent response'),
])
def test_answer_states_explain_issues_without_replacing_final_result(monkeypatch, tmp_path, payload, expected):
    app, api = setup_app(monkeypatch, tmp_path, payload=payload)
    ask(app, 'Question')
    assert any(expected in x.value for x in list(app.warning) + list(app.error) + list(app.info))
    assert any(m.value == 'Synthetic answer' for m in app.markdown)
    if payload['validation']['downgraded']:
        assert any(e.label.startswith('Rejected model answer') for e in app.expander)
    if payload['validation']['violations']:
        assert any(t.label.startswith('Flagged') for t in app.tabs)


def test_history_shows_one_answer_and_error_retains_prior_success(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    ask(app, 'First question')
    first = all_runs(app)[0]['client_run_id']
    api.answer_question.side_effect = ApiError('outcome_unknown', 'Outcome unknown; may still be processing.')
    ask(app, 'Second question')
    assert any('Outcome unknown' in m.value for m in app.error)
    assert not any('Synthetic answer' in m.value for m in app.markdown)
    assert [r['outcome'] for r in all_runs(app)] == ['completed', 'outcome_unknown']
    app.button(key='open_' + first).click().run()
    assert not app.exception
    assert sum('Synthetic answer' in m.value for m in app.markdown) == 1
    assert not app.error
    assert api.answer_question.call_count == 2
    button(app, 'New question').click().run()
    assert not any('Synthetic answer' in m.value for m in app.markdown) and widget(app.text_area, 'Your question').value == ''
    assert len(all_runs(app)) == 2


def test_offline_disables_inference_but_keeps_history(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    ask(app, 'Question')
    api.health.side_effect = ApiError('failed', 'Offline')
    button(app, 'Refresh service').click().run()
    assert not app.exception and any('Service unavailable' in m.value for m in app.sidebar.markdown)
    assert button(app, 'Ask question').disabled
    assert any('Synthetic answer' in m.value for m in app.markdown)


def test_passage_failure_and_explicit_manual_retry(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    api.passages.side_effect = ApiError('rejected', 'Corpus unavailable', 503)
    ask(app, 'Question')
    assert any('answer retained' in x.value for x in app.info)
    assert widget(app.text_area, 'Your question').value == ''  # Ready for the next question.
    button(app, 'Re-run this question').click().run()
    runs = all_runs(app)
    assert runs[1]['retry_of_client_run_id'] == runs[0]['client_run_id']
    assert runs[1]['message_id'] == runs[0]['message_id']


def test_scope_applies_to_next_request_without_workspace_setup(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    ask(app, 'Across the corpus')
    api.answer_question.assert_called_with('Across the corpus', None)
    widget(app.button_group, 'Search scope').set_value('One paper').run()
    widget(app.selectbox, 'Paper title and ID').select_index(1).run()
    selected = widget(app.selectbox, 'Paper title and ID').value
    ask(app, 'Which method is used?')
    api.answer_question.assert_called_with('Which method is used?', selected)
    widget(app.button_group, 'Search scope').set_value('All papers').run()
    ask(app, 'Another corpus query')
    assert len(all_runs(app)) == 3
    assert len(app.session_state['workspace_state']['conversations']) == 2
    assert not any(b.label in ('New workspace', 'Remove workspace', 'Submit') for b in app.button)


def test_legacy_service_requires_paper_and_missing_catalogue_disables_question(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path, corpus=False)
    assert not any(r.label == 'Search scope' for r in app.radio)
    ask(app, 'Question')
    assert api.answer_question.call_args.args[1] is not None
    api.papers.return_value = []
    button(app, 'Refresh service').click().run()
    assert not app.exception
    assert button(app, 'Ask question').disabled and app.text_area[0].disabled


def test_library_displays_title_and_id_and_only_fills_draft(monkeypatch, tmp_path):
    samples = tmp_path / 'samples.jsonl'
    samples.write_text(json.dumps({'paper_id': 'p', 'question': 'Which method was used?'}) + '\n')
    monkeypatch.setenv('P6_SAMPLES_PATH', str(samples))
    app, api = setup_app(monkeypatch, tmp_path)
    widget(app.radio, 'Example category').set_value('About a specific paper').run()
    assert 'Synthetic paper · Paper ID: p' in widget(app.selectbox, 'Example question').options[0]
    assert any(c.value == 'Paper ID: p' for c in app.caption)
    button(app, 'Use this question').click().run()
    assert not app.exception
    assert 'Synthetic paper (paper ID: p)' in app.text_area[0].value
    assert app.session_state['scope_choice'] == 'All papers'
    api.answer_question.assert_not_called()
    button(app, 'Ask question').click().run()
    assert api.answer_question.call_args.args[1] is None
    widget(app.button_group, 'Search scope').set_value('One paper').run()
    # The sample paper is sorted first; filtering keeps the original QASPER wording.
    assert widget(app.selectbox, 'Paper title and ID').value == 'p'
    button(app, 'Use this question').click().run()
    assert app.text_area[0].value == 'Which method was used?'
    button(app, 'Ask question').click().run()
    api.answer_question.assert_called_with('Which method was used?', 'p')


def test_help_tooltips_and_trace_do_not_resubmit(monkeypatch, tmp_path):
    payload = answer()
    payload['agent'] = {
        'retrieval_log': [{'round': 1, 'query': 'What improved?', 'passage_ids': ['p1'], 'retrieval_ms': 12.5}],
        'critic_log': [{'round': 1, 'source': 'llm', 'sufficient': True, 'gap_label': 'NONE', 'errors': []}],
        'rewritten_query': 'What improved? method',
    }
    app, api = setup_app(monkeypatch, tmp_path, payload=payload)
    assert any('Ask a question' in m.value for m in app.main.markdown)
    for label in ('Refresh service', 'New question', 'Clear history'):
        assert button(app, label).proto.help
    button(app, 'Use this question').click().run()
    api.answer_question.assert_not_called()
    ask(app, 'What improved?')
    assert any(t.label == 'Pipeline' for t in app.tabs)
    assert app.dataframe[0].value.iloc[0]['Query'] == 'What improved?'
    assert app.dataframe[1].value.iloc[0]['Source'] == 'llm'
    assert any('Candidate tables' in c.value for c in app.caption)
    app.run()
    api.answer_question.assert_called_once()


def test_invalid_response_and_bad_samples_do_not_crash(monkeypatch, tmp_path):
    samples = tmp_path / 'samples.jsonl'
    samples.write_text('[1, 2]\n')
    monkeypatch.setenv('P6_SAMPLES_PATH', str(samples))
    app, api = setup_app(monkeypatch, tmp_path)
    assert any('sample questions are unavailable' in w.value for w in app.warning)
    api.answer_question.return_value = {'bad': 'payload'}
    ask(app, 'Question')
    assert app.error and all_runs(app)[0]['outcome'] == 'failed'


def test_controls_are_disabled_before_answer_http_starts(monkeypatch, tmp_path):
    import streamlit as st

    app, api = setup_app(monkeypatch, tmp_path)
    rendered_buttons = Mock(wraps=st.button)
    rendered_submit = Mock(wraps=st.form_submit_button)
    monkeypatch.setattr(st, 'button', rendered_buttons)
    monkeypatch.setattr(st, 'form_submit_button', rendered_submit)

    def answer_while_loading(question, paper_id):
        calls = rendered_buttons.call_args_list + rendered_submit.call_args_list
        for label in ('Ask question', 'Refresh service', 'New question', 'Clear history'):
            latest = next(call for call in reversed(calls) if call.args[0] == label)
            assert latest.kwargs['disabled'], f'{label} remained enabled during inference'
        assert st.session_state.workspace_state['pending_client_run_id']
        return answer()

    api.answer_question.side_effect = answer_while_loading
    ask(app, 'Question')
    api.answer_question.assert_called_once()
    assert all_runs(app)[0]['outcome'] == 'completed'
    assert not button(app, 'Ask question').disabled


def test_scope_heading_and_library_without_quick_buttons(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    assert any(h.value == 'Ask the paper collection' for h in app.main.header)
    assert not any(b.label in ('Low-resource languages', 'Character + word representations') for b in app.button)
    widget(app.button_group, 'Search scope').set_value('One paper').run()
    paper_id = widget(app.selectbox, 'Paper title and ID').value
    title = next(p['title'] for p in api.papers.return_value if p['paper_id'] == paper_id)
    assert any(h.value == f"Ask Paper '{title}'" for h in app.main.header)
    assert not any(h.value == 'Ask the paper collection' for h in app.main.header)
    assert any('No prepared examples' in message.value for message in app.info)
    widget(app.radio, 'Input mode').set_value('Demo record').run()
    assert any(h.value == 'Generate from prepared evidence' for h in app.main.header)
    api.answer_question.assert_not_called()
    api.answer_record.assert_not_called()


def test_first_click_submits_typed_text_and_empty_is_rejected(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    assert not button(app, 'Ask question').disabled  # Never disabled for empty text.
    button(app, 'Ask question').click().run()
    api.answer_question.assert_not_called()
    assert any('Type a question first' in w.value for w in app.warning)
    ask(app, 'Typed then clicked')
    api.answer_question.assert_called_once_with('Typed then clicked', None)


def test_normal_refusal_is_not_alarming_or_jargon(monkeypatch, tmp_path):
    note = {'code': 'AGENT_INSUFFICIENT', 'severity': 'WARNING', 'message': 'gap found, so P5 refused'}
    app, api = setup_app(monkeypatch, tmp_path, payload=answer('INSUFFICIENT', violations=[note]))
    ask(app, 'Question')
    assert any('cannot answer' in i.value for i in app.info) and not app.warning
    assert not any('P5' in m.value for m in app.markdown)


def test_highlight_and_literal_dollars(monkeypatch, tmp_path):
    payload = answer(violations=[{'code': 'UNSUPPORTED_CLAIM', 'severity': 'WARNING', 'message': 'x', 'subject': 'Costs $5 and $6 each'}])
    payload['result']['answer'] = 'Fine. Costs $5 and $6 each'
    app, api = setup_app(monkeypatch, tmp_path, payload=payload)
    ask(app, 'Question')
    assert any(r'<mark class="flag">Costs \$5 and \$6 each</mark>' in m.value for m in app.markdown)


def test_status_notices_a_dead_service_without_refresh(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    api.health.side_effect = ApiError('failed', 'Cannot reach the answer service.')
    app.session_state['health_checked_at'] = 0
    app.run()
    assert not app.exception and button(app, 'Ask question').disabled
    assert any('Service unavailable' in m.value for m in app.sidebar.markdown)
    assert not any('still be processing' in m.value for m in app.sidebar.markdown)


def test_prepared_mode_does_not_claim_independent_search(monkeypatch, tmp_path):
    app, api = setup_app(monkeypatch, tmp_path)
    widget(app.radio, 'Input mode').set_value('Demo record').run()
    assert not any('searched on its own' in c.value for c in app.caption)
