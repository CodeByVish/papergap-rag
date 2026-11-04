"""Local Ollama adapter; P5 still owns prompting, parsing and validation."""

from __future__ import annotations

from typing import Any

import requests

from src.generation.generators.base import (
    BackendNotAvailable,
    GenerationStats,
    GeneratorBackend,
)
from src.generation.prompts.grounded_qa import build_messages


class OllamaGenerator(GeneratorBackend):
    name = "ollama"

    def __init__(
        self,
        model_id="qwen3:14b",
        *,
        base_url="http://127.0.0.1:11434",
        timeout=600,
        num_ctx=8192,
        max_new_tokens=1024,
        **options: Any,
    ):
        super().__init__(
            model_id,
            base_url=base_url,
            num_ctx=num_ctx,
            max_new_tokens=max_new_tokens,
            **options,
        )
        self.base_url = base_url.rstrip("/")
        self.timeout = float(timeout)
        self.num_ctx = int(num_ctx)
        self.max_new_tokens = int(max_new_tokens)
        self.model_digest = None

    def _post(self, endpoint, payload):
        try:
            response = requests.post(
                self.base_url + endpoint, json=payload, timeout=(5, self.timeout)
            )
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as exc:
            raise BackendNotAvailable(
                f"Ollama {endpoint} failed for {self.model_id}: {exc}"
            ) from exc

    def _load(self):
        # /api/show checks availability without silently downloading a model.
        self._post("/api/show", {"model": self.model_id})
        try:
            response = requests.get(self.base_url + "/api/tags", timeout=5)
            response.raise_for_status()
            models = response.json().get("models", [])
            self.model_digest = next(
                (m.get("digest") for m in models if m.get("name") == self.model_id),
                None,
            )
        except (requests.RequestException, ValueError) as exc:
            raise BackendNotAvailable(f"Cannot inspect Ollama models: {exc}") from exc

    def _chat(self, messages, *, max_new_tokens, temperature, top_p, enable_thinking):
        data = self._post(
            "/api/chat",
            {
                "model": self.model_id,
                "messages": list(messages),
                "stream": False,
                "think": bool(enable_thinking),
                "keep_alive": "10m",
                "options": {
                    "num_ctx": self.num_ctx,
                    "num_predict": max_new_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                    "seed": 42,
                },
            },
        )
        message = data.get("message", {})
        content = message.get("content")
        if not isinstance(content, str) or not content.strip():
            raise BackendNotAvailable("Ollama returned no answer content")
        seconds = data.get("total_duration", 0) / 1e9
        self.last_generation_stats = GenerationStats(
            prompt_tokens=data.get("prompt_eval_count"),
            completion_tokens=data.get("eval_count"),
            batch_seconds=seconds or None,
        )
        self.last_finish_reason = data.get("done_reason")
        return content

    def _generate_text(self, request):
        content = self._chat(
            build_messages(request, self.prompt_config),
            max_new_tokens=self.max_new_tokens,
            temperature=0.0,
            top_p=0.9,
            enable_thinking=False,
        )
        if self.last_finish_reason == "length":
            raise RuntimeError(
                "Ollama completion limit reached; increase P6_MAX_NEW_TOKENS"
            )
        return content

    def chat_batch(
        self,
        conversations,
        *,
        max_new_tokens=256,
        temperature=0.0,
        top_p=0.9,
        enable_thinking=None,
    ):
        self.load()
        return [
            self._chat(
                messages,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                enable_thinking=enable_thinking,
            )
            for messages in conversations
        ]

    def info(self):
        return {
            **super().info(),
            "model_digest": self.model_digest,
            "timing_policy": "Ollama total_duration; includes server load/evaluation",
        }
