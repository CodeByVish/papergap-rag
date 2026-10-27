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
2. [x] 正式检索模式及返回数量的选择。已确认使用 `bm25`，固定 `top_k=5`；实验配置见 `experiments/chunk_size/criteria_zn-CN.md` 及英文版。BM25 算法参数沿用实现的库默认值，不作为本次分块大小实验的待选配置；实现说明见 `experiments/chunk_size/BM25.md` 及英文版。
3. [x] 可读性通过／不通过的具体判定标准和示例。已记录语义完整、必要上下文充分及逻辑连贯三项判断指标、判定边界、示例和参考文献；见 `experiments/chunk_size/criteria_zn-CN.md` 的“可读性判定标准”章节及英文版。
4. [x] 可读性评审人员、是否隐藏分块大小及分歧处理方式。
    1. 我、队友都会审核；如果工作量很大，考虑 Codex 审核
    2. 暂定不必隐藏分块大小，直接展示 `experiments\chunk_size\criteria_zn-CN.md` 提到的可读性方面保存的 `.md` 文件即可
    3. 分歧只能看情况再说，无法制定处理方案
5. [x] 部分证据无法定位的答案标注，其已定位段落是否参与证据命中统计：一个问题的所有答案标注均须具有非空的文字证据，且每份标注中的全部证据都能唯一定位到原文段落；任一标注不满足条件，就排除整个问题。已同步抽样筛选、指标计算保护和回归测试；细则见 `experiments/chunk_size/criteria_zn-CN.md` 及英文版。
