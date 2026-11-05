import argparse
import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chunks", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    p.add_argument("--batch-size", type=int, default=64)
    a = p.parse_args()

    rows = [
        json.loads(line)
        for line in Path(a.chunks).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    ids = [r["chunk_id"] for r in rows]
    if not rows or len(ids) != len(set(ids)):
        raise ValueError("Expected nonempty chunks with unique IDs")

    if any(
        not r["text"].strip() or not r["paper_id"].strip() or not r["chunk_id"]
        for r in rows
    ):
        raise ValueError("Every chunk needs nonempty text, paper_id and chunk_id")

    encoder = SentenceTransformer(a.model)
    vectors = encoder.encode(
        [r["text"] for r in rows],
        batch_size=a.batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype("float32")

    # Normalized vectors + inner product implements cosine similarity.
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(out / "chunks.faiss"))
    (out / "row_ids.json").write_text(
        json.dumps(ids, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out / "config.json").write_text(
        json.dumps(
            {
                "model": a.model,
                "dimension": int(vectors.shape[1]),
                "normalized": True,
                "count": len(ids),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Indexed {len(ids)} chunks")


if __name__ == "__main__":
    main()
