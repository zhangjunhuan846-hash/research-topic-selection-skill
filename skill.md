---
name: research-topic-selection-skill-v3
description: Science-first multi-agent research topic selection workflow for chemical and materials engineering. Use it to mine literature corpora, generate candidate topics, plan collision checks, critique feasibility, design minimum viable experiments, and decide GO / CONDITIONAL GO / NO-GO.
---

# Research Topic Selection Skill v3

Use this skill when the user wants to select, evaluate, refine, or de-risk a research topic in chemical and materials engineering.

## Core rules

1. Start from scientific problems, not AI methods.
2. Do not fabricate citations, DOI, or prior-art search results.
3. Convert each topic into a testable research program.
4. Require minimum viable experiment design.
5. Use GO / CONDITIONAL GO / NO-GO decision gates.
6. Pass context through JSON files to reduce token usage.

## Workflow

1. Profile the literature corpus.
2. Build a problem landscape.
3. Generate candidate research topics.
4. Build collision-check plans.
5. Critique novelty and feasibility.
6. Design MVE experiments.
7. Decide GO / CONDITIONAL GO / NO-GO.
8. Produce a roadmap and memory update.

## Expected outputs

- `topic_selection_report.md`
- `candidate_scoreboard.csv`
- `collision_queries.csv`
- `mve_plan.csv`
- `decision_summary.json`
- `state/*.json`
