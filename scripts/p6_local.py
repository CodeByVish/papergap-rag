"""Prepared P6 local runtime: setup once, then `python -m scripts.p6_local start`."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

# Set before importing Torch/FAISS: this macOS wheel combination crashes when
# multiple OpenMP runtimes form worker teams. Retrieval uses one native thread.
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs/p6-local.env"
RUNTIME = ROOT / "results/p6-local"


def configure():
    from dotenv import dotenv_values

    values = dict(dotenv_values(CONFIG))
    override = Path(
        os.environ.get("P6_CONFIG_FILE", ROOT / ".env.p6.local")
    ).expanduser()
    if not override.is_absolute():
        override = ROOT / override
    if "P6_CONFIG_FILE" in os.environ and not override.is_file():
        raise FileNotFoundError(f"Configured override file does not exist: {override}")
    if override.exists():
        values.update(dotenv_values(override))
    # Config is authoritative, so old terminal exports cannot select stale paths.
    for key, value in values.items():
        os.environ[key] = value or ""
    for key in (
        "PAPERGAP_CORPUS",
        "PAPERGAP_DENSE_INDEX",
        "HF_HOME",
        "DEMO_AGENT_CACHE_FOLDER",
        "P5_RECORDS_PATH",
        "P6_SAMPLES_PATH",
        "P6_PAPER_CATALOG_PATH",
    ):
        value = Path(os.environ[key]).expanduser()
        os.environ[key] = str(value if value.is_absolute() else ROOT / value)
    os.chdir(ROOT)
    RUNTIME.mkdir(parents=True, exist_ok=True)


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def git_blob(revision, name, target):
    data = subprocess.check_output(["git", "show", f"{revision}:{name}"], cwd=ROOT)
    if target.exists() and target.read_bytes() != data:
        raise RuntimeError(f"Refusing to overwrite different local data: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def setup():
    """Use P5-matching inference text with existing development-only demo questions."""
    from scripts.build_indexes import build_indexes, load_passages

    ref = os.environ["P6_P3_REF"]
    revision = subprocess.check_output(["git", "rev-parse", ref], text=True).strip()
    corpus = Path(os.environ["PAPERGAP_CORPUS"])
    manifest = corpus.with_suffix(".manifest.json")
    digest = git_blob(revision, os.environ["P6_P3_CORPUS_PATH"], corpus)
    git_blob(revision, os.environ["P6_P3_MANIFEST_PATH"], manifest)
    source_manifest = json.loads(manifest.read_text())
    chunking = source_manifest["chunking"]
    if (chunking["chunk_size_words"], chunking["chunk_overlap_words"]) != (365, 40):
        raise RuntimeError("Demo requires the reviewed 365/40 corpus")
    expected = source_manifest["output"]
    if digest != expected["sha256"]:
        raise RuntimeError("P3 corpus SHA-256 does not match its manifest")
    passages = load_passages(corpus)
    if len(passages) != expected["passage_count"]:
        raise RuntimeError("P3 corpus count does not match its manifest")
    write_json(
        Path(os.environ["P6_PAPER_CATALOG_PATH"]),
        {p.paper_id: p.title for p in passages},
    )
    questions_path = RUNTIME / "sample-questions.jsonl"
    git_blob(
        revision,
        "data/processed/annotation_pilot_four_v3/questions.jsonl",
        questions_path,
    )
    questions = [
        json.loads(line)
        for line in questions_path.read_text().splitlines()
        if line.strip()
    ]
    paper_ids = {p.paper_id for p in passages}
    if not questions or any(q["paper_id"] not in paper_ids for q in questions):
        raise RuntimeError("Development samples do not match the corpus")
    write_json(
        RUNTIME / "data-source.json",
        {
            "schema_version": "v0-proposed",
            "p3_commit": revision,
            "corpus_sha256": digest,
            "passages": len(passages),
            "papers": len(paper_ids),
            "sample_source": "annotation_pilot_four_v3/questions.jsonl",
        },
    )
    print(
        f"Verified {len(passages)} passages / {len(paper_ids)} papers from P3 {revision}",
        flush=True,
    )
    index = Path(os.environ["PAPERGAP_DENSE_INDEX"])
    if not (index / "metadata.json").exists():
        print("Building matching 365/40 dense index (first run only)...", flush=True)
        build_indexes(
            corpus,
            index,
            device=os.environ["P6_INDEX_DEVICE"],
            cache_folder=os.environ["DEMO_AGENT_CACHE_FOLDER"],
        )
    else:
        from scripts.demo_p1 import _check_same_passages

        _check_same_passages(index, passages)
    print(
        "Preparing five hybrid-retrieval demo inputs (reranker="
        + os.environ["DEMO_AGENT_BGE"]
        + ")...",
        flush=True,
    )
    retriever = make_retriever(passages, offline=False)
    records = []
    for q in questions:
        hits = retriever(q["question"], q["paper_id"], int(os.environ["P6_TOP_K"]))
        records.append(
            {
                **q,
                "retrieval_round": 1,
                "retrieved_passages": [h.model_dump(mode="json") for h in hits],
            }
        )
    records_path = Path(os.environ["P5_RECORDS_PATH"])
    records_path.parent.mkdir(parents=True, exist_ok=True)
    records_path.write_text(
        "".join(json.dumps(r) + "\n" for r in records), encoding="utf-8"
    )
    lines = [
        "# Development questions for UI testing",
        "",
        "These five questions were already used in P3's development pilot; do not report them as held-out.",
        "",
    ]
    for n, q in enumerate(questions, 1):
        title = next(p.title for p in passages if p.paper_id == q["paper_id"])
        lines += [
            f"{n}. **{title}**",
            f"   Paper ID: `{q['paper_id']}`",
            f"   Question: {q['question']}",
            "",
        ]
    (RUNTIME / "SAMPLE_QUESTIONS.md").write_text("\n".join(lines), encoding="utf-8")
    packages = subprocess.check_output(
        [sys.executable, "-m", "pip", "freeze"], text=True
    )
    (RUNTIME / "packages.txt").write_text(packages)
    print("Setup complete. Run: ./scripts/p6-local.sh start", flush=True)


def make_retriever(passages, offline=None):
    from scripts.build_indexes import PINNED_REVISION
    from scripts.demo_hybrid import RERANKER_REVISION
    from scripts.demo_p1 import _check_same_passages
    from src.retrieval.bm25_retriever import BM25Retriever
    from src.retrieval.corpus_hybrid import CorpusHybridRetriever
    from src.retrieval.dense_retriever import DenseRetriever
    from src.retrieval.reranker import BGEReranker

    index = Path(os.environ["PAPERGAP_DENSE_INDEX"])
    _check_same_passages(index, passages)
    local_only = os.environ["DEMO_AGENT_OFFLINE"] == "1" if offline is None else offline
    dense = DenseRetriever.load(
        index,
        revision=PINNED_REVISION,
        device=os.environ["DEMO_AGENT_DEVICE"],
        cache_folder=os.environ["DEMO_AGENT_CACHE_FOLDER"],
        local_files_only=local_only,
    )
    scorer = (
        BGEReranker(
            revision=RERANKER_REVISION,
            device=os.environ["DEMO_AGENT_DEVICE"],
            cache_folder=os.environ["DEMO_AGENT_CACHE_FOLDER"],
            local_files_only=local_only,
        )
        if os.environ["DEMO_AGENT_BGE"] == "1"
        else None
    )
    return CorpusHybridRetriever(
        BM25Retriever(passages),
        dense,
        scorer=scorer,
        candidate_k=int(os.environ["DEMO_AGENT_CANDIDATE_K"]),
    ).retrieve


def make_generator():
    if os.environ["P6_BACKEND"] == "ollama":
        from src.generation.generators.ollama_backend import OllamaGenerator

        return OllamaGenerator(
            model_id=os.environ["P6_MODEL"],
            base_url=os.environ["P6_OLLAMA_BASE"],
            timeout=os.environ["P5_ANSWER_TIMEOUT"],
            num_ctx=int(os.environ["P6_OLLAMA_CONTEXT"]),
            max_new_tokens=int(os.environ["P6_MAX_NEW_TOKENS"]),
        )
    from src.generation.generators import get_generator

    if os.environ["P6_BACKEND"] == "mock":
        return get_generator("mock")
    if os.environ["P6_BACKEND"] == "vllm":
        return get_generator(
            "vllm",
            model_id=os.environ["P6_MODEL"],
            max_new_tokens=int(os.environ["P6_MAX_NEW_TOKENS"]),
        )
    raise ValueError("P6_BACKEND must be ollama, mock or vllm")


def serve():
    import uvicorn

    from scripts.build_indexes import load_passages
    from src.agent.demo import make_record_fn
    from src.agent.qwen_client import GeneratorChatClient
    from src.agent.sections import make_section_selector
    from src.generation.pipeline import GroundedQAPipeline
    from src.generation.server import create_app, load_passage_index

    corpus = Path(os.environ["PAPERGAP_CORPUS"])
    passages = load_passages(corpus)
    generator = make_generator()
    generator.load()
    retriever = make_retriever(passages)
    options = {}
    if os.environ["P6_PIPELINE"] == "adaptive":
        options["record_fn"] = make_record_fn(
            retriever,
            GeneratorChatClient(generator),
            max_retries=int(os.environ["DEMO_AGENT_MAX_RETRIES"]),
            default_top_k=int(os.environ["P6_TOP_K"]),
            section_selector=make_section_selector(passages)
            if os.environ["DEMO_AGENT_SCOPED"] == "1"
            else None,
        )
    elif os.environ["P6_PIPELINE"] == "static":
        options["retriever"] = lambda q, p, k: [
            h.model_dump(mode="json") for h in retriever(q, p, k)
        ]
    else:
        raise ValueError("P6_PIPELINE must be adaptive or static")
    app = create_app(
        GroundedQAPipeline(generator),
        **options,
        allow_corpus=True,
        papers=sorted({p.paper_id for p in passages}),
        passages=load_passage_index(corpus),
        top_k=int(os.environ["P6_TOP_K"]),
        token=os.environ["P5_API_TOKEN"] or None,
    )
    write_json(
        RUNTIME / "runtime.json",
        {
            "source_commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], text=True
            ).strip(),
            "source_status": subprocess.check_output(
                ["git", "status", "--short"], text=True
            ),
            "source_sha256": {
                str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                for directory in (ROOT / "src", ROOT / "scripts")
                for p in directory.rglob("*.py")
            },
            "generator": generator.info(),
            "pipeline": os.environ["P6_PIPELINE"],
            "corpus": str(corpus),
            "dense_index": os.environ["PAPERGAP_DENSE_INDEX"],
            "retrieval": {
                k: os.environ[k]
                for k in (
                    "DEMO_AGENT_BGE",
                    "DEMO_AGENT_DEVICE",
                    "DEMO_AGENT_SCOPED",
                    "DEMO_AGENT_MAX_RETRIES",
                    "DEMO_AGENT_CANDIDATE_K",
                    "P6_TOP_K",
                )
            },
        },
    )
    host = os.environ["P6_API_HOST"]
    if host not in ("127.0.0.1", "localhost") and not os.environ["P5_API_TOKEN"]:
        raise ValueError("Non-loopback API requires P5_API_TOKEN")
    uvicorn.run(app, host=host, port=int(os.environ["P6_API_PORT"]))


def ui():
    os.execv(
        sys.executable,
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "src/ui/app.py",
            "--server.address",
            "127.0.0.1",
            "--server.port",
            os.environ["P6_UI_PORT"],
        ],
    )


def port_free(port):
    with socket.socket() as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", int(port)))


def start(remote=False):
    import requests

    port_free(os.environ["P6_UI_PORT"])
    children = []
    handles = []
    try:
        if not remote:
            port_free(os.environ["P6_API_PORT"])
            handle = (RUNTIME / "api.log").open("a")
            handles.append(handle)
            children.append(
                subprocess.Popen(
                    [sys.executable, "-u", "-m", "scripts.p6_local", "serve"],
                    stdout=handle,
                    stderr=subprocess.STDOUT,
                )
            )
        deadline = time.monotonic() + 240
        while True:
            if any(c.poll() is not None for c in children):
                raise RuntimeError(f"API exited; see {RUNTIME / 'api.log'}")
            try:
                health = requests.get(os.environ["P5_API_BASE"] + "/health", timeout=3)
                health.raise_for_status()
                print("API ready:", health.json(), flush=True)
                break
            except requests.RequestException:
                if time.monotonic() > deadline:
                    raise RuntimeError(
                        f"API did not become ready; see {RUNTIME / 'api.log'}"
                    )
                time.sleep(1)
        children.append(
            subprocess.Popen([sys.executable, "-m", "scripts.p6_local", "ui"])
        )
        print(
            f"Open http://127.0.0.1:{os.environ['P6_UI_PORT']} — Ctrl+C stops this launcher's processes.",
            flush=True,
        )
        while all(c.poll() is None for c in children):
            time.sleep(1)
        raise RuntimeError("A runtime process exited; inspect terminal/API log")
    finally:
        for child in children:
            if child.poll() is None:
                child.terminate()
        for child in children:
            try:
                child.wait(timeout=10)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
        for handle in handles:
            handle.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command", choices=("setup", "serve", "ui", "start", "remote", "config")
    )
    args = parser.parse_args()
    configure()
    if args.command == "config":
        for key in dotenv_keys():
            print(
                f"{key}={'<configured>' if key == 'P5_API_TOKEN' and os.environ.get(key) else os.environ.get(key, '')}"
            )
    elif args.command in ("start", "remote"):
        start(remote=args.command == "remote")
    else:
        globals()[args.command]()


def dotenv_keys():
    from dotenv import dotenv_values

    return dotenv_values(CONFIG).keys()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
