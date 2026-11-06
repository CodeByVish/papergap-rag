"""Pure display validation; preserves the P5 response without redefining it."""
from copy import deepcopy
import html
import re


def parse_answer_record(payload):
    if not isinstance(payload, dict) or 'request_id' not in payload:
        raise ValueError('Answer response lacks request_id.')
    result = payload.get('result', {})
    if not isinstance(result, dict) or not all(k in result for k in ('answer', 'citations', 'evidence_status', 'retrieval_rounds', 'provenance')):
        raise ValueError('Answer response lacks the five result fields.')
    if (not isinstance(result['answer'], str) or not isinstance(result['citations'], list)
            or any(not isinstance(x, str) for x in result['citations'])
            or type(result['retrieval_rounds']) is not int or result['retrieval_rounds'] < 0
            or not isinstance(result['provenance'], list)
            or result['evidence_status'] not in ('SUFFICIENT', 'INSUFFICIENT')):
        raise ValueError('Invalid answer result field types or status.')
    validation = payload.get('validation')
    if (not isinstance(validation, dict) or type(validation.get('downgraded')) is not bool
            or not isinstance(validation.get('violations'), list)
            or any(not isinstance(v, dict) for v in validation['violations'])
            or not isinstance(payload.get('generation'), dict)):
        raise ValueError('Invalid validation or generation metadata.')
    return deepcopy(payload)


def classify_answer(record):
    result, validation = record['result'], record['validation']
    violations = validation['violations']
    if result['evidence_status'] == 'SUFFICIENT':
        if validation['downgraded'] or any(str(v.get('severity', '')).upper() != 'WARNING' for v in violations):
            return 'Inconsistent response'
        return 'Answer with warnings' if violations else 'Answered'
    if validation['downgraded']:
        return 'Validator blocked answer'
    codes = {str(v.get('code')) for v in violations}
    if 'EMPTY_CONTEXT' in codes:
        return 'Refusal: no retrieved evidence'
    if 'AGENT_INSUFFICIENT' in codes:
        return 'Refusal: agent found insufficient evidence'
    return 'Model refusal'


def citation_ids(record):
    return list(dict.fromkeys(record['result']['citations']))


def build_evidence_cards(ids, payload):
    cards = {}
    for pid in ids:
        row = payload.get('passages', {}).get(pid)
        cards[pid] = row if isinstance(row, dict) and isinstance(row.get('text'), str) else None
    return cards


VIOLATION_TITLES = {
    'UNSUPPORTED_CLAIM': 'A sentence may not be backed by the cited passages',
    'CLAIM_WITHOUT_EVIDENCE': 'A claim has no linked evidence',
    'CITATION_PROVENANCE_MISMATCH': 'Citations and claim links disagree',
    'PROVENANCE_OVERSTATED': 'A claim may overstate its source',
    'PROVENANCE_DERIVED': 'Claim links were derived automatically',
    'UNSUPPORTED_NUMERIC_CLAIM': 'A number was not found in the evidence',
    'CITATION_REPAIRED_FOR_NUMBER': 'A citation was added for a number',
    'UNCOVERED_QUESTION_CLAUSE': 'Part of the question may not be answered',
    'UNCOVERED_REQUIRED_COMPONENT': 'A required part of the answer is not cited',
    'GENERATED_WITH_INSUFFICIENT_EVIDENCE': 'Answered although the evidence check had doubts',
    'EMPTY_CONTEXT': 'No passages were retrieved',
    'AGENT_INSUFFICIENT': 'The evidence check found the passages insufficient',
}


def safe_markdown(text):
    """Show untrusted text literally: no HTML, maths ($...$) or Streamlit directives."""
    escaped = html.escape(str(text), quote=False).replace('$', r'\$')
    return re.sub(r':(?=[a-zA-Z/_-]+[\[:])', '&#58;', escaped)


def violation_title(violation):
    return VIOLATION_TITLES.get(str(violation.get('code')), 'Validation note')


def plain_message(violation):
    """Service text without internal team names such as P5."""
    message = re.sub(r'\bP\d\b', 'the system', str(violation.get('message') or 'No explanation supplied by the service.'))
    return message[:1].upper() + message[1:]


PARAPHRASED_CODES = ('UNSUPPORTED_CLAIM', 'CLAIM_WITHOUT_EVIDENCE', 'PROVENANCE_OVERSTATED')


def closest_sentence(answer, claim, threshold=0.6):
    """(start, end) of the answer sentence sharing most of the claim's words, if any."""
    words = set(re.findall(r'\w+', claim.lower()))
    best, best_score = None, threshold
    for found in re.finditer(r'\S.*?(?:[.!?](?=\s|$)|$)', answer, re.DOTALL):
        score = len(words & set(re.findall(r'\w+', found.group().lower()))) / max(len(words), 1)
        if score >= best_score:
            best, best_score = found.span(), score
    return best


def flagged_spans(answer, violations):
    """Merged (start, end) spans of flagged sentences found verbatim in the answer."""
    spans = []
    for violation in violations:
        raw = str(violation.get('subject') or '')
        subject = raw.strip()
        start = answer.find(subject) if len(subject.split()) >= 3 else -1
        if start < 0:
            # Provenance claims paraphrase the answer, so locate their closest sentence.
            match = closest_sentence(answer, subject) if violation.get('code') in PARAPHRASED_CODES else None
            if match:
                spans.append(match)
            continue
        end = start + len(subject)
        if len(raw) >= 120:  # The server truncates subjects; extend to the sentence end.
            stop = re.compile(r'[.!?](\s|$)').search(answer, end)
            end = stop.start() + 1 if stop else len(answer)
        spans.append((start, end))
    merged = []
    for start, end in sorted(spans):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    return merged


def highlighted_answer(answer, violations):
    """Escaped Markdown with flagged sentences wrapped in <mark>; returns (text, count)."""
    parts, cursor = [], 0
    spans = flagged_spans(answer, violations)
    for start, end in spans:
        parts += [safe_markdown(answer[cursor:start]),
                  f'<mark class="flag">{safe_markdown(answer[start:end])}</mark>']
        cursor = end
    parts.append(safe_markdown(answer[cursor:]))
    return ''.join(parts), len(spans)


def clipped_passage(text):
    """Mark chunk edges that fall mid-sentence with an ellipsis; the text itself is unchanged."""
    body = text.strip()
    if not body:
        return text
    clipped_start = body[0].islower() or body[0] in ',;:.)]'
    clipped_end = not re.search(r'[.!?][)\]"\']*$', body)
    return ('… ' if clipped_start else '') + body + (' …' if clipped_end else '')


def complete_sentences(text, previous='', following=''):
    """Fragments from neighbouring chunks that finish this passage's clipped sentences.

    Chunks overlap, so the overlap is located first and never shown twice.
    Returns ('', '') for an edge that is whole or cannot be resolved.
    """
    body = text.strip()
    before = after = ''
    if previous and clipped_passage(body).startswith('… '):
        at = previous.find(body[:40])
        head = previous[:at] if at >= 0 else previous
        ends = list(re.finditer(r'[.!?]\s+', head))
        before = head[ends[-1].end():] if ends else ''
    if following and clipped_passage(body).endswith(' …'):
        at = following.find(body[-40:])
        tail = following[at + 40:] if at >= 0 else following
        stop = re.search(r'[.!?](\s|$)', tail)
        after = tail[:stop.start() + 1] if stop else ''
    return (before if len(before) <= 400 else ''), (after if len(after) <= 400 else '')


def add_sentence_context(cards, neighbours):
    """Attach context_before/context_after to cards, given neighbour rows by passage ID."""
    for row in cards.values():
        if row:
            previous = (neighbours.get(row.get('previous_passage_id')) or {}).get('text', '')
            following = (neighbours.get(row.get('next_passage_id')) or {}).get('text', '')
            row['context_before'], row['context_after'] = complete_sentences(row['text'], previous, following)
    return cards


PROGRESS_STEPS = (('plan', 'Plan the question'), ('search', 'Search the papers'),
                  ('check', 'Check the evidence'), ('write', 'Write the answer'))


def progress_steps(events):
    """Stepper rows (label, state, latest detail); state is done, active or pending."""
    keys = [key for key, _ in PROGRESS_STEPS]
    current = next((e['active'] for e in reversed(events) if e.get('active')), 'plan')
    position = len(keys) if current == 'done' else keys.index(current) if current in keys else 0
    latest = {e['step']: e['message'] for e in events if e.get('step')}
    return [(label, 'done' if index < position else 'active' if index == position else 'pending',
             latest.get(key, ''))
            for index, (key, label) in enumerate(PROGRESS_STEPS)]


def paper_url(paper_id):
    """arXiv page for a QASPER paper ID, or None for anything else."""
    return f'https://arxiv.org/abs/{paper_id}' if re.fullmatch(r'\d{4}\.\d{4,5}', str(paper_id)) else None


STOP_LABELS = {'sufficient': 'Stopped: evidence judged enough',
               'insufficient_information': 'Stopped: evidence check says the papers cannot answer this',
               'max_rounds': 'Stopped: round limit reached'}


def stop_summary(events, rounds):
    """Chips saying why retrieval ended, from the saved live log; [] when not recorded."""
    for event in reversed(events or []):
        found = re.match(r'Stopped searching: (\w+), budget (\d+) rounds', event.get('message', ''))
        if found:
            reason, budget = found.groups()
            return [f'Round {rounds} of {budget}', STOP_LABELS.get(reason, 'Stopped: ' + reason)]
    return []


def source_ranks(events):
    """passage_id -> (search number, rank among that search's results, row), first kept search wins."""
    ranks = {}
    searches = [event['details'] for event in events or [] if event.get('details')]
    for number, rows in enumerate(searches, 1):
        for rank, row in enumerate((r for r in rows if r.get('kept')), 1):
            ranks.setdefault(row.get('passage_id'), (number, rank, row))
    return ranks
