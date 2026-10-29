"""Generator backends.

Importing this package is safe on a CPU-only machine: the Transformers and vLLM
modules import torch/vllm *inside* ``load()``, so a missing GPU stack surfaces as
a :class:`BackendNotAvailable` when you ask for a model, not as an ImportError
when you import a module.

    from src.generation.generators import get_generator
    generator = get_generator("mock")                    # always works
    generator = get_generator("vllm")                    # needs a CUDA box
    generator = get_generator("transformers", temperature=0.0)
"""

from __future__ import annotations

from typing import Any, Callable

from src.generation.generators.base import (
    BackendNotAvailable,
    GenerationStats,
    GeneratorBackend,
    ParseDiagnostics,
    ResponseParseError,
    parse_response,
)
from src.generation.generators.mock import DEFAULT_CYCLE, MockConfig, MockGenerator, MockScenario

__all__ = [
    "DEFAULT_CYCLE",
    "BackendNotAvailable",
    "GenerationStats",
    "GeneratorBackend",
    "MockConfig",
    "MockGenerator",
    "MockScenario",
    "ParseDiagnostics",
    "ResponseParseError",
    "available_backends",
    "get_generator",
    "parse_response",
]


def _load_vllm() -> type[GeneratorBackend]:
    from src.generation.generators.vllm_backend import VLLMGenerator

    return VLLMGenerator


def _load_transformers() -> type[GeneratorBackend]:
    from src.generation.generators.transformers_backend import TransformersGenerator

    return TransformersGenerator


#: Backends are resolved lazily so that naming "vllm" does not import vllm.
_REGISTRY: dict[str, Callable[[], type[GeneratorBackend]]] = {
    "mock": lambda: MockGenerator,
    "transformers": _load_transformers,
    "hf": _load_transformers,
    "vllm": _load_vllm,
}


def available_backends() -> list[str]:
    """Canonical backend names. Aliases are omitted."""
    return ["mock", "transformers", "vllm"]


def get_generator(name: str = "mock", **kwargs: Any) -> GeneratorBackend:
    """Build a backend by name.

    Raises
    ------
    KeyError
        Unknown name. The message lists the valid ones - a typo in a batch script
        should not cost you a queue slot.
    """
    key = name.strip().lower()
    if key not in _REGISTRY:
        raise KeyError(
            f"unknown generator backend {name!r}; "
            f"expected one of {available_backends()}"
        )
    backend_cls = _REGISTRY[key]()
    return backend_cls(**kwargs)
