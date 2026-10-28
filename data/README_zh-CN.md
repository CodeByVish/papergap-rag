# QASPER 数据指南

[English](README.md)

原始数据、处理后数据及 manifest 纳入 P3 工作分支 `p3-qasper-foundation`。本指南说明 Git 共享方式、本地复现流程及每份处理后文件的字段。所有命令均从仓库根目录、使用项目 Python 3.11 环境运行；先安装 `requirements.txt` 或 `requirements-dev.txt`。

## 数据版本与更新

Week 4 第 $2.5$ 步已完成：独立的 `qa_for_held_out_v2.jsonl` 冻结 $200$ 道合格题，与禁用题单无交集。原 BM25 文件已停用，保留原位及哈希；正式三算法检索已完成，见下方共同池章节；新版标注导出仍待执行。当前命令和字段见下方新增章节，后文旧 BM25 复现章节仅描述历史。

Week 4 第 $2.4.2$ 步已完成本次范围内的跨分支禁用题单：P1 的 $2593$ 题、P2 的 $106$ 题及 P3 的 $250$ 道选参题合并为 $2654$ 道唯一禁用题，保留全部符合排除条件的重复来源。范围内无已知待核实资格记录，不声称覆盖未记录的外部/P4–P6 用题。第 $2.5$ 步在新版冻结前重建核验此清单；后续明确新增证据须在再次抽样前补充新版本。正式检索已在第 $2.6$ 步完成，历史产物字节未改动。

Week 4 第 $2.3$ 步新增开发专用 BM25/Dense/Hybrid 试运行，目录为 `data/processed/annotation_pilot_multi_v2/`：$5$ 题、$36$ 条唯一配对，其中共有 $25$ 条、BM25 独有 $5$ 条、Dense 独有 $6$ 条，Hybrid 无独有配对；每种算法各 $25$ 次命中。下方原 BM25 试运行和 held-out 产物保留为历史版本。正式三算法检索已在第 $2.6$ 步完成；第 $2.5$ 步已完成新版 held-out 资格复核。不应将历史 BM25 模板作为新共同池分发。使用 `python -m scripts.build_annotation_pool multi-pilot` 复现；重跑时用 `--multi-output` 指定新目录。数据与其他受跟踪产物一起从 GitHub P3 分支获取；模型权重单独准备到已忽略的 `.cache/huggingface/`。本地 `annotation_pilot_multi_v1/` 初步快照保留，`v2` 在仅修正 import 的 lint 问题后重跑，两版配对和排名文件字节一致；拒绝覆盖已有目录。

第 $2.6$ 步正式 BM25/Dense/Hybrid 检索保存到 `data/processed/annotation_common_v2/`。直接消费已保存的 $200$ 题，不重新抽题；核验完整禁用清单及全部历史哈希，建索引前保存开发已冻结的 $365/40$/paper-scoped/top-$5$ 配置。各算法保留全部原始排名/分数，每条并集配对共享一份空标签，不复用历史检索结果。本步不关联 gold evidence；新版 Markdown 导出和人工标注仍属第 $2.8$–$2.9$ 步。

从 GitHub P3 分支与其他受跟踪数据一起获取这些文件及匹配输入。本地复现使用 `python -m src.data.build_common_pool run --output tmp/tmp_annotation_common_v2`，拒绝已有目录。按下方开发指引将固定模型放入已忽略的 `.cache/huggingface/`；CLI 在导入模型前设置 `HF_HUB_OFFLINE=1` 并在结束后恢复。首次启动遗漏开发入口已有的离线包装，在可选 processor 探测阶段失败，尚未完成 Dense 索引，未生成排名或配对；其三份运行前文件本地保留于 `tmp/tmp_common_pool_failed_processor/`。成功运行未改变检索参数。计算指标时将各算法原始排名关联共同最终标签，不用 Markdown 展示顺序。候选池外 passage 未判断；池内 Recall@K 的分母为并集中已判断相关的配对，gold-evidence recall 另受映射覆盖限制。采用问题层面隔离，允许共享论文，禁止按 held-out 调参。

正式核验结果：$200$ 题，每算法 $1000$ 次命中，$600$ 行排名，合并为 $1532$ 条唯一配对，每题 $5$–$11$ 条；Common $975$、BM25 独有 $277$、Dense 独有 $254$、Hybrid 独有 $26$。初始标签均为空，尚未进行人工标注。

## `data/processed/annotation_common_v2/questions.jsonl`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `paper_id` | `string` | 原始 ID，保持冻结题单顺序。 |
| `question` | `string` | 未经修改的问题原文。 |
| `source_split` | `string` | 官方来源，不按 split 筛选。 |

## `data/processed/annotation_common_v2/pairs.jsonl`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 本正式版本内从一开始的稳定编号。 |
| `question_id`, `paper_id`, `passage_id` | `string` | 唯一问题/passage 配对及论文范围。 |
| `source_split`, `question`, `paper_title`, `passage` | `string` | 来源、问题原文、真实标题及完整 passage 正文。 |
| `label` | `null` | 共享一份最终相关性标签，初始均为空。 |
| `retrieved_by[]` | `string` | 按 BM25/Dense/Hybrid 顺序保存真实来源。 |
| `retrievals[]` | `object` | 每个来源对应一份原始检索关系。 |
| `retrievals[].method` | `string` | BM25、Dense 或 Hybrid。 |
| `retrievals[].rank` | `integer` | 算法原始排名，从一至五。 |
| `retrievals[].score` | `number` | 有限的原始 BM25、余弦或 RRF 分数。 |
| `display_group` | `string` | 至少两路命中归 Common Retrieved Chunks，否则归唯一算法。 |

## `data/processed/annotation_common_v2/rankings.jsonl`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `method` | `string` | 每道冻结问题、每种算法一行。 |
| `hits[]` | `object` | 按原始排名保存恰好五个不同的同论文命中。 |
| `hits[].passage_id` | `string` | 语料原始 passage ID。 |
| `hits[].record_number` | `integer` | 关联唯一并集配对的稳定编号。 |
| `hits[].rank` | `integer` | 一至五的原始排名。 |
| `hits[].score` | `number` | 未经修改的有限算法分数。 |

## `data/processed/annotation_common_v2/frozen_config.json`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed。 |
| `chunk_size_words`, `chunk_overlap_words`, `top_k`, `question_count` | `integer` | $365$、$40$、$5$ 和 $200$。 |
| `question_selection`, `scope`, `record_order`, `label_policy` | `string` | 保存题单、论文范围、首次遇见顺序编号及每条配对一份空标签。 |
| `execution.HF_HUB_OFFLINE`, `execution.model_loading` | `string` | 离线值 1，与开发入口相同的模型加载策略。 |
| `retrieval` | `object` | 规范化的开发冻结配置，字段见开发 frozen-config 章节。 |
| `retrieval.mode` | `string` | hybrid，不使用重排器。 |
| `retrieval.candidate_k`, `retrieval.rrf_k` | `integer` | $20$ 和 $60$，等权 RRF。 |
| `retrieval.dense` | `object` | revision/device/batch_size/cache_folder/local_files_only 见开发章节，值未改变。 |
| `retrieval.reranker` | `object` | 规范化后的未启用默认值，本次不加载或使用。 |
| `retrieval.reranker.revision`, `retrieval.reranker.device`, `retrieval.reranker.cache_folder` | `string` | 未启用的 revision、CPU 及本地缓存路径。 |
| `retrieval.reranker.batch_size`, `retrieval.reranker.max_length` | `integer` | 未启用的默认值 $8$ 和 $512$。 |
| `retrieval.reranker.local_files_only` | `boolean` | 未启用的离线默认值 true。 |
| `retrievers.<method>` | `object` | 完整生效元数据，包括嵌套 bm25/dense/reranker、依赖版本和融合配置；字段与开发 manifest 的 retrievers 表一致。 |
| `retrievers.<method>.id`, `retrievers.<method>.mode`, `retrievers.<method>.source_commit`, `retrievers.<method>.scope`, `retrievers.<method>.score`, `retrievers.<method>.tie_break` | `string` | 实现标识、算法、上游提交、论文范围、原始分数含义及并列规则。 |
| `retrievers.<method>.packages.<package>` | `string` | 已安装依赖版本。 |
| `retrievers.<method>.persistent_score_cache`, `retrievers.<method>.bm25.enabled`, `retrievers.<method>.dense.enabled`, `retrievers.<method>.reranker.enabled` | `boolean` | 缓存及组件开关，不使用持久化分数缓存或重排器。 |
| `retrievers.<method>.bm25.tokenizer` | `string` | Casefold 加 Unicode 单词序列，独立 Dense 不含此字段。 |
| `retrievers.<method>.bm25.k1`, `retrievers.<method>.bm25.b`, `retrievers.<method>.bm25.epsilon` | `number` | 生效的 BM25 参数 $1.5$、$0.75$、$0.25$。 |
| `retrievers.<method>.dense.revision`, `retrievers.<method>.dense.device`, `retrievers.<method>.dense.cache_folder`, `retrievers.<method>.dense.model_name`, `retrievers.<method>.dense.tokenizer_revision`, `retrievers.<method>.dense.query_instruction`, `retrievers.<method>.dense.normalization`, `retrievers.<method>.dense.similarity_metric`, `retrievers.<method>.dense.index_type`, `retrievers.<method>.dense.truncation`, `retrievers.<method>.dense.truncation_observation` | `string` | 生效的 Dense 模型及编码元数据，具体含义见开发字段表。 |
| `retrievers.<method>.dense.batch_size`, `retrievers.<method>.dense.max_seq_length` | `integer` | 生效的 Dense batch size $32$、token 上限 $512$。 |
| `retrievers.<method>.dense.local_files_only` | `boolean` | 生效的 Dense/Hybrid 模型采用 true，离线加载。 |
| `retrievers.Hybrid.candidate_k_per_source`, `retrievers.Hybrid.rrf_k`, `retrievers.Hybrid.final_top_k` | `integer` | $20$、$60$ 和 $5$。 |
| `retrievers.Hybrid.rerank_all_fused_candidates` | `boolean` | False。 |

## `data/processed/annotation_common_v2/run_inputs.json`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `inputs.<path>` | `string` | 运行前配置、开发冻结、题单/manifest、禁用清单、语料、QA/论文及停用记录的精确字节 SHA-256。 |
| `code.commit`, `code.python` | `string` | 检索前记录的 HEAD 与 Python 版本。 |
| `code.working_tree_status[]` | `string` | 保存的 Git 短状态，包括未提交实现。 |
| `code.source_sha256.<path>` | `string` | 精确实现哈希，写结果前重新检查 src 和 scripts。 |

## `data/processed/annotation_common_v2/manifest.json`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `purpose`, `reason`, `reuse_policy`, `usage_boundary` | `string` | 提议中的正式版本、重建原因、不复用旧结果及评估边界。 |
| `historical_retained_files.<path>` | `string` | 全部 25 个旧 BM25 文件路径及未变的字节哈希。 |
| `settings` | `object` | 与 frozen_config.json 一致，嵌套字段见上文。 |
| `inputs.<path>`, `outputs.<path>` | `string` | 精确输入/输出哈希，manifest 不包含自身哈希。 |
| `code` | `object` | 嵌套字段与上文 run_inputs.json 一致。 |
| `indexed_paper_count`, `indexed_passage_count` | `integer` | 索引包含所选论文全部 passage，与全语料的 paper-scoped 检索等价。 |
| `validation.question_count`, `validation.pair_count`, `validation.ranking_count`, `validation.hits_per_method` | `integer` | 200 题、实际并集数量、600 行排名及每算法 1000 次命中。 |
| `validation.pair_counts_per_question.<question_id>`, `validation.group_counts.<group>` | `integer` | 每题及来源分组的实际唯一配对数量。 |
| `validation.pair_count_range[]` | `integer` | 实际最小/最大值，均在五至十五范围内。 |
| `runtime.platform`, `runtime.processor`, `runtime.timing_policy` | `string` | 主机及单次建索引加检索的计时规则，不作为延迟基准。 |
| `runtime.elapsed_seconds` | `number` | 建索引及检索墙钟秒数。 |

## `data/processed/qa_for_held_out_v2.jsonl`

第 $2.5$ 步为新版共同评估冻结独立 held-out 题单。首次抽样前，`configs/held_out_sampling_v2.json` 已固定种子 $2026102805$、候选 ID 升序及 Python `Random(seed).sample` 无放回抽样规则，保留抽取顺序。all-splits gold 映射有 $3329$ 道有效问题，排除 $1884$ 道禁用题；其余问题均满足每篇至少 $5$ 个 passage，得到 $1445$ 道候选。冻结 $200$ 道唯一问题，与禁用题单无交集：validation $78$ 题、test $122$ 题，覆盖 $174$ 篇论文，每篇至少 $6$ 个 passage。split 数量是随机结果，不是配额；不按官方 split 筛选。采用问题层面隔离，允许共享论文。抽样未通过预览候选问题、答案、证据或历史检索/标签内容选题。

在仓库根目录、项目 Python $3.11$ 环境执行以下命令，生成时拒绝覆盖已有文件。停用命令已经执行，不要删除记录重跑。JSONL、下方两份 manifest、配置及匹配输入均与其他受跟踪数据一起从 GitHub P3 分支获取，无须 Release。本地使用 `python -m src.data.freeze_held_out freeze --output tmp/tmp_qa_for_held_out_v2.jsonl` 复现相同 JSONL 字节；配套 manifest 记录新输出路径及本地代码身份。

```powershell
python -m src.data.freeze_held_out retire
python -m src.data.freeze_held_out freeze
python -m src.data.freeze_held_out verify
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id` | `string` | 原始唯一问题 ID，按冻结抽取顺序保存。 |
| `paper_id` | `string` | paper-scoped 检索使用的论文 ID。 |
| `question` | `string` | 抽取 ID 后从 QA 逐字复制的问题原文。 |
| `source_split` | `string` | 官方 split 来源，不直接指定评估角色。 |

## `data/processed/qa_for_held_out_v2.manifest.json`

由 `python -m src.data.freeze_held_out freeze` 生成，使用上述 `verify` 重建核验。抽样前验证完整禁用题单及历史文件哈希，核对 gold、语料、QA 及其配套输入哈希、固定 $365/40$ 分块、唯一非空 passage 和原始身份元数据。保存全部合格 ID、互斥排除列表及最终 ID。后续明确的开发用题证据须补充新禁用题单/版本；禁止根据 held-out 内容或结果选择系统配置。本次题单冻结不执行第 $2.6$ 步检索，也不冻结后续生成器或 agent 配置。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `purpose`, `status` | `string` | 暂定 schema、held-out 用途及冻结状态。 |
| `configuration` | `object` | 预先确定的完整抽样配置。 |
| `configuration.schema_version` | `string` | `v0-proposed`。 |
| `configuration.seed`, `configuration.question_count`, `configuration.minimum_passages_per_paper` | `integer` | 种子、题数及 passage 数量门槛。 |
| `configuration.sampling_rule`, `configuration.scope`, `configuration.isolation`, `configuration.eligibility` | `string` | 排序/抽样规则、all-splits 范围、问题隔离及元数据筛选条件。 |
| `configuration.reason`, `configuration.usage_boundary` | `string` | 重新抽样原因及禁止利用 held-out 调参的边界。 |
| `inputs.<path>` | `string` | 配置、停用记录、禁用题单/manifest、gold/manifest、语料/manifest 和原始导出的 SHA-256。 |
| `code.commit`, `code.python`, `code.implementation_sha256` | `string` | 生成时 HEAD、Python 版本及未提交实现的精确指纹；核验保留原 HEAD。 |
| `candidate_count`, `banned_question_count`, `question_count`, `paper_count` | `integer` | gold 候选数、完整禁用题数、抽中题数及论文数。 |
| `eligible_question_ids[]` | `string` | 升序合格问题 ID。 |
| `rejections.banned[]`, `rejections.fewer_than_minimum_passages[]` | `string` | 排除 ID；禁用优先于语料数量不足，避免重复统计。 |
| `question_ids[]` | `string` | 按抽取顺序冻结的最终 ID。 |
| `source_split_counts.<split>` | `integer` | 抽中题目的 split 数量。 |
| `selected_paper_passage_counts.<paper_id>` | `integer` | 各入选论文在语料中的唯一 passage 数。 |
| `historical_redrawn_question_ids[]` | `string` | 随机再次抽中的 $13$ 道合格旧题，不复用旧结果。 |
| `validation.exactly_200_unique`, `validation.banned_intersection_empty`, `validation.at_least_five_passages_per_paper` | `boolean` | 题数/唯一性、禁用交集及论文容量检查。 |
| `validation.canonical_question_text`, `validation.retained_history_hashes_verified`, `validation.exclusion_inventory_reconstructed` | `boolean` | 原文一致、历史字节未改动及完整禁用题单重建检查。 |
| `output.path`, `output.sha256` | `string` | 独立版本题单路径及字节哈希。 |
| `next_action` | `string` | 原样保留生成时的下一步说明；第 $2.6$ 步检索现已在独立共同池目录完成。 |

## `data/processed/historical_bm25_retirement.manifest.json`

由 `python -m src.data.freeze_held_out retire` 一次生成；`verify` 在重建新版冻结题单前核验此文件及全部历史字节。原 $25$ 个文件继续保存在 `qa_for_held_out.jsonl`、其 manifest 及 `annotation_held_out/`；配对、排名、分数、标签和编号仅属于已停用的历史 BM25 版本。存在此标记时，旧 `freeze` 及正式 BM25 `export` 命令拒绝执行；开发 pilot 入口仍可用。停用是为统一评估主动重新抽样，不代表全部旧题受污染。第 $2.4$ 步用途审计认定旧 BM25 为正常冻结评估，不整体禁用；其中 $95$ 题仍因其他已接收来源被禁用，其余 $105$ 题可继续接受候选元数据筛选。本次未发现新增调参用途证据。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `status`, `reason` | `string` | 暂定 schema、停用状态及重新抽样原因。 |
| `retained_files.<path>` | `string` | 每份原始历史文件的 SHA-256。 |
| `banned_manifest_sha256` | `string` | 已核验第 $2.4$ 步禁用 manifest 哈希。 |
| `usage_decision.source_id`, `usage_decision.path`, `usage_decision.sha256` | `string` | 历史用途判定身份及保存的 BM25 manifest 哈希。 |
| `usage_decision.question_ids[]` | `string` | 原评估的全部 $200$ 道题 ID。 |
| `usage_decision.decision`, `usage_decision.usage`, `usage_decision.reason` | `string` | 正常冻结评估不自动禁用；其他来源仍然适用。 |
| `historical_question_count` | `integer` | 原题单数量。 |
| `historical_banned_question_ids[]`, `other_historical_question_ids[]` | `string` | 原题单中属于/不属于完整禁用题单的 ID。 |
| `reuse_policy`, `replacement_questions` | `string` | 不复用旧结果的规则及规范替代题单路径。 |

## `data/processed/held_out_exclusion_sources/p1_used_question_ids.jsonl`

逐字节保存分支 `p1/week3-week4`、commit `3bb545c967efe63197cb99a799628162f5c2b512` 的 `docs/handoffs/p1_used_question_ids.jsonl`，共 $2593$ 个唯一 ID。随其他数据从 GitHub P3 分支获取。本地复现快照：使用 Python `subprocess.check_output` 捕获 `git show <commit>:docs/handoffs/p1_used_question_ids.jsonl`，再用 `Path.write_bytes` 保存，核对 `configs/held_out_exclusions.json` 的 SHA-256；避免改变字节的 shell 文本重定向。负责人原话及固定来源保存在 config/manifest。题库引用的历史文件无须存在或重新解析，缩减指定 ID 须有负责人明确更正。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `paper_id`, `source_split` | `string` | 交付的 QA 身份，与本地 QA 核对。 |
| `sources` | `array<string>` | 负责人报告的全部使用路径，原样保留。 |
| `usage` | `string` | 负责人描述的用途。 |
| `usage_categories` | `array<string>` | 负责人提供的细分用途。 |

## `data/processed/held_out_exclusion_sources/p2_used_question_ids.jsonl`

逐字节保存分支 `p2/question-usage-inventory`、commit `3b13f22fe6df29d15babea529cf2fc8f13c18f68` 的 `docs/handoffs/p2_used_question_ids.jsonl`，共 $106$ 个唯一 ID。从 GitHub P3 分支取得，或使用相同 Python 字节保真 `git show` 方法替换 commit/路径后复现，并核对固定 SHA-256。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `paper_id`, `source_split` | `string` | 交付的 QA 身份。 |
| `sources` | `array<string>` | 负责人报告的全部使用路径。 |
| `usage` | `string` | 负责人描述的用途。 |

## `data/processed/qa_banned_for_held_out.jsonl`

生成命令：`python -m src.data.build_held_out_exclusions`；已有产物核验：`python -m src.data.build_held_out_exclusions --verify`。本地复现且不替换共享数据：`python -m src.data.build_held_out_exclusions --output tmp/tmp_qa_banned_for_held_out.jsonl`，JSONL 字节相同，manifest 记录新输出路径和生成身份。拒绝覆盖已有输出。命令使用受跟踪的快照、QA、已保存 preparation/pilot manifest，无需网络、模型、随机种子重建或解析历史结果。JSONL、manifest、快照及 config 一起从 GitHub P3 分支获取，无须 Release。

负责人指定 ID 全部禁用。其他题按是否用于选择或调整模型、参数、算法、prompt 或证据处理规则判定，失败/作废实验遵循同一用途规则。P3 历史选参比较和三次开发 pilot 保留来源。旧 preparation 一律禁用的 $253$ 题不直接复用：$3$ 道功能 smoke 题及原 $200$ 题冻结 BM25 评估不自动禁用，但仍可能因其他符合排除条件的来源而禁用。原始导出、gold 映射本身不导致禁用。功能测试原话与用途判定保存在 config/manifest。禁用题单本身不是题单冻结记录；独立的 `v2` 冻结见上文。采用问题层面隔离，允许共享论文。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `paper_id`, `question`, `source_split` | `string` | 唯一 ID、对应论文、未修改问题原文和官方 split。 |
| `sources` | `array<object>` | 全部符合排除条件的来源，保留重复使用。 |
| `sources[].source_id`, `sources[].usage`, `sources[].exclusion_reason` | `string` | manifest 来源键、用途和排除理由。 |
| `sources[].original_record` | `object` | 完整交付行，保留全部原始元数据。 |
| `sources[].original_record.question_id` | `string` | 必有，用于回连原始 QA。 |
| `sources[].original_record.paper_id`, `.question`, `.source_split` | 可选 `string` | 来源提供的身份和原文，存在时与 QA 核对。 |
| `sources[].original_record.sources`, `.usage_categories` | 可选 `array<string>` | 完整负责人原始路径和分类。 |
| `sources[].original_record.usage` | 可选 `string` | 负责人原始用途描述。 |

## `data/processed/qa_banned_for_held_out.manifest.json`

与题单使用同一命令生成和核验。输入用精确字节 SHA-256，负责人来源另固定分支/commit/路径。本地版本记录生成时 HEAD/分支及输入/实现哈希，包含尚未提交的新文件，不表示这些文件当时已提交。核验允许后续 HEAD 改变，但重建题单并检查全部保存哈希。未知 ID、身份冲突、来源内重复问题 ID、固定哈希/数量变化、来源丢失或新增未决历史/pilot 用途均在写出前报错。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `purpose`, `repository`, `scope`, `exclusion_rule` | `string` | `v0-proposed`、用途、仓库和有范围边界的使用规则。 |
| `local_source_version` | `object` | 生成版本。 |
| `local_source_version.branch`, `.commit` | `string` | 本地 P3 分支和完整 HEAD SHA。 |
| `implementation` | `object` | 精确实现身份。 |
| `implementation.path`, `.sha256` | `string` | 模块路径及 SHA-256。 |
| `inputs` | `object<string,string>` | 配置/QA/快照/preparation/pilot/评估路径到 SHA-256 的映射。 |
| `owner_inventories` | `array<object>` | 负责人来源及原话。 |
| `owner_inventories[].source_id`, `.branch`, `.commit`, `.path`, `.snapshot`, `.sha256`, `.owner_statement` | `string` | 负责人键、来源身份、快照、哈希及原话。 |
| `owner_inventories[].question_count` | `integer` | 交付的唯一题数。 |
| `source_counts`, `source_split_counts` | `object<string,integer>` | 合并前各来源题数、合并后各 split 题数。 |
| `question_count`, `provenance_count` | `integer` | 唯一问题数及符合排除条件的来源关联数。 |
| `usage_decisions` | `array<object>` | P3 历史使用/冻结评估的用途判定。 |
| `usage_decisions[].source_id`, `.path`, `.sha256`, `.decision`, `.usage`, `.reason` | `string` | 来源身份/哈希、判定、用途及理由。 |
| `usage_decisions[].question_ids` | `array<string>` | 每项判定覆盖的已保存 ID。 |
| `configuration` | `object` | 确定性生成配置。 |
| `configuration.join_key`, `.order`, `.sampling` | `string` | 按 ID 回连、ID 升序、不抽样。 |
| `configuration.question_fields` | `array<string>` | 保留的原始问题字段。 |
| `unresolved_records` | `array<object>` | 接收范围内为空，未知用途阻止生成。 |
| `validation` | `object<string,boolean>` | ID 唯一、字段完整、身份一致、负责人/选参/来源完整覆盖和范围内未决记录检查。 |
| `output` | `object` | 输出题单身份。 |
| `output.path`, `.sha256` | `string` | 输出路径和 SHA-256。 |

## `data/processed/annotation_pilot_multi_v2/questions.jsonl`

本试运行所有产物均使用 `python -m scripts.build_annotation_pool multi-pilot --config configs/annotation_pilot.json` 生成。按保存顺序取选参题单前 $5$ 题，核验题单与 preparation 中的哈希一致，从同一份 $365/40$ 语料索引这些论文的全部 passage。不打开 held-out 题单或结果。CLI 在导入模型前启用离线模式，覆盖可选 processor 探测，结束后恢复原进程环境。首次准备固定版本权重：

```powershell
python -c "from huggingface_hub import snapshot_download; snapshot_download('BAAI/bge-small-en-v1.5', revision='5c38ec7c405ec4b44b94cc5a9bb96e735b38267a', cache_dir='.cache/huggingface', allow_patterns=['*.json','*.txt','*.safetensors','1_Pooling/*'], ignore_patterns=['onnx/*','openvino/*'])"
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `paper_id` | `string` | 原始问题与论文 ID。 |
| `question` | `string` | 未修改的问题原文。 |
| `source_split` | `string` | 官方 split 来源，不代表评估资格。 |

## `data/processed/annotation_pilot_multi_v2/frozen_config.json`

由相同的 `multi-pilot` 命令生成，是 `configs/annotation_pilot.json` 的精确副本。正式运行前复用此成功配置。此次沿用已有模型及默认融合设置验证可行性，不声称检索质量最优，不用 held-out 内容或结果选参。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | `v0-proposed`。 |
| `question_count`, `question_selection` | `integer`, `string` | 保存顺序中的前 $5$ 道开发题。 |
| `chunk_size_words`, `chunk_overlap_words`, `top_k` | `integer` | $365$、$40$、$5$。 |
| `retrieval` | `object` | 与单路检索器共用的 Hybrid 配置。 |
| `retrieval.mode` | `string` | `hybrid`，不重排序。 |
| `retrieval.candidate_k`, `retrieval.rrf_k` | `integer` | 每路最多 $20$ 候选；等权 RRF $1/(60+rank)$，$k=60$。 |
| `retrieval.dense` | `object` | BGE small English v1.5 推理配置。 |
| `retrieval.dense.revision` | `string` | 模型及 tokenizer 固定 SHA：`5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`。 |
| `retrieval.dense.device`, `retrieval.dense.batch_size` | `string`, `integer` | CPU，批大小 $32$。 |
| `retrieval.dense.cache_folder`, `retrieval.dense.local_files_only` | `string`, `boolean` | 项目内忽略目录，启用离线加载。 |

Dense 使用 L2 归一化向量，经 FAISS `IndexFlatIP` 计算余弦相似度，按 $512$ tokens 截断；问题前缀为 `Represent this sentence for searching relevant passages: `，passage 无前缀，导出保留完整正文。BM25 使用 casefold/Unicode word 分词，`k1=1.5`、`b=0.75`、`epsilon=0.25`。同分按 passage ID 升序，manifest 保存完整有效配置和依赖版本。

## `data/processed/annotation_pilot_multi_v2/pairs.jsonl`

使用 `python -m scripts.build_annotation_pool multi-pilot` 生成。每个 `(question_id, passage_id)` 一行，每题 $5$–$15$ 行。编号按题单顺序及 BM25/Dense/Hybrid 首次发现顺序生成，仅属于本开发版本，不改历史正式池编号。一份最终相关性标签供所有命中该配对的算法共用。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 本版本从 $1$ 开始的稳定编号。 |
| `question_id`, `paper_id`, `passage_id` | `string` | 原始关联 ID。 |
| `source_split`, `question`, `paper_title`, `passage` | `string` | 来源、问题原文、真实标题与完整 passage。 |
| `label` | `null or integer` | 初始为空，后续人工二元相关性。 |
| `retrieved_by` | `array<string>` | 按 BM25/Dense/Hybrid 顺序保存全部真实来源。 |
| `display_group` | `string` | 两路或三路共有为 `Common Retrieved Chunks`，否则为唯一来源名称。 |
| `retrievals` | `array<object>` | 全部算法配对关系及原始排名。 |
| `retrievals[].method`, `retrievals[].rank`, `retrievals[].score` | `string`, `integer`, `number` | 算法、从 $1$ 开始的原始排名及 BM25/余弦/RRF 原生分数。 |

## `data/processed/annotation_pilot_multi_v2/rankings.jsonl`

使用 `python -m scripts.build_annotation_pool multi-pilot` 生成，每题三行，分别保存各算法完整 top-$5$。计算指标时按原始排名关联共同标签，不按 Markdown 分组顺序计算。池外 passage 相关性未知；池内 Recall@K 只覆盖并集中已标相关记录，gold-reference recall 则受证据映射覆盖范围限制。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id`, `method` | `string` | 问题及公开的算法名称。 |
| `hits` | `array<object>` | 按原始排名保存的 $5$ 个不同、有效、同论文结果。 |
| `hits[].passage_id`, `hits[].record_number` | `string`, `integer` | 关联唯一配对。 |
| `hits[].rank`, `hits[].score` | `integer`, `number` | 原始排名和原生分数。 |

## `data/processed/annotation_pilot_multi_v2/verification.jsonl`

使用 `python -m scripts.build_annotation_pool multi-pilot` 生成，不作为标注视图分发。包含上述 `pairs.jsonl` 的全部字段，并在所有检索结束后关联参考证据，不使用参考初始化人工标签。嵌套证据字段与下方历史 `annotation_held_out/verification.jsonl` 表格保持一致。

| 新增字段 | 类型 | 含义 |
| --- | --- | --- |
| `gold_passage_ids` | `array<string>` | 映射的参考 passage ID。 |
| `gold_evidence_match` | `boolean` | 当前 passage 是否命中映射参考。 |
| `evidence_paragraphs` | `array<object>` | 原始证据段落及重叠信息。 |
| `evidence_paragraphs[].location`, `evidence_paragraphs[].text` | `string` | 来源坐标与原始正文。 |
| `evidence_paragraphs[].section_index`, `evidence_paragraphs[].paragraph_index` | `integer` | 从 $0$ 开始的章节及段落位置。 |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | 并集是否覆盖全部非空白字符。 |
| `evidence_paragraphs[].passage_matches` | `array<object>` | 参考段落与语料的重叠关系。 |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | 重叠 passage ID。 |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | 原文半开字符区间。 |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | 单个 passage 是否覆盖整段。 |

## `data/processed/annotation_pilot_multi_v2/manifest.json`

使用 `python -m scripts.build_annotation_pool multi-pilot` 生成。输入输出 SHA-256 标识本独立版本，拒绝覆盖已有目录。共享接口仍为 `v0-proposed`，保留历史 BM25 冻结记录及编号。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `purpose` | `string` | 提议版 schema 与开发试运行用途。 |
| `question_ids`, `question_count`, `pair_count` | `array<string>`, `integer`, `integer` | 有序题单及实际数量。 |
| `group_counts`, `pair_counts_per_question` | `object<string,integer>` | 各展示组与各题去重配对数。 |
| `indexed_paper_count`, `indexed_passage_count` | `integer` | 所选论文的完整索引范围。 |
| `settings` | `object` | 上述 `frozen_config.json` 的全部字段。 |
| `code` | `object` | 与下方历史 manifest 相同的 `commit`、`python`、`working_tree_status`、`source_sha256.<path>` 字段及类型。 |
| `inputs.<path>`, `outputs.<path>` | `string` | 输入输出的精确 SHA-256，不含 manifest 自身。 |
| `retrievers` | `object` | `BM25`、`Dense`、`Hybrid` 三种方法的有效元数据。 |
| `retrievers.<method>` | `object` | 下方历史 `retriever` 元数据，以及以下 Dense/融合字段。 |
| `retrievers.<method>.dense` | `object` | 启用状态、上表 Dense 配置、模型/tokenizer 版本、问题前缀、归一化、相似度、索引类型和截断说明。 |
| `retrievers.<method>.dense.enabled` | `boolean` | 是否启用 Dense。 |
| `retrievers.<method>.dense.max_seq_length` | `integer` | $512$。 |
| `retrievers.<method>.dense.model_name`, `tokenizer_revision`, `query_instruction`, `normalization`, `similarity_metric`, `index_type`, `truncation`, `truncation_observation` | `string` | 均为 `dense` 下的同级字段，说明精确编码规则；未测量实际截断频率。 |
| `retrievers.Hybrid.candidate_k_per_source`, `retrievers.Hybrid.rrf_k`, `retrievers.Hybrid.final_top_k` | `integer` | $20$、$60$、$5$。 |
| `retrievers.Hybrid.rerank_all_fused_candidates` | `boolean` | False。 |
| `configuration_status`, `selection_rationale`, `record_number_scope`, `validation` | `string` | 冻结状态、开发选择依据、编号范围和核验说明。 |

## `data/processed/annotation_pilot_multi_v2/annotator_A/` 和 `annotator_B/`

使用 `python -m scripts.build_annotation_pool multi-pilot` 生成，每个槽位为本次 $5$ 道开发题生成一批英文 Markdown，正式新版导出待完成。公开算法与标注者身份，隐藏 gold、分数、排名、内部 ID 和对方标签，无 HTML 或备注栏。两路或三路共有配对只出现一次，按稳定编号排列；独有配对按所属算法原始排名排列。每批最多 $20$ 题，同题不拆批，空分组显示 `None`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `Annotator:` | `text` | 填姓名或约定标识，不要求匿名。 |
| `Question NNNN`, `Paper:` | `heading`, `text` | 顺序题号、真实标题，随后引用问题原文。 |
| `Common Retrieved Chunks`, `BM25`, `Dense`, `Hybrid` | `level-three headings` | 共有组与三种算法独有组。 |
| `Passage N`, `Relevance N` | `level-four headings` | 每位标注者每个唯一配对出现一次。 |
| `Retrieved by:` | `text` | 全部真实算法来源。 |
| `Label:` | `blank, 0 or 1` | 初始空白，独立填写二元相关性。 |

### 历史 BM25 工作流

将 `data/raw/`、`data/processed/` 与两份指南一起提交，无需 GitHub Releases。保留来源许可声明、上游 revision、生成参数、评估范围及配套 manifest。Git 历史记录每次发布快照，使用精确提交复现指定版本。

在独立的本地暂存目录中重建变化的输出，保留标准文件名，同步重建依赖产物及 manifest。检查哈希与结构，并在两份指南中记录来源、参数、范围和变化后再提交。凭据、缓存、模型权重、索引及个人笔记不纳入共享快照。通过 `.gitattributes` 保留哈希绑定文件的原始字节。

### 获取数据

将 P3 工作分支克隆到新目录：

```powershell
git clone --branch p3-qasper-foundation https://github.com/CodeByVish/papergap-rag.git
Set-Location papergap-rag
git rev-parse HEAD
```

复现指定版本时，在干净工作区检出对应的精确提交。原始及处理后数据与 manifest 一起位于 `data/` 下，使用前验证哈希。不要单独修改 JSONL 而不重建对应 manifest 及依赖产物。本地复现使用下文各产物的命令，无需下载 Release 或解压数据包。

all-splits 映射属于机械生成的 gold 参考导出。使用下文保存的题单及使用审计确定资格；导出或下载全部划分不授权使用 held-out 题目选参。

## 目录结构与构建顺序

下列目录树列出标准产物；诊断报告为可选文件，可能不存在。`README_zh-CN.md`、`README.md` 与所列生成文件一起纳入 Git。

```text
data/
├── README.md                                           # English guide / 英文指南
├── README_zh-CN.md                                     # Chinese guide / 中文指南
├── raw/                                                # Tracked source data / 纳入 Git 的源数据
│   └── qasper/
│       ├── manifest.json                               # Source metadata and hashes / 来源及哈希
│       ├── train.jsonl
│       ├── validation.jsonl
│       └── test.jsonl
└── processed/                                          # Tracked generated outputs / 纳入 Git 的生成产物
    ├── papers.jsonl
    ├── qa.jsonl
    ├── qasper_export.manifest.json
    ├── passages.jsonl
    ├── passages.manifest.json
    ├── paper_catalog.json
    ├── passages_all_paper_text.jsonl
    ├── passages_all_paper_text.manifest.json
    ├── gold_evidence_mapping_all_splits.jsonl
    ├── gold_evidence_mapping_all_splits.manifest.json
    ├── qa_for_choosing_chunk_size.jsonl
    ├── annotation_preparation.manifest.json
    ├── qa_for_held_out.jsonl
    ├── qa_for_held_out.manifest.json
    ├── qa_for_held_out_v2.jsonl
    ├── qa_for_held_out_v2.manifest.json
    ├── historical_bm25_retirement.manifest.json
    ├── annotation_pilot/
    ├── annotation_held_out/
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

本地复现时，先按本指南相应命令生成 `papers.jsonl` 和所选 passage 语料，再执行目录构建命令。使用 Git 数据时，按上文获取 P3 快照，保留与目录匹配的语料；必要时在本地重建目录。路径只记录所选文件，不包含内容哈希；替换语料后必须重建目录。

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
| `source_split` | `string` | 官方来源划分；独立于评估角色保留。 |
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

## `data/processed/gold_evidence_mapping_all_splits.jsonl`

覆盖全部官方划分的全量 gold 参考映射。评估用途由独立题单及实际使用记录决定；文件覆盖范围本身不代表 held-out 已冻结或已失效。旧开发映射及其 manifest 已删除。

### 生成命令

```powershell
python -m scripts.export_evidence_mapping --scope all-splits-reference
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

all-splits 映射属于机械生成的 gold 参考导出。使用下文保存的题单及使用审计确定资格；导出或下载全部划分不授权使用 held-out 题目选参。

### 生成命令

```powershell
python -m scripts.export_evidence_mapping --scope all-splits-reference
```

### 字段表

| 字段名称 | JSON 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | gold-evidence-to-passage-v0-proposed。 |
| `split_policy_version` | `string` | 拟议划分策略版本。 |
| `source_splits` | `array<string>` | 选作证据映射的官方划分。 |
| `scope` | `string` | development 或 all-splits-reference；旧开发导出中可能缺失。 |
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

## 问题层面的 held-out 策略

Week 4 标注流程跨全部官方划分采用问题层面隔离，允许共享论文，并排除使用记录中的实验题。`src/data/split_policy.py` 的旧官方划分映射仍为早期选参实验的 `v0-proposed` 策略，不用于选择本次标注题单。不得将问答监督信息写入索引；检索仅接收论文正文和已保存的问题。本次候选池冻结不代表下游生成器或代理配置已冻结。

## 验证与参考快照

解压数据包或重建配套文件后，执行以下独立检查：

```powershell
python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages.jsonl --manifest data/processed/passages.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages_all_paper_text.jsonl --manifest data/processed/passages_all_paper_text.manifest.json
git check-ignore -v data/raw/qasper/manifest.json data/processed/papers.jsonl
```

语料检查器只需已发布的语料和 manifest，不需要原始/导出输入。构建器要求至少 $10{,}000$ 块、$100{,}000$ 原始词及足够的输出词。证据导出器检查论文/问答输入、哈希、语料范围及配置，重建块并验证精确 ID/文本后再映射。目前没有独立的证据映射检查 CLI；问答检查器不能替代映射验证。

下表为纳入 Git 的固定 $365/40$ 参考快照。产物变化时须更新配套 manifest。导出包含 $1{,}585$ 篇论文、$5{,}049$ 个问题及 $7{,}993$ 个答案标注；train、validation、test 分别有 $2{,}593$、$1{,}005$、$1{,}451$ 个问题。

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

## 历史 BM25 标注候选池复现与使用

本节及后续原 `qa_for_held_out` / `annotation_held_out` 字段表仅描述已停用的 BM25 版本。下方命令属于历史记录，停用标记会阻止旧版冻结/正式导出。当前题单使用上方独立 `v2` 命令复现；正式共同池检索已完成；新版标注导出仍待执行。

旧参数 `--scope all-splits-testing` 仍作为 `all-splits-reference` 的兼容别名，不再代表放弃 held-out 状态。可显式用 `--scope development` 生成独立命名的 `gold_evidence_mapping_development` 文件；本次数据包不保留该产物。排除 gold 映射中 $251$ 道已用题及 $1$ 道所属论文不足 $5$ 个块的题后，合格池有 $3{,}077$ 个 ID；另有 $2$ 个已用 ID 不在 gold 映射中。最终来源为 train $95$ 题、validation $40$ 题、test $65$ 题。

按下文顺序执行四个阶段：`prepare`、`pilot`、`freeze`、`export`。输入为已核验的 $365/40$ 全论文语料、all-splits gold 映射、原始导出、第 $4$ 轮保存题单及全部本地实验使用记录。拒绝覆盖已有输出。复现包须保留历史题单及审计记录，不得按种子重建历史题单。CLI 从仓库根目录运行，不读取 YAML 检索设置。

种子 $20261028$ 和规则在抽样前固定。不得查看 held-out 内容用于调试、选参或修改系统。本地审计排除了 $253$ 个已用 ID，其中 $3$ 个不在 $250$ 道选参题中；不能据此证明未记录的外部使用情况。核验产物包含 $200$ 题、$1{,}000$ 个唯一配对。两套空白 Markdown 对应未来 $2{,}000$ 次独立判断，目前尚未收集人工标签或计算一致率。评估期间保持本次候选池配置不变。

使用 Git 数据时，按上文获取 P3 快照，保留全部配套 manifest 和对应的语料、题单。本地复现先生成原始导出、全论文语料和 all-splits 参考映射，再恢复精确的历史实验产物，最后向未使用的路径运行四个阶段。`--data`、`--history`、`--pilot`、`--output` 用于选择位置；`--data` 内须保留标准输入文件名。再次构建前保存完整快照。分发时仅交付各自的 Markdown 批次；标注者不得查看仓库中的 JSONL 核验文件及 gold 参考。

## `data/processed/qa_for_choosing_chunk_size.jsonl`

从第 $4$ 轮实际保存的题单提取全部 $250$ 题，保持顺序及原文，不按种子重抽。

```powershell
python -m scripts.build_annotation_pool prepare
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `question_id` | `string` | 原始唯一问题 ID。 |
| `paper_id` | `string` | 原始论文 ID；允许共享论文。 |
| `question` | `string` | 原始问题文本，不改写。 |
| `source_split` | `string` | 官方来源划分，不代表评估角色。 |

## `data/processed/annotation_preparation.manifest.json`

准备阶段的来源及使用审计；包含已无效化实验。

```powershell
python -m scripts.build_annotation_pool prepare
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed。 |
| `inputs` | `object<string,string>` | 输入路径到精确 SHA-256 的映射。 |
| `inputs.<path>` | `string` | 该输入文件的字节哈希。 |
| `settings` | `object` | 冻结的语料及检索配置。 |
| `settings.chunk_size_words` | `integer` | $365$ 词。 |
| `settings.chunk_overlap_words` | `integer` | $40$ 词。 |
| `settings.top_k` | `integer` | 每题 $5$ 个不同块。 |
| `usage_audit` | `array<object>` | 全部已保存的本地 results manifest 及题单。 |
| `usage_audit[].file` | `string` | 审计文件路径。 |
| `usage_audit[].sha256` | `string` | 审计文件哈希。 |
| `usage_audit[].question_ids` | `array<string>` | 该次运行已使用的问题 ID。 |
| `excluded_question_ids` | `array<string>` | 已用题与选参题的 ID 并集。 |
| `audit_scope` | `string` | 仅覆盖本地已保存记录；未知外部未记录使用。 |
| `seed` | `integer` | 预先确定的 $20261028$。 |
| `sampling_rule` | `string` | 排序 ID 后按种子无放回简单随机抽样，保留抽取顺序。 |
| `scope` | `array<string>` | 全部三个官方划分。 |
| `isolation` | `string` | 问题层面隔离，允许共享论文。 |

## `data/processed/qa_for_held_out.jsonl`

开发试运行通过后保存的 $200$ 题；正式导出必须使用此文件，不得重新抽题。

```powershell
python -m scripts.build_annotation_pool freeze
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `question_id` | `string` | 原始唯一问题 ID。 |
| `paper_id` | `string` | 原始论文 ID；允许共享论文。 |
| `question` | `string` | 原始问题文本，不改写。 |
| `source_split` | `string` | 官方来源划分，不代表评估角色。 |

## `data/processed/qa_for_held_out.manifest.json`

冻结题单及配置，不代表未来生成器、代理或提示词已冻结。

```powershell
python -m scripts.build_annotation_pool freeze
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed。 |
| `purpose` | `string` | held-out 题单。 |
| `inputs` | `object<string,string>` | 输入路径到精确 SHA-256 的映射。 |
| `inputs.<path>` | `string` | 该输入文件的字节哈希。 |
| `settings` | `object` | 冻结的语料及检索配置。 |
| `settings.chunk_size_words` | `integer` | $365$ 词。 |
| `settings.chunk_overlap_words` | `integer` | $40$ 词。 |
| `settings.top_k` | `integer` | 每题 $5$ 个不同块。 |
| `code` | `object` | 包含未提交修改的代码身份。 |
| `code.commit` | `string` | 执行时的 Git HEAD。 |
| `code.python` | `string` | Python 运行时版本。 |
| `code.working_tree_status` | `array<string>` | Git 简短状态；运行可能使用未提交代码。 |
| `code.source_sha256` | `object<string,string>` | 全部 src/scripts Python 文件的精确哈希。 |
| `code.source_sha256.<path>` | `string` | 源码字节 SHA-256，导出时复核。 |
| `retriever` | `object` | 现有 P1/P2 适配器返回的元数据。 |
| `retriever.id` | `string` | p1-p2-static-retrieval 适配器。 |
| `retriever.mode` | `string` | bm25。 |
| `retriever.source_commit` | `string` | 上游适配器集成提交；实际代码另由 code 标识。 |
| `retriever.packages` | `object<string,string or null>` | 实际使用的包版本。 |
| `retriever.packages.<package>` | `string or null` | 安装的包版本；不可用时为 null。 |
| `retriever.scope` | `string` | 仅检索所属论文。 |
| `retriever.persistent_score_cache` | `boolean` | false，不使用持久化分数缓存。 |
| `retriever.score` | `string` | 原始 BM25 分数。 |
| `retriever.tie_break` | `string` | 上游稳定排序规则。 |
| `retriever.bm25` | `object` | 启用的稀疏检索设置。 |
| `retriever.bm25.enabled` | `boolean` | true。 |
| `retriever.bm25.tokenizer` | `string` | casefold 与 Unicode 词序列。 |
| `retriever.bm25.k1` | `number` | $1.5$。 |
| `retriever.bm25.b` | `number` | $0.75$。 |
| `retriever.bm25.epsilon` | `number` | $0.25$。 |
| `retriever.dense` | `object` | 禁用的稠密检索组件。 |
| `retriever.dense.enabled` | `boolean` | false，不使用稠密检索。 |
| `retriever.reranker` | `object` | 禁用的重排组件。 |
| `retriever.reranker.enabled` | `boolean` | false，不使用重排。 |
| `seed` | `integer` | $20261028$。 |
| `sampling_rule` | `string` | 预先确定的抽样规则。 |
| `scope` | `array<string>` | train、validation、test。 |
| `isolation` | `string` | 问题层面隔离，允许共享论文。 |
| `eligible_question_ids` | `array<string>` | 抽样前排序的合格题 ID；论文至少有 $5$ 个块。 |
| `excluded` | `object<string,string>` | gold 映射题 ID 到排除原因的映射。 |
| `excluded.<question_id>` | `string` | 已使用或所属论文不足 $5$ 个块。 |
| `prior_usage_excluded_question_ids` | `array<string>` | 全部已用 ID，即使不在 gold 映射中。 |
| `question_ids` | `array<string>` | 最终题单及顺序。 |
| `source_split_counts` | `object<string,integer>` | 按官方划分统计的抽样题数。 |
| `source_split_counts.<split>` | `integer` | 该划分入选的问题数。 |
| `usage_boundary` | `string` | 禁止根据 held-out 监督或结果选参、开发。 |

## `data/processed/annotation_pilot/pairs.jsonl`

仅用前 $5$ 道选参题，共 $25$ 对。 JSONL 为结构化源；内部 ID 仅用于关联。

```powershell
python -m scripts.build_annotation_pool pilot
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 稳定的全局编号；正式池为 $1$ 至 $1{,}000$。 |
| `question_id` | `string` | 原始唯一问题 ID。 |
| `paper_id` | `string` | 原始论文 ID；允许共享论文。 |
| `question` | `string` | 原始问题文本，不改写。 |
| `passage_id` | `string` | 语料中的精确块 ID。 |
| `paper_title` | `string` | 真实完整论文标题。 |
| `passage` | `string` | 检索块完整原文。 |
| `label` | `null or integer` | 初始为 null；后续人工 $0/1$ 标签须按稳定编号及标注者关联。 |

## `data/processed/annotation_pilot/verification.jsonl`

仅供核验，不得分发给标注者。

```powershell
python -m scripts.build_annotation_pool pilot
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 稳定的全局编号；正式池为 $1$ 至 $1{,}000$。 |
| `question_id` | `string` | 原始唯一问题 ID。 |
| `paper_id` | `string` | 原始论文 ID；允许共享论文。 |
| `question` | `string` | 原始问题文本，不改写。 |
| `passage_id` | `string` | 语料中的精确块 ID。 |
| `paper_title` | `string` | 真实完整论文标题。 |
| `passage` | `string` | 检索块完整原文。 |
| `label` | `null or integer` | 初始为 null；后续人工 $0/1$ 标签须按稳定编号及标注者关联。 |
| `retrieval_method` | `string` | bm25，仅核验文件保留。 |
| `rank` | `integer` | 从 $1$ 开始的原始检索排名。 |
| `score` | `number` | 原始检索分数。 |
| `gold_passage_ids` | `array<string>` | 与参考证据重叠的块 ID，不是人工标签。 |
| `gold_evidence_match` | `boolean` | 该块是否与映射的 gold 段落重叠。 |
| `evidence_paragraphs` | `array<object>` | 检索后关联的参考证据。 |
| `evidence_paragraphs[].location` | `string` | 原始证据段落坐标。 |
| `evidence_paragraphs[].section_index` | `integer` | 原始章节索引，从零开始。 |
| `evidence_paragraphs[].paragraph_index` | `integer` | 原始段落索引，从零开始。 |
| `evidence_paragraphs[].text` | `string` | 参考段落正文。 |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | 块并集覆盖全部非空白字符。 |
| `evidence_paragraphs[].passage_matches` | `array<object>` | 存在重叠的语料块。 |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | 精确匹配的块 ID。 |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | 左闭右开的字符区间 [start,end)。 |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | 单块是否覆盖完整段落。 |

## `data/processed/annotation_pilot/manifest.json`

记录精确输入、代码、配置及全部输出哈希。

```powershell
python -m scripts.build_annotation_pool pilot
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed。 |
| `purpose` | `string` | 开发试运行或 held-out 标注候选池。 |
| `question_count` | `integer` | 试运行 $5$ 题；正式 $200$ 题。 |
| `pair_count` | `integer` | 试运行 $25$ 对；正式 $1{,}000$ 对。 |
| `question_ids` | `array<string>` | 已保存的问题顺序。 |
| `inputs` | `object<string,string>` | 输入路径到精确 SHA-256 的映射。 |
| `inputs.<path>` | `string` | 该输入文件的字节哈希。 |
| `settings` | `object` | 冻结的语料及检索配置。 |
| `settings.chunk_size_words` | `integer` | $365$ 词。 |
| `settings.chunk_overlap_words` | `integer` | $40$ 词。 |
| `settings.top_k` | `integer` | 每题 $5$ 个不同块。 |
| `code` | `object` | 包含未提交修改的代码身份。 |
| `code.commit` | `string` | 执行时的 Git HEAD。 |
| `code.python` | `string` | Python 运行时版本。 |
| `code.working_tree_status` | `array<string>` | Git 简短状态；运行可能使用未提交代码。 |
| `code.source_sha256` | `object<string,string>` | 全部 src/scripts Python 文件的精确哈希。 |
| `code.source_sha256.<path>` | `string` | 源码字节 SHA-256，导出时复核。 |
| `retriever` | `object` | 现有 P1/P2 适配器返回的元数据。 |
| `retriever.id` | `string` | p1-p2-static-retrieval 适配器。 |
| `retriever.mode` | `string` | bm25。 |
| `retriever.source_commit` | `string` | 上游适配器集成提交；实际代码另由 code 标识。 |
| `retriever.packages` | `object<string,string or null>` | 实际使用的包版本。 |
| `retriever.packages.<package>` | `string or null` | 安装的包版本；不可用时为 null。 |
| `retriever.scope` | `string` | 仅检索所属论文。 |
| `retriever.persistent_score_cache` | `boolean` | false，不使用持久化分数缓存。 |
| `retriever.score` | `string` | 原始 BM25 分数。 |
| `retriever.tie_break` | `string` | 上游稳定排序规则。 |
| `retriever.bm25` | `object` | 启用的稀疏检索设置。 |
| `retriever.bm25.enabled` | `boolean` | true。 |
| `retriever.bm25.tokenizer` | `string` | casefold 与 Unicode 词序列。 |
| `retriever.bm25.k1` | `number` | $1.5$。 |
| `retriever.bm25.b` | `number` | $0.75$。 |
| `retriever.bm25.epsilon` | `number` | $0.25$。 |
| `retriever.dense` | `object` | 禁用的稠密检索组件。 |
| `retriever.dense.enabled` | `boolean` | false，不使用稠密检索。 |
| `retriever.reranker` | `object` | 禁用的重排组件。 |
| `retriever.reranker.enabled` | `boolean` | false，不使用重排。 |
| `freeze_manifest_sha256` | `string or null` | held-out 冻结 manifest 哈希；试运行时为 null。 |
| `outputs` | `object<string,string>` | 输出路径到 SHA-256 的映射，不含 manifest 自身。 |
| `outputs.<path>` | `string` | 输出字节哈希，包含盲审 Markdown。 |
| `validation` | `string` | 已完成的不变量核验。 |

## `data/processed/annotation_pilot/annotator_A/ and annotator_B/`

两套独立英文 Markdown 视图；正式每套 $10$ 批，每批 $20$ 题、$100$ 对。无 HTML、备注栏、内部 ID、gold、检索方法或分数。每条记录的两份视图须交给不同的人。

```powershell
python -m scripts.build_annotation_pool pilot
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `Annotator:` | `text` | 回收前填写真实标注者标识。 |
| `Record NNNN` | `heading` | 对应全局 record_number，不得修改。 |
| `Paper:` | `text` | 真实完整标题，不显示内部 ID。 |
| `Question / Passage` | `quoted text` | 原始内容，不得修改。 |
| `Relevance / Label:` | `blank, 0 or 1` | 仅填写 Label: 0 或 Label: 1，保留全部编号。 |

## `data/processed/annotation_held_out/pairs.jsonl`

正式 $200$ 题、$1{,}000$ 对；同题 $5$ 对相邻，顺序固定。 JSONL 为结构化源；内部 ID 仅用于关联。

```powershell
python -m scripts.build_annotation_pool export
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 稳定的全局编号；正式池为 $1$ 至 $1{,}000$。 |
| `question_id` | `string` | 原始唯一问题 ID。 |
| `paper_id` | `string` | 原始论文 ID；允许共享论文。 |
| `question` | `string` | 原始问题文本，不改写。 |
| `passage_id` | `string` | 语料中的精确块 ID。 |
| `paper_title` | `string` | 真实完整论文标题。 |
| `passage` | `string` | 检索块完整原文。 |
| `label` | `null or integer` | 初始为 null；后续人工 $0/1$ 标签须按稳定编号及标注者关联。 |

## `data/processed/annotation_held_out/verification.jsonl`

仅供核验，不得分发给标注者。

```powershell
python -m scripts.build_annotation_pool export
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 稳定的全局编号；正式池为 $1$ 至 $1{,}000$。 |
| `question_id` | `string` | 原始唯一问题 ID。 |
| `paper_id` | `string` | 原始论文 ID；允许共享论文。 |
| `question` | `string` | 原始问题文本，不改写。 |
| `passage_id` | `string` | 语料中的精确块 ID。 |
| `paper_title` | `string` | 真实完整论文标题。 |
| `passage` | `string` | 检索块完整原文。 |
| `label` | `null or integer` | 初始为 null；后续人工 $0/1$ 标签须按稳定编号及标注者关联。 |
| `retrieval_method` | `string` | bm25，仅核验文件保留。 |
| `rank` | `integer` | 从 $1$ 开始的原始检索排名。 |
| `score` | `number` | 原始检索分数。 |
| `gold_passage_ids` | `array<string>` | 与参考证据重叠的块 ID，不是人工标签。 |
| `gold_evidence_match` | `boolean` | 该块是否与映射的 gold 段落重叠。 |
| `evidence_paragraphs` | `array<object>` | 检索后关联的参考证据。 |
| `evidence_paragraphs[].location` | `string` | 原始证据段落坐标。 |
| `evidence_paragraphs[].section_index` | `integer` | 原始章节索引，从零开始。 |
| `evidence_paragraphs[].paragraph_index` | `integer` | 原始段落索引，从零开始。 |
| `evidence_paragraphs[].text` | `string` | 参考段落正文。 |
| `evidence_paragraphs[].fully_covered_by_passage_union` | `boolean` | 块并集覆盖全部非空白字符。 |
| `evidence_paragraphs[].passage_matches` | `array<object>` | 存在重叠的语料块。 |
| `evidence_paragraphs[].passage_matches[].passage_id` | `string` | 精确匹配的块 ID。 |
| `evidence_paragraphs[].passage_matches[].source_char_span` | `array<integer>` | 左闭右开的字符区间 [start,end)。 |
| `evidence_paragraphs[].passage_matches[].covers_full_paragraph` | `boolean` | 单块是否覆盖完整段落。 |

## `data/processed/annotation_held_out/manifest.json`

记录精确输入、代码、配置及全部输出哈希。

```powershell
python -m scripts.build_annotation_pool export
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed。 |
| `purpose` | `string` | 开发试运行或 held-out 标注候选池。 |
| `question_count` | `integer` | 试运行 $5$ 题；正式 $200$ 题。 |
| `pair_count` | `integer` | 试运行 $25$ 对；正式 $1{,}000$ 对。 |
| `question_ids` | `array<string>` | 已保存的问题顺序。 |
| `inputs` | `object<string,string>` | 输入路径到精确 SHA-256 的映射。 |
| `inputs.<path>` | `string` | 该输入文件的字节哈希。 |
| `settings` | `object` | 冻结的语料及检索配置。 |
| `settings.chunk_size_words` | `integer` | $365$ 词。 |
| `settings.chunk_overlap_words` | `integer` | $40$ 词。 |
| `settings.top_k` | `integer` | 每题 $5$ 个不同块。 |
| `code` | `object` | 包含未提交修改的代码身份。 |
| `code.commit` | `string` | 执行时的 Git HEAD。 |
| `code.python` | `string` | Python 运行时版本。 |
| `code.working_tree_status` | `array<string>` | Git 简短状态；运行可能使用未提交代码。 |
| `code.source_sha256` | `object<string,string>` | 全部 src/scripts Python 文件的精确哈希。 |
| `code.source_sha256.<path>` | `string` | 源码字节 SHA-256，导出时复核。 |
| `retriever` | `object` | 现有 P1/P2 适配器返回的元数据。 |
| `retriever.id` | `string` | p1-p2-static-retrieval 适配器。 |
| `retriever.mode` | `string` | bm25。 |
| `retriever.source_commit` | `string` | 上游适配器集成提交；实际代码另由 code 标识。 |
| `retriever.packages` | `object<string,string or null>` | 实际使用的包版本。 |
| `retriever.packages.<package>` | `string or null` | 安装的包版本；不可用时为 null。 |
| `retriever.scope` | `string` | 仅检索所属论文。 |
| `retriever.persistent_score_cache` | `boolean` | false，不使用持久化分数缓存。 |
| `retriever.score` | `string` | 原始 BM25 分数。 |
| `retriever.tie_break` | `string` | 上游稳定排序规则。 |
| `retriever.bm25` | `object` | 启用的稀疏检索设置。 |
| `retriever.bm25.enabled` | `boolean` | true。 |
| `retriever.bm25.tokenizer` | `string` | casefold 与 Unicode 词序列。 |
| `retriever.bm25.k1` | `number` | $1.5$。 |
| `retriever.bm25.b` | `number` | $0.75$。 |
| `retriever.bm25.epsilon` | `number` | $0.25$。 |
| `retriever.dense` | `object` | 禁用的稠密检索组件。 |
| `retriever.dense.enabled` | `boolean` | false，不使用稠密检索。 |
| `retriever.reranker` | `object` | 禁用的重排组件。 |
| `retriever.reranker.enabled` | `boolean` | false，不使用重排。 |
| `freeze_manifest_sha256` | `string or null` | held-out 冻结 manifest 哈希；试运行时为 null。 |
| `outputs` | `object<string,string>` | 输出路径到 SHA-256 的映射，不含 manifest 自身。 |
| `outputs.<path>` | `string` | 输出字节哈希，包含盲审 Markdown。 |
| `validation` | `string` | 已完成的不变量核验。 |

## `data/processed/annotation_held_out/annotator_A/ and annotator_B/`

两套独立英文 Markdown 视图；正式每套 $10$ 批，每批 $20$ 题、$100$ 对。无 HTML、备注栏、内部 ID、gold、检索方法或分数。每条记录的两份视图须交给不同的人。

```powershell
python -m scripts.build_annotation_pool export
```

| 字段名称 | 类型 | 含义 |
| --- | --- | --- |
| `Annotator:` | `text` | 回收前填写真实标注者标识。 |
| `Record NNNN` | `heading` | 对应全局 record_number，不得修改。 |
| `Paper:` | `text` | 真实完整标题，不显示内部 ID。 |
| `Question / Passage` | `quoted text` | 原始内容，不得修改。 |
| `Relevance / Label:` | `blank, 0 or 1` | 仅填写 Label: 0 或 Label: 1，保留全部编号。 |
