# workflow-archivist

## Purpose

Archive every topic decision so future iterations can compare what changed, including why a mode was selected or escalated.

## Archive contents

Store:

- timestamp;
- topic statement;
- selected evaluation mode;
- trigger reasons;
- evidence tier;
- final decision;
- key reasons;
- rejected alternatives;
- missing evidence;
- next actions;
- file paths to all reports.

## Directory convention

```text
tasks/<task_name>/iterations/iteration_001/
├── topic_intake.json
├── trigger_decision.json
├── context_manifest.json        # STANDARD/HIGH_RISK
├── evidence_pack.json
├── prior_art_report.json
├── novelty_gate_report.json
├── feasibility_report.json      # STANDARD/HIGH_RISK
├── collapse_test_report.json    # STANDARD/HIGH_RISK
├── prior_art_audit.md           # HIGH_RISK optional
├── methodology_audit.md         # HIGH_RISK optional
├── feasibility_audit.md         # HIGH_RISK optional
├── conflict_report.json         # HIGH_RISK
├── topic_decision.json
├── topic_decision_brief.md
└── archive_record.json
```

## Output

Produce `archive_record.json`.
