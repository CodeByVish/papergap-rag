# 分块大小评估指标

比较每块 $150$、$200$、$250$ 个词的配置。使用从 `data/processed/qa.jsonl` 抽取的同一批问题、相同检索方法和重叠词数，每次检索前 $5$ 个分块。抽样前先执行下方的问题筛选规则。

| 指标 | 衡量什么 | 怎么判断分块大小的好坏 |
| --- | --- | --- |
| 可读性通过率（Readability pass rate） | 对每种配置，人工抽查相同原文位置对应的分块。如果不看前后分块，也能理解当前分块表达的意思，就算通过。通过率为通过的分块数除以抽查的分块数。 | 越高越好。通过率低，说明分块可能太小，把解释切碎了。 |
| 证据命中率（Evidence Hit@$5$） | 在有可用文字证据的问题中，前 $5$ 个检索分块合起来，包含至少一个完整人工标注证据段落的问题占比。证据段落被切到多个分块中，只要这些分块都被检索到、合起来覆盖完整段落，也算命中。 | 越高越好，说明更多问题能找到有用证据。命中一个证据段落，不代表已经找全回答所需的证据。 |
| 完整证据率（Complete evidence rate@$5$） | 在同一批问题中，前 $5$ 个检索分块合起来，包含至少一份答案标注所列全部文字证据段落的问题占比。 | 越高越好，说明证据找得更全，尤其适合判断需要多处证据的问题。 |
| 检索词数（Retrieved word count） | 每个问题检索到的前 $5$ 个分块的总词数，再对所有问题取平均。重叠文字如果被重复传给回答模型，就重复计数。 | 越低，模型需要阅读的文字越少。在证据检索效果和可读性接近时，优先选择词数更少的配置；不能只凭词数少判断质量更好。 |

两个证据指标都要核对证据所属的论文和原文段落，不能只看是否有几个词相同。抽样前过滤没有可用文字证据的问题，过滤数量记录在 `manifest.json` 中。

## 实验配置与优先级

本实验以 `experiments/chunk_size/config.json` 为配置依据；与 `configs/default.yaml` 中用途相同的设置重复或冲突时，实验配置优先。当前运行器只读取实验 JSON 配置，不读取或合并 `configs/default.yaml`；缺省值由实验代码提供，不从 YAML 回退。通过 `--config` 指定其他实验 JSON 文件时，以该文件为准。

`configs/default.yaml` 是项目级配置提案。Git 历史显示，它在 2026/09/16 的项目执行计划与协作初始文件提交 `b564db7` 中创建，随后在 2026/09/26 的 P3 数据基础与统一导出提交 `1697e10`、`fa19dfc` 中补充数据设置。现有历史未显示它由其他 part 整合而来；它覆盖数据、检索、Agent、生成与评估多个模块，不能据此认定为某个 part 的运行配置。

| `configs/default.yaml` 设置 | 实验配置中的对应项 | 重复或差异及处理方式 |
| --- | --- | --- |
| `data.overlap_words`：$40$ | `overlap_words`：$40$ | 同一分块重叠设置，当前值相同；以实验配置为准。 |
| `retrieval.top_k`：$5$ | `top_k`：$5$ | 同一检索返回数量，当前值相同；以实验配置为准。 |
| `data.chunk_words`：$200$ | `candidates`：$150$、$200$、$250$ | 用途相关但结构不同；实验逐一比较候选大小，不采用 YAML 的单一大小。 |
| `seed`：$42$ | `seed`：$42$ | 用途和值相同；所有抽样过程使用实验配置中的种子，不读取 YAML。 |

YAML 的 `retrieval` 部分列出稠密模型、重排模型、候选数和 RRF 等提案设置，实验 JSON 当前仅指定 `retrieval.mode` 为 `bm25`，本次实验已确认使用此模式及 `top_k=5`。两者不是同一完整检索配置；本实验不会继承 YAML 的模型或融合参数。BM25 算法参数沿用实现的库默认值，属于检索器实现细节，不作为本次实验的待选配置或调优内容；输入、输出、完整流程及当前参数见 `experiments/chunk_size/BM25.md`。实验检索代码的缺省值和可选模式见 `experiments/chunk_size/README.md`。

除开头已列出的 `candidates` 外，当前实验 JSON 的全部设置如下；比较各候选分块大小时保持这些设置一致。

| 实验配置项 | 当前值 | 含义与约束 |
| --- | --- | --- |
| `overlap_words` | $40$ | 相邻分块重叠词数；每个候选分块大小必须大于该值。 |
| `top_k` | $5$ | 每个问题最多返回的分块数；当前指标约定要求固定为 $5$，可用分块不足时返回实际数量。 |
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

以下输出约定已实现，仍为 `v0-proposed`，待团队确认；运行命令见 `experiments/chunk_size/README.md`。所有路径都相对于项目根目录。每轮比较使用新的 `run_id`，避免覆盖已有结果。`run_id` 标识一轮比较；配置目录分别命名为 `chunk_size_150`、`chunk_size_200`、`chunk_size_250`。每种配置的文件保存在 `results/chunk_size/<run_id>/chunk_size_<size>/` 下，将 `<size>` 替换为 `150`、`200` 或 `250`。生成文件不提交到 Git。

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

两个证据指标和检索词数共用 `results/chunk_size/<run_id>/chunk_size_<size>/evidence_review.md`，无需单独保存检索明细文件。从 `data/processed/qa.jsonl` 抽样，不直接读取 raw data。抽样前要求：问题所属论文已进入所有待比较的检索库，且至少一份答案标注具有非空、全部可定位的文字证据段落。各分块大小使用同一批问题 ID。报告只展示筛选后抽中的可用问题，不展示来源划分、是否纳入统计或排除原因；原始来源信息保留在 `qa.jsonl` 中。

报告不展示来源划分，不代表改变现有留出集（held-out）约定。当前默认语料仅含原始 `train/validation` 论文。如果以后使用整个 `qa.jsonl`（含原始 `test` 问题）选择分块大小，需要配套检索语料并明确更新项目约定。参与选择分块大小的问题不能再视为独立的最终测试题。

证据段落使用 `paper_id + section_index + paragraph_index` 定位到 `papers.jsonl`；索引从 $0$ 开始，部分覆盖时补充段落内从 $0$ 开始、左闭右开的字符范围。各答案按标注分别保存，记录答案原文或答案值，以及每个引用段落的定位信息和完整原文。某份答案没有可用文字证据时注明，不得将空证据集合算作完整覆盖。

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
