# Standard prompt — research topic validation with tiered triggering

Use `$research-topic-selection-skill` to validate the following research-type paper topic.

## Candidate topic

{{candidate_topic}}

## Field boundary

{{field_boundary}}

## Available evidence

{{available_evidence}}

## Available capability

{{available_capability}}

## Decision consequence

{{decision_consequence}}

## Required output

Produce a GO / REVISE / NARROW / PIVOT / KILL topic decision brief if STANDARD or HIGH_RISK mode is triggered. If LIGHT mode is sufficient, produce a compact preliminary judgment and state whether escalation is needed.

Important constraints:

- Run only the research-topic-selection workflow.
- Do not perform manuscript review or paragraph polishing.
- Start with the lowest sufficient mode.
- Escalate only if trigger rules require it.
- Use targeted conflict review only in HIGH_RISK mode.
- Distinguish direct evidence from inference.
