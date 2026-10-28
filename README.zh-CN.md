# PaperGap

[English](README.md) | [简体中文](README.zh-CN.md)

一个以证据缺口驱动的智能体 RAG 系统，面向 NLP 研究论文，支持自适应的跨章节问答。

**当前状态**：P3 的数据准备和分块大小评估已集成 P1/P2 的静态 BM25、稠密、混合及重排序检索。离线测试已覆盖这些路径，真实模型运行尚未验证。生成模块和用户界面尚未集成。

## 从这里开始

- [逐周执行计划](docs/EXECUTION_PLAN.md)：任务、交付物和集成检查点。
- [需求与待定事项](docs/REQUIREMENTS.md)：评分标准映射，以及第一周需要解决的决策。
- [评估协议](docs/EVALUATION.md)：标注、留出数据和实验对比。
- [贡献指南](CONTRIBUTING.md)：环境配置、分支、评审和模块分工。
- [数据与 JSONL 字段](data/README_zh-CN.md)：P3 分支上的版本化 QASPER 导出、全量 gold 参考映射及按问题隔离的标注候选池。
- [每周进度跟踪](docs/WEEKLY_TRACKER.md)：每次团队会议时更新。
- [分块大小实验](experiments/chunk_size/README.md)：使用 P1/P2 检索比较按词数分块的方案，并导出证据和可读性评审材料，默认使用 BM25。可通过 JSON 的 `retrieval` 配置块选择其他模式；模型默认离线加载。

## 团队分工

| 成员 | 姓名 | 主要职责 | 负责实验 |
| --- | --- | --- | --- |
| P1 | Junlin Yin | BM25 与稠密检索；标准检索 API | BM25 与稠密检索对比 |
| P2 | Vishakha | 混合融合与重排序 | 混合检索与重排序消融实验 |
| P3 | Jingshuai Qian | QASPER 处理、分块与段落模式 | 分块与语料统计 |
| P4 | Ananya | LangGraph 规划器、评判器与自适应检索 | 静态与自适应 RAG 对比 |
| P5 | 待定 | 生成、引用与回答 API | 问答与证据支撑 |
| P6 | 待定 | Streamlit、评估基础设施与可复现性 | RAGAS 与端到端延迟 |

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

依赖文件目前使用暂定版本范围，尚未形成经过验证的锁定文件。安装过程只下载依赖库，不下载模型权重或数据集。学校 GPU 资源可用；P5 需在配置模型前确认硬件和资源分配细节；vLLM 与 GPU 专用依赖包需另行决定。P6 应在首次成功完成全新安装后记录最终解析的依赖版本。目前尚无应用启动命令。

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
└── results/          # 共享实验指标、报告与复现记录
```

## 作业交付

已提供的截止时间：**11 月 7 日 23:59（SGT，新加坡时间）**。提交一份 PDF，包含团队信息、完整报告，以及可访问的代码和数据集／结果链接。代码与报告计划于 11 月 6 日冻结。

**团队已确认的评分标准解释**：段落分块可计入 $10,000$ 篇文档，查询与段落配对可计入 $1,000$ 条评估记录。实际语料规模与标注一致性仍需验证，详见[需求文档](docs/REQUIREMENTS.md)。
