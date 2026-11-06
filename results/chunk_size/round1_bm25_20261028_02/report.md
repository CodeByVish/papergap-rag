# Round 1 分块评估 / chunk-size assessment

根据本轮 `summary.json` 整理。BM25，重叠 $40$ words，同一批 $50$ 题；仅评估证据命中、证据完整和读入词数，不使用可读性评分。历史配置见 `manifest.json`。

Based on this run's `summary.json`: BM25, $40$-word overlap and the same $50$ questions. Assess evidence hits, complete evidence and input words; readability is excluded. Historical settings are in `manifest.json`.

## 定量结果 / Results

| Size (words) | Top-$5$ hit | Top-$5$ complete | Mean words |
| --- | --- | --- | --- |
| $100$ | $15/50$ | $12/50$ | $469.16$ |
| $200$ | $25/50$ | $20/50$ | $832.88$ |
| $400$ | $30/50$ | $26/50$ | $1332.72$ |

| Size (words) | Budget (words) | Evidence hit | Complete evidence | Mean actual words | Exhausted |
| --- | --- | --- | --- | --- | --- |
| $100$ | $500$ | $15/50$ | $12/50$ | $500.00$ | $0$ |
| $100$ | $1000$ | $18/50$ | $14/50$ | $1000.00$ | $0$ |
| $100$ | $2000$ | $31/50$ | $22/50$ | $1991.32$ | $1$ |
| $200$ | $500$ | $19/50$ | $12/50$ | $500.00$ | $0$ |
| $200$ | $1000$ | $27/50$ | $21/50$ | $1000.00$ | $0$ |
| $200$ | $2000$ | $39/50$ | $35/50$ | $1977.10$ | $3$ |
| $400$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| $400$ | $1000$ | $27/50$ | $23/50$ | $1000.00$ | $0$ |
| $400$ | $2000$ | $36/50$ | $34/50$ | $1964.90$ | $6$ |

“Exhausted” 表示论文的全部分块仍不足以填满预算的问题数。两个证据指标均给出成功题数／总题数。

“Exhausted” counts questions whose papers have too few chunk words to fill the budget. Evidence metrics show successful questions divided by all sampled questions.

## 判断 / Assessment

$100$ 在全部固定预算下的两项证据指标均不优于 $200/400$，本轮不继续考虑它。$200$ 在 $500$ words 下命中更多，在 $2000$ words 下两项指标更高；$400$ 在 $1000$ words 下完整证据更多。下一轮比较 $200$–$400$ 之间的值。

At every fixed budget, $100$ does no better on either evidence metric than $200/400$. Drop it from the next round. $200$ has more hits at $500$ words and higher scores on both metrics at $2000$ words; $400$ has more complete evidence at $1000$ words. Compare intermediate sizes next.

每题占 $2$ 个百分点，小差异不能证明稳定优于其他值。以上只支持当前 BM25 条件下的比较；本轮不冻结知识库。最终选值见 Round 4 的 `report.md` 和 `experiments/chunk_size/criteria_zn-CN.md`。

Each question represents $2$ percentage points. Small differences do not establish a stable advantage. These results apply to the current BM25 setup and do not freeze the knowledge base. See Round 4's `report.md` and `experiments/chunk_size/criteria.md` for the final selection.
