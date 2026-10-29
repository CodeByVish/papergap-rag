# QASPER 数据指南

[English](README.md)

原始数据、处理后数据及 manifest 纳入 P3 工作分支 `p3-qasper-foundation`。本指南说明 Git 共享方式、本地复现流程及每份处理后文件的字段。所有命令均从仓库根目录、使用项目 Python 3.11 环境运行；先安装 `requirements.txt` 或 `requirements-dev.txt`。

## 数据版本与更新

第 $4$ 周第 $3$ 步已完成。`data/processed/annotation_common_v3/` 保存 BM25、Dense、Hybrid RRF、Hybrid RRF followed by BGE reranking 在原冻结 $200$ 题上的全新检索：每算法 $1000$ 次命中，$800$ 行排名，共 $1853$ 条唯一配对，每题 $6$–$14$ 条。原三算法的 $600$ 组 passage ID 及排名与 v2 完全一致，分数也全部一致。`data/processed/annotation_common_v3_markdown/` 保存两套独立空白英文标注文件，每套 $10$ 批、每批 $20$ 道完整问题，各批配对数为 $179,185,187,188,174,187,190,191,177,195$。第 $4$ 步仅使用此核验通过的四算法版本，安排两位不同人员独立完成 $3706$ 次初始判断；人工标签、一致率及裁决待执行。v2 共同池和模板字节不变，作为历史版本保留。

本次范围内的禁用清单将 P1 的 $2593$、P2 的 $106$ 和 P3 的 $250$ 道选参题合并为 $2654$ 道唯一禁用题，保留全部符合排除条件的重复来源。不声称覆盖未记录的外部/P4–P6 用题。采用问题层面隔离，允许共享论文。后续明确新增的用题证据须在再次抽样前补充新清单版本；禁止根据 held-out 内容或结果选择系统配置。

第四算法先在前 $5$ 道已保存开发题上验证，得到 $45$ 条配对，再在正式运行前通过 `configs/annotation_four.json` 和 `annotation_pilot_four_v3/frozen_config.json` 冻结。BGE reranker base revision 为 `2cfc18c9415c912f9d8155881c133215df768a70`，CPU、批大小 $8$、问题与 passage 对按 longest-first 截断至 $512$ token，使用原始 logit，同分按 RRF 降序、passage ID 升序。对 BM25 top-$20$ 和 Dense top-$20$ 的完整融合并集评分后取最终 top-$5$；等权 RRF $k=60$ 及原三算法配置不变。未使用 held-out 调参或重新抽题。

清理提交 `685a08c` 删除了旧 pilot/BM25 文件，但现有 manifest 仍要求其哈希。核验现优先读取当前文件，仅对缺失的历史标注文件读取本地 Git blob，核对原 SHA-256，不恢复已删除的工作文件；复现须保留完整 Git 历史。共同池核验器直接检查冻结题单及输入哈希、原文与顺序、禁用交集和论文资格，不重新抽题；旧 freeze 重建命令仍需要旧工作文件。

新缓存先联网准备以下固定模型文件，只保留 safetensors 权重、配置和 tokenizer，避免重复下载其他权重格式；后续运行离线加载。

```powershell
python -c "from huggingface_hub import snapshot_download; snapshot_download('BAAI/bge-small-en-v1.5', revision='5c38ec7c405ec4b44b94cc5a9bb96e735b38267a', cache_dir='.cache/huggingface', allow_patterns=['*.json', '*.safetensors', 'vocab.txt'])"
python -c "from huggingface_hub import snapshot_download; snapshot_download('BAAI/bge-reranker-base', revision='2cfc18c9415c912f9d8155881c133215df768a70', cache_dir='.cache/huggingface', allow_patterns=['*.json', '*.safetensors', 'sentencepiece.bpe.model'])"
```

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
python -m src.data.export_common_annotations run --pool data/processed/annotation_common_v3 --output data/processed/annotation_common_v3_markdown
python -m src.data.export_common_annotations verify --pool data/processed/annotation_common_v3 --output data/processed/annotation_common_v3_markdown
```

本地复现时将正式池输出改为 `--output tmp/tmp_annotation_common_v3`，导出使用对应 `--pool` 和 `--output tmp/tmp_annotation_common_v3_markdown`；开发复现使用 `--output tmp/tmp_annotation_pilot_four_v3`。拒绝已有目录。数据及 manifest 随 GitHub `p3` 工作分支获取。模型仅放在忽略的 `.cache/huggingface/`。下方 v2 章节仅说明历史产物，禁止将其用于第 $4$ 步。

## `data/processed/annotation_common_v3/questions.jsonl`

生成及核验命令：

```powershell
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id, paper_id` | `string` | 原始问题及论文 ID，保持保存顺序。 |
| `question` | `string` | 问题原文。 |
| `source_split` | `string` | 官方来源 split，不表示评估用途。 |

## `data/processed/annotation_pilot_four_v3/questions.jsonl`

字段及类型沿用本指南上方 `questions.jsonl` 表。仅使用前 $5$ 道已保存开发题、$5$ 篇论文、$70$ 条 passage；得到 $45$ 条唯一配对、$20$ 行排名、每算法 $25$ 次命中。`pilot=true`，历史映射与对比为空，开发模式不读取 held-out 题单或 gold。

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool verify --four --output data/processed/annotation_pilot_four_v3
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id, paper_id` | `string` | 与上方对应正式产物字段约束相同。 |
| `question` | `string` | 与上方对应正式产物字段约束相同。 |
| `source_split` | `string` | 与上方对应正式产物字段约束相同。 |

## `data/processed/annotation_common_v3/pairs.jsonl`

生成及核验命令：

```powershell
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 本版本内首次遇见顺序生成的稳定编号。 |
| `question_id, paper_id, passage_id` | `string` | 唯一问题与 passage 配对及论文范围。 |
| `source_split, question, paper_title, passage` | `string` | 来源 split、问题原文、真实标题和完整正文。 |
| `label` | `null` | 初始为空，命中该配对的算法共用最终标签。 |
| `retrieved_by[]` | `string` | 按冻结算法顺序保存全部真实来源。 |
| `retrievals[]` | `object` | 每个来源对应一条原始命中关系。 |
| `retrievals[].method` | `string` | 四算法之一的冻结名称。 |
| `retrievals[].rank` | `integer` | 算法原始排名 1 至 5。 |
| `retrievals[].score` | `number` | 有限的 BM25、余弦、RRF 或 BGE 原始 logit。 |
| `display_group` | `string` | 至少两算法命中归入 Common Retrieved Chunks，否则归入唯一来源。 |

## `data/processed/annotation_pilot_four_v3/pairs.jsonl`

字段及类型沿用本指南上方 `pairs.jsonl` 表。仅使用前 $5$ 道已保存开发题、$5$ 篇论文、$70$ 条 passage；得到 $45$ 条唯一配对、$20$ 行排名、每算法 $25$ 次命中。`pilot=true`，历史映射与对比为空，开发模式不读取 held-out 题单或 gold。

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool verify --four --output data/processed/annotation_pilot_four_v3
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `record_number` | `integer` | 与上方对应正式产物字段约束相同。 |
| `question_id, paper_id, passage_id` | `string` | 与上方对应正式产物字段约束相同。 |
| `source_split, question, paper_title, passage` | `string` | 与上方对应正式产物字段约束相同。 |
| `label` | `null` | 与上方对应正式产物字段约束相同。 |
| `retrieved_by[]` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrievals[]` | `object` | 与上方对应正式产物字段约束相同。 |
| `retrievals[].method` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrievals[].rank` | `integer` | 与上方对应正式产物字段约束相同。 |
| `retrievals[].score` | `number` | 与上方对应正式产物字段约束相同。 |
| `display_group` | `string` | 与上方对应正式产物字段约束相同。 |

## `data/processed/annotation_common_v3/rankings.jsonl`

生成及核验命令：

```powershell
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id, method` | `string` | 每道题、每算法一行。 |
| `hits[]` | `object` | 按原始排名保存五条不同且有效的同论文命中。 |
| `hits[].passage_id` | `string` | 语料中的 passage ID。 |
| `hits[].record_number` | `integer` | 指向唯一配对的编号。 |
| `hits[].rank` | `integer` | 算法原始排名 1 至 5。 |
| `hits[].score` | `number` | 未经修改的算法有限原始分数。 |

## `data/processed/annotation_pilot_four_v3/rankings.jsonl`

字段及类型沿用本指南上方 `rankings.jsonl` 表。仅使用前 $5$ 道已保存开发题、$5$ 篇论文、$70$ 条 passage；得到 $45$ 条唯一配对、$20$ 行排名、每算法 $25$ 次命中。`pilot=true`，历史映射与对比为空，开发模式不读取 held-out 题单或 gold。

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool verify --four --output data/processed/annotation_pilot_four_v3
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id, method` | `string` | 与上方对应正式产物字段约束相同。 |
| `hits[]` | `object` | 与上方对应正式产物字段约束相同。 |
| `hits[].passage_id` | `string` | 与上方对应正式产物字段约束相同。 |
| `hits[].record_number` | `integer` | 与上方对应正式产物字段约束相同。 |
| `hits[].rank` | `integer` | 与上方对应正式产物字段约束相同。 |
| `hits[].score` | `number` | 与上方对应正式产物字段约束相同。 |

## `data/processed/annotation_common_v3/frozen_config.json`

生成及核验命令：

```powershell
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | v0-proposed，待团队确认。 |
| `chunk_size_words, chunk_overlap_words, top_k` | `integer` | $365$、$40$ 和 $5$。 |
| `methods[]` | `string` | BM25、Dense、Hybrid RRF、Hybrid RRF followed by BGE reranking。 |
| `scope, candidate_policy, record_order` | `string` | 问题原文、论文范围、完整融合并集和原始排名首次遇见编号。 |
| `retrieval.mode` | `string` | hybrid_rerank，四算法复用归一化配置。 |
| `retrieval.candidate_k, retrieval.rrf_k` | `integer` | 每来源至多 $20$ 条，等权 RRF 的 $k=60$。 |
| `retrieval.dense.revision` | `string` | BGE small English v1.5 固定为 5c38ec7c405ec4b44b94cc5a9bb96e735b38267a。 |
| `retrieval.reranker.revision` | `string` | BGE reranker base 固定为 2cfc18c9415c912f9d8155881c133215df768a70。 |
| `retrieval.dense.device, retrieval.reranker.device` | `string` | 两个模型均使用 cpu。 |
| `retrieval.dense.batch_size, retrieval.reranker.batch_size` | `integer` | 分别为 $32$ 和 $8$。 |
| `retrieval.reranker.max_length` | `integer` | 问题与 passage 对合计至多 $512$ token。 |
| `retrieval.dense.cache_folder, retrieval.reranker.cache_folder` | `string` | 解析后的已忽略 .cache/huggingface 路径。 |
| `retrieval.dense.local_files_only, retrieval.reranker.local_files_only` | `boolean` | 均为 true，运行前准备固定模型文件。 |
| `execution.HF_HUB_OFFLINE` | `string` | 模型导入前设为 1，CLI 在 finally 中恢复。 |
| `execution.persistent_score_cache` | `boolean` | false，重新执行模型评分。 |
| `reranker_inference.model_name, reranker_inference.truncation, reranker_inference.score, reranker_inference.tie_break` | `string` | BAAI/bge-reranker-base；longest-first 截断；float32 原始 logit；依次按 logit 降序、RRF 降序、passage ID 升序。 |
| `reranker_inference.padding` | `boolean` | true，按推理批次填充。 |
| `retrievers.<method>` | `object` | 完整嵌套字段沿用下方 v2 frozen-config 章节的 retrievers 表，组件开关按实际算法设置。 |
| `retrievers.<method>.reranker.revision, .device, .cache_folder, .model_name, .tokenizer_revision, .length_limit, .truncation_observation` | `string` | 第四算法的模型与 tokenizer revision、设备、缓存、成对长度约束和观察限制；元数据不声称实测截断。 |
| `retrievers.<method>.reranker.batch_size, .max_length` | `integer` | 第四算法实际使用 $8$ 和 $512$。 |
| `retrievers.<method>.reranker.local_files_only, .enabled, .padding, .truncation, .raw_logits` | `boolean` | 第四算法启用的重排配置均为 true。 |
| `retrievers.<method>.candidate_k_per_source, .rrf_k, .final_top_k` | `integer` | 两个 Hybrid 版本均为 $20$、$60$、$5$。 |
| `retrievers.<method>.rerank_all_fused_candidates` | `boolean` | 仅第四算法为 true，评分前不截取 top-5。 |

## `data/processed/annotation_pilot_four_v3/frozen_config.json`

字段及类型沿用本指南上方 `frozen_config.json` 表。仅使用前 $5$ 道已保存开发题、$5$ 篇论文、$70$ 条 passage；得到 $45$ 条唯一配对、$20$ 行排名、每算法 $25$ 次命中。`pilot=true`，历史映射与对比为空，开发模式不读取 held-out 题单或 gold。

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool verify --four --output data/processed/annotation_pilot_four_v3
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `string` | 与上方对应正式产物字段约束相同。 |
| `chunk_size_words, chunk_overlap_words, top_k` | `integer` | 与上方对应正式产物字段约束相同。 |
| `methods[]` | `string` | 与上方对应正式产物字段约束相同。 |
| `scope, candidate_policy, record_order` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrieval.mode` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrieval.candidate_k, retrieval.rrf_k` | `integer` | 与上方对应正式产物字段约束相同。 |
| `retrieval.dense.revision` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrieval.reranker.revision` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrieval.dense.device, retrieval.reranker.device` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrieval.dense.batch_size, retrieval.reranker.batch_size` | `integer` | 与上方对应正式产物字段约束相同。 |
| `retrieval.reranker.max_length` | `integer` | 与上方对应正式产物字段约束相同。 |
| `retrieval.dense.cache_folder, retrieval.reranker.cache_folder` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrieval.dense.local_files_only, retrieval.reranker.local_files_only` | `boolean` | 与上方对应正式产物字段约束相同。 |
| `execution.HF_HUB_OFFLINE` | `string` | 与上方对应正式产物字段约束相同。 |
| `execution.persistent_score_cache` | `boolean` | 与上方对应正式产物字段约束相同。 |
| `reranker_inference.model_name, reranker_inference.truncation, reranker_inference.score, reranker_inference.tie_break` | `string` | 与上方对应正式产物字段约束相同。 |
| `reranker_inference.padding` | `boolean` | 与上方对应正式产物字段约束相同。 |
| `retrievers.<method>` | `object` | 与上方对应正式产物字段约束相同。 |
| `retrievers.<method>.reranker.revision, .device, .cache_folder, .model_name, .tokenizer_revision, .length_limit, .truncation_observation` | `string` | 与上方对应正式产物字段约束相同。 |
| `retrievers.<method>.reranker.batch_size, .max_length` | `integer` | 与上方对应正式产物字段约束相同。 |
| `retrievers.<method>.reranker.local_files_only, .enabled, .padding, .truncation, .raw_logits` | `boolean` | 与上方对应正式产物字段约束相同。 |
| `retrievers.<method>.candidate_k_per_source, .rrf_k, .final_top_k` | `integer` | 与上方对应正式产物字段约束相同。 |
| `retrievers.<method>.rerank_all_fused_candidates` | `boolean` | 与上方对应正式产物字段约束相同。 |

## `data/processed/annotation_common_v3/run_inputs.json`

生成及核验命令：

```powershell
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `inputs.<path>` | `string` | 运行前输入 SHA-256，包括语料、题单、禁用清单和冻结配置。 |
| `code.commit, code.python` | `string` | 运行前 Git HEAD 和 Python 版本。 |
| `code.working_tree_status[]` | `string` | 运行前短状态，包含未提交修改。 |
| `code.source_sha256.<path>` | `string` | 保存结果前再次核验的 src/scripts 源码哈希。 |
| `history.<path>` | `string` | 未变的 v2 共同池、模板及历史 BM25 哈希；开发模式为空。 |

## `data/processed/annotation_pilot_four_v3/run_inputs.json`

字段及类型沿用本指南上方 `run_inputs.json` 表。仅使用前 $5$ 道已保存开发题、$5$ 篇论文、$70$ 条 passage；得到 $45$ 条唯一配对、$20$ 行排名、每算法 $25$ 次命中。`pilot=true`，历史映射与对比为空，开发模式不读取 held-out 题单或 gold。

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool verify --four --output data/processed/annotation_pilot_four_v3
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `inputs.<path>` | `string` | 与上方对应正式产物字段约束相同。 |
| `code.commit, code.python` | `string` | 与上方对应正式产物字段约束相同。 |
| `code.working_tree_status[]` | `string` | 与上方对应正式产物字段约束相同。 |
| `code.source_sha256.<path>` | `string` | 与上方对应正式产物字段约束相同。 |
| `history.<path>` | `string` | 与上方对应正式产物字段约束相同。 |

## `data/processed/annotation_common_v3/manifest.json`

生成及核验命令：

```powershell
python -m src.data.build_common_pool run --four
python -m src.data.build_common_pool verify --four
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version, purpose, reason, usage_boundary` | `string` | 暂定结构、运行用途、重建原因及 held-out 与空标签边界。 |
| `pilot` | `boolean` | 仅开发试运行为 true。 |
| `settings` | `object` | 与 frozen_config.json 完全相同，嵌套字段见上表。 |
| `inputs.<path>, outputs.<path>, historical_retained_files.<path>` | `string` | 输入、输出和历史 SHA-256；优先当前字节，已删除旧产物使用本地 Git 历史核对。 |
| `code` | `object` | 嵌套身份字段与 run_inputs.json 相同。 |
| `historical_comparison.rankings_compared, .identical_id_rank_lists, .identical_score_lists` | `integer` | 正式运行对比原三算法 $600$ 组排名；另报分数一致数；开发模式为空对象。 |
| `indexed_passage_count, indexed_paper_count` | `integer` | 所选论文完整索引的 passage 数和论文数。 |
| `validation.question_count, .pair_count, .ranking_count, .hits_per_method` | `integer` | 实际题数、唯一配对数、原始排名行数和每算法命中数。 |
| `validation.pair_counts_per_question.<question_id>, validation.group_counts.<group>` | `integer` | 每题和每展示分组的实际唯一配对数。 |
| `validation.pair_count_range[]` | `integer` | 观察到的最小、最大值，须位于 $5$–$20$。 |
| `runtime.platform, runtime.policy` | `string` | 主机及单次 CPU 建索引和四算法耗时口径，不是延迟基准。 |
| `runtime.elapsed_seconds` | `number` | 建索引及检索的实际秒数。 |

## `data/processed/annotation_pilot_four_v3/manifest.json`

字段及类型沿用本指南上方 `manifest.json` 表。仅使用前 $5$ 道已保存开发题、$5$ 篇论文、$70$ 条 passage；得到 $45$ 条唯一配对、$20$ 行排名、每算法 $25$ 次命中。`pilot=true`，历史映射与对比为空，开发模式不读取 held-out 题单或 gold。

```powershell
python -m src.data.build_common_pool pilot --four
python -m src.data.build_common_pool verify --four --output data/processed/annotation_pilot_four_v3
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version, purpose, reason, usage_boundary` | `string` | 与上方对应正式产物字段约束相同。 |
| `pilot` | `boolean` | 与上方对应正式产物字段约束相同。 |
| `settings` | `object` | 与上方对应正式产物字段约束相同。 |
| `inputs.<path>, outputs.<path>, historical_retained_files.<path>` | `string` | 与上方对应正式产物字段约束相同。 |
| `code` | `object` | 与上方对应正式产物字段约束相同。 |
| `historical_comparison.rankings_compared, .identical_id_rank_lists, .identical_score_lists` | `integer` | 与上方对应正式产物字段约束相同。 |
| `indexed_passage_count, indexed_paper_count` | `integer` | 与上方对应正式产物字段约束相同。 |
| `validation.question_count, .pair_count, .ranking_count, .hits_per_method` | `integer` | 与上方对应正式产物字段约束相同。 |
| `validation.pair_counts_per_question.<question_id>, validation.group_counts.<group>` | `integer` | 与上方对应正式产物字段约束相同。 |
| `validation.pair_count_range[]` | `integer` | 与上方对应正式产物字段约束相同。 |
| `runtime.platform, runtime.policy` | `string` | 与上方对应正式产物字段约束相同。 |
| `runtime.elapsed_seconds` | `number` | 与上方对应正式产物字段约束相同。 |

## `data/processed/annotation_common_v3_markdown/annotator_A/` / `annotator_B/`

```powershell
python -m src.data.export_common_annotations run --pool data/processed/annotation_common_v3 --output data/processed/annotation_common_v3_markdown
python -m src.data.export_common_annotations verify --pool data/processed/annotation_common_v3 --output data/processed/annotation_common_v3_markdown
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `Annotator:` | `text` | 初始为空的身份栏，第 4 步分配两位不同人员。 |
| `Question NNNN; Paper:; quoted question` | `text/headings` | 全局题号、真实标题和问题原文。 |
| `Common Retrieved Chunks; four method sections` | `headings` | 至少两来源放入 Common 并按编号排列；独有结果按原排名；空分组为 None。 |
| `Passage N; Relevance N; Retrieved by:` | `text/headings` | 每条配对在每套中出现一次，展示完整引用正文和真实来源。 |
| `Label:` | `empty text` | 仅填写 Label: 0 或 Label: 1；有用的部分证据也相关，仅主题重合不足。 |

各套 $10$ 批，每批 $20$ 题。隐藏 gold、分数、排名、内部 ID 和另一人的标签；不生成 HTML 或备注栏。保留空白模板和每人回收原件；空白核验器有意拒绝已填写标签的副本。

## `data/processed/annotation_common_v3_markdown/manifest.json`

使用上一节相同的导出与核验命令。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version, purpose, policy` | `string` | v0-proposed；独立空白且公开来源的视图，按原始排名计算指标。 |
| `inputs.<path>, outputs.<path>, source_sha256.<path>` | `string` | 共同池输入、Markdown 输出及生成代码 SHA-256。 |
| `question_count, pair_count_per_annotator` | `integer` | 保存题数和每套实际唯一配对数。 |
| `slots[]` | `string` | A、B 模板槽位，不代表已分配人员。 |
| `batches[].batch, .question_count, .pair_count` | `integer` | 从 1 开始的批号、完整题数和实际配对数。 |

## `data/processed/annotation_common_v2_markdown/annotator_A/` 和 `annotator_B/`

使用 `python -m src.data.export_common_annotations run` 生成，使用 `python -m src.data.export_common_annotations verify` 核验空白原始模板。从 GitHub `p3` 工作分支随受跟踪数据获取模板及 manifest。本地复现使用 `python -m src.data.export_common_annotations run --output tmp/tmp_annotation_export`，核验时使用同一 `--output`。拒绝已有目录。不下载模型、重新检索、抽题或关联 gold；源共同池六项文件哈希不变。

每套含 `batch_01.md` 至 `batch_10.md`，每批 $20$ 道完整问题。各批配对数为 $156,158,156,155,146,152,151,152,144,162$，每套共 $1532$ 条。两套是相同配对的独立副本，不是 $3064$ 条不同 records。A/B 仅为模板槽位，第 $2.9$ 步须为每条配对安排两位不同人员。仅分发各自的 Markdown 副本，保留空白原件；填写后的副本不应通过空白模板核验。独立提交前不分享 gold/reference JSONL 或另一人的判断。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `Annotator:` | `text` | 初始为空，填写姓名或约定标识。 |
| `0 — Not relevant`、`1 — Relevant` | `instructions` | 有助于回答问题的证据（包括部分证据）为相关，仅主题重合不足以判相关。 |
| `Question NNNN` | `level-two heading` | 按已保存题序跨批连续编号。 |
| `Paper:` 及引用的问题 | `text` | 真实论文标题及原问题，不显示内部 ID。 |
| `Common Retrieved Chunks`、`BM25`、`Dense`、`Hybrid` | `level-three headings` | Common 收录至少两个来源的配对，按稳定编号排列；独有组按原始排名排列；空组显示 `None`。 |
| `Passage N`、`Relevance N` | `level-four headings` | 现有 `record_number`，每套中每条配对出现一次；引用原 passage 正文。 |
| `Retrieved by:` | `text` | 全部实际算法来源，公开算法身份。 |
| `Label:` | `empty text` | 仅填写 `Label: 0` 或 `Label: 1`，保留编号、问题和 passage。 |

不生成 HTML 或备注栏。视图不投影 gold、分数、原始排名、内部 question/paper/passage ID 或另一人的标签。原始排名及 ID 映射仍保存在原 JSONL 中；计算指标时按这些排名关联共同最终标签，不用 Markdown 展示顺序。导出完成不代表已取得人工判断或一致率。

## `data/processed/annotation_common_v2_markdown/manifest.json`

使用上方相同的 `src.data.export_common_annotations` 命令生成和核验，从 GitHub `p3` 分支随两套模板获取。协议仍为 `v0-proposed`。核验覆盖源共同池与历史哈希、模板哈希、完整覆盖及每条记录的准确投影。源码哈希记录生成实现；只读核验不要求当前源码与历史生成字节一致。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`、`purpose`、`policy` | `string` | 提议协议、空白模板用途及独立判断与公开来源策略。 |
| `inputs` | `object<string,string>` | 共同池 manifest、题单、配对和排名路径到字节 SHA-256 的映射。 |
| `source_sha256` | `object<string,string>` | 导出器及复用渲染器路径到生成时源码 SHA-256 的映射。 |
| `question_count`、`pair_count_per_annotator` | `integer` | 每套 $200$ 题、$1532$ 条唯一配对。 |
| `slots` | `array<string>` | 独立空白模板槽位 `A` 和 `B`，尚未分配人员。 |
| `batches` | `array<object>` | 各批覆盖数量，两套相同。 |
| `batches[].batch` | `integer` | 从 $1$ 开始的批次编号。 |
| `batches[].question_count`、`batches[].pair_count` | `integer` | 该批完整问题数和实际并集配对数。 |
| `outputs` | `object<string,string>` | 全部 $20$ 份 Markdown 路径到字节 SHA-256 的映射，不包含 manifest 自身。 |

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
| `retrieval` | `object` | 三个算法共用的规范化检索配置。 |
| `retrieval.mode` | `string` | hybrid，不使用重排器。 |
| `retrieval.candidate_k`, `retrieval.rrf_k` | `integer` | $20$ 和 $60$，等权 RRF。 |
| `retrieval.dense` | `object` | BGE small English v1.5 推理配置，具体字段见下方。 |
| `retrieval.dense.revision` | `string` | 固定模型/tokenizer revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`。 |
| `retrieval.dense.device`, `retrieval.dense.cache_folder` | `string` | CPU 和已忽略的本地模型缓存。 |
| `retrieval.dense.batch_size` | `integer` | 每批推理 $32$ 个问题或 passage。 |
| `retrieval.dense.local_files_only` | `boolean` | True，从本地缓存加载固定模型。 |
| `retrieval.reranker` | `object` | 规范化后的未启用默认值，本次不加载或使用。 |
| `retrieval.reranker.revision`, `retrieval.reranker.device`, `retrieval.reranker.cache_folder` | `string` | 未启用的 revision、CPU 及本地缓存路径。 |
| `retrieval.reranker.batch_size`, `retrieval.reranker.max_length` | `integer` | 未启用的默认值 $8$ 和 $512$。 |
| `retrieval.reranker.local_files_only` | `boolean` | 未启用的离线默认值 true。 |
| `retrievers.<method>` | `object` | 完整生效元数据，包括嵌套 bm25/dense/reranker、依赖版本和融合配置；嵌套字段见下方。 |
| `retrievers.<method>.id`, `retrievers.<method>.mode`, `retrievers.<method>.source_commit`, `retrievers.<method>.scope`, `retrievers.<method>.score`, `retrievers.<method>.tie_break` | `string` | 实现标识、算法、上游提交、论文范围、原始分数含义及并列规则。 |
| `retrievers.<method>.packages.<package>` | `string` | 已安装依赖版本。 |
| `retrievers.<method>.persistent_score_cache`, `retrievers.<method>.bm25.enabled`, `retrievers.<method>.dense.enabled`, `retrievers.<method>.reranker.enabled` | `boolean` | 缓存及组件开关，不使用持久化分数缓存或重排器。 |
| `retrievers.<method>.bm25.tokenizer` | `string` | Casefold 加 Unicode 单词序列，独立 Dense 不含此字段。 |
| `retrievers.<method>.bm25.k1`, `retrievers.<method>.bm25.b`, `retrievers.<method>.bm25.epsilon` | `number` | 生效的 BM25 参数 $1.5$、$0.75$、$0.25$。 |
| `retrievers.<method>.dense.revision`, `retrievers.<method>.dense.device`, `retrievers.<method>.dense.cache_folder`, `retrievers.<method>.dense.model_name`, `retrievers.<method>.dense.tokenizer_revision`, `retrievers.<method>.dense.query_instruction`, `retrievers.<method>.dense.normalization`, `retrievers.<method>.dense.similarity_metric`, `retrievers.<method>.dense.index_type`, `retrievers.<method>.dense.truncation`, `retrievers.<method>.dense.truncation_observation` | `string` | 生效的模型/tokenizer 标识、CPU 设备、本地缓存、问题前缀、L2 归一化、余弦相似度、FAISS IndexFlatIP 和 token 截断元数据。 |
| `retrievers.<method>.dense.batch_size`, `retrievers.<method>.dense.max_seq_length` | `integer` | 生效的 Dense batch size $32$、token 上限 $512$。 |
| `retrievers.<method>.dense.local_files_only` | `boolean` | 生效的 Dense/Hybrid 模型采用 true，离线加载。 |
| `retrievers.Hybrid.candidate_k_per_source`, `retrievers.Hybrid.rrf_k`, `retrievers.Hybrid.final_top_k` | `integer` | $20$、$60$ 和 $5$。 |
| `retrievers.Hybrid.rerank_all_fused_candidates` | `boolean` | False。 |

## `data/processed/annotation_common_v2/run_inputs.json`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `inputs.<path>` | `string` | 运行前配置、题单/manifest、禁用清单、语料、QA/论文及溯源记录的精确字节 SHA-256。 |
| `code.commit`, `code.python` | `string` | 检索前记录的 HEAD 与 Python 版本。 |
| `code.working_tree_status[]` | `string` | 保存的 Git 短状态，包括未提交实现。 |
| `code.source_sha256.<path>` | `string` | 精确实现哈希，写结果前重新检查 src 和 scripts。 |

## `data/processed/annotation_common_v2/manifest.json`

使用 `python -m src.data.build_common_pool run` 生成，使用 `python -m src.data.build_common_pool verify` 核验。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `purpose`, `reason`, `reuse_policy`, `usage_boundary` | `string` | 提议中的正式版本、重建原因、不复用旧结果及评估边界。 |
| `historical_retained_files.<path>` | `string` | 生成时记录的溯源路径到 SHA-256 的映射。 |
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

由 `python -m src.data.freeze_held_out retire` 一次生成。此现有溯源 manifest 记录重新抽样原因、问题层面用途判定、原始字节指纹及替代题单路径，不作为当前标注候选池。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `status`, `reason` | `string` | 暂定 schema、停用状态及重新抽样原因。 |
| `retained_files.<path>` | `string` | 生成时记录的溯源路径到 SHA-256 的映射。 |
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

生成命令：`python -m src.data.build_held_out_exclusions`；已有产物核验：`python -m src.data.build_held_out_exclusions --verify`。本地复现且不替换共享数据：`python -m src.data.build_held_out_exclusions --output tmp/tmp_qa_banned_for_held_out.jsonl`，JSONL 字节相同，manifest 记录新输出路径和生成身份。拒绝覆盖已有输出。生成使用负责人快照、QA、preparation 审计及生成时的用途记录；精确输入哈希保存在配套 manifest。JSONL、manifest、快照及 config 一起从 GitHub P3 分支获取，无须 Release。

负责人指定 ID 全部禁用。其他题按是否用于选择或调整模型、参数、算法、prompt 或证据处理规则判定，失败/作废实验遵循同一用途规则。纯功能测试和冻结配置下的评估不自动导致禁用，但其他符合排除条件的来源仍可禁用这些题。原始导出、gold 映射本身不导致禁用。用途证据与判定保存在 config/manifest。禁用题单本身不是题单冻结记录；独立的 `v2` 冻结见上文。采用问题层面隔离，允许共享论文。

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

与题单使用同一命令生成和核验。输入用精确字节 SHA-256，负责人来源另固定分支/commit/路径。本地版本记录生成时 HEAD/分支及输入/实现哈希，包含尚未提交的新文件，不表示这些文件当时已提交。核验允许后续 HEAD 改变，但重建题单并检查全部保存哈希。未知 ID、身份冲突、来源内重复问题 ID、固定哈希/数量变化、来源丢失或未决用途证据均在写出前报错。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version`, `purpose`, `repository`, `scope`, `exclusion_rule` | `string` | `v0-proposed`、用途、仓库和有范围边界的使用规则。 |
| `local_source_version` | `object` | 生成版本。 |
| `local_source_version.branch`, `.commit` | `string` | 本地 P3 分支和完整 HEAD SHA。 |
| `implementation` | `object` | 精确实现身份。 |
| `implementation.path`, `.sha256` | `string` | 模块路径及 SHA-256。 |
| `inputs` | `object<string,string>` | 生成输入路径到 SHA-256 的映射。 |
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

## 数据共享与更新

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

下列目录树列出现有原始数据和处理后产物。`README_zh-CN.md`、`README.md` 与所列生成文件一起纳入 Git。

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
    ├── annotation_common_v2/
    ├── annotation_common_v2_markdown/
    ├── held_out_exclusion_sources/
    ├── qa_banned_for_held_out.jsonl
    ├── qa_banned_for_held_out.manifest.json
    ├── sample_passages_100.jsonl
    └── sample_passages_100.manifest.json
```

构建顺序：原始采集 → `papers.jsonl`、`qa.jsonl` 和导出 manifest → 开发/全论文正文语料及样本 → 证据映射。下文每份文件均有独立生成命令和字段表；重复列出的命令会同时生成配套文件，每个独立构建只需执行一次。

各构建器拒绝已存在的输出路径。重建时使用新的暂存目录，并同步调整全流程的输入/输出路径。语料和样本 CLI 不读取 YAML，旧默认值为 $200/40$ 词，因此必须显式传入选定的 $365/40$ 参数。这里是词数，不是模型 token 数。

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

这是本地 JSON 加载器，不是 Hub 下载或块构建器，记录仍为论文级。原始文件、生成语料和配套 manifest 一起纳入 Git；源压缩包、缓存及暂存目录不纳入 Git。只有不再需要且满足实验保留要求时，才清理本地输出。

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

保留用于溯源的 $200$ 题题单；当前正式评估使用 `qa_for_held_out_v2.jsonl`。

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
