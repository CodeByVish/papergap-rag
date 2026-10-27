> 只记录当前最新完成的工作和下一步。

最新完成：2026/10/27 完成 `TODO.md` 的 `2.3`，已勾选。默认 `bm25` 在真实 QASPER 数据上通过配置解析、完整比较 CLI、报告导出和 `summarize` 验证。当前分支为 `p3-qasper-foundation`，实际代码提交为 `a67458ac5f9d808cbf2c481f34d391ca21ac8446`，运行 manifest 记录工作区干净；旧交接中的未提交整合状态已过时。本次未修改源代码、提交或推送。

使用项目环境 `D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe`，Python $3.11.16$、`rank-bm25==0.2.2`。先独立核验已有导出：$1,585$ 篇论文、$5,049$ 道问题、$7,993$ 份答案标注，结构、关联和哈希检查通过。实验仅用原始 `train/validation` 建候选及索引；排除 $1,451$ 道 held-out 问题、$955$ 道无可用文本证据问题、$3$ 道论文未出现在全部候选语料的问题，可用池为 $2,640$ 道。没有人工查看 held-out 监督文本。

临时配置 `tmp/tmp_chunk_smoke_bm25.json` 复制默认配置，仅将问题数改为 $3$、可读性原文数改为 $2$；比较 $150/200/250$ words、重叠 $40$ words、top-$5$，种子仍为 $42/43$。正式配置 `experiments/chunk_size/config.json` 未改动。复现命令如下，重跑比较时必须更换 run ID：

```powershell
& 'D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe' -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
& 'D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe' -m scripts.evaluate_chunk_size run --config tmp/tmp_chunk_smoke_bm25.json --run-id smoke_p1_bm25_01
& 'D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe' -m scripts.evaluate_chunk_size summarize --run-dir results/chunk_size/smoke_p1_bm25_01
```

产物保留在 `results/chunk_size/smoke_p1_bm25_01/`：根目录有完成标志 `manifest.json` 和 `summary.json`；每个 `chunk_size_<size>/` 下均有 `evidence_review.md`、`readability.md`。实际检索器为 P1/P2 适配中的真实 P1 BM25，dense 和 reranker 均关闭。三种大小使用相同的 $3$ 道问题和 $2$ 处原文位置；为全部 development/validation 论文建库。

| Chunk words | 语料 passage 数 | Evidence Hit@$5$ | Complete evidence rate@$5$ | 平均检索词数 | 可读性待评 chunk 数 |
| --- | --- | --- | --- | --- | --- |
| $150$ | $42,145$ | $2/3$ | $2/3$ | $700.33$ | $4$ |
| $200$ | $32,073$ | $3/3$ | $2/3$ | $867.00$ | $3$ |
| $250$ | $26,883$ | $3/3$ | $2/3$ | $1,011.33$ | $3$ |

独立产物检查脚本为 `tmp/tmp_verify_chunk_smoke.ps1`；使用 `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tmp/tmp_verify_chunk_smoke.ps1` 执行通过，仅在该进程绕过本机脚本执行策略，未更改系统策略。检查实际输入哈希、配置、检索器身份、共同问题与原文位置、每题报告布尔值、检索 ID、逐 chunk 词数和汇总分子／分母一致。`summarize` 成功后所有人工结果仍为 `pending`，可读性通过率仍为 `null`。临时配置与检查脚本已从磁盘复读。

本次指标只用于检查流水线，不能据此选择最优大小；没有执行正式评估或人工可读性评分。真实 dense／hybrid／hybrid_rerank 权重、设备及 tokenizer 截断仍未验证；若正式选择其中任一模式，必须先完成该模式的真实试跑，不能套用本次 BM25 验证结论。共享接口、split policy 和输出仍为 `v0-proposed`。生成数据、结果和 `tmp/` 均保持 Git 忽略。用户已确认将 Week 3 四份文档作为共享内容提交；`weekly-work/` 的整体忽略规则已移除，个人笔记仍应留在本地。

下一步执行 `2.4`：确认并固定正式检索模式及参数，使用正式样本量和新 run ID 运行，完成人工可读性评审后汇总。若继续 BM25，可使用当前默认配置；若更换模式，先按 `INTEGRATION_PLAN.md` 第三阶段准备固定 SHA 权重并完成真实模型试跑与截断观察。代码整合来源和接口约定仍见 `INTEGRATION_PLAN.md`，评估定义及输出格式见 `experiments/chunk_size/criteria.md` 和中文版。
