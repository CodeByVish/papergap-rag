> 只记录当前最新完成的工作和下一步。

最新完成：2026/10/28 已执行 `TODO.md` 的 $2.4.2.2$（Round 2），结果位于 `results/chunk_size/round2_bm25_20261028_01/`。使用项目环境 `D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe` 执行 `python -m scripts.evaluate_chunk_size run --run-id round2_bm25_20261028_01`，重新构建全部 $9$ 组分块和 BM25 排序，未复用旧指标；运行时工作区干净，代码提交为 `4a3023646848474d0e86dc3d388326ac5a2c294e`。

配置：$200/225/250/275/300/325/350/375/400$ words/chunk、重叠 $40$ words、`top_k=5`、$50$ 个问题、$5$ 篇论文各 $2$ 个可读性段落、`seed=42`；同时完成 top-$5$ 与固定 $500/1000/2000$ words 预算比较。范围及取点依据、控制量和选值规则见中英文 criteria；历史设置以各轮 `manifest.json` 为准。

有效 Round 1 对照为 `results/chunk_size/round1_bm25_20261028_02/`。执行前已用全部候选核验论文交集、输入数据哈希、配置控制量、问题 ID 及顺序、筛选统计和可读性原文位置；执行后核验共享 `questions.jsonl` 字节一致，$200/400$ 两组的语料哈希、保存排序、可读性文件及全部逐问题和汇总结果一致（排除耗时）。两轮使用同一批 $50$ 个问题；合格池 $2466$ 个，不使用原始 `test` 调参。留出策略见 `data/README.md`。

已保存共享 `manifest.json`、`summary.json`、`summary.html`、`questions.jsonl`，每个 `chunk_size_<size>/` 下包含 `ranked_chunks.jsonl`、`evidence_review.md`、`readability.md`，共 $31$ 个文件。结构化输入保留证据位置、完整检索分块及来源映射，可独立重算指标；manifest 记录输入和结构化文件哈希、依赖、硬件、抽样、语料哈希和排序保存状态。结果供 Git 共享；原始数据、生成语料和临时脚本继续忽略，未提交或推送。

运行快照：以下列出固定预算下的最高计数，分母均为 $50$；仅供下一步定位结果，不作为最终选值或显著性结论。完整各候选指标、实际词数、耗尽数和 top-$5$ 见 `summary.html` 与 `summary.json`。

| 词数预算 | 最高证据命中率及候选 words/chunk | 最高完整证据率及候选 words/chunk |
| --- | --- | --- |
| $500$ | $19/50=38\%$，$200$ | $16/50=32\%$，$325$ |
| $1000$ | $29/50=58\%$，$325$ | $25/50=50\%$，$325$ |
| $2000$ | $40/50=80\%$，$225$ | $36/50=72\%$，$225/350/375$ |

可读性沿用 $10$ 个原文段落（短 $8$、长 $2$），全部候选合计 $104$ 个待审核分块；所有标签为 `pending`，通过率为 `null`。原文样本未重抽，尚未执行可读性审核或最终配置冻结。

验证：`tmp/tmp_preflight_round2.py` 在正式检索前核验跨轮输入、全部候选的论文交集和抽样；正式 `run`、`regenerate` 结构化重算、`summarize` 均正常退出。`tmp/tmp_verify_round2.py` 在初次运行及重算汇总后均通过，覆盖输入与结构化文件 SHA-256、全部输出非空、共享问题及顺序、逐问题与汇总指标、预算词数约束、预算增大时覆盖不下降、待审核状态，以及 $200/400$ 两组跨轮精确一致性。未修改运行代码。

作废实验继续排除：旧 Round 1 的 `results/chunk_size/round1_bm25_20261028_01/INVALIDATED.md` 保留替代路径；此前 $150/200/250$ 的 `formal_bm25_20261028_01/` 与 `smoke_p1_bm25_01/` 作废状态继续有效。不得将其指标参与选值或合并。

下一步：执行 `TODO.md` 的 $2.4.3$，结合有效 Round 1 与本轮的固定预算结果和逐问题得失，在 `results/chunk_size/round2_bm25_20261028_01/report.md` 保存简洁评估。每题对应 $2$ 个百分点，小差异不直接宣布胜出；各预算优胜者不同则保留成本与覆盖的取舍。按 criteria 判断是否需向区间外补测；最终定版前完成可读性审核。共享接口、split policy 和输出仍为 `v0-proposed`；本轮仅使用 BM25，真实 dense / hybrid / reranker 模型及截断检查尚未执行。整合来源见 `INTEGRATION_PLAN.md`，配置及重算命令见 `experiments/chunk_size/README.md`。
