工作进展同步在 `weekly-work/week-3/HANDOFF.md` 中

1. [x] 确认比较配置：约 150、200、250 words/chunk，这里按词数计，不是 token。
    1. 我已经在 `experiments/chunk_size/config.json` 的配置文件中记录了候选 chunk sizes
2. [ ] 评估质量：抽查分块可读性，结合 development/validation 上的检索结果选择配置。
    1. [x] 制定评估指标：记录在 `experiments/chunk_size/criteria.md` 中
        1. 不要写废话，不要写得过于复杂；把我当成不怎么了解 RAG 的人，用最简单、直白的语言描述
        2. 内容只需要包括：什么指标、这个指标怎么判断 chunk size 的好坏
        3. 英文版 `criteria.md`，中文版 `criteria_zn-CN.md`
    2. [x] 把所有运行代码、展开评估所需的代码汇总、整合到 p3 分支
        1. [x] 补充执行实验所需的代码
            1. 读取、解析 `experiments/chunk_size/config.json` 的参数，通过正确方式传入 chunk 环节中
            2. 保存 `experiments/chunk_size/criteria.md` 所需的数据、结果
        2. [x] 整合实验所需的其他分支的代码
            1. [x] 浏览其他分支的代码，罗列需要整合到 p3 的清单，记在 `weekly-work/week-3` 的 `.md` 文件中：哪个 part 的什么代码/文件/文件夹，整合到 p3 分支的什么代码/文件/文件夹中。清单见 `weekly-work/week-3/INTEGRATION_PLAN.md`。
            2. [x] 按照 `weekly-work/week-3/INTEGRATION_PLAN.md` 执行代码整合
    3. [x] 试运行确保代码能正常工作（已验证默认 `bm25`，运行 `smoke_p1_bm25_01`；其他模式尚未验证）
        1. 配置能正常解析
        2. 系统能正常运行
        3. 所需结果能正确导出到对应路径（路径详见 `experiments/chunk_size/criteria.md` 或中文版）
    4. [ ] 展开正式运行、评估
        1. [ ] 完善 `criteria.md` 的实验方案，使之可执行。我的观察是，还缺少从 `qa.jsonl` 中随机选取问题的抽样方案。待完善清单见 `weekly-work/week-3/EXPERIMENT_GAPS.md`。
        2. [ ] 正式执行实验方案，运行代码，保存所需结果
        3. [ ] 对于各类结果展开评估，评估结果保存在 `results/chunk_size/{run_id}/report.md`。报告尽量简洁、易懂，能定量就不要只定性，不要写冗余内容。
3. [ ] 定版交付：确定分块配置、冻结知识库，补充分块分析、语料统计和数据处理文档。
