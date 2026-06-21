# Tiered trigger prompt

Use `$tiered-trigger-router` after `$research-topic-intake-router`.

Select exactly one mode:

```text
LIGHT / STANDARD / HIGH_RISK
```

Decision principles:

1. Use the lowest sufficient mode.
2. Do not run multi-agent conflict by default.
3. Escalate only when novelty, prior-art, feasibility, methodology, or decision consequence requires it.
4. Record why skipped modules were skipped.
5. Allow later escalation if gate results reveal higher risk.

Return `trigger_decision.json`.
