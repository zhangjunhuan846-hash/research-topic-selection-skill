# High-risk targeted conflict prompt

Use `$targeted-conflict-gate` for this candidate topic because `tiered-trigger-router` selected HIGH_RISK or a later gate escalated the task.

Inputs:

- `topic_intake.json`
- `trigger_decision.json`
- `evidence_pack.json`
- `prior_art_report.json`
- `novelty_gate_report.json`
- `feasibility_report.json`
- `collapse_test_report.json`
- auditor reports, if generated

Run only the relevant high-risk auditors first:

- `prior-art-auditor` if direct overlap or prior-art risk is central;
- `methodology-auditor` if hypothesis, controls, statistics, or confounding risk is central;
- `feasibility-auditor` if resource, data, instrument, or timeline risk is central.

Then run Advocate, Skeptic, and Arbiter roles. Keep each role focused on topic viability, not manuscript writing.

Final output:

- `conflict_report.json`
- short arbiter decision
