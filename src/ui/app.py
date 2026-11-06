"""PaperRAG: a question-first UI over the P5 HTTP boundary."""
from concurrent.futures import ThreadPoolExecutor, wait as wait_for
import html
import os
import json
import threading
from pathlib import Path
from time import monotonic, perf_counter
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
from src.ui.api_client import ApiConfig, ApiError, P5ApiClient
from src.ui.view_models import (add_sentence_context, clipped_passage, parse_answer_record, classify_answer, citation_ids, build_evidence_cards,
                                highlighted_answer, paper_url, plain_message, progress_steps, source_ranks, stop_summary, safe_markdown, violation_title)
from src.ui.record_loader import load_records, record_label
from src.ui.conversation_state import new_session, create_conversation, begin_run, finish_run, attach_evidence, clear_conversation, export_runs

st.set_page_config(page_title='PaperRAG', page_icon=':material/description:', layout='wide')

HEALTH_POLL_SECONDS = 15
CORPUS_SAMPLE_QUESTIONS = [
    'What methods are used for low-resource language identification?',
    'How do studies combine character-level and word-level representations?',
    'What approaches improve cross-lingual transfer for low-resource languages?',
]
HOW_IT_WORKS = [
    ('1 · Search', 'Finds the most relevant passages across the collection or in one paper.'),
    ('2 · Check', 'A critic decides if the evidence is enough. A validator flags unsupported claims.'),
    ('3 · Answer', 'You get a cited answer. Open any source to read the passage it came from.'),
]
REFUSALS = {
    'Model refusal': 'No answer — the retrieved passages did not contain enough to answer this question.',
    'Refusal: no retrieved evidence': 'No answer — no matching passages were found, so the model was not asked.',
    'Refusal: agent found insufficient evidence': 'No answer — the evidence check found the passages cannot answer this question.',
}
STYLE = """<style>
:root {--system-font: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif;}
/* Spans are left out so Material icon glyphs keep their own font. */
[data-testid="stApp"], h1, h2, h3, p, li, label, button, textarea, input, .question, [data-testid="stMarkdownContainer"] {
  font-family: var(--system-font) !important;
}
/* Fresh pastel backdrop: teal lower left, rose lower right, cream upper right. */
[data-testid="stApp"] {
  background:
    radial-gradient(60% 70% at 8% 88%, rgba(120, 190, 205, .75), transparent 70%),
    radial-gradient(50% 60% at 88% 78%, rgba(240, 170, 190, .6), transparent 70%),
    radial-gradient(55% 55% at 92% 8%, rgba(250, 228, 190, .8), transparent 70%),
    radial-gradient(60% 60% at 18% 8%, rgba(208, 232, 232, .9), transparent 70%),
    #EEF3F4;
  background-attachment: fixed;
}
[data-testid="stHeader"] {background: transparent;}
/* Frosted glass: translucent fill, bright rim, soft shadow. */
[data-testid="stSidebar"], [class*="st-key-glass"], .status, .chip, [data-testid="stAlert"] > div,
[data-testid="stExpander"] details, [data-testid="stPopoverBody"], [data-baseweb="popover"] > div {
  background: rgba(255, 255, 255, .42) !important;
  -webkit-backdrop-filter: blur(18px) saturate(150%);
  backdrop-filter: blur(18px) saturate(150%);
  border: 1px solid rgba(255, 255, 255, .75) !important;
  box-shadow: 0 8px 28px rgba(45, 90, 110, .12), inset 0 1px 0 rgba(255, 255, 255, .85);
}
[class*="st-key-glass"] {border-radius: 20px !important;}
[data-testid="stSidebar"] {border-width: 0 1px 0 0 !important;}
[data-testid="stSidebar"] > div {background: transparent;}
.stButton button, .stDownloadButton button, [data-testid="stPopover"] button, [data-testid="stFormSubmitButton"] button {
  border-radius: 14px; border: 1px solid rgba(255, 255, 255, .8); background: rgba(255, 255, 255, .5);
  box-shadow: 0 3px 10px rgba(45, 90, 110, .1), inset 0 1px 0 rgba(255, 255, 255, .9);
}
.stButton button[kind*="tertiary"] {border-color: transparent; background: transparent; box-shadow: none;}
button[kind*="primary"] {
  background: linear-gradient(180deg, rgba(56, 160, 182, .92), rgba(11, 92, 107, .95)) !important;
  border-color: rgba(255, 255, 255, .55) !important; color: #fff !important;
}
[data-testid="stTextArea"] textarea, [data-baseweb="textarea"], [data-baseweb="select"] > div {
  background: rgba(255, 255, 255, .5) !important; border-radius: 14px;
}
.block-container {max-width: 860px; padding-top: 2.5rem;}
/* Pull the title up beside the sidebar's collapse button, which stays clickable above it. */
[data-testid="stSidebarHeader"] {position: relative; z-index: 2;}
[data-testid="stSidebarUserContent"] {margin-top: -60px;}
[data-testid="stSidebar"] h1 {font-size: 1.5rem; padding: 0; margin-bottom: 1rem;}
.eyebrow {font-size: .72rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: #4F5E6B; margin: .5rem 0 .1rem;}
.status {border-radius: 14px; padding: .55rem .75rem; font-size: .9rem; font-weight: 600;}
.status small {display: block; font-weight: 400; font-family: monospace; color: #6B7080; overflow-wrap: anywhere;}
.status i {display: inline-block; width: .55rem; height: .55rem; border-radius: 50%; margin-right: .45rem;}
.status.up i {background: #2E7D4F;} .status.down i {background: #B3412F;}
.chip {display: inline-block; border-radius: 999px; padding: .1rem .65rem; margin: 0 .35rem .35rem 0; font-size: .8rem; color: #3D4654;}
.question {font-size: 1.7rem; font-weight: 600; line-height: 1.25; overflow-wrap: anywhere;}
.st-key-glass_answer p, .st-key-glass_answer li {font-size: 1.05rem; line-height: 1.65;}

.st-key-glass_answer [data-testid="stCaptionContainer"] p, .st-key-glass_answer button p {font-size: .82rem; line-height: 1.4;}
mark.flag {background: #FBEFCF; border-bottom: 2px solid #D9A93A; padding: 0 .1rem; color: inherit;}
.passage {white-space: pre-wrap; font-size: .92rem; line-height: 1.55; overflow-wrap: anywhere;}
[class*="st-key-glass_step"] {min-height: 10.5rem;}
.stepper {list-style: none; margin: .4rem 0 .6rem; padding: 0;}
.step {position: relative; display: flex; gap: .8rem; padding-bottom: 1.05rem;}
.step:last-child {padding-bottom: 0;}
.step:not(:last-child)::before {content: ''; position: absolute; left: .62rem; top: 1.5rem; bottom: -.1rem; width: 2px; background: #C9D5DA;}
.step.done:not(:last-child)::before {background: #0B5C6B;}
.step i {flex: none; box-sizing: border-box; width: 1.3rem; height: 1.3rem; border-radius: 50%; border: 2px solid #C9D5DA; background: rgba(255, 255, 255, .7);}
.step.done i {background: #0B5C6B; border-color: #0B5C6B; box-shadow: inset 0 0 0 .3rem #0B5C6B, inset 0 0 0 .45rem #fff;}
.step.active i {border-color: rgba(11, 92, 107, .2); border-top-color: #0B5C6B; animation: step-spin .9s linear infinite;}
.step b {display: block; font-size: .95rem; line-height: 1.3rem;}
.step small {display: block; color: #5A6675; font-size: .8rem; line-height: 1.35; overflow-wrap: anywhere;}
.step.pending b {color: #9AA5B1; font-weight: 500;}
@keyframes step-spin {to {transform: rotate(360deg);}}
@media (prefers-reduced-motion: reduce) {.step.active i {animation: none; border-color: #0B5C6B;}}
.context {color: #8A93A0;}
.mono {font-family: monospace; font-size: .75rem; color: #6B7080; overflow-wrap: anywhere;}
</style>"""


def eyebrow(text):
    st.markdown(f'<p class="eyebrow">{html.escape(text)}</p>', unsafe_allow_html=True)


def chips(values):
    st.markdown(''.join(f'<span class="chip">{html.escape(str(v))}</span>' for v in values), unsafe_allow_html=True)


def refresh(client):
    """Keep the last known capabilities on failure, so the page does not change shape while offline."""
    st.session_state.setdefault('health', {})
    st.session_state.setdefault('papers', [])
    st.session_state.connection_error = None
    st.session_state.health_checked_at = monotonic()
    try:
        st.session_state.health = client.health()
        st.session_state.papers = client.papers() if st.session_state.health['retrieval'] else []
    except ApiError as exc:
        st.session_state.connection_error = str(exc)


def poll_health(client):
    """Notice a service that died or came back, without waiting for a manual refresh."""
    if (st.session_state.workspace_state['pending_client_run_id']
            or monotonic() - st.session_state.health_checked_at < HEALTH_POLL_SECONDS - 1):
        return
    st.session_state.health_checked_at = monotonic()
    was_down = bool(st.session_state.connection_error)
    try:
        client.health()
    except ApiError as exc:
        if not was_down:
            st.session_state.connection_error = str(exc)
            st.rerun()
        return
    if was_down:
        refresh(client)
        st.rerun()


@st.fragment(run_every=HEALTH_POLL_SECONDS)
def render_status(client):
    poll_health(client)
    health, error = st.session_state.health, st.session_state.connection_error
    detail = error or f"{health.get('backend', 'unknown')} · {health.get('model_id', 'model not reported')}"
    state, label = ('down', 'Service unavailable') if error else ('up', 'Service connected')
    st.markdown(f'<div class="status {state}"><i></i>{label}<small>{html.escape(str(detail))}</small></div>',
                unsafe_allow_html=True)
    if st.button('Refresh service', icon=':material/refresh:', type='tertiary',
                 disabled=bool(st.session_state.workspace_state['pending_client_run_id']),
                 help='Check API availability and reload capabilities and papers. Does not submit a question or reload configuration.'):
        refresh(client)
        st.rerun()


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
        finish_run(state, cid, rid, 'failed', error='The service returned an answer in an unexpected format.', elapsed=(perf_counter() - start) * 1000)
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
            neighbours = [row[key] for row in cards.values() if row
                          for key in ('previous_passage_id', 'next_passage_id') if row.get(key)]
            if neighbours:
                add_sentence_context(cards, client.passages(neighbours).get('passages', {}))
            attach_evidence(state, cid, rid, cards, (perf_counter() - start) * 1000)
        except ApiError as exc:
            attach_evidence(state, cid, rid, cards, (perf_counter() - start) * 1000, str(exc))
    else:
        attach_evidence(state, cid, rid, cards)


def clock(seconds):
    return f'{int(seconds) // 60}:{int(seconds) % 60:02d}'


def progress_text(events):
    return '\n'.join(f"{clock(row['elapsed_s'])}  {row['message']}" for row in events)


def stepper_html(events):
    rows = ''.join(f'<li class="step {state}"><i></i><div><b>{html.escape(label)}</b>'
                   f'<small>{html.escape(detail)}</small></div></li>'
                   for label, state, detail in progress_steps(events))
    return f'<ol class="stepper">{rows}</ol>'


def render_candidates(run):
    """Per-search candidates recorded live: ranks, fusion score and whether each was kept."""
    searches = [row['details'] for row in run.get('progress_log') or [] if row.get('details')]
    for number, rows in enumerate(searches, 1):
        kept = sum(row['kept'] for row in rows)
        with st.expander(f'Search {number} candidates · {kept} kept of {len(rows)}'):
            st.dataframe([{
                'Kept': row['kept'], 'Paper': row.get('title') or row.get('paper_id'),
                'Section': row.get('section'), 'BM25 rank': row.get('bm25_rank'),
                'Dense rank': row.get('dense_rank'), 'RRF score': row.get('rrf_score'),
            } for row in rows], hide_index=True)


def wait_for_answer(client, state, owner, run, record, runs):
    """Run the blocking request on a worker so the page can show a live timer."""
    times = [r['answer_http_elapsed_ms'] / 1000 for r in runs.values()
             if r['outcome'] == 'completed' and r['answer_http_elapsed_ms'] is not None]
    context = get_script_run_ctx()

    def work():
        add_script_run_ctx(threading.current_thread(), context)
        submit_request(client, state, owner, run, run['capabilities'], record)

    poller = P5ApiClient(client.config)  # requests sessions are not shared across threads.
    events = []
    def show(snapshot):
        nonlocal events
        if isinstance(snapshot, dict) and snapshot.get('events') and snapshot['events'] != events:
            events = snapshot['events']
            stepper.markdown(stepper_html(events), unsafe_allow_html=True)
            log.code(progress_text(events), language=None, wrap_lines=True)

    with st.container(border=True, key='glass_wait'):
        eyebrow('Waiting for the final answer')
        timer = st.empty()
        stepper = st.empty()
        stepper.markdown(stepper_html([]), unsafe_allow_html=True)
        with st.expander('Live log'):
            log = st.empty()
        st.caption('Please keep this page open. This can take several minutes.')
        start = monotonic()
        with ThreadPoolExecutor(max_workers=1) as pool:
            task = pool.submit(work)
            while not wait_for([task], timeout=1).done:
                expected = f' · last answer took {clock(times[-1])}' if times else ''
                timer.markdown(f'**{clock(monotonic() - start)}** elapsed{expected}')
                try:
                    snapshot = poller.progress()
                except ApiError:  # An older server has no live log; the timer still runs.
                    continue
                if isinstance(snapshot, dict) and snapshot.get('active'):
                    show(snapshot)
            task.result()
        if run['outcome'] == 'completed':  # Pick up the closing steps for the saved log.
            try:
                show(poller.progress())
            except ApiError:
                pass
    run['progress_log'] = events


def find_context(state, mode, paper_id):
    return next((c['id'] for c in state['conversations'].values()
                 if c['mode'] == mode and c['paper_id'] == paper_id), None)


def queue_request(state, cid, mode, paper_id, submission, health, record, retry_of):
    """Capture the run in the button callback, before controls render as disabled."""
    if state['pending_client_run_id']:
        return
    if cid is None:
        cid = create_conversation(state, mode, paper_id)
    state['active_conversation_id'] = cid
    run = begin_run(state, cid, submission, health, retry_of)
    st.session_state.queued_request = (cid, run['client_run_id'], record)
    st.session_state.history_run = run['client_run_id']


def submit_question(state, mode, paper_id, health):
    """Form callback: read the committed draft here, because callback args predate the submit."""
    question = st.session_state.get('question_draft', '').strip()
    if not question:
        st.session_state.composer_notice = 'Type a question first.'
        return
    st.session_state.question_draft = ''  # The composer is for the next question.
    submission = {'question': question, 'paper_id': paper_id}
    queue_request(state, find_context(state, mode, paper_id), mode, paper_id, submission, health, None, None)


def rerun(state, run, health):
    context = state['conversations'][run['conversation_id']]
    queue_request(state, context['id'], context['mode'], context['paper_id'], run['submission'],
                  health, None, run['client_run_id'])


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
    search = record.get('search') or {}
    if search:
        st.caption('Search scope: ' + ('All indexed papers' if search.get('scope') == 'corpus' else 'One paper'))
        if search.get('source_papers'):
            st.caption('Retrieved papers before final prompt selection: ' + safe_markdown('; '.join(paper_label(pid, titles or {}) for pid in search['source_papers'])))
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
    st.caption('Candidate tables appear for free questions on servers with live progress. Reranker scores are not recorded.')


def render_usage_help():
    with st.popover('How to use', icon=':material/info:', help='Learn how to ask questions, use examples and review evidence.'):
        st.markdown(
            '**Ask a question**\n\n'
            '1. Keep **All papers**, or select **One paper** to limit retrieval.\n'
            '2. Type into **Your question**, or pick one from **Examples**.\n'
            '3. Click **Ask question**, or press Ctrl+Enter (⌘+Enter on Mac).\n\n'
            '**Read the result**\n\n'
            'The answer appears at the top of the page. Review any warning; highlighted '
            'sentences were flagged. Use the **Sources**, **Flagged**, **Pipeline** and '
            '**Debug** tabs for detail. A warning does not certify that an answer is correct.\n\n'
            '**History and advanced tools**\n\n'
            '**Recent questions** in the sidebar reopens one previous result. '
            '**New question** clears the draft and result view. '
            '**Advanced settings** contains prepared-record mode, exports and history cleanup.\n\n'
            'Questions are independent: history is not sent to the model. '
            'Wait for completion before asking again. Export useful runs before closing '
            'or refreshing the page; history is session-only.'
        )


def render_banner(record, highlighted):
    """Explain the actual validation state without treating every warning as a refusal."""
    status = classify_answer(record)
    issues = len(record['validation']['violations'])
    if status == 'Answer with warnings':
        st.warning(f"**Evidence needs review.** Validation raised {issues} issue{'s' if issues != 1 else ''}. "
                   + ('Flagged sentences are highlighted in the answer; ' if highlighted else
                      'These concern the answer as a whole, not one sentence, so nothing is highlighted. ')
                   + 'see the **Flagged** tab before relying on it.',
                   icon=':material/warning:')
    elif status == 'Validator blocked answer':
        st.warning('**Validator blocked answer.** The response below is a refusal. '
                   'The rejected draft is in the **Flagged** tab.', icon=':material/block:')
    elif status == 'Inconsistent response':
        st.error('**Inconsistent response.** Evidence status and validation disagree. '
                 'Treat this result as unverified and inspect the **Debug** tab.')
    elif status in REFUSALS:
        st.info(REFUSALS[status], icon=':material/info:')


def render_flagged(record):
    validation = record['validation']
    if validation.get('downgrade_reason'):
        st.caption('Validator reason: ' + safe_markdown(plain_message({'message': validation['downgrade_reason']})))
    for number, violation in enumerate(validation['violations']):
        with st.container(border=True, key=f'glass_flag_{number}'):
            chips([violation.get('code') or 'Validation issue',
                   'Severity · ' + str(violation.get('severity') or 'not supplied').lower()])
            st.markdown('**' + safe_markdown(violation_title(violation)) + '**')
            st.write(safe_markdown(plain_message(violation)))
            if violation.get('subject'):
                st.caption('Subject: ' + safe_markdown(violation['subject']))
    if validation['downgraded']:
        with st.expander('Rejected model answer — not the accepted answer'):
            raw = validation.get('raw_result')
            st.text(raw.get('answer', 'Unavailable') if isinstance(raw, dict) else 'Unavailable')


def render_sources(run, titles):
    if run.get('evidence_error'):
        st.info('Citation lookup unavailable; answer retained. ' + run['evidence_error'])
    if not run['evidence']:
        st.info('No passages were cited for this response.')
    ranks = source_ranks(run.get('progress_log'))
    if ranks:
        st.caption('Ordered by search round, then by rank within that search (RRF score). '
                   'Cited passages only; every candidate is in the Pipeline tab.')
    ordered = sorted(run['evidence'].items(), key=lambda item: ranks[item[0]][:2] if item[0] in ranks else (99, 0))
    for number, (pid, row) in enumerate(ordered, 1):
        with st.container(border=True, key=f'glass_source_{number}'):
            source = (titles.get(row.get('paper_id')) or row.get('title')) if row else None
            st.markdown(f"**[{number}] {safe_markdown(source or 'Source paper unavailable')}**")
            if pid in ranks:
                search, rank, info = ranks[pid]
                chips([f'Search {search} · rank {rank}', f"RRF {info.get('rrf_score')}",
                       f"BM25 #{info.get('bm25_rank') or '–'}", f"Dense #{info.get('dense_rank') or '–'}"])
            if row:
                st.caption('Section: ' + safe_markdown(row.get('section') or 'Not supplied'))
                before, after = row.get('context_before', ''), row.get('context_after', '')
                shown = clipped_passage(f"{'A ' if before else ''}{row['text']}{' .' if after else ''}")
                shown = shown[2 if before else 0:len(shown) - (2 if after else 0)]
                context = '<span class="context">{}</span>'
                st.markdown('<div class="passage">' + (context.format(html.escape(before + ' ')) if before else '')
                            + html.escape(shown) + (context.format(html.escape(' ' + after)) if after else '')
                            + '</div>', unsafe_allow_html=True)
                link = paper_url(row.get('paper_id'))
                if link:
                    st.markdown(f'[Open the paper on arXiv ↗]({link})')
                if before or after:
                    st.caption('Grey text completes a sentence from the neighbouring passage.')
            else:
                st.info('Passage text unavailable')
            ids = f"Passage {pid}" + (f" · Paper {row['paper_id']}" if row and row.get('paper_id') else '')
            st.markdown(f'<div class="mono">{html.escape(ids)}</div>', unsafe_allow_html=True)


def render_debug(run, record):
    if run.get('progress_log'):
        st.code(progress_text(run['progress_log']), language=None, wrap_lines=True)
    st.caption(f"Client run: {run['client_run_id']} · Outcome: {run['outcome']}")
    elapsed = run['answer_http_elapsed_ms']
    if elapsed is not None:
        st.caption(f'Answer HTTP: {elapsed:.0f} ms (includes waiting; not isolated inference time)')
    if record:
        st.caption(f"Request ID: {record['request_id']} · Retrieval rounds: {record['result']['retrieval_rounds']}")
        st.json({k: record[k] for k in ('validation', 'generation', 'agent', 'search') if k in record})
        st.json(record['result']['provenance'])


def run_scope(submission, titles):
    if 'record_index' in submission:
        return 'Prepared evidence'
    paper_id = submission.get('paper_id')
    return (titles.get(paper_id) or paper_id) if paper_id else 'All papers'


def render_question(run, titles):
    submission = run['submission']
    eyebrow('Your question')
    text = submission.get('question') or submission.get('record_label', 'Exported state')
    st.markdown(f'<div class="question">{html.escape(text)}</div>', unsafe_allow_html=True)


def render_answer(run, titles, state, health, ready):
    submission = run['submission']
    record = run['answer_record']
    render_question(run, titles)
    values = [run_scope(submission, titles)]
    if record:
        rounds = record['result']['retrieval_rounds']
        retrieved = {pid for row in (record.get('agent') or {}).get('retrieval_log') or []
                     for pid in row.get('passage_ids') or []}
        values.append(f"{rounds} retrieval round{'s' if rounds != 1 else ''}")
        values.append((f'{len(retrieved)} passages retrieved · ' if retrieved else '') + f"{len(run['evidence'])} cited")
        values += stop_summary(run.get('progress_log'), rounds)
    chips(values)
    if 'record_index' not in submission:
        context = state['conversations'][run['conversation_id']]
        st.button('Re-run this question', icon=':material/replay:', type='tertiary', key='rerun_' + run['client_run_id'],
                  disabled=not ready or len(context['runs']) >= 50, on_click=rerun, args=(state, run, health),
                  help='Link another execution of this question. A timeout does not cancel the earlier request; no automatic retry occurs.')
    if run['error']:
        st.error(run['error'])
        st.info('This attempt has no accepted answer. Previous results remain available in Recent questions.')
    if not record:
        with st.tabs(['Debug'])[0]:
            render_debug(run, record)
        return
    validation = record['validation']
    answer_text, highlighted = highlighted_answer(record['result']['answer'], validation['violations'])
    render_banner(record, highlighted)
    with st.container(border=True, key='glass_answer'):
        eyebrow('Answer')
        # Only result.answer is accepted; raw_result is always shown separately as rejected.
        st.markdown(answer_text, unsafe_allow_html=True)
        note, copy, download = st.columns([3, 1.3, 1.7], vertical_alignment='center')
        note.caption("Checks flag risks. They don't certify accuracy. Read the cited passages.")
        with copy.popover('Copy', icon=':material/content_copy:', help='Show the answer text with a copy icon.'):
            st.code(record['result']['answer'], language=None, wrap_lines=True)
        download.download_button('Run JSON', export_runs(state, [run['client_run_id']]), 'paperrag-run.json',
                                 'application/json', icon=':material/download:', key='dl_' + run['client_run_id'],
                                 help='Save this answer, its citations, validation and timings.')
    flagged = len(validation['violations'])
    labels = [f"Sources · {len(run['evidence'])}"]
    if flagged or validation['downgraded']:
        labels.append(f'Flagged · {flagged}')
    labels += ['Pipeline', 'Debug']
    tabs = iter(st.tabs(labels))
    with next(tabs):
        render_sources(run, titles)
    if len(labels) == 4:
        with next(tabs):
            render_flagged(record)
    with next(tabs):
        render_candidates(run)
        render_pipeline_trace(record, submission, titles)
    with next(tabs):
        render_debug(run, record)


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


def open_run(rid):
    st.session_state.history_run = rid


def keep_scope():
    """A segmented control can be deselected; scope must always have a value."""
    if st.session_state.scope_choice is None:
        st.session_state.scope_choice = st.session_state.get('last_scope', 'All papers')
    st.session_state.last_scope = st.session_state.scope_choice


def clear_history(state):
    for cid in list(state['conversations']):
        clear_conversation(state, cid, remove=True)
    new_question()
    st.session_state.export_selection = []


def render_question_library(samples, titles, paper_id, corpus_scope, disabled):
    """One example library for both corpus and paper-filtered questions."""
    matching = [row for row in samples if corpus_scope or row['paper_id'] == paper_id]
    st.caption('Sample questions to get you started. Pick one, then edit it before asking.')
    if not matching and not corpus_scope:
        st.info('No prepared examples are available for this paper. Type your own question.')
        return
    groups = (['Across all papers'] if corpus_scope else []) + (['About a specific paper'] if matching else [])
    group = groups[0]
    if len(groups) > 1:
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
        st.write(safe_markdown(title or 'Paper title unavailable'))
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
                       'paperrag-sample-questions.json', 'application/json',
                       help='Save the example questions with their paper IDs and titles. No inference is run.')


def render_hero(mode, scope, paper_id, titles):
    if mode == 'Demo record':
        st.header('Generate from prepared evidence')
        st.caption('Generates a fresh answer from a saved input. Retrieval and the agent are not rerun.')
    else:
        if scope == 'All papers':
            st.header('Ask the paper collection')
        elif paper_id:
            st.header(f"Ask Paper '{titles.get(paper_id) or paper_id}'")
        else:
            st.header('Select a paper to ask a question')
        st.caption('Answers come from indexed passages, with sources you can check. '
                   "Each question is searched on its own; earlier messages aren't sent to the model.")


def render_composer(state, mode, scope, paper_id, samples, titles, health, pending, ready):
    """One card for input and submission. Returns nothing: submission happens in callbacks."""
    context_paper = paper_id if mode == 'Free question' else None
    cid = find_context(state, mode, context_paper)
    previous = list(state['conversations'][cid]['runs'].values()) if cid else []
    limited = len(previous) >= 50 or (cid is None and len(state['conversations']) >= 10)
    if limited:
        st.info('Session limit reached. Export useful runs, then Clear history in Advanced settings.')
    with st.container(border=True, key='glass_composer'):
        label, examples = st.columns([3, 1], vertical_alignment='center')
        with label:
            eyebrow('Your question' if not previous else 'Ask another question')
        with examples.popover('Examples', icon=':material/list:', disabled=pending, use_container_width=True):
            if mode == 'Free question':
                render_question_library(samples, titles, paper_id, scope == 'All papers', pending)
            else:
                st.info('Use Exported record to select a prepared evidence example. '
                        'Switch Input mode to Free question to browse editable query examples.')
        retry_help = 'Link another execution of this question. A timeout does not cancel the earlier request; no automatic retry occurs.'
        ask_help = 'Run one question or prepared record. Wait for the validated answer; a timeout does not cancel inference.'
        if mode == 'Demo record':
            path = os.getenv('P5_RECORDS_PATH')
            try:
                records = load_records(path) if path else []
            except ValueError as exc:
                st.error(str(exc))
                records = []
            if not records:
                st.info('Prepared records unavailable. Set P5_RECORDS_PATH or use Free question mode.')
                st.button('Ask question', type='primary', disabled=True, help=ask_help)
                return
            index = st.selectbox('Exported record', range(len(records)), disabled=pending, format_func=lambda i: record_label(records[i], i),
                                 help='Send the selected prepared input unchanged. No fresh retrieval is performed.')
            record = records[index]
            submission = {'record_index': index, 'record_label': record_label(record, index),
                          'paper_id': record.get('paper_id'), 'question': record.get('question')}
            retry_of = None
            if previous and previous[-1]['submission'] == submission and st.checkbox(
                    'Re-run the last matching question', disabled=pending, help=retry_help):
                retry_of = previous[-1]['client_run_id']
            st.button('Ask question', type='primary', disabled=not ready or limited, icon=':material/arrow_forward:',
                      on_click=queue_request, args=(state, cid, mode, None, submission, health, record, retry_of), help=ask_help)
            return
        available = health.get('retrieval') and (scope == 'All papers' or paper_id is not None)
        enabled = ready and available
        notice = st.session_state.pop('composer_notice', None)
        if notice:
            st.warning(notice)
        # A form commits the text and the click together, so the first click always counts.
        with st.form('composer', border=False):
            st.text_area('Your question', key='question_draft', disabled=not enabled, label_visibility='collapsed',
                         placeholder='Ask about methods, results, or comparisons across papers…',
                         help='Ask one complete question. Previous messages are not included in the request.')
            left, right = st.columns([3, 1], vertical_alignment='center')
            left.caption('Scope · ' + safe_markdown(run_scope({'paper_id': paper_id}, titles)))
            with right:
                st.form_submit_button('Ask question', type='primary', disabled=not enabled or limited, use_container_width=True,
                                      on_click=submit_question, args=(state, mode, paper_id, health), help=ask_help)
        if not health.get('retrieval'):
            st.info('Free input is disabled because this service has no retrieval. Use Demo record in Advanced settings.')


def render_recent(runs, history_ids, titles, pending):
    def text(rid):
        submission = runs[rid]['submission']
        return submission.get('question') or submission.get('record_label', 'Prepared record')
    if not history_ids:
        st.caption('Your questions from this session appear here.')
        return
    with st.container(height=min(330, 70 * len(history_ids) + 20), border=False):
        for rid in history_ids:
            run = runs[rid]
            short = text(rid) if len(text(rid)) <= 70 else text(rid)[:69].rstrip() + '…'
            selected = st.session_state.get('history_run') == rid
            st.button(safe_markdown(short), key='open_' + rid, on_click=open_run, args=(rid,), disabled=pending,
                      type='secondary' if selected else 'tertiary', use_container_width=True,
                      help=f"{run_scope(run['submission'], titles)} · {run['outcome']} · {run['submitted_at']} · {rid[:8]}. "
                           'Opens the saved answer; does not rerun inference.')


def main():
    try:
        config = ApiConfig.from_env()
        client = P5ApiClient(config)
    except ValueError as exc:
        st.error(str(exc))
        return
    st.markdown(STYLE, unsafe_allow_html=True)
    if 'workspace_state' not in st.session_state:
        st.session_state.workspace_state = new_session()
    state = st.session_state.workspace_state
    if 'health' not in st.session_state:
        refresh(client)
    samples = load_samples()
    titles = load_paper_titles()
    titles.update({p['paper_id']: p['title'] for p in st.session_state.papers if p.get('title')})
    runs = {r['client_run_id']: r for c in state['conversations'].values() for r in c['runs'].values()}
    pending = bool(state['pending_client_run_id'])
    with st.sidebar:
        st.title('PaperRAG')
        render_status(client)
        health = st.session_state.health
        papers = st.session_state.papers
        chunks = health.get('passages')
        st.caption(f'{len(papers):,} NLP papers' + (f' · {chunks:,} passages' if chunks else '') + ' indexed')
        st.button('New question', icon=':material/add:', on_click=new_question, disabled=pending, use_container_width=True,
                  help='Clear the draft and selected answer. Previous runs remain in Recent questions; the search scope stays selected.')
        eyebrow('Search scope')
        scope = 'One paper'
        if health.get('corpus_search'):
            st.session_state.setdefault('scope_choice', 'All papers')
            scope = st.segmented_control('Search scope', ['All papers', 'One paper'], key='scope_choice', on_change=keep_scope,
                                         label_visibility='collapsed', disabled=pending,
                                         help='Applies to the next question. All papers searches the indexed collection; One paper restricts retrieval.') or 'All papers'
        paper_id = None
        if scope == 'One paper':
            if not health.get('corpus_search'):
                st.caption('This service supports paper-scoped search only.')
            if papers:
                sample_ids = {row['paper_id'] for row in samples}
                ordered = sorted(papers, key=lambda p: (p['paper_id'] not in sample_ids, p['paper_id']))
                paper_id = st.selectbox('Paper title and ID', [p['paper_id'] for p in ordered], disabled=pending,
                                        format_func=lambda pid: paper_label(pid, titles),
                                        help='Restrict the next question to this paper. Titles are readable labels; IDs identify the source.')
            else:
                st.info('No papers available. Refresh service to reload the catalogue.')
        else:
            st.caption(f'Searching all {len(papers):,} papers.')
        eyebrow('Recent questions')
        history_ids = sorted(runs, key=lambda rid: runs[rid]['submitted_at'], reverse=True)
        if st.session_state.get('history_run') not in runs:
            st.session_state.history_run = None
        render_recent(runs, history_ids, titles, pending)
        def history_label(rid):
            run = runs[rid]
            text = run['submission'].get('question') or run['submission'].get('record_label', 'Prepared record')
            return f"{text} · {run['outcome']} · {run['submitted_at']} · {rid[:8]}"
        with st.expander('Advanced settings', icon=':material/tune:'):
            mode = st.radio('Input mode', ['Free question', 'Demo record'], disabled=pending,
                            help='Free question runs fresh retrieval. Demo record generates from prepared evidence without fresh retrieval.')
            st.caption(f"Retrieval: {health.get('retrieval', 'unknown')} · Passage text: {health.get('passage_text', 'unknown')} · Agent: {health.get('agent', False)}")
            st.caption('API: ' + config.base_url)
            selected = st.multiselect('Select runs to export (choose five for report)', history_ids, key='export_selection', disabled=pending,
                                      format_func=history_label, help='Choose saved attempts for the JSON report download. Full agent traces are omitted.')
            if selected:
                st.download_button('Download selected runs', export_runs(state, selected), 'paperrag-runs.json',
                                   'application/json', help='Save answers, citations, validation and HTTP timings. This does not call the model.')
            st.button('Clear history', on_click=clear_history, args=(state,), disabled=pending or not runs,
                      help='Delete all session history and drafts. Export first; this does not delete corpus files or cancel inference.')
            st.caption('History is session-only. Up to 10 search contexts and 50 attempts per context; export before clearing.')
    _, help_column = st.columns([3, 1])
    with help_column:
        render_usage_help()
    # The result area comes first, so an answer never lands below the fold. The composer
    # renders first in script order, so controls show as disabled before the request blocks.
    result = st.empty()  # Replaced on write, so an old view does not linger during a request.
    ready = bool(health) and not st.session_state.connection_error and not pending
    render_composer(state, mode, scope, paper_id, samples, titles, health, pending, ready)
    selected_run = st.session_state.get('history_run')
    with result.container():
        if 'queued_request' in st.session_state:
            owner, rid, input_record = st.session_state.pop('queued_request')
            run = state['conversations'][owner]['runs'][rid]
            render_question(run, titles)
            chips([run_scope(run['submission'], titles)])
            wait_for_answer(client, state, owner, run, input_record, runs)
            st.rerun()
        if selected_run in runs:
            render_answer(runs[selected_run], titles, state, health, ready)
        else:
            render_hero(mode, scope, paper_id, titles)
            for column, (name, text) in zip(st.columns(3), HOW_IT_WORKS):
                with column.container(border=True, key='glass_step_' + name[0]):
                    eyebrow(name)
                    st.caption(text)


if __name__ == '__main__':
    main()
