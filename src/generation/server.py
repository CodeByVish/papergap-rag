"""Live demo service: the Option-C answer endpoint.

The demo architecture decided on 2026-10-29 is **a FastAPI wrapper around
:func:`src.generation.harness.answer_record` on the cluster, called from the local UI
through an SSH tunnel**. This module is that wrapper and nothing else: it owns
the HTTP shape, the serialisation and the health checks, while the answer
semantics stay in the pipeline so the live demo and P6's runner produce the same
record from the same code path.

Four constraints shape the implementation, and each one is a measured property
of this cluster rather than a preference:

1. **One engine, one request at a time.** The offline vLLM ``LLM`` object is not
   thread-safe (``docs/AGENT_HANDOFF.md`` §6). FastAPI runs a ``def`` endpoint in
   a threadpool, so without a lock two concurrent clicks would drive the engine
   from two threads. A global non-blocking lock answers ``429`` instead of
   queuing: a demo that appears frozen for 30 s is worse than one that says
   "busy, retry".
2. **Warm up before opening the port.** Loading Qwen3-8B takes 1-2 minutes and
   the first generate pays the graph-capture cost. A server that listens first
   makes the demo's first click look broken, which is exactly when nobody is in
   the room to debug it.
3. **Bind to loopback.** The process runs on a shared compute node. The tunnel
   provides the network path; the server must never be reachable from the node's
   LAN.
4. **No retrieval dependency of its own.** Free-form questions need P2's
   retriever, but P5 neither owns nor imports it. A caller injects a
   ``retriever(question, paper_id, top_k) -> hits`` callable (``--retriever
   module:factory``), and its hit payloads go through the same
   :func:`~src.generation.adapters.retrieval.build_request` as an exported record. When
   no retriever is configured the server still answers full ``record`` payloads,
   which is the replay shape the UI can use before retrieval is wired.

The response body is the canonical answer record
(``request_id``, five-key ``result``, ``validation``, ``generation``, optional
``agent``) - the same object :func:`~src.generation.harness.answer_record` returns to
P4's harness. The UI must read ``["result"]``; nothing here reshapes it.

Run it::

    python -m src.generation.server --model ~/p5/models/Qwen3-8B --port 8000

Dependencies are deliberately imported lazily. ``src.generation`` must stay importable
on a CPU-only box with no FastAPI installed - the test suite is the reason.
"""

from __future__ import annotations

import argparse
import importlib
import json
import logging
import sys
import threading
import time
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, Sequence

from src.generation.generators.base import BackendNotAvailable
from src.generation.harness import answer_record
from src.generation.pipeline import GroundedQAPipeline
from src.generation.prompts.grounded_qa import PROMPT_VERSION

LOGGER = logging.getLogger("src.generation.server")

#: A retriever adapter: ``(question, paper_id, top_k) -> list of hits``.
#: Hits may be P2's nested ``{"passage": {...}}`` objects or already flat; the
#: adapter in :mod:`src.generation.adapters.retrieval` accepts both.
RetrieverFn = Callable[[str, str, int], Sequence[Mapping[str, Any]]]

#: Used when no ``--warmup-record`` is supplied. One synthetic passage is enough
#: to exercise generate -> parse -> validate; the answer is expected to be a
#: refusal and its content is never inspected.
WARMUP_RECORD: dict[str, Any] = {
    "question": "Warm-up: does this passage describe the demo server?",
    "question_id": "warmup",
    "paper_id": "warmup",
    "retrieval_round": 1,
    "retrieved_passages": [
        {
            "passage": {
                "passage_id": "qasper-passage-v1-" + "0" * 64,
                "paper_id": "warmup",
                "title": "Warm-up",
                "section": "serving",
                "chunk_number": 0,
                "text": (
                    "This passage exists only so that the demo server loads the "
                    "model and runs one generation before accepting requests."
                ),
            },
            "rank": 1,
            "rrf_score": 1.0,
            "reranker_score": None,
        }
    ],
}


class ServerDependencyMissing(RuntimeError):
    """Raised when FastAPI/uvicorn are absent, with the exact install command.

    Same policy as :class:`~src.generation.generators.base.BackendNotAvailable`: the
    message names the fix, because whoever hits this is on a compute node in a
    job that is already burning a GPU.
    """


# --------------------------------------------------------------------------- #
# Inputs: retriever and paper list
# --------------------------------------------------------------------------- #


def load_retriever(spec: str) -> RetrieverFn:
    """Resolve ``"module:factory"`` into a retriever callable.

    The factory is called once, at startup, so a slow index load happens before
    the port opens. Its return value must be callable with
    ``(question, paper_id, top_k)``; the hits it returns are passed to
    ``build_request`` unchanged.
    """
    module_name, separator, attribute = spec.partition(":")
    if not separator or not module_name or not attribute:
        raise ValueError(
            f"retriever spec {spec!r} must look like 'package.module:factory'"
        )
    factory = getattr(importlib.import_module(module_name), attribute, None)
    if factory is None:
        raise ValueError(f"{module_name} has no attribute {attribute!r}")
    retriever = factory()
    if not callable(retriever):
        raise TypeError(
            f"{spec} returned {type(retriever).__name__}, not a callable "
            "retriever(question, paper_id, top_k)"
        )
    return retriever


def paper_ids_from(path: str | Path) -> list[str]:
    """Unique ``paper_id`` values in a retrieval dump, sorted.

    The UI needs a paper selector because QASPER retrieval is paper-scoped
    (``paper_scope: question.paper_id``): "free-form" means a new question about
    a paper we already indexed, not a question about an arbitrary paper. The
    dump is the cheapest reliable source for that list - it is already on the
    cluster and it is the same set the scored runs used.
    """
    seen: set[str] = set()
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            paper_id = record.get("paper_id")
            if isinstance(paper_id, str) and paper_id:
                seen.add(paper_id)
    return sorted(seen)


def first_record(path: str | Path) -> dict[str, Any]:
    """The first JSON object in a JSONL file, for use as a warm-up record."""
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if isinstance(record, dict):
                return record
    raise ValueError(f"{path} contains no JSON object to warm up from")


#: Candidate field names for the passage-text lookup. They mirror the adapter's
#: tolerance: a P2 hit may be nested under ``passage``, and a corpus dump may use
#: ``content`` for the text.
_PASSAGE_ID_KEYS = ("passage_id", "id", "chunk_id")
_PASSAGE_TEXT_KEYS = ("text", "content", "chunk")


def _first_field(record: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        value = record.get(key)
        if value is not None:
            return value
    return None


#: Keys a line may use to carry a list of hits. The first two are the shapes
#: that actually exist on the cluster today: a retrieval dump wraps its hits in
#: ``retrieved_passages``, and a corpus dump is one passage per line.
_HIT_LIST_KEYS = ("retrieved_passages", "passages", "hits")


def _passage_records(raw: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    """Flatten one dump line into passage records.

    Three shapes are accepted, because the demo must work with whichever file
    is on the cluster: a corpus line (flat), a single P2 hit (nested under
    ``passage``), and a retrieval envelope (a question with
    ``retrieved_passages``). The envelope case is why an index built from P5's
    only current dump used to come out empty.
    """
    for key in _HIT_LIST_KEYS:
        inner = raw.get(key)
        if isinstance(inner, list):
            out: list[Mapping[str, Any]] = []
            for item in inner:
                if isinstance(item, Mapping):
                    nested = item.get("passage")
                    out.append(nested if isinstance(nested, Mapping) else item)
            return out
    nested = raw.get("passage")
    return [nested if isinstance(nested, Mapping) else raw]


def load_passage_index(path: str | Path) -> dict[str, dict[str, Any]]:
    """Map ``passage_id -> {text, paper_id, title, section}`` from a dump.

    Citations are opaque ``qasper-passage-v1-<sha256>`` ids, so a UI that shows
    them without this map can only display hashes. The map is built once at
    startup (32k passages is tens of MB, and the node has 377 GiB of RAM) rather
    than per request, because the demo must not wait on file I/O mid-question.

    Accepts a corpus ``passages.jsonl``, a single P2 hit per line, or a
    retrieval dump whose records carry ``retrieved_passages`` - see
    :func:`_passage_records`. Entries without an id or text are skipped, since
    neither can be rendered.
    """
    index: dict[str, dict[str, Any]] = {}
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(raw, Mapping):
                continue
            for record in _passage_records(raw):
                passage_id = _first_field(record, _PASSAGE_ID_KEYS)
                text = _first_field(record, _PASSAGE_TEXT_KEYS)
                if not isinstance(passage_id, str) or not isinstance(text, str):
                    continue
                index[passage_id] = {
                    "text": text,
                    "paper_id": _first_field(record, ("paper_id", "doc_id")),
                    "title": _first_field(record, ("title", "paper_title")),
                    "section": _first_field(record, ("section", "section_name")),
                }
    return index


# --------------------------------------------------------------------------- #
# Warm-up
# --------------------------------------------------------------------------- #


def warm_up(
    pipeline: GroundedQAPipeline,
    record: Optional[Mapping[str, Any]] = None,
    *,
    echo: Callable[[str], None] = print,
) -> float:
    """Run one answer through the real path and return the elapsed seconds.

    Deliberately uses :func:`answer_record`, i.e. ``answer_safe``: a warm-up that
    raises on a refusal would be useless, because a refusal is a normal outcome
    for a synthetic passage. ``BackendNotAvailable`` still propagates - a
    missing package or GPU must stop the job before the port opens, not after.
    """
    started = time.perf_counter()
    output = answer_record(pipeline, dict(record or WARMUP_RECORD))
    elapsed = time.perf_counter() - started
    status = "refusal" if output["result"]["evidence_status"] == "INSUFFICIENT" else "answered"
    echo(
        f"[warmup] {status} in {elapsed:.1f}s "
        f"(prompt {output['generation'].get('prompt_version', PROMPT_VERSION)})"
    )
    return elapsed


# --------------------------------------------------------------------------- #
# The app
# --------------------------------------------------------------------------- #


def _require_fastapi() -> Any:
    """FastAPI is needed to build the app; uvicorn only to serve it."""
    try:
        import fastapi  # noqa: F401
    except ImportError as exc:
        raise ServerDependencyMissing(
            f"The demo server needs FastAPI ({exc}).\n"
            "Install it into the vLLM venv - it is pure Python and does not "
            "touch torch or transformers:\n"
            '  "$VLLM_PY" -m pip install "fastapi>=0.110" "uvicorn>=0.29"'
        ) from exc
    return fastapi


def _require_uvicorn() -> Any:
    try:
        import uvicorn  # noqa: F401
    except ImportError as exc:
        raise ServerDependencyMissing(
            f"The demo server needs uvicorn to listen ({exc}):\n"
            '  "$VLLM_PY" -m pip install "uvicorn>=0.29"'
        ) from exc
    return uvicorn


def create_app(
    pipeline: GroundedQAPipeline,
    *,
    retriever: Optional[RetrieverFn] = None,
    papers: Sequence[str] = (),
    passages: Optional[Mapping[str, Mapping[str, Any]]] = None,
    top_k: int = 5,
    token: Optional[str] = None,
    prompt_version: str = PROMPT_VERSION,
) -> Any:
    """Build the FastAPI app around an already-loaded pipeline.

    ``pipeline`` is passed in rather than constructed here so that the caller
    owns the one engine this job is allowed to load, and so tests can build the
    app with the mock backend. Loading and warm-up are :func:`main`'s job.
    """
    fastapi = _require_fastapi()
    from fastapi import Body, Header, HTTPException

    app = fastapi.FastAPI(
        title="P5 grounded QA demo",
        version=prompt_version,
        description=(
            "Live wrapper around src.generation.harness.answer_record. One answer at a "
            "time; a refusal is a 200 with evidence_status=INSUFFICIENT."
        ),
    )

    #: Serialises retrieval + generation. Non-blocking on purpose: a queued
    #: request would hold a threadpool thread for up to ~20 s and hide the
    #: problem from the UI, while a 429 is visible and retryable.
    lock = threading.Lock()
    started_at = time.time()
    state: dict[str, Any] = {"warmup_seconds": None}

    backend_info = pipeline.generator.info()

    def _check_token(authorization: Optional[str]) -> None:
        if token is None:
            return
        expected = f"Bearer {token}"
        if authorization != expected:
            raise HTTPException(status_code=401, detail="bad or missing bearer token")

    def _parse_body(body: Mapping[str, Any]) -> dict[str, Any]:
        """Validate the request without touching the retriever or the engine.

        Kept outside the lock so a malformed payload always gets its 400 instead
        of losing a race to a 429, which would tell the caller nothing.
        """
        if "record" in body:
            if "question" in body:
                raise HTTPException(
                    status_code=400,
                    detail="send either 'record' or 'question', not both",
                )
            record = body["record"]
            if not isinstance(record, Mapping):
                raise HTTPException(
                    status_code=400, detail="'record' must be a JSON object"
                )
            return {"record": dict(record)}

        question = body.get("question")
        if not isinstance(question, str) or not question.strip():
            raise HTTPException(
                status_code=400,
                detail="'question' must be a non-empty string (or send 'record')",
            )
        paper_id = body.get("paper_id")
        if not isinstance(paper_id, str) or not paper_id.strip():
            raise HTTPException(
                status_code=400,
                detail=(
                    "'paper_id' is required for a free-form question: QASPER "
                    "retrieval is paper-scoped"
                ),
            )
        if retriever is None:
            raise HTTPException(
                status_code=503,
                detail=(
                    "free-form retrieval is not configured on this server; "
                    "restart it with --retriever module:factory, or send a full "
                    "'record' exported by the agent"
                ),
            )
        return {
            "question": question.strip(),
            "paper_id": paper_id.strip(),
            "request_id": body.get("request_id"),
        }

    def _one_at_a_time(parsed: Mapping[str, Any]) -> dict[str, Any]:
        """Run retrieval and generation under one lock.

        The lock covers the retriever too, not just the model: P2's retriever may
        hold its own GPU encoder, and "one engine per job" is a property of the
        whole request path. Validation of the body happens before this, so a bad
        payload is still a 400.
        """
        if not lock.acquire(blocking=False):
            raise HTTPException(
                status_code=429,
                detail=(
                    "the demo server answers one question at a time; "
                    "wait for the current answer (p90 ~17 s) and retry"
                ),
            )
        try:
            if "record" in parsed:
                record = dict(parsed["record"])
            else:
                hits = retriever(parsed["question"], parsed["paper_id"], top_k)
                if not isinstance(hits, Sequence) or isinstance(hits, (str, bytes)):
                    raise HTTPException(
                        status_code=500,
                        detail=(
                            "the configured retriever returned "
                            f"{type(hits).__name__}; expected a list of hits"
                        ),
                    )
                record = {
                    "question": parsed["question"],
                    "question_id": parsed["request_id"]
                    or f"ui-{int(time.time() * 1000)}",
                    "paper_id": parsed["paper_id"],
                    "retrieval_round": 1,
                    "retrieved_passages": list(hits),
                }
            return answer_record(pipeline, record)
        except (ValueError, TypeError) as exc:
            # A malformed record means the caller and P5 disagree about the
            # contract. That is a client error, and it must not look like a
            # refusal - the same distinction answer_safe makes internally.
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except BackendNotAvailable as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        finally:
            lock.release()

    @app.get("/health")
    def health() -> dict[str, Any]:
        """Liveness for the tunnel check and for the UI's status badge."""
        return {
            "status": "ok",
            "backend": backend_info.get("backend"),
            "model_id": backend_info.get("model_id"),
            "prompt_version": prompt_version,
            "retrieval": retriever is not None,
            "passage_text": bool(passages),
            "top_k": top_k,
            "papers": len(papers),
            "warmup_seconds": state["warmup_seconds"],
            "uptime_seconds": round(time.time() - started_at, 1),
        }

    @app.get("/papers")
    def paper_list() -> dict[str, Any]:
        """The paper ids the UI may ask about. Empty when ``--papers-from`` is unset."""
        return {"papers": list(papers)}

    @app.post("/passages")
    def passage_texts(
        body: dict[str, Any] = Body(...),
        authorization: Optional[str] = Header(default=None),
    ) -> dict[str, Any]:
        """Resolve cited ids to text so the UI can highlight the evidence.

        Separate from ``/answer`` on purpose: the answer record is the frozen
        contract shared with the batch files, and adding passage text to it
        would make the live record diverge from the one P6 scores. ``missing``
        is returned rather than treated as an error - a citation the corpus dump
        does not contain is worth displaying as missing, not crashing on.
        """
        _check_token(authorization)
        ids = body.get("ids")
        if not isinstance(ids, list) or not all(isinstance(i, str) for i in ids):
            raise HTTPException(
                status_code=400, detail="'ids' must be a list of passage-id strings"
            )
        if len(ids) > 500:
            raise HTTPException(
                status_code=400, detail="at most 500 ids per request"
            )
        if passages is None:
            raise HTTPException(
                status_code=503,
                detail=(
                    "passage text is not loaded on this server; start it with "
                    "--passages-from <passages.jsonl> to resolve citation ids"
                ),
            )
        found = {key: dict(passages[key]) for key in ids if key in passages}
        missing = [key for key in ids if key not in passages]
        return {"passages": found, "missing": missing}

    @app.post("/answer")
    def answer(
        body: dict[str, Any] = Body(...),
        authorization: Optional[str] = Header(default=None),
    ) -> dict[str, Any]:
        _check_token(authorization)
        parsed = _parse_body(body)
        started = time.perf_counter()
        result = _one_at_a_time(parsed)
        elapsed = time.perf_counter() - started

        status = result["result"]["evidence_status"]
        codes = ",".join(
            violation.get("code", "?")
            for violation in result.get("validation", {}).get("violations", [])
        ) or "-"
        paper = parsed.get("paper_id") or (parsed.get("record") or {}).get("paper_id")
        LOGGER.info(
            "answer request_id=%s paper=%s %.2fs %s codes=%s",
            result.get("request_id"),
            paper,
            elapsed,
            status,
            codes,
        )
        return result

    # Exposed so main() can record the warm-up time before uvicorn listens.
    app.state.demo_state = state
    return app


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.generation.server",
        description=(
            "Option-C demo service: answer_record over HTTP, bound to loopback, "
            "reached through an SSH tunnel from the laptop."
        ),
    )
    parser.add_argument("--model", default="Qwen/Qwen3-8B", help="local model path")
    parser.add_argument(
        "--backend", default="vllm", choices=("vllm", "transformers", "mock")
    )
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--gpu-memory-utilization", type=float, default=0.85)
    parser.add_argument("--max-model-len", type=int, default=32768)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument(
        "--retriever",
        default=None,
        help="'module:factory' returning retriever(question, paper_id, top_k)",
    )
    parser.add_argument(
        "--papers-from",
        default=None,
        help="retrieval dump whose paper_id values populate GET /papers",
    )
    parser.add_argument(
        "--passages-from",
        default=None,
        help="corpus passages.jsonl that backs POST /passages (citation -> text)",
    )
    parser.add_argument(
        "--warmup-record",
        default=None,
        help="JSONL file; its first record is used for the warm-up answer",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="require 'Authorization: Bearer <token>' (optional; loopback only)",
    )
    parser.add_argument("--no-warmup", action="store_true")
    parser.add_argument("--log-level", default="info")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    from src.generation.generators import get_generator

    if args.backend == "mock":
        generator = get_generator("mock")
    else:
        generator = get_generator(
            args.backend,
            model_id=args.model,
            max_new_tokens=args.max_new_tokens,
            gpu_memory_utilization=args.gpu_memory_utilization,
            max_model_len=args.max_model_len,
        )

    pipeline = GroundedQAPipeline(generator)
    retriever = load_retriever(args.retriever) if args.retriever else None
    papers = paper_ids_from(args.papers_from) if args.papers_from else []
    passages = load_passage_index(args.passages_from) if args.passages_from else None
    warmup_record = first_record(args.warmup_record) if args.warmup_record else None

    if passages is not None:
        if passages:
            LOGGER.info(
                "passage index: %d passages from %s", len(passages), args.passages_from
            )
        else:
            # An empty index is worse than none: /passages answers 200 with
            # every id missing, which looks like a data problem to the UI.
            LOGGER.warning(
                "passage index is EMPTY after reading %s; POST /passages will "
                "report every id as missing. Check the file's record shape.",
                args.passages_from,
            )

    app = create_app(
        pipeline,
        retriever=retriever,
        papers=papers,
        passages=passages,
        top_k=args.top_k,
        token=args.token,
    )

    # Weights land in VRAM here, before uvicorn listens. A failure at this point
    # costs the job's setup time, not a demo slot.
    generator.load()
    if args.no_warmup:
        LOGGER.warning("warm-up skipped (--no-warmup); the first request will pay it")
    else:
        seconds = warm_up(pipeline, warmup_record, echo=LOGGER.info)
        app.state.demo_state["warmup_seconds"] = round(seconds, 1)

    # Resolved before the log line, so "listening" is never printed by a process
    # that is about to die on a missing dependency.
    uvicorn = _require_uvicorn()

    LOGGER.info(
        "listening on http://%s:%d  (retrieval=%s, papers=%d, top_k=%d)",
        args.host,
        args.port,
        "on" if retriever is not None else "off",
        len(papers),
        args.top_k,
    )

    # An app object rather than an import string, and no reload: either would
    # spawn a second process and therefore a second 8B engine on the same A40.
    uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level)
    return 0


if __name__ == "__main__":  # pragma: no cover - exercised by the sbatch job
    sys.exit(main())
