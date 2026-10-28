# Round 2 分块评估 / chunk-size assessment

根据本轮 `summary.json` 整理。BM25，重叠 $40$ words，同一批 $50$ 题；仅评估证据命中、证据完整和读入词数，不使用可读性评分。历史配置见 `manifest.json`。

Based on this run's `summary.json`: BM25, $40$-word overlap and the same $50$ questions. Assess evidence hits, complete evidence and input words; readability is excluded. Historical settings are in `manifest.json`.

## 定量结果 / Results

| Size (words) | Top-$5$ hit | Top-$5$ complete | Mean words |
| --- | --- | --- | --- |
| $200$ | $25/50$ | $20/50$ | $832.88$ |
| $225$ | $24/50$ | $18/50$ | $921.68$ |
| $250$ | $28/50$ | $23/50$ | $991.30$ |
| $275$ | $26/50$ | $22/50$ | $1074.08$ |
| $300$ | $28/50$ | $24/50$ | $1156.64$ |
| $325$ | $30/50$ | $26/50$ | $1203.84$ |
| $350$ | $28/50$ | $26/50$ | $1231.52$ |
| $375$ | $32/50$ | $28/50$ | $1291.60$ |
| $400$ | $30/50$ | $26/50$ | $1332.72$ |

| Size (words) | Budget (words) | Evidence hit | Complete evidence | Mean actual words | Exhausted |
| --- | --- | --- | --- | --- | --- |
| $200$ | $500$ | $19/50$ | $12/50$ | $500.00$ | $0$ |
| $200$ | $1000$ | $27/50$ | $21/50$ | $1000.00$ | $0$ |
| $200$ | $2000$ | $39/50$ | $35/50$ | $1977.10$ | $3$ |
| $225$ | $500$ | $17/50$ | $13/50$ | $500.00$ | $0$ |
| $225$ | $1000$ | $26/50$ | $19/50$ | $1000.00$ | $0$ |
| $225$ | $2000$ | $40/50$ | $36/50$ | $1976.68$ | $4$ |
| $250$ | $500$ | $13/50$ | $11/50$ | $500.00$ | $0$ |
| $250$ | $1000$ | $27/50$ | $21/50$ | $1000.00$ | $0$ |
| $250$ | $2000$ | $38/50$ | $33/50$ | $1972.68$ | $4$ |
| $275$ | $500$ | $14/50$ | $12/50$ | $500.00$ | $0$ |
| $275$ | $1000$ | $23/50$ | $19/50$ | $1000.00$ | $0$ |
| $275$ | $2000$ | $39/50$ | $34/50$ | $1969.48$ | $5$ |
| $300$ | $500$ | $16/50$ | $14/50$ | $500.00$ | $0$ |
| $300$ | $1000$ | $26/50$ | $22/50$ | $1000.00$ | $0$ |
| $300$ | $2000$ | $38/50$ | $35/50$ | $1968.68$ | $5$ |
| $325$ | $500$ | $17/50$ | $16/50$ | $500.00$ | $0$ |
| $325$ | $1000$ | $29/50$ | $25/50$ | $1000.00$ | $0$ |
| $325$ | $2000$ | $37/50$ | $34/50$ | $1968.10$ | $6$ |
| $350$ | $500$ | $15/50$ | $14/50$ | $500.00$ | $0$ |
| $350$ | $1000$ | $27/50$ | $24/50$ | $1000.00$ | $0$ |
| $350$ | $2000$ | $38/50$ | $36/50$ | $1967.30$ | $6$ |
| $375$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| $375$ | $1000$ | $25/50$ | $21/50$ | $1000.00$ | $0$ |
| $375$ | $2000$ | $38/50$ | $36/50$ | $1965.70$ | $6$ |
| $400$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| $400$ | $1000$ | $27/50$ | $23/50$ | $1000.00$ | $0$ |
| $400$ | $2000$ | $36/50$ | $34/50$ | $1964.90$ | $6$ |

“Exhausted” 表示论文的全部分块仍不足以填满预算的问题数。两个证据指标均给出成功题数／总题数。

“Exhausted” counts questions whose papers have too few chunk words to fill the budget. Evidence metrics show successful questions divided by all sampled questions.

## 判断 / Assessment

$375$ 的 top-$5$ 两项指标最高，为 $32/50$ 和 $28/50$，但平均读入 $1291.60$ words。$325$ 在 $1000$ words 下两项指标最高，为 $29/50$ 和 $25/50$，且在 $500$ words 下完整证据最多，为 $16/50$。$225$ 在 $2000$ words 下命中最多，为 $40/50$，完整证据与 $350/375$ 并列，为 $36/50$。没有一个值在所有预算下都最好；下一轮保留 $325$ 和 $375$ 附近的候选。

$375$ leads both top-$5$ metrics at $32/50$ and $28/50$, using $1291.60$ words on average. $325$ leads both metrics at $1000$ words ($29/50$ and $25/50$) and complete evidence at $500$ words ($16/50$). At $2000$ words, $225$ leads evidence hits ($40/50$) and ties $350/375$ for complete evidence ($36/50$). No size leads every budget; keep candidates around $325$ and $375$ for the next round.

每题占 $2$ 个百分点，小差异不能证明稳定优于其他值。以上只支持当前 BM25 条件下的比较；本轮不冻结知识库。最终选值见 Round 4 的 `report.md` 和 `experiments/chunk_size/criteria_zn-CN.md`。

Each question represents $2$ percentage points. Small differences do not establish a stable advantage. These results apply to the current BM25 setup and do not freeze the knowledge base. See Round 4's `report.md` and `experiments/chunk_size/criteria.md` for the final selection.
