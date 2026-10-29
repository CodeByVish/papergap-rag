"""Pure display validation; preserves the P5 response without redefining it."""
from copy import deepcopy


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
