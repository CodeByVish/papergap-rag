# PaperRAG Streamlit Application — Implementation Plan

**Goal:** A Streamlit app for questions about NLP papers. It retrieves evidence from PaperRAG, sends that evidence to a configurable LLM API, and shows the answer with inspectable sources.

**V1 design:** one Streamlit app, prebuilt BM25 and FAISS indexes, one LLM provider initially. Build the corpus and indexes offline; never rebuild all papers during app startup.

**Implementation in this repository:** the entry point is `src/ui/app.py` and
UI resource/configuration helpers are in `src/ui/services.py`. The sample
`paperrag/` backend modules below map to `src/retrieval/indexed_retriever.py`
and `src/generation/{prompting,llm_client}.py`; the index adapter reuses the
existing RRF implementation. See [UI setup and usage](README.md) for the runnable
commands, optional index dependencies, and current Python/Java guidance.
The implemented baseline searches the whole corpus; strict paper/year filters,
reranking, and the adaptive agent loop remain future integrations.

## Contents

- [Requirements](#requirements)
- [Architecture](#architecture)
- [UI](#ui)
- [Repository and setup](#repo)
- [Index contract](#contract)
- [Offline index build](#build)
- [Hybrid retrieval code](#retrieval)
- [Prompting and LLM adapters](#llm)
- [Streamlit app code](#app)
- [Testing](#testing)
- [Hosting](#hosting)
- [Risks and decisions](#risks)

<a id="requirements"></a>
## 1. Requirements

Users can ask about one paper or compare papers, optionally choose a configured model and evidence count, receive an evidence-grounded answer, and inspect cited passages with paper title, section, page, and ACL Anthology link.

Example questions:
- What problem does this paper address, what method does it propose, and how is it evaluated?
- What limitations do the authors identify, and which passages support them?
- Compare the datasets and baselines used in these two papers.

V1 excludes arbitrary PDF uploads, in-app corpus rebuilding, persistent chat history, visual-only figure retrieval, and complex agent loops.

Acceptance criteria:
- Query searches sparse and dense indexes, then fuses the rankings.
- Retrieved evidence is placed in the LLM prompt.
- Sources shown correspond to retrieved chunks.
- Empty retrieval, missing credentials, and API failures have clear UI messages.
- Evaluation questions and gold answers are not in the index.

<a id="architecture"></a>
## 2. Architecture

~~~mermaid
flowchart TD
  U["User question"] --> UI["Streamlit UI"]
  UI --> R["PaperRAG retriever"]
  R --> B["BM25 / Pyserini"]
  R --> D["Dense / FAISS"]
  B --> F["RRF fusion"]
  D --> F
  F --> X["Optional reranker"]
  X --> E["Evidence passages"]
  E --> P["Prompt builder"]
  P --> L["Qwen / Grok API"]
  L --> C["Citation check"]
  C --> UI
  UI --> S["Source cards"]
~~~

The LLM is the answer generator. The PaperRAG retriever searches your corpus first; the app sends the question plus retrieved passages to the LLM.

<a id="ui"></a>
## 3. UI design

~~~text
┌──────────────────────────── PaperRAG ─────────────────────────────┐
│ Ask questions about NLP papers and inspect supporting evidence.    │
├───────────────────────┬──────────────────────────────────────────┤
│ Settings              │ Question                                 │
│ Provider: Qwen / Grok │ [ What limitation do authors identify? ] │
│ Model: configured     │ [ Ask ]                                   │
│ Evidence count: 5     │ Answer with [E1], [E2] citations         │
│ Paper/year filter     │ ▼ Sources: paper · section · page         │
│                       │ Evidence passage · Open ACL paper          │
└───────────────────────┴──────────────────────────────────────────┘
~~~

Keep the UI simple. Put diagnostics in a collapsed expander. Show provider, number of passages, latency, evidence text, and clickable source links. Do not expose API keys or raw stack traces.

<a id="repo"></a>
## 4. Repository and setup

Keep the Streamlit entry point and any UI-only components, pages, or assets inside `src/ui/`. Keep retrieval, prompting, and LLM adapters in `paperrag/`. Run the commands below from the repository root; `python -m streamlit` keeps the root package importable. Paths for data, indexes, and `.streamlit/secrets.toml` remain relative to the repository root.

~~~text
paperrag/
├── src/
│   └── ui/
│       └── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/secrets.toml.example
├── paperrag/
│   ├── retrieval.py
│   ├── prompting.py
│   └── llm_client.py
├── scripts/
│   ├── export_pyserini.py
│   └── build_dense_index.py
├── data/chunks.jsonl
└── indexes/
    ├── sparse/lucene/
    └── dense/
        ├── chunks.faiss
        └── row_ids.json
~~~

.gitignore:

~~~gitignore
.streamlit/secrets.toml
.env
__pycache__/
*.py[cod]
.venv/
data/raw/
data/derived/
indexes/
~~~

Setup commands:

~~~bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
~~~

Windows PowerShell:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

Starter requirements.txt:

~~~text
streamlit
openai
sentence-transformers
faiss-cpu
pyserini
numpy
~~~

Pin the versions tested by the team before final submission. Pyserini/Lucene may require a compatible Java runtime; check its installation instructions.

~~~bash
python -m pip install -r requirements.txt
~~~

<a id="contract"></a>
## 5. Index contract

Canonical data/chunks.jsonl has one record per passage:

~~~json
{
  "chunk_id": "2026.acl-long.123__chunk_00018",
  "paper_id": "2026.acl-long.123",
  "title": "Example NLP Paper",
  "section_path": ["Experiments", "Main Results"],
  "page_start": 7,
  "page_end": 8,
  "text": "Passage text...",
  "source_url": "https://aclanthology.org/2026.acl-long.123/"
}
~~~

Dense index row_ids.json stores chunk IDs in the exact vector insertion order. Rebuild it every time the dense index is rebuilt. Pyserini records use id as chunk ID and contents as searchable passage text. Retrieval results map to the canonical chunk record.

<a id="build"></a>
## 6. Offline build commands and scripts

Build indexes before deployment, not inside the query handler.

~~~bash
python scripts/export_pyserini.py \
  --chunks data/chunks.jsonl \
  --output data/pyserini_collection

python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input data/pyserini_collection \
  --index indexes/sparse/lucene \
  --generator DefaultLuceneDocumentGenerator \
  --threads 4 \
  --storeRaw

python scripts/build_dense_index.py \
  --chunks data/chunks.jsonl \
  --output indexes/dense \
  --model sentence-transformers/all-MiniLM-L6-v2

python -m streamlit run src/ui/app.py
~~~

### scripts/export_pyserini.py

~~~python
import argparse
import json
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chunks", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()

    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)
    seen = set()
    count = 0

    with Path(a.chunks).open(encoding="utf-8") as src, \
         (out / "chunks.jsonl").open("w", encoding="utf-8") as dst:
        for line_no, line in enumerate(src, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            cid, text = row["chunk_id"], row["text"].strip()
            if not text:
                continue
            if cid in seen:
                raise ValueError(f"Duplicate chunk ID on line {line_no}: {cid}")
            seen.add(cid)
            dst.write(json.dumps(
                {"id": cid, "contents": text}, ensure_ascii=False
            ) + "\n")
            count += 1
    print(f"Wrote {count} passages")

if __name__ == "__main__":
    main()
~~~

### scripts/build_dense_index.py

~~~python
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
    (out / "config.json").write_text(json.dumps({
        "model": a.model,
        "dimension": int(vectors.shape[1]),
        "normalized": True,
        "count": len(ids)
    }, indent=2), encoding="utf-8")
    print(f"Indexed {len(ids)} chunks")

if __name__ == "__main__":
    main()
~~~

<a id="retrieval"></a>
## 7. Hybrid retrieval code

Use Reciprocal Rank Fusion (RRF). It combines ranks rather than raw BM25 and cosine scores, whose scales differ.

~~~text
RRF(d) = sum over retrievers r of 1 / (k0 + rank_r(d))
~~~

Start with k0=60 and 25 candidates from each retriever; tune using evaluation results.

### paperrag/retrieval.py

~~~python
import json
from pathlib import Path
import faiss
from pyserini.search.lucene import LuceneSearcher
from sentence_transformers import SentenceTransformer

class PaperRAGRetriever:
    def __init__(self, sparse_dir, dense_path, row_ids_path,
                 chunks_path, model_name):
        self.sparse = LuceneSearcher(sparse_dir)
        self.dense = faiss.read_index(dense_path)
        self.encoder = SentenceTransformer(model_name)
        self.row_ids = json.loads(
            Path(row_ids_path).read_text(encoding="utf-8")
        )
        self.chunks = {}
        with Path(chunks_path).open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    row = json.loads(line)
                    self.chunks[row["chunk_id"]] = row
        if self.dense.ntotal != len(self.row_ids):
            raise ValueError("FAISS count differs from row-ID mapping")

    def sparse_search(self, query, k):
        hits = self.sparse.search(query, k=k)
        return [h.docid for h in hits if h.docid in self.chunks]

    def dense_search(self, query, k):
        q = self.encoder.encode(
            [query], convert_to_numpy=True, normalize_embeddings=True
        ).astype("float32")
        scores, rows = self.dense.search(q, k)
        result = []
        for row in rows[0]:
            if row >= 0:
                cid = self.row_ids[int(row)]
                if cid in self.chunks:
                    result.append(cid)
        return result

    @staticmethod
    def rrf(sparse_ids, dense_ids, k0=60):
        scores = {}
        for ranking in (sparse_ids, dense_ids):
            for rank, cid in enumerate(ranking, start=1):
                scores[cid] = scores.get(cid, 0.0) + 1.0 / (k0 + rank)
        return sorted(scores, key=scores.get, reverse=True), scores

    def retrieve(self, query, top_k=5, candidates=25):
        s = self.sparse_search(query, candidates)
        d = self.dense_search(query, candidates)
        ranked, scores = self.rrf(s, d)
        output = []
        for cid in ranked[:top_k]:
            row = dict(self.chunks[cid])
            row["rrf_score"] = scores[cid]
            output.append(row)
        return output
~~~

Optional reranker: rerank the fused top 20–50 passages with a cross-encoder and return 5–8. Add only after evaluating the hybrid baseline.

<a id="llm"></a>
## 8. Prompting and LLM APIs

### Prompt builder: paperrag/prompting.py

~~~python
def build_messages(question, passages):
    blocks = []
    for i, row in enumerate(passages, start=1):
        row["evidence_id"] = f"E{i}"
        section = " > ".join(row.get("section_path", [])) or "Unknown section"
        page = row.get("page_start", "unknown")
        blocks.append(
            f"[E{i}] {row.get('title', row['paper_id'])}\n"
            f"Paper: {row['paper_id']} | Section: {section} | Page: {page}\n"
            f"Passage: {row['text']}\nSource: {row.get('source_url', '')}"
        )
    system = (
        "Answer about NLP papers using only supplied evidence. Cite substantive "
        "claims with IDs such as [E1]. Say when evidence is insufficient or "
        "conflicting. Never invent paper facts."
    )
    user = f"Question:\n{question}\n\nEvidence:\n\n{chr(10).join(blocks)}"
    return system, user, passages
~~~

Qwen and Grok offer OpenAI-compatible interfaces, but endpoints and request formats differ. Qwen Singapore Model Studio uses a workspace-specific endpoint and matching regional key. xAI quickstart documents https://api.x.ai/v1 and the Responses API. Verify current model access before deployment:
[Qwen quickstart](https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen) · [xAI quickstart](https://docs.x.ai/developers/quickstart)

### Secrets configuration

Create .streamlit/secrets.toml locally, add it to .gitignore, and never commit it. In Streamlit Cloud, enter secrets through deployment settings.

~~~toml
[llm.qwen]
api_key = "replace-me"
base_url = "https://YOUR_WORKSPACE_ID.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
model = "configure-current-model"

[llm.grok]
api_key = "replace-me"
base_url = "https://api.x.ai/v1"
model = "configure-current-model"

[rag]
sparse_index_dir = "indexes/sparse/lucene"
dense_index_path = "indexes/dense/chunks.faiss"
dense_row_ids_path = "indexes/dense/row_ids.json"
chunks_path = "data/chunks.jsonl"
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
~~~

### Provider adapter: paperrag/llm_client.py

~~~python
from openai import OpenAI

def generate(provider, config, system_prompt, user_prompt):
    client = OpenAI(
        api_key=config["api_key"],
        base_url=config["base_url"],
        timeout=90.0,
        max_retries=2,
    )
    model = config["model"]

    if provider == "qwen":
        result = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
        )
        return result.choices[0].message.content or ""

    if provider == "grok":
        result = client.responses.create(
            model=model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return result.output_text or ""

    raise ValueError(f"Unknown provider: {provider}")
~~~

Keep provider differences in this module. SDK compatibility does not guarantee every parameter behaves the same across providers. Streamlit secret handling: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

<a id="app"></a>
## 9. Streamlit app code

### src/ui/app.py

~~~python
import time
import streamlit as st
from paperrag.retrieval import PaperRAGRetriever
from paperrag.prompting import build_messages
from paperrag.llm_client import generate

st.set_page_config(page_title="PaperRAG", page_icon="📄", layout="wide")

@st.cache_resource
def get_retriever():
    cfg = st.secrets["rag"]
    return PaperRAGRetriever(
        cfg["sparse_index_dir"],
        cfg["dense_index_path"],
        cfg["dense_row_ids_path"],
        cfg["chunks_path"],
        cfg["embedding_model"],
    )

st.title("PaperRAG")
st.caption("Ask about NLP papers and inspect the evidence.")

with st.sidebar:
    st.header("Settings")
    provider = st.selectbox("LLM provider", ["qwen", "grok"])
    top_k = st.slider("Evidence passages", 3, 10, 5)
    diagnostics = st.toggle("Show diagnostics", value=False)

question = st.chat_input("Ask about methods, experiments, findings, or limitations")

if question:
    st.chat_message("user").write(question)
    started = time.perf_counter()
    try:
        retriever = get_retriever()
        with st.spinner("Retrieving evidence…"):
            passages = retriever.retrieve(question, top_k=top_k)

        if not passages:
            st.warning("No relevant evidence was retrieved.")
            st.stop()

        system, user, passages = build_messages(question, passages)
        with st.spinner("Generating answer…"):
            answer = generate(
                provider, dict(st.secrets["llm"][provider]), system, user
            )

        elapsed = time.perf_counter() - started
        st.chat_message("assistant").markdown(answer)
        st.caption(f"{provider} · {len(passages)} passages · {elapsed:.2f}s")

        with st.expander("Sources and evidence", expanded=True):
            for row in passages:
                eid = row.get("evidence_id", "E?")
                title = row.get("title", row["paper_id"])
                section = " › ".join(row.get("section_path", []))
                page = row.get("page_start", "unknown")
                st.markdown(f"**[{eid}] [{title}]({row.get('source_url', '')})**")
                st.caption(f"{section} · page {page} · {row['paper_id']}")
                st.write(row["text"])
                st.divider()

        if diagnostics:
            st.json({
                "provider": provider,
                "seconds": round(elapsed, 3),
                "chunk_ids": [p["chunk_id"] for p in passages],
                "rrf_scores": [p.get("rrf_score") for p in passages],
            })
    except KeyError as exc:
        st.error(f"Missing configuration: {exc}")
    except Exception as exc:
        # For a public app, log full detail on the server instead.
        st.error(f"Request failed: {type(exc).__name__}")
~~~

<a id="testing"></a>
## 10. Testing

~~~bash
python -m streamlit run src/ui/app.py
python -m compileall src/ui paperrag scripts
python -m pytest -q
~~~

Smoke-test direct wording, paraphrase, multi-section question, unsupported query, exact acronym, and missing API key. Create a fixed retrieval set with relevant chunk IDs and report Recall@K, MRR, and nDCG@K. Evaluate answer quality separately from retrieval.

<a id="hosting"></a>
## 11. Hosting

### Recommended for a course demo: GitHub repo + Streamlit Community Cloud

1. Push app code, requirements, README, and appropriately sized index assets to GitHub.
2. Keep real keys out of the repository.
3. Create a Community Cloud app from the repo and select the branch and set the main file path to `src/ui/app.py`.
4. Add API keys in deployment secrets.
5. Check startup, index load, memory use, and API connectivity.

Docs: [Streamlit deploy](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app) · [Streamlit secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)

### GitHub Pages cannot run Streamlit

GitHub repositories store code. GitHub Pages serves static HTML/CSS/JavaScript and does not run Python or a Streamlit backend. It can host a project landing page, not the RAG app. Use Streamlit Community Cloud or a container host for the Python service.
Source: [GitHub Pages docs](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

Optional Dockerfile:

~~~dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ui ./src/ui
COPY paperrag ./paperrag
COPY data ./data
COPY indexes ./indexes
EXPOSE 8501
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"
CMD ["python", "-m", "streamlit", "run", "src/ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
~~~

~~~bash
docker build -t paperrag-streamlit .
docker run --rm -p 8501:8501 paperrag-streamlit
~~~

Inject secrets through the host’s secret manager or mounted file, never inside the image. Streamlit Docker guide: https://docs.streamlit.io/deploy/tutorials/docker

Check the real host storage and memory limits before choosing it. A public demo can generate unexpected provider charges; constrain query length/evidence count and monitor usage.

<a id="risks"></a>
## 12. Risks and decisions

| Risk | Mitigation |
|---|---|
| Index too large for host | Measure disk and memory; store large artifacts separately. |
| Noisy PDF extraction | Preserve page/section metadata and inspect sample papers. |
| Unsupported model claims | Evidence-only prompt, visible evidence, unsupported-query tests, faithfulness evaluation. |
| Citation ID exists but passage does not support claim | Label validation is not entailment; assess faithfulness separately. |
| API costs or rate limits | Start with one provider, cap evidence, set billing alerts. |
| Key exposure | Server-side secrets only; never commit or send keys to browser JS. |
| Evaluation leakage | Keep questions and gold answers outside indexes. |
| External API data terms | Check provider and course rules before sending paper excerpts. |
| Unfair model comparison | Freeze corpus, queries, evidence, and generation settings. |

### Milestones

1. Agree on chunk schema and IDs.
2. Validate BM25, dense, and RRF retrieval locally.
3. Add one LLM provider and test errors.
4. Implement answer and source-card UI.
5. Evaluate on fixed retrieval and QA set.
6. Deploy and test clean startup.

### Remaining decisions

- Which provider is the initial baseline?
- Is the demo public or access-restricted?
- What are index size and hosting memory constraints?
- Are figures/tables part of v1?
- Who owns annotation, secrets, deployment, and monitoring?

## References

- [Streamlit Community Cloud deployment](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
- [Streamlit secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
- [Streamlit Docker guide](https://docs.streamlit.io/deploy/tutorials/docker)
- [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Qwen Model Studio API quickstart](https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen)
- [xAI API quickstart](https://docs.x.ai/developers/quickstart)
- [ACL Anthology data access](https://aclanthology.org/faq/api/)

Model names, pricing, endpoint formats, and hosting limits change. Verify them at deployment. Code above is a starting implementation, not a measured performance claim.


sample: https://llm-examples.streamlit.app