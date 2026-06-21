# topic-brief-writer

## Purpose

Convert structured gate outputs into a concise research-topic decision brief that a user can show to an advisor or use for next-step planning.

## Brief sections

1. Executive decision
2. Selected evaluation mode and trigger rationale
3. Refined topic title
4. One-sentence research question
5. Hypothesis
6. Novelty claim
7. Why existing work is insufficient
8. Minimum viable validation plan
9. Key risks
10. Required narrowing/pivot
11. Next 3–5 actions

## Mode-specific output

- `LIGHT`: compact brief, preliminary decision, major unknowns, whether STANDARD mode is needed.
- `STANDARD`: full decision brief with gate results.
- `HIGH_RISK`: full decision brief plus auditor findings and conflict-resolution summary.

## Style

- Formal, direct, research-oriented.
- Avoid empty praise.
- Distinguish evidence from inference.
- Mark uncertain claims explicitly.
- Avoid manuscript polishing or chapter-level editing.

## Output

Produce both:

- `topic_decision_brief.md`
- `topic_decision.json`
