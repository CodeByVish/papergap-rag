"""Paired question differences with paper-clustered bootstrap uncertainty."""

import random
from collections import defaultdict

from src.evaluation.common import finite, index_rows, mean
from src.evaluation.performance import percentile


def compare(left, right, metrics, resamples=1000, seed=42):
    if type(resamples) is not int or resamples < 1:
        raise ValueError("Resamples must be positive")
    a, b = index_rows(left), index_rows(right)
    result = []
    for metric in metrics:
        groups = defaultdict(list)
        for qid in sorted(a.keys() & b.keys()):
            x, y = a[qid], b[qid]
            if x.get("paper_id") != y.get("paper_id") or not x.get("paper_id"):
                raise ValueError("Comparison requires matching paper identity")
            if finite(x.get(metric)) and finite(y.get(metric)):
                groups[x["paper_id"]].append(y[metric] - x[metric])
        papers = sorted(groups)
        values = [v for p in papers for v in groups[p]]
        rng, samples = random.Random(seed), []
        if papers:
            for _ in range(resamples):
                chosen = [rng.choice(papers) for _ in papers]
                samples.append(mean(v for p in chosen for v in groups[p]))
        result.append(
            {
                "metric": metric,
                "paired_questions": len(values),
                "papers": len(papers),
                "mean_right_minus_left": mean(values),
                "ci_low": percentile(samples, 0.025),
                "ci_high": percentile(samples, 0.975),
                "resamples": resamples,
                "seed": seed,
                "left_only_questions": len(a.keys() - b.keys()),
                "right_only_questions": len(b.keys() - a.keys()),
            }
        )
    return result
