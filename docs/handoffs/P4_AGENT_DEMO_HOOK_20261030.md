# P4 -> P5: run the full agent inside the Option C demo server

Date: 2026-10-30. Branch: `p4/demo-agent-hook`. Status: P4 side done and tested; the server change below is P5's to apply.

## Why

`DEMO_OPTION_C.md` serves a typed question by calling a plain `retriever(question, paper_id, top_k)` and then
`answer_record`. That path never runs the agent: no planner, no critic, no retries, no rewritten query, no
`gap_label`. The demo would then show P5's generator over single-round retrieval, not the system the report
describes. The static arm of the experiment is exactly that baseline.

## What P4 added

| File | What it is |
| --- | --- |
| `src/agent/demo.py` | `make_record_fn(retriever, critic_client, ...)`: `record_fn(question, paper_id, top_k, request_id=None)` runs the whole graph and returns the exported agent record that `answer_record` already takes. |
| `scripts/demo_agent_factory.py` | `factory(pipeline)`: builds the retriever from `DEMO_AGENT_*` environment variables and the critic from `pipeline.generator`. No second model is loaded. |
| `tests/test_demo.py` | 8 tests (record shape, critic rounds, blank question, per-`top_k` graph cache, factory configuration). |

A blank question raises `ValueError`, which the server already maps to HTTP 400.

## What P5 changes

`src/generation/server.py` only: a `--record-fn module:factory` option, a `record_fn` argument to `create_app`, and
one branch in `_one_at_a_time`. `/health` gains `"agent": true`. `--retriever` and `--record-fn` are alternatives.
The `record` payload path and the plain-retriever path are unchanged.

```bash
python -m src.generation.server --record-fn scripts.demo_agent_factory:factory \
  --papers-from $P5_ROOT/data/bge/retrieval.jsonl --passages-from <passages.jsonl> --token ...
```

Environment for the factory (full list in the docstring of `scripts/demo_agent_factory.py`):
`DEMO_AGENT_PASSAGES`, `DEMO_AGENT_DENSE_INDEX` (required); `DEMO_AGENT_SCOPED` (default 1), `DEMO_AGENT_BGE`,
`DEMO_AGENT_SCORE_CACHE`, `DEMO_AGENT_CACHE_FOLDER`, `DEMO_AGENT_OFFLINE`, `DEMO_AGENT_DEVICE` (default `cpu`).

Retrieval models stay on the CPU by default because vLLM checks free GPU memory when it loads.

## What was and was not verified

- Verified: factory -> `record_fn` -> `answer_record` on real pilot retrieval with the mock backend, on current
  main. The answer has `request_id`, the five-key `result`, `validation`, `generation` and the `agent` block
  with `retrieval_rounds` equal to the rounds actually run.
- Not verified: the HTTP layer. `fastapi` is not installed in P4's environment, so `tests/test_server.py` and
  `scripts/smoke_demo_server.py` were not run against the diff below. Please run them, and check that no existing
  test asserts the exact key set of `/health` (the diff adds `agent`).
- Not verified: the Qwen critic inside the server (needs the cluster).
- Expected latency: one answer call plus up to three critic calls of about 2-4 s each, so roughly 20-30 s per
  question when all three rounds run. This is inside the 120 s client timeout in `P6_UI_CONTRACT.md`.

## The server diff (against main at `97e33b2`)

```diff
diff --git a/src/generation/server.py b/src/generation/server.py
index baabba5..baec5d8 100644
--- a/src/generation/server.py
+++ b/src/generation/server.py
@@ -63,6 +63,11 @@ from src.generation.prompts.grounded_qa import PROMPT_VERSION
 
 LOGGER = logging.getLogger("src.generation.server")
 
+#: P4's agent hook: ``(question, paper_id, top_k, request_id) -> exported agent record``.
+#: Runs the whole agent loop (retrieval rounds + critic) and returns the record
+#: ``answer_record`` expects; takes precedence over a plain retriever.
+RecordFn = Callable[..., dict[str, Any]]
+
 #: A retriever adapter: ``(question, paper_id, top_k) -> list of hits``.
 #: Hits may be P2's nested ``{"passage": {...}}`` objects or already flat; the
 #: adapter in :mod:`src.generation.adapters.retrieval` accepts both.
@@ -136,6 +141,21 @@ def load_retriever(spec: str) -> RetrieverFn:
     return retriever
 
 
+def load_record_fn(spec: str, pipeline: Any) -> RecordFn:
+    """Resolve ``"module:factory"`` and call ``factory(pipeline)``.
+
+    The factory gets the pipeline so the agent's critic can share the one engine
+    this job is allowed to load.
+    """
+    module_name, _, attr = spec.partition(":")
+    if not module_name or not attr:
+        raise ValueError(f"record-fn spec {spec!r} must look like 'package.module:factory'")
+    record_fn = getattr(importlib.import_module(module_name), attr)(pipeline)
+    if not callable(record_fn):
+        raise TypeError(f"{spec} returned {type(record_fn).__name__}, not a callable")
+    return record_fn
+
+
 def paper_ids_from(path: str | Path) -> list[str]:
     """Unique ``paper_id`` values in a retrieval dump, sorted.
 
@@ -319,6 +339,7 @@ def create_app(
     pipeline: GroundedQAPipeline,
     *,
     retriever: Optional[RetrieverFn] = None,
+    record_fn: Optional[RecordFn] = None,
     papers: Sequence[str] = (),
     passages: Optional[Mapping[str, Mapping[str, Any]]] = None,
     top_k: int = 5,
@@ -393,7 +414,7 @@ def create_app(
                     "retrieval is paper-scoped"
                 ),
             )
-        if retriever is None:
+        if retriever is None and record_fn is None:
             raise HTTPException(
                 status_code=503,
                 detail=(
@@ -427,6 +448,10 @@ def create_app(
         try:
             if "record" in parsed:
                 record = dict(parsed["record"])
+            elif record_fn is not None:
+                record = record_fn(
+                    parsed["question"], parsed["paper_id"], top_k, parsed["request_id"]
+                )
             else:
                 hits = retriever(parsed["question"], parsed["paper_id"], top_k)
                 if not isinstance(hits, Sequence) or isinstance(hits, (str, bytes)):
@@ -464,7 +489,8 @@ def create_app(
             "backend": backend_info.get("backend"),
             "model_id": backend_info.get("model_id"),
             "prompt_version": prompt_version,
-            "retrieval": retriever is not None,
+            "retrieval": retriever is not None or record_fn is not None,
+            "agent": record_fn is not None,
             "passage_text": bool(passages),
             "top_k": top_k,
             "papers": len(papers),
@@ -572,6 +598,12 @@ def build_parser() -> argparse.ArgumentParser:
         default=None,
         help="'module:factory' returning retriever(question, paper_id, top_k)",
     )
+    parser.add_argument(
+        "--record-fn",
+        default=None,
+        help="'module:factory'; factory(pipeline) returns P4's record_fn "
+        "(runs the full agent per question; replaces --retriever)",
+    )
     parser.add_argument(
         "--papers-from",
         default=None,
@@ -618,7 +650,10 @@ def main(argv: Optional[Sequence[str]] = None) -> int:
         )
 
     pipeline = GroundedQAPipeline(generator)
+    if args.retriever and args.record_fn:
+        raise SystemExit("--retriever and --record-fn are alternatives; pass one")
     retriever = load_retriever(args.retriever) if args.retriever else None
+    record_fn = load_record_fn(args.record_fn, pipeline) if args.record_fn else None
     papers = paper_ids_from(args.papers_from) if args.papers_from else []
     passages = load_passage_index(args.passages_from) if args.passages_from else None
     warmup_record = first_record(args.warmup_record) if args.warmup_record else None
@@ -640,6 +675,7 @@ def main(argv: Optional[Sequence[str]] = None) -> int:
     app = create_app(
         pipeline,
         retriever=retriever,
+        record_fn=record_fn,
         papers=papers,
         passages=passages,
         top_k=args.top_k,
```
