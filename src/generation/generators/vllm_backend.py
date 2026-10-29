"""vLLM backend for Qwen3-8B.

This is the backend to use for actual evaluation runs. vLLM's PagedAttention and
continuous batching give several times the throughput of the Transformers path on
the same weights, and - more importantly for this project - its KV cache
accounting is explicit, so ``gpu_memory_utilization`` buys you a predictable
context budget instead of an out-of-memory crash halfway through a batch.

Two constraints that decide whether this backend is even available:

* **vLLM does not run on native Windows.** On the university cluster (Linux) this
  is a non-issue. On this Windows workstation you need WSL2, or use the
  Transformers backend. :meth:`load` says so explicitly rather than failing with
  an opaque import error.
* **``gpu_memory_utilization`` is a fraction of the card, not a byte budget.**
  On the measured card - one whole NVIDIA A40, 45.0 GiB - ``0.85`` reserves
  ~38.3 GiB: ~16.4 GB of bf16 weights plus ~21.5 GiB of KV cache, roughly
  156,000 tokens. See ``docs/GPU_FEASIBILITY.md`` for the arithmetic.

Qwen3 is a hybrid-reasoning model and defaults to thinking *on*. ``LLM.chat``
is called with ``chat_template_kwargs={"enable_thinking": False}`` so the model
answers directly instead of emitting a reasoning trace that would break the
prompt's JSON-only contract.
"""

from __future__ import annotations

import time
from typing import Any, ClassVar, Mapping, Optional, Sequence

from src.generation.generators.base import (
    BackendNotAvailable,
    GenerationStats,
    GeneratorBackend,
)
from src.generation.prompts.grounded_qa import PromptConfig, build_messages
from src.generation.schema import GenerationRequest

DEFAULT_MODEL_ID = "Qwen/Qwen3-8B"

_INSTALL_HINT = (
    "The 'vllm' backend needs the vllm package ({error}).\n"
    "vLLM does not support native Windows - run this on the Linux cluster or "
    "inside WSL2.\n"
    "  pip install 'vllm>=0.8.5'"
)


def _length(value: Any) -> Optional[int]:
    """``len(value)`` for something sequence-shaped, ``None`` for anything else."""
    try:
        return len(value)
    except TypeError:
        return None


def _count_tokens(outputs: Any) -> tuple[Optional[int], Optional[int]]:
    """``(prompt_tokens, completion_tokens)``, each ``None`` when unavailable.

    Every attribute access is guarded, and that is the entire reason this is a
    function rather than three lines inline. vLLM moves these fields around
    between releases and returns ``None`` for ``prompt_token_ids`` when the
    engine was not asked to retain them, so a bare read is a crash waiting for a
    version bump. A crash here is expensive in a way it is not elsewhere: it
    lands after the weights have loaded, and it would cost a whole job to lose a
    metric that is merely useful.

    A total is returned only when **every** row reported a length. Summing the
    rows that answered and calling it the batch total would understate the count
    by an amount nothing downstream can see, which is worse than saying nothing.

    ``None`` is never downgraded to ``0``: a zero here divides every tokens/s
    computed from it into a number that looks like a measurement and is not.
    """
    rows = list(outputs or [])
    if not rows:
        return None, None

    prompt_lengths: list[Optional[int]] = []
    completion_lengths: list[Optional[int]] = []

    for output in rows:
        prompt_lengths.append(_length(getattr(output, "prompt_token_ids", None)))
        completions = getattr(output, "outputs", None)
        first = completions[0] if completions else None
        completion_lengths.append(_length(getattr(first, "token_ids", None)))

    prompt_total = (
        sum(prompt_lengths)  # type: ignore[arg-type]
        if all(length is not None for length in prompt_lengths)
        else None
    )
    completion_total = (
        sum(completion_lengths)  # type: ignore[arg-type]
        if all(length is not None for length in completion_lengths)
        else None
    )
    return prompt_total, completion_total


class VLLMGenerator(GeneratorBackend):
    """Qwen3-8B served by vLLM's offline ``LLM`` engine.

    Parameters
    ----------
    gpu_memory_utilization:
        Fraction of total VRAM vLLM may reserve for weights + KV cache. Raise it
        to fit a longer context; lower it to leave room for another process.
        With one whole 45.0 GiB A40 per job, ``0.85`` is a deliberate choice: it
        leaves ~6.7 GiB untouched so a monitoring process, or whatever else
        lands on the node, does not push the card over.
    max_model_len:
        Hard cap on prompt + generation length. Qwen3-8B's native window is
        32768. Lowering this is the single most effective way to shrink the KV
        cache if VRAM gets tight.
    """

    name: ClassVar[str] = "vllm"
    supports_batch: ClassVar[bool] = True

    def __init__(
        self,
        model_id: str = DEFAULT_MODEL_ID,
        *,
        dtype: str = "bfloat16",
        gpu_memory_utilization: float = 0.85,
        max_model_len: int = 32768,
        tensor_parallel_size: int = 1,
        max_new_tokens: int = 768,
        temperature: float = 0.0,
        top_p: float = 0.9,
        enable_thinking: bool | None = False,
        prompt_config: PromptConfig | None = None,
        enforce_eager: bool = False,
        download_dir: str | None = None,
        **options: Any,
    ) -> None:
        super().__init__(
            model_id,
            dtype=dtype,
            gpu_memory_utilization=gpu_memory_utilization,
            max_model_len=max_model_len,
            tensor_parallel_size=tensor_parallel_size,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            enable_thinking=enable_thinking,
            enforce_eager=enforce_eager,
            **options,
        )
        self.dtype = dtype
        self.gpu_memory_utilization = gpu_memory_utilization
        self.max_model_len = max_model_len
        self.tensor_parallel_size = tensor_parallel_size
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.enable_thinking = enable_thinking
        self.prompt_config = prompt_config or PromptConfig()
        self.enforce_eager = enforce_eager
        self.download_dir = download_dir

        self._llm: Any = None

    # -- lifecycle --------------------------------------------------------- #

    def _load(self) -> None:
        try:
            from vllm import LLM, SamplingParams
        except ImportError as exc:  # pragma: no cover - exercised only without deps
            raise BackendNotAvailable(_INSTALL_HINT.format(error=exc)) from exc

        self._sampling_params_cls = SamplingParams
        self._llm = LLM(
            model=self.model_id,
            dtype=self.dtype,
            gpu_memory_utilization=self.gpu_memory_utilization,
            max_model_len=self.max_model_len,
            tensor_parallel_size=self.tensor_parallel_size,
            enforce_eager=self.enforce_eager,
            download_dir=self.download_dir,
            trust_remote_code=True,
        )

    def unload(self) -> None:
        # Dropping the engine frees the KV cache blocks and the weight tensors;
        # vLLM has no explicit close() in the offline API.
        self._llm = None
        super().unload()

    # -- generation -------------------------------------------------------- #

    def _generate_text(self, request: GenerationRequest) -> str:
        return self.generate_batch([request])[0]

    def generate_batch(self, requests: Sequence[GenerationRequest]) -> list[str]:
        """Build P5's grounded-QA conversations and serve them in one call.

        Returns per-row ``outputs[0].text``. If a row was stopped by the token
        limit rather than by EOS, the text is still returned - the parse layer
        reports the resulting truncation instead of dropping the sample.
        """
        if not requests:
            return []

        conversations = [
            build_messages(request, self.prompt_config) for request in requests
        ]
        return self.chat_batch(
            conversations,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            enable_thinking=self.enable_thinking,
        )

    def chat_batch(
        self,
        conversations: Sequence[Sequence[Mapping[str, str]]],
        *,
        max_new_tokens: int = 256,
        temperature: float = 0.0,
        top_p: float = 0.9,
        enable_thinking: bool | None = None,
    ) -> list[str]:
        """One ``LLM.chat`` call for arbitrary conversations.

        This is the shared-inference entry point for P4's critic. It uses the
        same loaded engine as ``generate_batch``, so a job that runs the agent
        and P5 pays for the weights once. The per-call defaults are deliberately
        greedy and short; the caller owns parsing and validation of whatever
        schema it asked for.
        """
        if not conversations:
            return []
        self._ensure_loaded()

        sampling = self._sampling_params_cls(
            max_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
        )

        # `chat_template_kwargs` exists in vLLM >= 0.8.5. On an older pin the
        # thinking switch cannot be applied here; the parse layer will flag the
        # thinking block that results. `None` means "use this backend's setting",
        # which is False for Qwen3 - a caller asking for a JSON reply should not
        # have to repeat that.
        thinking = self.enable_thinking if enable_thinking is None else enable_thinking
        chat_kwargs: dict[str, Any] = {}
        if thinking is not None:
            chat_kwargs["chat_template_kwargs"] = {"enable_thinking": thinking}

        started = time.perf_counter()
        try:
            outputs = self._llm.chat(conversations, sampling, **chat_kwargs)
        except TypeError:
            outputs = self._llm.chat(conversations, sampling)
        elapsed = time.perf_counter() - started

        prompt_tokens, completion_tokens = _count_tokens(outputs)
        if prompt_tokens is None or completion_tokens is None:
            # One line per batch, not per row. The engine reports these only when
            # it was asked to retain them, so an absent count is a legitimate
            # outcome rather than a bug - but a silent absence reads as "forgot
            # to measure", so the job log says which it is.
            print(
                "[vllm] token accounting unavailable for this batch "
                f"(prompt={prompt_tokens}, completion={completion_tokens}); "
                "tokens/s will be reported as unavailable, not as zero."
            )

        self.last_generation_stats = GenerationStats(
            batch_size=len(conversations),
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            batch_seconds=elapsed,
        )

        # An aborted or filtered request returns an empty ``outputs`` list. The
        # list comprehension this replaces would raise IndexError there, killing
        # a phase that has already paid for the engine load - for one row the
        # parse layer is perfectly capable of reporting as a failure.
        texts: list[str] = []
        for output in outputs:
            completions = getattr(output, "outputs", None)
            texts.append(completions[0].text if completions else "")
        return texts

    def info(self) -> dict[str, Any]:
        info = super().info()
        if self._llm is not None:
            info["kv_cache_budget_gb"] = round(
                self.gpu_memory_utilization * self._total_memory_gb(), 2
            )
        return info

    @staticmethod
    def _total_memory_gb() -> float:
        """Total VRAM of device 0, or 0.0 when torch is unavailable."""
        try:
            import torch

            if not torch.cuda.is_available():
                return 0.0
            return torch.cuda.get_device_properties(0).total_memory / 1024**3
        except Exception:  # pragma: no cover - purely informational
            return 0.0
