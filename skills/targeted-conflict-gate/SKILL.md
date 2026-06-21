# targeted-conflict-gate

## Purpose

Run conflict-based review only for HIGH_RISK topic decisions. This is the token-saving substitute for always-on multi-agent debate.

## Trigger conditions

Use this gate if any condition is true:

- selected mode is `HIGH_RISK`;
- novelty decision is `conditional_pass` or `fail` but user still wants to proceed;
- prior-art risk score is 4 or 5;
- feasibility is `needs_key_resource` or `not_feasible`;
- collapse test returns `survives_if_narrowed`, `needs_pivot`, or `collapses`;
- final decision would affect dissertation direction, major experiments, opening report, grant/proposal, or publication strategy;
- the user explicitly asks for multi-role conflict review.

## Roles

### Advocate

Argues for continuing the topic. Must identify the strongest defensible framing and the minimum claim that could survive peer review.

### Skeptic

Argues against continuing the topic. Must identify prior-art, feasibility, methodological, and logic failures.

### Arbiter

Integrates both sides and decides whether the topic should proceed, narrow, pivot, or die.

## Optional high-risk auditors

Before Advocate / Skeptic / Arbiter, run only the auditors relevant to the trigger reason:

- `prior-art-auditor` for direct overlap or novelty-defeating literature risk;
- `methodology-auditor` for hypothesis, controls, statistics, or confounding risk;
- `feasibility-auditor` for resource, instrument, sample, data, or timeline risk.

## Token control

Each role receives only:

- topic_intake.json
- trigger_decision.json
- evidence_pack.json
- prior_art_report.json
- novelty_gate_report.json
- feasibility_report.json
- collapse_test_report.json
- auditor reports, if generated

No full-document reading unless explicitly required.

## Output

Produce `conflict_report.json`.
