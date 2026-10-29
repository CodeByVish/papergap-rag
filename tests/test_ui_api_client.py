from unittest.mock import Mock
import pytest
import requests
from src.ui.api_client import ApiConfig, ApiError, P5ApiClient


def client(payload=None, status=200):
    session = Mock()
    session.request.return_value.status_code = status
    session.request.return_value.json.return_value = payload or {}
    return P5ApiClient(ApiConfig(), session), session


def test_config_and_requests():
    assert ApiConfig('http://localhost:8000/').base_url == 'http://localhost:8000'
    for url in ('file:///tmp/a', 'https://secret@host', 'http://host?token=secret'):
        with pytest.raises(ValueError):
            ApiConfig(url)
    with pytest.raises(ValueError):
        ApiConfig(answer_timeout=10)
    api, session = client()
    api.answer_question(' query ', 'paper')
    assert session.request.call_args.kwargs['json'] == {'question': 'query', 'paper_id': 'paper'}
    assert session.request.call_args.kwargs['timeout'][1] >= 120
    api.answer_record({'question': 'q'})
    assert session.request.call_args.kwargs['json'] == {'record': {'question': 'q'}}
    with pytest.raises(ValueError):
        api.answer_question(' ', 'paper')


@pytest.mark.parametrize('status', [400, 401, 429, 503, 500])
def test_status_no_retry(status):
    api, session = client(status=status)
    with pytest.raises(ApiError) as error:
        api.answer_question('q', 'p')
    assert error.value.status == status
    session.request.assert_called_once()


@pytest.mark.parametrize('exception', [requests.Timeout('secret'), requests.ConnectionError('secret')])
def test_ambiguous_transport(exception):
    api, session = client()
    session.request.side_effect = exception
    with pytest.raises(ApiError) as error:
        api.answer_question('q', 'p')
    assert error.value.kind == 'outcome_unknown' and 'secret' not in str(error.value)
    session.request.assert_called_once()


def test_invalid_json_and_health():
    api, session = client()
    session.request.return_value.json.side_effect = ValueError('secret')
    with pytest.raises(ApiError, match='invalid JSON'):
        api.health()
    session.request.return_value.json.side_effect = None
    session.request.return_value.json.return_value = {'retrieval': 'false', 'passage_text': False}
    with pytest.raises(ApiError, match='boolean'):
        api.health()


def test_catalogue_and_passages():
    api, session = client({'papers': [{'paper_id': 'p', 'title': 'Paper'}]})
    assert api.papers()[0]['paper_id'] == 'p'
    session.request.return_value.json.return_value = {'passages': {}, 'missing': ['p']}
    api.passages(['p', 'p'])
    assert session.request.call_args.kwargs['json'] == {'ids': ['p']}


def test_explicit_auth_redaction(monkeypatch):
    monkeypatch.setenv('P5_API_TOKEN', 'private-test-token')
    with pytest.raises(ValueError, match='both'):
        ApiConfig.from_env()
    monkeypatch.setenv('P5_AUTH_HEADER', 'Authorization')
    monkeypatch.setenv('P5_AUTH_SCHEME', 'Bearer')
    config = ApiConfig.from_env()
    assert 'private-test-token' not in repr(config)
    api, session = client()
    api.config = config
    api.answer_question('q', 'p')
    assert session.request.call_args.kwargs['headers'] == {'Authorization': 'Bearer private-test-token'}


@pytest.mark.parametrize('papers,expected', [(['1706.04115'], [{'paper_id': '1706.04115'}]), ([], [])])
def test_formal_p5_string_catalogue(papers, expected):
    api, _ = client({'papers': papers})
    assert api.papers() == expected
