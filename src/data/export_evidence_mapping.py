"""Export QA evidence mapped to a verified passage corpus.

The export retains every answer annotation separately and records partial source
coverage. It creates derived gold references, not human relevance judgments.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from src.data.chunking import ChunkingConfig, build_passages_from_record
from src.data.map_evidence import (
    locate_annotations,
    passage_spans,
    source_paragraphs,
    uncovered_spans,
)
from src.data.passage_ids import PassageIdContext
from src.data.qasper_export import check_qasper_export, load_verified_papers
from src.data.split_policy import (
    SPLIT_POLICY_VERSION,
    assert_data_use_allowed,
    project_role_for_official_split,
)


def file_hash(path: Path) -> str:
    """Hash exact artifact bytes for provenance and corpus validation.

    Args:
        path: Existing input or generated output file.

    Returns:
        Lowercase SHA-256 digest computed with bounded memory.
    """
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def map_question(
    question: dict[str, Any],
    paragraphs: dict[str, dict[str, Any]],
    spans: dict[str, dict[str, tuple[int, int]]],
) -> dict[str, Any] | None:
    """Keep only questions whose every answer has fully covered text evidence.

    Args:
        question: QASPER QA row with nonempty, uniquely locatable evidence.
        paragraphs: Source paragraphs indexed by original location.
        spans: Verified corpus passage IDs mapped to paragraph character ranges.

    Returns:
        A JSON-compatible question mapping, or None for an ineligible question.
        Passage matches describe any non-whitespace overlap; full coverage is
        reported separately for each match and for the union of all matches.
    """
    annotations = locate_annotations(question, paragraphs)
    if not annotations or not all(item['usable'] for item in annotations):
        return None
    locations = sorted({loc for item in annotations for loc in item['locations']})
    evidence = []
    for location in locations:
        paragraph = paragraphs[location]
        matches = []
        for passage_id, passage_locations in spans.items():
            if location not in passage_locations:
                continue
            start, end = passage_locations[location]
            if not paragraph['text'][start:end].strip():
                continue
            matches.append({
                'passage_id': passage_id,
                'source_char_span': [start, end],
                'covers_full_paragraph': not uncovered_spans(
                    paragraph['text'], [(start, end)]
                ),
            })
        # A paragraph split across chunks is valid only when their union covers
        # every non-whitespace character, not merely when one chunk overlaps it.
        if uncovered_spans(
            paragraph['text'], [tuple(item['source_char_span']) for item in matches]
        ):
            return None
        evidence.append({
            'location': location,
            'section_index': paragraph['section_index'],
            'paragraph_index': paragraph['paragraph_index'],
            'text': paragraph['text'],
            'passage_matches': matches,
            'fully_covered_by_passage_union': True,
        })
    return {
        'schema_version': 'gold-evidence-to-passage-v0-proposed',
        'question_id': question['question_id'],
        'paper_id': question['paper_id'],
        'source_split': question['source_split'],
        'question': question['question'],
        'qa_metadata': {
            key: value for key, value in question.items()
            if key not in {'question_id', 'paper_id', 'source_split', 'question', 'answers'}
        },
        'annotations': [
            {
                **original,
                'annotation_id': item['annotation_id'],
                'answer': item['answer'],
                'evidence_locations': item['locations'],
            }
            for item, original in zip(annotations, question['answers'], strict=True)
        ],
        'evidence_paragraphs': evidence,
        'gold_passage_ids': sorted({
            match['passage_id']
            for item in evidence
            for match in item['passage_matches']
        }),
    }


def export_evidence_mapping(
    *,
    papers: Path,
    qa: Path,
    export_manifest: Path,
    passages: Path,
    passages_manifest: Path,
    output: Path,
    manifest_output: Path,
    scope: str = 'development',
) -> dict[str, Any]:
    """Validate inputs, map all eligible questions in the chosen scope, and publish.

    Args:
        papers: Paper-only QASPER JSONL export.
        qa: QA export containing the original source split on each row.
        export_manifest: Export provenance and expected input hashes.
        passages: Existing corpus; its exact IDs and text are checked.
        passages_manifest: Corpus provenance and chunking configuration.
        output: New JSONL destination; existing files are never overwritten.
        manifest_output: New destination for hashes and filtering counts.
        scope: development excludes test; all-splits-reference includes every
            split as reference mappings. The legacy all-splits-testing spelling
            remains an alias; neither spelling decides question usage rights.

    Returns:
        Manifest describing the complete export, with per-split filtering counts.

    Raises:
        ValueError: Inputs disagree or the corpus scope does not match the export.
        FileExistsError: Either output already exists.
    """
    if scope not in ('development', 'all-splits-reference', 'all-splits-testing'):
        raise ValueError('scope must be development or all-splits-reference')
    all_splits = scope != 'development'
    selected_splits = ('train', 'validation', 'test') if all_splits else ('train', 'validation')
    inputs = (papers, qa, export_manifest, passages, passages_manifest)
    targets = (output, manifest_output)
    resolved = [path.resolve() for path in (*inputs, *targets)]
    if len(set(resolved)) != len(resolved):
        raise ValueError('input and output paths must all differ')
    if any(path.exists() or path.is_symlink() for path in targets):
        raise FileExistsError('mapping output or manifest already exists')
    check_qasper_export(papers_path=papers, qa_path=qa, manifest_path=export_manifest)
    export, records = load_verified_papers(
        papers_path=papers, manifest_path=export_manifest
    )
    corpus_manifest = json.loads(passages_manifest.read_text(encoding='utf-8'))
    expected_scope = 'all-paper-text' if all_splits else 'development'
    if corpus_manifest['scope'] != expected_scope:
        raise ValueError(f'mapping export requires a {expected_scope} corpus')
    if corpus_manifest['output']['file'] != passages.name:
        raise ValueError('passage filename differs from corpus manifest')
    if corpus_manifest['output']['sha256'] != file_hash(passages):
        raise ValueError('passage hash differs from corpus manifest')
    if corpus_manifest['source']['export_papers_sha256'] != file_hash(papers):
        raise ValueError('corpus was built from a different paper export')
    settings = corpus_manifest['chunking']
    config = ChunkingConfig(**{
        key: settings[key] for key in (
            'chunk_size_words', 'chunk_overlap_words',
            'normalization_version', 'chunking_version',
        )
    })
    source = export['source']
    context = PassageIdContext(
        dataset_id=source['dataset_id'],
        resolved_revision=source['resolved_revision'],
        local_parser_version=source['local_parser_version'],
        normalization_version=config.normalization_version,
        chunking_version=config.chunking_version,
        chunk_size_words=config.chunk_size_words,
        chunk_overlap_words=config.chunk_overlap_words,
    )
    corpus = {}
    with passages.open(encoding='utf-8') as handle:
        for line in handle:
            row = json.loads(line)
            if row['passage_id'] in corpus:
                raise ValueError('duplicate passage ID')
            corpus[row['passage_id']] = row
    if len(corpus) != corpus_manifest['output']['passage_count']:
        raise ValueError('passage count differs from manifest')
    questions: dict[str, list[dict[str, Any]]] = defaultdict(list)
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    with qa.open(encoding='utf-8') as handle:
        for line in handle:
            question = json.loads(line)
            split = question['source_split']
            counts[split]['total'] += 1
            if split not in selected_splits:
                counts[split]['held_out_excluded'] += 1
                continue
            for asset in ('question', 'answer', 'label'):
                # Mechanical reference mapping does not authorize tuning or
                # decide the status of any independent held-out question list.
                if all_splits:
                    continue
                assert_data_use_allowed(
                    project_role=project_role_for_official_split(split),
                    asset=asset, purpose='chunk_selection', evaluation_frozen=False,
                )
            questions[question['paper_id']].append(question)
    rows = []
    seen_passages = set()
    for paper in records:
        if paper['source_split'] not in selected_splits:
            continue
        built = build_passages_from_record(paper, context=context, config=config).passages
        for item in built:
            passage = item.passage.model_dump(mode='json')
            passage_id = passage['passage_id']
            if corpus.get(passage_id) != passage:
                raise ValueError('rebuilt passage differs from supplied corpus')
            seen_passages.add(passage_id)
        if not questions[paper['id']]:
            continue
        paragraphs = source_paragraphs(paper)
        spans = passage_spans(paper, built, config)
        for question in questions[paper['id']]:
            mapped = map_question(question, paragraphs, spans)
            reason = 'eligible' if mapped else 'invalid_or_uncovered_answer_evidence'
            counts[question['source_split']][reason] += 1
            if mapped:
                rows.append(mapped)
    if seen_passages != set(corpus):
        raise ValueError('corpus contains unexpected passages')
    rows.sort(key=lambda row: row['question_id'])
    manifest = {
        'schema_version': 'gold-evidence-to-passage-v0-proposed',
        'split_policy_version': SPLIT_POLICY_VERSION,
        'source_splits': list(selected_splits),
        'scope': 'all-splits-reference' if all_splits else scope,
        'evaluation_design': (
            'all-splits gold reference mappings; usage determined by independent question lists and usage records; coverage alone neither freezes nor invalidates held-out status'
            if all_splits else 'development-only evidence references'
        ),
        'chunking': settings,
        'inputs': {
            name: {'file': path.name, 'sha256': file_hash(path)}
            for name, path in zip(
                ('papers', 'qa', 'export_manifest', 'passages', 'passages_manifest'),
                inputs, strict=True,
            )
        },
        'filtering_counts': dict(counts),
        'mapping_rule': 'unique whole-paragraph evidence; all answers required',
        'passage_match_rule': 'any non-whitespace overlap; full union coverage required',
        'offset_rule': 'zero-based half-open Python character offsets in evidence text',
        'label_status': 'derived gold evidence references; not human relevance labels',
        'held_out_freeze': False,
    }
    created = []
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('x', encoding='utf-8', newline='\n') as handle:
            created.append(output)
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
        manifest['output'] = {
            'file': output.name, 'rows': len(rows), 'sha256': file_hash(output),
        }
        manifest_output.parent.mkdir(parents=True, exist_ok=True)
        with manifest_output.open('x', encoding='utf-8', newline='\n') as handle:
            created.append(manifest_output)
            handle.write(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + '\n')
    except Exception:
        for path in created:
            path.unlink(missing_ok=True)
        raise
    return manifest
