#!/usr/bin/env python3
"""Compute a simple transparent topic triage score.

This is not a replacement for expert judgment. It is a deterministic helper for
comparing multiple candidate topics before running the full skill.
"""
from __future__ import annotations
import argparse, csv
from pathlib import Path

FIELDS = [
    'topic',
    'novelty_0_5',
    'feasibility_0_5',
    'evidence_0_5',
    'publishability_0_5',
    'prior_art_risk_0_5',
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('csv_file', help='CSV with columns: ' + ', '.join(FIELDS))
    ap.add_argument('--out', default='topic_scores.csv')
    args = ap.parse_args()

    rows = []
    with open(args.csv_file, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        missing = [x for x in FIELDS if x not in reader.fieldnames]
        if missing:
            raise SystemExit(f'Missing columns: {missing}')
        for r in reader:
            novelty = float(r['novelty_0_5'])
            feasibility = float(r['feasibility_0_5'])
            evidence = float(r['evidence_0_5'])
            publishability = float(r['publishability_0_5'])
            prior_art_risk = float(r['prior_art_risk_0_5'])
            score = 0.30*novelty + 0.25*feasibility + 0.20*evidence + 0.25*publishability - 0.30*prior_art_risk
            r['triage_score'] = round(score, 3)
            if score >= 3.2:
                r['triage_label'] = 'strong_candidate'
            elif score >= 2.2:
                r['triage_label'] = 'needs_review'
            elif score >= 1.2:
                r['triage_label'] = 'weak_or_needs_pivot'
            else:
                r['triage_label'] = 'likely_kill'
            rows.append(r)

    rows.sort(key=lambda x: float(x['triage_score']), reverse=True)
    with open(args.out, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else FIELDS + ['triage_score','triage_label'])
        writer.writeheader()
        writer.writerows(rows)
    print(f'Wrote {args.out}')


if __name__ == '__main__':
    main()
