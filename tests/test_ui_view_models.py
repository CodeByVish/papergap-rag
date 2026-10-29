from copy import deepcopy
import pytest
from src.ui.view_models import parse_answer_record, classify_answer, citation_ids, build_evidence_cards


def answer(status='SUFFICIENT', violations=None, downgraded=False):
    return {'request_id': 'question-1', 'result': {'answer': 'Synthetic answer', 'citations': ['p1', 'p1', 'p2'], 'evidence_status': status, 'retrieval_rounds': 1, 'provenance': []},
            'validation': {'violations': violations or [], 'downgraded': downgraded, 'raw_result': {'answer': 'Rejected answer'}, 'downgrade_reason': 'Synthetic reason'}, 'generation': {'backend': 'mock', 'prompt_version': 'synthetic'}}


@pytest.mark.parametrize('status,violations,down,expected', [
    ('SUFFICIENT', [], False, 'Answered'),
    ('SUFFICIENT', [{'severity': 'WARNING'}], False, 'Answer with warnings'),
    ('INSUFFICIENT', [{'code': 'EMPTY_CONTEXT'}], False, 'Refusal: no retrieved evidence'),
    ('INSUFFICIENT', [{'code': 'AGENT_INSUFFICIENT'}], False, 'Refusal: agent found insufficient evidence'),
    ('INSUFFICIENT', [], False, 'Model refusal'),
    ('INSUFFICIENT', [{'code': 'EMPTY_CONTEXT'}], True, 'Validator blocked answer'),
    ('SUFFICIENT', [], True, 'Inconsistent response'),
    ('SUFFICIENT', [{'severity': 'ERROR'}], False, 'Inconsistent response')])
def test_classification(status, violations, down, expected):
    assert classify_answer(parse_answer_record(answer(status, violations, down))) == expected


def test_invalid_and_copy():
    payload = answer()
    parsed = parse_answer_record(payload)
    parsed['result']['answer'] = 'changed'
    assert payload['result']['answer'] != 'changed'
    for key in payload['result']:
        broken = deepcopy(payload)
        del broken['result'][key]
        with pytest.raises(ValueError):
            parse_answer_record(broken)


def test_citation_fallback():
    ids = citation_ids(answer())
    assert ids == ['p1', 'p2']
    cards = build_evidence_cards(ids, {'passages': {'p1': {'text': 'Evidence'}}, 'missing': ['p2']})
    assert cards['p1']['text'] == 'Evidence' and cards['p2'] is None
