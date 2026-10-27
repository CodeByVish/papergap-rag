# 实验方案待完善清单

1. [x] 可读性抽样方案。已实现；配置和抽样细则见 `experiments/chunk_size/criteria_zn-CN.md` 及英文版。
    1. 文章采样数量 `n_paper`，每篇文章的段落样本量 `n_paragraph`。确保 `n_paper * n_paragraph` 是一个合理的数值
    2. 长短段落覆盖：尽量均衡；抽取的段落尽量平均分布在不同文章内，但绝不要求每一篇文章都要覆盖，否则审核工作量过大（以实际待评 chunk 数估算审核工作量）
    3. 抽样方式
        1. 从 `data/processed/papers.jsonl` 中随机抽取 `n_paper` 篇文章。
        2. 每篇文章按原文段落顺序划分为 `n_paragraph` 个连续区间，每个区间随机抽一个段落；不足时全部抽取。
        3. 在整批样本层面兼顾长短段落覆盖（抽样完成后大致检查即可），无需每篇都覆盖。
    4. 固定随机种子（建议 `experiments/chunk_size/config.json` 中，所有随机过程采用相同的 random seed）
    5. `n_paper`、`n_paragraph` 一并记入 `experiments/chunk_size/config.json` 中
    6. 补充相关代码，在 `experiments\chunk_size\criteria_zn-CN.md` 和英文版，补充实验配置和这个采样方案
2. 正式检索模式及固定参数的选择。已选用 `bm25`；算法说明及当前参数见 `experiments/chunk_size/BM25.md` 和英文版。当前使用 `top_k=5` 及库缺省值 $k_1=1.5$、$b=0.75$、$\epsilon=0.25$；固定参数仍待正式确认，本条暂不标为全部完成。
3. 可读性通过／不通过的具体判定标准和示例。
4. 可读性评审人员、是否隐藏分块大小及分歧处理方式。
5. 部分证据无法定位的答案标注，其已定位段落是否参与证据命中统计。
6. 若采用 `dense` 或重排模型，长分块截断对比较结果的检查方案。
7. 小幅指标差异的复核方案（是否重复抽样或报告不确定性）。
8. 指标 “接近” 的范围、多项指标冲突时的取舍及最终分块大小选择规则。
