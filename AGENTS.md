# AGENTS.md

This project uses a JSON-first multi-agent workflow for research topic selection. Agents should avoid reading the full corpus repeatedly. Each agent reads only the required upstream JSON state and writes a new JSON file.

## Agent protocol

- Do not fabricate citations, DOIs, search results, or prior-art claims.
- Mark uncertainty explicitly.
- Prefer science-first topic framing before AI-first methods.
- Penalize topics that cannot define a minimum viable experiment.
- Penalize pure algorithmic wrapping without a materials-science question.
- All intermediate outputs must be JSON serializable.

## Agents

### 01 Corpus Profile Agent
Input: `papers.csv`, `constraints.yaml`
Output: `state/01_corpus_profile.json`

Tasks:
- count records, year range, topic keywords;
- identify dense themes and sparse themes;
- identify data quality issues;
- summarize domain boundaries.

### 02 Problem Landscape Agent
Input: `state/01_corpus_profile.json`
Output: `state/02_problem_landscape.json`

Tasks:
- convert literature themes into materials-science problems;
- identify variables, mechanisms, and unresolved conflicts;
- separate real scientific questions from generic optimization claims.

### 03 Candidate Generator Agent
Input: `state/02_problem_landscape.json`
Output: `state/03_candidate_topics.json`

Tasks:
- propose 3-8 candidate research programs;
- provide science question, hypothesis, variables, target metrics, and why-now rationale;
- mark whether AI is necessary or only optional.

### 04 Collision Planner Agent
Input: `state/03_candidate_topics.json`
Output: `state/04_collision_plan.json`

Tasks:
- generate 8-12 precise queries and 5 broad queries per topic;
- define direct collision, partial collision, and adjacent acceptable;
- do not claim collision status unless search evidence is supplied.

### 05 Novelty & Feasibility Critic
Input: `state/03_candidate_topics.json`, `state/04_collision_plan.json`
Output: `state/05_critic_review.json`

Tasks:
- score scientific strength, novelty, feasibility, data availability, and risk;
- identify fatal weaknesses;
- downgrade overclaimed AI-first topics.

### 06 MVE Designer Agent
Input: `state/05_critic_review.json`
Output: `state/06_mve_designs.json`

Tasks:
- design minimum viable experiments;
- define controls, measurements, replication, success metrics, and kill criteria;
- estimate whether the experiment is suitable for a master's-stage project.

### 07 Decision Gate Arbiter
Input: `state/05_critic_review.json`, `state/06_mve_designs.json`
Output: `state/07_decision_gate.json`

Tasks:
- assign GO / CONDITIONAL GO / NO-GO;
- explain conditions for upgrade/downgrade;
- produce a candidate scoreboard.

### 08 Roadmap & Historian Agent
Input: all prior JSON states
Output: `state/08_roadmap_memory.json`, `topic_selection_report.md`

Tasks:
- write master-to-PhD roadmap;
- preserve decisions and rejected topics;
- generate a concise report and next-action list.
