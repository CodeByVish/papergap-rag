"""Optional, explicitly configured RAGAS 0.2.15 judge adapter. Never called by QA scoring."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
from importlib.metadata import version

from src.evaluation.common import finite, index_rows, mean
from src.evaluation.qa import prediction, references

METRICS = ("faithfulness", "answer_relevance", "context_precision")


def prepare_samples(questions, predictions, gold, contexts):
    qmap, pmap, gmap, cmap = map(index_rows, (questions, predictions, gold, contexts))
    if (set(pmap) | set(cmap)) - set(qmap):
        raise ValueError("Prediction/context outside selected scope")
    samples = []
    for qid, q in qmap.items():
        sample = {
            "question_id": qid,
            "paper_id": q["paper_id"],
            "question": q["question"],
        }
        if qid not in pmap:
            sample["status"] = "missing_prediction"
        else:
            if (
                pmap[qid].get("paper_id", q["paper_id"]) != q["paper_id"]
                or pmap[qid].get("question", q["question"]) != q["question"]
            ):
                raise ValueError("Prediction question identity mismatch")
            text, status = prediction(pmap[qid])
            sample.update(response=text, status=status)
        if sample["status"] == "answered":
            c = cmap.get(qid)
            if not c:
                sample["status"] = "missing_context"
            elif (
                c.get("paper_id") != q["paper_id"]
                or c.get("exact_rendered") is not True
                or not c.get("provenance")
            ):
                raise ValueError(
                    "Contexts require matching paper, exact_rendered=true and provenance"
                )
            elif not isinstance(c.get("contexts"), list) or not all(
                isinstance(x, str) and x.strip() for x in c["contexts"]
            ):
                raise ValueError("Contexts must be ordered nonempty strings")
            elif not c["contexts"]:
                sample["status"] = "empty_context"
            else:
                sample["contexts"] = c["contexts"]
            if qid in gmap:
                if gmap[qid].get("paper_id", q["paper_id"]) != q["paper_id"]:
                    raise ValueError("Reference paper mismatch")
                try:
                    refs, _ = references(gmap[qid])
                except (ValueError, TypeError):
                    refs = []
                sample["reference"] = refs[0] if refs else None
        samples.append(sample)
    return samples


def score_samples(samples, judge=None):
    """No judge means validation-only. Inject a fake judge only in tests."""
    rows = []
    for sample in samples:
        row = {k: sample[k] for k in ("question_id", "paper_id")}
        for metric in METRICS:
            status = sample["status"]
            if (
                status == "answered"
                and metric == "context_precision"
                and not sample.get("reference")
            ):
                status = "missing_reference"
            value = None
            if status == "answered":
                if judge is None:
                    status = "ready_not_scored"
                else:
                    try:
                        value = judge(metric, sample)
                        valid = finite(value) and (
                            (-1 <= value <= 1)
                            if metric == "answer_relevance"
                            else (0 <= value <= 1)
                        )
                        status = "ok" if valid else "invalid_judge_score"
                        if not valid:
                            value = None
                    except Exception as e:  # noqa: BLE001 - keep evaluator failures as explicit statuses
                        status = "judge_error:" + type(e).__name__
            row[metric] = value
            row[metric + "_status"] = status
        rows.append(row)
    summary = {"questions": len(rows), "mode": "live" if judge else "validation_only"}
    for metric in METRICS:
        summary[metric] = mean(r[metric] for r in rows)
        summary[metric + "_n"] = sum(r[metric] is not None for r in rows)
        summary[metric + "_statuses"] = {
            s: sum(r[metric + "_status"] == s for r in rows)
            for s in sorted({r[metric + "_status"] for r in rows})
        }
    return rows, summary


class RagasJudge:
    """One sequential call per metric, with bounded timeout and zero automatic retries.

    The optional trace stores raw judge outputs locally. It is sensitive and never committed.
    """

    def __init__(self, config, cache):
        if version("ragas") != "0.2.15":
            raise ValueError(
                "Install requirements-evaluation.txt in a separate environment"
            )
        from langchain_core.callbacks import BaseCallbackHandler
        from langchain_openai import ChatOpenAI, OpenAIEmbeddings
        from ragas.embeddings import LangchainEmbeddingsWrapper
        from ragas.llms import LangchainLLMWrapper
        from ragas.metrics import (
            Faithfulness,
            LLMContextPrecisionWithReference,
            ResponseRelevancy,
        )
        from ragas.run_config import RunConfig

        for key in (
            "judge_model",
            "embedding_model",
            "judge_revision",
            "embedding_revision",
            "timeout_seconds",
        ):
            if not config.get(key):
                raise ValueError("Judge configuration missing " + key)
        key = os.environ.get(config.get("api_key_env", "OPENAI_API_KEY"))
        if not key:
            raise ValueError(
                "Set configured API-key environment variable; never put keys in JSON"
            )
        self.config, self.cache, self.trace = config, cache, []

        class Trace(BaseCallbackHandler):
            def on_llm_end(inner, response, **kwargs):
                self.trace.append(
                    {
                        "llm_output": response.llm_output,
                        "generations": [
                            [{"text": g.text} for g in group]
                            for group in response.generations
                        ],
                    }
                )

        timeout = config["timeout_seconds"]
        if not finite(timeout) or timeout <= 0:
            raise ValueError("timeout_seconds must be positive")
        kwargs = {"api_key": key}
        if config.get("base_url"):
            kwargs["base_url"] = config["base_url"]
        run = RunConfig(timeout=timeout, max_retries=0, max_workers=1, seed=42)
        llm = LangchainLLMWrapper(
            ChatOpenAI(
                model=config["judge_model"],
                temperature=0,
                timeout=timeout,
                max_retries=0,
                callbacks=[Trace()],
                **kwargs,
            ),
            run_config=run,
        )
        embeddings = LangchainEmbeddingsWrapper(
            OpenAIEmbeddings(
                model=config["embedding_model"],
                max_retries=0,
                request_timeout=timeout,
                **kwargs,
            )
        )
        self.metrics = {
            "faithfulness": Faithfulness(llm=llm),
            "answer_relevance": ResponseRelevancy(llm=llm, embeddings=embeddings),
            "context_precision": LLMContextPrecisionWithReference(llm=llm),
        }
        self.cache.mkdir(parents=True, exist_ok=True)

    def __call__(self, metric, sample):
        from ragas import SingleTurnSample

        evaluator = self.metrics[metric]
        prompts = {k: v.to_string() for k, v in evaluator.get_prompts().items()}
        identity = {
            "sample": sample,
            "metric": metric,
            "config": self.config,
            "ragas_version": "0.2.15",
            "prompts": prompts,
            "metric_parameters": {"strictness": getattr(evaluator, "strictness", None)},
        }
        digest = hashlib.sha256(
            json.dumps(identity, sort_keys=True).encode()
        ).hexdigest()
        path = self.cache / (digest + ".json")
        if path.exists():
            return json.loads(path.read_text())["score"]
        single = SingleTurnSample(
            user_input=sample["question"],
            response=sample["response"],
            retrieved_contexts=sample["contexts"],
            reference=sample.get("reference"),
        )

        async def run():
            return await asyncio.wait_for(
                evaluator.single_turn_ascore(single), self.config["timeout_seconds"]
            )

        value = float(asyncio.run(run()))
        if finite(value):
            path.write_text(
                json.dumps({"identity": identity, "score": value}, allow_nan=False)
                + "\n"
            )
        return value
