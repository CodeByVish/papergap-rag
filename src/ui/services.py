"""Streamlit resource boundary; heavy retrieval dependencies load on demand."""

from pathlib import Path

import streamlit as st

from src.retrieval.indexed_retriever import IndexedRetriever

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAG = {
    "sparse_index_dir": "indexes/sparse/lucene",
    "dense_index_path": "indexes/dense/chunks.faiss",
    "dense_row_ids_path": "indexes/dense/row_ids.json",
    "chunks_path": "data/chunks.jsonl",
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
}


def rag_config(overrides):
    if not isinstance(overrides, dict):
        raise TypeError("Expected a [rag] table")
    cfg = DEFAULT_RAG | {k: v for k, v in overrides.items() if k in DEFAULT_RAG}
    if any(not isinstance(value, str) or not value.strip() for value in cfg.values()):
        raise ValueError("RAG settings must be nonempty strings")
    for key in DEFAULT_RAG:
        if key != "embedding_model":
            cfg[key] = str(ROOT / cfg[key])
    return cfg


def missing_artifacts(cfg):
    paths = [Path(value) for key, value in cfg.items() if key != "embedding_model"]
    paths.append(Path(cfg["dense_index_path"]).with_name("config.json"))
    return [
        str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        for path in paths
        if not path.exists()
    ]


@st.cache_resource(show_spinner=False)
def get_retriever(cfg):
    return IndexedRetriever(**cfg)
