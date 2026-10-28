# 第 4 周工作记录

[English](week-4-report-en.md) | **简体中文**

截至 2026/10/28

## UI 论文选择目录

完成轻量论文目录构建模块，从 `data/processed/papers.jsonl` 提取论文元数据，结合当前配置使用的 `data/processed/passages.jsonl` 生成可选论文和章节列表，供 UI 一次加载。目录仅收录实际存在 passage 的论文和章节；这里的可检索表示有 passage 可参与检索，不保证每次查询命中。UI 接入尚未完成。

### 涉及代码

| 代码路径 | 职责 |
| --- | --- |
| `src/data/build_paper_catalog.py` | 提供 `build_paper_catalog()`，读取论文与 passage，校验 ID 唯一、正文非空和论文／章节引用，汇总各论文及章节的 passage 数。 |
| `scripts/build_paper_catalog.py` | 提供命令行入口，显式接收 `--passages`，写出 UTF-8 JSON，并拒绝覆盖已有输出。 |
| `tests/data/test_paper_catalog.py` | 覆盖来源顺序、同名章节合并、缺失元数据、空语料、重复 ID、无效引用、空正文和输出保护，共 $9$ 项测试。 |

### 成果文件与字段

本地成果为 `data/processed/paper_catalog.json`，包含 $1{,}168$ 篇可选论文、$16{,}187$ 个论文／章节名条目，覆盖所选语料的全部 $21{,}360$ 条 passage。生成文件保持在 Git 忽略范围内，本次未发布数据 Release。

目录顶层包含 `schema_version`、`passages_file` 和 `papers`；协议仍为 `v0-proposed`，`passages_file` 记录本次使用的 `data/processed/passages.jsonl`。每篇论文包含 `paper_id`、`title`、`authors`、`passage_count` 和 `sections`；每个章节包含 `name` 和 `passage_count`。字段类型、含义、构建命令及本地复现／Release 使用流程见 `data/README.md` 的[目录章节（英文）](../../data/README.md#dataprocessedpaper_catalogjson)及 `data/README_zh-CN.md` 的[对应章节（中文）](../../data/README_zh-CN.md#dataprocessedpaper_catalogjson)。

章节按原文首次出现顺序排列，规范化后同名的章节合并计数；各章节计数之和等于论文计数。缺失或空白字符串使用 `null`，缺失作者列表使用 `[]`，不推测补写；当前 QASPER 导出未提供作者。UI 检索必须使用 `passages_file` 所记录的同一份语料，替换语料后须重建目录。

### 验证结果

独立读取已保存的目录和 passage 语料，核验论文 ID 唯一、全部论文／章节计数一致，以及总 passage 数完整覆盖。新增 $9$ 项测试通过，全量 $530$ 项测试通过；字符检查、Python 语法检查和 Ruff 检查通过。全量测试命令如下，显式指定仓库内的临时目录以避开旧临时目录的访问限制：

```powershell
python -m pytest tests -q --basetemp tmp/tmp_pytest_week4_catalog --tb=short
```
