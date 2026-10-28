> 只记录当前最新完成的工作和下一步。

最新完成：2026/10/28 已执行 `TODO.md` 的 $2.4.2.4$（Round 4），结果位于 `results/chunk_size/round4_bm25_20261028_01/`。新增 `src/evaluation/chunk_size_validation.py`，实现旧题排除、固定题单准备／复用、三组指标、逐题得失、跨轮回归核验及简洁报告；同步中英文 criteria 和实验 README。未提交或推送，运行 manifest 如实记录代码提交及工作区修改状态。

运行方式：使用 `D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe`，先执行 `python -m scripts.evaluate_chunk_size run --run-id round4_bm25_20261028_01 --prepare-plan experiments/chunk_size/round4_question_plan.json` 冻结题单，再以 `--question-plan experiments/chunk_size/round4_question_plan.json` 替换准备参数正式检索。配置为 $325/365/375$ words、重叠 $40$ words、`top_k=5`、`seed=42`，完整比较 $500/1000/2000$ words；运行前固定新增题的 $1000$ words 完整证据率为主要指标，该预算尚非最终部署约定。

抽样：重新核验合格池 $2466$ 题，排除原有 $50$ 题后剩余 $2416$ 题；按 ID 排序后用固定种子抽取 $200$ 题，未使用 `test`。旧题／新题／合计覆盖 $48/184/224$ 篇论文，来源问题数分别为 train $37/152/189$、validation $13/48/61$；新旧论文交集 $8$ 篇，不能称为论文独立验证。题单、顺序、分组、筛选数量、来源划分及输入哈希保存在 `question_plan.json` 和 manifest 中。

新增题主要预算结果：$325/365/375$ 的证据命中率为 $123/200$、$131/200$、$131/200$，完整证据率为 $104/200$、$106/200$、$108/200$。$375$ 对 $365$ 的完整证据独有成功为 $5$ 对 $3$ 题；不能据此宣布显著或稳定最优。$500$ words 下 $325$ 的完整证据率较高，$2000$ words 下 $375$ 的完整证据率较高而 $365$ 命中率较高；保留预算取舍，不继续细搜或换种子。

已保存本轮 `manifest.json`、`question_plan.json`、`questions.jsonl`、`summary.json`、`summary.html`、`report.md`，以及三个候选各自的 `ranked_chunks.jsonl`、`evidence_review.md`、`readability.md`。结果用于 Git 共享；原始数据、生成语料、模型、索引和临时脚本不入 Git。此前作废实验继续排除；有效前三轮路径及历史配置见中英文 criteria 和各轮 manifest。

验证：字符扫描、Python 语法和变更范围 Ruff 检查通过；`python -m pytest -q tests --basetemp tmp/tmp_pytest_round4_all_tests -x` 共 $518$ 项通过，其中评估模块 $102$ 项通过。`tmp/tmp_verify_round4.py` 独立核验输入／参考／结构化文件哈希、题组计数、预算词数与单调性、分组指标、逐题得失、旧题与 Round 3 的原文／证据、语料、排序、指标和可读性文件一致；`regenerate` 与 `summarize` 后 summary 字节不变，SHA-256 为 `db30119ad51f23b6b11ab7747734a21991924758d1e8bfff5485c5942085d340`。原始题单留在 `experiments/chunk_size/round4_question_plan.json`，供后续复用及核验。

下一步：继续 `TODO.md` 的 $2.4.3$，根据新增题的主要预算结果与逐题得失完成综合评估；当前 `report.md` 已提供本轮定量记录。可读性沿用原有 $10$ 个段落，本轮 $31$ 个分块仍为 `pending`，通过率为 `null`；审核后再讨论最终配置冻结。本轮新增题已经用于选参，不能再充当独立最终测试题。BM25 结论不推广到 dense／hybrid／reranker；接口、split policy 和最终配置继续为 `v0-proposed`。整合来源见 `INTEGRATION_PLAN.md`，完整命令与行为见 `experiments/chunk_size/README.md`。
