"""Persistent content-addressed cross-encoder scores; no passage-ID shortcuts."""

import hashlib
import json
import math
import sqlite3
from pathlib import Path


class CachedPairScorer:
    """Cache raw logits by full query, full passage text and scorer identity.

    Identity must describe every setting that affects scoring. Model revision
    must be immutable; changing a model/settings/text creates different keys.
    Failures and invalid scores are never cached. Separate processes may share
    the SQLite file; each scorer instance owns its connection.
    """

    def __init__(self, scorer, path, *, identity):
        revision = identity.get("revision", "")
        if (
            not isinstance(revision, str)
            or len(revision) != 40
            or any(c not in "0123456789abcdef" for c in revision)
        ):
            raise ValueError("Score caching requires a pinned model revision SHA")
        if not identity.get("model_name"):
            raise ValueError("Score caching requires model_name")
        self.namespace = json.dumps(identity, sort_keys=True, allow_nan=False)
        self.scorer = scorer
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path, timeout=30)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS scores (key TEXT PRIMARY KEY, score REAL NOT NULL)"
        )
        self.hits = self.misses = 0

    def score(self, query, texts):
        keys = [
            hashlib.sha256(
                json.dumps([self.namespace, query, text], ensure_ascii=False).encode()
            ).hexdigest()
            for text in texts
        ]
        values = {}
        missing = {}
        for key, text in zip(keys, texts, strict=True):
            if key in values or key in missing:
                continue
            row = self.connection.execute(
                "SELECT score FROM scores WHERE key=?", (key,)
            ).fetchone()
            if row is None:
                missing[key] = text
            else:
                if not math.isfinite(row[0]):
                    raise ValueError("Nonfinite cached score")
                values[key] = row[0]
        self.hits += sum(key in values for key in keys)
        self.misses += len(missing)
        if missing:
            scores = list(self.scorer.score(query, list(missing.values())))
            if len(scores) != len(missing) or not all(math.isfinite(s) for s in scores):
                raise ValueError("Scorer must return one finite score per missing pair")
            values.update(zip(missing, map(float, scores), strict=True))
            with self.connection:
                self.connection.executemany(
                    "INSERT OR IGNORE INTO scores VALUES (?, ?)",
                    [(key, values[key]) for key in missing],
                )
        return [values[key] for key in keys]

    def close(self):
        self.connection.close()
