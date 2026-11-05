import argparse
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chunks", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()

    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)
    seen = set()
    count = 0

    with (
        Path(a.chunks).open(encoding="utf-8") as src,
        (out / "chunks.jsonl").open("w", encoding="utf-8") as dst,
    ):
        for line_no, line in enumerate(src, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            cid, text = row["chunk_id"], row["text"].strip()
            if not text or not cid or not row["paper_id"].strip():
                raise ValueError(f"Empty text or identifier on line {line_no}")
            if cid in seen:
                raise ValueError(f"Duplicate chunk ID on line {line_no}: {cid}")
            seen.add(cid)
            dst.write(
                json.dumps({"id": cid, "contents": text}, ensure_ascii=False) + "\n"
            )
            count += 1
    if count == 0:
        raise ValueError("The chunk corpus is empty")
    print(f"Wrote {count} passages")


if __name__ == "__main__":
    main()
