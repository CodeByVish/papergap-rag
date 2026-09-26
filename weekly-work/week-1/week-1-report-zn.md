# 第 1 周工作报告：QASPER 数据基础

截至 $2026$ 年 $9$ 月 $26$ 日

## 1. 摘要与范围

本周我完成了固定版 QASPER 的获取与质检（acquisition and quality checks）、论文与问答分离导出、文本块（passage）模型与构建流程，并对固定版本中的图表与表格证据可用性做了定向审计；同时整理了 $100$ 条依赖样本及两种语料范围的计量结果。开发语料数字沿用 `data/README.md` 的既有基准，全论文正文语料数字依据本地 manifest。本报告记录本人已完成且有来源可核对的工作；split 角色映射和 Passage 接口仍是待团队确认的 `v0-proposed` 提案，后续检索与问答实验不属于本周成果。

工作主线为：固定版原始数据获取与质检 → 论文/问答分离导出 → `Passage` 定义与构建 → $100$ 条样本及两个语料范围的计量核对 → 图表和表格可用性核验。原始 split 保持不变，下载的原始数据和生成工件保留在本地忽略目录。

## 2. 固定数据来源、获取逻辑与质检

输入为 `allenai/qasper` 配置 `qasper`，固定修订 `fdc9d8214fbab5dd782958601db4d678e6934a54`，来源版本 `0.3.0`。固定完整修订号使输入版本可追溯。获取程序核对官方归档的声明大小和 SHA-256，只读取清单中允许的归档成员，并生成包含版本、split 文件行数和哈希的 `manifest.json`；获取阶段保留未清洗、未分块的原始 `train`、`validation`、`test` 记录。离线检查器先验证 manifest、split 哈希与行数，再读取结构并生成检查报告。

| 官方 split | 论文数 | 问题数 | 答案标注数 | 原始文件 SHA-256 |
| --- | ---: | ---: | ---: | --- |
| `train` | $888$ | $2{,}593$ | $2{,}675$ | `7a25389963d05d97de9462d4e46b2ef367f37b898de55f5833bae7aa4b6e8732` |
| `validation` | $281$ | $1{,}005$ | $1{,}764$ | `f3e8f8072bbb42c6f770cdbc311672738683505eef401a7b75e0c08cfb7c5945` |
| `test` | $416$ | $1{,}451$ | $3{,}554$ | `308380c3da5287ac450582c457a9a75303b8361360dd88e727afd021c8320779` |
| 合计 | $1{,}585$ | $5{,}049$ | $7{,}993$ | — |

一行原始 JSONL 对应一篇论文；问题数是所有论文 `qas` 列表长度之和，答案标注数是所有问题 `answers` 列表长度之和，同一答案标注中的字段或证据项不另计为答案。检查报告记录三个官方 split 的论文 ID 两两不交叉，也没有 split 内重复论文 ID；这是对发布数据划分的观察，不自动确定项目评估角色。

质检观察到 $1$ 篇论文的 `full_text` 是空列表、$8$ 个章节名去除首尾空白后为空、$12$ 个章节名为 `null`，以及 $1{,}537$ 个空白段落字符串。它们是原始结构统计，不表示获取或检查程序丢弃了整篇论文。上述 split 计数与结构异常来自 `docs/QASPER_DATASET_INSPECTION.md`；原始文件 SHA-256 与本地 `data/raw/qasper/manifest.json` 一致。

## 3. 原始结构与统一导出

数据流为：三个原始 split（每篇论文内嵌 `qas`）→ 只读投影 → `papers.jsonl`（一行一篇论文）＋`qa.jsonl`（一行一个问题）＋`qasper_export.manifest.json`。三个 split 在派生文件中按 `train`、`validation`、`test` 顺序写入；每条派生记录保留 `source_split` 以追溯原始来源。物理合并不改变官方 split 或项目评估边界。

字段类型参照固定版 [QASPER 0.3.0 schema](https://huggingface.co/datasets/allenai/qasper/blob/fdc9d8214fbab5dd782958601db4d678e6934a54/dataset_infos.json)；下表以 JSON 类型表示，`array<T>` 表示元素类型为 `T` 的数组，`null` 表示 JSON 空值。

### 原始论文记录

| 字段名 | 类型 | 含义 |
| --- | --- | --- |
| `id` | `string` | 来源论文 ID；导出的问答记录用 `paper_id` 指向它。 |
| `title` | `string` | 论文标题；作为原始字段保留。 |
| `abstract` | `string` | 论文摘要；作为原始字段保留。 |
| `full_text` | `array<object>` | 有序正文章节列表；每项含 `section_name`（`string` 或 `null`）和 `paragraphs`（`array<string>`），供正文 Passage 构建使用。 |
| `figures_and_tables` | `array<object>` | 图表条目列表；每项含 `caption`（`string`）和 `file`（`string` 文件名），元数据不等于可用图像文件。 |
| `qas` | `array<object>` | 论文内嵌的问题及完整答案标注；导出时从论文记录移出。 |

### `papers.jsonl`

该文件保留原始论文记录表中的论文字段，但移除 `qas`，并增加以下来源字段。

| 字段名 | 类型 | 含义 |
| --- | --- | --- |
| `source_split` | `string` | 该论文来自官方 `train`、`validation` 或 `test` split；原始论文记录本身没有此字段。 |

### `qa.jsonl`

每行是一道问题记录，保留完整问题对象与答案标注，并增加关联论文和来源 split 的字段。

| 字段名 | 类型 | 含义 |
| --- | --- | --- |
| `question_id` | `string` | 问题 ID。 |
| `paper_id` | `string` | 所属论文 ID，对应 `papers.jsonl` 的 `id`。 |
| `source_split` | `string` | 来源论文所在的官方 `train`、`validation` 或 `test` split。 |
| `question` | `string` | 问题文本。 |
| `answers` | `array<object>` | 该问题的完整答案标注数组；每项结构见下方“答案标注”。 |
| `nlp_background` | `string` | 提问者报告的 NLP 经验背景。 |
| `paper_read` | `string` | 记录提问者是否读过论文的状态。 |
| `question_writer` | `string` | 提问者 ID。 |
| `search_query` | `string` | 提问者用于从候选摘要中找到该论文摘要的检索词；可为空字符串。 |
| `topic_background` | `string` 或 `null` | 提问者对论文主题的熟悉程度；原始数据允许为 `null`。 |

### 答案标注

`answers` 数组中的每一项是一条答案标注。

| 字段名 | 类型 | 含义 |
| --- | --- | --- |
| `annotation_id` | `string` | 答案标注 ID。 |
| `worker_id` | `string` | 答案标注者 ID。 |
| `answer` | `object` | 标注的答案内容，包含证据、答案文本或标签；字段见下表。 |

### 答案内容

| 字段名 | 类型 | 含义 |
| --- | --- | --- |
| `answer.evidence` | `array<string>` | 标注者用于作答的证据段落、图或表的文本项。 |
| `answer.extractive_spans` | `array<string>` | 从论文中抽取的答案片段列表。 |
| `answer.free_form_answer` | `string` | 自由文本答案。 |
| `answer.highlighted_evidence` | `array<string>` | 标注者选中的证据句子；这些句子比 `evidence` 中的段落级文本更细。 |
| `answer.unanswerable` | `bool` | 标记该问题是否无法回答。 |
| `answer.yes_no` | `bool` 或 `null` | 是／否答案标签；可为布尔值或 JSON `null`。 |

`papers.jsonl` 保留原论文顶层字段、移除 `qas`，再增加 `source_split`；`qa.jsonl` 保留完整原始问题对象和所有答案标注，再增加 `paper_id` 与 `source_split`。两份文件以 `paper_id` 关联。检索语料构建器只读论文导出，不会从 `qa.jsonl` 读取问题、答案或证据标注。

导出器拒绝重复论文 ID 和问题 ID。独立检查器核对输入来源、输出文件哈希、行数、split 计数、答案标注计数，以及每个问题与论文的 ID 和 split 关联；现有逐条投影比较记录显示原始论文及问题的字段和值一致。对 `test` 文件的结构复核仅用于机械投影、计数、哈希与关联检查，没有预览 `test` 问题或答案文本，也没有据此调参。

## 4. `Passage` 模型、构建原理与 ID

当前公有 `Passage` 模型包含 $8$ 个字段，字段集合和序列语义标记为 `v0-proposed`。下表中的“空值”描述 JSON 表示；除两个邻接字段外，字段都要求非空值。

| 字段 | 类型或空值 | 语义 | 构建规则或下游用途 |
| --- | --- | --- | --- |
| `passage_id` | 非空字符串 | Passage 的稳定引用 ID。 | 由固定数据与转换上下文及来源坐标生成；供去重和引用使用。 |
| `paper_id` | 非空字符串 | 来源论文 ID。 | 对应原始论文 `id`。 |
| `title` | 非空字符串 | 规范化后的论文标题。 | 仅做换行和首尾空白规范化；空白标题不会生成 passage。 |
| `section` | 非空字符串 | 展示用章节名。 | 章节名不用于判定源容器边界，也不因同名而合并章节。 |
| `chunk_number` | 从 $0$ 开始的整数 | 单个源容器内连续的块序号。 | 等于 ID 坐标中的 `chunk_index`；每个容器从 $0$ 重新编号。 |
| `text` | 非空字符串 | 单个源容器中的正文块。 | 按 Unicode 非空白词串切分；不跨论文或章节边界。 |
| `previous_passage_id` | 非空字符串或 JSON `null` | 同一源容器中的直接前一块。 | 容器首块为 `null`；其他值指向直接前邻。 |
| `next_passage_id` | 非空字符串或 JSON `null` | 同一源容器中的直接后一块。 | 容器末块为 `null`；其他值指向直接后邻。 |

当前构建器只读取论文 `id`、`title` 和 `full_text`；它不会读取 `qas`、问题、答案、证据或图表元数据。每个原始 `full_text[section_index]` 都单独作为一个源容器处理，同名章节不合并。同一章节内的多个有效段落按原序用空行连接后分块。文本规范化（normalization）将 CRLF 和 CR 行尾统一为 LF、移除段落首尾空白并丢弃空段落；内部空白、大小写、标点、Unicode 内容、段落顺序和证据标记原样保留。章节名和标题也只做行尾与首尾空白处理。分块（chunking）按 Unicode 非空白词串（`\S+`）计数；当前窗口为 $200$ 词，重叠 $40$ 词，步长 $160$ 词。这是当前工作配置，不是实验最优值或冻结参数。

空白或 `null` 章节名、没有有效正文的章节会跳过；结构不合法的章节会报错。跳过的章节仍保留原始 `section_index` 坐标，后续章节不重编号。`source_split`、`section_index`、`source_kind` 是导出来源信息、内部坐标或 manifest 元数据，不属于当前公有 $8$ 字段；目前实际构建的来源类型是 `full_text`。

ID 的内部坐标为 `(paper_id, source_kind, section_index, chunk_index)`。哈希输入还包含固定数据修订、解析器版本、文本规范化版本、分块版本和块大小/重叠参数；最终格式为 `qasper-passage-v1-` 加 $64$ 位小写 SHA-256。显示标题、章节名、`source_split` 和输出行号不参与 ID。这样即使章节显示名相同也不会跨容器混合，且同一固定输入与配置下的引用和去重键保持稳定。邻接仅连接相同 `(paper_id, source_kind, section_index)` 中的直接相邻块；每个容器的首尾连接为 JSON `null`。抽象摘要和图表条目虽在 ID 坐标类型中预留，目前并未生成这两类 passage。

原始 `section_index` 是 `full_text` 章节列表中的从 $0$ 开始的位置，即使前面的章节被跳过也不重编号。当前 ID 上下文使用解析器版本 $1$、`text-normalization-v1` 和 `word-chunking-v1`。

## 5. 样本、完整语料与统计口径

$100$ 条依赖样本只使用 `train` 与 `validation` 的论文正文，按稳定论文顺序选择完整章节块组，每篇论文最多选一组，最终由 $100$ 篇不同论文组成。样本用于接口和可复现检查，不能代表完整语料规模；本地 `sample_passages_100.manifest.json` 记录的文件 SHA-256 为 `d017b7937d2e9a54ee653c8a3a94f37afa2819d548c0f79eacc93f08832bdb42`。

| 语料范围 | 来源 split | 用途 | 来源论文数 | 实际产生 passage 的论文数 | 唯一 passage 数 | 去重叠来源词数 | 含重叠 passage 词数 | SHA-256 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `development` | `train` + `validation` | 开发语料 | $1{,}169$ | $1{,}168$ | $32{,}073$ | $4{,}262{,}446$ | $4{,}897{,}846$ | `abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790` |
| `all-paper-text` | 三个官方 split 的论文正文 | `index_for_inference` | $1{,}585$ | $1{,}584$ | $42{,}719$ | $5{,}659{,}921$ | $6{,}495{,}041$ | `32fa43714d6be6822636fd8513af8358cfff78474d50f7c310a1b90d28a868fa` |

“来源论文数”是进入该语料范围的论文数；“实际产生 passage 的论文数”只计至少生成一个正文块的论文；两者差 $1$，但现有统计没有逐篇对应证据，不能断言缺少 passage 的论文就是那篇 `full_text` 为空的论文。“唯一 passage 数”按 `passage_id` 去重。去重叠来源词数对实际参与生成 passage 的来源段落每段只计一次；含重叠 passage 词数对输出块逐块计数，因此包含相邻窗口的重复词。计数使用 Unicode 非空白词串。

项目规模门槛为至少 $10{,}000$ 个 passage 和 $100{,}000$ 个词。当前开发语料超过门槛；这些是语料规模统计，不代表检索或问答性能。`development` 行的数字和哈希来自 `data/README.md` 记录的既有基准，当前工作区没有对应开发语料 JSONL 或 manifest，故不称为本次重建验证结果。`all-paper-text` 行来自当前本地 `data/processed/passages_all_paper_text.manifest.json`，与其统计和 SHA-256 一致。

## 6. split 隔离、图表与表格限制

官方 split 与项目角色的映射仍为 `v0-proposed`：`train → development`、`validation → validation`、`test → held_out`。映射按整篇论文隔离，不按问题或 passage 重新随机拆分；官方论文 ID 互斥是检查观察，项目角色映射与最终评估冻结尚未完成确认。`all-paper-text` 包含 `test` 论文正文，只用于推理索引。`test` 问题、答案、证据与人工标签不得用于调参、prompt 设计或分块参数选择。

现有专项图表审计记录：$1{,}551$ 篇论文含图表条目，共 $11{,}364$ 条引用，其中表格 $6{,}492$ 条、图片 $4{,}872$ 条。图表记录提供 caption 与 `.png` 文件名，但固定官方归档没有对应图像，本地可定位图像为 $0/11{,}364$。这些图表引用数来自报告中的专项审计，并非 manifest 自动统计或当前重新执行的审计。

论文 `full_text` 有时会复述个别表格事实，但不能保证提供完整单元格数据；定向抽样既发现正文可回答的情况，也发现证据只存在于缺失表格图像的情况。因此，基于正文 passage 的证据召回会受限。`FLOAT SELECTED: ` 是观察到的证据标记，但没有映射到具体图表条目。定向样本不能用于推算整体问答覆盖率。

## 7. 交付物、复现入口与结论

| 产物 | 作用 | 来源、状态或复现入口 |
| --- | --- | --- |
| `data/raw/qasper/manifest.json` | 固定输入版本、split 行数与哈希。 | 随下载生成；当前本地存在，原始数据目录不入 Git。 |
| `data/processed/qasper_inspection.json` | split 结构与异常计数报告。 | 由 `scripts.inspect_qasper` 生成；检查文档记录的 SHA-256 为 `deff21fdc2297dbd5b23299f243a214e4d92bd8b26cd544d6d1e0d6184f7f81a`，文件当前未保留。 |
| `data/processed/papers.jsonl`、`qa.jsonl`、`qasper_export.manifest.json` | 论文/问答分离导出及计数、关联、哈希元数据。 | 由 `scripts.export_qasper` 生成；当前本地存在，派生数据目录不入 Git。 |
| `data/processed/sample_passages_100.jsonl` 与其 manifest | $100$ 条接口复现样本及选择、统计和哈希记录。 | 由 `scripts.build_sample_passages` 生成；当前本地存在。 |
| `data/processed/passages.jsonl` 与 `passages.manifest.json` | `development` 完整语料基准。 | 文件与 manifest 当前未保留；`data/README.md` 留有可复现基准计数和哈希。 |
| `data/processed/passages_all_paper_text.jsonl` 与其 manifest | 含三 split 论文正文的推理索引。 | 由 `scripts.build_corpus --scope all-paper-text` 生成；当前本地存在，仅用于推理索引。 |

完整字段和运行细节见 [`data/README.md`](../../data/README.md)。下列命令从仓库根目录运行，展示从固定输入到样本及两种语料的完整复现链。示例使用新的输出名称；下载目录、导出文件、样本和语料输出均要求目标不存在。再次复现时为所有输出改用尚未使用的名称。复现会下载并生成本地数据；本周报告编辑没有运行这些命令。

```powershell
python -m scripts.download_qasper --output-dir data/raw/qasper-week1-reproduction --revision fdc9d8214fbab5dd782958601db4d678e6934a54
python -m scripts.inspect_qasper --input-dir data/raw/qasper-week1-reproduction --output data/processed/qasper_inspection_week1_reproduction.json
python -m scripts.export_qasper --input-dir data/raw/qasper-week1-reproduction --papers-output data/processed/papers_week1_reproduction.jsonl --qa-output data/processed/qa_week1_reproduction.jsonl --manifest-output data/processed/qasper_export_week1_reproduction.manifest.json
python -m scripts.check_qasper_export --papers data/processed/papers_week1_reproduction.jsonl --qa data/processed/qa_week1_reproduction.jsonl --manifest data/processed/qasper_export_week1_reproduction.manifest.json
python -m scripts.build_sample_passages --papers data/processed/papers_week1_reproduction.jsonl --export-manifest data/processed/qasper_export_week1_reproduction.manifest.json --output data/processed/sample_passages_100_week1_reproduction.jsonl --manifest-output data/processed/sample_passages_100_week1_reproduction.manifest.json
python -m scripts.build_corpus --papers data/processed/papers_week1_reproduction.jsonl --export-manifest data/processed/qasper_export_week1_reproduction.manifest.json --scope development --output data/processed/passages_development_week1_reproduction.jsonl --manifest-output data/processed/passages_development_week1_reproduction.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages_development_week1_reproduction.jsonl --manifest data/processed/passages_development_week1_reproduction.manifest.json
python -m scripts.build_corpus --papers data/processed/papers_week1_reproduction.jsonl --export-manifest data/processed/qasper_export_week1_reproduction.manifest.json --scope all-paper-text --output data/processed/passages_all_paper_text_week1_reproduction.jsonl --manifest-output data/processed/passages_all_paper_text_week1_reproduction.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages_all_paper_text_week1_reproduction.jsonl --manifest data/processed/passages_all_paper_text_week1_reproduction.manifest.json
```

`data/raw/` 与 `data/processed/` 中的原始数据和生成 JSONL、manifest 不进入 Git；队友可按 `data/README.md` 和上述命令在本地复现。报告保留工件文件名、计数口径和来源哈希，不包含问题、答案、证据或大段样本内容。

本周形成的数据基础是：可复现的固定版获取与质检、论文/问答完整分离导出、只依赖论文正文的八字段 Passage 构建、$100$ 条依赖样本，以及达到课程规模门槛的开发语料基准和全论文正文推理索引。当前限制是图像文件缺失且表格正文不完整，当前分块参数尚未优化，`Passage` 接口与 split 角色映射仍为 `v0-proposed`；定向图表抽样不能提供总体覆盖结论。
