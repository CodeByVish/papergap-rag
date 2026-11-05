# PaperGap

[English](README.md) | [简体中文](README.zh-CN.md)

一个以证据缺口驱动的智能体 RAG 系统，面向 NLP 研究论文，支持自适应的跨章节问答。

**当前状态**：P1/P2 真实数据检索与评估工具、P4 智能体组件、P5 v7 生成及 R4 重排输入、Streamlit UI 已提供。P5 已报告训练集集成示例的 Qwen 测量；P4 评判器的真实 Qwen 验证、最终留出评估和完整共享流程验收仍待完成。详见 [P1 实验](docs/P1_WEEK3_WEEK4.md)、[P2 交接](docs/P2_STATUS.md)、[P5 第六周](docs/P5_WEEK6.md)和[进度跟踪](docs/WEEKLY_TRACKER.md)。

P3 已交付 $365/40$ 词数分块语料、gold 映射、论文目录及覆盖 $200$ 题、$1853$ 条唯一配对的四算法共同池。两套标签均已填写并交接 P6；填写完整不能证明独立标注、一致率、裁决或最终评估完成。详见[第三周报告](weekly-work/week-3/week-3-report-zn.md)和[第四周报告](weekly-work/week-4/week-4-report-zn-CN.md)。模式仍为 `v0-proposed`。

## 从这里开始

- [逐周执行计划](docs/EXECUTION_PLAN.md)：任务、交付物和集成检查点。
- [需求与待定事项](docs/REQUIREMENTS.md)：评分标准映射，以及第一周需要解决的决策。
- [评估协议](docs/EVALUATION.md)：标注、留出数据和实验对比。
- [贡献指南](CONTRIBUTING.md)：环境配置、分支、评审和模块分工。
- [数据与 JSONL 字段](data/README_zh-CN.md)：P3 分支上的版本化 QASPER 导出、全量 gold 参考映射及按问题隔离的标注候选池。
- [每周进度跟踪](docs/WEEKLY_TRACKER.md)：每次团队会议时更新。
- [P1 用题清单](docs/handoffs/P1_QUESTION_USAGE.md)：供全组留出题排除审计使用的历史开发用题记录。
- [分块大小实验](experiments/chunk_size/README.md)：使用 P1/P2 检索比较按词数分块的方案，并导出证据和可读性评审材料，默认使用 BM25。可通过 JSON 的 `retrieval` 配置块选择其他模式；模型默认离线加载。

## 团队分工

| 成员 | 姓名 | 主要职责 | 负责实验 |
| --- | --- | --- | --- |
| P1 | Junlin Yin | BM25 与稠密检索；标准检索 API | BM25 与稠密检索对比 |
| P2 | Vishakha | 混合融合与重排序 | 混合检索与重排序消融实验 |
| P3 | Jingshuai Qian | QASPER 处理、分块与段落模式 | 分块与语料统计 |
| P4 | Ananya | LangGraph 规划器、评判器与自适应检索 | 静态与自适应 RAG 对比 |
| P5 | Junyu Hu | 生成、引用与回答 API（v7/R4 已集成） | 问答与证据支撑 |
| P6 | Changyan Xu | Streamlit、评估基础设施与可复现性 | RAGAS 与端到端延迟 |

每位成员均需参与标注、撰写各自的报告部分、验证自己的模块，并评审另一位成员的工作。P6 协调集成；各模块提供者负责自己的接口和集成修复。

## 计划中的处理流程

选定论文与问题 → BM25 和稠密检索 → RRF → 重排序 → 证据评判器 → 必要时进行定向检索 → 基于证据回答或拒答 → 引用校验 → Streamlit。

最多执行一次初始检索和两次重试。可选的双评判器和 NLI 将在必需的流程与评估工作完成后再考虑。

## 本地环境配置

初始环境使用 Python 3.11。在克隆后的 `papergap-rag` 目录中运行以下命令：

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Windows 激活命令：`.venv\Scripts\activate`。

依赖文件目前使用暂定版本范围，尚未形成经过验证的锁定文件。安装过程只下载依赖库，不下载模型权重或数据集。学校 GPU 资源可用；P5 需在配置模型前确认硬件和资源分配细节；vLLM 与 GPU 专用依赖包需另行决定。P6 应在首次成功完成全新安装后记录最终解析的依赖版本。使用 `python -m streamlit run src/ui/app.py` 启动 UI，详见 [UI 配置与用法](src/ui/README.md)。

UI 当前使用 `IndexedRetriever` 和直接 LLM 客户端；接入共享 P1/P2 检索、P4 编排与 P5 `GroundedQAPipeline` 后仍需集成验收。

以下检索接口、命令、历史证据及限制与英文版同步保留；详细模块记录见各节链接。

## P1 retrieval: Week 1 / Week 2

Use Python 3.11 with the dependencies from `requirements-dev.txt` installed as described above. For an existing Conda environment, run `conda activate papergap` and check `python --version`; a VS Code interpreter selection does not change every terminal's Python. Run all commands below from the repository root.

`BM25Retriever` and `DenseRetriever` share this interface:

```python
retrieve(query: str, paper_id: str, top_k: int) -> list[RetrievalHit]
```

Both use the existing `Passage` and `RetrievalHit` schemas. Results preserve the original Passage fields and IDs, use continuous ranks starting at 1, and contain at most K distinct passages from the selected paper. Unknown papers return `[]`; invalid queries, paper IDs and K values raise `ValueError`. Each paper has its own index, so retrieval selects the top K within that paper. Equal scores are ordered by passage ID.

Dense retrieval uses `BAAI/bge-small-en-v1.5`. The commands below pin revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` and default to CPU. Only queries receive `Represent this sentence for searching relevant passages: `, including the trailing space; passages use their original text. Both embedding types receive L2 normalization, and FAISS `IndexFlatIP` computes cosine similarity. This embedding model is separate from P2's `BAAI/bge-reranker-base` cross-encoder.

Build the dense index from an explicit Passage JSONL input:

```bash
python -B -m scripts.build_indexes --passages tests/fixtures/mock_passages.jsonl --output-dir indexes/p1-week2-synthetic --local-files-only
```

The output directory must be new or empty. The saved artifacts contain the per-paper FAISS indexes, complete row-to-Passage mappings, and checked model/encoding metadata; loading them does not re-encode passages. BM25 is built in memory from the JSONL input and is not persisted by this command. `--model-name` accepts only the selected BGE model; `--revision`, `--device` and `--cache-folder` are available when an explicit setting is needed. `--revision` must be a 40-character lowercase commit SHA; branch and tag names such as `main` are rejected. Use the same revision when building and loading. The default model cache is `.cache/huggingface`. `--local-files-only` requires the pinned model to be cached; omit it to allow a first model download.

Run a sample query against BM25 and the saved dense index:

```bash
python -B -m scripts.demo_p1 --passages tests/fixtures/mock_passages.jsonl --dense-index-dir indexes/p1-week2-synthetic --paper-id synthetic-ir --query "Which method uses sparse term matching for passage retrieval?" --top-k 3 --local-files-only
```

Without `--dense-index-dir`, the demo builds dense indexes in memory from the supplied JSONL. The demo reports both rankings and times `retrieve` with `time.perf_counter` after one warm-up call per retriever. Loading, passage encoding and index construction are excluded; dense query encoding is included. The bundled fixture has eight synthetic passages across two papers. These timings are only a local smoke measurement, not real-corpus performance results.

Run the offline regression tests with the same Python 3.11 interpreter:

```bash
python -B -m pytest tests/test_p1.py -v
python -B -m pytest -q
```

Dense unit tests use deterministic fake encoders with real FAISS and do not download models. A real SentenceTransformer run is a separate check. See the [Week 1/2 verification record](docs/WEEKLY_TRACKER.md#p1-verification-evidence) for historical synthetic runs, the Week 3/4 workflow below for P1 real-corpus experiments, and the [P2 real-data handoff](docs/P2_WEEK2.md) for Hybrid/reranking evidence. Retrieval quality metrics remain pending compatible gold mappings and the agreed P6 evaluation protocol; P1/P2 metric tooling is available. Track the agreed QASPER raw/processed artifacts and manifests under `data/` following the bilingual data guides. Keep model weights, caches, indexes and large local outputs ignored; review shared results under `results/README.md`.

## P1 retrieval: Week 3 / Week 4

The real-data workflow and reproducible PowerShell commands are documented in
[P1 Week 3 / Week 4](docs/P1_WEEK3_WEEK4.md). It runs P3's pinned data preparation
in a separate worktree and validates its Passage JSONL and manifests before
using the existing P1 retrievers. The recorded development convention indexes
train plus validation paper text and queries **train only**; the split policy
remains `v0-proposed`.

`python -B -m scripts.run_p1_experiment --help` describes the experiment entry
point. It loads the saved Dense index, saves/reloads a reproducible BM25 JSON
snapshot, verifies both complete Passage mappings, and writes `results.jsonl`,
`queries.jsonl` and `run.json` to a new or empty output directory. `--limit`
limits queries only; the full corpus remains indexed. Zero-hit questions are
retained. The run records input hashes, model revision, code state, source
hashes and retrieval latency. BM25 loading rebuilds its in-memory term index;
Dense loading reuses the stored passage vectors without re-encoding them.
The `evaluate` subcommand audits saved rankings and adapts independently supplied
labels; see the [provisional evaluation contract](docs/P1_EVALUATION.md).

The original `retrieve(query, paper_id, top_k)` callback remains supported.
Both independent retrievers also accept keyword-only `section="Results"`
with exact matching before top-K selection. Callers can supply a rewritten
query directly. Merged P2 Hybrid retrieval forwards exact sections to both
callbacks, and the P4 graph accepts a caller-supplied section selector. P4 still
owns the per-paper selector and same-round unscoped fallback. The historical
P1 integration checks used fixed request bindings; they do not establish
dynamic section selection. See [section interfaces](docs/P2_AGENT_CACHE.md).

P1 saved-ranking scoring and P2 retrieval evaluation/pooling tools are
available. Compatible gold evidence-to-passage mappings, relevance rules and
the approved held-out/configuration freeze remain external inputs. This
workflow exports real retrieval candidates and latency; quality metrics remain
unavailable until those inputs are supplied. See the [P2 evaluation handoff](docs/P2_EVALUATION_HANDOFF.md)
and the linked P1 verification record for scope and limitations.

The Week 3/4 delivery branch includes main's merged P2 and P4 APIs.
`python -B -m scripts.run_p1_integration --help` describes the bounded integration
check using existing artifacts and fixed request sections. It does not establish
dynamic section selection or real critic quality. The [18 October integration](docs/P1_WEEK3_WEEK4.md#main-integration-after-p2-merge-18-october-2026)
records historical execution. The [28 October checkpoint](docs/WEEKLY_TRACKER.md#p1-question-usage-handoff-and-main-sync-28-october-2026)
records the question-use handoff; see the [29 October checkpoint](docs/WEEKLY_TRACKER.md#p1-main-sync-after-ui-and-generation-merge-29-october-2026)
for the current branch refresh and validation.

## P2 real-data Hybrid and reranking

`python -B -m scripts.demo_hybrid --help` is now available from main. The CLI
loads the supplied Passage JSONL and saved Dense index, checks their mapping,
and runs RRF; `--bge` enables optional BGE reranking. See [P2 commands, model
revisions and measured pilot](docs/P2_WEEK2.md) for inputs, offline cache controls
and `scripts.benchmark_p2`. Use dependencies appropriate to your platform;
the documented macOS ARM64 lock and repair procedure are platform-specific.

P1's 100-question handoff remains RRF-only with null reranker fields. P2's later
independent reranked export is recorded separately and does not change the P1
package's provenance or establish a retrieval-quality gain. See the [separate
artifact records](docs/P1_WEEK3_WEEK4.md#separate-p1-and-p2-artifacts).

## 仓库结构

```text
papergap-rag/
├── docs/             # 计划、需求、评估与团队进度跟踪
├── configs/          # 拟议的共享配置
├── src/
│   ├── data/         # P3：数据准备
│   ├── retrieval/    # P1/P2：检索器、融合与重排序
│   ├── agent/        # P4：规划与自适应检索
│   ├── generation/   # P5：生成与引用校验
│   ├── evaluation/   # P6 与实验负责人：指标与日志
│   └── ui/           # P6：Streamlit
├── scripts/          # 可复现的命令行入口
├── tests/            # 模块与集成测试
├── data/             # 纳入 Git 的 QASPER 数据、manifest 与双语指南
├── results/          # 审核后的分块实验结果；其他本地输出忽略
├── experiments/     # 分块选择与复现入口
└── weekly-work/     # 仅共享已发布双语报告
```

## 作业交付

已提供的截止时间：**11 月 7 日 23:59（SGT，新加坡时间）**。提交一份 PDF，包含团队信息、完整报告，以及可访问的代码和数据集／结果链接。代码与报告计划于 11 月 6 日冻结。

**团队已确认的评分标准解释**：段落分块可计入 $10,000$ 篇文档，查询与段落配对可计入 $1,000$ 条评估记录。实际语料规模与标注一致性仍需验证，详见[需求文档](docs/REQUIREMENTS.md)。
