"""Scientific paper QA: a question-first UI over the P5 HTTP boundary."""
import os
import json
from pathlib import Path
from time import perf_counter
import streamlit as st
from src.ui.api_client import ApiConfig, ApiError, P5ApiClient
from src.ui.view_models import parse_answer_record, classify_answer, citation_ids, build_evidence_cards
from src.ui.record_loader import load_records, record_label
from src.ui.conversation_state import new_session, create_conversation, begin_run, finish_run, attach_evidence, clear_conversation, export_runs

st.set_page_config(page_title='NLP Scientific Paper RAG', page_icon='📄', layout='wide')

CORPUS_SAMPLE_QUESTIONS = [
    'What methods are used for low-resource language identification?',
    'How do studies combine character-level and word-level representations?',
    'What approaches improve cross-lingual transfer for low-resource languages?',
]


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


def submit_request(client, state, cid, run, health, record=None):
    submission = run['submission']
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



def queue_request(state, cid, mode, paper_id, submission, health, record, retry_of):
    """Capture the run in the button callback, before controls render as disabled."""
    if state['pending_client_run_id']:
        return
    if cid is None:
        cid = create_conversation(state, mode, paper_id)
    state['active_conversation_id'] = cid
    run = begin_run(state, cid, submission, health, retry_of)
    st.session_state.queued_request = (cid, run['client_run_id'], record)


def load_paper_titles():
    path = Path(os.getenv('P6_PAPER_CATALOG_PATH') or
                Path(__file__).resolve().parents[2] / 'data/processed/p6-paper-catalog.json')
    try:
        titles = json.loads(path.read_text(encoding='utf-8'))
        return {key: value for key, value in titles.items()
                if isinstance(key, str) and isinstance(value, str)} if isinstance(titles, dict) else {}
    except (OSError, ValueError):
        return {}


def paper_label(paper_id, titles):
    title = titles.get(paper_id)
    return f'{title} · {paper_id}' if title else (paper_id or 'All papers')


def render_pipeline_trace(record, submission, titles=None):
    with st.expander('Pipeline details'):
        search = record.get('search') or {}
        if search:
            st.caption('Search scope: ' + ('All indexed papers' if search.get('scope') == 'corpus' else 'One paper'))
            if search.get('source_papers'):
                st.caption('Retrieved papers before final prompt selection: ' + '; '.join(paper_label(pid, titles or {}) for pid in search['source_papers']))
        if 'record_index' in submission:
            st.info('Prepared record: any retrieval trace belongs to the saved input. This submission runs generation, not fresh retrieval.')
        agent = record.get('agent') or {}
        rounds = agent.get('retrieval_log') or []
        critics = agent.get('critic_log') or []
        st.caption('Read this alongside the answer and validation warnings. Traces show supplied backend events, not hidden model reasoning.')
        if rounds:
            st.dataframe([{
                'Round': row.get('round'),
                'Query': row.get('query', ''),
                'Triggered by': row.get('triggered_by', ''),
                'Section': row.get('section') or ('Whole corpus' if search.get('scope') == 'corpus' else 'Whole paper'),
                'Passages': len(row.get('passage_ids') or []),
                'Paper IDs': ', '.join(row.get('paper_ids') or []),
                'Scope': row.get('search_scope', 'Not supplied'),
                'Retrieval ms': row.get('retrieval_ms'),
            } for row in rounds], hide_index=True)
            for row in rounds:
                st.caption('Round ' + str(row.get('round')) + ' passage IDs')
                st.code('\n'.join(row.get('passage_ids') or []), language=None)
        else:
            st.info('No per-round retrieval trace was supplied for this response.')
        if critics:
            st.markdown('**Critic decisions**')
            st.dataframe([{
                'Round': row.get('round'), 'Source': row.get('source'),
                'Sufficient': row.get('sufficient'), 'Gap': row.get('gap_label'),
                'Errors': '; '.join(str(e) for e in row.get('errors', [])),
            } for row in critics], hide_index=True)
        if agent.get('rewritten_query'):
            st.markdown('**Last rewritten query**')
            st.text(agent['rewritten_query'])
        st.caption('Separate BM25/dense candidate rankings, RRF scores and reranker scores are not included in this API trace. They cannot be reconstructed from the final rank alone.')


def render_usage_help():
    with st.popover('ⓘ How to use', help='Learn how to ask questions, use examples and review evidence.'):
        st.markdown(
            '**Ask a question**\n\n'
            '1. Keep **All papers**, or select **One paper** to limit retrieval.\n'
            '2. Type into **Your question**, or choose an example below it.\n'
            '3. Click **Ask question**. No workspace setup is needed.\n\n'
            '**Read the result**\n\n'
            'The submitted question appears above its **Answer**. Review any warning, '
            'then expand **Sources**, **Pipeline details**, or **Debug information**. '
            'A warning does not certify that an answer is correct.\n\n'
            '**History and advanced tools**\n\n'
            'Use **History** below Search scope to open one previous result. '
            '**New question** clears the draft and result view. '
            '**Advanced settings** contains prepared-record mode, exports and history cleanup.\n\n'
            'Questions are independent: history is not sent to the model. '
            'Wait for completion before asking again. Export useful runs before closing '
            'or refreshing the page; history is session-only.'
        )


def render_validation(record):
    """Explain the actual validation state without treating every warning as a refusal."""
    status = classify_answer(record)
    validation = record['validation']
    if status == 'Answered':
        st.caption('Answer returned without validation warnings. Check the sources for factual accuracy.')
        return
    if status == 'Answer with warnings':
        st.warning('Evidence needs review — the answer was returned, but validation flagged issues. '
                   'Check the details and cited passages before relying on it.')
    elif status == 'Validator blocked answer':
        st.warning('Validator blocked answer — the displayed final response is a refusal. '
                   'The rejected draft is available separately.')
    elif status == 'Inconsistent response':
        st.error('Inconsistent response — evidence status and validation disagree. '
                 'Treat this result as unverified and inspect Debug information.')
    else:
        st.warning(status + ' — the service did not accept an evidence-supported answer.')
    if validation.get('downgrade_reason'):
        st.caption('Validator reason: ' + str(validation['downgrade_reason']))
    if validation['violations']:
        with st.expander('What was flagged?'):
            for violation in validation['violations']:
                st.markdown('**' + str(violation.get('code') or 'Validation issue') + '**')
                st.write(str(violation.get('message') or 'No explanation supplied by the service.'))
                if violation.get('subject'):
                    st.caption('Subject: ' + str(violation['subject']))
                st.caption('Severity: ' + str(violation.get('severity') or 'Not supplied'))
    if validation['downgraded']:
        with st.expander('Rejected model answer — not the accepted answer'):
            raw = validation.get('raw_result')
            st.text(raw.get('answer', 'Unavailable') if isinstance(raw, dict) else 'Unavailable')


def render_answer(run, titles):
    submission = run['submission']
    st.divider()
    with st.container(border=True):
        st.caption('Your submitted question')
        st.write(submission.get('question') or submission.get('record_label', 'Exported state'))
        scope = 'Prepared evidence' if 'record_index' in submission else paper_label(submission.get('paper_id'), titles)
        st.caption('Search scope for this result: ' + scope)
    st.subheader('Answer')
    if run['error']:
        st.error(run['error'])
        st.info('This attempt has no accepted answer. Previous results remain available in History.')
    record = run['answer_record']
    if record:
        # Only result.answer is accepted; raw_result is always shown separately as rejected.
        st.markdown(record['result']['answer'])
        render_validation(record)
        with st.expander(f"Sources · {len(run['evidence'])} cited passages"):
            if run.get('evidence_error'):
                st.info('Citation lookup unavailable; answer retained. ' + run['evidence_error'])
            if not run['evidence']:
                st.info('No passages were cited for this response.')
            for number, (pid, row) in enumerate(run['evidence'].items(), 1):
                source = paper_label(row['paper_id'], titles) if row and row.get('paper_id') else (row.get('title') if row else None)
                st.markdown(f"**[{number}] {source or 'Source paper unavailable'}**")
                if row:
                    if row.get('title') and not titles.get(row.get('paper_id')):
                        st.write(row['title'])
                    st.caption('Section: ' + str(row.get('section') or 'Not supplied'))
                    st.text(row['text'])
                else:
                    st.info('Passage text unavailable')
                st.caption('Passage ID: ' + pid)
        render_pipeline_trace(record, submission, titles)
    with st.expander('Debug information'):
        st.caption(f"Client run: {run['client_run_id']} · Outcome: {run['outcome']}")
        elapsed = run['answer_http_elapsed_ms']
        if elapsed is not None:
            st.caption(f'Answer HTTP: {elapsed:.0f} ms (includes waiting; not isolated inference time)')
        if record:
            st.caption(f"Request ID: {record['request_id']} · Retrieval rounds: {record['result']['retrieval_rounds']}")
            st.json({k: record[k] for k in ('validation', 'generation', 'agent', 'search') if k in record})
            st.json(record['result']['provenance'])


def load_samples():
    path = os.getenv('P6_SAMPLES_PATH')
    if not path:
        return []
    try:
        rows = [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]
        if any(not isinstance(row, dict) or not isinstance(row.get('paper_id'), str)
               or not row['paper_id'].strip() or not isinstance(row.get('question'), str)
               or not row['question'].strip() for row in rows):
            raise ValueError('Invalid sample question')
        return rows
    except (OSError, ValueError):
        st.warning('Prepared sample questions are unavailable; rerun local setup. You can still type a question.')
        return []


def set_draft(question):
    st.session_state.question_draft = question


def new_question():
    set_draft('')
    st.session_state.history_run = None


def clear_history(state):
    for cid in list(state['conversations']):
        clear_conversation(state, cid, remove=True)
    new_question()
    st.session_state.export_selection = []


def render_question_library(samples, titles, paper_id, corpus_scope, disabled):
    """One example library for both corpus and paper-filtered questions."""
    matching = [row for row in samples if corpus_scope or row['paper_id'] == paper_id]
    with st.expander('Browse all examples'):
        st.caption('Development examples, not held-out evaluation questions. Select one to edit before asking.')
        if not matching and not corpus_scope:
            st.info('No prepared examples are available for this paper. Type your own question above.')
            return
        groups = (['Across all papers'] if corpus_scope else []) + (['About a specific paper'] if matching else [])
        group = st.radio('Example category', groups, horizontal=True, key='example_category', disabled=disabled,
                         help='Topic queries search the corpus. Paper-specific examples identify their source by title and ID.')
        if group == 'Across all papers':
            examples = [{'question': question, 'paper_id': None} for question in CORPUS_SAMPLE_QUESTIONS]
        else:
            examples = matching
        def label(index):
            row = examples[index]
            if row['paper_id']:
                return f"{row['question']} — {row.get('title') or titles.get(row['paper_id'], 'Untitled paper')} · Paper ID: {row['paper_id']}"
            return row['question']
        index = st.selectbox('Example question', range(len(examples)), format_func=label, disabled=disabled,
                             help='Paper-specific options show the question, paper title and paper ID.')
        example = examples[index]
        question = example['question']
        if example['paper_id']:
            title = example.get('title') or titles.get(example['paper_id'])
            st.write(title or 'Paper title unavailable')
            st.caption('Paper ID: ' + example['paper_id'])
            if corpus_scope:
                # QASPER questions often say “they”; anchor them without silently enabling a paper filter.
                question = f"In the paper {title or example['paper_id']} (paper ID: {example['paper_id']}), {question}"
                st.caption('The paper reference is included in the draft. Search scope stays All papers.')
        st.button('Use this question', on_click=set_draft, args=(question,), disabled=disabled,
                  help='Fill Your question without submitting or changing the selected search scope.')
        library = ([{'paper_id': None, 'question': q} for q in CORPUS_SAMPLE_QUESTIONS] if corpus_scope else []) + [
            {**row, 'title': row.get('title') or titles.get(row['paper_id'], '')} for row in matching]
        st.download_button('Download sample questions', json.dumps(library, indent=2),
                           'scientific-paper-sample-questions.json', 'application/json',
                           help='Save the example questions with their paper IDs and titles. No inference is run.')


def main():
    try:
        config = ApiConfig.from_env()
        client = P5ApiClient(config)
    except ValueError as exc:
        st.error(str(exc))
        return
    if 'workspace_state' not in st.session_state:
        st.session_state.workspace_state = new_session()
    state = st.session_state.workspace_state
    if 'health' not in st.session_state:
        refresh(client)
    if 'next_history_run' in st.session_state:
        st.session_state.history_run = st.session_state.pop('next_history_run')
    samples = load_samples()
    titles = load_paper_titles()
    titles.update({p['paper_id']: p['title'] for p in st.session_state.papers if p.get('title')})
    runs = {r['client_run_id']: r for c in state['conversations'].values() for r in c['runs'].values()}
    pending = bool(state['pending_client_run_id'])
    with st.sidebar:
        st.title('NLP Scientific Paper RAG')
        render_usage_help()
        st.header('Connection')
        if st.button('Refresh service', disabled=pending,
                     help='Check API availability and reload capabilities and papers. Does not submit a question or reload configuration.'):
            refresh(client)
            titles.update({p['paper_id']: p['title'] for p in st.session_state.papers if p.get('title')})
        health = st.session_state.health
        if st.session_state.connection_error:
            st.error(st.session_state.connection_error)
        else:
            st.caption('Service connected · ' + str(health.get('backend', 'unknown')) + ' · ' + str(health.get('model_id', 'model not reported')))
        st.header('Search scope')
        scope = st.radio('Search scope', ['All papers', 'One paper'], label_visibility='collapsed', disabled=pending,
                         help='Applies to the next question. All papers searches the indexed collection; One paper restricts retrieval.') if health.get('corpus_search') else 'One paper'
        paper_id = None
        papers = st.session_state.papers
        if scope == 'One paper':
            if not health.get('corpus_search'):
                st.caption('This service supports paper-scoped search only.')
            if papers:
                sample_ids = {row['paper_id'] for row in samples}
                papers = sorted(papers, key=lambda p: (p['paper_id'] not in sample_ids, p['paper_id']))
                paper_id = st.selectbox('Paper title and ID', [p['paper_id'] for p in papers], disabled=pending,
                                        format_func=lambda pid: paper_label(pid, titles),
                                        help='Restrict the next question to this paper. Titles are readable labels; IDs identify the source.')
            else:
                st.info('No papers available. Refresh service to reload the catalogue.')
        else:
            st.caption(f'Search across {len(papers):,} indexed papers.')
        st.header('History')
        history_ids = sorted(runs, key=lambda rid: runs[rid]['submitted_at'], reverse=True)
        if st.session_state.get('history_run') not in runs:
            st.session_state.history_run = None
        def history_label(rid):
            if rid is None:
                return 'New question'
            run = runs[rid]
            text = run['submission'].get('question') or run['submission'].get('record_label', 'Prepared record')
            return f"{text} · {run['outcome']} · {run['submitted_at']} · {rid[:8]}"
        st.selectbox('Previous questions', [None] + history_ids, key='history_run', format_func=history_label,
                     disabled=pending, help='Open one saved question and its answer. Does not rerun inference or change search scope.')
        st.button('+ New question', on_click=new_question, disabled=pending,
                  help='Clear the draft and selected answer. Previous runs remain in History; the search scope stays selected.')
        with st.expander('Advanced settings'):
            mode = st.radio('Input mode', ['Free question', 'Demo record'], disabled=pending,
                            help='Free question runs fresh retrieval. Demo record generates from prepared evidence without fresh retrieval.')
            st.caption(f"Retrieval: {health.get('retrieval', 'unknown')} · Passage text: {health.get('passage_text', 'unknown')} · Agent: {health.get('agent', False)}")
            st.caption('API: ' + config.base_url)
            selected = st.multiselect('Select runs to export (choose five for report)', history_ids, key='export_selection', disabled=pending,
                                      format_func=history_label, help='Choose saved attempts for the JSON report download. Full agent traces are omitted.')
            if selected:
                st.download_button('Download selected runs', export_runs(state, selected), 'scientific-paper-rag-runs.json',
                                   'application/json', help='Save answers, citations, validation and HTTP timings. This does not call the model.')
            st.button('Clear history', on_click=clear_history, args=(state,), disabled=pending or not runs,
                      help='Delete all session history and drafts. Export first; this does not delete corpus files or cancel inference.')
            st.caption('History is session-only. Up to 10 search contexts and 50 attempts per context; export before clearing.')
    if mode == 'Demo record':
        st.header('Generate from prepared evidence')
    elif scope == 'All papers':
        st.header('Ask the paper collection')
    elif paper_id:
        st.header(f"Ask Paper '{titles.get(paper_id) or paper_id}'")
    else:
        st.header('Select a paper to ask a question')
    st.caption('Each question runs an independent search. Previous messages are not sent to the model.')
    record = None
    submission = None
    disabled = not health or bool(st.session_state.connection_error) or pending
    if mode == 'Demo record':
        st.info('Prepared evidence mode: generates a fresh answer from a saved input; retrieval and agent are not rerun.')
        path = os.getenv('P5_RECORDS_PATH')
        try:
            records = load_records(path) if path else []
        except ValueError as exc:
            st.error(str(exc))
            records = []
        if records:
            index = st.selectbox('Exported record', range(len(records)), disabled=pending, format_func=lambda i: record_label(records[i], i),
                                 help='Send the selected prepared input unchanged. No fresh retrieval is performed.')
            record = records[index]
            submission = {'record_index': index, 'record_label': record_label(record, index),
                          'paper_id': record.get('paper_id'), 'question': record.get('question')}
        else:
            st.info('Prepared records unavailable. Set P5_RECORDS_PATH or use Free question mode.')
            disabled = True
    else:
        available = health.get('retrieval') and (scope == 'All papers' or paper_id is not None)
        question = st.text_area('Your question', key='question_draft', disabled=disabled or not available,
                                placeholder='Ask about methods, results, or comparisons across papers…',
                                help='Ask one complete question. Previous messages are not included in the request.')
        disabled = disabled or not available or not question.strip()
        submission = {'question': question.strip(), 'paper_id': paper_id}
        if not health.get('retrieval'):
            st.info('Free input is disabled because this service has no retrieval. Use Demo record in Advanced settings.')
    # Contexts are internal storage only; scope applies directly to each new submission.
    context_paper = paper_id if mode == 'Free question' else None
    cid = next((c['id'] for c in state['conversations'].values()
                if c['mode'] == mode and c['paper_id'] == context_paper), None)
    previous = list(state['conversations'][cid]['runs'].values()) if cid else []
    if len(previous) >= 50 or (cid is None and len(state['conversations']) >= 10):
        st.info('Session limit reached. Export useful runs, then Clear history in Advanced settings.')
        disabled = True
    retry_of = None
    if submission and previous and previous[-1]['submission'] == submission:
        if st.checkbox('Manual retry of the last matching question (new execution)',
                       disabled=pending, help='Link another execution of this question. A timeout does not cancel the earlier request; no automatic retry occurs.'):
            retry_of = previous[-1]['client_run_id']
    st.button('Ask question', type='primary', disabled=disabled,
              on_click=queue_request, args=(state, cid, mode, context_paper, submission, health, record, retry_of),
              help='Run one question or prepared record. Wait for the validated answer; a timeout does not cancel inference.')
    if mode == 'Free question':
        render_question_library(samples, titles, paper_id, scope == 'All papers', pending)
    else:
        with st.expander('Browse all examples'):
            st.info('Use Exported record above to select a prepared evidence example. '
                    'Switch Input mode to Free question to browse editable query examples.')
    if 'queued_request' in st.session_state:
        owner, rid, input_record = st.session_state.pop('queued_request')
        run = state['conversations'][owner]['runs'][rid]
        with st.spinner('Searching and checking evidence. This may take several minutes; the response is not streamed.'):
            submit_request(client, state, owner, run, run['capabilities'], input_record)
        st.session_state.next_history_run = rid
        st.rerun()
    selected_run = st.session_state.get('history_run')
    if selected_run in runs:
        render_answer(runs[selected_run], titles)
    else:
        st.info('Ask a question to see its answer here, or open a previous result from History.')


if __name__ == '__main__':
    main()
