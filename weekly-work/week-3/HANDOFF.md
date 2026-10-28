> 只记录当前最新完成的工作和下一步。

最新完成：已按取消可读性评分的要求完成 `TODO.md` 的 $2.5$。有效 Round 1–3 已补充简短的中英文评估报告，Round 4 报告已补充 top-$5$ 分组结果、选值原因和边界。第 $2$ 项及 $2.4$ 的运行评估已完成，第 $3$ 项定版交付仍未完成。

选定 chunk size 为 $365$ words，overlap 为 $40$ words，适用于当前 BM25，仍标为 `v0-proposed`。Round 4 新增 $200$ 题中，$365$ 的 top-$5$ 两项证据指标比 $375$ 各多 $2$ 题；$1000$ words 下命中相同，但原定主指标完整证据率为 $106/200$，略低于 $375$ 的 $108/200$。$2000$ words 下各有取舍，$500$ words 下 $325$ 更好。因此这是综合选值，没有证明稳定最优；重叠词数未单独调优。

报告路径：`results/chunk_size/round1_bm25_20261028_02/report.md`、`results/chunk_size/round2_bm25_20261028_01/report.md`、`results/chunk_size/round3_bm25_20261028_01/report.md`、`results/chunk_size/round4_bm25_20261028_01/report.md`。选值和取消可读性的说明见 `experiments/chunk_size/criteria.md` 与 `criteria_zn-CN.md`。历史可读性样本和程序字段保留，不要求评分，不阻碍本次选值。

本次只整理报告和进度，没有重跑实验或修改输入、排名、summary、manifest。前三轮使用同一批 $50$ 题，Round 4 保留旧题并新增 $200$ 题；新增题与旧题有 $8$ 篇论文重合，不能称为论文独立验证。新增题已用于选参，不能再用作独立最终测试题。原始题单在 `experiments/chunk_size/round4_question_plan.json`，各轮配置、哈希和回归记录保留在对应 manifest；运行命令见 `experiments/chunk_size/README.md`，整合来源见 `INTEGRATION_PLAN.md`。

下一步：执行 `TODO.md` 第 $3$ 项，在交付配置中落实 $365/40$，冻结知识库，补充分块分析、语料统计和数据处理文档。当前 `experiments/chunk_size/config.json` 仍保留 Round 4 的 $325/365/375$ 候选，用于实验复现，不代表已经更新部署配置。若用于 dense／hybrid／reranker，先用实际模型检查 token 长度和截断，并验证检索效果；全项目配置、接口和 split policy 的冻结仍需相关模块负责人确认。
