"""Paper-scoped BGE cosine retrieval with persistent FAISS row mappings."""

import hashlib
import json
import re
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Protocol

import faiss
import numpy as np

from .schemas import Passage, RetrievalHit

DEFAULT_MODEL_NAME = "BAAI/bge-small-en-v1.5"
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "
_INDEX_SETTINGS = {
    "format_version": 1,
    "query_instruction": QUERY_INSTRUCTION,
    "normalization": "l2",
    "similarity_metric": "cosine",
    "index_type": "IndexFlatIP",
    "max_seq_length": 512,
}


class Encoder(Protocol):
    """Injected encoders must declare an identity, not just a vector dimension.

    Callers are responsible for assigning a new revision when their encoder's
    weights or encoding behavior change. Test encoders should use a test name.
    """

    model_name: str
    revision: str | None

    def encode(self, texts: Sequence[str]) -> np.ndarray: ...


class _SentenceTransformerEncoder:
    """Load the approved model lazily; never add an implicit model prompt."""

    model_name = DEFAULT_MODEL_NAME

    def __init__(
        self, revision, device, batch_size, cache_folder, local_files_only
    ) -> None:
        self.revision = revision
        self._device = device
        self._batch_size = batch_size
        self._cache_folder = str(
            cache_folder
            if cache_folder is not None
            else Path(__file__).resolve().parents[2] / ".cache/huggingface"
        )
        self._local_files_only = local_files_only
        self._model = None

    def encode(self, texts: Sequence[str]) -> np.ndarray:
        if self._model is None:
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer(
                self.model_name,
                revision=self.revision,
                device=self._device,
                cache_folder=self._cache_folder,
                local_files_only=self._local_files_only,
            )
            candidates = (
                getattr(model[0].auto_model.config, "_commit_hash", None),
                getattr(model.model_card_data, "base_model_revision", None),
                self.revision,
            )
            resolved = next(
                (
                    value
                    for value in candidates
                    if isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value)
                ),
                None,
            )
            if resolved is None:
                raise ValueError("Cannot resolve an immutable model revision")
            if (
                self.revision is not None
                and re.fullmatch(r"[0-9a-f]{40}", self.revision)
                and resolved != self.revision
            ):
                raise ValueError("Loaded model revision does not match the index")
            self.revision = resolved
            model.max_seq_length = _INDEX_SETTINGS["max_seq_length"]
            self._model = model
        return self._model.encode(
            list(texts),
            batch_size=self._batch_size,
            convert_to_numpy=True,
            normalize_embeddings=False,
            show_progress_bar=False,
            prompt="",
        )


def _encoder_identity(encoder: Encoder) -> tuple[str, str | None]:
    name = getattr(encoder, "model_name", None)
    revision = getattr(encoder, "revision", None)
    if not isinstance(name, str) or not name.strip():
        raise ValueError("encoder must declare a nonempty model_name")
    if not hasattr(encoder, "revision") or (
        revision is not None and (not isinstance(revision, str) or not revision.strip())
    ):
        raise ValueError("encoder must declare a revision string or None")
    return name, revision


def _normalize_vectors(values, count: int, dimension: int | None) -> np.ndarray:
    """Validate and normalize in float64 before producing contiguous float32."""
    try:
        array = np.asarray(values)
    except (TypeError, ValueError) as error:
        raise ValueError("Embeddings must be a rectangular numeric matrix") from error
    if array.dtype.kind not in "fiu":
        raise ValueError("Embeddings must contain real numeric values")
    if array.ndim != 2 or array.shape[0] != count or array.shape[1] < 1:
        raise ValueError("Embedding count or matrix shape is invalid")
    if dimension is not None and array.shape[1] != dimension:
        raise ValueError("Embedding dimension does not match the index")
    array = array.astype(np.float64)
    if not np.isfinite(array).all():
        raise ValueError("Embeddings must contain finite values")
    # Scaling first avoids overflowing the norm of otherwise finite vectors.
    scale = np.max(np.abs(array), axis=1, keepdims=True)
    if np.any(scale == 0):
        raise ValueError("Zero-norm embeddings cannot define cosine similarity")
    array = array / scale
    array = array / np.linalg.norm(array, axis=1, keepdims=True)
    return np.ascontiguousarray(array, dtype=np.float32)


class DenseRetriever:
    """One IndexFlatIP per paper, sharing the same encoder and cosine rules.

    Pass ``retriever.retrieve`` as P2's dense callback. Inject an Encoder for
    offline tests; the default path uses the approved SentenceTransformer.
    """

    def __init__(
        self,
        passages: Iterable[Passage],
        *,
        encoder: Encoder | None = None,
        revision: str | None = None,
        device: str = "cpu",
        batch_size: int = 32,
        cache_folder: str | Path | None = None,
        local_files_only: bool = False,
    ) -> None:
        if (
            isinstance(batch_size, bool)
            or not isinstance(batch_size, int)
            or batch_size < 1
        ):
            raise ValueError("batch_size must be a positive integer")
        if revision is not None and (
            not isinstance(revision, str) or not revision.strip()
        ):
            raise ValueError("revision must be a nonempty string or None")
        self._encoder_kind = (
            "injected" if encoder is not None else "sentence_transformer"
        )
        self._encoder = (
            encoder
            if encoder is not None
            else _SentenceTransformerEncoder(
                revision, device, batch_size, cache_folder, local_files_only
            )
        )
        self._model_name, self._revision = _encoder_identity(self._encoder)
        if revision is not None and self._revision != revision:
            raise ValueError("encoder revision does not match the requested revision")
        self._dimension: int | None = None
        self._passages: dict[str, list[Passage]] = {}
        self._indexes: dict[str, faiss.IndexFlatIP] = {}
        seen_ids: set[str] = set()
        for passage in passages:
            if passage.passage_id in seen_ids:
                raise ValueError(f"Duplicate passage_id: {passage.passage_id}")
            seen_ids.add(passage.passage_id)
            self._passages.setdefault(passage.paper_id, []).append(passage)
        for paper_id in sorted(self._passages):
            paper_passages = self._passages[paper_id]
            paper_passages.sort(key=lambda passage: passage.passage_id)
            vectors = self._encode([passage.text for passage in paper_passages])
            self._dimension = vectors.shape[1]
            index = faiss.IndexFlatIP(self._dimension)
            index.add(vectors)
            self._indexes[paper_id] = index

    def _encode(self, texts: Sequence[str]) -> np.ndarray:
        if _encoder_identity(self._encoder) != (self._model_name, self._revision):
            raise ValueError("Encoder model_name or revision changed after indexing")
        vectors = _normalize_vectors(
            self._encoder.encode(texts), len(texts), self._dimension
        )
        identity = _encoder_identity(self._encoder)
        # A fresh real model resolves a branch/tag to an immutable commit once.
        if self._encoder_kind == "sentence_transformer" and self._dimension is None:
            self._revision = identity[1]
        if identity != (self._model_name, self._revision):
            raise ValueError("Encoder model_name or revision changed during encoding")
        return vectors

    def retrieve(self, query: str, paper_id: str, top_k: int) -> list[RetrievalHit]:
        """Return deterministic cosine top-K within the selected paper only."""
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a nonempty string")
        if not isinstance(paper_id, str) or not paper_id.strip():
            raise ValueError("paper_id must be a nonempty string")
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer")
        if paper_id not in self._indexes:
            return []
        query_vector = self._encode([QUERY_INSTRUCTION + query])
        index = self._indexes[paper_id]
        # Include every tie at the K boundary before applying the stable order.
        scores, rows = index.search(query_vector, index.ntotal)
        if not np.isfinite(scores).all():
            raise ValueError("FAISS must return finite cosine scores")
        passages = self._passages[paper_id]
        ranked = sorted(
            (
                (passages[int(row)], float(score))
                for row, score in zip(rows[0], scores[0])
            ),
            key=lambda item: (-item[1], item[0].passage_id),
        )
        return [
            RetrievalHit(passage=passage, rank=rank, score=score)
            for rank, (passage, score) in enumerate(ranked[:top_k], start=1)
        ]

    def save(self, directory: str | Path) -> None:
        """Write indexes and metadata into a new or empty directory.

        Each paper's ordered Passage list is its row-to-Passage mapping. No
        model weights are saved here. Existing nonempty directories are refused.
        """
        if _encoder_identity(self._encoder) != (self._model_name, self._revision):
            raise ValueError("Encoder identity no longer matches the index")
        directory = Path(directory)
        if directory.exists() and (not directory.is_dir() or any(directory.iterdir())):
            raise ValueError("Save directory must be new or empty")
        directory.mkdir(parents=True, exist_ok=True)
        metadata = {
            **_INDEX_SETTINGS,
            "model_name": self._model_name,
            "revision": self._revision,
            "encoder_kind": self._encoder_kind,
            "embedding_dimension": self._dimension,
            "papers": [],
        }
        for number, paper_id in enumerate(sorted(self._indexes)):
            data = faiss.serialize_index(self._indexes[paper_id]).tobytes()
            (directory / f"paper-{number:06d}.faiss").write_bytes(data)
            metadata["papers"].append(
                {
                    "paper_id": paper_id,
                    "passages": [p.model_dump() for p in self._passages[paper_id]],
                    "index_sha256": hashlib.sha256(data).hexdigest(),
                }
            )
        (directory / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    @classmethod
    def load(
        cls,
        directory: str | Path,
        *,
        encoder: Encoder | None = None,
        model_name: str | None = None,
        revision: str | None = None,
        query_instruction: str = QUERY_INSTRUCTION,
        device: str = "cpu",
        batch_size: int = 32,
        cache_folder: str | Path | None = None,
        local_files_only: bool = False,
    ) -> "DenseRetriever":
        """Restore saved FAISS vectors without re-encoding any passage.

        Optional model_name/revision arguments assert the expected identity.
        Injected indexes require an explicitly supplied, matching encoder.
        Real indexes restore the recorded immutable revision on first query.
        """
        directory = Path(directory)
        metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
        if not isinstance(metadata, dict):
            # Malformed persisted JSON is a value error, not an API type error.
            raise ValueError("Index metadata must be an object")  # noqa: TRY004
        for key, expected in _INDEX_SETTINGS.items():
            if (
                type(metadata.get(key)) is not type(expected)
                or metadata[key] != expected
            ):
                raise ValueError(f"Incompatible index metadata: {key}")
        if query_instruction != QUERY_INSTRUCTION:
            raise ValueError(
                "query_instruction does not match the saved encoding rules"
            )
        saved_name = metadata.get("model_name")
        saved_revision = metadata.get("revision")
        if not isinstance(saved_name, str) or not saved_name.strip():
            raise ValueError("Missing or invalid model_name metadata")
        if "revision" not in metadata or (
            saved_revision is not None
            and (not isinstance(saved_revision, str) or not saved_revision.strip())
        ):
            raise ValueError("Missing or invalid revision metadata")
        if model_name is not None and model_name != saved_name:
            raise ValueError("model_name does not match the saved index")
        if revision is not None and revision != saved_revision:
            raise ValueError("revision does not match the saved index")
        kind = metadata.get("encoder_kind")
        if kind == "injected":
            if encoder is None:
                raise ValueError("An injected index requires its matching encoder")
            if _encoder_identity(encoder) != (saved_name, saved_revision):
                raise ValueError(
                    "Encoder model_name or revision does not match the index"
                )
        elif kind == "sentence_transformer":
            if encoder is not None or saved_name != DEFAULT_MODEL_NAME:
                raise ValueError(
                    "Saved index requires the approved SentenceTransformer"
                )
        else:
            raise ValueError("Invalid encoder_kind metadata")
        papers = metadata.get("papers")
        dimension = metadata.get("embedding_dimension")
        if not isinstance(papers, list) or "embedding_dimension" not in metadata:
            raise ValueError("Missing papers or embedding_dimension metadata")
        if papers:
            if type(dimension) is not int or dimension < 1:
                raise ValueError("Invalid embedding_dimension metadata")
            if kind == "sentence_transformer" and (
                not isinstance(saved_revision, str)
                or not re.fullmatch(r"[0-9a-f]{40}", saved_revision)
            ):
                raise ValueError("Real indexes require an immutable model revision")
        elif dimension is not None:
            raise ValueError("Empty indexes must have a null embedding_dimension")
        result = cls(
            [],
            encoder=encoder,
            revision=saved_revision,
            device=device,
            batch_size=batch_size,
            cache_folder=cache_folder,
            local_files_only=local_files_only,
        )
        result._dimension = dimension
        seen_ids: set[str] = set()
        for number, paper in enumerate(papers):
            if not isinstance(paper, dict):
                raise ValueError("Invalid paper mapping")  # noqa: TRY004
            paper_id = paper.get("paper_id")
            if not isinstance(paper_id, str) or not paper_id.strip():
                raise ValueError("Invalid paper_id in index mapping")
            if paper_id in result._indexes:
                raise ValueError("Duplicate paper_id in index mapping")
            raw_passages = paper.get("passages")
            if not isinstance(raw_passages, list) or not raw_passages:
                raise ValueError("Each paper index requires a nonempty Passage mapping")
            passages = [Passage.model_validate(raw) for raw in raw_passages]
            for passage in passages:
                if passage.paper_id != paper_id:
                    raise ValueError(
                        "Passage belongs to another paper in index mapping"
                    )
                if passage.passage_id in seen_ids:
                    raise ValueError("Duplicate passage_id in index mapping")
                seen_ids.add(passage.passage_id)
            if passages != sorted(passages, key=lambda passage: passage.passage_id):
                raise ValueError(
                    "Passage mapping is not in the saved canonical row order"
                )
            data = (directory / f"paper-{number:06d}.faiss").read_bytes()
            if hashlib.sha256(data).hexdigest() != paper.get("index_sha256"):
                raise ValueError("FAISS index checksum does not match its mapping")
            try:
                index = faiss.deserialize_index(np.frombuffer(data, dtype=np.uint8))
            except RuntimeError as error:
                raise ValueError("Invalid FAISS index data") from error
            if (
                not isinstance(index, faiss.IndexFlatIP)
                or index.metric_type != faiss.METRIC_INNER_PRODUCT
            ):
                raise ValueError("FAISS index must be IndexFlatIP")
            if index.d != dimension or index.ntotal != len(passages):
                raise ValueError(
                    "FAISS dimension or row count does not match the mapping"
                )
            vectors = index.reconstruct_n(0, index.ntotal)
            if not np.isfinite(vectors).all() or not np.allclose(
                np.linalg.norm(vectors.astype(np.float64), axis=1),
                1.0,
                rtol=1e-5,
                atol=1e-6,
            ):
                raise ValueError("Saved FAISS vectors must be finite and L2 normalized")
            result._passages[paper_id] = passages
            result._indexes[paper_id] = index
        return result
