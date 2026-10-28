# 第 4 周工作记录

[English](week-4-report-en.md) | **简体中文**

截至 2026/10/29

## Question-passage held-out 标注文件准备

整理已用于开发的禁用题，排除后独立冻结 $200$ 道 held-out 问题。按开发阶段冻结的 $365/40$ 分块配置，分别用 BM25、Dense、Hybrid 在问题所属论文内检索 top-$5$，合并去重得到 $1532$ 条 question-passage 配对，再导出两套独立的英文 Markdown 标注模板。当前标签全部为空，人员分配和人工判断尚未开展。

### 涉及代码

| 代码路径 | 工作内容 |
| --- | --- |
| `src/data/build_held_out_exclusions.py` | 汇总 P1/P2 指定题库及已保存的 P3 开发用题，生成禁用清单。 |
| `src/data/freeze_held_out.py` | 排除禁用题、冻结新版题单，保留并停用旧 BM25 产物。 |
| `src/data/build_common_pool.py` | 按冻结配置执行三路检索，保存原始排名并合并唯一配对。 |
| `src/data/build_multi_retriever_pilot.py` | 提供三路检索、配对合并和 Markdown 分批渲染的共用逻辑。 |
| `src/data/export_common_annotations.py` | 从已保存配对导出 A/B 两套空白模板，核验内容、分组、编号及文件哈希。 |
| `tests/data/test_held_out_exclusions.py`、`test_freeze_held_out.py`、`test_common_pool.py`、`test_multi_retriever_pilot.py`、`test_common_annotation_export.py` | 覆盖禁用题、抽样冻结、配对去重、排名关联及模板导出核验。 |

### 涉及文件

以下路径均相对于仓库根目录；前三项配置位于 `configs/`，其余数据产物位于 `data/processed/`。

| 文件或目录 | 用途 |
| --- | --- |
| `configs/held_out_exclusions.json`、`configs/held_out_sampling_v2.json`、`configs/annotation_pilot.json` | 禁用来源、抽样规则及开发阶段冻结的检索配置。 |
| `data/processed/qa_banned_for_held_out.jsonl`、`qa_banned_for_held_out.manifest.json` | 禁用题清单及来源记录。 |
| `data/processed/qa_for_held_out_v2.jsonl`、`qa_for_held_out_v2.manifest.json` | 当前正式使用的冻结题单及抽样记录。 |
| `data/processed/passages_all_paper_text.jsonl`、`papers.jsonl` | 检索正文及论文标题来源。 |
| `data/processed/annotation_common_v2/` | 保存题单、唯一配对、各算法原始排名、冻结配置、运行输入和 manifest。 |
| `data/processed/annotation_common_v2_markdown/annotator_A/batch_01.md` 至 `batch_10.md`，以及 `annotator_B/` 下的同名文件 | 队友需要评审的正式标注模板；A/B 内容相同，供不同人员独立填写。 |
| `data/processed/annotation_common_v2_markdown/manifest.json` | 模板来源、批次数量及文件哈希记录。 |
| `data/processed/historical_bm25_retirement.manifest.json` | 旧 BM25 文件的停用与保留记录。 |

### 每份 Markdown 的固定模板

每套共 $10$ 份 `.md`，每份包含 $20$ 道问题；每题有 $5$–$11$ 个去重 passage，因此各批配对数不同。所有文件使用以下结构：

| 层级 | 固定内容 |
| --- | --- |
| 文件头 | `# Passage relevance annotation`、空白 `Annotator:`、英文判断说明：能帮助回答问题（含部分有效证据）记为 `1`，否则记为 `0`；仅主题相近不足以判相关。 |
| 问题 | `## Question 0001` 形式的全局问题编号，随后是 `Paper:` 论文标题和引用格式的问题原文。 |
| 分组 | 依次为 `### Common Retrieved Chunks`、`### BM25`、`### Dense`、`### Hybrid`。Common 收录至少两种算法命中的配对，后三组仅收录各算法独有配对；空组显示 `None`。 |
| Passage | `#### Passage <编号>`、`Retrieved by:` 算法来源及引用格式的完整 passage 正文。Common 按稳定记录编号排列，独有组按对应算法原始排名排列。 |
| 判断栏 | `#### Relevance <同一编号>` 和空白 `Label:`；填写 `Label: 0` 或 `Label: 1`。 |

填写文件头的标注者姓名或约定标识后，逐条判断相关性，保留正文及编号。模板公开算法来源，不展示 gold 证据、检索分数、原始排名数值或内部 ID；同一配对仅出现一次，并用稳定编号关联回结构化配对文件。

## 当前重建状态：第 $2.5$–$2.8$ 步

独立的 `data/processed/qa_for_held_out_v2.jsonl` 冻结 $200$ 题，与 $2654$ 道禁用题无交集。全量 gold 映射的 $3329$ 题排除 $1884$ 道禁用题后，得到 $1445$ 道合格候选。抽样前固定种子 $2026102805$、ID 升序及 Python `Random(seed).sample` 规则。实际抽中 validation $78$ 题、test $122$ 题，覆盖 $174$ 篇论文，不设 split 配额或筛选。采用问题层面隔离，允许共享论文。接收范围为 P1/P2 负责人指定题库及已保存的 P3 开发用途；纯功能检查、原始导出、gold 映射及正常冻结评估不自动禁用。不声称覆盖未记录的外部/P4–P6 用题；后续明确新增开发用途证据须补充清单并复核资格。

原 BM25 题单及标注产物已停用，全部 $25$ 个文件和哈希由 `historical_bm25_retirement.manifest.json` 原位保留。停用不等于全部旧题受污染：$95$ 道旧题因其他来源禁用，$13$ 道合格旧题随机再次抽中。不复用旧配对、排名、分数、标签或编号。下方旧 BM25 章节仅描述历史产物与命令，不是当前交付；其中旧任务编号以当前 Week 4 清单为准。

BM25、Dense、Hybrid 已按开发阶段冻结的 $365/40$/paper-scoped/top-$5$ 配置分别重新检索，保存到 `data/processed/annotation_common_v2/`。每算法 $1000$ 次命中，$600$ 行排名合并为 $1532$ 条唯一配对，每题 $5$–$11$ 条；Common $975$ 条、BM25 独有 $277$ 条、Dense 独有 $254$ 条、Hybrid 独有 $26$ 条。数量来自实际并集去重，不固定为 $1000$ 条；设计范围为每题 $5$–$15$ 条。全部标签为空；新版正式 Markdown 已导出至下方独立目录，本次投影不生成 gold 关联核验文件。双语数据指南已说明现有六项产物、嵌套字段、冻结模型及融合配置、GitHub P3 获取方式和本地复现。

第 $2.7$ 步同步双语数据指南与报告、评估协议、需求文档、执行计划、项目概览、共享周追踪及本地交接和清单。再次执行只读 `python -m src.data.build_common_pool verify` 通过：$200$ 题、$1532$ 条配对、$600$ 行排名、每算法 $1000$ 次命中，并核验匹配输入及全部保留的历史哈希。本次文档任务未重跑检索、重新抽样或修改数据，未提交或推送。

第 $2.8$ 步已完成：`data/processed/annotation_common_v2_markdown/` 保存两套独立空白英文 Markdown，每套 $10$ 批，每批 $20$ 题，覆盖全部 $1532$ 条唯一配对。来源、分组、独有结果原始排名顺序、稳定编号、标题、问题和正文均与 JSONL 一致。每套各批配对数为 $156,158,156,155,146,152,151,152,144,162$。使用 `python -m src.data.export_common_annotations verify` 只读核验。A/B 仅为模板槽位，尚未分配实际人员；第 $2.9$ 步的分配、$3064$ 次独立判断、裁决前一致率及裁决待执行。未重新检索，冻结共同池和全部历史文件字节未变。

第 $2.9$ 步待执行：每条唯一配对分配两位不同标注者独立判断，共需 $2\times1532=3064$ 次初始判断。保留各自原件和原始标签，检查完整性及合法性，先算裁决前一致率，再保留独立的最终裁决标签。`Instruction.pdf` 第 $4$ 页 Question $4$ 要求至少 $1000$ 条人工标注 records、至少 $80\%$ 一致率，推荐三位标注者并允许两位；仅建池尚未满足要求。各算法按原始排名关联共同最终标签计算指标，不按 Markdown 顺序计算。池内 Recall@K 仅覆盖并集中已判断相关配对；QASPER evidence-reference recall 单独使用映射的 `gold_passage_ids`，受映射及覆盖限制。池外 passage 仍未判断。禁止使用 held-out 内容或结果调参；未来生成器和 agent 配置仍须单独冻结。见[评估协议](../../docs/EVALUATION.md#current-annotation-and-metric-protocol)。

第 $2.8$ 步核验：$26$ 项定向测试和 `tests/` 下全部 $570$ 项测试通过；字符、语法、Ruff 和 diff 检查通过。只读导出核验覆盖两套模板、冻结输入及保留的历史文件，最终复现的 Markdown 字节完全一致。双语数据指南已记录生成与核验命令及全部新增产物字段。

## 历史完成记录：第 $2.4.2$ 步

固定版本的 P1 $2593$ 题、P2 $106$ 题及 P3 $250$ 道选参题合并为 `data/processed/qa_banned_for_held_out.jsonl` 的 $2654$ 道唯一禁用题，保留 $3864$ 条符合排除条件的来源关联。负责人快照、原话、分支/commit/路径、哈希、用途判定和生成配置保存在 manifest 及 `configs/held_out_exclusions.json`。身份与来源核验通过，接收范围内无已知未决资格记录，不声称覆盖未记录的外部/P4–P6 用题。纯功能检查与正常冻结评估不自动禁用。核验包括 $5$ 项定向测试、语法/lint、来源 blob 字节一致和完整产物重建，均通过。双语数据指南已说明复现和嵌套字段。下一步为第 $2.5$ 步，保留并停用历史 BM25 产物，重新独立抽取 held-out 题单；本次未重新抽样、正式检索、提交或推送。

## 历史开发里程碑：第 $2.3$ 步

完成 BM25/Dense/Hybrid 开发试运行，按保存顺序取前 $5$ 道选参题。三路使用同一份 $365/40$ 语料、问题原文、所选论文的全部 passage 及 top-$5$，得到 $36$ 条唯一配对：共有 $25$ 条、BM25 独有 $5$ 条、Dense 独有 $6$ 条，Hybrid 无独有配对。所选 $5$ 篇论文共 $70$ 条 passage。`python -m scripts.build_annotation_pool multi-pilot` 导出到 `data/processed/annotation_pilot_multi_v2/`，结构化文件保留完整排名、分数和 gold 关联，两套独立英文 Markdown 模板公开算法来源并保留空标签，不展示 gold、分数和内部 ID。BGE small revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`、余弦相似度及等权 RRF $20/60$ 保存到 `frozen_config.json`，只验证开发可行性，未使用 held-out 选参。初步 `v1` 快照保留，`v2` 在仅修正 import 的 lint 问题后重跑，两版配对及排名文件字节一致。

定向测试 $46$ 项通过。独立落盘核验通过，覆盖输入、输出及当前源码哈希、问题原文、语料标题和正文、并集唯一性、各算法完整排名与 record 关联、检索后 gold 关联及标注视图字段隐藏。已同步双语数据指南和评估、需求记录。下方原 BM25 完成状态及盲审视图描述属于历史记录。pilot 完成时下一步为第 $2.4$ 步跨分支实际使用审计（现已按下述范围完成）；正式三算法扩池、held-out 资格复核、新版正式模板与人工判断待完成。本次未提交或推送。

## UI 论文选择目录

完成轻量论文目录构建模块，从 `data/processed/papers.jsonl` 提取论文元数据，结合当前配置使用的 `data/processed/passages.jsonl` 生成可选论文和章节列表，供 UI 一次加载。目录仅收录实际存在 passage 的论文和章节；这里的可检索表示有 passage 可参与检索，不保证每次查询命中。UI 接入尚未完成。

### 涉及代码

| 代码路径 | 职责 |
| --- | --- |
| `src/data/build_paper_catalog.py` | 提供 `build_paper_catalog()`，读取论文与 passage，校验 ID 唯一、正文非空和论文／章节引用，汇总各论文及章节的 passage 数。 |
| `scripts/build_paper_catalog.py` | 提供命令行入口，显式接收 `--passages`，写出 UTF-8 JSON，并拒绝覆盖已有输出。 |
| `tests/data/test_paper_catalog.py` | 覆盖来源顺序、同名章节合并、缺失元数据、空语料、重复 ID、无效引用、空正文和输出保护，共 $9$ 项测试。 |

### 成果文件与字段

本地成果为 `data/processed/paper_catalog.json`，包含 $1{,}168$ 篇可选论文、$16{,}187$ 个论文／章节名条目，覆盖所选语料的全部 $21{,}360$ 条 passage。目录及来源数据与 manifest 一起纳入 P3 工作分支。

目录顶层包含 `schema_version`、`passages_file` 和 `papers`；协议仍为 `v0-proposed`，`passages_file` 记录本次使用的 `data/processed/passages.jsonl`。每篇论文包含 `paper_id`、`title`、`authors`、`passage_count` 和 `sections`；每个章节包含 `name` 和 `passage_count`。字段类型、含义、构建命令及本地复现及 Git 数据获取流程见 `data/README.md` 的[目录章节（英文）](../../data/README.md#dataprocessedpaper_catalogjson)及 `data/README_zh-CN.md` 的[对应章节（中文）](../../data/README_zh-CN.md#dataprocessedpaper_catalogjson)。

章节按原文首次出现顺序排列，规范化后同名的章节合并计数；各章节计数之和等于论文计数。缺失或空白字符串使用 `null`，缺失作者列表使用 `[]`，不推测补写；当前 QASPER 导出未提供作者。UI 检索必须使用 `passages_file` 所记录的同一份语料，替换语料后须重建目录。

### 验证结果

独立读取已保存的目录和 passage 语料，核验论文 ID 唯一、全部论文／章节计数一致，以及总 passage 数完整覆盖。新增 $9$ 项测试通过，全量 $530$ 项测试通过；字符检查、Python 语法检查和 Ruff 检查通过。全量测试命令如下，显式指定仓库内的临时目录以避开旧临时目录的访问限制：

```powershell
python -m pytest tests -q --basetemp tmp/tmp_pytest_week4_catalog --tb=short
```

## 历史 BM25 标注候选池与 held-out 题单

完成本地工作计划第 $2.1$–$2.7$ 步，实现从历史选参题恢复、开发题试运行、held-out 抽样冻结到正式候选池及盲审文件导出的完整流程。正式题单包含 $200$ 道问题，每题使用 BM25 在所属论文内检索 $5$ 个不同 passage，共生成 $1{,}000$ 条唯一的 `(question_id, passage_id)` 配对。双人独立标注文件已准备好，实际人员分配、标签回收、一致率计算和分歧裁决尚未开展，因此第 $2$ 步整体仍未完成。

### 涉及代码

| 代码路径 | 职责 |
| --- | --- |
| `src/data/build_annotation_pool.py` | 实现历史题单提取、已有实验使用记录审计、开发题试运行、资格筛选与抽样冻结、BM25 配对生成、gold evidence 事后关联，以及独立标注 Markdown 分批导出；检查输入哈希并拒绝覆盖已有成果。 |
| `scripts/build_annotation_pool.py` | 提供 `prepare`、`pilot`、`freeze`、`export` 四阶段命令行入口，按顺序完成开发验证和正式导出。 |
| `src/data/export_evidence_mapping.py`、`scripts/export_evidence_mapping.py` | 调整 gold 映射导出说明与入口，保留 all-splits 全量参考映射，将命令行默认范围改为全量参考映射，保留开发范围及旧参数别名。 |
| `tests/data/test_annotation_pool.py` | 覆盖盲审字段隐藏与 gold 关联、Markdown 分批及全局编号、输入哈希和重复 ID 保护、历史使用排除与冻结题单保护，共 $4$ 项测试。 |
| `tests/evaluation/test_chunk_size.py` | 同步 gold 映射入口调整后的相关验证。 |

### 题单准备与抽样边界

保留 `data/processed/gold_evidence_mapping_all_splits.jsonl` 及其 manifest，作为全部官方 split 中有效问题的统一 gold 参考；删除旧的 `data/processed/gold_evidence_mapping.jsonl` 及其 manifest。全量映射的覆盖范围本身不决定某道题是否属于 held-out，具体用途由独立题单和实际使用记录决定。

固定 `chunk_size_words=365`、`chunk_overlap_words=40`，使用 `data/processed/passages_all_paper_text.jsonl`。从 Week 3 第 $4$ 轮已保存的 `results/chunk_size/round4_bm25_20261028_01/questions.jsonl` 提取全部 $250$ 道实际选参题，不依靠随机种子重建历史题单。先取其中 $5$ 道开发题生成 $25$ 条配对，验证检索、去重、导出及 gold evidence 关联，通过后再抽取 held-out 题单。

已有本地实验审计包含失效实验及试运行，共识别 $253$ 个已使用的问题 ID，其中 $3$ 个不在上述 $250$ 题内。全量 gold 映射中有 $251$ 个问题因已有使用记录被排除，另有 $1$ 个问题因所属论文不足 $5$ 条 passage 被排除，最终得到 $3{,}077$ 个合格候选问题。审计范围限于已保存的本地实验记录，不据此保证不存在未记录的外部使用。

抽样前仅依据 ID、使用记录和语料元数据判断资格，不预览候选问题、答案或证据内容。对合格 ID 升序排列，使用预先确定的随机种子 $20261028$ 无放回抽取 $200$ 题并保留抽取顺序；结果包含官方 `train` 的 $95$ 题、`validation` 的 $40$ 题和 `test` 的 $65$ 题。本次采用问题层面的隔离，允许与选参题共享论文，不声称论文互斥，也不将该题单称为普通测试人工标注集。

正式配对仅使用已保存的 held-out 题单，不重新抽题。冻结记录保存输入文件 SHA-256、抽样范围、排除原因、合格及最终 ID、检索配置、Git 提交、工作区修改状态、Python 版本及源码哈希。不得依据 held-out 问题、答案、证据、人工标签或评估结果调参或开发；本次冻结针对候选池的抽样和检索配置，不代表尚未实现的生成器或 agent 配置已冻结。

### 成果文件与字段

| 成果路径 | 内容与用途 |
| --- | --- |
| `data/processed/qa_for_choosing_chunk_size.jsonl` | 保存实际使用的 $250$ 道选参题，字段为 `question_id`、`paper_id`、`question`、`source_split`。 |
| `data/processed/annotation_preparation.manifest.json` | 保存历史输入哈希、使用记录审计、排除 ID、固定配置和预先确定的抽样规则。 |
| `data/processed/qa_for_held_out.jsonl` | 保存冻结后的 $200$ 道 held-out 问题，字段与选参题单相同。 |
| `data/processed/qa_for_held_out.manifest.json` | 保存资格筛选与抽样记录、最终题单、来源 split 计数、代码和输入指纹及使用边界。 |
| `data/processed/annotation_pilot/` | 保存开发题试运行的 $25$ 条配对、核验记录、manifest 和两套英文 Markdown 视图。 |
| `data/processed/annotation_held_out/pairs.jsonl` | 保存正式 $1{,}000$ 条配对及稳定的全局记录编号，作为后续人工标签关联的结构化数据源。 |
| `data/processed/annotation_held_out/verification.jsonl` | 在配对字段上增加检索方法、排名、分数、gold passage ID、命中情况和证据段落，仅供内部核验。 |
| `data/processed/annotation_held_out/manifest.json` | 保存正式导出的题单、配对数量、检索配置、代码版本、输入及输出哈希和冻结 manifest 哈希。 |
| `data/processed/annotation_held_out/annotator_A/`、`data/processed/annotation_held_out/annotator_B/` | 两套独立的英文 Markdown 标注模板，每套 $10$ 批，每批 $20$ 题、$100$ 条配对，供后续分配给不同标注者。 |

`pairs.jsonl` 的字段为 `record_number`、`question_id`、`paper_id`、`passage_id`、`paper_title`、`question`、`passage` 和 `label`，初始 `label` 全部为 `null`。核验文件额外包含 `retrieval_method`、`rank`、`score`、`gold_passage_ids`、`gold_evidence_match` 和 `evidence_paragraphs`；gold 信息仅在检索完成后关联，不参与检索和候选排序，也不向标注者分发。相关 manifest 的协议仍标记为 `v0-proposed`。

Markdown 每条记录使用 `## Record 0001` 形式的二级标题，并显示真实论文标题 `Paper: Full Paper Title`，下设 `### Question`、`### Passage`、`### Relevance`。文件头统一给出 `0 — Not relevant`、`1 — Relevant` 的英文判断说明，并保留 `Annotator:`；每条记录初始保留空白 `Label:`，标注者仅填写 `Label: 0` 或 `Label: 1`。同一问题的 $5$ 条配对相邻，全局编号从 $0001$ 到 $1000$ 保持不变，通过 JSONL 中的编号与内部 ID 映射回收标签。

两套视图隐藏内部 ID、gold 参考、检索方法、排名、分数及另一人的标签，仅提供问题、passage、真实论文标题和待填标签；不生成 HTML，不设置备注栏。`annotator_A` 和 `annotator_B` 目前只是独立模板槽位，不代表已分配实际队友或取得人工判断。

生成命令、完整字段类型及含义、输出路径和 held-out 使用边界已同步到 `data/README.md` 与 `data/README_zh-CN.md`；`docs/EVALUATION.md`、`docs/REQUIREMENTS.md`、`docs/WEEKLY_TRACKER.md` 及相关配置说明已调整为问题层面的隔离。按以下顺序执行各阶段；已有成果会触发保护，不应直接重复覆盖或重新抽样：

```powershell
python -m scripts.build_annotation_pool prepare
python -m scripts.build_annotation_pool pilot
python -m scripts.build_annotation_pool freeze
python -m scripts.build_annotation_pool export
```

### 验证结果

本阶段已保存的验证记录显示，相关定向测试 $43$ 项通过，全量测试 $534$ 项通过，字符检查、Python 语法检查和 Ruff 检查通过。全量测试使用以下命令：

```powershell
python -m pytest tests -q --basetemp tmp/tmp_pytest_week4_all --tb=short
```

独立读取落盘成果，核验开发试运行的 $5$ 题／$25$ 对和正式导出的 $200$ 题／$1{,}000$ 对数量正确；正式题单与历史已使用 ID 无交集，每题恰有 $5$ 个不同且属于同一论文的有效 passage，全部 `(question_id, passage_id)` 配对唯一。另核验 passage 正文与真实论文标题关联、gold 关联、冻结输入及输出哈希、盲审字段隐藏、两套 Markdown 的批次与全局编号，以及全部初始标签为空。

以上结果证明候选池与空白标注文件已准备完成，尚无人工相关性标签或一致率结果。后续按第 $2.8$ 步为每条记录安排两位不同队友独立判断，保留各自原件与原始标签，再汇总并进行一致率检查和分歧裁决。
