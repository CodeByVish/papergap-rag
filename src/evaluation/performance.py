"""Explicit latency denominators; throughput uses batch wall time, never sum of spans."""

from __future__ import annotations

from src.evaluation.common import finite, index_rows


def percentile(values, quantile):
    values = sorted(values)
    if not values:
        return None
    position = (len(values) - 1) * quantile
    low = int(position)
    high = min(low + 1, len(values) - 1)
    return values[low] + (values[high] - values[low]) * (position - low)


def summarize_performance(
    rows, batch_seconds=None, latency_field="internal_pipeline_s"
):
    from src.evaluation.qa import prediction

    if batch_seconds is not None and (not finite(batch_seconds) or batch_seconds <= 0):
        raise ValueError("Batch seconds must be finite and positive")
    index_rows(rows)
    times, successes, errors = [], 0, 0
    for row in rows:
        _, status = prediction(row)
        errors += status == "error"
        successes += status != "error"
        if latency_field == "internal_pipeline_s":
            a, b = row.get("elapsed_s"), row.get("answer_s")
            if any(v is not None and (not finite(v) or v < 0) for v in (a, b)):
                raise ValueError("Invalid agent/generation latency")
            value = a + b if finite(a) and finite(b) else None
        else:
            value = row.get(latency_field)
        if value is not None and (not finite(value) or value < 0):
            raise ValueError("Invalid latency")
        if status != "error" and value is not None:
            times.append(value)
    return {
        "latency_field": latency_field,
        "requests": len(rows),
        "latency_n": len(times),
        "p50_seconds": percentile(times, 0.5),
        "p95_seconds": percentile(times, 0.95),
        "technical_errors": errors,
        "successful_requests": successes,
        "batch_seconds": batch_seconds,
        "successful_requests_per_second": successes / batch_seconds
        if batch_seconds
        else None,
        "completed_requests_per_second": len(rows) / batch_seconds
        if batch_seconds
        else None,
    }


def usage_cost(rows, pricing=None):
    """Normalized usage ledger: one row per call, no inferred tokens or invented price."""
    totals = {}
    for row in rows:
        component = row["component"]
        key = (component, row["model"])
        record = totals.setdefault(
            key,
            {
                "component": component,
                "model": row["model"],
                "calls": 0,
                "input_tokens": 0,
                "output_tokens": 0,
            },
        )
        record["calls"] += 1
        for field in ("input_tokens", "output_tokens"):
            value = row.get(field)
            if type(value) is not int or value < 0:
                raise ValueError("Usage requires nonnegative integer token counts")
            record[field] += value
    for key, record in totals.items():
        rate = (pricing or {}).get(key[1])
        record["cost"] = None
        if rate:
            for f in ("input_per_million", "output_per_million"):
                if not finite(rate.get(f)) or rate[f] < 0:
                    raise ValueError("Invalid token price")
            for f in ("currency", "date", "source"):
                if not rate.get(f):
                    raise ValueError("Pricing requires currency, date and source")
            record.update(
                currency=rate["currency"],
                price_date=rate["date"],
                price_source=rate["source"],
            )
            record["cost"] = (
                record["input_tokens"] * rate["input_per_million"]
                + record["output_tokens"] * rate["output_per_million"]
            ) / 1e6
    return list(totals.values())
