"""P5 - evidence-constrained generation and grounding.

Public surface used by P6:

    from src.generation import (
        GenerationResult, EvidenceStatus, RetrievedPassage, GenerationRequest,
        GroundedQAPipeline, CitationValidator, MockGenerator,
    )
"""

from src.generation.citations import (
    CitationValidator,
    Severity,
    ValidationConfig,
    ValidationReport,
    ValidationViolation,
    ViolationCode,
)
from src.generation.harness import answer_record, make_answer_fn
from src.generation.pipeline import GroundedQAPipeline, PipelineOutput, run_batch_to_jsonl
from src.generation.prompts.grounded_qa import (
    PROMPT_VERSION,
    SYSTEM_PROMPT,
    build_messages,
    build_prompt,
)
from src.generation.schema import (
    ANSWER_KEYS,
    REFUSAL_ANSWER,
    SCHEMA_VERSION,
    EvidenceStatus,
    GenerationRequest,
    GenerationResult,
    ProvenanceEntry,
    RetrievedPassage,
    Support,
)

__all__ = [
    "ANSWER_KEYS",
    "CitationValidator",
    "EvidenceStatus",
    "GenerationRequest",
    "GenerationResult",
    "GroundedQAPipeline",
    "PROMPT_VERSION",
    "PipelineOutput",
    "ProvenanceEntry",
    "REFUSAL_ANSWER",
    "RetrievedPassage",
    "SCHEMA_VERSION",
    "SYSTEM_PROMPT",
    "Severity",
    "Support",
    "ValidationConfig",
    "ValidationReport",
    "ValidationViolation",
    "ViolationCode",
    "answer_record",
    "build_messages",
    "build_prompt",
    "make_answer_fn",
    "run_batch_to_jsonl",
]

__version__ = "0.1.0"


def __getattr__(name: str):
    """Lazily expose the generator backends.

    `MockGenerator` is dependency-free, but importing `src.generation.generators` also
    pulls in the transformers/vLLM backend modules. Those modules import
    torch/vllm *lazily* (inside `load()`), so a plain import is safe - but going
    through `__getattr__` keeps the failure mode obvious if that ever changes.
    """
    if name in {"MockGenerator", "MockScenario", "get_generator"}:
        from src.generation import generators

        return getattr(generators, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
