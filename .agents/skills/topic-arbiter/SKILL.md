# topic-arbiter

## Purpose

Make the final balanced topic decision after all required gates for the selected evaluation mode.

## Inputs

Use available structured reports:

- topic_intake.json
- trigger_decision.json
- evidence_pack.json, if generated
- prior_art_report.json
- novelty_gate_report.json
- feasibility_report.json, STANDARD/HIGH_RISK
- collapse_test_report.json, STANDARD/HIGH_RISK
- auditor reports, HIGH_RISK if generated
- conflict_report.json, HIGH_RISK if generated

## Decision logic

Use:

- `GO` when novelty, feasibility, and collapse survival are all acceptable.
- `REVISE` when the topic is promising but the claim/hypothesis needs correction.
- `NARROW` when a publishable subset exists but the current scope is too broad.
- `PIVOT` when the current frame is weak but adjacent framing is stronger.
- `KILL` when novelty or feasibility is fatally insufficient.

## Mode-specific discipline

- In LIGHT mode, do not overstate certainty. Mark the result as a preliminary judgment.
- In STANDARD mode, provide a formal decision.
- In HIGH_RISK mode, explicitly state whether Advocate / Skeptic / Arbiter changed the decision compared with the gate-only result.

## Required reasoning structure

1. selected mode and why it was sufficient;
2. strongest pro-continuation argument;
3. strongest anti-continuation argument;
4. what must be changed;
5. what evidence is missing;
6. final decision.

## Output

Produce `topic_decision.json`.
