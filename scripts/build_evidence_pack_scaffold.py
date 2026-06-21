#!/usr/bin/env python3
"""Create a compact evidence-pack scaffold from a plain-text note file.

This does not judge the evidence. It only structures user-provided notes into
placeholder records that agents can later refine.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('notes_file')
    ap.add_argument('--topic-id', default='topic_001')
    ap.add_argument('--out', default='evidence_pack.json')
    args = ap.parse_args()

    text = Path(args.notes_file).read_text(encoding='utf-8')
    chunks = [line.strip('- ').strip() for line in text.splitlines() if line.strip()]
    items = []
    for i, chunk in enumerate(chunks, start=1):
        items.append({
            'claim': chunk,
            'support_type': 'background',
            'source_ids': [f'note_{i:03d}'],
            'confidence': 'low',
            'notes': 'Auto-scaffolded from notes; requires human/agent verification.'
        })

    pack = {
        'topic_id': args.topic_id,
        'evidence_items': items,
        'direct_prior_art_candidates': [],
        'adjacent_prior_art_candidates': [],
        'evidence_limits': ['Auto-scaffold only; not a verified evidence pack.']
    }
    Path(args.out).write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Wrote {args.out}')


if __name__ == '__main__':
    main()
