# Round 4 validation

Primary: complete evidence rate at $1000$ words, declared before retrieval. New questions are the main validation group; regression and combined groups are reported separately.

| Group | Size (words) | Budget | Evidence hit | Complete evidence | Mean actual words | Exhausted |
| --- | --- | --- | --- | --- | --- | --- |
| combined | $325$ | $500$ | $115/250$ | $91/250$ | $500.00$ | $0$ |
| combined | $325$ | $1000$ | $152/250$ | $129/250$ | $999.28$ | $1$ |
| combined | $325$ | $2000$ | $203/250$ | $186/250$ | $1959.52$ | $24$ |
| combined | $365$ | $500$ | $111/250$ | $86/250$ | $500.00$ | $0$ |
| combined | $365$ | $1000$ | $156/250$ | $128/250$ | $999.28$ | $1$ |
| combined | $365$ | $2000$ | $211/250$ | $191/250$ | $1958.56$ | $24$ |
| combined | $375$ | $500$ | $112/250$ | $87/250$ | $500.00$ | $0$ |
| combined | $375$ | $1000$ | $156/250$ | $129/250$ | $999.28$ | $1$ |
| combined | $375$ | $2000$ | $208/250$ | $191/250$ | $1958.40$ | $24$ |
| new | $325$ | $500$ | $98/200$ | $75/200$ | $500.00$ | $0$ |
| new | $325$ | $1000$ | $123/200$ | $104/200$ | $999.10$ | $1$ |
| new | $325$ | $2000$ | $166/200$ | $152/200$ | $1957.38$ | $18$ |
| new | $365$ | $500$ | $97/200$ | $73/200$ | $500.00$ | $0$ |
| new | $365$ | $1000$ | $131/200$ | $106/200$ | $999.10$ | $1$ |
| new | $365$ | $2000$ | $171/200$ | $154/200$ | $1956.58$ | $18$ |
| new | $375$ | $500$ | $97/200$ | $74/200$ | $500.00$ | $0$ |
| new | $375$ | $1000$ | $131/200$ | $108/200$ | $999.10$ | $1$ |
| new | $375$ | $2000$ | $170/200$ | $155/200$ | $1956.58$ | $18$ |
| regression | $325$ | $500$ | $17/50$ | $16/50$ | $500.00$ | $0$ |
| regression | $325$ | $1000$ | $29/50$ | $25/50$ | $1000.00$ | $0$ |
| regression | $325$ | $2000$ | $37/50$ | $34/50$ | $1968.10$ | $6$ |
| regression | $365$ | $500$ | $14/50$ | $13/50$ | $500.00$ | $0$ |
| regression | $365$ | $1000$ | $25/50$ | $22/50$ | $1000.00$ | $0$ |
| regression | $365$ | $2000$ | $40/50$ | $37/50$ | $1966.50$ | $6$ |
| regression | $375$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| regression | $375$ | $1000$ | $25/50$ | $21/50$ | $1000.00$ | $0$ |
| regression | $375$ | $2000$ | $38/50$ | $36/50$ | $1965.70$ | $6$ |

| New questions: left / right | View | Metric | Left only | Right only |
| --- | --- | --- | --- | --- |
| 325 / 365 | top_5 | `evidence_hit_at_5` | $6$ | $15$ |
| 325 / 365 | top_5 | `complete_evidence_at_5` | $7$ | $14$ |
| 325 / 365 | 500 | `evidence_hit` | $10$ | $9$ |
| 325 / 365 | 500 | `complete_evidence` | $8$ | $6$ |
| 325 / 365 | 1000 | `evidence_hit` | $3$ | $11$ |
| 325 / 365 | 1000 | `complete_evidence` | $7$ | $9$ |
| 325 / 365 | 2000 | `evidence_hit` | $2$ | $7$ |
| 325 / 365 | 2000 | `complete_evidence` | $6$ | $8$ |
| 325 / 375 | top_5 | `evidence_hit_at_5` | $8$ | $15$ |
| 325 / 375 | top_5 | `complete_evidence_at_5` | $9$ | $14$ |
| 325 / 375 | 500 | `evidence_hit` | $10$ | $9$ |
| 325 / 375 | 500 | `complete_evidence` | $8$ | $7$ |
| 325 / 375 | 1000 | `evidence_hit` | $3$ | $11$ |
| 325 / 375 | 1000 | `complete_evidence` | $7$ | $11$ |
| 325 / 375 | 2000 | `evidence_hit` | $4$ | $8$ |
| 325 / 375 | 2000 | `complete_evidence` | $7$ | $10$ |
| 365 / 375 | top_5 | `evidence_hit_at_5` | $4$ | $2$ |
| 365 / 375 | top_5 | `complete_evidence_at_5` | $4$ | $2$ |
| 365 / 375 | 500 | `evidence_hit` | $1$ | $1$ |
| 365 / 375 | 500 | `complete_evidence` | $1$ | $2$ |
| 365 / 375 | 1000 | `evidence_hit` | $3$ | $3$ |
| 365 / 375 | 1000 | `complete_evidence` | $3$ | $5$ |
| 365 / 375 | 2000 | `evidence_hit` | $4$ | $3$ |
| 365 / 375 | 2000 | `complete_evidence` | $4$ | $5$ |

Top-5 metrics, exact paired question IDs, group paper IDs and split counts are in `summary.json`; `summary.html` shows all group aggregates. New questions may share papers with regression questions. Small differences do not establish significance or a stable optimum. Do not redraw the sample or continue a dense search on these questions. Readability is excluded from this assessment. The selected BM25 chunk size is $365$ words with $40$ words of overlap; the reasons are below. Shared interfaces remain `v0-proposed`.

## Top-5 results

| Group | Size (words) | Evidence hit | Complete evidence | Mean words |
| --- | --- | --- | --- | --- |
| combined | $325$ | $168/250$ | $144/250$ | $1172.33$ |
| combined | $365$ | $180/250$ | $154/250$ | $1253.16$ |
| combined | $375$ | $177/250$ | $151/250$ | $1267.74$ |
| new | $325$ | $138/200$ | $118/200$ | $1164.45$ |
| new | $365$ | $147/200$ | $125/200$ | $1246.83$ |
| new | $375$ | $145/200$ | $123/200$ | $1261.78$ |
| regression | $325$ | $30/50$ | $26/50$ | $1203.84$ |
| regression | $365$ | $33/50$ | $29/50$ | $1278.50$ |
| regression | $375$ | $32/50$ | $28/50$ | $1291.60$ |

## 综合判断与选值 / Assessment and selection

选定 chunk size 为 $365$ words，overlap 为 $40$ words。主要看新增 $200$ 题：$365$ 的 top-$5$ 证据命中和完整证据分别为 $147/200$、$125/200$，比 $375$ 各多 $2$ 题，平均读入词数也较少，为 $1246.83$ 对 $1261.78$。

Select $365$ words per chunk with $40$ words of overlap. On the $200$ new questions, $365$ scores $147/200$ for top-$5$ evidence hits and $125/200$ for complete evidence, each $2$ questions ahead of $375$. It also uses fewer words on average: $1246.83$ versus $1261.78$.

在预先确定的主指标——新增题 $1000$ words 预算下的完整证据率——上，$375$ 为 $108/200$，略高于 $365$ 的 $106/200$；两者证据命中相同，均为 $131/200$。逐题比较中，$375$ 独有完整证据成功 $5$ 题，$365$ 独有成功 $3$ 题。因此不能说 $365$ 在主指标上胜出，也不能凭这点差异认定两者有稳定优劣。

On the predeclared primary metric, complete evidence on new questions at $1000$ words, $375$ scores $108/200$ versus $106/200$ for $365$. Evidence hits are tied at $131/200$. Paired complete-evidence successes are $5$ exclusive to $375$ and $3$ exclusive to $365$. Thus $365$ does not win the primary metric, and the small difference does not establish a stable advantage for either size.

在 $2000$ words 预算下，$365$ 命中 $171/200$，比 $375$ 多 $1$ 题；完整证据为 $154/200$，比 $375$ 少 $1$ 题。在 $500$ words 下，$325$ 的两项指标更高，为 $98/200$ 和 $75/200$。综合 top-$5$ 和 $1000/2000$ words 的结果，采用 $365$，不再细搜同一题集。$40$ words 重叠沿用四轮实验设置，本轮没有比较其他重叠值。

At $2000$ words, $365$ has $171/200$ evidence hits, $1$ more than $375$, and $154/200$ complete-evidence successes, $1$ fewer. At $500$ words, $325$ leads both metrics at $98/200$ and $75/200$. Considering top-$5$ and the $1000/2000$-word budgets together, adopt $365$ without further searching on these questions. Keep the $40$-word overlap used in all four rounds; other overlap values were not compared.

本次不使用可读性评分，也不再要求人工可读性审核。评估和选值已完成；历史可读性样本和字段保留，不参与判断。题集用于选参后不再作为独立最终测试集。共享配置仍为 `v0-proposed`，其他检索方式的验证和知识库冻结属于后续交付。

Readability scoring and manual readability review are no longer required. Assessment and selection are complete; historical readability samples and fields remain but do not affect the decision. These questions are no longer an independent final test set. The shared configuration remains `v0-proposed`; validation of other retrieval modes and knowledge-base freezing remain later delivery tasks.
