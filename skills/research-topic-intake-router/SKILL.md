# research-topic-intake-router

## Purpose

Classify the incoming request and convert it into a structured topic-intake record. This is the first step before tiered triggering.

## When to use

Use this first whenever the user asks for topic selection, topic validation, topic screening, novelty judgment, feasibility analysis, or whether a research direction is worth doing.

## Input extraction

Extract:

- candidate topic;
- field/domain;
- target paper type;
- target journal level, if stated;
- available evidence sources;
- available experimental or computational capability;
- claimed novelty;
- hidden constraints;
- user’s desired decision style;
- whether the decision affects thesis, opening report, submission, grant/proposal, expensive experiments, or long-term research direction.

## Routing labels

Use one or more:

- `topic_generation`
- `topic_validation`
- `novelty_check`
- `prior_art_attack`
- `feasibility_check`
- `scope_narrowing`
- `topic_pivot`
- `decision_brief`

## Risk triage

Set `risk_level`:

- `low`: early idea, wording/scope decision, or low-cost screening.
- `medium`: serious topic validation, novelty or feasibility uncertain, advisor-facing output possible.
- `high`: dissertation direction, opening report, submission strategy, grant/proposal, major experiment, or long-term research investment.

## Suggested evaluation mode

Set `requested_mode` only if the user explicitly asks for it. Otherwise infer a preliminary `risk_level` and let `tiered-trigger-router` choose the final mode.

## Output

Produce `topic_intake.json` following `.agents/schemas/topic_intake.schema.json`.
