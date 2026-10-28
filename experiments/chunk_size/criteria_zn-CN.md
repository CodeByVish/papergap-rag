# 分块大小评估指标

Round 1 已完成每块 $100/200/400$ words 的 BM25 比较，有效结果见 `results/chunk_size/round1_bm25_20261028_02/`。Round 2 已完成 $200/225/250/275/300/325/350/375/400$ 共 $9$ 个候选，结果见 `results/chunk_size/round2_bm25_20261028_01/`，对应 `weekly-work/week-3/TODO.md` 的 $2.4.2.2$。Round 3 已完成下方 $10$ 个候选，结果见 `results/chunk_size/round3_bm25_20261028_01/`，对应 $2.4.2.3$；`config.json` 保留本轮配置。三轮均比较固定 top-$5$ 和固定 $500/1000/2000$ words 预算；使用从 `data/processed/qa.jsonl` 筛选的同一批问题、相同检索方法和重叠词数。此前 $150/200/250$ 的实验作废，不参与选值或合并。

## 候选分块大小的依据与建议

### 执行计划是否已解释这三个值

[`docs/EXECUTION_PLAN.md`](../../docs/EXECUTION_PLAN.md) 的 Week 2 / P3 建议从约 $200$ words、重叠 $40$ words 开始，并保留章节边界；Week 3 / P3 用 “such as” 列出 $150$、$200$、$250$ words，要求按开发集检索结果及可读性选最终值。计划没有为这三个数提供参考文献、QASPER 长度分布或模型长度预算依据，也没有说它们是最优范围。

因此，将其理解为围绕 $200$ words、上下各变动 $25\%$ 的局部敏感性检查是合理推断，不能写成计划已明确给出的设计理由。该范围适合检查现有默认值附近的变化，但可能遗漏明显更短或更长的有效窗口。

### 研究和项目分别支持什么

以下只使用原始论文及官方模型资料。文献能支持候选范围的设计，不能代替本项目实验；尤其要区分 words、模型 tokens、数据领域和检索方式。

| 来源 | 原始设置或发现 | 本项目据此做什么 | 不能据此断言什么 |
| --- | --- | --- | --- |
| DPR，EMNLP 2020，第 4.1 节 [S1] | 将 Wikipedia 切为互不重叠的 $100$ words passages。 | 将 $100$ words 加为短窗口对照，检查更集中的词项匹配和较低阅读成本。 | 未证明 $100$ words 适合 QASPER；本项目保留 $40$ words 重叠，也不构成 DPR 复现。 |
| Wang et al.，EMNLP 2024，第 3.2 节、附录 A.2、表 3 [S2] | 比较 $128/256/512/1024/2048$ 的分块尺度；中等尺度在该实验中表现较好。使用 Lyft 年报、长输入 embedding 和生成评估，重叠为 $20$ tokens。 | 借鉴跨倍数尺度筛选的做法，避免只在默认值附近细调。 | 其 token 分块设置不能直接改写成同数值的 words，也不能证明本项目某个值最优。 |
| QASPER，NAACL 2021 [S3] | 问题围绕科研论文全文，包含需要综合论文不同位置信息的任务，并有支持证据标注。 | 保留完整证据率指标，并增加较长窗口，检查方法、条件及结果是否被切散。 | 该文未推荐本项目的固定分块词数；更长窗口也不能代替跨章节检索。 |
| BAAI 官方 `bge-small-en-v1.5` 模型卡 [S4]，以及本地 `src/retrieval/reranker.py` | embedding 的序列长度为 $512$ tokens；本地 reranker 默认将问题与 passage 配对后截断到 $512$ tokens。 | 候选范围还需通过真实 tokenizer 的长度和截断检查，才能用于最终 dense / hybrid / reranker 选择。 | $512$ tokens 不等于 $512$ words；短于 $512$ words 也不保证没有截断。 |

### 建议值及选择理由

**Round 1 使用 BM25，执行 $100$、$200$、$400$ words 粗筛，保留重叠 $40$ words。** 这是 `v0-proposed` 实验设计，不是文献共同推荐的标准组合，也不冻结语料。本轮用两个证据指标和检索词数粗筛；导出可读性样本，但暂不评分。

| 候选值 | 选择理由 | 主要检查的问题 |
| --- | --- | --- |
| $100$ words | DPR 的 $100$ words 提供同单位的短窗口先例 [S1]；相对当前默认值减半。 | 证据是否更易被词项检索命中，还是完整段落需占用太多返回名额、可读性下降。 |
| $200$ words | 保留现有项目默认值，在 Round 1 中重新运行作为对照；其依据首先是项目现状，而非某篇论文证明最优。 | 当前成本与证据完整性的折中是否仍有竞争力。 |
| $400$ words | 相对默认值加倍，与 $100/200$ 形成倍数尺度；借鉴 [S2] 的宽范围筛选，并针对 QASPER 上下文需求 [S3] 设置长窗口压力点。$400$ 是本项目设计值，不是论文原始最优值。 | 上下文扩大是否提高完整证据率，以及额外文字、无关内容和模型截断是否抵消收益。 |

不得复用作废实验，包括其中的 $200$ words 结果。历史候选及控制量以各有效运行的 `manifest.json` 为准，不以当前配置重建历史设置。

### Round 2：已确认的细筛方案

2026/10/28 已确认并执行：比较 $200/225/250/275/300/325/350/375/400$ words/chunk，在 $200$–$400$ words 内每隔 $25$ words 取值，共 $9$ 个候选。结果见 `results/chunk_size/round2_bm25_20261028_01/summary.html`。输入哈希、问题 ID 及顺序、证据筛选和可读性原文位置已核验；除耗时外，$200/400$ 对照的语料哈希、保存排序及逐问题结果与 Round 1 完全一致。结构化重算及汇总核验通过。全部 $104$ 个可读性分块仍待审核；综合评估属于 TODO 的 $2.4.3$。共享接口及最终分块配置仍为 `v0-proposed`。

范围依据为有效 Round 1 的 `summary.html`：$100$ words 在各固定预算下的两个证据指标均不优于 $200/400$；$200$ 与 $400$ 各有优势，适合进一步比较中间值。

| 固定预算 | $200$ words：命中率／完整证据率 | $400$ words：命中率／完整证据率 |
| --- | --- | --- |
| $500$ words | $38\%/24\%$ | $30\%/26\%$ |
| $1000$ words | $54\%/42\%$ | $54\%/46\%$ |
| $2000$ words | $78\%/70\%$ | $72\%/68\%$ |

| 候选值（words） | 取值理由 |
| --- | --- |
| $200/400$ | 保留两端对照，核验跨轮结果一致。 |
| $300$ | 检查范围中点能否取得更好的成本与覆盖折中。 |
| $250/350$ | 分别检查范围下半段和上半段。 |
| $225/275/325/375$ | 将间隔细化到 $25$ words，观察较优区间是否稳定。 |

这些具体取点来自本地结果和均匀搜索设计，文献未证明它们最优。执行与选值规则如下。

1. 沿用有效 Round 1 的同一批 $50$ 个问题及顺序、证据筛选、论文范围、BM25 设置、$40$ words 重叠、`top_k=5`、`seed=42` 和可读性原文位置。执行前核验问题 ID、顺序和原文位置一致；固定种子不能代替核验。
2. 使用新 `run_id` 保存全部 $9$ 组结果，保留并核验 $200/400$ 对照，不覆盖 Round 1。以全部 $500/1000/2000$ words 固定预算下的两个证据指标为主要依据，同时报告实际词数和耗尽数；top-$5$ 为补充。
3. 不只凭 top-$5$ 选择长块：Round 1 的 $400$ words 完整证据率为 $52\%$，高于 $200$ 的 $40\%$，但平均检索词数也从 $832.88$ 增至 $1332.72$。
4. 每题对应 $2$ 个百分点，小差异先检查逐问题得失；各预算的优胜者不同则保留成本与覆盖的取舍。若固定预算比较仍指向端点，再向下补测 $175$ 或向上补测 $425/450$，不能直接宣布全局最优。
5. 最终定版前完成可读性审核；BM25 结论不直接推广到 dense / hybrid / reranker，模型输入长度检查仍按下方规则执行。

本项目的 words 是 `src/data/chunking.py` 用 `\S+` 计数的 Unicode 非空白片段。这里继续使用这一单位，不将论文 token 数按固定比例换算成词数。换用 token 分块、按句子调整边界或改变跨段落规则，均应作为单独实验，避免同时改变多个因素。

### Round 3：已确认的局部细筛方案

2026/10/28 已确认并执行：比较 $325/335/345/350/355/365/375/385/395/400$ words/chunk，共 $10$ 个候选，配置保留在 `config.json`。结果见 `results/chunk_size/round3_bm25_20261028_01/summary.html`，已完成 `weekly-work/week-3/TODO.md` 的 $2.4.2.3$。输入哈希、问题 ID 及顺序、证据筛选和可读性原文位置已核验；除耗时外，$325/350/375/400$ 四个对照的语料哈希、保存排序及逐问题结果与 Round 2 完全一致。结构化重算和可读性汇总后，`summary.json` 与初次结果字节一致；产物及预算核验通过。全部 $107$ 个可读性分块仍待审核；综合评估属于 $2.4.3$。共享接口及最终分块配置仍为 `v0-proposed`。

依据 Round 2 的 `summary.html`，从 $325$ 开始：$375$ 的 top-$5$ 命中率／完整证据率最高，为 $64\%/56\%$，但平均检索词数为 $1291.60$，高于 $325$ 的 $1203.84$；在 $1000$ words 预算下，$325$ 的两项指标最高，为 $58\%/50\%$，而 $375$ 为 $50\%/42\%$。$325$ 在 $500$ words 预算下的完整证据率也最高，为 $32\%$。因此保留 $325$ 与 $375$ 两处附近，不仅围绕 top-$5$ 最优点搜索。

| 候选值（words） | 取值理由 |
| --- | --- |
| $325/350/375/400$ | 保留 Round 2 对照，核验跨轮结果一致。 |
| $335/345/355/365/385/395$ | 在 $325$–$400$ 区间按约 $10$ words 的间隔细筛；保留已有对照后，部分相邻点间隔为 $5$ words。 |

这是依据本地结果制定的局部搜索方案，不代表区间外不存在更优值，也没有文献证明这些具体值最优。沿用前两轮同一批 $50$ 个问题及顺序、证据筛选、论文范围、BM25 设置、$40$ words 重叠、`top_k=5`、`seed=42` 和可读性原文位置；使用新 `run_id` 保存全部 $10$ 组结果，不覆盖已有结果，并核验四个对照的语料、排序及逐问题结果一致，耗时除外。

继续以全部 $500/1000/2000$ words 预算下的两个证据指标为主要依据，同时报告实际词数和耗尽数，top-$5$ 为补充。当前每题对应 $2$ 个百分点，$375$ 相比 $325$ 的 top-$5$ 优势仅为 $2$ 题；先检查逐题得失，暂不全面细化到每隔 $5$ words。最终定版前完成可读性审核，并用独立或扩大的开发／验证题集验证候选值；BM25 结果不直接推广到 dense / hybrid / reranker。

### 解释结果时必须保留的边界

- **重叠固定的是绝对词数**：$100/200/400$ words 配合 $40$ words 重叠时，重叠比例分别为 $40\%/20\%/10\%$。本轮回答的是“固定重叠词数下哪个窗口更合适”，不能声称隔离了重叠比例的影响。固定比例的对照可另做，不能混入本轮结果。
- **固定 top-$5$ 不等于固定文字预算**：三种大小最多返回约 $500/1000/2000$ words，实际受末尾短块及可用块数影响。完整段落覆盖指标也天然更容易受长窗口影响。因此，应同时比较证据命中率、完整证据率、可读性和检索词数，不能只凭长块的覆盖率选值。若要声称同预算下更好，需要采用下方已在新 BM25 运行中实现的固定输入预算对照。
- **BM25 结果只支持 BM25 条件下的选择**：$400$ words 是 BM25 的长窗口压力点，不保证适用于 BGE。正式 dense / hybrid / reranker 比较前，使用实际 checkpoint 和 tokenizer，记录各候选的未截断 token 长度分布、超限比例及问题–passage 对的超限比例。若存在截断，现有完整文字覆盖指标不等于模型实际看到了全部证据；不能用该指标声称模型可见证据完整。长度检查尚未执行，也不是现有自动报告已提供的字段。
- **只用开发／验证数据选值**：沿用现有论文级划分及证据筛选规则，使用同一问题样本；不利用 held-out 最终标签选择候选或调整范围。当前 $50$ 个问题适合初筛，小幅差异需逐问题检查；未定义统计门槛时，不声称显著胜出。
- **最终确认范围**：先检查 corpus 数量及质量要求，再根据上述指标及失败案例选工作值；若用于全项目冻结，应由 P3 与受影响的 P1/P2 等模块负责人确认，并同步配置、语料版本和双语文档。Round 1 粗筛不冻结全项目配置。

### References：候选值依据

1. [S1] Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. 2020. [Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/). *EMNLP 2020*, pp. 6769–6781. DOI: [10.18653/v1/2020.emnlp-main.550](https://doi.org/10.18653/v1/2020.emnlp-main.550). 选值依据见第 4.1 节。
2. [S2] Xiaohua Wang et al. 2024. [Searching for Best Practices in Retrieval-Augmented Generation](https://aclanthology.org/2024.emnlp-main.981/). *EMNLP 2024*, pp. 17716–17736. DOI: [10.18653/v1/2024.emnlp-main.981](https://doi.org/10.18653/v1/2024.emnlp-main.981). 选值依据见正式发表版第 3.2 节、附录 A.2 及表 3。
3. [S3] Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A. Smith, and Matt Gardner. 2021. [A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers](https://aclanthology.org/2021.naacl-main.365/). *NAACL-HLT 2021*, pp. 4599–4610. DOI: [10.18653/v1/2021.naacl-main.365](https://doi.org/10.18653/v1/2021.naacl-main.365). 用于说明任务与证据需求，不作为固定长度推荐。
4. [S4] BAAI. [bge-small-en-v1.5: Official Model Card](https://huggingface.co/BAAI/bge-small-en-v1.5). `Evaluation` 的 `Sequence Length` 列；访问日期：2026/10/28。用于确认模型输入约束，不作为最优分块大小证据。

## 评估指标

| 指标 | 衡量什么 | 怎么判断分块大小的好坏 |
| --- | --- | --- |
| 可读性通过率（Readability pass rate） | 对每种配置，人工抽查相同原文位置对应的分块，按[可读性判定标准](#可读性判定标准)检查语义完整、必要上下文充分及逻辑连贯。通过率为通过的分块数除以抽查的分块数。 | 越高越好。通过率低，说明分块可能太小，把解释切碎了。 |
| 证据命中率（Evidence Hit@$5$） | 在有可用文字证据的问题中，前 $5$ 个检索分块合起来，包含至少一个完整人工标注证据段落的问题占比。证据段落被切到多个分块中，只要这些分块都被检索到、合起来覆盖完整段落，也算命中。 | 越高越好，说明更多问题能找到有用证据。命中一个证据段落，不代表已经找全回答所需的证据。 |
| 完整证据率（Complete evidence rate@$5$） | 在同一批问题中，前 $5$ 个检索分块合起来，包含至少一份答案标注所列全部文字证据段落的问题占比。 | 越高越好，说明证据找得更全，尤其适合判断需要多处证据的问题。 |
| 检索词数（Retrieved word count） | 每个问题检索到的前 $5$ 个分块的总词数，再对所有问题取平均。重叠文字如果被重复传给回答模型，就重复计数。 | 越低，模型需要阅读的文字越少。在证据检索效果和可读性接近时，优先选择词数更少的配置；不能只凭词数少判断质量更好。 |
| 相同文字预算下的证据覆盖率 | 每个问题最多读取 $B$ words，计算预算内的证据命中率和完整证据率，定义沿用上方两个证据指标，但不限制 chunk 数。 | 同一预算下覆盖越高越好，避免大块仅因读入更多文字而占优；结合多个预算比较成本与覆盖。 |

两个证据指标都要核对证据所属的论文和原文段落，不能只看是否有几个词相同。抽样前，若问题没有答案标注，或任一标注缺少非空、全部可唯一定位的文字证据，就排除整个问题。排除数量记录在 `manifest.json` 的 `filtering_counts.invalid_answer_evidence` 中。

## 固定文字预算下的证据覆盖：执行方案

该 `v0-proposed` 流程已在有效 Round 1 中执行，Round 2 沿用，预算由 `config.json` 的 `word_budgets` 指定；历史汇总不会自动补齐。固定预算指相同的词数额度，不是预先指定同一段原文；不同配置可以检索到不同文字。它衡量送入阅读环节的证据覆盖，不直接衡量生成答案质量。

### 预算和统计口径

预先固定 $B\in\{500,1000,2000\}$ words，全部候选均使用这三档，不能看结果后只挑有利的一档。三档最初对应 Round 1 的 $100/200/400$ words 在 top-$5$ 下的名义最大词数；Round 2 保持不变，以便跨轮比较。这是本项目的对照设计，不是文献推荐值。沿用有效 Round 1 的同一批 $50$ 个问题、问题顺序、证据筛选、论文范围、BM25 参数、重叠及种子；不重新抽题，不使用作废实验。

- **预算内证据命中率**：预算内文字合起来完整覆盖至少一个标注证据段落的问题数，除以同一批全部问题数。
- **预算内完整证据率**：预算内文字合起来完整覆盖至少一份答案标注全部证据段落的问题数，除以同一批全部问题数。这里只是沿用现有两种覆盖判定，不另设含糊的“覆盖百分比”。
- **实际阅读词数**：每题实际保留的词数；重叠文字重复扣预算，原文覆盖按位置合并、不重复算证据。仅计 chunk 正文，标题、ID、提示词及分隔符不计入这项实验预算；不换算为模型 tokens。

### 每个问题如何执行

1. 各配置在问题所属论文内独立进行 BM25 检索，按分数降序、同分按 passage ID 升序排列。排名不使用答案或证据标签，纳入后的 chunk 内文字顺序保持原样。
2. 沿排名依次纳入 chunk，达到 $B$ words 即停止。这里不受原 top-$5$ 限制；应取得足以填满最大预算的排名，或取得该论文的全部可用 chunk，不能因只取了前 $5$ 个就误判语料耗尽。三档预算共用同一份排名的前缀。
3. 最后一块超过剩余额度时，仅保留其前 $r$ 个词，$r$ 为剩余额度；不跳过该块去选更短的后续块，也不按证据位置挑选内容。词按 Unicode 非空白片段 `\S+` 计数，截断点为第 $r$ 个词的末尾，保留其前方原始文字；余额为 $0$ 时不再纳入 chunk。
4. 根据实际保留文字重算原文字符覆盖范围。截断点之后的证据不计入；多个保留片段可以合起来覆盖完整段落，空白间隙沿用现行处理规则。禁止直接复用未截断 chunk 的 `full/partial` 标记或 top-$5$ 的真假结果。
5. 若全部可用 chunk 仍不足 $B$ words，使用全部实际文字，记录实际词数、`corpus_exhausted` 和未用预算，不重复填充、不剔除该问题。各组预算上限相同，但此时实际阅读量可能不同；每组每档报告耗尽问题数，避免声称所有问题都恰好读满预算。
6. 按每个分块大小、每档预算汇总上述两种覆盖率，同时报告平均实际词数和耗尽问题数。预算增大后的截取内容应包含较小预算内容；同一配置、同一问题的覆盖结果不应随预算增大而下降。可读性仍审核完整 chunk，不用预算末尾的人为截断评分。

### 能否利用现有 `evidence_review.md`

可以复用这份报告展示的排名、完整 chunk 文字、答案分组、证据原文及原文定位，作为复核材料；但现有文件只保存前 $5$ 块，且覆盖表只给出证据段落内的范围，没有完整的 chunk 内字符到原文位置映射。它不是对所有预算都充分的独立计算输入。只有某题已保存的排名前缀足以达到预算，或已确认列出该论文全部可用块，才无需补充后续检索；不足时不能把“报告到末尾”当成“语料耗尽”。例如，$100$ words 的前 $5$ 块最多 $500$ words，无法据此计算 $1000/2000$ words 的完整预算结果，连 $500$ 也可能因短块而未填满。

可靠执行时，读取该有效运行的 `manifest.json`，核对配置、代码、输入哈希和问题 ID；利用相同输入及分块实现重建带原文位置的 chunk，并按需补齐 BM25 排名。截断后通过原文映射重算覆盖，避免仅凭字符串相似或旧表格推断。已有 top-$5$ 报告用于核验重建结果，不能把作废结果作为输入。

新增结果仍可保存在同一类 `evidence_review.md` 中：保留原 top-$5$ 内容，在现有 `### Retrieved chunks` 下按排名补充所需后续 chunk，在现有 `### Evaluation results` 下追加每档预算的表格。每档保存预算、实际词数、纳入的 passage IDs／排名、末块保留词数和 chunk 内字符区间、预算内证据覆盖区间、两项覆盖真假、完整覆盖的答案标注及缺失证据、是否耗尽。保留 chunk 全文，另标实际保留区间，便于复核截断位置。

实现时将逐题预算结果和按大小／预算汇总的分子、分母、覆盖率、平均实际词数、耗尽问题数同步保存到 `summary.json`；在 `manifest.json` 记录预算列表、词数口径、截断规则、排名深度、来源 run ID 和输入哈希。使用新的 `run_id` 保存扩展结果，不覆盖已有 Round 1 文件；固定 top-$5$ 与固定预算分别标注，不能将新结果命名为 `@5`。预算列表及新增字段须先补实现和验证，再执行，不把本方案当成已产出的结果。

比较时优先看同预算覆盖和实际词数，再结合原 top-$5$ 的成本与覆盖、完整 chunk 可读性选择后续候选。不能仅凭大块的 top-$5$ 覆盖更高，认定 $400$ words 最优。

## 结构化数据保存与报告生成方案

本节的 `v0-proposed` 输出约定已在新 BM25 运行中实现。独立保存问题与证据信息，不从 Markdown 反向解析计算输入：JSONL 保存计算依据，`summary.json` 保存计算结果，`evidence_review.md` 展示同一份结果。已保存排名支持所需预算时，修改预算或报告格式无需重复运行 BM25，也不依赖 Markdown 的标题、表格和代码围栏。命令和字段路径见 `README.md`；其他检索模式保留原 top-$5$ 流程。

### 文件分工

所有文件均位于 `results/chunk_size/<run_id>/`，实验结果提交到 Git 共享；原始数据集和生成语料不提交到 Git。

| 路径 | 内容与用途 |
| --- | --- |
| `questions.jsonl` | 每行一个通过筛选并抽中的问题，包含答案分组和完整证据；本轮共用一份，各分块大小使用相同问题。 |
| `chunk_size_<size>/ranked_chunks.jsonl` | 每行一个问题的一条 BM25 检索结果，包含完整 chunk；供全部检索定量指标读取。 |
| `manifest.json` | 保存配置、来源、文件哈希及各问题的排名保存状态，判断结果是否足够或真正耗尽。 |
| `summary.json`、`chunk_size_<size>/evidence_review.md` | 从上述结构化输入生成，分别供程序读取结果和人工复核；不作为定量指标的原始输入。 |

### 共用问题文件：`questions.jsonl`

每行至少包含 `question_id`、`paper_id`、`question`、`annotations` 和 `evidence_paragraphs`。`annotations` 保留每份原始答案的 `annotation_id`、`answer` 和 `evidence_locations`，不得把不同答案的证据混成一个集合；`evidence_paragraphs` 保存该题涉及的去重证据段落，每项包含 `location`、`section_index`、`paragraph_index` 和完整原文 `text`。`location` 沿用 `paper_id:section_index:paragraph_index`，索引从 $0$ 开始。

按共享问题顺序保存，每个抽中问题恰好一行；只纳入通过现行证据筛选的问题。来源划分、排除统计及输入哈希继续由 manifest／上游导出维护，报告仍不展示来源划分。三种配置不各自复制问题文件。后续覆盖计算直接读取这里的证据原文，无需重新读取 raw data 或解析 Markdown。

### 排名文件：`ranked_chunks.jsonl`

| 字段 | 含义 |
| --- | --- |
| `question_id`、`paper_id` | 关联共用问题及其所属论文。 |
| `rank`、`score` | 从 $1$ 开始的连续排名及有限的原始 BM25 分数；分数降序，同分 passage ID 升序。 |
| `passage_id`、`text`、`word_count` | chunk 标识、未截断完整正文及按 `\S+` 计算的词数。 |
| `source_spans` | chunk 内字符范围到原文位置的映射；每项至少包含 `chunk_start`、`chunk_end`、`location`、`source_start`、`source_end`。 |

`source_spans` 保存 chunk 中全部来自原文的文字映射，不只保存当前答案的证据部分；字符区间从 $0$ 开始、左闭右开，拼接分隔符不映射为原文证据。映射必须能将任意预算截断点投影到原始段落；若规范化改变字符位置，需保存更细的分段映射或等价精确映射，不能假定两侧字符长度总是相同。

按共用问题顺序、再按 `rank` 写行；同一问题内 passage ID 唯一，所有结果必须属于该题论文。排名不使用答案或证据，零分或负分不另加阈值过滤。两份 JSONL 均使用 UTF-8，每行一个 JSON 对象，通过 `question_id` 关联，不依赖行号或 Markdown 展示顺序。

### 保留数量与完整性

每题保存同时满足以下条件的最短排名前缀：至少前 $5$ 条，且完整 chunk 累计词数达到最大预算 $B_{\max}=2000$ words；若论文全部可用 chunk 先耗尽，则全部保存。预算边界的最后一块仍保存全文，计算时再截断。无需统一保存 $100$ 条，也不以固定条数上限阻止填满预算；若资源限制导致提前停止，应标记不完整，对不支持的指标报错，不能当作语料耗尽或零覆盖。

在 `manifest.json` 中按分块大小和 `question_id` 保存 `saved_count`、`available_count`、`saved_word_count`、`ranking_complete` 和 `retention_satisfied`。`ranking_complete` 表示已保存该论文全部可用 chunk；`retention_satisfied` 表示已满足前 $5$ 加最大预算要求，或已全部保存。没有可用 chunk 的问题仍须出现在共用问题文件和状态记录中。`corpus_exhausted` 仅在全部可用 chunk 已读完且仍未填满该预算时成立，不能由 JSONL 到文件末尾推断。

### 统一计算与报告生成

1. 检索阶段保存共用问题文件、各大小的排名文件及 manifest，记录文件 SHA-256、schema 版本、问题顺序、分块配置、BM25 参数、预算、截断规则及排名保存状态。
2. 计算阶段先核验文件哈希、问题集合、排名连续性、排序、ID 唯一性、词数与原文映射。每题用前 $5$ 条计算证据命中率@5、完整证据率@5和检索词数，用同一排名的预算前缀计算新增两种覆盖率及实际词数；不足前 $5$ 条时使用全部可用结果，须有完整排名状态佐证。
3. 根据问题证据和 chunk 原文映射计算覆盖，截断后重算。由同一份逐题计算结果同时生成 `summary.json` 和 `evidence_review.md`，避免分别实现两套判定；Markdown 保留原有问题、答案、排名、证据范围及结果展示，并追加预算结果。
4. 调整预算未超出已保存排名能力时，直接读取 JSONL 重算和生成报告，无需重新检索；需要更多排名时，使用相同输入及 BM25 设置补齐，在新 run ID 下保存，不能把缺失排名当成未命中。从原 Round 1 迁移时先按前节重建并核验，不从旧 Markdown 猜测原文映射。

可读性仍使用独立抽样的完整 chunk 和人工标签，其样本不一定出现在问题检索排名中，因此不能只靠排名文件生成可读性样本。上述统一输入通过 `run` 和 `regenerate` 用于定量检索报告；`summarize` 继续导入人工可读性标签。`source_spans` 额外保存每段的 `source_text` 供独立校验，CRLF 使用不等长的精确分段。manifest 的 `structured_inputs` 保存文件哈希、schema、规则、`source_run_id`（新运行时为 null）及按大小和问题 ID 索引的 `ranking_states`。

## 可读性评审人员、是否隐藏分块大小及分歧处理方式

1. 我、队友都会审核；如果工作量很大，考虑 Codex 审核
2. 暂定不必隐藏分块大小，直接展示 `experiments\chunk_size\criteria_zn-CN.md` 提到的可读性方面保存的 `.md` 文件即可
3. 分歧只能看情况再说，无法制定处理方案

## 可读性判定标准

本实验的可读性指分块能否独立理解并保留完整语义。假定评审员具备基本 NLP 背景，先只阅读当前分块，不阅读相邻分块或原文；作出初步判断后，再对照原文核实切分造成的缺失，不能用原文补足后的理解代替分块自身的可理解性。

| 判断指标 | 判定问题 | 不通过的典型情况 |
| --- | --- | --- |
| 语义完整 | 分块中的陈述是否表达完整，关键条件、对象或结论是否被切断？ | 结尾停在 “The model outperforms the baseline when…”；或切掉了决定陈述含义的限制条件。 |
| 必要上下文充分 | 能否识别核心陈述中的研究对象、方法和关键指代？ | 只有 “This method improves it significantly.”，块内无法识别方法和改进对象。 |
| 逻辑连贯 | 能否理解块内句子之间的关系，是否存在影响理解的突兀拼接？ | 尚在介绍一种方法就突然进入另一项实验，缺少理解两者关系所需的结构或过渡。 |

三项均满足时标记为 `pass`；任一项存在影响理解的问题时标记为 `fail`。不通过时，在现有 `Reason` 栏写明不满足的指标、具体文字及缺失内容，例如“必要上下文不足：`This method` 的指代对象位于前一块，当前块无法识别”。三项是同一通过／不通过判断的检查维度，不新增独立汇总指标或评分字段。

判断边界如下：

- 出现 BM25、Transformer 等背景术语不自动判为不通过；论文自定义且理解当前陈述必需的符号、缩写或对象需要足够说明。
- 出现引用或图表编号不自动判为不通过。“Table 2 shows that model A outperforms model B.” 已表达主要结论；若只有 “The results are shown in Table 2.”，且不查看表格就无法知道所述结果，则必要上下文不足。
- 以 “However” 等连接词开头不自动判为不通过；仅当缺失的对比或承接内容影响当前陈述的理解时才判为不通过。
- 不要求每块回答完整问题或包含全部实验细节；回答所需证据是否齐全由证据指标衡量。

以下为自拟的简化示例：

| 分块文本 | 结果 | 理由 |
| --- | --- | --- |
| “We evaluate BM25 on QASPER. BM25 retrieves five passages for each question.” | `pass` | 对象、操作和陈述完整，句间关系清楚。 |
| “It performs better under these settings.” | `fail` | 必要上下文不足：无法识别对象、比较基准和设置。 |
| “BM25 retrieves five passages for each question. We exclude questions without” | `fail` | 语义不完整：末尾的筛选条件被切断。 |

### 参考文献与借鉴范围

以上标准是针对本实验改编的人工评审规则，不是下列论文原有的标准量表。

1. Arihant Jain, Purav Aggarwal, and Anoop Saladi. 2025. [AutoChunker: Structured Text Chunking and its Evaluation](https://aclanthology.org/2025.acl-industry.69/). In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 6: Industry Track)*, pages 983–995. DOI: [10.18653/v1/2025.acl-industry.69](https://doi.org/10.18653/v1/2025.acl-industry.69). 第 4.2 节及附录 B.2 的 Prompt 3 以自包含、完整意思、必要上下文和非突兀边界判断分块完整性；本文借鉴其维度，将 LLM 二元判断改为人工评审。
2. Eunsol Choi, Jennimaria Palomaki, Matthew Lamm, Tom Kwiatkowski, Dipanjan Das, and Michael Collins. 2021. [Decontextualization: Making Sentences Stand-Alone](https://aclanthology.org/2021.tacl-1.27/). *Transactions of the Association for Computational Linguistics*, 9:447–461. DOI: [10.1162/tacl_a_00377](https://doi.org/10.1162/tacl_a_00377). 该文研究句子在保留原意的前提下脱离上下文后能否被理解；本文借鉴其对必要上下文和指代清晰性的关注，不执行句子改写。

## 实验配置与优先级

本实验以 `experiments/chunk_size/config.json` 为配置依据；与 `configs/default.yaml` 中用途相同的设置重复或冲突时，实验配置优先。当前运行器只读取实验 JSON 配置，不读取或合并 `configs/default.yaml`；缺省值由实验代码提供，不从 YAML 回退。通过 `--config` 指定其他实验 JSON 文件时，以该文件为准。

`configs/default.yaml` 是项目级配置提案。Git 历史显示，它在 2026/09/16 的项目执行计划与协作初始文件提交 `b564db7` 中创建，随后在 2026/09/26 的 P3 数据基础与统一导出提交 `1697e10`、`fa19dfc` 中补充数据设置。现有历史未显示它由其他 part 整合而来；它覆盖数据、检索、Agent、生成与评估多个模块，不能据此认定为某个 part 的运行配置。

| `configs/default.yaml` 设置 | 实验配置中的对应项 | 重复或差异及处理方式 |
| --- | --- | --- |
| `data.overlap_words`：$40$ | `overlap_words`：$40$ | 同一分块重叠设置，当前值相同；以实验配置为准。 |
| `retrieval.top_k`：$5$ | `top_k`：$5$ | 同一检索返回数量，当前值相同；以实验配置为准。 |
| `data.chunk_words`：$200$ | `candidates`：$325/335/345/350/355/365/375/385/395/400$ | 用途相关但结构不同；实验逐一比较 Round 3 候选大小，不采用 YAML 的单一大小。 |
| `seed`：$42$ | `seed`：$42$ | 用途和值相同；所有抽样过程使用实验配置中的种子，不读取 YAML。 |

YAML 的 `retrieval` 部分列出稠密模型、重排模型、候选数和 RRF 等提案设置，实验 JSON 当前仅指定 `retrieval.mode` 为 `bm25`，本次实验已确认使用此模式及 `top_k=5`。两者不是同一完整检索配置；本实验不会继承 YAML 的模型或融合参数。BM25 算法参数沿用实现的库默认值，属于检索器实现细节，不作为本次实验的待选配置或调优内容；输入、输出、完整流程及当前参数见 `experiments/chunk_size/BM25.md`。实验检索代码的缺省值和可选模式见 `experiments/chunk_size/README.md`。

除开头已列出的 `candidates` 外，当前实验 JSON 的全部设置如下；比较各候选分块大小时保持这些设置一致。

| 实验配置项 | 当前值 | 含义与约束 |
| --- | --- | --- |
| `overlap_words` | $40$ | 相邻分块重叠词数；每个候选分块大小必须大于该值。 |
| `top_k` | $5$ | 每个问题最多返回的分块数；当前指标约定要求固定为 $5$，可用分块不足时返回实际数量。 |
| `word_budgets` | $500/1000/2000$ | BM25 的互不重复正整数词数预算；独立于 top-$5$，保存足以支持最大预算的排名。 |
| `question_sample_count` | $50$ | 按下方筛选规则形成可用问题池后，计划抽取的问题数；不足时使用全部可用问题，并记录实际数量。 |
| `question_sampling_method` | `simple_random_without_replacement` | 从筛选后的问题池简单随机无放回抽样；当前唯一支持的方法。各候选配置共用抽中问题。 |
| `n_paper` | $5$ | 可读性抽样的计划论文数；可用论文不足时全部抽取。 |
| `n_paragraph` | $2$ | 每篇抽中论文的计划段落数；可用段落不足时全部抽取。 |
| `seed` | $42$ | 问题、论文及区间内段落抽样共用的种子；问题和可读性抽样各自用该值初始化随机生成器。 |
| `retrieval.mode` | `bm25` | 使用 P1 的 `BM25Retriever`，按问题所属论文检索；每种分块大小、每篇论文独立建索引，无需模型权重。 |

## 可读性抽样方案

从已核验的 `data/processed/papers.jsonl` 导出中，随机无放回抽取最多 `n_paper` 篇论文。仅使用原始 `train/validation` 中出现在全部候选语料、且包含非空可分块段落的论文；不要求论文出现在抽中的问题中。抽样前按论文 ID 排序。空段落和无名称章节按分块器规则排除。

每篇抽中论文按章节、段落索引排列可用段落，再划分为 `n_paragraph` 个连续区间；边界为 $\lfloor iL/k\rfloor$，其中 $i=0,\ldots,k$，$L$ 为可用段落数，$k=\min(L,\texttt{n\_paragraph})$。每个区间随机抽取一个段落，不足时全部抽取。各候选分块大小共用这批原文位置，使样本分散在少量论文的不同位置，无需覆盖每篇论文。

默认预算为 $5\times2=10$ 个原文段落。整批样本尽量兼顾长短段落，不要求每篇论文都覆盖。抽样后查看 `manifest.json` 中的 `readability_sampling.paragraph_word_counts` 和 `length_check`：不超过 $150$ 个空白分隔词记为短段落，超过则记为长段落。这只是覆盖检查分类，不是通过／不通过标准；代码不会自动重抽或保证数量相等。若覆盖或工作量不合适，在保存的新配置中调整样本量，保持统一种子并使用新 run ID。

审核工作量以 `manifest.json` 中的 `readability_review_chunk_counts` 和 `readability_review_chunk_count_total` 为准，不以原文段落数代替。每种大小纳入触及抽中段落的全部分块，并按 passage ID 去重；总量为各候选大小待评数量之和，各候选分别审核。`readability_sampling` 还记录计划／实际论文数、抽中论文 ID 和各篇实际段落数。人工审核前，标签均保留 `pending`。

旧配置键 `readability_sample_count`、`question_seed`、`readability_seed` 不再接受。自定义运行配置须迁移到 `n_paper`、`n_paragraph` 和 `seed`；已完成的历史运行仍可使用 `summarize`。

## 评估过程中需要保存什么

以下输出约定已实现，仍为 `v0-proposed`，待团队确认；运行命令见 `experiments/chunk_size/README.md`。所有路径都相对于项目根目录。每轮比较使用新的 `run_id`，避免覆盖已有结果。每种配置的文件保存在 `results/chunk_size/<run_id>/chunk_size_<size>/` 下，`<size>` 取该轮 `candidates` 中的值，例如 Round 2 的 `200`、`225`、`400`。这些实验结果文件提交到 Git 共享。

| 指标 | 代码需要保存的内容 | 配置目录下的文件 |
| --- | --- | --- |
| 可读性通过率（Readability pass rate） | 导出原文、原文位置（论文、章节、段落和字符范围）、分块 ID 和完整分块文字，供人工检查。不同配置使用相同抽查原文位置。按下方 Markdown 结构保存，每个分块填写 `pass` 或 `fail`，不通过时简要说明原因。 | `readability.md`：每个抽查原文一个二级章节。 |
| 证据命中率（Evidence Hit@$5$） | 保存每个抽查问题、答案及可定位的证据段落、检索分块及其段落覆盖情况，以及该问题是否命中的结果。不展示来源划分或是否纳入统计的字段。 | `evidence_review.md`：每个问题一个二级章节，与完整证据率共用。 |
| 完整证据率（Complete evidence rate@$5$） | 在同一问题章节中保存：是否完整覆盖至少一份答案标注的全部文字证据、满足条件的答案标注，以及未完整覆盖的答案标注还缺少哪些证据。 | `evidence_review.md`。 |
| 检索词数（Retrieved word count） | 在每个检索分块的子章节中增加词数，在每个问题的评估结果中保存检索总词数。 | `evidence_review.md`：与两个证据指标共用。 |

### 人工可读性检查文件结构

检查文件保存在 `results/chunk_size/<run_id>/chunk_size_<size>/readability.md`。每个抽查原文形成一个 `##` 章节，包含三个 `###` 子章节：原文、分块（ID 和文字）、评估结果。完整展示所有选中检查的分块，每个唯一分块 ID 对应一行评估结果。同一分块出现在多个原文样本中时，不重复计数。生成的检查报告遵循项目要求使用英文标题，如下所示。

```markdown
# Readability Review

## Source sample: <sample_id>

### Source text

Paper: <paper_id>; section: <section_index>; paragraphs: <paragraph_indices>; character span: <start:end>.

<Original source text, with enough context to check the chunk boundaries.>

### Chunks (ID and text)

Passage ID: `<passage_id>`

<Full chunk text. Repeat the ID and text for each selected chunk.>

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `<passage_id>` | pending | |
```

代码生成时填写 `pending`，人工检查后改为 `pass` 或 `fail`。判断可读性时，先看分块本身能否独立理解，再对照原文检查切断了什么。评分完成后，汇总代码读取结果表，以通过的唯一分块数除以全部已评分的唯一分块数。遇到未知标签或缺少结果行时应提示，不能直接算作不通过。

### 证据检查文件结构与问题抽样

两个证据指标和检索词数共用 `results/chunk_size/<run_id>/chunk_size_<size>/evidence_review.md` 展示；后续计算输入按“结构化数据保存与报告生成方案”保存为 JSONL。从 `data/processed/qa.jsonl` 抽样，不直接读取 raw data。抽样前要求：问题所属论文已进入所有待比较的检索库，至少有一份答案标注，且所有答案标注均具有非空文字证据，每份标注中的全部证据都能唯一定位到原文段落。任一标注存在空证据、原文缺失、重复段落导致定位歧义或 `FLOAT SELECTED` 证据，就排除整个问题，其已定位证据也不参与命中统计。被排除的问题不参与两个证据指标及检索词数统计。各分块大小使用同一批问题 ID。报告只展示筛选后抽中的可用问题，不展示来源划分、是否纳入统计或排除原因；原始来源信息保留在 `qa.jsonl` 中。

报告不展示来源划分，不代表改变现有留出集（held-out）约定。当前默认语料仅含原始 `train/validation` 论文。如果以后使用整个 `qa.jsonl`（含原始 `test` 问题）选择分块大小，需要配套检索语料并明确更新项目约定。参与选择分块大小的问题不能再视为独立的最终测试题。

证据段落使用 `paper_id + section_index + paragraph_index` 定位到 `papers.jsonl`；索引从 $0$ 开始，部分覆盖时补充段落内从 $0$ 开始、左闭右开的字符范围。各答案按标注分别保存，记录答案原文或答案值，以及每个引用段落的定位信息和完整原文。报告中的所有标注都已通过证据筛选，不得将空证据集合算作完整覆盖。筛选规则不改变完整证据率的判定：完整覆盖至少一份答案标注的全部证据即可。

每个问题一个 `##` 章节，包含四个 `###` 子章节；每份答案和前 $5$ 个检索分块分别形成独立的 `####` 子章节。生成报告使用英文标题和字段，问题、答案和段落原文保持原样。

```markdown
# Evidence Review

## Question: <question_id>

### Question ID and text

Question ID: `<question_id>`; paper ID: `<paper_id>`.

<Original question text.>

### Answers

#### Answer: <annotation_id>

<Original answer text or answer value.>

Evidence location: `<paper_id>:<section_index>:<paragraph_index>`

<Full original evidence paragraph. Repeat for each referenced paragraph.>

### Retrieved chunks

#### Rank 1: <passage_id>

Passage ID: `<passage_id>`; retrieval score: <score>.

Word count: <word_count>.

<Full chunk text. Repeat this subsection for each retrieved chunk.>

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `<paper_id>:<section_index>:<paragraph_index>` | full / partial | <start:end> |

### Evaluation results

Evidence Hit@5: <true or false>

Complete evidence rate@5: <true or false>

Total retrieved words: <sum of the retrieved chunks' word counts>.

Fully covered answer annotations: <annotation IDs, or none>.

Missing evidence by answer annotation: <paragraph locations and uncovered spans>.
```

代码根据检索分块合并后的原文覆盖范围计算逐问题结果，Markdown 用于展示和复查。每个分块列出触及的全部已标注证据段落，注明完整覆盖或部分覆盖；没有触及时填写 `none`。只有部分覆盖不算命中，但多个分块可以合起来覆盖完整段落。完整覆盖至少一个证据段落，算命中；完整覆盖至少一份可用答案标注的全部文字证据段落，算证据完整。两个汇总指标均以抽查问题数为分母，结果只代表这批样本上的表现。

词数按展示的分块文字计算，与分块代码一致：以 Unicode 空白字符分隔的连续非空白文本计为一个词，不按模型 token 计算。每个问题的检索总词数为各检索分块词数之和，重叠文字重复计数。`summary.json` 中的检索词数指标为同一批抽查问题的检索总词数的平均值。

另外，在 `results/chunk_size/<run_id>/manifest.json` 保存实际运行配置、代码提交号及工作区是否有修改、输入文件路径及哈希、划分策略版本、检索器／模型版本、依赖和随机种子。记录可读性抽查的原文位置、抽中问题 ID、计划和实际问题抽样数量、按原因分类的过滤数量及抽样随机种子，确保可以重复比较。实现运行代码时，还需遵循 `results/README.md` 的共享实验记录要求。

将比较结果保存在 `results/chunk_size/<run_id>/summary.json`：每种配置一条记录，包含四项指标值、适用指标的分子和分母，以及尚未完成人工评分的分块数。两个证据指标统计同一批抽中问题，与 `evidence_review.md` 展示的逐问题结果一致。所有抽查分块完成人工评分前，可读性通过率保存为 `null`；评分完成后，根据人工标签更新。不要把待评分当成不通过。
