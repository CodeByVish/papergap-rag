import json
import pytest
from src.ui.conversation_state import new_session, create_conversation, begin_run, finish_run, attach_evidence, clear_conversation, export_runs


def test_routing_duplicates_retries_and_isolation():
    state, other = new_session(), new_session()
    assert state['ui_session_id'] != other['ui_session_id']
    a = create_conversation(state, 'Free question', 'paper-a')
    run = begin_run(state, a, {'question': 'q'}, {'mode': 'mock'})
    b = create_conversation(state, 'Free question', 'paper-b')
    with pytest.raises(ValueError, match='pending'):
        begin_run(state, b, {}, {})
    with pytest.raises(ValueError, match='pending'):
        clear_conversation(state, a)
    assert finish_run(state, a, run['client_run_id'], 'outcome_unknown', error='Timed out')
    retry = begin_run(state, a, {'question': 'q'}, {}, run['client_run_id'])
    assert retry['client_run_id'] != run['client_run_id']
    assert retry['message_id'] == run['message_id']
    assert not finish_run(state, a, run['client_run_id'], 'completed', answer={'bad': True})
    finish_run(state, a, retry['client_run_id'], 'completed', answer={'ok': True})
    attach_evidence(state, a, retry['client_run_id'], {'id': None}, error='Unavailable')
    assert state['conversations'][b]['runs'] == {}
    assert other['conversations'] == {}
    exported = json.loads(export_runs(state, [retry['client_run_id']]))
    assert len(exported['runs']) == 1 and exported['runs'][0]['outcome'] == 'completed'
    clear_conversation(state, a)
    assert not state['conversations'][a]['runs']


def test_limits_and_distinct_identical_queries():
    s = new_session()
    c = create_conversation(s, 'Free question', 'p')
    ids = []
    for _ in range(50):
        r = begin_run(s, c, {'question': 'same'}, {})
        ids.append(r['client_run_id'])
        finish_run(s, c, r['client_run_id'], 'completed')
    assert len(set(ids)) == 50
    with pytest.raises(ValueError, match='limit'):
        begin_run(s, c, {}, {})
    for _ in range(9):
        create_conversation(s, 'Demo record')
    with pytest.raises(ValueError, match='limit'):
        create_conversation(s, 'Demo record')
    clear_conversation(s, c, remove=True)
    assert c not in s['conversations']


def test_five_run_export_removes_private_state():
    s = new_session()
    c = create_conversation(s, 'Demo record')
    ids = []
    for _ in range(5):
        r = begin_run(s, c, {'record_index': 0}, {'mode': 'mock', 'token': 'private'})
        ids.append(r['client_run_id'])
        finish_run(s, c, r['client_run_id'], 'completed', answer={
            'result': {'answer': 'Synthetic'}, 'agent': {'raw_state': 'private'},
            'generation': {'api_key': 'private', 'backend': 'mock'}}, elapsed=10)
    data = export_runs(s, ids)
    assert 'private' not in data and 'raw_state' not in data
    assert len(json.loads(data)['runs']) == 5
    assert 'agent' in s['conversations'][c]['runs'][ids[0]]['answer_record']
