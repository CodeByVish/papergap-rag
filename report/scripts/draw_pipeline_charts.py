"""Draw the offline indexing and online retrieval charts into report/images."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "images"
INK = "#1f2933"
MUTED = "#52606d"
STYLES = {
    "step": dict(fc="#e8f0fa", ec="#2f5f9e", ls="-"),
    "data": dict(fc="#f1f3f5", ec="#6b7780", ls="-"),
    "excluded": dict(fc="#ffffff", ec="#8a94a0", ls=(0, (3, 2))),
    "optional": dict(fc="#fff6e5", ec="#b7791f", ls=(0, (3, 2))),
    "output": dict(fc="#e6f4ea", ec="#2f7d4f", ls="-"),
}
plt.rcParams["font.family"] = ["Helvetica", "Arial", "DejaVu Sans"]
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["svg.fonttype"] = "none"


def canvas(width, height):
    """One data unit is one millimetre, so text sizes stay true in the report."""
    fig = plt.figure(figsize=(width / 25.4, height / 25.4), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, title, body="", style="step", size=7.2):
    s = STYLES[style]
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0,rounding_size=1.4",
        fc=s["fc"], ec=s["ec"], ls=s["ls"], lw=0.8, zorder=2,
    ))
    if body:
        ax.text(x + 2.2, y + 1.9, title, fontsize=size + 0.4, fontweight="bold",
                color=INK, va="top", zorder=3)
        ax.text(x + 2.2, y + 5.8, body, fontsize=size, color=INK, va="top",
                linespacing=1.28, zorder=3)
    else:
        ax.text(x + w / 2, y + h / 2, title, fontsize=size + 0.4, fontweight="bold",
                color=INK, va="center", ha="center", zorder=3)


def arrow(ax, points, color=INK, ls="-", label=None, label_at=None):
    """Draw an orthogonal path through `points` with one arrowhead at the end."""
    xs, ys = zip(*points[:-1])
    ax.plot(xs, ys, color=color, lw=0.9, ls=ls, zorder=1, solid_capstyle="butt")
    ax.add_patch(FancyArrowPatch(
        points[-2], points[-1], arrowstyle="-|>", mutation_scale=7,
        color=color, lw=0.9, ls=ls, shrinkA=0, shrinkB=0, zorder=1,
    ))
    if label:
        ax.text(*label_at, label, fontsize=6.6, color=color, ha="center", va="center",
                zorder=4, bbox=dict(fc="white", ec="none", pad=0.8))


def legend(ax, y, entries):
    x = 2
    for style, text in entries:
        s = STYLES[style]
        ax.add_patch(FancyBboxPatch(
            (x, y), 5, 3, boxstyle="round,pad=0,rounding_size=0.6",
            fc=s["fc"], ec=s["ec"], ls=s["ls"], lw=0.7,
        ))
        ax.text(x + 6.2, y + 1.5, text, fontsize=6.6, color=MUTED, va="center")
        x += 9 + 1.5 * len(text)


def offline():
    fig, ax = canvas(170, 143)
    left, step_w = 2, 104
    right, data_w = 112, 56
    mid = left + step_w / 2

    box(ax, left, 2, step_w, 16, "1  Acquire and verify  (scripts.download_qasper)",
        "Pinned Hugging Face revision fdc9d821 for dataset metadata\n"
        "Official v0.3 train/dev and test/evaluator archives\n"
        "Check archive size and SHA-256; parse required JSON members")
    box(ax, right, 2, data_w, 16, "data/raw/qasper/",
        "train, validation, test .jsonl\nmanifest.json (checksums)", "data")
    arrow(ax, [(left + step_w, 10), (right, 10)])

    box(ax, left, 23, step_w, 26, "2  Separate papers from questions  (scripts.export_qasper)",
        "Remove qas from each paper record; add source_split\n"
        "Write questions, answers and evidence to a separate file\n"
        "Reject duplicate paper and question IDs\n"
        "Record counts and hashes in qasper_export.manifest.json")
    box(ax, right, 23, data_w, 12, "qa.jsonl",
        "Questions, answers, evidence: never indexed", "excluded", size=6.6)
    box(ax, right, 37, data_w, 12, "papers.jsonl",
        "Title, abstract, full text, figures/tables", "data", size=6.6)
    arrow(ax, [(right + 28, 18), (right + 28, 20.5), (mid, 20.5), (mid, 23)])
    arrow(ax, [(left + step_w, 29), (right, 29)])
    arrow(ax, [(left + step_w, 43), (right, 43)])

    box(ax, left, 54, step_w, 28, "3  Build passages  (scripts.build_corpus, scope all-paper-text)",
        "Verify the export; read only id, title and full_text\n"
        "Clean: normalise line endings, trim outer whitespace,\n"
        "drop blank paragraphs and blank or unnamed sections\n"
        "Chunk within each section: 365-word windows, 40-word overlap\n"
        "Assign deterministic passage IDs and prev/next links\n"
        "Require at least 10,000 passages and 100,000 words")
    box(ax, right, 54, data_w, 28, "passages_all_paper_text.jsonl",
        "28,617 passages, 1,584 papers\n"
        "(train + validation + test text)\n"
        "Manifest: chunking, counts, SHA-256\n"
        "Abstracts, figures, tables excluded", "data", size=6.6)
    arrow(ax, [(right + 28, 49), (right + 28, 51.5), (mid, 51.5), (mid, 54)])
    arrow(ax, [(left + step_w, 68), (right, 68)])

    box(ax, 2, 87, 166, 8, "4  Build indexes from validated passage JSONL  (scripts.build_indexes)")
    arrow(ax, [(right + 28, 82), (right + 28, 87)])
    lw, rx = 80, 88
    box(ax, 2, 100, lw, 16, "Sparse: per-paper BM25",
        "Tokenise with casefold and \\w+\nBM25Okapi (k1 = 1.5, b = 0.75)\n"
        "Construction check only; object not saved")
    box(ax, rx, 100, lw, 16, "Dense: per-paper FAISS",
        "Encode passage text with bge-small-en-v1.5\n(revision 5c38ec7c); L2-normalise\n"
        "One exact IndexFlatIP per paper")
    arrow(ax, [(42, 95), (42, 100)])
    arrow(ax, [(128, 95), (128, 100)])
    box(ax, 2, 121, lw, 12.5, "No BM25 file",
        "Rebuilt from passage JSONL at service start", "excluded")
    box(ax, rx, 121, lw, 12.5, "Dense index directory",
        "paper-NNNNNN.faiss, one per paper\nmetadata.json: model, passages, SHA-256s", "data")
    arrow(ax, [(42, 116), (42, 121)])
    arrow(ax, [(128, 116), (128, 121)])
    legend(ax, 138, [("step", "Processing step"), ("data", "Saved artifact"),
                     ("excluded", "Not indexed or not saved")])
    return fig


def online():
    fig, ax = canvas(170, 129)
    full, lw, rx = 162, 78, 86
    lc, rc, mid = 41, 125, 83
    dash = (0, (3, 2))
    amber = STYLES["optional"]["ec"]
    box(ax, 2, 2, full, 16, "Retrieval request for one round",
        "Query: the question, or the rewritten query on a retry\n"
        "Paper filter: selected paper_id\n"
        "Section: none in round 1; a retry may name one exact section of that paper", "data")
    ax.plot([lc, rc], [21, 21], color=INK, lw=0.9, zorder=1)
    ax.plot([mid, mid], [18, 21], color=INK, lw=0.9, zorder=1)
    arrow(ax, [(lc, 21), (lc, 24)])
    arrow(ax, [(rc, 21), (rc, 24)])

    box(ax, 2, 24, lw, 19.5, "BM25 branch",
        "Tokenise query with casefold and \\w+\n"
        "Score all passages in the paper's BM25Okapi\n"
        "Optional exact section filter\n"
        "Keep top 20; ties broken by passage ID")
    box(ax, rx, 24, lw, 19.5, "Dense branch",
        "Prefix BGE query instruction; encode; L2-normalise\n"
        "Exact cosine search of the paper's IndexFlatIP\n"
        "Optional exact section filter\n"
        "Keep top 20; ties broken by passage ID")
    ax.plot([lc, lc, rc, rc], [43.5, 46.5, 46.5, 43.5], color=INK, lw=0.9, zorder=1)
    arrow(ax, [(mid, 46.5), (mid, 49)])

    box(ax, 2, 49, full, 12.5, "Reciprocal rank fusion",
        "Deduplicate by passage ID: up to 40 unique candidates, keeping each source's rank and score\n"
        "Score = sum over BM25 and dense of 1 / (60 + rank); sort by score, then passage ID")

    box(ax, 2, 67, lw, 12.5, "Current configuration",
        "No reranker; keep the RRF order")
    box(ax, rx, 67, lw, 12.5, "Optional reranker, off by default",
        "bge-reranker-base scores the whole union", "optional")
    arrow(ax, [(lc, 61.5), (lc, 67)])
    arrow(ax, [(rc, 61.5), (rc, 67)], color=amber, ls=dash)

    box(ax, 2, 85, full, 8, "Return up to 8 passages for this round (top_k = 8)")
    arrow(ax, [(lc, 79.5), (lc, 85)])
    arrow(ax, [(rc, 79.5), (rc, 85)], color=amber, ls=dash)

    box(ax, 2, 99, lw, 12.5, "Agent evidence pool",
        "Append new passages by ID\nCritic reads the generator view")
    box(ax, rx, 99, lw, 12.5, "Generator view",
        "select_passages: at most 8 passages,\neach cut to 1,200 characters", "output")
    arrow(ax, [(lc, 93), (lc, 99)])
    arrow(ax, [(2 + lw, 105), (rx, 105)])

    retry = "#2f5f9e"
    ax.plot([lc, lc, 167.5, 167.5], [111.5, 115.5, 115.5, 10], color=retry, lw=0.9,
            ls=dash, zorder=1)
    arrow(ax, [(167.5, 10), (164, 10)], color=retry, ls=dash)
    ax.text(103, 115.5, "Critic finds a gap: rewrite query and retry (at most 3 rounds). "
            "Empty section search repeats on the whole paper.",
            fontsize=6.4, color=retry, ha="center", va="center", zorder=4,
            bbox=dict(fc="white", ec="none", pad=0.8))
    ax.text(2, 120.5, "Local UI \"All papers\" (paper_id = null) follows the same steps with global BM25 "
            "and one global FAISS index, and has no section retries.",
            fontsize=6.6, color=MUTED, va="center")
    legend(ax, 124, [("step", "Processing step"), ("data", "Input"),
                     ("optional", "Disabled option"), ("output", "Text sent to the generator")])
    return fig


for name, draw in (("offline-corpus-index", offline), ("online-hybrid-retrieval", online)):
    figure = draw()
    OUT.mkdir(exist_ok=True)
    figure.savefig(OUT / f"{name}.png", dpi=300, facecolor="white")
    figure.savefig(OUT / f"{name}.pdf", facecolor="white")
    plt.close(figure)
