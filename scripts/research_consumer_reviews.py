"""Validate downstream imports without reassigning canonical theorem ownership."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def reviewed_consumers(root: Path, ownership: dict) -> list[dict]:
    path = root / 'catalog/research-consumer-reviews.json'
    if not path.is_file():
        return []
    document = json.loads(path.read_text(encoding='utf-8-sig'))
    if document.get('schema') != 'mtt.research-consumer-reviews.v1':
        raise ValueError('invalid consumer review schema')
    sources = {r['result_id']: r for r in ownership['results']}
    source_map = document.get('result_source_map', {})
    if not isinstance(source_map, dict):
        raise ValueError('invalid Kernel-to-curated result map')
    seen_ids, seen_pairs = set(), set()
    validated = []
    for row in document.get('reviews', []):
        rid, paper = row.get('id'), row.get('paper_id')
        if not rid or rid in seen_ids or not isinstance(paper, str):
            raise ValueError('missing or duplicate consumer review identity')
        seen_ids.add(rid)
        directory = root / 'papers' / paper
        if directory.resolve().parent != (root / 'papers').resolve():
            raise ValueError('invalid consumer paper path')
        if not (directory / 'metadata.json').is_file():
            raise ValueError(f'unknown consumer paper: {paper}')
        tex = (directory / 'main.tex').read_text(encoding='utf-8-sig')
        actual = hashlib.sha256(tex.encode('utf-8')).hexdigest()
        if actual != row.get('main_tex_lf_sha256'):
            raise ValueError(f'stale consumer manuscript: {rid}')
        if row.get('state') not in {'integrated', 'not_applicable'}:
            raise ValueError(f'unaccepted consumer disposition: {rid}')
        if len(row.get('assessment', '')) < 40 or not row.get('reviewer') or not row.get('reviewed_at'):
            raise ValueError(f'incomplete contextual consumer assessment: {rid}')
        anchors = row.get('anchors', [])
        if not anchors or any(not a or a not in tex for a in anchors):
            raise ValueError(f'missing consumer evidence anchor: {rid}')
        source_ids = row.get('curated_result_ids', [])
        if not source_ids or len(set(source_ids)) != len(source_ids):
            raise ValueError(f'missing or duplicate consumer source: {rid}')
        if set(row.get('result_hashes', {})) != set(source_ids):
            raise ValueError(f'incomplete consumer source hashes: {rid}')
        owners = {}
        for source_id in source_ids:
            source = sources.get(source_id)
            if not source or source['sha256'] != row['result_hashes'][source_id]:
                raise ValueError(f'stale consumer source: {rid}/{source_id}')
            owner = source.get('contextual_review') or {}
            if owner.get('state') not in {'integrated', 'historical_context'} or owner.get('stale_reasons'):
                raise ValueError(f'unreviewed consumer source owner: {rid}/{source_id}')
            owner_tex = (root/'papers'/source['integration_owner']/'main.tex').read_text(encoding='utf-8-sig').encode('utf-8')
            if hashlib.sha256(owner_tex).hexdigest() != owner.get('main_tex_lf_sha256'):
                raise ValueError(f'stale canonical owner: {rid}/{source_id}')
            owners[source_id] = source['integration_owner']
        result_ids = row.get('result_ids', [])
        if not result_ids or len(set(result_ids)) != len(result_ids):
            raise ValueError(f'missing or duplicate Kernel result mapping: {rid}')
        mapped_sources = set()
        for kernel_id in result_ids:
            if not isinstance(kernel_id, str) or not kernel_id.startswith('R.'):
                raise ValueError(f'invalid Kernel result id: {rid}')
            pair = (paper, kernel_id)
            if pair in seen_pairs:
                raise ValueError(f'duplicate consumer placement: {paper}/{kernel_id}')
            seen_pairs.add(pair)
            mapping = source_map.get(kernel_id)
            if (not isinstance(mapping, list) or not mapping
                    or len(set(mapping)) != len(mapping)
                    or any(s not in sources for s in mapping)):
                raise ValueError(f'unregistered Kernel source mapping: {rid}/{kernel_id}')
            selected = row.get('kernel_result_sources', {}).get(kernel_id, mapping)
            if (not isinstance(selected, list) or not selected
                    or len(set(selected)) != len(selected)
                    or not set(selected) <= set(mapping)):
                raise ValueError(f'unregistered per-review source binding: {rid}/{kernel_id}')
            mapped_sources.update(selected)
        if mapped_sources != set(source_ids):
            raise ValueError(f'consumer source mapping mismatch: {rid}')
        validated.append({**row, 'canonical_owner_papers': owners,
                          'locations': [{'source_ref': f'papers/{paper}/main.tex',
                                         'line_start': tex[:tex.index(a)].count('\n')+1,
                                         'anchor': a} for a in anchors]})
    return validated
