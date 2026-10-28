"""Generate gold evidence-to-passage JSONL for eligible QASPER questions.

Run from the repository root with python -m scripts.export_evidence_mapping.
Corpus chunking settings are read from its verified manifest, not CLI defaults.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from src.data.export_evidence_mapping import export_evidence_mapping


def main() -> int:
    """Parse artifact locations and export strict evidence mappings.

    Returns:
        Zero on success, or one with an actionable validation error on stderr.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--scope', choices=('development', 'all-splits-testing'), default='development',
        help='all-splits-testing uses every split as ordinary tests, waiving held-out status',
    )
    defaults = {
        'papers': 'papers.jsonl',
        'qa': 'qa.jsonl',
        'export_manifest': 'qasper_export.manifest.json',
        'passages': 'passages.jsonl',
        'passages_manifest': 'passages.manifest.json',
        'output': 'gold_evidence_mapping.jsonl',
        'manifest_output': 'gold_evidence_mapping.manifest.json',
    }
    for key, name in defaults.items():
        parser.add_argument(
            '--' + key.replace('_', '-'), type=Path,
            default=None,
        )
    arguments = vars(parser.parse_args())
    if arguments['scope'] == 'all-splits-testing':
        defaults.update({
            'passages': 'passages_all_paper_text.jsonl',
            'passages_manifest': 'passages_all_paper_text.manifest.json',
            'output': 'gold_evidence_mapping_all_splits.jsonl',
            'manifest_output': 'gold_evidence_mapping_all_splits.manifest.json',
        })
    for key, name in defaults.items():
        if arguments[key] is None:
            arguments[key] = Path('data/processed') / name
    try:
        manifest = export_evidence_mapping(**arguments)
    except (ValueError, TypeError, KeyError, OSError) as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
