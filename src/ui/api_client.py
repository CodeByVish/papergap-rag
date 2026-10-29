"""P5 HTTP boundary. No model imports, implicit retries, or shared user state."""
from dataclasses import dataclass, field
import os
import re
from urllib.parse import urlsplit
import requests


class ApiError(Exception):
    def __init__(self, kind, message, status=None):
        super().__init__(message)
        self.kind, self.status = kind, status


@dataclass(frozen=True)
class ApiConfig:
    base_url: str = 'http://127.0.0.1:8000'
    answer_timeout: float = 120
    token: str = field(default="", repr=False)
    auth_header: str = ""
    auth_scheme: str = ""

    def __post_init__(self):
        url = urlsplit(self.base_url)
        if url.scheme not in ('http', 'https') or not url.hostname or url.username or url.password or url.query or url.fragment:
            raise ValueError('P5_API_BASE must be an HTTP(S) URL without credentials, query or fragment.')
        if not 120 <= self.answer_timeout <= 3600:
            raise ValueError('Answer timeout must be between 120 and 3600 seconds.')
        if bool(self.token) != bool(self.auth_header):
            raise ValueError('Set both P5_API_TOKEN and P5_AUTH_HEADER using values confirmed by P5.')
        if self.auth_header and (not re.fullmatch(r'[A-Za-z0-9-]+', self.auth_header) or self.auth_header.lower() not in ('authorization', 'x-api-key', 'x-auth-token', 'x-demo-token')):
            raise ValueError('Unsupported authentication header; confirm the contract with P5.')
        if any(c in (self.token + self.auth_scheme) for c in ('\r', '\n')):
            raise ValueError('Invalid authentication configuration.')
        object.__setattr__(self, 'base_url', self.base_url.rstrip('/'))

    @classmethod
    def from_env(cls):
        return cls(os.getenv('P5_API_BASE', cls.base_url), float(os.getenv('P5_ANSWER_TIMEOUT', '120')),
                   os.getenv('P5_API_TOKEN', ''), os.getenv('P5_AUTH_HEADER', ''), os.getenv('P5_AUTH_SCHEME', ''))


class P5ApiClient:
    def __init__(self, config, session=None):
        self.config = config
        self.session = session or requests.Session()

    def _request(self, method, path, body=None):
        headers = {}
        if self.config.token:
            headers[self.config.auth_header] = ' '.join(x for x in (self.config.auth_scheme, self.config.token) if x)
        try:
            response = self.session.request(method, self.config.base_url + path, json=body, headers=headers,
                                            timeout=(5, self.config.answer_timeout if path == '/answer' else 10))
        except (requests.Timeout, requests.ConnectionError):
            raise ApiError('outcome_unknown', 'Connection lost or timed out; the service may still be processing. Retry manually.') from None
        except requests.RequestException:
            raise ApiError('failed', 'HTTP request failed. Check the service configuration.') from None
        if response.status_code != 200:
            messages = {400: 'Request rejected: check the P5 contract; do not automatically retry.',
                        401: 'Authentication required. Confirm authentication configuration with P5.',
                        429: 'Service busy. Retry manually in about 20 seconds.',
                        503: 'This service capability is unavailable.'}
            raise ApiError('rejected', messages.get(response.status_code, 'Service returned an HTTP error.'), response.status_code)
        try:
            payload = response.json()
        except ValueError:
            raise ApiError('failed', 'Service returned invalid JSON.') from None
        if not isinstance(payload, dict):
            raise ApiError('failed', 'Service returned an invalid response object.')
        return payload

    def health(self):
        data = self._request('GET', '/health')
        if any(type(data.get(k)) is not bool for k in ('retrieval', 'passage_text')):
            raise ApiError('failed', 'Health response lacks boolean capability flags.')
        return data

    def papers(self):
        data = self._request('GET', '/papers').get('papers')
        if not isinstance(data, list):
            raise ApiError('failed', 'Paper catalogue must be a list.')
        normalized = []
        for paper in data:
            if isinstance(paper, str) and paper.strip():
                normalized.append({'paper_id': paper})
            elif isinstance(paper, dict) and isinstance(paper.get('paper_id'), str) and paper['paper_id'].strip():
                normalized.append(paper)
            else:
                raise ApiError('failed', 'Paper catalogue contains an invalid paper ID.')
        return normalized

    def answer_record(self, record):
        if not isinstance(record, dict) or not record:
            raise ValueError('Select a valid exported AgentState.')
        return self._request('POST', '/answer', {'record': record})

    def answer_question(self, question, paper_id):
        if not question.strip() or not paper_id:
            raise ValueError('A complete question and paper are required.')
        return self._request('POST', '/answer', {'question': question.strip(), 'paper_id': paper_id})

    def passages(self, ids):
        data = self._request('POST', '/passages', {'ids': list(dict.fromkeys(ids))})
        if not isinstance(data.get('passages'), dict) or not isinstance(data.get('missing'), list):
            raise ApiError('failed', 'Invalid passage lookup response.')
        return data
