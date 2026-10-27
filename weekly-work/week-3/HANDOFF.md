> 只记录当前最新完成的工作和下一步。

最新完成：2026/10/28 执行 `TODO.md` 的 $2.4.2.1$（Round 1），将 `experiments/chunk_size/config.json` 改为 $100/200/400$ words/chunk，使用项目环境 `D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe` 重新运行全部三组，未复用旧结果。命令为 `python -m scripts.evaluate_chunk_size run --run-id round1_bm25_20261028_01`。固定重叠 $40$ words、BM25、`top_k=5`、$50$ 个问题、$5$ 篇论文各 $2$ 个段落、`seed=42`；候选依据及本轮范围已同步中英文 criteria 和实验 README。

结果保存于 `results/chunk_size/round1_bm25_20261028_01/`：`manifest.json`、`summary.json`，以及每个 `chunk_size_<size>/` 下的 `evidence_review.md`、`readability.md`。完成标记 `manifest.json` 记录配置、代码提交、运行时工作区状态、输入哈希、依赖、硬件、抽样及检索设置。运行时有配置和文档修改，未修改运行代码；生成结果与 `tmp/` 均保持 Git 忽略。

| Words/chunk | Evidence Hit@5 | 完整证据率@5 | 平均检索词数 | 语料 chunk 数 | 待审核 chunk 数 |
| --- | --- | --- | --- | --- | --- |
| $100$ | $15/50=30\%$ | $12/50=24\%$ | $469.16$ | $69344$ | $24$ |
| $200$ | $25/50=50\%$ | $20/50=40\%$ | $832.88$ | $32073$ | $13$ |
| $400$ | $30/50=60\%$ | $26/50=52\%$ | $1332.72$ | $20490$ | $11$ |

问题筛选：总计 $5049$ 个问题，排除原始 `test` 的 $1451$ 个、论文不在所有候选语料中的 $3$ 个、任一答案标注证据不合格的 $1129$ 个；合格池 $2466$ 个，实际抽取 $50$ 个，三组问题及顺序一致。每份答案标注均须具有非空、全部可唯一定位的文字证据；完整证据指标要求完整覆盖至少一份标注。原始导出核验与留出策略见 `data/README.md`，本轮不使用原始 `test` 调参。

粗筛仅使用定量检索结果；可读性样本已导出，实际覆盖 $5$ 篇论文、$10$ 个原文段落，共 $48$ 个唯一分块待审核。以 $150$ words 为界，短段落 $8$ 个、长段落 $2$ 个；覆盖偏短，未自动重抽。全部可读性标签保持 `pending`，通过率为 `null`。$400$ words 的证据覆盖最高，平均检索词数也最高；本轮固定 top-$5$ 而非固定文字预算，尚未确定最优值，也未执行 Round 2 或最终可读性评估。

旧实验作废：按用户本次指示，此前无充分依据的 $150/200/250$ 比较全部退出选值，包括旧 $200$ words 结果。`results/chunk_size/formal_bm25_20261028_01/` 和 `results/chunk_size/smoke_p1_bm25_01/` 均已添加 `INVALIDATED.md`；保留原始产物只供追溯，不合并、不复用其指标。旧 manifest 与 summary 保持原样。

验证：正式运行和 `python -m scripts.evaluate_chunk_size summarize --run-dir results/chunk_size/round1_bm25_20261028_01` 均正常退出。`tmp/tmp_verify_round1.ps1` 独立核验全部输入 SHA-256、三组配置及控制量、三组问题与顺序、每组 $50$ 个问题报告、所需文件非空、逐问题指标与汇总分子分母一致、待审核数与 `null` 通过率，全部通过。PowerShell 默认脚本策略阻止直接执行核验脚本，改用进程级 `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tmp/tmp_verify_round1.ps1` 完成，未修改系统策略。本次未改代码、未重复运行测试套件，未提交或推送。

下一步：执行 `TODO.md` 的 $2.4.2.2$，根据本轮证据覆盖和检索词数确定 Round 2，每个候选值说明理由；若扩展或细化 $400$ words 端点，不能据本轮宣称其为全局最优。完整结果评估及简洁 `report.md` 仍属于待完成的 $2.4.3$。最终定版前再完成可读性审核；评审人员、大小可见性及分歧约定见中英文 criteria。共享接口、split policy 和输出仍为 `v0-proposed`；本轮只运行 BM25，真实 dense / hybrid / reranker 模型及截断检查尚未执行。整合来源及固定 SHA、可选模型准备见 `INTEGRATION_PLAN.md` 和 `experiments/chunk_size/README.md`。
