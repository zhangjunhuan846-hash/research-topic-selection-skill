# tiered-trigger-router

## Purpose

Select the lowest sufficient evaluation mode for a research topic: `LIGHT`, `STANDARD`, or `HIGH_RISK`. This is the main token-saving controller.

## Inputs

Use:

- `topic_intake.json`
- any user-stated urgency or consequence
- available evidence level
- requested output type
- available resources/capabilities

## Modes

### LIGHT

Use when:

- the user asks for a quick first judgment;
- the topic is one of many candidates;
- no formal GO/REVISE/NARROW/PIVOT/KILL decision is required;
- no expensive experiment or thesis/paper decision depends on the answer;
- available evidence is thin and only rough filtering is justified.

### STANDARD

Use when:

- the user wants a formal decision brief;
- the topic may be shown to an advisor;
- the topic may become a paper plan or thesis subtopic;
- novelty, prior-art, feasibility, and collapse-test all need to be judged;
- the user asks whether the topic is worth doing seriously.

### HIGH_RISK

Use when:

- the topic affects dissertation direction, opening report, submission strategy, grant/proposal, or expensive experiments;
- direct prior art may defeat the topic;
- novelty is weak or disputed;
- feasibility depends on missing data, instruments, collaborations, or long timelines;
- the user explicitly asks for multi-role conflict review;
- the final decision has high opportunity cost.

## Escalation rules after gates

After prior-art, novelty, feasibility, or collapse-test reports exist, re-check escalation:

- prior-art risk score ≥ 4 → `HIGH_RISK`
- novelty decision = `fail` and user may continue → `HIGH_RISK`
- feasibility label = `needs_key_resource` or `not_feasible` → `HIGH_RISK`
- collapse-test result is not `survives` → `HIGH_RISK`
- novelty decision = `conditional_pass` or prior-art risk score 2–3 → at least `STANDARD`

## De-escalation rules

Do not upgrade if:

- the user only wants topic brainstorming;
- no decision consequence exists;
- the available evidence is too thin for a reliable high-risk debate;
- the issue is merely title wording or field boundary wording.

## Output

Produce `trigger_decision.json` following `.agents/schemas/trigger_decision.schema.json` with:

- selected_mode;
- trigger_reasons;
- non_trigger_reasons;
- modules_to_run;
- modules_to_skip;
- escalation_allowed_later;
- token_budget_note.
