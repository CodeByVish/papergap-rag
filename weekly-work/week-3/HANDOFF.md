> 只记录当前最新完成的工作和下一步。

最新完成：2026/10/27 实现 `EXPERIMENT_GAPS.md` 第 $1$ 条可读性抽样方案。默认 `n_paper=5`、`n_paragraph=2`，从各候选语料共同包含的原始 `train/validation` 论文中随机抽取论文，再按原文段落顺序划分连续区间，每区间抽一个段落；不足时全部抽取。问题、论文及段落抽样统一使用 `seed=42`。旧配置键 `readability_sample_count`、`question_seed`、`readability_seed` 已移除，自定义运行配置需迁移；历史完成产物仍可汇总。

`manifest.json` 新增整批段落词数及长短覆盖检查、计划／实际论文数、每篇实际段落数、各候选大小实际待评唯一 chunk 数及总量。长短检查使用 $150$ words 分界，仅供抽样后检查，不自动重抽，不设置逐篇配额。默认 $10$ 个原文段落不等于人工审核 chunk 数。配置、README、中英文 criteria 和整合计划配置示例已同步，第 $1$ 条已勾选；第 $2$ 至 $8$ 条仍待完善。

验证：项目环境 `D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe`，字符扫描、Python 语法及 Ruff 检查通过；评估模块 $65$ 项测试通过，项目完整测试 $481$ 项通过。完整测试命令为 `python -m pytest -q --basetemp tmp/tmp_pytest_readability_full_01`。系统默认 pytest 临时目录存在权限问题，使用项目内临时目录后通过。未执行正式实验、人工评分、提交或推送。

已有真实 BM25 试跑 `results/chunk_size/smoke_p1_bm25_01/` 保留，使用旧抽样配置和种子，只证明此前流水线可运行，不能作为本次抽样方案的正式结果。原始导出复现与核验见 `data/README.md`；代码整合来源与固定 SHA、可选模型准备见 `INTEGRATION_PLAN.md`；现行实验配置、采样和输出定义见 `experiments/chunk_size/criteria.md` 及中文版。生成数据、结果和 `tmp/` 均保持 Git 忽略。共享接口、split policy 和输出仍为 `v0-proposed`；真实 dense／hybrid／hybrid_rerank 权重、设备和 tokenizer 截断尚未验证。

下一步：继续完善 `EXPERIMENT_GAPS.md` 第 $2$ 至 $8$ 条；确认正式检索模式、固定参数和评审规则后，按 `TODO.md` 的 $2.4$ 使用新 run ID 正式运行，先检查整批长短覆盖及实际 chunk 审核工作量，再完成人工评分与汇总。保留 `TODO.md` 的正式实验和方案完善任务未完成状态。
