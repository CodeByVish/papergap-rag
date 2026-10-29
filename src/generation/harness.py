"""The answer step P4's experiment harness injects into both arms.

``src/agent/experiments.py`` calls

    answer_fn(record: dict) -> dict

once per exported agent record, with the **same function** for the static and
adaptive systems, and stores the return value as ``record["answer"]``. P5 owns
that function and nothing else about the harness: P4 runs the graph and the
critic, P6 builds the runner, and this module turns one exported record into
one answer record.

Two properties matter more than the code:

1. **One code path for both arms.** The function never looks at ``adaptive``;
   it sees only the record's terminal state. The static arm stops at round 1
   with ``sufficient=False`` and still generates. That is the agreed rule
   (2026-10-20, reconfirmed after PR #17): refusing on ``sufficient=False``
   would make the baseline measure the critic's calibration rather than the
   answer quality, and would give the two arms different generation calls.

2. **The refusal decision lives in the pipeline, not here.** This module does
   not re-implement the rule. :meth:`GroundedQAPipeline.answer` refuses without
   a model call only when ``gap_label == INSUFFICIENT_INFORMATION`` or no
   passages were retrieved, and records ``AGENT_INSUFFICIENT`` / ``EMPTY_CONTEXT``
   so the two terminal refusals stay distinguishable from a model refusal.

The return value is P5's canonical answer record, the same shape
``run_batch_to_jsonl`` writes (minus the batch ``index``)::

    {"request_id": ..., "result": {five keys}, "validation": ..., "generation": ...}

``result`` is the frozen five-key payload P6 consumes. ``validation`` and
``generation`` are the audit trail (violations, downgrade reason, raw-text
excerpt); a consumer that only wants answers reads ``["result"]``. The agent
block is attached when the record came from P4, mirroring the batch writer.

An exception is **not** caught here. P4's harness wraps the call per record and
stores ``answer_error`` without stopping the run, which is the behaviour a
six-hour job needs; swallowing it twice would make a broken export look like a
refusal.
"""

from __future__ import annotations

from typing import Any, Callable

from src.generation.adapters.retrieval import build_request
from src.generation.pipeline import GroundedQAPipeline

#: The callable P4's ``run_system`` accepts. Kept as an alias so the shared
#: repository can annotate its parameter with the same name without importing
#: P5 just for a type.
AnswerFn = Callable[[dict[str, Any]], dict[str, Any]]


def answer_record(
    pipeline: GroundedQAPipeline, record: dict[str, Any]
) -> dict[str, Any]:
    """Run P5 on one exported agent record and return a JSON-safe answer record.

    ``record`` is ``export_record(state)`` from ``src/agent/export.py``: the
    terminal ``AgentState`` as a dict, including ``retrieved_passages`` with
    their text. The adapter already tolerates both the nested P2 hit shape and
    a flat one, so no reshaping happens here.

    Raises
    ------
    ValueError, TypeError
        The record is not an AgentState export (no question, no passage list,
        a malformed evidence map). That is an integration bug, not a model
        result; P4's harness records it as ``answer_error`` and continues.
    BackendNotAvailable
        The generator cannot run here. Re-raised by
        :meth:`GroundedQAPipeline.answer_safe` for the same reason: a missing
        GPU or package must fail loudly instead of being counted as a refusal.
    """
    adapted = build_request(record)
    request = adapted.request

    # answer_safe converts parse and generation failures into a
    # GENERATION_ERROR refusal and re-raises BackendNotAvailable. Using the
    # safe path means one bad sample cannot abort the harness run.
    output = pipeline.answer_safe(request)

    answer: dict[str, Any] = {
        "request_id": request.request_id,
        **output.to_wire(),
    }
    agent = request.agent_trace()
    if agent is not None:
        answer["agent"] = agent
    return answer


def make_answer_fn(pipeline: GroundedQAPipeline) -> AnswerFn:
    """Bind a pipeline into the ``answer_fn`` P4's ``run_system`` expects.

    The pipeline holds the one generator engine the job is allowed to load
    (one A40 fits one 8B model), so it is constructed once and closed over::

        generator = get_generator("vllm", model_id=...)
        pipeline = GroundedQAPipeline(generator)
        records = run_system(
            items, retriever,
            adaptive=True,
            critic_client=GeneratorChatClient(generator),
            answer_fn=make_answer_fn(pipeline),
        )

    The same bound function is passed to the static arm. Sharing it is the
    point: the experiment compares retrieval and critic decisions, not two
    subtly different calls into the generator.
    """

    def answer_fn(record: dict[str, Any]) -> dict[str, Any]:
        return answer_record(pipeline, record)

    return answer_fn
