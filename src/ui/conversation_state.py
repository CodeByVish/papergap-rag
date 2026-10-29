"""Session-local execution identities and guarded terminal transitions."""
from copy import deepcopy
from datetime import datetime, timezone
from uuid import uuid4
import json


def uid():
    return str(uuid4())


def now():
    return datetime.now(timezone.utc).isoformat()


def new_session():
    return {'ui_session_id': uid(), 'conversations': {}, 'active_conversation_id': None, 'pending_client_run_id': None}


def create_conversation(state, mode, paper_id=None):
    if len(state['conversations']) >= 10:
        raise ValueError('Workspace limit reached. Export and remove a workspace first.')
    cid = uid()
    state['conversations'][cid] = {'id': cid, 'mode': mode, 'paper_id': paper_id, 'runs': {}}
    state['active_conversation_id'] = cid
    return cid


def begin_run(state, cid, submission, capabilities, retry_of=None):
    if state['pending_client_run_id']:
        raise ValueError('A request is already pending in this session.')
    conversation = state['conversations'][cid]
    if len(conversation['runs']) >= 50:
        raise ValueError('Run limit reached. Export and clear this workspace first.')
    prior = conversation['runs'].get(retry_of) if retry_of else None
    if retry_of and (not prior or prior['submission'] != submission):
        raise ValueError('Retry must reference the same submission in this workspace.')
    rid = uid()
    run = {'client_run_id': rid, 'conversation_id': cid,
           'message_id': prior['message_id'] if prior else uid(), 'retry_of_client_run_id': retry_of,
           'submission': deepcopy(submission), 'capabilities': {k: deepcopy(capabilities[k]) for k in ('retrieval', 'passage_text', 'mode') if k in capabilities},
           'service_mode': capabilities.get('mode', 'unknown'), 'submitted_at': now(), 'outcome': 'pending', 'answer_record': None,
           'error': None, 'evidence': {}, 'answer_http_elapsed_ms': None, 'citation_http_elapsed_ms': None}
    conversation['runs'][rid] = run
    state['pending_client_run_id'] = rid
    return run


def finish_run(state, cid, rid, outcome, answer=None, error=None, elapsed=None):
    run = state['conversations'][cid]['runs'][rid]
    if run['outcome'] != 'pending':
        return False
    if outcome not in ('completed', 'rejected', 'failed', 'outcome_unknown'):
        raise ValueError('Invalid terminal outcome.')
    run.update(outcome=outcome, answer_record=deepcopy(answer), error=error,
               answer_http_elapsed_ms=elapsed, finished_at=now())
    if state['pending_client_run_id'] == rid:
        state['pending_client_run_id'] = None
    return True


def attach_evidence(state, cid, rid, cards, elapsed=None, error=None):
    run = state['conversations'][cid]['runs'][rid]
    if run['outcome'] != 'completed':
        raise ValueError('Evidence requires a completed answer.')
    run.update(evidence=deepcopy(cards), citation_http_elapsed_ms=elapsed, evidence_error=error)


def clear_conversation(state, cid, remove=False):
    conversation = state['conversations'][cid]
    if any(r['outcome'] == 'pending' for r in conversation['runs'].values()):
        raise ValueError('Cannot clear a pending workspace; this does not cancel inference.')
    if remove:
        del state['conversations'][cid]
        if state['active_conversation_id'] == cid:
            state['active_conversation_id'] = next(iter(state['conversations']), None)
    else:
        conversation['runs'].clear()


def export_runs(state, ids):
    runs = [deepcopy(r) for c in state['conversations'].values() for r in c['runs'].values() if r['client_run_id'] in ids]
    for run in runs:
        record = run.get('answer_record')
        if record:
            record.pop('agent', None)  # May contain the full exported AgentState.
    def sanitize(value):
        if isinstance(value, dict):
            return {k: sanitize(v) for k, v in value.items() if not any(secret in k.lower() for secret in ('token', 'secret', 'password', 'authorization', 'credential', 'api_key'))}
        if isinstance(value, list):
            return [sanitize(v) for v in value]
        return value
    runs = sanitize(runs)
    return json.dumps({'schema_version': 'p6-ui-export-v1', 'exported_at': now(),
                       'timing_definition': 'answer_http_elapsed_ms includes HTTP waiting/processing; excludes citations and rendering. Not model inference time.',
                       'runs': runs}, indent=2)
