from copy import deepcopy
import pytest
from src.ui.view_models import (parse_answer_record, classify_answer, citation_ids, build_evidence_cards,
                                clipped_passage, complete_sentences, highlighted_answer, paper_url, progress_steps, source_ranks, stop_summary, plain_message, safe_markdown)


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


def test_safe_markdown_and_truncated_highlight():
    assert safe_markdown('<b>$5 :red[x]') == r'&lt;b>\$5 &#58;red[x]'.replace('>', '&gt;')
    sentence = 'word ' * 30 + 'end.'
    text, count = highlighted_answer('Fine. ' + sentence, [{'subject': sentence[:120]}])
    assert count == 1 and text.endswith('end.</mark>')
    assert highlighted_answer('Plain', [{'subject': 'p1'}]) == ('Plain', 0)
    assert 'the system' in plain_message({'message': 'so P5 refused'})


def test_clipped_passage_marks_only_mid_sentence_edges():
    assert clipped_passage('Whole sentence.') == 'Whole sentence.'
    assert clipped_passage('and so on. In addition, the') == '… and so on. In addition, the …'


def test_complete_sentences_skips_overlap_and_whole_edges():
    body = 'and the overlap region continues here for a while, then it stops'
    previous = 'First one. This sentence ' + body[:50]
    following = body[-45:] + ' at the end. Next sentence.'
    assert complete_sentences(body, previous, following) == ('This sentence ', ' at the end.')
    assert complete_sentences('Whole.', 'Earlier text.', 'Later text.') == ('', '')
    assert complete_sentences('cut off', '', '') == ('', '')


def test_progress_steps_loop_back_and_finish():
    events = [{'step': 'plan', 'active': 'search', 'message': 'Planned'},
              {'step': 'check', 'active': 'check', 'message': 'not enough'},
              {'step': 'search', 'active': 'search', 'message': 'Rewrote'}]
    assert [row[1] for row in progress_steps(events)] == ['done', 'active', 'pending', 'pending']
    assert progress_steps(events)[2][2] == 'not enough'
    assert [row[1] for row in progress_steps(events + [{'active': 'done', 'message': 'x'}])] == ['done'] * 4
    assert progress_steps([])[0][1] == 'active'


def test_paraphrased_claim_highlights_its_sentence_only_for_claim_codes():
    answer_text = 'First fact stands alone. The model improves accuracy on small datasets.'
    claim = {'code': 'PROVENANCE_OVERSTATED', 'subject': 'model improves accuracy on datasets'}
    text, count = highlighted_answer(answer_text, [claim])
    assert count == 1 and '<mark class="flag">The model improves accuracy on small datasets.</mark>' in text
    assert highlighted_answer(answer_text, [{**claim, 'code': 'UNCOVERED_QUESTION_CLAUSE'}])[1] == 0


def test_paper_url():
    assert paper_url('1909.00694') == 'https://arxiv.org/abs/1909.00694'
    assert paper_url('local-paper') is None


def test_stop_summary_and_source_ranks():
    log = [{'message': 'x', 'details': [{'passage_id': 'a', 'kept': True}, {'passage_id': 'b', 'kept': False}]},
           {'message': 'y', 'details': [{'passage_id': 'c', 'kept': True}, {'passage_id': 'a', 'kept': True}]},
           {'message': 'Stopped searching: max_rounds, budget 3 rounds.'}]
    assert stop_summary(log, 3) == ['Round 3 of 3', 'Stopped: round limit reached']
    assert stop_summary([], 1) == []
    ranks = source_ranks(log)
    assert ranks['a'][:2] == (1, 1) and ranks['c'][:2] == (2, 1) and 'b' not in ranks
