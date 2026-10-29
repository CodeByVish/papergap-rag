# P5 → 全组：demo 服务（方案 C）交接

日期：2026-10-29　分支：`p5/demo-service`　状态：集群实测通过

**一句话**：demo 采用"集群实时服务 + 笔记本 UI"。服务是 `src/generation/server.py`
的 FastAPI 包装，内部只调用 `answer_record`，所以 demo 和 P6 runner 走的是同一条
生成/校验路径。已在集群用真实 vLLM 验证：warmup 7.4 s，一条回答 14.7 s。

本文件按人分节。只有 P6 需要改代码；P4 不需要动作；P2/P3 各有可选配合项。

---

## 新增与修改的文件

| 文件 | 说明 |
|---|---|
| `src/generation/server.py` | 新增：FastAPI 服务，端点 `/answer`、`/health`、`/papers`、`/passages` |
| `scripts/cluster/80_demo_server.sbatch` | 新增：集群启动作业，自动识别 `src.generation.server` 或 `nlp_p5.server` |
| `scripts/smoke_demo_server.py` | 新增：真实 socket 冒烟，15 项检查，不需要 GPU |
| `scripts/capture_demo_responses.py` | 新增：生成 UI 状态样本 |
| `scripts/demo_client.py` | 新增：笔记本侧客户端，一条命令跑完 health/answer/passages |
| `tests/test_server.py` | 新增：22 个测试（真实 ASGI，含 429 并发） |
| `examples/demo_ui_responses.json` | 新增：12 个真实捕获的 UI 状态 |
| `docs/DEMO_OPTION_C.md` | 新增：架构、隧道、演示当天清单、故障表 |
| `docs/P6_UI_CONTRACT.md` | 新增：P6 UI 的字段级契约 |
| `requirements.txt` | 追加 `fastapi`、`uvicorn`（纯 Python，不动 torch） |

---

## 致 P6（Changyan）— 影响最大，需要改代码

**现状**：`src/ui/app.py` 现在调用 `src.generation.llm_client.generate(...)`
（OpenAI 风格的外部 provider），并在 `src/ui/services.py` 里直接构造进程内检索器，
prompt 来自 `src/generation/prompting.py`。这条路径和 P5 的 pipeline 是两套实现。

**demo 改为 HTTP 调用**，服务返回 P5 的冻结记录：

| 端点 | 用途 |
|---|---|
| `POST /answer` | 传 `{"record": {...}}` 或 `{"question", "paper_id"}` |
| `GET /health` | 状态徽章、能力开关（`retrieval` / `passage_text`） |
| `GET /papers` | 论文选择器数据源 |
| `POST /passages` | citation 哈希 → 原文 |

**必须注意**：

1. `/answer` 和 `/passages` 需要 `Authorization: Bearer <token>`，token 由 P5 演示当天给出；
   `/health`、`/papers` 不需要。建议环境变量 `P5_API_BASE`、`P5_API_TOKEN`，不要写死。
2. **refusal 是 200**，不是错误码；用 `result.evidence_status` 判断。
3. `validation.downgraded == true` 是**校验器拦截**，原文在
   `validation.raw_result.answer`，要单独展示，不能只显示"拒答"。
4. 一次只答一个，并发返回 429；p90 约 17 s，HTTP 超时 ≥ 120 s。
5. 没有流式输出；100 题没有 gold answer，UI 只能展示合规状态。

**开发不需要集群**（仓库根执行）：

```bash
python -m src.generation.server --backend mock
```

12 个状态样本在 `examples/demo_ui_responses.json`，契约见 `docs/P6_UI_CONTRACT.md`。

**`llm_client` 要不要留**：建议保留给 held-out 实验，但 demo 只能走服务这一条；
两套路径同时存在时，UI 展示的答案和评测记录的答案会悄悄分叉。最终用哪条需要全组决定
（我的建议：评测也统一到 `answer_record`，`llm_client` 只在需要外部 provider 时用）。

---

## 致 P4（Ananya）— 不需要动作

- `AgentState`、`build_agent_graph`、`run_system`、`answer_fn` 全部未改。
- 新服务只是 `answer_record` 的 HTTP 包装：返回 `request_id` + 五键 `result` +
  `validation` + `generation` + 可选 `agent`，与你的 harness 结果同构。
- 如果之后要跑 agent trace，直接复用这个服务即可，不要再写第二个 runner。

---

## 致 P2 — 代码不用改，两件可选配合

1. **自由提问**（当前 demo 不支持）：需要一个工厂函数，形式为
   `module:factory`，返回 `retriever(question, paper_id, top_k) -> hits`，
   hits 可以是你的嵌套 `{"passage": {...}}` 形状。启动时设
   `DEMO_RETRIEVER=模块:函数`，服务会在锁内串行调用它。
2. **原文解析范围**：`PASSAGES_FROM` 已支持直接指向你的 retrieval dump
   （服务端认 `retrieved_passages` 信封），所以 100 题里的 478 条 passage
   今天就能显示原文；全语料需要 `passages.jsonl`（见致 P3）。

---

## 致 P3 — 一个可选项

如果希望 `/passages` 能解析**全部**语料，把 `passages.jsonl`（32,073 条，
sha256 `abc42568…97790`）放到集群固定路径，服务用 `PASSAGES_FROM` 指向它即可。
不影响生成，不放也能演示（只是语料外 id 显示为 missing）。

---

## 所有人须知

- **回答契约不变**：`answer / citations / evidence_status / retrieval_rounds /
  provenance` 五键，`request_id` 是对齐键。
- **两套包路径不要混用**：共享仓库用 `src.generation...`，独立 P5 仓库用
  `nlp_p5...`。同一进程只用一套，否则 `isinstance` 和异常捕获会静默失效。
- **新增依赖只有 fastapi / uvicorn**，纯 Python，不能牵动 torch / transformers。
- **集群访问方式有变化**：本集群**不能** SSH 进计算节点（密码被拒，密钥也被拒），
  所以用单跳：服务绑 `0.0.0.0` + token，笔记本
  `ssh -N -L 8000:<节点>:18080 <user>@10.96.189.12`。不要再试 `ssh -J`。
- **演示由 P5 账号跑作业**（谁的账号跑，谁的配额；也只有账号主人能开隧道），
  见 `docs/DEMO_OPTION_C.md` §2.1。

---

## 验证记录

- 集群：job 48890 / TC2N01，`vllm` + `p5-grounded-qa-v7`，warmup 7.4 s，
  一条 AgentState 回答 `SUFFICIENT`、2 citations、`PROVENANCE_OVERSTATED` warning、
  14.7 s；`/passages` found=2 missing=0。
- 本地：独立仓库 561 tests；共享仓库 `tests/test_server.py` 22 passed，
  `scripts/smoke_demo_server.py` 15/15 通过。

## 待确认

1. **P6**：demo 是否统一走服务；`llm_client` 是否保留。
2. **P2**：是否提供 `module:factory` 形式的检索入口（决定自由提问能否演示）。
3. **P3**：`passages.jsonl` 是否放集群（决定 citation 原文覆盖全语料还是仅 dump）。
4. 演示账号与时间窗口（当前按 P5 账号、6 小时窗口准备）。
