"""Hugging Face Transformers backend for Qwen3-8B.

Use this backend for the first smoke test on the cluster and for debugging.
It needs no compilation and no special serving stack, which makes it the safest
way to answer "does Qwen3-8B load on this GPU at all?" before introducing vLLM.
For batch generation over a whole evaluation set, prefer
:mod:`src.generation.generators.vllm_backend` - it is several times faster for the same
weights because it batches properly and manages the KV cache explicitly.

Memory expectation for Qwen3-8B in bfloat16: ~16.4 GB of weights (8.2B params x
2 bytes) plus a few GB of activations and the KV cache. That fits the measured
card - one whole NVIDIA A40, 45.0 GiB - with a wide margin;
``scripts/check_gpu.py`` prints the same arithmetic against whatever GPU you
actually land on.

Qwen3 specifics handled here:

* ``enable_thinking=False`` is passed to ``apply_chat_template``. Qwen3 defaults
  to thinking *on*, and a thinking trace breaks the "JSON object and nothing
  else" contract the prompt asks for. Backends older than the flag simply ignore
  it (see the ``TypeError`` fallback in :meth:`_apply_template`).
* ``pad_token_id`` is pinned to ``eos_token_id``, which Qwen3 does not set by
  default and which would otherwise make batched generation warn or misbehave.
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

_CPU_HINT = (
    "No CUDA device is visible. Set allow_cpu=True to run anyway (this is fine for "
    "a shape check on a tiny prompt, but it will be extremely slow for real "
    "generation)."
)

#: Accepted ``torch_dtype`` spellings, mapped to the canonical ``torch`` attribute.
#: Kept as plain strings so validation never depends on what a particular torch
#: build happens to expose.
_DTYPE_ALIASES = {
    "bfloat16": "bfloat16",
    "bf16": "bfloat16",
    "float16": "float16",
    "fp16": "float16",
    "float32": "float32",
    "fp32": "float32",
}


class TransformersGenerator(GeneratorBackend):
    """Qwen3-8B served through ``transformers`` + ``accelerate``.

    Parameters
    ----------
    model_id:
        HF hub id or a local path to a downloaded snapshot. On the cluster prefer
        a local path: the login node may have no outbound network.
    torch_dtype:
        ``"bfloat16"`` (recommended for Qwen3 on Ampere or newer), ``"float16"``
        on older cards, or ``"auto"`` to trust ``config.json``.
    device_map:
        ``"auto"`` shards across visible GPUs. With one card it behaves like
        ``"cuda:0"``.
    temperature:
        ``0.0`` means greedy decoding, which is what you want for reproducible
        grounded generation. Anything above zero enables sampling and makes the
        citation metrics noisy.
    """

    name: ClassVar[str] = "transformers"

    def __init__(
        self,
        model_id: str = DEFAULT_MODEL_ID,
        *,
        torch_dtype: str = "bfloat16",
        device_map: str = "auto",
        max_new_tokens: int = 768,
        temperature: float = 0.0,
        top_p: float = 0.9,
        enable_thinking: bool | None = False,
        prompt_config: PromptConfig | None = None,
        allow_cpu: bool = False,
        trust_remote_code: bool = True,
        **options: Any,
    ) -> None:
        super().__init__(
            model_id,
            torch_dtype=torch_dtype,
            device_map=device_map,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            enable_thinking=enable_thinking,
            allow_cpu=allow_cpu,
            **options,
        )
        self.torch_dtype = torch_dtype
        self.device_map = device_map
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.enable_thinking = enable_thinking
        self.prompt_config = prompt_config or PromptConfig()
        self.allow_cpu = allow_cpu
        self.trust_remote_code = trust_remote_code

        self._torch: Any = None
        self._tokenizer: Any = None
        self._model: Any = None

    # -- lifecycle --------------------------------------------------------- #

    def _load(self) -> None:
        # The three failure modes are checked in order of how much they narrow the
        # diagnosis: torch missing, then no GPU, then transformers missing. A
        # single combined try/except would report "missing torch" for a machine
        # whose real problem is a CPU-only build, which is the wrong thing to
        # debug first.
        try:
            import torch
        except ImportError as exc:  # pragma: no cover - exercised only without deps
            raise BackendNotAvailable(
                "The 'transformers' backend needs torch:\n"
                "  pip install torch --index-url https://download.pytorch.org/whl/cu124\n"
                f"(import failed with: {exc})"
            ) from exc

        if not torch.cuda.is_available() and not self.allow_cpu:
            raise BackendNotAvailable(_CPU_HINT)

        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:  # pragma: no cover - exercised only without deps
            raise BackendNotAvailable(
                "The 'transformers' backend needs transformers and accelerate:\n"
                "  pip install 'transformers>=4.51.0' 'accelerate>=0.30'\n"
                f"(import failed with: {exc})"
            ) from exc

        self._torch = torch
        self._tokenizer = AutoTokenizer.from_pretrained(
            self.model_id, trust_remote_code=self.trust_remote_code
        )

        # `torch_dtype` was renamed to `dtype` in transformers 4.56; the old name
        # still works but warns. Try the new spelling first so the run log stays
        # clean on a modern install, and fall back for older pins.
        load_kwargs: dict[str, Any] = {
            "device_map": self.device_map,
            "trust_remote_code": self.trust_remote_code,
        }
        dtype = self._resolve_dtype(torch)
        try:
            self._model = AutoModelForCausalLM.from_pretrained(
                self.model_id, dtype=dtype, **load_kwargs
            )
        except TypeError:
            self._model = AutoModelForCausalLM.from_pretrained(
                self.model_id, torch_dtype=dtype, **load_kwargs
            )
        self._model.eval()

        if self._tokenizer.pad_token_id is None:
            self._tokenizer.pad_token_id = self._tokenizer.eos_token_id

    def unload(self) -> None:
        self._model = None
        self._tokenizer = None
        if self._torch is not None and self._torch.cuda.is_available():
            self._torch.cuda.empty_cache()
        self._torch = None
        super().unload()

    # -- generation -------------------------------------------------------- #

    def _generate_text(self, request: GenerationRequest) -> str:
        return self.generate_batch([request])[0]

    def generate_batch(self, requests: Sequence[GenerationRequest]) -> list[str]:
        """Build P5's grounded-QA conversations and serve them in one call."""
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
        enable_thinking: Optional[bool] = None,
    ) -> list[str]:
        """Batched generation for arbitrary conversations, with left padding.

        This is the shared-inference entry point for P4's critic. It uses the
        same loaded model as ``generate_batch``; the caller owns parsing and
        validation of whatever schema it asked for.

        Left padding is required: with right padding every row's first generated
        token would sit at a different offset and slicing off the prompt would
        mix prompt text into the output.
        """
        if not conversations:
            return []
        self._ensure_loaded()
        torch = self._torch

        prompts = [
            self._apply_template(
                messages, enable_thinking=enable_thinking
            )
            for messages in conversations
        ]
        self._tokenizer.padding_side = "left"
        encoded = self._tokenizer(prompts, return_tensors="pt", padding=True)
        encoded = {key: value.to(self._input_device()) for key, value in encoded.items()}
        prompt_width = encoded["input_ids"].shape[1]

        generate_kwargs: dict[str, Any] = {
            "max_new_tokens": max_new_tokens,
            "pad_token_id": self._tokenizer.pad_token_id,
        }
        if temperature and temperature > 0:
            generate_kwargs.update(
                do_sample=True, temperature=temperature, top_p=top_p
            )
        else:
            generate_kwargs.update(do_sample=False)

        started = time.perf_counter()
        with torch.inference_mode():
            output = self._model.generate(**encoded, **generate_kwargs)
        elapsed = time.perf_counter() - started

        self.last_generation_stats = GenerationStats(
            batch_size=len(conversations),
            prompt_tokens=_prompt_token_count(encoded),
            completion_tokens=_completion_token_count(
                output, prompt_width, self._tokenizer.pad_token_id
            ),
            batch_seconds=elapsed,
        )

        return [
            self._tokenizer.decode(row[prompt_width:], skip_special_tokens=True)
            for row in output
        ]

    # -- helpers ----------------------------------------------------------- #

    def _apply_template(
        self,
        messages: Sequence[Mapping[str, str]],
        *,
        enable_thinking: Optional[bool] = None,
    ) -> str:
        """Render chat messages with the model's own chat template.

        ``None`` means "use this backend's setting", which is ``False`` for
        Qwen3. An explicit value wins, so a caller that really wants a reasoning
        trace can ask for one without constructing a second backend.
        """
        template_kwargs: dict[str, Any] = {"add_generation_prompt": True, "tokenize": False}
        thinking = self.enable_thinking if enable_thinking is None else enable_thinking
        if thinking is not None:
            template_kwargs["enable_thinking"] = thinking
        try:
            return self._tokenizer.apply_chat_template(messages, **template_kwargs)
        except TypeError:
            # Chat template predates the Qwen3 thinking switch. Sending the
            # messages without it is better than failing the run; the parse layer
            # will flag the resulting ` thinking` block as format drift.
            template_kwargs.pop("enable_thinking", None)
            return self._tokenizer.apply_chat_template(messages, **template_kwargs)

    def _input_device(self) -> Any:
        """Where input tensors must live when the model is sharded."""
        device = getattr(self._model, "device", None)
        if device is not None and str(device) != "meta":
            return device
        return next(self._model.parameters()).device

    def _resolve_dtype(self, torch: Any) -> Any:
        """Map a dtype name onto a ``torch`` attribute.

        The name is validated *before* any ``torch`` attribute is read. Building the
        mapping eagerly would raise AttributeError on an unknown name on a torch
        build that lacks one of the attributes, reporting an obscure error instead
        of the actionable "unknown torch_dtype" message.
        """
        if self.torch_dtype == "auto":
            return "auto"
        canonical = _DTYPE_ALIASES.get(self.torch_dtype)
        if canonical is None:
            raise BackendNotAvailable(
                f"unknown torch_dtype {self.torch_dtype!r}; expected one of "
                f"{sorted(_DTYPE_ALIASES)} or 'auto'"
            )
        return getattr(torch, canonical)

    def peak_memory_gb(self) -> float | None:
        """Peak allocated VRAM since the last reset, in GB. ``None`` on CPU."""
        if self._torch is None or not self._torch.cuda.is_available():
            return None
        return self._torch.cuda.max_memory_allocated() / 1024**3

    def info(self) -> dict[str, Any]:
        info = super().info()
        info["peak_memory_gb"] = round(self.peak_memory_gb() or 0.0, 2)
        return info


def _prompt_token_count(encoded: dict[str, Any]) -> Optional[int]:
    """Real prompt tokens across the batch, padding excluded.

    The attention mask is the only honest source here. ``input_ids`` is left
    padded to the longest prompt in the batch, so its width overstates the
    prefill by the padding - on a single request that error is zero, on a batch
    of eight prompts differing by hundreds of tokens it is not. Counting the
    mask is also what makes the single-request and batched numbers comparable.

    ``None`` when the tokenizer returned no mask, rather than falling back to the
    padded width: an overcount that looks like a measurement is worse than a
    missing number, because nothing downstream can tell it is wrong.
    """
    mask = encoded.get("attention_mask")
    if mask is None:
        return None
    return int(mask.sum())


def _completion_token_count(output: Any, prompt_width: int, pad_token_id: Any) -> int:
    """Generated tokens across the batch. Approximate, and known to be.

    Two small errors in opposite directions, neither worth correcting:

    * Rows that stopped at EOS are pad-filled out to the widest row in the
      batch, so the count is short by the number of pads.
    * The EOS token that ended each row *is* a real generated token, and
      ``skip_special_tokens=True`` hides it from the decoded text.

    A correction would have to assume every row stopped at EOS, which is false
    for rows that hit ``max_new_tokens`` - and those are exactly the rows whose
    count matters. So the number is reported as approximate instead.
    """
    generated = output[:, prompt_width:]
    return int((generated != pad_token_id).sum())


def template_supports_thinking(tokenizer: Any) -> bool:
    """Whether this tokenizer's chat template accepts ``enable_thinking``.

    Useful as a pre-flight check on a new cluster: if it returns False, the
    Transformers path is running with thinking on and the prompt will need the
    ``/no_think`` soft switch instead.
    """
    template = getattr(tokenizer, "chat_template", None)
    if not isinstance(template, str):
        return False
    return "enable_thinking" in template
