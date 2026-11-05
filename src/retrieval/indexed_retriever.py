"""Read-only adapter for the plan's prebuilt Lucene and FAISS artifacts."""

import json
from pathlib import Path
from threading import Lock

from .fusion import reciprocal_rank_fusion
from .schemas import Passage, RetrievalHit


def load_chunks(path):
    chunks = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        cid = row["chunk_id"]
        if not isinstance(cid, str) or not cid or cid in chunks:
            raise ValueError("Chunk IDs must be nonempty and unique")
        if not row["text"].strip() or not row["paper_id"].strip():
            raise ValueError("Each chunk needs nonempty text and paper_id")
        chunks[cid] = row
    if not chunks:
        raise ValueError("The chunk corpus is empty")
    return chunks


class IndexedRetriever:
    def __init__(
        self,
        sparse_index_dir,
        dense_index_path,
        dense_row_ids_path,
        chunks_path,
        embedding_model,
    ):
        self.chunks = load_chunks(chunks_path)
        self.row_ids = json.loads(Path(dense_row_ids_path).read_text())
        if (
            not isinstance(self.row_ids, list)
            or len(set(self.row_ids)) != len(self.row_ids)
            or set(self.row_ids) != set(self.chunks)
        ):
            raise ValueError("Dense row IDs must match the canonical chunk IDs exactly")
        config = json.loads(Path(dense_index_path).with_name("config.json").read_text())
        if config["model"] != embedding_model or config["normalized"] is not True:
            raise ValueError("Embedding configuration differs from the built index")
        import faiss
        from pyserini.search.lucene import LuceneSearcher
        from sentence_transformers import SentenceTransformer

        self.dense = faiss.read_index(str(dense_index_path))
        if (
            self.dense.ntotal != len(self.row_ids)
            or self.dense.d != config["dimension"]
            or self.dense.ntotal != config["count"]
            or self.dense.metric_type != faiss.METRIC_INNER_PRODUCT
        ):
            raise ValueError("FAISS index and metadata do not match")
        self.sparse = LuceneSearcher(str(sparse_index_dir))
        self.encoder = SentenceTransformer(embedding_model)
        self.lock = Lock()

    def _hits(self, ids):
        hits = []
        for rank, (cid, score) in enumerate(ids, 1):
            row = self.chunks[cid]
            passage = Passage(
                passage_id=cid,
                paper_id=row["paper_id"],
                title=row.get("title", row["paper_id"]),
                section=" > ".join(row.get("section_path", [])),
                chunk_number=0,
                text=row["text"],
            )
            hits.append(RetrievalHit(passage=passage, rank=rank, score=float(score)))
        return hits

    def retrieve(self, query, top_k=5, candidates=25):
        if not query.strip() or not 1 <= top_k <= candidates:
            raise ValueError("Expected a question and 1 <= top_k <= candidates")
        # Cached resources are shared across sessions; serialize model/search access.
        with self.lock:
            sparse = [
                (h.docid, h.score) for h in self.sparse.search(query, k=candidates)
            ]
            if any(cid not in self.chunks for cid, _ in sparse):
                raise ValueError("Sparse index does not match the chunk corpus")
            vector = self.encoder.encode(
                [query], convert_to_numpy=True, normalize_embeddings=True
            ).astype("float32")
            scores, rows = self.dense.search(vector, min(candidates, len(self.row_ids)))
        dense = [
            (self.row_ids[int(i)], score)
            for i, score in zip(rows[0], scores[0])
            if i >= 0
        ]
        fused = reciprocal_rank_fusion(
            {"bm25": self._hits(sparse), "dense": self._hits(dense)}
        )
        return [
            dict(self.chunks[hit.passage.passage_id], rrf_score=hit.rrf_score)
            for hit in fused[:top_k]
        ]
