# Dense：如何用语义向量检索论文分块

本文说明本项目 `DenseRetriever` 的核心思路、输入、输出和完整流程，并区分独立 Dense 检索与 Hybrid 中的 Dense 分支。内容以当前实现和三方法检索配置为准；共享 passage 接口仍为 `v0-proposed`。英文版见 [dense.en.md](dense.en.md)。

## 1. 核心思路

Dense 检索把问题和论文分块分别编码成固定长度的数值向量，再按向量的相似程度排序。向量由预训练模型根据文字计算，目标是让语义相关的问题和分块得到较高相似度，因此不要求双方出现完全相同的关键词。

例如，问题是 `How does the model reduce overfitting?`，分块写的是 `We randomly disable neurons during training.`。即使没有相同的关键术语，编码器也可能识别两者的关系。但语义相似不保证分块包含完整答案，也不保证模型能正确区分否定、数字或实验条件。

本项目默认使用 `BAAI/bge-small-en-v1.5`，通过 `SentenceTransformer` 调用同一个编码器处理问题和分块。当前检索代码使用预训练权重进行推理，不执行训练或微调。

设问题为 $q$、分块为 $p$、编码器为 $E$。代码先得到并归一化向量：

$$
\mathbf{v}_q=E(\text{instruction}+q),\qquad \mathbf{v}_p=E(p.\text{text}),\qquad \hat{\mathbf{v}}=\frac{\mathbf{v}}{\lVert\mathbf{v}\rVert_2}
$$

再用归一化向量的内积计算余弦相似度：

$$
\operatorname{score}(q,p)=\hat{\mathbf{v}}_q^\top\hat{\mathbf{v}}_p=\frac{\mathbf{v}_q^\top\mathbf{v}_p}{\lVert\mathbf{v}_q\rVert_2\lVert\mathbf{v}_p\rVert_2}
$$

其中，`instruction` 是只加在问题前的检索指令。分数越高，分块在当前问题下越靠前。这里的“内积等于余弦相似度”依赖于两侧都已完成 L2 归一化。

## 2. 输入是什么

### 建索引的输入

`DenseRetriever(passages, ...)` 接收已经切好的 `Passage` 集合。P3 的论文正文来自 `data/processed/papers.jsonl`，分块由上游程序生成；Dense 不决定分块边界。当前三方法检索配置采用约 $365$ words 的分块和 $40$ words 的重叠，这些是项目配置，不是 Dense 算法的固有限制。

| 字段 | 类型 | 在 Dense 中的作用 |
| --- | --- | --- |
| `passage_id` | `str` | 全局唯一标识；用于索引行映射和同分排序。 |
| `paper_id` | `str` | 按论文建立独立索引，限制查询范围。 |
| `title` | `str` | 保留给展示和追溯，不拼接到编码文本中。 |
| `section` | `str` | 保留章节信息，不拼接到编码文本中。 |
| `chunk_number` | `int` | 非负分块序号，随记录保留。 |
| `text` | `str` | 非空分块正文，是唯一参与分块编码的字段。 |
| `previous_passage_id` | `str` 或 `null` | 前一分块 ID；可以为空，不自动扩展相邻分块。 |
| `next_passage_id` | `str` 或 `null` | 后一分块 ID；可以为空，不自动扩展相邻分块。 |

P3 适配层只投影这八个公开字段。原文位置、标准答案、gold evidence 和人工相关性标签不进入 Dense 索引或相似度计算；评估需要的附加字段由调用方另外保留。

### 查询的输入

查询接口是 `retrieve(query, paper_id, top_k)`。

| 参数 | 类型与约束 | 含义 |
| --- | --- | --- |
| `query` | 非空且不能全为空白的 `str` | 问题原文；检索器在编码前添加固定指令。 |
| `paper_id` | 非空且不能全为空白的 `str` | 只检索该论文的分块。 |
| `top_k` | 正整数，不接受布尔值 | 最多返回的分块数；当前三方法对比各自返回 $5$ 个。 |

当前 Dense 接口没有 `section` 过滤参数。章节信息会随结果返回，但不会自动把搜索范围限制到某一章节。

## 3. 输出是什么

直接调用检索器得到按相似度排序的 `list[RetrievalHit]`。每条结果包含：

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `passage` | `Passage` | 原始分块记录，包含上述八个字段和完整 `text`。 |
| `rank` | `int` | 从 $1$ 开始的最终 Dense 名次。 |
| `score` | 有限 `float` | 当前问题与该分块的余弦相似度。 |

P3 的 `scored_ids()` 再将结果转换成有序的 `(passage_id, score)` 列表，保持原排名；评估程序按 ID 找回完整分块和原文位置。

余弦分数在数学上介于 $-1$ 和 $1$ 之间，实际存储受浮点误差影响。它不是相关概率或答案正确率，不能与 BM25 原始分数、RRF 分数或重排器 logit 直接相加或混作同一尺度。

当前实现不设置最低相似度门槛，零分和负分也参与排序。若该论文有 $N$ 个分块，则返回 $\min(\text{top\_k},N)$ 个；论文 ID 合法但不存在时返回 `[]`。参数不合法时抛出 `ValueError`。排序规则为 `score` 降序，同分按 `passage_id` 升序；即使所有分块都不相关，也可能返回完整的 top-$K$ 列表。

## 4. 完整流程

```text
建索引阶段
论文正文 → 上游分块 → 校验公开字段和唯一 ID
    → 按 paper_id 分组，每组按 passage_id 升序
    → 用 BGE 编码各分块 text → L2 归一化
    → 每篇论文建立 FAISS IndexFlatIP，保留索引行到原分块的映射
    → 可选：保存索引与 metadata.json

查询阶段
query + paper_id + top_k
    → 校验参数 → 选择该论文的索引；不存在则返回 []
    → 在问题前添加固定指令 → 用同一版本 BGE 编码 → L2 归一化
    → 计算与该论文所有分块的内积，即余弦相似度
    → 按分数降序、passage_id 升序排序 → 返回最多 top_k 条 RetrievalHit

后续处理
Dense 结果 → 独立评估，或交给 Hybrid 做 RRF 融合
评估程序 → 按 ID 找回完整文本和原文位置 → 核对证据或人工标签
```

### 第一步：准备和分组分块

上游程序先完成清洗和分块，再构造 `Passage`。检索器拒绝重复的 `passage_id`，按 `paper_id` 分组，并把每篇论文的分块按 `passage_id` 升序排列。这个顺序决定 FAISS 的行号与原始分块如何对应。若实验改变分块大小或候选语料，应为新语料重新建索引。

### 第二步：加载编码器

默认编码器在第一次编码时加载模型，模型缓存缺省位于项目的 `.cache/huggingface/`。当前实验配置固定模型 revision 为 `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`；直接使用 `DenseRetriever` 时也可以传入 revision，首次加载会解析并记录不可变的模型提交版本。

索引与查询必须使用相同的模型、revision 和编码规则，只有向量维度相同并不足以保证兼容。代码检查编码器身份，拒绝建索引后改变身份的编码器。测试可以注入声明了身份的替代编码器；这不是当前真实模型实验路径。

### 第三步：编码分块并处理长度

每个分块只编码 `text`，不添加问题指令，也不额外拼接标题或章节名。代码设置 `prompt=""`，避免 `SentenceTransformer` 再隐式添加其他 prompt。

默认 BGE 路径设置 `max_seq_length=512`，超出模型输入上限的文本会被 tokenizer 截断。这个上限按模型 token 计算，并包含特殊 token；问题侧还要容纳指令。实验中的 words 按空白分隔计数，和 token 不是同一单位，因此约 $365$ words 不保证一定放得进 $512$ tokens。

当前实现把每个分块作为一个输入文本，不在内部滑窗，也不对截断后的剩余部分再编码、汇总。返回结果和评估报告仍保留完整 `text`，所以“返回的文字”可能长于“编码器实际看到的文字”。实验元数据记录了截断策略，但不等于逐块核验过真实 tokenizer 的截断情况。

### 第四步：归一化并建立向量索引

代码检查向量矩阵的行数、维度、数值类型和有限性，拒绝零向量。归一化先用 `float64` 计算，并先按最大绝对值缩放以避免求范数溢出，最后转成连续的 `float32` 矩阵。

每篇论文建立一个 `faiss.IndexFlatIP`，加入归一化后的分块向量；所有论文共用同一个编码器。这是对论文内向量进行精确内积搜索的平面索引，不是近似最近邻索引。原始分块列表与索引行号一一对应，检索命中后据此恢复正文和元数据。

### 第五步：编码问题

先校验 `query`、`paper_id` 和 `top_k`，再检查目标论文是否存在。只有找到对应索引才编码问题。问题前添加的指令如下，代码中的字符串末尾有一个空格：

```text
Represent this sentence for searching relevant passages:
```

随后使用同一编码器得到问题向量，并按与分块相同的规则进行 L2 归一化。

### 第六步：评分、排序和截取

代码调用 `index.search(query_vector, index.ntotal)`，取回目标论文全部分块的分数和行号，再按分数降序、`passage_id` 升序排序，最后截取 `top_k`。取回全部候选能确保第 $K$ 名边界上的同分项也进入统一排序，避免 FAISS 返回同分项的内部顺序决定最终结果。

若目标论文有 $N$ 个分块、向量维度为 $d$，不计问题编码，当前查询的向量评分工作量约为 $O(Nd)$，之后的完整排序约为 $O(N\log N)$。`top_k` 控制输出数量，不会让当前实现只计算 $K$ 个候选的分数。

### 第七步：交付结果或保存索引

独立 Dense 检索直接返回 `RetrievalHit`；评估和生成答案由后续模块处理。Dense 自身不读取标准答案、不判断证据是否充分，也不生成回答。

可选的 `save(directory)` 将每篇论文的向量写为 `paper-000000.faiss` 等文件，并在 `metadata.json` 中保存模型身份、编码设置、向量维度、完整分块行映射和各索引文件的 SHA-256。保存目录必须是新目录或空目录，模型权重不包含在索引文件中。

`DenseRetriever.load(directory, ...)` 恢复已有向量，不重新编码分块；它核对元数据、校验和、行映射、索引类型、维度和归一化状态。真实编码器在首次查询时才加载保存的模型 revision，因此复用索引仍需要相应模型文件。模型权重和索引均保留在 Git 之外。

## 5. 一个可以手算的例子

假设归一化后的问题向量是 $(1,0)$，某篇论文有以下三个分块。这里只用二维假想向量解释计算，不是 BGE 的真实输出，也不是实验结果。

| 分块 ID | 归一化向量 | 与问题的内积 |
| --- | --- | --- |
| `A` | $(0.8,0.6)$ | $1\times0.8+0\times0.6=0.8$ |
| `B` | $(0.8,-0.6)$ | $0.8$ |
| `C` | $(-1,0)$ | $-1$ |

当 `top_k=2` 时，返回 `A`、`B`，分数均约为 $0.8$，名次分别为 $1$、$2$；同分时 `A` 在前。若 `top_k=5`，只有三个可用分块，因此返回 `A`、`B`、`C`，负分的 `C` 也会保留。结果数量足够，不等于证据充分。

## 6. 当前配置及其在 Hybrid 中的位置

| 设置 | 当前实现或实验配置 |
| --- | --- |
| 模型 | `BAAI/bge-small-en-v1.5`；默认真实编码器固定使用该模型。 |
| 实验 revision | `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`。 |
| 设备与编码批量 | 当前三方法配置为 `device="cpu"`、`batch_size=32`。 |
| 最大输入长度 | 默认 BGE 路径为 $512$ tokens；不提供分块内部滑窗。 |
| 分块编码文本 | 仅 `text`，不加检索指令。 |
| 问题编码文本 | 固定检索指令加原始问题。 |
| 向量与索引 | L2 归一化、`float32`、每篇论文一个 `IndexFlatIP`。 |
| 查询范围与同分处理 | 指定论文内；同分按 `passage_id` 升序。 |
| 模型缓存 | `.cache/huggingface/`；实验配置为 `local_files_only=true`，要求预先准备缓存。 |
| 独立 Dense 的返回量 | 当前三方法对比为 top-$5$；接口本身允许其他正整数。 |
| Hybrid 中的 Dense 候选量 | 每次最多 $20$ 个；随后与 BM25 候选做 RRF，`rrf_k=60`，最终取 $5$ 个。 |

`src/data/build_multi_retriever_pilot.py` 在 BM25、Dense、Hybrid 三方法之间复用同一套 sparse 和 dense 索引。独立 Dense 列表按余弦分数排序；Hybrid 使用两路排名做 RRF，不直接相加 BM25 和余弦原始分数。当前三方法建池路径不启用重排；单独的 `hybrid_rerank` 模式才会继续调用 BGE cross-encoder，其 logit 不是这里的 Dense 分数。

三方法配置入口是 `configs/annotation_pilot.json`，正式建池会保存冻结配置和来源信息。`configs/default.yaml` 中的 `dense_model: null` 仍是共享配置占位项，不能据此判断当前实现未选定模型。冻结规则、数据来源和产物获取方式以[数据说明](../../data/README_zh-CN.md)为准，评估边界见[评估协议](../../docs/EVALUATION.md)。

## 7. 如何运行现有入口

在项目根目录、已安装项目依赖的 Python 环境中执行以下命令。示例使用合成 fixture，不读取正式评估问题；`--local-files-only` 要求缓存中已有上述固定 revision 的完整模型文件。

先构建索引。`.cache/dense-demo/` 必须不存在或为空；该入口同时验证 BM25 能否建索引，但只持久化 Dense 索引。

```powershell
python -m scripts.build_indexes --passages tests/fixtures/mock_passages.jsonl --output-dir .cache/dense-demo --device cpu --local-files-only
```

再从同一份分块文件加载索引并查询：

```powershell
python -m scripts.demo_p1 --passages tests/fixtures/mock_passages.jsonl --dense-index-dir .cache/dense-demo --paper-id synthetic-ir --query "How are semantic vectors used for retrieval?" --top-k 5 --device cpu --local-files-only
```

该 demo 分别打印 BM25 和 Dense 的结果，包含名次、分块 ID、分数、章节和文本预览；不会做 Hybrid 融合。它先分别预热一次，再计时一次完整检索调用，不计模型加载与建索引，单次耗时不能视为性能基准。真实语料应替换为对应 Passage JSONL 和论文 ID，并保证查询文件与保存索引的分块完全一致。

## 8. 对应代码

- [dense_retriever.py](../../src/retrieval/dense_retriever.py)：编码指令、归一化、按论文建索引、精确检索、稳定排序及保存和加载。
- [schemas.py](../../src/retrieval/schemas.py)：`Passage` 和 `RetrievalHit` 字段；共享接口仍为 `v0-proposed`。
- [chunk_size_retrieval.py](../../src/evaluation/chunk_size_retrieval.py)：P3 字段投影、检索模式选择、分数适配和实验元数据。
- [build_multi_retriever_pilot.py](../../src/data/build_multi_retriever_pilot.py) 与 [build_common_pool.py](../../src/data/build_common_pool.py)：三方法复用索引及正式公共评估池流程。
- [hybrid_retriever.py](../../src/retrieval/hybrid_retriever.py) 与 [fusion.py](../../src/retrieval/fusion.py)：Dense 候选的 RRF 融合及可选重排入口。
- [annotation_pilot.json](../../configs/annotation_pilot.json)：当前三方法检索参数。
- [build_indexes.py](../../scripts/build_indexes.py) 与 [demo_p1.py](../../scripts/demo_p1.py)：本地构建、加载和查询入口。
