"""Smoke-test the demo service over real sockets, without a GPU.

The unit tests drive the app through ``TestClient``, which bypasses the network.
This script starts three actual ``uvicorn`` servers on loopback - one without a
hook, one with a plain retriever, one with an agent record hook - and checks
every endpoint the P6 UI is allowed to call.
It is the check to run after touching ``src.generation/server.py`` and before a demo:

    python scripts/smoke_demo_server.py

What it covers:

* ``/health``, ``/papers``, ``/answer`` (record form), ``/passages``;
* a terminal refusal and the canonical five-key result;
* free-form input with a stub retriever, and the 503 when none is wired;
* free-form input through an agent ``record_fn`` that returns the pre-answer
  export, including the ``agent`` block and the health flag;
* the concurrency guarantee - two simultaneous questions get ``{200, 429}``,
  because the offline engine is not thread-safe and the lock must say so;
* the passage index built from a *retrieval dump*, which is the shape that
  exists on the cluster.

What it cannot cover: the vLLM backend, P2's real retriever, the scheduler and
the SSH tunnel. Those are cluster-only; see ``docs/DEMO_OPTION_C.md`` §5.

Exit codes: 0 all checks passed, 1 a check failed, 2 uvicorn is not installed.
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable, Optional

# Allow `python scripts/smoke_demo_server.py` from either checkout: the shared
# repo keeps the package at src/generation (repo root importable), the standalone
# repo at src.generation (src/ importable). Without this, Python puts scripts/ on
# sys.path and the project import fails.
for _candidate in (
    Path(__file__).resolve().parents[1],
    Path(__file__).resolve().parents[1] / "src",
):
    if str(_candidate) not in sys.path:
        sys.path.insert(0, str(_candidate))

from src.generation.generators import MockGenerator, MockScenario
from src.generation.pipeline import GroundedQAPipeline
from src.generation.server import create_app, load_passage_index, paper_ids_from

ID_A = "qasper-passage-v1-" + "a" * 64
ID_B = "qasper-passage-v1-" + "b" * 64
ID_UNKNOWN = "qasper-passage-v1-" + "0" * 64

TEXT_A = "The model sets a new state of the art on the benchmark."
TEXT_B = "The method uses a two-stage encoder."


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #


def dump_records() -> list[dict[str, Any]]:
    """Two retrieval-dump records: one answerable, one with no passages."""

    def hit(passage_id: str, text: str, rank: int) -> dict[str, Any]:
        return {
            "passage": {
                "passage_id": passage_id,
                "paper_id": "paper-A",
                "title": "Synthetic paper",
                "section": "results",
                "chunk_number": rank - 1,
                "text": text,
            },
            "rank": rank,
            "rrf_score": 1.0 / rank,
            "reranker_score": None,
        }

    return [
        {
            "question_id": "q-1",
            "question": "What result is reported?",
            "paper_id": "paper-A",
            "retrieval_round": 1,
            "retrieved_passages": [hit(ID_A, TEXT_A, 1), hit(ID_B, TEXT_B, 2)],
            "sufficient": True,
            "gap_label": "NONE",
            "required_components": ["result"],
            "evidence_map": {"result": [ID_A]},
        },
        {
            "question_id": "q-2",
            "question": "What method is used?",
            "paper_id": "paper-B",
            "retrieval_round": 1,
            "retrieved_passages": [],
        },
    ]


def write_dump(directory: Path) -> Path:
    path = directory / "retrieval.jsonl"
    path.write_text(
        "".join(json.dumps(record) + "\n" for record in dump_records()),
        encoding="utf-8",
    )
    return path


def slow_retriever(delay: float = 0.4) -> Callable[[str, str, int], list[dict[str, Any]]]:
    """A stub retriever that is slow enough to make the 429 race deterministic."""

    def retrieve(question: str, paper_id: str, top_k: int) -> list[dict[str, Any]]:
        time.sleep(delay)
        return dump_records()[0]["retrieved_passages"]

    return retrieve


def agent_record(question: str, paper_id: str) -> dict[str, Any]:
    """A stub agent hook: the first fixture record, before the answer.

    P4's factory returns ``run_system(..., answer_fn=None)[0]``; this is the
    same shape with a fixed retrieval result, enough to exercise the server path.
    """
    record = dict(dump_records()[0])
    record["question"] = question
    record["question_id"] = f"ui-{int(time.time() * 1000)}"
    return record


# --------------------------------------------------------------------------- #
# A real server on a real port
# --------------------------------------------------------------------------- #


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


class LocalServer:
    """Run ``uvicorn`` in a thread and expose its base URL as a context manager."""

    def __init__(self, app: Any) -> None:
        import uvicorn  # imported here so the module imports without the dep

        self.port = free_port()
        self._server = uvicorn.Server(
            uvicorn.Config(
                app, host="127.0.0.1", port=self.port, log_level="warning"
            )
        )
        self._thread = threading.Thread(target=self._server.run, daemon=True)

    def __enter__(self) -> str:
        self._thread.start()
        deadline = time.time() + 20
        while time.time() < deadline:
            if self._server.started:
                try:
                    status, _body = request("GET", self.base + "/health", timeout=1)
                    if status == 200:
                        return self.base
                except OSError:
                    pass
            time.sleep(0.05)
        raise RuntimeError("the server did not become ready within 20 s")

    def __exit__(self, *exc_info: object) -> None:
        self._server.should_exit = True
        self._thread.join(timeout=10)

    @property
    def base(self) -> str:
        return f"http://127.0.0.1:{self.port}"


def request(
    method: str, url: str, body: Optional[dict[str, Any]] = None, timeout: float = 30
) -> tuple[int, Any]:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        url, data=data, method=method, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, json.loads(response.read().decode("utf-8") or "null")
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode("utf-8") or "null")


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def check(self, name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
        if not ok:
            self.failures.append(name)


def run(dump: Path, report: Report) -> None:
    papers = paper_ids_from(dump)
    passages = load_passage_index(dump)
    records = dump_records()

    report.check("passage index built from a retrieval dump", len(passages) == 2,
                 f"{len(passages)} passages")
    report.check("paper ids read", papers == ["paper-A", "paper-B"], str(papers))

    # -- server 1: no retriever -------------------------------------------- #
    print("\nserver without a retriever")
    app = create_app(
        GroundedQAPipeline(MockGenerator(MockScenario.GROUNDED)),
        papers=papers,
        passages=passages,
    )
    with LocalServer(app) as base:
        status, health = request("GET", base + "/health")
        report.check("GET /health is 200", status == 200, f"status {status}")
        report.check(
            "health reports prompt version and capabilities",
            health.get("prompt_version") == "p5-grounded-qa-v7"
            and health.get("retrieval") is False
            and health.get("agent") is False
            and health.get("passage_text") is True,
            json.dumps(
                {k: health.get(k) for k in ("prompt_version", "retrieval", "agent", "passage_text")}
            ),
        )

        status, body = request("GET", base + "/papers")
        report.check("GET /papers lists the dump's papers",
                     status == 200 and body.get("papers") == papers)

        status, answer = request("POST", base + "/answer", {"record": records[0]})
        result = answer.get("result", {}) if isinstance(answer, dict) else {}
        report.check("POST /answer (record) is 200", status == 200, f"status {status}")
        report.check(
            "the answer has the frozen five keys",
            set(result) == {"answer", "citations", "evidence_status",
                            "retrieval_rounds", "provenance"},
            str(sorted(result)),
        )
        report.check("the answer is SUFFICIENT with citations",
                     result.get("evidence_status") == "SUFFICIENT" and result.get("citations"),
                     f'{result.get("evidence_status")}, {len(result.get("citations") or [])} citations')
        report.check("the agent block is carried", "agent" in answer)

        status, refused = request("POST", base + "/answer", {"record": records[1]})
        codes = [v["code"] for v in refused.get("validation", {}).get("violations", [])]
        report.check(
            "an empty context is a 200 refusal, not an error",
            status == 200 and refused["result"]["evidence_status"] == "INSUFFICIENT"
            and "EMPTY_CONTEXT" in codes,
            f"status {status}, codes {codes}",
        )

        status, _ = request("POST", base + "/answer", {"paper_id": "paper-A"})
        report.check("a malformed body is 400", status == 400, f"status {status}")

        status, lookup = request("POST", base + "/passages", {"ids": [ID_A, ID_UNKNOWN]})
        report.check(
            "POST /passages resolves text and reports missing ids",
            status == 200
            and lookup.get("passages", {}).get(ID_A, {}).get("text") == TEXT_A
            and lookup.get("missing") == [ID_UNKNOWN],
            f"found {len(lookup.get('passages', {}))}, missing {len(lookup.get('missing', []))}",
        )

        status, body = request(
            "POST", base + "/answer",
            {"question": "What result is reported?", "paper_id": "paper-A"},
        )
        report.check("free-form without a retriever is 503", status == 503, f"status {status}")

    # -- server 2: with a retriever ---------------------------------------- #
    print("\nserver with a retriever")
    app = create_app(
        GroundedQAPipeline(MockGenerator(MockScenario.GROUNDED)),
        retriever=slow_retriever(),
        papers=papers,
        passages=passages,
    )
    with LocalServer(app) as base:
        status, answer = request(
            "POST", base + "/answer",
            {"question": "What result is reported?", "paper_id": "paper-A"},
        )
        report.check("free-form with a retriever is 200", status == 200, f"status {status}")
        report.check(
            "free-form generates its own request id",
            isinstance(answer.get("request_id"), str)
            and answer["request_id"].startswith("ui-"),
            str(answer.get("request_id")),
        )

        barrier = threading.Barrier(2)
        statuses: list[int] = []

        def ask() -> None:
            barrier.wait()
            code, _ = request(
                "POST", base + "/answer",
                {"question": "What result is reported?", "paper_id": "paper-A"},
            )
            statuses.append(code)

        threads = [threading.Thread(target=ask) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=10)
        report.check(
            "two simultaneous questions get {200, 429}",
            sorted(statuses) == [200, 429],
            f"statuses {sorted(statuses)}",
        )

    # -- server 3: with an agent record hook ------------------------------- #
    print("\nserver with an agent record hook")
    app = create_app(
        GroundedQAPipeline(MockGenerator(MockScenario.GROUNDED)),
        record_fn=agent_record,
        papers=papers,
        passages=passages,
    )
    with LocalServer(app) as base:
        status, health = request("GET", base + "/health")
        report.check(
            "health reports the agent hook",
            status == 200
            and health.get("agent") is True
            and health.get("retrieval") is True,
            json.dumps({k: health.get(k) for k in ("agent", "retrieval")}),
        )

        status, answer = request(
            "POST", base + "/answer",
            {"question": "What result is reported?", "paper_id": "paper-A"},
        )
        result = answer.get("result", {}) if isinstance(answer, dict) else {}
        report.check(
            "free-form through the agent hook is 200", status == 200, f"status {status}"
        )
        report.check(
            "the agent hook answer has the five keys and the agent block",
            set(result)
            == {"answer", "citations", "evidence_status", "retrieval_rounds", "provenance"}
            and "agent" in answer,
            str(sorted(result)),
        )
        report.check(
            "the agent hook answer is SUFFICIENT with citations",
            result.get("evidence_status") == "SUFFICIENT" and result.get("citations"),
            f'{result.get("evidence_status")}, {len(result.get("citations") or [])} citations',
        )


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--keep", action="store_true", help="keep the temporary dump for inspection"
    )
    args = parser.parse_args(argv)

    try:
        import uvicorn  # noqa: F401
    except ImportError:
        print("uvicorn is not installed; run: pip install 'uvicorn>=0.29'", file=sys.stderr)
        return 2

    report = Report()
    with tempfile.TemporaryDirectory(prefix="p5-smoke-") as tmp:
        dump = write_dump(Path(tmp))
        print(f"fixture: {dump}")
        run(dump, report)
        if args.keep:
            kept = Path("runs/_smoke_retrieval.jsonl")
            kept.parent.mkdir(parents=True, exist_ok=True)
            kept.write_text(dump.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"kept fixture at {kept}")

    print()
    if report.failures:
        print(f"FAILED: {len(report.failures)} check(s): {', '.join(report.failures)}")
        return 1
    print("OK: all demo-server checks passed over real sockets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
