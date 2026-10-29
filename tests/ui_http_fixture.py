"""Synthetic HTTP fixture, NOT P5's mock service. No datasets or models."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from contextlib import contextmanager
from threading import Thread


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == '/health':
            self.send_json({'retrieval': True, 'passage_text': True, 'mode': 'mock'})
        elif self.path == '/papers':
            self.send_json({'papers': [{'paper_id': 'synthetic-paper', 'title': 'Synthetic demonstration paper'}]})
        else:
            self.send_json({'detail': 'Not found'}, 404)

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        if self.path == '/passages':
            self.send_json({'passages': {'synthetic-evidence': {'text': 'Synthetic evidence for layout and HTTP testing.', 'paper_id': 'synthetic-paper', 'title': 'Synthetic demonstration paper', 'section': 'Results'}}, 'missing': []})
        elif self.path == '/answer':
            self.send_json({'request_id': 'synthetic-question', 'result': {
                'answer': 'This is a synthetic test answer, not a model result.',
                'citations': ['synthetic-evidence'], 'evidence_status': 'SUFFICIENT', 'retrieval_rounds': 1, 'provenance': []},
                'validation': {'violations': [], 'downgraded': False},
                'generation': {'backend': 'synthetic-http-fixture', 'prompt_version': 'test-only'}})
        else:
            self.send_json({'detail': 'Not found'}, 404)


@contextmanager
def serve():
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


if __name__ == '__main__':
    ThreadingHTTPServer(('127.0.0.1', 18000), Handler).serve_forever()
