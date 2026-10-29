"""P5 Option C UI. Run from the repository root with Streamlit."""
import os
from time import perf_counter
import streamlit as st
from src.ui.api_client import ApiConfig, ApiError, P5ApiClient
from src.ui.view_models import parse_answer_record, classify_answer, citation_ids, build_evidence_cards
from src.ui.record_loader import load_records, record_label
from src.ui.conversation_state import new_session, create_conversation, begin_run, finish_run, attach_evidence, clear_conversation, export_runs

st.set_page_config(page_title='PaperGap', page_icon='📄', layout='wide')


def refresh(client):
    st.session_state.health = {}
    st.session_state.papers = []
    st.session_state.connection_error = None
    try:
        st.session_state.health = client.health()
        if st.session_state.health['retrieval']:
            st.session_state.papers = client.papers()
    except ApiError as exc:
        st.session_state.connection_error = str(exc)


def submit_request(client, state, cid, submission, health, record=None, retry_of=None):
    run = begin_run(state, cid, submission, health, retry_of)
    rid = run['client_run_id']
    start = perf_counter()
    try:
        payload = client.answer_record(record) if record is not None else client.answer_question(submission['question'], submission['paper_id'])
        elapsed = (perf_counter() - start) * 1000
        parsed = parse_answer_record(payload)
        finish_run(state, cid, rid, 'completed', answer=parsed, elapsed=elapsed)
    except ApiError as exc:
        finish_run(state, cid, rid, exc.kind, error=str(exc), elapsed=(perf_counter() - start) * 1000)
        return
    except ValueError:
        finish_run(state, cid, rid, 'failed', error='Answer response does not match the P5 contract.', elapsed=(perf_counter() - start) * 1000)
        return
    except Exception:
        finish_run(state, cid, rid, 'outcome_unknown', error='Unexpected client failure; service outcome is unknown. Refresh service before retrying manually.', elapsed=(perf_counter() - start) * 1000)
        return
    ids = citation_ids(parsed)
    cards = dict.fromkeys(ids)
    if health.get('passage_text') and ids:
        start = perf_counter()
        try:
            cards = build_evidence_cards(ids, client.passages(ids))
            attach_evidence(state, cid, rid, cards, (perf_counter() - start) * 1000)
        except ApiError as exc:
            attach_evidence(state, cid, rid, cards, (perf_counter() - start) * 1000, str(exc))
    else:
        attach_evidence(state, cid, rid, cards)


def render_answer(run):
    submission = run['submission']
    st.subheader(submission.get('question') or submission.get('record_label', 'Exported state'))
    st.caption(f"Paper: {submission.get('paper_id') or 'record-owned'} · Run: {run['client_run_id']} · {run['outcome']}")
    if run['error']:
        st.error(run['error'])
    record = run['answer_record']
    if not record:
        return
    status = classify_answer(record)
    if status == 'Answered':
        st.success(status)
    else:
        st.warning(status)
    st.markdown(record['result']['answer'])
    if record['validation']['downgraded']:
        st.warning('Validator reason: ' + str(record['validation'].get('downgrade_reason') or 'Unavailable'))
        with st.expander('Rejected model answer — not the accepted answer'):
            raw = record['validation'].get('raw_result')
            st.text(raw.get('answer', 'Unavailable') if isinstance(raw, dict) else 'Unavailable')
    st.caption(f"Request ID: {record['request_id']} · Backend run ID unavailable · Answer HTTP: {run['answer_http_elapsed_ms']:.0f} ms · Retrieval rounds: {record['result']['retrieval_rounds']}")
    if run.get('evidence_error'):
        st.info('Citation lookup unavailable; answer retained. ' + run['evidence_error'])
    for pid, row in run['evidence'].items():
        with st.expander('Citation: ' + pid):
            st.code(pid, language=None)
            if row:
                st.text(str(row.get('title', '')))
                st.caption(f"{row.get('paper_id', '')} · {row.get('section', '')}")
                st.text(row['text'])
            else:
                st.info('Passage text unavailable')
    with st.expander('Validation, provenance, generation and supplied agent trace'):
        st.json({k: record[k] for k in ('validation', 'generation', 'agent') if k in record})
        st.json(record['result']['provenance'])
    st.divider()


def main():
    st.title('PaperGap — evidence-grounded QA')
    st.caption('Each question is independent. Workspace history is not sent to the model. Session history may be lost on refresh or reconnect.')
    try:
        client = P5ApiClient(ApiConfig.from_env())
    except ValueError as exc:
        st.error(str(exc))
        return
    if 'workspace_state' not in st.session_state:
        st.session_state.workspace_state = new_session()
    state = st.session_state.workspace_state
    if 'health' not in st.session_state:
        refresh(client)
    with st.sidebar:
        st.header('Connection')
        if st.button('Refresh service'):
            refresh(client)
        health = st.session_state.health
        if st.session_state.connection_error:
            st.error(st.session_state.connection_error)
        st.caption(f"Retrieval: {health.get('retrieval', 'unknown')} · Passage text: {health.get('passage_text', 'unknown')}")
        st.caption('Service mode: ' + str(health.get('mode', 'unknown')))
        mode = st.radio('New workspace mode', ['Free question', 'Demo record'])
        papers = st.session_state.papers
        paper = st.selectbox('Paper for new workspace', papers, format_func=lambda p: p.get('title') or p['paper_id']) if mode == 'Free question' and papers else None
        if mode == 'Free question' and not health.get('retrieval'):
            st.info('Free input disabled: service retrieval is unavailable.')
        if st.button('New workspace', disabled=bool(state['pending_client_run_id']) or (mode == 'Free question' and not paper)):
            try:
                create_conversation(state, mode, paper['paper_id'] if paper else None)
            except ValueError as exc:
                st.error(str(exc))
        choices = list(state['conversations'])
        if choices:
            current = state['active_conversation_id']
            cid = st.selectbox('Workspace', choices, index=choices.index(current),
                               format_func=lambda c: f"{state['conversations'][c]['mode']} · {state['conversations'][c]['paper_id'] or 'exported records'} · {c[:8]}")
            state['active_conversation_id'] = cid
            if st.button('Clear workspace', disabled=bool(state['pending_client_run_id'])):
                clear_conversation(state, cid)
            if st.button('Remove workspace', disabled=bool(state['pending_client_run_id'])):
                clear_conversation(state, cid, remove=True)
                st.rerun()
        all_runs = [r for c in state['conversations'].values() for r in c['runs'].values()]
        selected = st.multiselect('Select runs to export (choose five for report)', [r['client_run_id'] for r in all_runs])
        if selected:
            st.download_button('Download selected runs', export_runs(state, selected), 'papergap-ui-runs.json', 'application/json')
    cid = state['active_conversation_id']
    if cid is None:
        st.info('Create a workspace in the sidebar. Demo record mode works without free-query retrieval.')
        return
    conversation = state['conversations'][cid]
    st.header(conversation['mode'] + ': ' + (conversation['paper_id'] or 'exported AgentState inputs'))
    for run in conversation['runs'].values():
        render_answer(run)
    record = None
    submission = None
    health = st.session_state.health
    disabled = not health or bool(state['pending_client_run_id']) or len(conversation['runs']) >= 50
    if conversation['mode'] == 'Demo record':
        st.info('Uses an exported state as input; does not establish fresh retrieval.')
        path = os.getenv('P5_RECORDS_PATH')
        if not path:
            st.info('Set P5_RECORDS_PATH to a local JSON array or JSONL file supplied by P5.')
            return
        try:
            records = load_records(path)
        except ValueError as exc:
            st.error(str(exc))
            return
        index = st.selectbox('Exported record', range(len(records)), format_func=lambda i: record_label(records[i], i))
        record = records[index]
        submission = {'record_index': index, 'record_label': record_label(record, index), 'paper_id': record.get('paper_id'), 'question': record.get('question') if isinstance(record.get('question'), str) else None}
    else:
        paper_available = conversation['paper_id'] in {p['paper_id'] for p in st.session_state.papers}
        question = st.text_area('Complete question', disabled=not health.get('retrieval', False) or not paper_available)
        if not paper_available:
            st.info('Workspace paper is unavailable in the current catalogue. Refresh service or create a new workspace.')
        disabled = disabled or not health.get('retrieval') or not paper_available or not question.strip()
        submission = {'question': question.strip(), 'paper_id': conversation['paper_id']}
    if len(conversation['runs']) >= 50:
        st.info('Run limit reached. Export and clear this workspace.')
    previous = list(conversation['runs'].values())
    retry_of = None
    if previous and previous[-1]['submission'] == submission:
        if st.checkbox('Manual retry of the last matching question (new execution)'):
            retry_of = previous[-1]['client_run_id']
    if st.button('Submit', disabled=disabled):
        with st.spinner('Processing — the service may take up to 120 seconds or longer. No streaming.'):
            submit_request(client, state, cid, submission, health, record, retry_of)
        st.rerun()


if __name__ == '__main__':
    main()
