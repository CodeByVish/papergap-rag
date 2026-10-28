# QASPER 数据指南

[English](README.md)

原始数据和处理后数据均不纳入 Git。本指南说明版本化 Release 共享方式、本地复现流程及每份处理后文件的字段。所有命令均从仓库根目录、使用项目 Python 3.11 环境运行；先安装 `requirements.txt` 或 `requirements-dev.txt`。

## 数据包与更新

约定将 `data/raw/` 与 `data/processed/` 一起作为版本化 GitHub Release 附件发布，并关联 `p3` 的精确提交。保留全部配套 manifest、来源许可声明和溯源信息。代码和中英文文档纳入 Git；数据及压缩包继续忽略。

本次文档修改尚未发布数据 Release。[仓库 Releases 页面](https://github.com/CodeByVish/papergap-rag/releases) 仅为入口，不表示已有数据包。发布后，应在两份指南中同步填写实际版本对应的附件链接及代码提交。

### 发布一个版本

1. 在独立的本地暂存目录中重建变化的输出，保留标准文件名，并同步重建依赖产物及 manifest。选定发布文件前检查哈希、结构、范围和引用。新版本验证通过前保留旧的本地快照。

2. 使用新版本名，例如先 `data-v1`、再 `data-v2`；这些只是示例，并非已发布版本。在 Release 说明中记录 `p3` 精确代码提交、上游 revision、解析/规范化/切分版本、切分参数、包含文件、评估范围、变化及验证结果。

3. 仅打包 `data/raw/` 和选定的完整 `data/processed/` 输出，保留相对 `data/` 的路径。每份 JSONL 必须带上对应 manifest。排除凭据、缓存、暂存文件、模型权重、索引及个人笔记。可选检查报告仅在重新生成且明确选中时纳入。

4. 将压缩包和独立的 SHA-256 校验文件上传为 Release 附件。保留旧版本；数据变化后发布新 Release，不静默替换已发布附件。同步更新两份指南中的下载链接。目前采用手动发布，后续如需自动化再单独配置。

以下打包示例假设已选定并验证的文件位于标准目录，且 `tmp/` 已存在。将示例版本改为准备发布的新版本；压缩包顶层为 `raw/` 和 `processed/`。同版本压缩包已存在时，不要覆盖。

```powershell
$packageVersion = 'data-v1'
$packagePath = "tmp/tmp_qasper-$packageVersion.zip"
Compress-Archive -LiteralPath data/raw,data/processed -DestinationPath $packagePath
$packageHash = (Get-FileHash -LiteralPath $packagePath -Algorithm SHA256).Hash.ToLowerInvariant()
$checksumLine = "$packageHash  tmp_qasper-$packageVersion.zip`n"
[System.IO.File]::WriteAllText("$packagePath.sha256", $checksumLine, [System.Text.UTF8Encoding]::new($false))
```

### 下载与使用

选择指定的数据 Release，并检出其记录的代码提交。下载 ZIP 及校验文件，将 `Get-FileHash -LiteralPath <downloaded-zip> -Algorithm SHA256` 的结果与发布的校验值比较，先解压到独立目录。备份已有本地数据后，再将已验证的 `raw/` 和 `processed/` 目录复制到仓库的 `data/` 中。manifest 与数据文件保持相邻，并执行下文检查。不要单独修改 JSONL 而不重建对应 manifest 及依赖产物。

下载数据包不改变评估使用权限：默认策略下，留出集的问题、答案和证据仍受限制。显式的 `all-splits-testing` 产物属于普通测试，不能用于声称独立留出评估结果。

## 目录结构与构建顺序

下列目录树列出标准产物；诊断报告为可选文件，可能不存在。`README_zh-CN.md` 与 `README.md` 一起纳入 Git；生成文件继续忽略。

```text
data/
├── README.md                                           # English guide / 英文指南
├── README_zh-CN.md                                     # Chinese guide / 中文指南
├── raw/                                                # Ignored source data / 忽略的源数据
│   └── qasper/
│       ├── manifest.json                               # Source metadata and hashes / 来源及哈希
│       ├── train.jsonl
│       ├── validation.jsonl
│       └── test.jsonl
└── processed/                                          # Ignored generated outputs / 忽略的生成产物
    ├── papers.jsonl
    ├── qa.jsonl
    ├── qasper_export.manifest.json
    ├── passages.jsonl
    ├── passages.manifest.json
    ├── paper_catalog.json
    ├── passages_all_paper_text.jsonl
    ├── passages_all_paper_text.manifest.json
    ├── gold_evidence_mapping.jsonl
    ├── gold_evidence_mapping.manifest.json
    ├── gold_evidence_mapping_all_splits.jsonl
    ├── gold_evidence_mapping_all_splits.manifest.json
    ├── sample_passages_100.jsonl
    ├── sample_passages_100.manifest.json
    └── qasper_inspection.json                          # Optional diagnostics / 可选诊断
```

构建顺序：原始采集 → `papers.jsonl`、`qa.jsonl` 和导出 manifest → 开发/全论文正文语料及样本 → 证据映射。下文每份文件均有独立生成命令和字段表；重复列出的命令会同时生成配套文件，每个独立构建只需执行一次。

除可选检查器会替换报告外，各构建器拒绝已存在的输出路径。重建时使用新的暂存目录，并同步调整全流程的输入/输出路径。语料和样本 CLI 不读取 YAML，旧默认值为 $200/40$ 词，因此必须显式传入选定的 $365/40$ 参数。这里是词数，不是模型 token 数。

字段表使用 JSON 类型。点路径和 `[]` 表示嵌套字段；`<split>` 表示 `train`、`validation` 或 `test`，`<input>` 表示已列出的输入名称。源数据导出也保留可能存在的额外原始字段；表格描述固定 QASPER 来源和当前导出器，不表示会修复原始结构。

## 原始 QASPER 采集

### 生成命令

```powershell
python -m scripts.download_qasper --output-dir data/raw/qasper --revision fdc9d8214fbab5dd782958601db4d678e6934a54
```

采集将上游 `dev` 映射为本地 `validation`，`train` 和 `test` 保留原名。每个原始 JSONL 行是一篇完整论文，包含 `id`、`title`、`abstract`、`full_text`、`figures_and_tables`、`qas`。`qas[]` 使用 `qa.jsonl` 章节说明的问题字段，但没有新增的 `paper_id` 和 `source_split`。论文内容字段与 `papers.jsonl` 一致，但没有 `source_split`。原始记录尚未规范化或切块。

`--output-dir` 必填。已有目标目录会被拒绝，除非指定 `--force`；该选项整体替换已验证的采集并支持回滚，不是追加或断点续传。可接受的原始目录只能包含 `manifest.json`、`train.jsonl`、`validation.jsonl`、`test.jsonl`。命令需要访问 Hugging Face Hub 和官方源压缩包；QASPER 为公开数据，无需 Hugging Face token。

### 原始 manifest 字段

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | manifest 协议版本。 |
| `dataset` | `object` | 数据集 ID/config、请求及解析后的 revision、源数据集版本、本地解析器版本。 |
| `licenses` | `object` | Hub 和源数据的许可声明；再分发时保留。 |
| `repository_files` | `array<object>` | 固定 qasper.py 及 dataset_infos.json 的字节数和 SHA-256。 |
| `splits` | `array<object>` | 每份 JSONL 的划分名、文件名、行数、字节数和 SHA-256。 |
| `source_verification` | `string` | 固定验证协议标识。 |
| `source_archives` | `array<object>` | 官方 URL、声明/实测字节数和哈希、必需成员。 |
| `libraries` | `object` | Python 和 huggingface-hub 运行版本。 |
| `output` | `object` | 编码、换行、聚合哈希算法及 aggregate_sha256。 |

采集只将固定的 `qasper.py` 和 `dataset_infos.json` 作为字节验证，不执行远程代码，也不使用 `trust_remote_code`。两个官方压缩包的字节数、SHA-256 和必需成员必须一致；不将压缩包解压到磁盘。来源、指纹或结构变化时直接报错。`--revision main` 仅用于上游检查，不是团队复现命令。聚合哈希按 JSONL 相对路径排序，覆盖各路径及单文件哈希，不包含 `manifest.json`。原始 JSONL 为 UTF-8、LF、递归排序键的紧凑格式；保留清单以复现。

## `data/processed/papers.jsonl`

每行一篇论文，包含全部官方划分。保留除 qas 外的全部原始顶层字段，新增 source_split。它是段落构建器的纯论文输入。

### 生成命令

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `id` | `string` | 原始论文标识。 |
| `title` | `string` | 原始论文标题。 |
| `abstract` | `string` | 原始摘要；当前不参与索引。 |
| `full_text` | `array<object>` | 按原始顺序排列的章节。 |
| `full_text[].section_name` | `string or null` | 原始章节名称；段落构建器跳过空白或 null 名称的章节。 |
| `full_text[].paragraphs` | `array<string>` | 规范化前、按原始顺序排列的段落。 |
| `figures_and_tables` | `array<object>` | 原始图表元数据；当前不参与索引。 |
| `figures_and_tables[].caption` | `string` | 原始图表说明。 |
| `figures_and_tables[].file` | `string` | 源图表文件引用；并非随包提供的图片。 |
| `source_split` | `string` | 官方划分：train、validation 或 test。 |

## `data/processed/paper_catalog.json`

供 UI 一次加载论文选择列表的轻量元数据，在选定的 passage 语料构建后生成；UI 尚未集成。下列命令使用 `configs/default.yaml` 中 `data.passages_path` 指定的语料。必填参数 `--passages` 必须指向 UI 检索实际使用的文件；语料变化后，在新的暂存路径重建目录，验证后再替换本地快照。脚本拒绝已存在的输出路径。

### 生成命令

```powershell
python -m scripts.build_paper_catalog --papers data/processed/papers.jsonl --passages data/processed/passages.jsonl --output data/processed/paper_catalog.json
```

仅收录实际存在 passage 的论文和章节。导出文件中的论文 ID、语料中的 passage ID 必须唯一；每条 passage 必须有非空正文，并引用导出文件中的论文及规范化章节。论文按导出顺序排列；章节按 `full_text` 中首次出现的顺序排列，规范化后同名的章节合并计数，因为章节过滤使用名称。章节名遵循 passage 规范化规则：统一为 LF 换行并去除首尾空白。缺失或空白元数据字符串为 `null`，缺失作者列表为 `[]`，不推测补写作者。这里的可检索表示有 passage 可参与检索，不保证每次查询命中。

### 字段表

| 字段名 | JSON 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | 暂定目录协议，`v0-proposed`。 |
| `passages_file` | `string` | 实际 `--passages` 输入路径，使用正斜杠；从仓库根目录构建时，相对路径以仓库根目录为基准。UI 检索必须使用同一份语料。 |
| `papers` | `array<object>` | 至少有一条 passage 的可选论文。 |
| `papers[].paper_id` | `string` | 唯一的源论文 ID。 |
| `papers[].title` | `string or null` | 源标题，缺失时为 `null`。 |
| `papers[].authors` | `array<string or null>` | 来源提供的作者；缺失字符串为 `null`，缺失作者列表为空。当前固定版本的 QASPER 导出不含作者。 |
| `papers[].passage_count` | `integer` | 该论文在所选语料中的 passage 总数。 |
| `papers[].sections` | `array<object>` | 所选语料中实际存在的章节，按原文顺序排列。 |
| `papers[].sections[].name` | `string or null` | 规范化的源章节名；缺失且语料中存在空章节 passage 时为 `null`。当前语料构建器丢弃无名称章节。 |
| `papers[].sections[].passage_count` | `integer` | 该论文、该章节名对应的 passage 数；各章节计数之和等于论文计数。 |

本地复现时，先按本指南相应命令生成 `papers.jsonl` 和所选 passage 语料，再执行目录构建命令。使用 Release 时，遵循前述下载、校验及解压流程，保留与目录匹配的语料；若数据包未包含目录，可在本地生成。本次变更未发布目录的 Release 下载链接。路径只记录所选文件，不包含内容哈希；替换语料后必须重建目录。

## `data/processed/qa.jsonl`

每行一个原始问题，保留全部答案标注。包含全部官方划分；仅新增 paper_id 和 source_split，不过滤原始问答字段。通过 paper_id 关联论文，再通过证据匹配得到块 ID。

### 生成命令

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `question_id` | `string` | 原始问题标识。 |
| `paper_id` | `string` | 关联 papers.jsonl 的 id。 |
| `source_split` | `string` | 官方来源划分；普通测试模式也保留此字段。 |
| `question` | `string` | 原始问题文本。 |
| `nlp_background` | `string` | 提问者的 NLP 背景。 |
| `paper_read` | `string` | 原始论文阅读情况记录。 |
| `question_writer` | `string` | 原始提问者标识。 |
| `search_query` | `string` | 原始检索查询。 |
| `topic_background` | `string` | 提问者的主题背景。 |
| `answers` | `array<object>` | 全部备选答案标注；分别保留。 |
| `answers[].annotation_id` | `string` | 原始标注标识。 |
| `answers[].worker_id` | `string` | 原始标注者元数据；不作为相关性监督。 |
| `answers[].answer` | `object` | 原始答案内容。 |
| `answers[].answer.evidence` | `array<string>` | 标注的证据文本，可能包含 FLOAT SELECTED 标记。 |
| `answers[].answer.extractive_spans` | `array<string>` | 抽取式参考答案片段。 |
| `answers[].answer.free_form_answer` | `string` | 自由文本参考答案，可能为空。 |
| `answers[].answer.highlighted_evidence` | `array<string>` | 原始高亮证据；不用于段落匹配。 |
| `answers[].answer.unanswerable` | `boolean` | 是否标记为无法回答。 |
| `answers[].answer.yes_no` | `boolean or null` | 是非题参考答案；其他答案类型为 null。 |

## `data/processed/qasper_export.manifest.json`

与 papers.jsonl 和 qa.jsonl 同时生成，不需独立构建。绑定来源及输出哈希、划分计数和拟议策略。输出文件名为基本文件名；三份导出文件需保持在同一目录。

### 生成命令

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | manifest 格式版本。 |
| `artifact` | `string` | qasper_papers_and_qa。 |
| `split_policy_version` | `string` | 拟议的论文互斥划分策略版本。 |
| `source` | `object` | 固定的上游及导出来源。 |
| `source.dataset_id` | `string` | allenai/qasper。 |
| `source.resolved_revision` | `string` | 上游不可变的完整提交 SHA。 |
| `source.local_parser_version` | `integer` | 本地源数据解析器版本。 |
| `source.source_manifest_sha256` | `string` | raw/qasper/manifest.json 的哈希。 |
| `source.split_files` | `object` | 以 train、validation、test 为键的输入清单。 |
| `source.split_files.<split>.rows` | `integer` | 来源论文行数。 |
| `source.split_files.<split>.sha256` | `string` | 来源划分 JSONL 的字节哈希。 |
| `split_counts` | `object` | 按官方划分记录的计数。 |
| `split_counts.<split>.papers` | `integer` | 论文数。 |
| `split_counts.<split>.questions` | `integer` | 问题数。 |
| `split_counts.<split>.answer_annotations` | `integer` | 答案标注数。 |
| `outputs` | `object` | 两个输出 JSONL 文件的清单。 |
| `outputs.<papers\|qa>.file` | `string` | 输出基本文件名；各导出文件位于同一目录。 |
| `outputs.<papers\|qa>.rows` | `integer` | 输出行数。 |
| `outputs.<papers\|qa>.sha256` | `string` | 输出 SHA-256。 |
| `outputs.qa.answer_annotation_count` | `integer` | 全部问答行的答案标注总数。 |

## `data/processed/passages.jsonl`

configs/default.yaml:data.passages_path 使用的默认开发语料，仅包含 train 和 validation。当前固定来源的 365/40 构建包含 21,360 个块；精确计数和哈希以 manifest 为准。

### 生成命令

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `passage_id` | `string` | 不透明、确定性的 qasper-passage-v1- SHA-256 标识。 |
| `paper_id` | `string` | 来源论文标识。 |
| `title` | `string` | 规范化后的论文标题。 |
| `section` | `string` | 规范化后的章节显示名称；同名章节仍为独立容器。 |
| `chunk_number` | `integer` | 同一原始来源容器内从零开始、连续的块序号。 |
| `text` | `string` | 规范化后的正文块；不包含问答监督信息。 |
| `previous_passage_id` | `string or null` | 同一容器内的直接前驱；首块为 null。 |
| `next_passage_id` | `string or null` | 同一容器内的直接后继；末块为 null。 |

## `data/processed/passages.manifest.json`

passages.jsonl 的配套文件。scope=development、artifact=development_corpus、purpose=development。记录全部官方划分，包括被排除且输出块数为零的 test。

### 生成命令

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | manifest 格式版本。 |
| `artifact` | `string` | development_corpus 或 inference_corpus。 |
| `purpose` | `string` | development 或 index_for_inference。 |
| `scope` | `string` | development 或 all-paper-text。 |
| `source` | `object` | 固定的上游及导出来源。 |
| `source.dataset_id` | `string` | allenai/qasper。 |
| `source.resolved_revision` | `string` | 上游不可变的完整提交 SHA。 |
| `source.local_parser_version` | `integer` | 本地源数据解析器版本。 |
| `source.export_papers_file` | `string` | 输入论文导出文件的基本文件名。 |
| `source.export_papers_sha256` | `string` | 论文导出文件精确字节的 SHA-256。 |
| `source.source_splits` | `object` | 从导出 source.split_files 复制的原始划分清单。 |
| `source.source_splits.<split>.rows` | `integer` | 原始划分的论文行数。 |
| `source.source_splits.<split>.sha256` | `string` | 原始划分的字节哈希。 |
| `source.split_policy_version` | `string` | 拟议划分策略版本。 |
| `source.split_counts` | `object` | 按划分记录的范围及计数元数据。 |
| `source.split_counts.<split>.project_role` | `string` | development、validation 或 held_out。 |
| `source.split_counts.<split>.included_in_scope` | `boolean` | 是否纳入当前构建范围。 |
| `source.split_counts.<split>.source_paper_count` | `integer` | 该划分在输入导出中的论文数。 |
| `source.split_counts.<split>.passage_count` | `integer` | 该划分生成的块数。 |
| `chunking` | `object` | 精确的规范化及切分配置。 |
| `chunking.source_kinds` | `array<string>` | 当前仅 full_text。 |
| `chunking.normalization_version` | `string` | 文本规范化实现版本。 |
| `chunking.chunking_version` | `string` | 按词切分实现版本。 |
| `chunking.chunk_size_words` | `integer` | 每块最多包含的 Unicode 非空白词段数；当前选用值为 365。 |
| `chunking.chunk_overlap_words` | `integer` | 相邻块重叠词段数；当前选用值为 40。 |
| `chunking.word_rule` | `string` | 词数统计规则。 |
| `chunking.type_rule` | `string` | casefold 后的词型定义（语料及映射 manifest）。 |
| `output` | `object` | 语料清单、计数及评分要求检查。 |
| `output.file` | `string` | 语料基本文件名。 |
| `output.sha256` | `string` | 语料精确字节的哈希。 |
| `output.scope` | `string` | 与顶层 scope 一致。 |
| `output.purpose` | `string` | 与顶层 purpose 一致。 |
| `output.source_paper_count` | `integer` | 选定范围内的输入论文数。 |
| `output.indexed_paper_count` | `integer` | 至少生成一个块的论文数。 |
| `output.passage_count` | `integer` | 块总数。 |
| `output.unique_passage_count` | `integer` | 不同块 ID 的数量。 |
| `output.source_word_count` | `integer` | 原始词数，不重复计算块重叠。 |
| `output.passage_word_count` | `integer` | 输出块词数，包含重叠。 |
| `output.passage_word_type_count` | `integer` | 块中经 casefold 后的不同词型数。 |
| `output.minimum_passages` | `integer` | 要求的最低块数。 |
| `output.minimum_words` | `integer` | 要求的最低词数。 |
| `output.rubric_minimum_met` | `boolean` | 是否满足至少 10,000 块及 100,000 词的要求。 |

## `data/processed/passages_all_paper_text.jsonl`

包含 train、validation、test 的论文正文，用于推理索引。不包含问答字段。当前固定来源的 365/40 构建包含 28,617 个块；纳入留出论文不表示允许使用其监督信息调参。

### 生成命令

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope all-paper-text --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages_all_paper_text.jsonl --manifest-output data/processed/passages_all_paper_text.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `passage_id` | `string` | 不透明、确定性的 qasper-passage-v1- SHA-256 标识。 |
| `paper_id` | `string` | 来源论文标识。 |
| `title` | `string` | 规范化后的论文标题。 |
| `section` | `string` | 规范化后的章节显示名称；同名章节仍为独立容器。 |
| `chunk_number` | `integer` | 同一原始来源容器内从零开始、连续的块序号。 |
| `text` | `string` | 规范化后的正文块；不包含问答监督信息。 |
| `previous_passage_id` | `string or null` | 同一容器内的直接前驱；首块为 null。 |
| `next_passage_id` | `string or null` | 同一容器内的直接后继；末块为 null。 |

## `data/processed/passages_all_paper_text.manifest.json`

passages_all_paper_text.jsonl 的配套文件。scope=all-paper-text、artifact=inference_corpus、purpose=index_for_inference。按来源划分记录纳入的论文正文；不是冻结问题池的 manifest。

### 生成命令

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope all-paper-text --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/passages_all_paper_text.jsonl --manifest-output data/processed/passages_all_paper_text.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | manifest 格式版本。 |
| `artifact` | `string` | development_corpus 或 inference_corpus。 |
| `purpose` | `string` | development 或 index_for_inference。 |
| `scope` | `string` | development 或 all-paper-text。 |
| `source` | `object` | 固定的上游及导出来源。 |
| `source.dataset_id` | `string` | allenai/qasper。 |
| `source.resolved_revision` | `string` | 上游不可变的完整提交 SHA。 |
| `source.local_parser_version` | `integer` | 本地源数据解析器版本。 |
| `source.export_papers_file` | `string` | 输入论文导出文件的基本文件名。 |
| `source.export_papers_sha256` | `string` | 论文导出文件精确字节的 SHA-256。 |
| `source.source_splits` | `object` | 从导出 source.split_files 复制的原始划分清单。 |
| `source.source_splits.<split>.rows` | `integer` | 原始划分的论文行数。 |
| `source.source_splits.<split>.sha256` | `string` | 原始划分的字节哈希。 |
| `source.split_policy_version` | `string` | 拟议划分策略版本。 |
| `source.split_counts` | `object` | 按划分记录的范围及计数元数据。 |
| `source.split_counts.<split>.project_role` | `string` | development、validation 或 held_out。 |
| `source.split_counts.<split>.included_in_scope` | `boolean` | 是否纳入当前构建范围。 |
| `source.split_counts.<split>.source_paper_count` | `integer` | 该划分在输入导出中的论文数。 |
| `source.split_counts.<split>.passage_count` | `integer` | 该划分生成的块数。 |
| `chunking` | `object` | 精确的规范化及切分配置。 |
| `chunking.source_kinds` | `array<string>` | 当前仅 full_text。 |
| `chunking.normalization_version` | `string` | 文本规范化实现版本。 |
| `chunking.chunking_version` | `string` | 按词切分实现版本。 |
| `chunking.chunk_size_words` | `integer` | 每块最多包含的 Unicode 非空白词段数；当前选用值为 365。 |
| `chunking.chunk_overlap_words` | `integer` | 相邻块重叠词段数；当前选用值为 40。 |
| `chunking.word_rule` | `string` | 词数统计规则。 |
| `chunking.type_rule` | `string` | casefold 后的词型定义（语料及映射 manifest）。 |
| `output` | `object` | 语料清单、计数及评分要求检查。 |
| `output.file` | `string` | 语料基本文件名。 |
| `output.sha256` | `string` | 语料精确字节的哈希。 |
| `output.scope` | `string` | 与顶层 scope 一致。 |
| `output.purpose` | `string` | 与顶层 purpose 一致。 |
| `output.source_paper_count` | `integer` | 选定范围内的输入论文数。 |
| `output.indexed_paper_count` | `integer` | 至少生成一个块的论文数。 |
| `output.passage_count` | `integer` | 块总数。 |
| `output.unique_passage_count` | `integer` | 不同块 ID 的数量。 |
| `output.source_word_count` | `integer` | 原始词数，不重复计算块重叠。 |
| `output.passage_word_count` | `integer` | 输出块词数，包含重叠。 |
| `output.passage_word_type_count` | `integer` | 块中经 casefold 后的不同词型数。 |
| `output.minimum_passages` | `integer` | 要求的最低块数。 |
| `output.minimum_words` | `integer` | 要求的最低词数。 |
| `output.rubric_minimum_met` | `boolean` | 是否满足至少 10,000 块及 100,000 词的要求。 |

## `data/processed/gold_evidence_mapping.jsonl`

不抽样地将符合条件的 train/validation 问题映射到已验证的开发语料。已有的本地旧导出可能缺少 qa_metadata 及标注元数据；需要下表当前字段时，应导出到新路径。映射结构仍为 v0-proposed。

### 生成命令

```powershell
python -m scripts.export_evidence_mapping --scope development
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed。 |
| `question_id` | `string` | 原始问题标识。 |
| `paper_id` | `string` | 来源论文标识。 |
| `source_split` | `string` | 官方来源划分。 |
| `question` | `string` | 原始问题文本。 |
| `qa_metadata` | `object` | 其他原始问答字段；当前导出器原样保留。 |
| `qa_metadata.nlp_background` | `string` | 提问者的 NLP 背景。 |
| `qa_metadata.paper_read` | `string` | 原始论文阅读情况记录。 |
| `qa_metadata.question_writer` | `string` | 原始提问者标识。 |
| `qa_metadata.search_query` | `string` | 原始检索查询。 |
| `qa_metadata.topic_background` | `string` | 提问者的主题背景。 |
| `annotations` | `array<object>` | 分别保留的备选答案及定位后的证据。 |
| `annotations[].annotation_id` | `string` | 原始标注 ID 转为字符串；缺失时使用答案数组索引。 |
| `annotations[].worker_id` | `string (if present)` | 当前导出器保留的原始标注者元数据（若存在）。 |
| `annotations[].answer` | `object` | 原始答案内容。 |
| `annotations[].answer.evidence` | `array<string>` | 标注的证据文本，可能包含 FLOAT SELECTED 标记。 |
| `annotations[].answer.extractive_spans` | `array<string>` | 抽取式参考答案片段。 |
| `annotations[].answer.free_form_answer` | `string` | 自由文本参考答案，可能为空。 |
| `annotations[].answer.highlighted_evidence` | `array<string>` | 原始高亮证据；不用于段落匹配。 |
| `annotations[].answer.unanswerable` | `boolean` | 是否标记为无法回答。 |
| `annotations[].answer.yes_no` | `boolean or null` | 是非题参考答案；其他答案类型为 null。 |
| `annotations[].evidence_locations` | `array<string>` | 指向 evidence_paragraphs[].location 的非空引用列表。 |
| `evidence_paragraphs` | `array<object>` | 各答案引用的原始证据段落，已去重。 |
| `evidence_paragraphs[].location` | `string` | paper_id:section_index:paragraph_index 形式的引用。 |
| `evidence_paragraphs[].section_index` | `integer` | 原始 full_text 中从零开始的索引。 |
| `evidence_paragraphs[].paragraph_index` | `integer` | 原始 paragraphs 中从零开始的索引；空白段落也计入。 |
| `evidence_paragraphs[].text` | `string` | 原始证据段落，保留空白及换行。 |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | 导出问题中为 true：匹配块的并集覆盖全部非空白字符。 |
| `evidence_paragraphs[].passage_matches` | `array<object>` | 所有与证据存在非空白字符重叠的块。 |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | 所选语料中的精确块标识。 |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | 原始证据段落中的两个 Python 字符偏移，表示左闭右开区间 [start, end)；不是字节、token 或块内偏移。 |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | 此块单独是否覆盖该段落的全部非空白内容。 |
| `gold_passage_ids` | `array<string>` | 与任一标注证据重叠的块 ID，排序去重；并非人工相关性标签。 |

只有在至少有一个答案、且每个答案的非空证据都能唯一定位到完整正文段落并被语料完整覆盖时，才保留该问题。空证据、`FLOAT SELECTED`、缺失段落、重复文本歧义或覆盖不足会排除整道题。匹配只规范化换行及外部空白，不做模糊匹配或答案子串匹配。备选答案须分组计算覆盖率，不能合并成一个答案。`gold_passage_ids` 包含部分重叠块；单块不一定覆盖完整证据。未入选的块也不能直接视为不相关。问答、答案、证据及派生标签不得写入检索语料。

## `data/processed/gold_evidence_mapping.manifest.json`

开发证据映射的配套文件。当前导出记录 scope=development 及仅开发数据的 evaluation_design；本地旧 manifest 可能没有这两个字段。held_out_freeze=false 不表示创建或冻结了留出问题池。

### 生成命令

```powershell
python -m scripts.export_evidence_mapping --scope development
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed。 |
| `split_policy_version` | `string` | 拟议划分策略版本。 |
| `source_splits` | `array<string>` | 选作证据映射的官方划分。 |
| `scope` | `string` | development 或 all-splits-testing；旧开发导出中可能缺失。 |
| `evaluation_design` | `string` | 评估设计含义；旧开发导出中可能缺失。 |
| `chunking` | `object` | 精确的规范化及切分配置。 |
| `chunking.source_kinds` | `array<string>` | 当前仅 full_text。 |
| `chunking.normalization_version` | `string` | 文本规范化实现版本。 |
| `chunking.chunking_version` | `string` | 按词切分实现版本。 |
| `chunking.chunk_size_words` | `integer` | 每块最多包含的 Unicode 非空白词段数；当前选用值为 365。 |
| `chunking.chunk_overlap_words` | `integer` | 相邻块重叠词段数；当前选用值为 40。 |
| `chunking.word_rule` | `string` | 词数统计规则。 |
| `chunking.type_rule` | `string` | casefold 后的词型定义（语料及映射 manifest）。 |
| `inputs` | `object` | papers、qa、export_manifest、passages、passages_manifest 的哈希。 |
| `inputs.<input>.file` | `string` | 输入基本文件名。 |
| `inputs.<input>.sha256` | `string` | 输入字节哈希。 |
| `filtering_counts` | `object` | 按官方划分记录的问题计数；零计数类别可能缺失。 |
| `filtering_counts.<split>.total` | `integer` | 检查的问题数。 |
| `filtering_counts.<split>.eligible` | `integer` | 保留的问题数。 |
| `filtering_counts.<split>.held_out_excluded` | `integer` | 因开发范围限制而排除的问题数。 |
| `filtering_counts.<split>.invalid_or_uncovered_answer_evidence` | `integer` | 因证据缺失、歧义或覆盖不完整而排除的问题数。 |
| `mapping_rule` | `string` | 证据须唯一匹配整段；所有答案均须通过。 |
| `passage_match_rule` | `string` | 任意非空白字符重叠，且匹配并集完整覆盖证据。 |
| `offset_rule` | `string` | 证据文本中从零开始、左闭右开的 Python 字符偏移。 |
| `label_status` | `string` | 自动派生的 gold 参考，不是人工相关性标签。 |
| `held_out_freeze` | `boolean` | false：不是最终留出集冻结记录。 |
| `output` | `object` | 映射输出清单。 |
| `output.file` | `string` | 映射 JSONL 基本文件名。 |
| `output.rows` | `integer` | 符合条件的问题行数。 |
| `output.sha256` | `string` | 映射 JSONL 精确字节的哈希。 |

## `data/processed/gold_evidence_mapping_all_splits.jsonl`

显式对 train、validation、test 进行普通测试的导出。默认选用全论文正文语料及独立的 all-splits 输出名。此评估设计放弃 test 的独立留出地位，不得将结果报告为独立留出性能。

### 生成命令

```powershell
python -m scripts.export_evidence_mapping --scope all-splits-testing
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed。 |
| `question_id` | `string` | 原始问题标识。 |
| `paper_id` | `string` | 来源论文标识。 |
| `source_split` | `string` | 官方来源划分。 |
| `question` | `string` | 原始问题文本。 |
| `qa_metadata` | `object` | 其他原始问答字段；当前导出器原样保留。 |
| `qa_metadata.nlp_background` | `string` | 提问者的 NLP 背景。 |
| `qa_metadata.paper_read` | `string` | 原始论文阅读情况记录。 |
| `qa_metadata.question_writer` | `string` | 原始提问者标识。 |
| `qa_metadata.search_query` | `string` | 原始检索查询。 |
| `qa_metadata.topic_background` | `string` | 提问者的主题背景。 |
| `annotations` | `array<object>` | 分别保留的备选答案及定位后的证据。 |
| `annotations[].annotation_id` | `string` | 原始标注 ID 转为字符串；缺失时使用答案数组索引。 |
| `annotations[].worker_id` | `string (if present)` | 当前导出器保留的原始标注者元数据（若存在）。 |
| `annotations[].answer` | `object` | 原始答案内容。 |
| `annotations[].answer.evidence` | `array<string>` | 标注的证据文本，可能包含 FLOAT SELECTED 标记。 |
| `annotations[].answer.extractive_spans` | `array<string>` | 抽取式参考答案片段。 |
| `annotations[].answer.free_form_answer` | `string` | 自由文本参考答案，可能为空。 |
| `annotations[].answer.highlighted_evidence` | `array<string>` | 原始高亮证据；不用于段落匹配。 |
| `annotations[].answer.unanswerable` | `boolean` | 是否标记为无法回答。 |
| `annotations[].answer.yes_no` | `boolean or null` | 是非题参考答案；其他答案类型为 null。 |
| `annotations[].evidence_locations` | `array<string>` | 指向 evidence_paragraphs[].location 的非空引用列表。 |
| `evidence_paragraphs` | `array<object>` | 各答案引用的原始证据段落，已去重。 |
| `evidence_paragraphs[].location` | `string` | paper_id:section_index:paragraph_index 形式的引用。 |
| `evidence_paragraphs[].section_index` | `integer` | 原始 full_text 中从零开始的索引。 |
| `evidence_paragraphs[].paragraph_index` | `integer` | 原始 paragraphs 中从零开始的索引；空白段落也计入。 |
| `evidence_paragraphs[].text` | `string` | 原始证据段落，保留空白及换行。 |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | 导出问题中为 true：匹配块的并集覆盖全部非空白字符。 |
| `evidence_paragraphs[].passage_matches` | `array<object>` | 所有与证据存在非空白字符重叠的块。 |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | 所选语料中的精确块标识。 |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | 原始证据段落中的两个 Python 字符偏移，表示左闭右开区间 [start, end)；不是字节、token 或块内偏移。 |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | 此块单独是否覆盖该段落的全部非空白内容。 |
| `gold_passage_ids` | `array<string>` | 与任一标注证据重叠的块 ID，排序去重；并非人工相关性标签。 |

只有在至少有一个答案、且每个答案的非空证据都能唯一定位到完整正文段落并被语料完整覆盖时，才保留该问题。空证据、`FLOAT SELECTED`、缺失段落、重复文本歧义或覆盖不足会排除整道题。匹配只规范化换行及外部空白，不做模糊匹配或答案子串匹配。备选答案须分组计算覆盖率，不能合并成一个答案。`gold_passage_ids` 包含部分重叠块；单块不一定覆盖完整证据。未入选的块也不能直接视为不相关。问答、答案、证据及派生标签不得写入检索语料。

## `data/processed/gold_evidence_mapping_all_splits.manifest.json`

all-splits 映射的配套文件。scope=all-splits-testing，evaluation_design 明确记录全部官方划分上的普通测试；held_out_freeze 仍为 false。

### 生成命令

```powershell
python -m scripts.export_evidence_mapping --scope all-splits-testing
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed。 |
| `split_policy_version` | `string` | 拟议划分策略版本。 |
| `source_splits` | `array<string>` | 选作证据映射的官方划分。 |
| `scope` | `string` | development 或 all-splits-testing；旧开发导出中可能缺失。 |
| `evaluation_design` | `string` | 评估设计含义；旧开发导出中可能缺失。 |
| `chunking` | `object` | 精确的规范化及切分配置。 |
| `chunking.source_kinds` | `array<string>` | 当前仅 full_text。 |
| `chunking.normalization_version` | `string` | 文本规范化实现版本。 |
| `chunking.chunking_version` | `string` | 按词切分实现版本。 |
| `chunking.chunk_size_words` | `integer` | 每块最多包含的 Unicode 非空白词段数；当前选用值为 365。 |
| `chunking.chunk_overlap_words` | `integer` | 相邻块重叠词段数；当前选用值为 40。 |
| `chunking.word_rule` | `string` | 词数统计规则。 |
| `chunking.type_rule` | `string` | casefold 后的词型定义（语料及映射 manifest）。 |
| `inputs` | `object` | papers、qa、export_manifest、passages、passages_manifest 的哈希。 |
| `inputs.<input>.file` | `string` | 输入基本文件名。 |
| `inputs.<input>.sha256` | `string` | 输入字节哈希。 |
| `filtering_counts` | `object` | 按官方划分记录的问题计数；零计数类别可能缺失。 |
| `filtering_counts.<split>.total` | `integer` | 检查的问题数。 |
| `filtering_counts.<split>.eligible` | `integer` | 保留的问题数。 |
| `filtering_counts.<split>.held_out_excluded` | `integer` | 因开发范围限制而排除的问题数。 |
| `filtering_counts.<split>.invalid_or_uncovered_answer_evidence` | `integer` | 因证据缺失、歧义或覆盖不完整而排除的问题数。 |
| `mapping_rule` | `string` | 证据须唯一匹配整段；所有答案均须通过。 |
| `passage_match_rule` | `string` | 任意非空白字符重叠，且匹配并集完整覆盖证据。 |
| `offset_rule` | `string` | 证据文本中从零开始、左闭右开的 Python 字符偏移。 |
| `label_status` | `string` | 自动派生的 gold 参考，不是人工相关性标签。 |
| `held_out_freeze` | `boolean` | false：不是最终留出集冻结记录。 |
| `output` | `object` | 映射输出清单。 |
| `output.file` | `string` | 映射 JSONL 基本文件名。 |
| `output.rows` | `integer` | 符合条件的问题行数。 |
| `output.sha256` | `string` | 映射 JSONL 精确字节的哈希。 |

## `data/processed/sample_passages_100.jsonl`

仅从 train 和 validation 生成的确定性依赖样本。按论文稳定排序，使用子集和选择完整来源容器；每篇论文最多一个容器，优先覆盖更多论文。固定为 100 个块；固定来源的 365/40 样本包含 100 篇论文、20,017 个块内词。

### 生成命令

```powershell
python -m scripts.build_sample_passages --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/sample_passages_100.jsonl --manifest-output data/processed/sample_passages_100.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `passage_id` | `string` | 不透明、确定性的 qasper-passage-v1- SHA-256 标识。 |
| `paper_id` | `string` | 来源论文标识。 |
| `title` | `string` | 规范化后的论文标题。 |
| `section` | `string` | 规范化后的章节显示名称；同名章节仍为独立容器。 |
| `chunk_number` | `integer` | 同一原始来源容器内从零开始、连续的块序号。 |
| `text` | `string` | 规范化后的正文块；不包含问答监督信息。 |
| `previous_passage_id` | `string or null` | 同一容器内的直接前驱；首块为 null。 |
| `next_passage_id` | `string or null` | 同一容器内的直接后继；末块为 null。 |

## `data/processed/sample_passages_100.manifest.json`

与样本同时生成。记录来源哈希、选择前的规范化总计、选中的完整容器及输出哈希。由于不选择部分容器，样本邻接关系保持完整。

### 生成命令

```powershell
python -m scripts.build_sample_passages --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --chunk-size-words 365 --chunk-overlap-words 40 --output data/processed/sample_passages_100.jsonl --manifest-output data/processed/sample_passages_100.manifest.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `manifest_schema_version` | `integer` | manifest 格式版本。 |
| `artifact` | `string` | sample_passages_100。 |
| `source` | `object` | 固定的上游及导出来源。 |
| `source.dataset_id` | `string` | allenai/qasper。 |
| `source.resolved_revision` | `string` | 上游不可变的完整提交 SHA。 |
| `source.local_parser_version` | `integer` | 本地源数据解析器版本。 |
| `source.export_papers_file` | `string` | 输入论文导出文件的基本文件名。 |
| `source.export_papers_sha256` | `string` | 论文导出文件精确字节的 SHA-256。 |
| `source.source_splits` | `array<object>` | 开发数据的来源划分清单。 |
| `source.source_splits[].name` | `string` | train 或 validation。 |
| `source.source_splits[].project_role` | `string` | 拟议项目角色。 |
| `source.source_splits[].input_paper_count` | `integer` | 该划分的输入论文数。 |
| `source.source_splits[].source_sha256` | `string` | 原始划分的 SHA-256。 |
| `normalization` | `object` | 样本选择前、全部已检查开发记录的规范化计数。 |
| `normalization.paragraphs_seen` | `integer` | 检查的来源段落数。 |
| `normalization.paragraphs_emitted` | `integer` | 保留的非空规范化段落数。 |
| `normalization.blank_paragraphs_dropped` | `integer` | 丢弃的空白段落数。 |
| `normalization.line_ending_replacements` | `integer` | CRLF/CR 转 LF 的替换次数。 |
| `normalization.outer_whitespace_trims` | `integer` | 外部空白裁剪次数。 |
| `normalization.sections_seen` | `integer` | 检查的来源章节数。 |
| `normalization.sections_emitted` | `integer` | 保留的章节数。 |
| `normalization.blank_sections_dropped` | `integer` | 丢弃的空白名称章节数。 |
| `normalization.null_sections_dropped` | `integer` | 丢弃的 null 名称章节数。 |
| `normalization.empty_sections_dropped` | `integer` | 丢弃的无可用段落章节数。 |
| `normalization.invalid_papers_dropped` | `integer` | 规范化阶段排除的论文数。 |
| `chunking` | `object` | 精确的规范化及切分配置。 |
| `chunking.source_kinds` | `array<string>` | 当前仅 full_text。 |
| `chunking.normalization_version` | `string` | 文本规范化实现版本。 |
| `chunking.chunking_version` | `string` | 按词切分实现版本。 |
| `chunking.chunk_size_words` | `integer` | 每块最多包含的 Unicode 非空白词段数；当前选用值为 365。 |
| `chunking.chunk_overlap_words` | `integer` | 相邻块重叠词段数；当前选用值为 40。 |
| `chunking.word_rule` | `string` | 词数统计规则。 |
| `selection` | `object` | 确定性的完整容器选择元数据。 |
| `selection.method` | `string` | 按论文稳定排序的完整容器子集和选择。 |
| `selection.target_passage_count` | `integer` | 目标块数（100）。 |
| `selection.selected_container_count` | `integer` | 选中的来源容器数。 |
| `selection.selected_paper_count` | `integer` | 选中的不同论文数。 |
| `selection.selected_section_count` | `integer` | 选中的不同章节数。 |
| `selection.selected_groups` | `array<object>` | 选中的完整来源容器。 |
| `selection.selected_groups[].source_split` | `string` | 官方来源划分。 |
| `selection.selected_groups[].project_role` | `string` | 拟议项目角色。 |
| `selection.selected_groups[].paper_id` | `string` | 来源论文标识。 |
| `selection.selected_groups[].source_kind` | `string` | full_text。 |
| `selection.selected_groups[].section_index` | `integer` | 原始章节位置，从零开始。 |
| `selection.selected_groups[].passage_count` | `integer` | 该选中容器的块数。 |
| `output` | `object` | 样本序列化规则及计数。 |
| `output.file` | `string` | 样本基本文件名。 |
| `output.format` | `string` | jsonl。 |
| `output.encoding` | `string` | utf-8。 |
| `output.newline` | `string` | lf。 |
| `output.passage_count` | `integer` | 样本块总数（100）。 |
| `output.unique_passage_count` | `integer` | 不同块 ID 的数量。 |
| `output.unique_paper_count` | `integer` | 不同来源论文数。 |
| `output.passage_word_count` | `integer` | 输出样本词数，包含重叠。 |
| `output.sha256` | `string` | 样本精确字节的哈希。 |

## `data/processed/qasper_inspection.json`

可选离线诊断报告；当前精简本地目录中不存在。报告前检查采集目录恰好包含四个文件、划分哈希/行数、JSON 解析及关键嵌套结构。与其他构建器不同，它会替换已有报告。来源：src/data/qasper_inspection.py。

### 生成命令

```powershell
python -m scripts.inspect_qasper --input-dir data/raw/qasper --output data/processed/qasper_inspection.json
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `provenance` | `object` | 固定来源元数据及输入字节哈希。 |
| `provenance.dataset_id` | `string` | 来自采集 manifest 的 dataset_id。 |
| `provenance.config` | `string` | 来自采集 manifest 的 config。 |
| `provenance.source_dataset_version` | `string` | 来自采集 manifest 的 source_dataset_version。 |
| `provenance.requested_revision` | `string` | 来自采集 manifest 的 requested_revision。 |
| `provenance.resolved_revision` | `string` | 来自采集 manifest 的 resolved_revision。 |
| `provenance.manifest_schema_version` | `integer` | 原始 manifest 格式版本。 |
| `provenance.licenses` | `object` | 原始来源许可声明。 |
| `provenance.input_files` | `object` | 以划分 JSONL 基本文件名为键的输入清单。 |
| `provenance.input_files.<file>.bytes` | `integer` | 输入字节数。 |
| `provenance.input_files.<file>.rows` | `integer` | 输入论文数。 |
| `provenance.input_files.<file>.sha256` | `string` | 输入精确字节的哈希。 |
| `counting_definitions` | `object<string, string>` | 论文、问题、标注、段落、ID 及答案类型的计数定义。 |
| `per_split` | `object` | 按官方划分记录的详细诊断。 |
| `global_totals` | `object<string, integer>` | paper_count、question_count、answer_annotation_count、unique_paper_id_count、unique_question_id_count、chapter_count、paragraph_count、paragraph_string_count 计数。 |
| `field_anomalies` | `object` | 分划分及全局的字段/类别异常计数与示例坐标。 |
| `section_anomalies` | `object` | 分划分及全局的字段/类别异常计数与示例坐标。 |
| `question_anomalies` | `object` | 分划分及全局的字段/类别异常计数与示例坐标。 |
| `answer_field_anomalies` | `object` | 分划分及全局的字段/类别异常计数与示例坐标。 |
| `answer_types` | `object` | 按说明的优先级统计各划分及全局答案类型。 |
| `ambiguous_payload` | `object` | 各划分及全局的答案内容歧义计数。 |
| `evidence` | `object` | 各划分及全局的证据和高亮证据诊断。 |
| `duplicate_paragraphs` | `object` | same_paper 与 cross_paper 重复段落汇总。 |
| `duplicate_paragraphs.<scope>.duplicate_group_count` | `integer` | 重复段落组数。 |
| `duplicate_paragraphs.<scope>.involved_paragraph_count` | `integer` | 重复组中的段落实例数。 |
| `duplicate_paragraphs.cross_paper.involved_paper_count` | `integer` | 跨论文重复涉及的不同论文数。 |
| `duplicate_paragraphs.<scope>.examples` | `array<object>` | 数量受限的 occurrence_count、paper_id_count、locations 示例。 |
| `split_overlap` | `object` | 论文/问题交集及划分内部重复 ID。 |
| `split_overlap.paper_id_intersections` | `object<string, array<string>>` | 各划分对的论文 ID 交集。 |
| `split_overlap.question_id_intersections` | `object<string, array<string>>` | 各划分对的问题 ID 交集。 |
| `split_overlap.within_split_duplicate_paper_ids` | `object<string, array<string>>` | 以划分为键的重复论文 ID。 |
| `split_overlap.observed_paper_disjoint` | `boolean` | 仅当划分内部无重复且划分之间论文无交集时为 true。 |
| `open_decisions` | `array<string>` | 需评审的观察结果及待定事项。 |
| `per_split.<split>.paper_count` | `integer` | 论文行数。 |
| `per_split.<split>.question_count` | `integer` | 问题数。 |
| `per_split.<split>.answer_annotation_count` | `integer` | 答案标注数。 |
| `per_split.<split>.unique_paper_id_count` | `integer` | 不同的非空白论文 ID 数。 |
| `per_split.<split>.duplicate_paper_id_count` | `integer` | 发生重复的不同论文 ID 数。 |
| `per_split.<split>.unique_question_id_count` | `integer` | 不同的非空白问题 ID 数。 |
| `per_split.<split>.duplicate_question_id_count` | `integer` | 发生重复的不同问题 ID 数。 |
| `per_split.<split>.ambiguous_payload_count` | `integer` | 含多种有效答案内容类型的标注数。 |
| `per_split.<split>.duplicate_paper_id_values` | `array<string>` | 排序后的重复论文 ID。 |
| `per_split.<split>.duplicate_question_id_values` | `array<string>` | 排序后的重复问题 ID。 |
| `per_split.<split>.question_annotation_count_stats` | `object` | 每题标注数的 min、median、max。 |
| `per_split.<split>.question_annotation_count_stats.<min\|median\|max>` | `number or null` | 汇总计数；无问题时为 null，中位数可为小数。 |
| `per_split.<split>.chapters` | `object` | 原始章节及段落统计。 |
| `per_split.<split>.chapters.chapter_count` | `integer` | 原始 full_text 列表项数。 |
| `per_split.<split>.chapters.paragraph_count` | `integer` | 原始段落条目数，含空白/非字符串。 |
| `per_split.<split>.chapters.paragraph_string_count` | `integer` | 字符串类型段落条目数。 |
| `per_split.<split>.chapters.anomalies` | `object` | 章节字段/类别异常计数。 |
| `per_split.<split>.field_anomalies` | `object` | 该划分的字段/类别异常计数。 |
| `per_split.<split>.question_anomalies` | `object` | 该划分的字段/类别异常计数。 |
| `per_split.<split>.answer_field_anomalies` | `object` | 该划分的字段/类别异常计数。 |
| `per_split.<split>.answer_types` | `object<string, integer>` | unanswerable、yes_no、extractive、free_form、invalid_or_empty 的计数。 |
| `per_split.<split>.evidence` | `object` | evidence 和 highlighted_evidence 诊断，采用下述证据计数结构。 |
| `<anomaly-counter>.<field>.<category>.count` | `integer` | 异常块的共享结构；对应类别的计数。 |
| `<anomaly-counter>.<field>.<category>.locations` | `array<object>` | 每类最多十个稳定的诊断坐标。 |
| `<location>.split` | `string` | 诊断位置的官方划分。 |
| `<location>.paper_id` | `string or null` | 论文标识；无效时为 null。 |
| `<location>.line_number` | `integer` | 从一开始的来源 JSONL 行号。 |
| `<location>.<section_index\|paragraph_index\|question_index\|answer_index>` | `integer (when present)` | 异常对应的零基来源数组索引（若存在）。 |
| `<location>.<question_id\|field>` | `string or null (when present)` | 适用时记录问题标识或异常字段。 |
| `<evidence-counter>.total_items` | `integer` | 全部证据条目数。 |
| `<evidence-counter>.blank_items` | `integer` | 空白证据字符串数。 |
| `<evidence-counter>.non_string_items` | `integer` | 非字符串证据条目数。 |
| `<evidence-counter>.annotations_with_items` | `integer` | 含证据条目的标注数。 |
| `<evidence-counter>.float_selected_hits` | `integer` | FLOAT SELECTED 前缀匹配数。 |
| `<evidence-counter>.hit_paper_count` | `integer` | 含此前缀匹配的论文数。 |
| `<evidence-counter>.figures_and_tables_items_in_hit_papers` | `integer` | 匹配论文中的图表总条目数；不是推断出的证据映射。 |
| `<evidence-counter>.float_selected_prefix_forms` | `array<string>` | 观察到的不同前缀形式。 |
| `<evidence-counter>.anomaly_locations` | `object<string, array<object>>` | 以证据异常类别为键的有界坐标列表。 |

`<anomaly-counter>` 和 `<evidence-counter>` 表示复用的诊断对象结构，不是实际顶层键；同一结构分别用于各划分和全局汇总。异常类别、字段名和部分坐标按观测结果出现，不代表每个记录都包含它们。来源计数定义与示例均由检查器生成，不包含问题、答案或证据原文。

## Passage ID 协议

Passage ID 是不透明、确定性的标识。公开构造函数为 `src/data/passage_ids.py` 的 `make_passage_id(*, context, paper_id, source_kind, section_index, chunk_index) -> str`，所有参数必须显式提供。

不可变上下文为 `PassageIdContext(dataset_id, resolved_revision, local_parser_version, normalization_version, chunking_version, chunk_size_words, chunk_overlap_words)`。生产 QASPER 配置要求 `dataset_id="allenai/qasper"`、完整的小写 $40$ 字符 `resolved_revision`、正整数解析器版本、非空版本字符串、正数块大小，以及 `0 <= chunk_overlap_words < chunk_size_words`。

规范载荷恰有 `scheme`、`dataset`、`transform`、`coordinate` 四个顶层键。`dataset` 包含数据集 ID、解析后的 revision 和本地解析器版本；`transform` 包含规范化版本、切分版本及块大小/重叠；`coordinate` 包含论文 ID、来源类型、章节索引及块索引。实现使用 UTF-8 `json.dumps(..., ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)` 序列化后，对完整字节求 SHA-256。

结果格式为 `qasper-passage-v1-<64 lowercase hex characters>`；前缀为 `PASSAGE_ID_SCHEME_VERSION`，摘要不截断。消费者应读取记录或 manifest 的元数据，不解析 ID。P2 用它去重，P5 用它引用，邻接字段使用相同生成值；ID 函数本身不查询或验证其他记录。

`section_index` 是过滤空容器前的原始来源位置，`chunk_index` 是同一容器内确定性切分器输出的零基位置。预留来源类型为 `full_text`、`abstract`、`figure_table`；正文和图表使用原始列表位置，摘要使用 `0`。预留坐标不等于已批准索引该类型。

ID 包含固定来源 revision、解析器版本、规范化/切分版本、切分参数、论文 ID、来源类型及来源坐标；不包含显示标题、章节名、文本、来源划分、输出顺序、路径、时间或机器状态。`source_split` 不影响单块身份；完整集合由 manifest 和输出哈希标识。

任何可能改变块字节的规范化或切分变化，都须增加相应版本。载荷、字段含义、哈希方式或输出前缀变化须升级 `PASSAGE_ID_SCHEME_VERSION`，不能假设新旧 ID 兼容。ID 函数不负责生成块、选择摘要/图表策略、填邻接或映射证据。

合成示例采用 `paper_id="paper-a"`、`source_kind="full_text"`、`section_index=2`、`chunk_index=3` 及测试中的合成上下文，得到 `qasper-passage-v1-fe1214d2ab869911e267500cd9b8903dc8e3d4d1e66bde218d0bcc938da8c6ee`。

## Passage 序列协议

序列协议仍为 `v0-proposed`；公开 `Passage` 保持八个字段。是否增加来源字段由 `P3-D001` 跟踪，等待团队评审。

`chunk_number` 等于传给 ID 构造函数的 `chunk_index`，在同一内部容器 `(paper_id, source_kind, section_index)` 中必须是连续的 `0..N-1`。每个原始正文章节都是独立序列；未来若批准摘要或图表索引，也遵循同一规则。

邻接只指向同一容器内按块序号排列的直接前驱/后继。非空链接必须指向存在的块且双向互反。空白、无效或未批准的容器不生成记录；不能留下序号空洞、静默重编号或绕过缺失块连边。由于公开模型没有内部来源坐标，集合级条件由构建验证器检查。

边界缺失邻居在 Python 中为 `None`，在 JSON 中显式为 `null`。空字符串、缺失键、哨兵值、自指、悬空 ID 和跨容器链接都不合法。

1. 三块容器使用 `0 -> 1 -> 2`，首块前驱和末块后继为 `null`。
2. 下一正文章节从 `chunk_number=0` 重新开始；相邻章节边界不连边。
3. 单块容器的块序号为 `0`，前驱和后继均为 `null`。
4. 两个容器即使显示同一章节名，也须各自编号、各自保持边界。

摘要和图表是否索引、`FLOAT SELECTED` 如何映射仍由 `P3-D002`、`P3-D003` 跟踪。

## Passage 切分边界协议

切分边界协议仍为 `v0-proposed`。每个块只能来自一个内部容器 `(paper_id, source_kind, section_index)`；同容器的多个段落可以按原始顺序合并。

论文 ID 或来源类型变化都是硬边界。每个原始 `full_text[section_index]` 都是独立容器，即使相邻章节同名；未来批准的摘要和每个图表容器也保持独立。

不依据章节标题、语义相似度或标题层级推断合并。标题缺失或空白不放宽边界，同名不合并。词切分器只能在同一容器中按原始顺序组合段落，不能将某章节末段与下一章节首段拼成一个块。

来源章节索引使用未过滤的原始列表位置；丢弃空容器后不能重新编号后续章节。空容器不生成块，也不成为跨容器连边的依据。原始段落索引需保留用于后续证据定位。需要跨章节上下文时，检索应返回多个块。

切分边界比邻接规则更严格：前者限制哪些来源文本可进入同一个块，后者限制已生成块的直接邻接；两者都不能依据输出顺序或显示章节名推断。Step 5 的构建接口必须接收一个来源容器及其坐标、保留段落顺序后调用词切分器，调用者不能传入多个容器拼成的字符串。Step 7 的集合级负例须覆盖两篇论文、两个章节、重复标题及空白标题，证明块不跨硬边界。单记录 Passage 模型只能声明来源前提，无法验证内部坐标。

摘要/图表是否索引仍由团队决定；本规则也不定义 FLOAT SELECTED 证据映射，后者由 P3-D003 跟踪。

## 规范化与切分协议

实现位于 `src/data/chunking.py`。Week 3 在 `configs/default.yaml` 中选用 `text-normalization-v1`、`word-chunking-v1`、`chunk_words=365`、`overlap_words=40`，单位为词，不是 token。有效 Round 1–4 实验为 BM25 选择了此工作配置，依据与限制见[英文实验标准](../experiments/chunk_size/criteria.md)及[中文实验标准](../experiments/chunk_size/criteria_zn-CN.md)。它不是已证明的稳定最优值，也未验证为 dense/hybrid/reranker 配置。配置、结构及划分策略仍为 `v0-proposed`。

语料和样本构建器不读取 YAML，旧 CLI 默认值仍为 $200/40$。复现时必须显式传 `--chunk-size-words 365 --chunk-overlap-words 40`。参数影响块身份，改变后须重建依赖索引并刷新保存的块引用。

规范化逐段将 CRLF 和孤立 CR 转为 LF，仅裁掉首尾 Unicode 空白，丢弃变空段落；内部空白、标点、大小写、Unicode、段落顺序及证据标记不变。标题及章节名同样处理换行与首尾空白。空白或 `null` 章节名直接跳过，不猜测名称；空白论文标题使该论文不生成块。`NormalizationReport` 记录段落/章节计数、丢弃项及变换次数；样本 manifest 保留该报告。

词定义为 `\S+` 匹配的 Unicode 非空白连续段。每个窗口最多 `chunk_size_words` 个词段，下一窗口前进 `chunk_size_words - chunk_overlap_words` 个词段。文本保留从首个到末个选中词段的原始规范化字符跨度，不重建或折叠内部空白。同容器段落只以两个 LF 相连；内部结果保留块触及的原始段落索引。

`build_passages_from_record` 只读取 `id`、`title`、`full_text`，不读取问答、答案、证据、高亮证据或图表元数据。原始正文章节分别处理，同名章节也不合并；空白名称按上述规则跳过。空章节不使后续原始索引变化。当前公开构建器只生成 `full_text` 块，摘要/图表仍待团队决定。

`build_passages_from_records` 按论文 ID、来源类型、原始章节索引和块索引确定性排序。私有坐标为 `(paper_id, source_kind, section_index, chunk_index)`，公开 `Passage` 仍为八字段。邻接只在同一来源容器内填充。`validate_built_passages` 拒绝重复 ID、空文本、缺失块序号、悬空链接及不互反或跨容器邻接。不依据输出顺序或显示章节名推断边界。

## 拟议划分策略

策略为 `qasper-official-paper-disjoint-v0-proposed`，按整篇论文映射：`train -> development`、`validation -> validation`、`test -> held_out`。官方来源划分和项目角色保留在语料或实验 manifest 中，均不参与单块 ID。

固定 revision 的检查显示三划分分别含 $888$、$281$、$416$ 篇论文，划分内部无重复论文 ID，三组两两交集均为空，`observed_paper_disjoint: true`。这些是评审证据，不是运行时硬编码计数。

同一论文的标题、正文、问题、答案、证据及全部派生块必须属于同一项目角色。不按问题或块重新切分/平衡论文，也不将官方划分名称解释为模型训练用途。`src/data/split_policy.py` 的 `validate_paper_disjoint_splits` 要求恰有三个官方划分键、非空且无首尾空白的论文 ID、划分内无重复且划分间无交集；它不读文件、不改输入。

该提案由 `P3-D004` 跟踪，等待 P5/P6 评审。`evaluation.held_out_manifest: null` 表示问题及标注池尚未创建，不允许临时抽取 test 问题调参。未来重新映射须升级策略版本并重做泄漏检查；公开 Passage 结构及 ID 不变，manifest 记录划分、角色、策略、切分配置及输出哈希。

## 留出集资产使用策略

资产分为 `paper_text`、`question`、`answer`、`label`；用途分为 `index_for_inference`、`tuning`、`prompt_design`、`chunk_selection`、`final_evaluation`。`label` 包含人工相关性及从答案/证据派生的监督；提示设计包括模板措辞、few-shot 示例选择、critic/generator 提示迭代。

该策略适用于保留独立最终评估集的流程。显式选用的 `all-splits-testing` 将全部官方划分作为普通测试，并在 manifest 中记录例外；其结果不能声称独立留出性能。其他默认流程保持下表限制。

| 项目角色 | 资产 | 推理索引 | 调参 | 提示设计 | 切分选择 | 最终评估 |
| --- | --- | --- | --- | --- | --- | --- |
| `development` 或 `validation` | `paper_text`、`question`、`answer`、`label` | 允许 | 允许 | 允许 | 允许 | 允许 |
| `held_out` | `paper_text` | 允许 | 禁止 | 禁止 | 禁止 | 禁止 |
| `held_out` | `question` | 禁止 | 禁止 | 禁止 | 禁止 | 冻结后允许 |
| `held_out` | `answer` 或 `label` | 禁止 | 禁止 | 禁止 | 禁止 | 冻结后允许 |

`src/data/split_policy.py:assert_data_use_allowed` 是机器可读守卫。调用者须显式提供布尔 `evaluation_frozen`；留出问题仅在冻结后用于最终评估查询，答案/标签仅在冻结后用于最终评分及报告。不从日期、分支、文件或环境变量推断冻结状态。

开发和验证资产可用于调参、提示及切分选择，但必须在读取留出评估资产前记录并冻结所有决定。允许使用监督不代表允许把问题、答案、证据、worker ID、annotation ID 或标签写入检索语料。未来评估入口应仅向 RAG 暴露 `question_id`、`paper_id`、`question`，持久化推理结果后再读取答案及证据评分。

## 留出集索引净化

留出论文正文仅可用于推理证据索引。接收完整原始记录的构建器须在规范化/切分前，按团队批准的正文白名单构造内部视图，排除 `qas` 及嵌套的问题、答案、证据、高亮证据、worker ID 和 annotation ID。正文索引权限不包含同一记录内的监督字段。

语料 manifest 须记录来源划分、项目角色、`SPLIT_POLICY_VERSION`、切分配置及输出哈希；单个 `Passage` 不增加划分字段。留出问题/标注 manifest 与检索语料分离，保留冻结提交及配置，由 `P3-D005` 跟踪。

当前 `data.split_policy.held_out_usage` 允许 `index_paper_text: true`，禁止调参、提示设计和切分选择，并要求最终评估前显式冻结。`evaluation.held_out_manifest: null` 不是临时抽取留出问题的许可。冻结记录及重跑规则仍由 `P3-D005`、`P3-D006` 跟踪，待团队评审。

## 验证与参考快照

解压数据包或重建配套文件后，执行以下独立检查：

```powershell
python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages.jsonl --manifest data/processed/passages.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages_all_paper_text.jsonl --manifest data/processed/passages_all_paper_text.manifest.json
git check-ignore -v data/raw/qasper/manifest.json data/processed/papers.jsonl
```

语料检查器只需已发布的语料和 manifest，不需要原始/导出输入。构建器要求至少 $10{,}000$ 块、$100{,}000$ 原始词及足够的输出词。证据导出器检查论文/问答输入、哈希、语料范围及配置，重建块并验证精确 ID/文本后再映射。目前没有独立的证据映射检查 CLI；问答检查器不能替代映射验证。

下表为已有固定来源的 $365/40$ 参考快照，不表示已发布 Release。新数据包应以自身 manifest 和校验值为准。导出包含 $1{,}585$ 篇论文、$5{,}049$ 个问题及 $7{,}993$ 个答案标注；train、validation、test 分别有 $2{,}593$、$1{,}005$、$1{,}451$ 个问题。

| 语料 | 来源论文数 | 索引论文数 | 块数 | 原始词数 | 块内词数 | Casefold 后词型数 |
| --- | --- | --- | --- | --- | --- | --- |
| 开发语料 | $1{,}169$ | $1{,}168$ | $21{,}360$ | $4{,}262{,}446$ | $4{,}469{,}326$ | $174{,}636$ |
| 全论文正文 | $1{,}585$ | $1{,}584$ | $28{,}617$ | $5{,}659{,}921$ | $5{,}930{,}961$ | $210{,}909$ |

全论文正文语料中的 train、validation、test 块数分别为 $16{,}457$、$4{,}903$、$7{,}257$。词数按 Unicode 非空白连续段统计，原始词数不重复计算块重叠。

| 产物 | 预期 SHA-256 |
| --- | --- |
| `passages.jsonl` | `ecb1c601cdaebcd8e1e6bfeaf43f9cb4867f89e9762799ab06e7901549a9e403` |
| `passages_all_paper_text.jsonl` | `8eeef0119e322fc9253255e2c6db6cb38ec276d7ebf3669dd28a856a636aa93e` |
| `sample_passages_100.jsonl` | `b3343a793f7428ad796bff83a79f8bd70528a89cd9d099d978fe69727ec0fa2c` |

如已安装可选的 `datasets` 包，可在本地读取原始划分：

```python
import datasets

dataset = datasets.load_dataset(
    "json",
    data_files={
        "train": "data/raw/qasper/train.jsonl",
        "validation": "data/raw/qasper/validation.jsonl",
        "test": "data/raw/qasper/test.jsonl",
    },
)
```

这是本地 JSON 加载器，不是 Hub 下载或块构建器，记录仍为论文级。原始文件、生成语料、manifest、源压缩包、缓存及暂存目录均不纳入 Git。只有不再需要且满足实验保留要求时，才清理本地输出。
