> 只记录当前最新完成的工作和下一步。

最新完成：已执行 `TODO.md` 的 $3.1$。`configs/default.yaml` 已落实 chunk size 为 $365$ words、overlap 为 $40$ words；`data/processed/passages.jsonl`、`passages_all_paper_text.jsonl`、`sample_passages_100.jsonl` 及各自 manifest 已重建，分别包含 $21{,}360$、$28{,}617$、$100$ 条。`data/README.md` 已同步参数、显式运行命令、语料统计、哈希和核验结果。配置、共享接口及 split policy 继续保留 `v0-proposed`。

选定 chunk size 为 $365$ words，overlap 为 $40$ words，适用于当前 BM25，仍标为 `v0-proposed`。Round 4 新增 $200$ 题中，$365$ 的 top-$5$ 两项证据指标比 $375$ 各多 $2$ 题；$1000$ words 下命中相同，但原定主指标完整证据率为 $106/200$，略低于 $375$ 的 $108/200$。$2000$ words 下各有取舍，$500$ words 下 $325$ 更好。因此这是综合选值，没有证明稳定最优；重叠词数未单独调优。

核验：两个完整语料通过 `scripts.check_corpus`；三个落盘文件均按 YAML 参数从原始论文容器重建并逐条核对，正文非空、每块不超过 $365$ words、ID 无重复、编号连续、相邻引用在原容器内有效且互逆、语料范围及输出哈希一致。`papers.jsonl`、`qa.jsonl` 和 export manifest 的哈希未变。生成数据保持 Git 忽略；旧本地文件已备份在 `tmp/tmp_week3_before_365/`，核验摘要为 `tmp/tmp_week3_365_verification.json`，执行脚本为 `tmp/tmp_rebuild_week3.py`。

选参依据见 `experiments/chunk_size/criteria.md`、`criteria_zn-CN.md` 和有效 Round 1–4 的 `results/chunk_size/<run_id>/report.md`；具体 run ID 见 `TODO.md`。本次没有重跑或改写历史实验。前三轮使用同一批 $50$ 题，Round 4 保留旧题并新增 $200$ 题；新增题与旧题有 $8$ 篇论文重合，不能称为论文独立验证。新增题已用于选参，不能再用作独立最终测试题。原始题单在 `experiments/chunk_size/round4_question_plan.json`，各轮配置、哈希和回归记录保留在对应 manifest；运行命令见 `experiments/chunk_size/README.md`，整合来源见 `INTEGRATION_PLAN.md`。

下一步：执行 `TODO.md` 的 $3.2$，编写内容一致的 `week-3-report-en.md` 和 `week-3-report-zn.md`，引用实验说明、各轮 `summary.html` 及 `report.md`，写明参数已落实、passages 已重建并通过核验。`experiments/chunk_size/config.json` 仍保留 Round 4 的 $325/365/375$ 候选用于复现。构建命令不会自动读取 YAML，复现时须显式传入 $365/40$；新参数改变 passage ID，下游索引和旧引用须按新语料更新。若用于 dense／hybrid／reranker，先用实际模型检查 token 长度、截断和检索效果；全项目冻结仍需相关模块负责人确认。
