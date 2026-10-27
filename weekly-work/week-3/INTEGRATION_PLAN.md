# 分块实验代码整合清单

对应 `TODO.md` 的 `2.2.2.1`／`2.2.2.2`。2026/10/27 已按下述固定快照完成四种静态模式整合及离线验收；$473$ 项测试通过。配置、适配模块、新增测试和运行说明已落地；后续 `2.3` 已完成真实数据 BM25 试运行，其他模式的真实模型验证仍未执行。以下保留来源、设计约定和验收清单，最新完成状态、试运行产物及下一步见 `HANDOFF.md`。

共享范围更新：用户已确认将 Week 3 四份文档提交并推送，`weekly-work/` 的整体忽略规则已移除。下文关于本地记录及不提交的约定仅描述代码整合阶段当时的范围。

## 结论与范围

本次指标只需要分块、检索和人工可读性评审。最小接入是用 P1 的 `BM25Retriever` 替换实验内的临时 BM25 实现；完整静态检索接入 P1 dense、P2 RRF 和运行时可选的 BGE 重排。P4 Agent、P5 生成模型和 P6 UI 均不属于这四项指标的依赖，因此本次无需部署 P5 的 Qwen。

为避免执行时重新设计范围，本清单将代码交付定为：先接通 P1 BM25，再接通可选择的 `dense`、`hybrid` 和 `hybrid_rerank`，用离线替身验证全部四种模式。默认仍为 `bm25`；实现某种模式不代表已选择它作为正式实验方法，也不要求为完成代码整合下载模型。正式比较时固定一种检索模式及全部检索参数，只改变 chunk size；不能把不同检索模式的结果当作纯分块大小比较。

## Sol Medium 执行约定

- 在现有 `p3-qasper-foundation` 工作区内完成本项。开始时读取本文件、`AGENTS.md`、`CONTRIBUTING.md`、`experiments/chunk_size/README.md` 和相关测试；核对 `git status --short --branch`、`git rev-parse HEAD`。当前审核基线为下节的 P3 提交；若有后续提交或用户修改，先核对受影响文件，保留已有改动。
- 使用固定提交取文件，不直接 merge main、不 cherry-pick 包含其他 part 的整笔提交，也不切换到来源分支。先用 `git diff HEAD <source-sha> -- <path>` 检查同名文件，再用 `git restore --source=<source-sha> --worktree -- <明确的文件列表>` 引入；只允许下表列出的路径，不覆盖 P3 评估、数据、说明、忽略规则或依赖文件。
- 下列主干快照是可复现来源；`git fetch` 后 `origin/main` 可能移动，不因此自动更换来源。若指定对象本地不存在，先 fetch 以取得对象，再按固定 SHA 读取；确需改用新快照时重新检查文件和依赖，并更新本清单。
- 复用已有项目 Python 环境。当前本机环境为 `D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe`；先检查版本和所需包，再运行命令。本文后续 `python` 均指该环境，不使用 PATH 中可能指向 Anaconda base 的解释器。
- 任务终点是可审查的本地代码、配置、说明和通过记录；本次不要求提交、推送或合并。以后提交或推送前按 `CONTRIBUTING.md` 和 `verify-before-push` 执行。`weekly-work/` 已被 Git 忽略，更新本清单及本地交接即可，不强制加入共享提交。

## 已核对的分支

初次清单记录于 2026/10/27，已执行 `git fetch origin`；本次复审使用本地已有的固定对象，未再次 fetch。P3 当前基线为 `p3-qasper-foundation@0640cb1e3a2fe50e11c0eb2bafc84758b4520f57`。下表是该次来源快照及合并关系；若执行时改用其他快照，应重新检查差异。

| Part | 分支与快照 | 代码核对结果 |
| --- | --- | --- |
| 已合并公共代码 | `origin/main@5ccfb070a00f71dd2f95f69afb31868c296f35c4` | 包含 P1 基础检索、P2 融合／重排／缓存／评估工具和 P4 Agent；本次优先从这里取已合并的检索代码。 |
| P1 | `origin/p1/retrieval@5d3f4477f42887067bb4b3f8bd9231f1bc9289e9`；`origin/p1/week3-week4@6828629debe89e73740a3f49037bc98bb8c65143` | 前者已进入 main；后者尚未进入 main，额外提供原生 section 过滤、BM25 保存／加载、独立实验和评估适配。本次不依赖这些增量。 |
| P2 | `origin/p2/batch-hybrid-handoff@314f29c401f2ebb78e60092143a75c660aaa176d`；`origin/p2/agent-sections-cache@25f85be131f2db558f64c8e2dfc88a89d82b05bf`；`origin/p2/evaluation-pooling@fe92df2a017907f81753387852d046aeb09ff970` | 三个分支均已进入 main。最新分支的检索、评估和脚本目录与 main 一致，无需重复取多个历史版本。 |
| P4 | `origin/p4-agent-skeleton`、`origin/p4/week2-planner`、`origin/p4/week3-critic`、`origin/p4/week5-rewriter`、`origin/p4/week6-smoke-test`、`origin/p4/week7-qwen-critic`、`origin/p4/tracker-update` | 均已进入上述 main；已核对 graph、nodes、experiments 和 Qwen client 的调用边界。本次不运行规划、critic 或重试。 |
| P5 | `origin/p5/generation-integration@11b3639c8a7ac7fe8d17435b3f7b8df52adae44f` | 尚未进入 main；提供 `src/generation/`、检索到生成的适配、Transformers／vLLM／mock 后端。本次指标不调用生成。 |
| P6 | `origin/P6_StreamlitUI@82f95d4400ec7c3b0433b16204304bf59f41c0b2` | 尚未进入 main；提供 Streamlit、LLM client 和另一套索引适配。该适配使用 `chunk_id`、`section_path`，检索接口无 `paper_id` 参数，不能直接替换 P3 的按论文检索。 |

另已检查 `origin/docs/project-plan-and-starter-files`，该历史文档分支已进入 main，无额外实验代码。以上合并状态使用 `git branch -r --merged origin/main` 和 `--no-merged origin/main` 核对。

## 从其他分支引入的文件

下表的来源统一固定为 `5ccfb070a00f71dd2f95f69afb31868c296f35c4`，目标分支为 `p3-qasper-foundation`。按列出的文件引入，并保留 P3 现有分块评估实现。先完成最小接入，再补齐其余行；“混合检索”是第二阶段的代码范围，运行时仍按所选模式加载。

| 范围 | Part | 来源代码／文件 | P3 目标位置 | 用途 |
| --- | --- | --- | --- | --- |
| 最小接入 | P1/P2 | `src/retrieval/schemas.py` | 同路径新增 | P1 的 `RetrievalHit`、P2 的 `RetrievedPassage` 及其嵌套 passage 模型。保留现有 `src/data/schemas.py`。 |
| 最小接入 | P1 | `src/retrieval/bm25_retriever.py` | 同路径新增 | 按论文构建 BM25，保留 passage ID，按分数和 ID 排序。 |
| 混合检索 | P1 | `src/retrieval/dense_retriever.py` | 同路径新增 | BGE embedding、按论文 FAISS cosine 检索及索引保存／加载。每种 chunk size 单独建索引。 |
| 混合检索 | P2 | `src/retrieval/fusion.py` | 同路径新增 | 对 BM25／dense 的排名做 RRF，并按 passage ID 去重。 |
| 混合检索 | P2 | `src/retrieval/hybrid_retriever.py` | 同路径新增 | 连接两个检索器，返回融合或重排后的前若干条结果。 |
| 混合检索 | P2 | `src/retrieval/reranker.py` | 同路径新增 | `hybrid_retriever.py` 直接导入这里的 `PairScorer`、`rerank`，所以即使关闭重排也需要此文件。BGE 权重只在实际评分时加载。 |
| 缓存 API 配套 | P2 | `src/retrieval/score_cache.py` | 同路径新增，随重排模块保留 | 保持上游 `BGEReranker.cached()` 可用；本次实验适配不调用它，持久评分缓存固定关闭。 |
| 匹配上游测试 | P1/P2 | `scripts/build_indexes.py`、`scripts/demo_p1.py`、`scripts/demo_hybrid.py` | 各自同路径新增 | 下列上游测试依赖这些模块；同时提供模型 revision 常量和单次诊断入口。它们不替代 P3 比较入口。 |
| 匹配上游测试 | P1/P2 | `tests/test_p1.py`、`tests/test_p2.py`、`tests/test_hybrid_cli.py` | 各自同路径新增 | 检索、融合、重排、索引一致性和 CLI 回归。BM25 阶段先补聚焦用例；完整导入这些测试需要上面的混合检索模块及脚本，`test_p1.py` 顶层就导入 FAISS／dense／hybrid，不能用 `-k bm25` 绕开缺失依赖。 |
| 测试数据 | P1/P2 | `tests/fixtures/mock_passages.jsonl`、`tests/fixtures/mock_retrieval_results.json` | 各自同路径新增 | 上述测试直接读取的小型合成 fixture。 |

上游 `src/retrieval/__init__.py` 为空，P3 已有该文件，无需替换。P3 和 main 的 `src/data/`、`requirements.txt`、`requirements-dev.txt` 当前无差异，无需重复导入。

## P3 连接代码

除引入检索文件，以下连接代码也已实现，使 `scripts.evaluate_chunk_size` 能按配置调用它们。

| 来源／现有入口 | P3 目标位置 | 具体改动 |
| --- | --- | --- |
| P1/P2 检索 API；P3 的 `RetrieverFactory` | 新增 `src/evaluation/chunk_size_retrieval.py` | 为每个候选语料创建独立检索器，将 P1/P2 返回对象按原排名转成 `(passage_id, score)`。只向检索器传问题文本、论文 ID 和检索参数。 |
| `run_chunk_size.py::build_candidate` 的候选记录 | 上述新适配模块 | 先明确投影公共八字段，并经 P3 `Passage` 校验，再用字典创建 retrieval `Passage`。私有 `spans` 留在评估侧；两种模型都禁止额外字段，不能直接传整条候选记录，也不能直接混用两个模型实例。 |
| `run_chunk_size.py::run_comparison` | `src/evaluation/run_chunk_size.py` | 接入 factory 与 `retriever_metadata`，保留已有自定义 factory 入口；保留抽样、证据覆盖、词数和可读性汇总。将 `local_bm25` 保留为委托 P1 适配的兼容包装，不再维护第二套 BM25 算法。 |
| P3 数值配置与 CLI | `experiments/chunk_size/config.json`、`src/evaluation/run_chunk_size.py::load_config`、`scripts/evaluate_chunk_size.py` | 按下节格式增加可选 `retrieval` 配置；未配置时使用 P1 BM25。CLI 继续用已有 `--config` 选文件，无需另加模式参数和优先级。同步 CLI 说明及预期依赖／模型错误的提示，保留 `run`、`summarize` 和已有参数。 |
| P1/P2 模型常量与实际运行参数 | 适配模块及现有 `manifest.json` 生成逻辑 | 记录来源提交和实际生效参数，细节见下节；运行逻辑不得为读取常量而依赖 `scripts.*`，在适配层集中维护模型 SHA，并在传参测试中确认实际转发的值。 |
| P3 现有评估测试 | `tests/evaluation/test_chunk_size.py`；新增 `tests/evaluation/test_chunk_size_retrieval.py` | 验证去除私有字段后 ID／文本保持不变、按论文检索、空结果、分数转换和不同大小独立建索引；用 fake encoder／scorer 验证连线，保留现有异常结果检查。 |
| P3 运行文档 | `experiments/chunk_size/README.md`、`README.md` | 同步实际配置、命令、依赖与接入状态；只有评估规则改变时才同时更新 `criteria.md` 和 `criteria_zn-CN.md`。 |
| 项目建议配置 | `configs/default.yaml` | 当前无运行入口读取此文件，本次不需要修改。实验配置唯一入口是 `experiments/chunk_size/config.json` 或 CLI 的 `--config`；不能只改 YAML 就声称参数已生效。 |

分数转换规则：P1 结果使用 `score`；P2 结果使用非空的 `reranker_score`，否则使用 `rrf_score`。判断必须用是否为 `None`，因为重排分数为零或负数也有效。保持返回排名，继续由 `retrieve_question` 拒绝重复 ID、错误论文、未知 ID、非有限分数和超过 top-$5$ 的结果。

## 适配、配置和记录的明确约定

### 适配与构造顺序

1. 公共字段只取 `passage_id`、`paper_id`、`title`、`section`、`chunk_number`、`text`、`previous_passage_id`、`next_passage_id`。先 `src.data.schemas.Passage.model_validate(public_record).model_dump()`，再构造 `src.retrieval.schemas.Passage`；使用明确的类别名区分两者。禁止重算 ID、截断或改写文本、把问题／答案／证据混入索引。原候选记录及 `spans` 保持不变，以便按返回 ID 回查评估。
2. 从校验后的 `retrieval` 设置创建 factory；factory 每接收一份候选语料，就为该大小创建独立 BM25／dense 索引。返回的 callable 必须接受 `(query, paper_id, top_k)`，内部将上游对象转成有序 `(passage_id, float(score))`，不重新按转换后的分数排序。适配模块不反向导入 `run_chunk_size.py`，避免与 runner 形成环依赖。
3. `bm25` 只构造 `BM25Retriever(passages)`；`dense` 只构造 `DenseRetriever(passages, **dense_settings)`。这两种模式直接取 top-$5$，不经过 RRF。
4. `hybrid` 构造 BM25 和 dense，再传入 `HybridRetriever(sparse.retrieve, dense.retrieve, scorer=None, candidate_k=..., rrf_k=...)`。`hybrid_rerank` 额外构造 `BGEReranker(**reranker_settings)` 作为 `scorer`。`candidate_k` 是每个来源的候选数；先 RRF 去重，再对全部融合候选重排，最后取 top-$5$，不是先裁成 $5$ 条再重排。两个来源各取 $20$ 条时，重排最多处理 $40$ 条。
5. 按模式延迟导入和构造依赖：BM25 路径不导入 FAISS、SentenceTransformers、Torch 或 Transformers；`hybrid` 不构造 BGE scorer，`summarize` 不加载任何检索模型。测试使用可注入或可 monkeypatch 的 encoder／scorer；替身必须声明自己的身份，不能在元数据中冒充真实 BGE。
6. 保留 `run_comparison(retriever_factory=..., retriever_metadata=...)` 的现有扩展入口。有 custom factory 时仍必须提供 metadata，实际检索来源以 custom factory 为准并明确记录；不得把配置里的 BM25／BGE 描述套到替身上。仅传 metadata 而不传 custom factory 应报错，避免描述与实际实现不符。
7. 每个大小处理完释放不再使用的检索器和索引，避免同时保留多套 dense 模型及 FAISS。允许复用同一版本的只读模型权重，不复用不同候选语料的行号、passage 映射或索引。首版直接建内存索引，不新增跨运行索引复用或持久评分缓存。

### 配置格式与校验

保留当前全部分块键，在默认 `config.json` 中显式加入 `"retrieval": {"mode": "bm25"}`。旧配置缺少 `retrieval` 时也归一化成同一 BM25 设置。四个合法模式名称固定为 `bm25`、`dense`、`hybrid`、`hybrid_rerank`。下例是已支持的完整重排模式配置，便于验证和测试；不是本次选定的正式实验配置。

```json
{
  "candidates": [150, 200, 250],
  "overlap_words": 40,
  "top_k": 5,
  "question_sample_count": 50,
  "readability_sample_count": 10,
  "question_seed": 42,
  "readability_seed": 43,
  "retrieval": {
    "mode": "hybrid_rerank",
    "candidate_k": 20,
    "rrf_k": 60,
    "dense": {
      "revision": "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a",
      "device": "cpu",
      "batch_size": 32,
      "cache_folder": ".cache/huggingface",
      "local_files_only": true
    },
    "reranker": {
      "revision": "2cfc18c9415c912f9d8155881c133215df768a70",
      "device": "cpu",
      "batch_size": 8,
      "max_length": 512,
      "cache_folder": ".cache/huggingface",
      "local_files_only": true
    }
  }
}
```

- 上例各检索参数作为缺省值；唯独 `mode` 缺省为 `bm25`。按嵌套对象补默认值，不用浅合并覆盖整段。配置根对象及 `retrieval`、`dense`、`reranker` 对象都拒绝未知键、非对象或 `null`；其余原有分块校验继续保留。
- `candidate_k`、`rrf_k` 和两个 `batch_size` 必须为正整数，拒绝布尔值；hybrid 两种模式的 `candidate_k` 不小于 `top_k`。重排 `max_length` 为 $1$ 至 $512$ 的整数；两类 `revision` 为 $40$ 位小写十六进制 SHA；`local_files_only` 必须是布尔值。设备和缓存路径为非空字符串，缓存相对路径从项目根目录解析并记录实际路径；设备不使用自动选择。未使用的段仍校验，但不加载相应依赖或模型。
- P1 dense 构造函数没有 `model_name`、`max_seq_length` 或 query instruction 参数；它们固定为下表的上游值，不把这些额外键展开传入构造函数。BM25 的 `k1`、`b`、`epsilon` 也保持上游缺省值；本次不扩展公共 API。BGE scorer 使用固定 `BAAI/bge-reranker-base`，其余参数按示例转发。
- 默认离线加载模型，测试不得自动联网。真实试运行缺少依赖、指定 revision 缓存或设备时，明确报错并保留失败记录；不能悄悄降级成 BM25、改用其他 revision，或为继续运行而自动下载模型。需要下载时使用独立的准备步骤；若主动设置 `local_files_only=false`，在运行说明和 manifest 中记录。

### Manifest 与计时

- 保留现有输入哈希、`question_ids`、可读性位置、语料哈希、依赖和代码状态。`manifest.config` 保存补齐默认值后的配置；`manifest.retriever` 描述实际活动的实现，包括导入来源 SHA、模式、包版本、评分含义、论文范围和排序规则。未启用的 dense／reranker 在活动元数据中标为未启用，不声称加载或验证过模型。
- dense 活动元数据包括模型名／SHA、tokenizer 对应 SHA、完整 query instruction、`max_seq_length=512`、L2 normalization、cosine／`IndexFlatIP`、设备、batch size 和离线策略。reranker 包括模型／tokenizer SHA、设备、batch size、`max_length`、padding／truncation 和 raw logits。hybrid 另记 `candidate_k_per_source`、`rrf_k`、全候选重排及最后 top-$5$；持久评分缓存为关闭。
- 每个大小的 `summary.sizes[size].index_seconds` 包括该次 factory 构造、模型初始化及编码建索引；现有逐问题 `retrieval_seconds` 继续覆盖整次检索。首版不增加隐藏 warm-up；BGE 首次评分的延迟加载会计入首题时间，在 `timing_policy` 中明确说明。不得照抄上游 demo 的“已 warm-up、排除加载”描述，也不根据这些单次时间作性能结论。
- 截断只发生在模型内部，报告和词数仍使用完整 chunk。记录 dense 的单文本限制和 reranker 的 query–passage pair 限制；真实模型试运行时用相应 tokenizer 检查代表性长 chunk／问题对，把观察结果写入本地试运行记录。尚未检查时写明未验证，不编造截断数量或比例。

## 模型、依赖和运行边界

| 项目 | 已核实的上游设置 | 后续处理 |
| --- | --- | --- |
| BM25 | `rank-bm25`；Unicode `\w+`、`casefold`；`k1=1.5`、`b=0.75`、`epsilon=0.25` | 不下载模型，适合先做本地真实数据试运行。 |
| Dense | `BAAI/bge-small-en-v1.5`；revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`；最大序列长度 $512$ tokens | 引用 P1 已有 checkpoint；记录 query instruction、L2 normalization 和 cosine 设置。 |
| RRF | `candidate_k=20`、`rrf_k=60` 是现有起始值 | 全部 chunk sizes 保持相同；不在同一轮分块比较中同时调整它们。 |
| BGE 重排 | `BAAI/bge-reranker-base`；revision `2cfc18c9415c912f9d8155881c133215df768a70`；默认 `batch_size=8`、`max_length=512` | 仅在选择重排模式时下载／加载。它是检索重排模型，不是 P5 的生成模型。 |
| Python 依赖 | P3 已列出 `numpy`、`pydantic`、`rank-bm25`、`sentence-transformers`、`faiss-cpu`、`torch`、`transformers`、`pytest` 等 | 列出不等于当前环境都已安装；整合时检查实际版本。第二阶段接入重排代码时，将 main `requirements-p2.txt` 中的 `sentencepiece>=0.2,<1` 合入 P3 `requirements.txt`，无需复制整套依赖文件。 |

词数仍按现有 chunker 计算，不能把 $150/200/250$ words 改成 tokens。BGE 编码和重排有 token 长度限制；选择这些模式时，试运行需检查截断并记录策略，报告中的 retrieved word count 仍统计完整返回 chunk 文本。

保留 P3 的 `papers.jsonl`、`qa.jsonl` 和导出校验入口，只使用原始 `train/validation` 的问题选择分块配置。每个大小从自己的候选语料建索引，不复用默认 $200$ words 的旧索引或其他同学已有的检索结果。模型、索引、缓存和运行结果留在已忽略的本地目录；共享 schema、划分和输出继续标记为 `v0-proposed`。

## 本次不引入的代码

| Part | 已浏览的代码／文件 | 原因 |
| --- | --- | --- |
| P1 后续增量 | `origin/p1/week3-week4` 的 `src/retrieval/experiment.py`、`evaluation.py`、`agent_integration.py`、`scripts/run_p1_experiment.py`、`run_p1_integration.py`，以及 BM25／dense 的 section 和保存增量 | 独立实验入口限 train，评估依赖外部 relevance labels；本次已用 P3 入口处理 development/validation、证据原文和人工评审。当前无需 section 过滤或 BM25 持久化。 |
| P2 批处理／通用评估 | main 的 `scripts/batch_hybrid.py`、`benchmark_p2.py`、`retrieval_ablation.py`、`prepare_p2_pilot.py`、`prepare_p2_annotations.py`，以及 `src/evaluation/retrieval.py`、`pooling.py` | 用于独立检索消融、排名指标和标注池，不能直接生成本次要求的段落覆盖／可读性报告。保留作后续实验参考，不替换 P3 的评估模块。 |
| P2 section／Agent 测试 | `src/retrieval/scoped.py`、`scripts/run_hybrid_agent.py`、`tests/test_p2_sections_cache.py` | 当前不需要 section／Agent；该测试文件在模块加载时导入 P4 graph，不能靠筛选测试名称消除依赖。若以后启用评分缓存，应把纯缓存用例提取到独立测试文件。 |
| P4 | main 的 `src/agent/`、`scripts/run_agent_demo.py`、`evaluate_planner.py`、`smoke_agent_real.py` | 规划、critic 和多轮改写会引入额外实验变量，不是当前静态 top-$5$ 指标的依赖。 |
| P5 | `origin/p5/generation-integration` 的 `src/generation/`、`scripts/generate_from_retrieval.py`、`smoke_test_qwen3.py`、`scripts/cluster/` | 本次不计算答案质量或生成指标，因此无需本地大模型、集群或 mock 生成后端。 |
| P6 | `origin/P6_StreamlitUI` 的 `src/ui/`、`src/retrieval/indexed_retriever.py`、`src/generation/llm_client.py`、`prompting.py`、`scripts/build_dense_index.py`、`export_pyserini.py` | UI／另一套语料和索引接口不满足当前按论文检索边界；不引入 Pyserini、Java 或外部 LLM API 依赖。 |

main 的 `AGENTS.md` 仍是旧的文档语言规则，`.gitignore` 缺少 P3 的 `/tmp/`；不要用它们覆盖当前 P3 文件。上游说明可查阅 main 的 `docs/P2_WEEK2.md` 和 `docs/P2_AGENT_CACHE.md`，本次操作说明集中维护在 P3 的实验 README。

## 后续执行与验收

### 第一阶段：接通 BM25

- [x] 引入 retrieval schema 和 P1 BM25，完成公共字段投影、兼容包装和 factory 接入。旧配置及默认 CLI 都实际调用 P1；运行结果不再标为 `experiment-local-paper-bm25-v1`。
- [x] 实现配置归一化和校验，保留 custom factory 入口，用现有合成导出 fixture 跑完整 `run`、产物检查和 `summarize`。保留无效检索结果、原始 test 问题排除、证据覆盖和人工标签异常检查。
- [x] 更新实验 README 的 BM25 状态；`tests/evaluation` 和 `tests/data` 已随完整接入一起验收。

### 第二阶段：补齐静态检索代码

- [x] 引入表中其余文件及 `sentencepiece` 依赖，接通另外三种模式。关闭重排时不创建 scorer；关闭 dense 时不导入重依赖。完成所有模式的实际活动元数据和错误提示。
- [x] 在 `tests/evaluation/test_chunk_size_retrieval.py` 及现有评估测试中覆盖下表行为。替身测试经配置分发进入真实适配层，保留真实 BM25、FAISS、融合和重排逻辑。

| 验证范围 | 最少验收行为 |
| --- | --- |
| Schema 与 ID | 含 `spans` 的候选能正确投影；八字段、ID、文本和原始记录不变；违规公共字段报错。 |
| P1 适配 | BM25／dense 分别保留上游顺序、ID 和分数；未知论文返回空列表；少于 $5$ 条时不补齐，不跨论文。 |
| P2 适配 | RRF 分数正确取出；重排分数为 `0.0`、负值及 `None` 时选择正确；重排看见全部去重候选，最后才取 top-$5$。 |
| 参数转发 | 真实 dense 检索逻辑配 fake encoder；真实 hybrid／rerank 逻辑配 fake scorer；检验前缀、revision、batch、设备、长度和离线设置转发，不下载权重。 |
| 语料隔离 | 每个 chunk size 的索引接收自己的候选 ID／文本；结果只来自该份语料。不能只数 factory 调用次数。 |
| 配置与扩展 | 旧配置、四种模式、嵌套缺省值和非法值；custom factory＋metadata 仍可使用，实际来源记录正确。 |
| 端到端产物 | 同一份合成导出分别用四种模式跑比较；每种模式内部各大小的 `question_ids` 和可读性原文位置一致；指标能追溯至返回 ID 及 `spans`，manifest 与实际模式一致。 |
| 轻量路径与失败 | 新进程中默认 BM25 不导入重依赖；`summarize` 不加载模型；缺模型／设备报错且不降级；失败目录没有完成标志 `manifest.json`，已有 run 不被覆盖。 |

参数转发测试应拦截实际构造或模型加载调用；fake encoder 自身不接收 `device`／`batch_size`，只用 fake encoder 检索不能证明这些参数已转发。可复用上游测试中的 loader stub。上游 `test_p2_sections_cache.py` 仍不导入本次范围。

- [x] 已用项目环境完成字符扫描、语法／编译、Ruff、完整测试和差异检查。下列为复核命令，最新测试使用的 basetemp 为 `tmp/tmp_pytest_chunk_integration_final`。

```powershell
python -m pytest tests/test_p1.py tests/test_p2.py tests/test_hybrid_cli.py tests/evaluation tests/data -q --basetemp tmp/tmp_pytest_chunk_integration -p no:cacheprovider --tb=short
python -m compileall -q src/retrieval src/evaluation scripts
python -m ruff check --no-cache src/retrieval src/evaluation scripts tests/evaluation tests/test_p1.py tests/test_p2.py tests/test_hybrid_cli.py
git diff --check
git status --short --branch
```

- [x] 将实际配置、四种模式、模型准备／离线错误、API 和运行状态同步到 `experiments/chunk_size/README.md` 及根 README；四项指标和双语 criteria 的含义保持一致。引入文件和新增适配／测试均已纳入未跟踪文件复核。
- [x] 全部通过后勾选 TODO 的 `2.2.2.2`，更新本地 HANDOFF；真实试运行和正式评估仍未勾选，真实模型明确标为未验证。

### 第三阶段：真实数据试运行与正式运行

这是后续 TODO 的 `2.3`／`2.4`，不包含在本次代码整合完成状态中。整合后先核对真实导出，再创建 `tmp/tmp_chunk_smoke_bm25.json`：复制实际默认配置，仅将问题数改为 $3$、可读性原文数改为 $2$、模式显式设为 `bm25`；仍比较 $150/200/250$ words。临时文件全部放 `tmp/`，修改后从磁盘复读。

```powershell
python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
python -m scripts.evaluate_chunk_size run --config tmp/tmp_chunk_smoke_bm25.json --run-id smoke_p1_bm25_01
python -m scripts.evaluate_chunk_size summarize --run-dir results/chunk_size/smoke_p1_bm25_01
```

上述命令需在配置文件写好且前一条成功后运行，已有 run ID 就换新 ID。检查 `manifest.json` 最后写出、实际 P1 身份、相同问题／原文位置、每大小的两份 Markdown 及 `summary.json` 一致。未人工评分时，`summarize` 成功但可读性仍为 `null`；不要自动填 `pass` 来通过验收。

减少问题数只减少查询，不减少 `run_comparison` 为全部 train/validation 论文建候选和索引的工作量。BM25 可先验证完整 CLI；dense／重排先用已验证的 development `sample_passages_100.jsonl`，通过引入的 `scripts.build_indexes` 和 `scripts.demo_hybrid` 检查模型加载及单次查询，保存到独立的本地索引／诊断目录。这份默认 $200$-word 样本只用于诊断，不能作为三种大小的正式比较索引；之后按吞吐量和资源决定完整比较，不能把少量问题试跑称为少量论文建索引。

若正式选 dense／hybrid／hybrid_rerank，则还必须按所选配置完成实际模型的 P3 比较入口试运行，检查 SHA、缓存、各大小独立索引、截断和产物，再将 `2.3` 标为该模式已验证。BM25 试跑成功只能证明 BM25；尚未准备好其他模型时可继续保留其未验证状态，正式模式仍待确定。

试运行通过后才进入 `2.4`：确认并固定正式模式、模型版本、样本量、种子和检索参数，每轮使用新 `run_id`，完成人工可读性评审后汇总。当前没有正式指标或最优 chunk size 结论。

## 代码整合验证记录

2026/10/27 代码整合时使用本机项目 Python 执行下列完整检查，结果为 $473$ passed。模型加载器使用离线替身，真实检索、FAISS、融合和重排逻辑参与测试；测试产物明确声明替身身份。字符扫描、`compileall`、Ruff 和 `git diff --check` 均通过。当次已在现有环境安装 `sentencepiece==0.2.2`，未下载权重、运行真实数据实验、提交或推送；后续真实数据 BM25 试运行记录见 `HANDOFF.md`。

```powershell
& 'D:/Apps/Programming/Anaconda/virtue_envs/papergap-rag/python.exe' -m pytest tests/test_p1.py tests/test_p2.py tests/test_hybrid_cli.py tests/evaluation tests/data -q --basetemp tmp/tmp_pytest_chunk_integration_final -p no:cacheprovider --tb=short
```
