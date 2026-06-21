#!/usr/bin/env python3
"""Initialize a research-topic-selection task workspace."""
from __future__ import annotations
import argparse
from pathlib import Path
from datetime import datetime
import json

FILES = {
    'topic_intake.json': {},
    'trigger_decision.json': {},
    'context_manifest.json': {},
    'evidence_pack.json': {},
    'prior_art_report.json': {},
    'novelty_gate_report.json': {},
    'feasibility_report.json': {},
    'collapse_test_report.json': {},
    'prior_art_audit.md': '# Prior-art audit\n\n',
    'methodology_audit.md': '# Methodology audit\n\n',
    'feasibility_audit.md': '# Feasibility audit\n\n',
    'conflict_report.json': {},
    'topic_decision.json': {},
    'topic_decision_brief.md': '# Research Topic Decision Brief\n\n',
    'archive_record.json': {},
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('task_name', help='Task name, e.g. biomass_hard_carbon_topic')
    ap.add_argument('--root', default='tasks')
    ap.add_argument('--iteration', default='iteration_001')
    args = ap.parse_args()

    task_dir = Path(args.root) / args.task_name / 'iterations' / args.iteration
    task_dir.mkdir(parents=True, exist_ok=True)

    for name, template in FILES.items():
        path = task_dir / name
        if path.exists():
            continue
        if isinstance(template, dict):
            template = dict(template)
            template.setdefault('_created_at', datetime.now().isoformat(timespec='seconds'))
            path.write_text(json.dumps(template, ensure_ascii=False, indent=2), encoding='utf-8')
        else:
            path.write_text(template, encoding='utf-8')

    print(f'Initialized: {task_dir}')


if __name__ == '__main__':
    main()
