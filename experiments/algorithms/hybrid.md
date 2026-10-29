# Hybrid：融合关键词与语义检索

本文说明本项目 `HybridRetriever` 的核心思路、输入、输出和完整流程，以当前实现和三方法检索配置为准。共享 passage 接口仍为 `v0-proposed`。英文版见 [hybrid.en.md](hybrid.en.md)。

## 1. 核心思路

Hybrid 对同一个问题、同一篇论文分别运行 BM25 和 Dense，再用 Reciprocal Rank Fusion（RRF，倒数排名融合）合并两路候选。BM25 根据词项匹配评分，适合定位术语、模型名等文字线索；Dense 根据语义向量的余弦相似度评分，可以补充表述不同但语义相关的分块。两路方法的具体流程分别见 [BM25.md](BM25.md) 和 [dense.md](dense.md)。

BM25 原始分数与 Dense 余弦分数不在同一尺度，因此当前实现只用各路名次计算融合分数，不直接相加原始分数，也不做原始分数归一化。设分块为 $p$，返回它的来源集合为 $S(p)$，则：

$$
\operatorname{RRF}(p)=\sum_{s\in S(p)}\frac{1}{k_{\mathrm{RRF}}+r_s(p)}
$$

其中，$r_s(p)$ 是来源 $s$ 内从 $1$ 开始的原始名次，$k_{\mathrm{RRF}}$ 对应代码参数 `rrf_k`，默认值为 $60$。所有来源等权；某一路没有返回该分块时，该路贡献为 $0$。名次越靠前，贡献越大；同时出现在两路结果中的分块会累加两项贡献。

`rrf_k` 是平滑名次差异的常数，不是候选数量。`candidate_k` 才控制每路最多取多少候选，`top_k` 控制最终最多返回多少条。Hybrid 的目标是利用两类检索线索互补，但是否改善证据召回或答案质量仍需实验验证。

## 2. 输入是什么

### 初始化输入

`HybridRetriever(sparse, dense, *, scorer=None, candidate_k=20, rrf_k=60)` 接收已经准备好的检索回调，不自行切分论文或建立索引。

| 参数 | 类型与默认值 | 含义 |
| --- | --- | --- |
| `sparse` | 检索回调 | 项目中使用 `BM25Retriever.retrieve`。 |
| `dense` | 检索回调 | 项目中使用 `DenseRetriever.retrieve`。 |
| `scorer` | `PairScorer` 或 `None`，默认 `None` | 可选重排器，提供 `score(query, texts)`；未提供时仅执行 RRF。 |
| `candidate_k` | 正整数，默认 $20$ | 向每一路请求的候选上限。 |
| `rrf_k` | 正整数，默认 $60$ | RRF 公式中的平滑常数。 |

两路回调均接收 `(query, paper_id, top_k)`，返回 `list[RetrievalHit]`。此处回调中的 `top_k` 实际由 Hybrid 的 `candidate_k` 传入。每条候选包含完整 `passage`、从 $1$ 开始的 `rank` 和有限浮点数 `score`。

两路应使用同一份分块语料和相同的 ID 映射。公开 `Passage` 字段为 `passage_id`、`paper_id`、`title`、`section`、`chunk_number`、`text`、`previous_passage_id` 和 `next_passage_id`；字段类型和含义见 [Dense 输入说明](dense.md#2-输入是什么)。同一 ID 代表的完整分块记录必须一致。原文位置、标准答案、gold evidence 和人工标签由评估侧保留，不参与 Hybrid 检索或融合。

### 查询输入

查询接口是 `retrieve(query, paper_id, top_k=5, *, section=None)`。

| 参数 | 类型与约束 | 含义 |
| --- | --- | --- |
| `query` | 非空且不能全为空白的 `str` | 两路使用同一问题原文；Dense 内部另加固定检索指令。 |
| `paper_id` | 非空且不能全为空白的 `str` | 两路都只检索该论文。 |
| `top_k` | 正整数，默认 $5$ | 最终输出上限。 |
| `section` | 非空且不能全为空白的 `str` 或 `None` | 预留的章节过滤参数，默认不限制章节。 |

`candidate_k`、`rrf_k` 和 `top_k` 均不接受布尔值。Hybrid 类本身不要求 `candidate_k >= top_k`，但实验适配层对 Hybrid 模式施加了这一约束。

当 `section` 非空时，Hybrid 会将其作为关键字参数传给两路回调，并检查返回章节。当前项目的 `BM25Retriever.retrieve` 和 `DenseRetriever.retrieve` 均不接收此参数，直接传入会触发 `TypeError`；现有三方法路径使用 `section=None`。只有配套回调实现章节过滤后，才能使用这一预留接口。

## 3. 输出是什么

输出为按最终名次排列的 `list[RetrievedPassage]`，不是生成的答案。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `passage` | `Passage` | 完整原始分块，保留正文和元数据。 |
| `rank` | `int` | 从 $1$ 开始的最终名次；启用重排时为重排后的名次。 |
| `source_scores` | `dict[str, SourceScore]` | 仅记录实际返回该分块的来源，当前键为 `bm25`、`dense`。 |
| `source_scores[source].rank` | `int` | 该分块在来源内从 $1$ 开始的原始名次。 |
| `source_scores[source].score` | 有限 `float` | 对应来源的原始分数，供追溯，不参与 RRF 算分。 |
| `rrf_score` | 正的有限 `float` | 按来源名次计算的 RRF 分数；重排后仍保留。 |
| `reranker_score` | 有限 `float` 或 `None` | 未重排时为 `None`；BGE 重排时为原始 logit。 |

设去重后的候选并集大小为 $U$，输出数量为 $\min(\text{top\_k},U)$。每路遵守候选上限时，$U\leq 2\times\text{candidate\_k}$；默认最多融合 $40$ 个不同分块。两路都为空时返回 `[]`，仅一路为空时仍融合另一条列表。现有 BM25、Dense 对合法但不存在的论文 ID 都返回空列表，因此 Hybrid 也返回 `[]`。

未启用重排时，按 `rrf_score` 降序、`passage_id` 升序排列。启用重排时，按 `reranker_score` 降序，再按 `rrf_score` 降序、`passage_id` 升序排列。RRF 分数和重排 logit 都不是相关概率或答案正确率；当前没有最低相关性门槛，上游的零分、负分候选仍可能因名次而进入最终结果。

P3 的 `scored_ids()` 将结果转成有序 `(passage_id, score)` 列表，保持最终排名：有重排分数时取重排分数，否则取 RRF 分数。零或负的重排 logit 仍是有效分数，只有 `None` 才回退到 RRF。

## 4. 完整流程

```text
准备阶段
论文正文 → 上游切分为统一 Passage 集合
    → 建立 BM25 词项索引与 Dense 向量索引，或加载已有 Dense 索引
    → 将两路 retrieve 回调交给 HybridRetriever

查询阶段
query + paper_id + top_k
    → 校验查询参数
    → BM25：论文内词项评分与排序，最多 candidate_k 条
    → Dense：问题编码、归一化与余弦排序，最多 candidate_k 条
    → 检查候选论文范围
    → 按 passage_id 合并，检查同 ID 内容与来源内名次一致性
    → 按来源原始名次计算 RRF，保存原始名次和分数
    → 按 RRF 降序、passage_id 升序排序
    → 无 scorer：截取 top_k
    → 有 scorer：对整个候选并集重排，再截取 top_k
    → 返回 RetrievedPassage，交给后续评估或答案生成模块
```

### 第一步：准备两路索引

上游清洗、切分论文，并给分块分配稳定 ID。P3 适配层仅投影八个公开字段到检索接口。BM25 和 Dense 按论文建立各自索引；三方法建池程序复用同一套 sparse、dense 实例，分别支持独立 BM25、独立 Dense 和 Hybrid。

BM25 使用分块 `text` 的词项统计；Dense 使用 `BAAI/bge-small-en-v1.5` 编码 `text`，L2 归一化后放入 FAISS `IndexFlatIP`。标题、章节与相邻分块 ID 随结果保留，不额外拼入这两路的检索文本，也不自动扩展邻块。Hybrid 不持有独立的第三套索引。

### 第二步：校验查询并分别召回

Hybrid 校验非空问题、论文 ID、正整数 `top_k` 和可选 `section`，随后依次调用 sparse、dense；当前实现不是并发调用。两路接收相同问题和论文 ID，各自返回最多 `candidate_k` 条候选，按原始分数降序、ID 升序排列，并记录原始名次。

Dense 内部在问题前加 `Represent this sentence for searching relevant passages: `，分块侧不加该指令。Dense 默认输入上限为 $512$ tokens，超长文本会截断；返回记录仍保留完整正文。Hybrid 不改变两路的编码、分词或截断规则。

### 第三步：检查范围并按 ID 去重

任一路返回其他论文的分块时，Hybrid 抛出 `ValueError`。RRF 随后按 `passage_id` 合并两路记录，同一分块只在候选并集中出现一次，但保留各来源的名次与原始分数。

同一来源重复返回同一 ID 时，只保留其最优原始名次，不重复累计贡献，也不重新压缩其他名次。相同 ID 对应不同分块内容、同一来源把同一名次分配给不同 ID，或同一 ID 在同一来源同一名次出现冲突分数时，均抛出 `ValueError`。

### 第四步：计算 RRF 并排序

对候选并集中每个 ID，按公式汇总所有已出现来源的贡献。代码使用 `RetrievalHit.rank`，而非候选在列表中的当前位置，也不依据原始分数重新排位。按 RRF 降序、ID 升序形成确定性列表，并重新赋予连续的最终名次。

### 第五步：可选重排并截取

默认 `scorer=None`，直接截取 RRF 列表前 `top_k` 条。若配置 scorer，则先对整个去重并集评分，再截取，不会先把 RRF 列表缩到 `top_k`。

项目可选的 `BGEReranker` 使用 `BAAI/bge-reranker-base`，将每个问题与候选 `text` 配对，默认每批 $8$ 对，并按 `max_length=512` tokens 填充、截断。它输出每对一个原始 logit，不做 sigmoid 概率转换。重排阶段要求每个候选恰有一个有限分数，否则报错；按重排分数、RRF、ID 排序后重编最终名次，保留来源信息和原 RRF 分数。

### 第六步：交付可追溯结果

调用方获得最终分块列表，可序列化为 JSON，或由 P3 转为 ID、分数列表后关联完整正文与证据位置。Hybrid 本身不判断答案是否充分、不读取 gold evidence，也不生成答案。候选召回之外的分块不会被融合或重排阶段补回；最终效果受到候选数量、分块方式和模型截断的共同影响。

## 5. 一个可以手算的例子

假设 `rrf_k=60`，两路各返回 $3$ 个候选：BM25 为 `A, B, C`，Dense 为 `B, D, A`。下表中的字母表示分块 ID。

| 分块 | BM25 名次 | Dense 名次 | RRF 计算 | 近似分数 |
| --- | --- | --- | --- | --- |
| `A` | $1$ | $3$ | $1/61+1/63$ | $0.032266$ |
| `B` | $2$ | $1$ | $1/62+1/61$ | $0.032522$ |
| `C` | $3$ | 未返回 | $1/63$ | $0.015873$ |
| `D` | 未返回 | $2$ | $1/62$ | $0.016129$ |

最终 RRF 顺序为 `B, A, D, C`。若 `top_k=2` 且未重排，则返回 `B, A`。若启用重排，`A, B, C, D` 都会先被评分，最终顺序可以改变。

## 6. 当前项目配置与使用入口

| 项目 | 当前设置或行为 |
| --- | --- |
| 保留的三方法配置 | `configs/annotation_pilot.json`：`mode="hybrid"`、`candidate_k=20`、`rrf_k=60`、`top_k=5`。 |
| 分块配置 | 约 $365$ words，重叠 $40$ words；属于项目配置，不是 Hybrid 的固有限制。 |
| Dense 模型版本 | `BAAI/bge-small-en-v1.5`，revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`。 |
| 三方法重排 | `build_multi_retriever_pilot.py` 在三方法模式下不传 scorer，不启用 BGE 重排。 |
| 四方法正式评估 | `configs/annotation_four.json` 冻结新增的 BGE 重排；`python -m src.data.build_common_pool run --four` 统一重新检索，`annotation_common_v3/` 为当前核验通过的共同池。完整配置、字段与复现见[数据指南](../../data/README_zh-CN.md)。 |
| 实验可选模式 | `hybrid` 只做 RRF；`hybrid_rerank` 对整个融合候选并集做 BGE 重排。 |
| 模型长度 | Dense 单文本默认上限 $512$ tokens；BGE 重排默认问题与分块对上限 $512$ tokens。words 不等于 tokens。 |

已有匹配的 Passage JSONL 和 Dense 索引时，可以在项目根目录使用 `scripts/demo_hybrid.py`；将下面占位路径和论文 ID 替换为实际值：

```powershell
python -m scripts.demo_hybrid --passages "path/to/passages.jsonl" --dense-index-dir "path/to/dense-index" --query "What is the main contribution?" --paper-id "paper-id" --candidate-k 20 --rrf-k 60 --top-k 5 --local-files-only
```

该 demo 会检查输入分块与保存索引的映射一致性，默认只运行 RRF，加 `--bge` 才启用重排。`--local-files-only` 要求所需模型已在缓存中。输出 JSON 包含参数、模型版本、两路候选数量、去重候选数、结果及耗时。计时在一次预热后进行一次完整检索，不含模型与索引加载，不能把单次耗时视为性能基准。

## 7. 实现依据

- [hybrid_retriever.py](../../src/retrieval/hybrid_retriever.py)：查询编排、参数与范围检查、可选重排入口。
- [fusion.py](../../src/retrieval/fusion.py)：RRF 公式、去重、一致性检查和同分排序。
- [schemas.py](../../src/retrieval/schemas.py)：`v0-proposed` 输入、输出结构。
- [reranker.py](../../src/retrieval/reranker.py)：BGE 配对评分和最终重排。
- [build_multi_retriever_pilot.py](../../src/data/build_multi_retriever_pilot.py) 与 [annotation_pilot.json](../../configs/annotation_pilot.json)：三方法共用索引与当前配置。
- [chunk_size_retrieval.py](../../src/evaluation/chunk_size_retrieval.py)：实验模式、参数约束和 ID／分数适配。
- [demo_hybrid.py](../../scripts/demo_hybrid.py)：保存索引的查询入口和计时策略。
