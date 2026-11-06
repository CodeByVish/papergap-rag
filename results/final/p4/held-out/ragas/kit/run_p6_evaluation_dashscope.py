"""Run P6's evaluator with DashScope-compatible embeddings.

DashScope's OpenAI-compatible /embeddings endpoint accepts strings, not the
token-id arrays that langchain-openai sends when check_embedding_ctx_length is
True (the default). This wrapper sets that flag to False for OpenAIEmbeddings
and then calls the unchanged scripts.run_p6_evaluation CLI. The repository is
not modified; the patch is visible here and should be recorded in the run notes.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path.home() / "p4-critic-20261103" / "repo-heldout"
sys.path.insert(0, str(REPO))

import langchain_openai  # noqa: E402

_Original = langchain_openai.OpenAIEmbeddings


class DashScopeEmbeddings(_Original):  # type: ignore[misc, valid-type]
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("check_embedding_ctx_length", False)
        super().__init__(*args, **kwargs)


langchain_openai.OpenAIEmbeddings = DashScopeEmbeddings

from scripts.run_p6_evaluation import main  # noqa: E402

if __name__ == "__main__":
    main(sys.argv[1:])
