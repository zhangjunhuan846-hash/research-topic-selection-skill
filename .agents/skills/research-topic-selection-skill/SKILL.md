# research-topic-selection-skill

## Purpose

Coordinate a complete research-topic validation loop. This skill is for research-type paper topic selection, not manuscript revision.

v3 adds tiered triggering: use the lowest sufficient evaluation mode and escalate only when evidence risk or decision consequence requires it.

## Inputs

Accept any of the following:

- a candidate research topic;
- a rough idea or research direction;
- a literature search result summary;
- a CSV/abstract-screening result;
- an advisor suggestion;
- a previous topic brief;
- a draft section used only to infer the topic boundary.

## Required first step

Always run:

```text
research-topic-intake-router
→ tiered-trigger-router
```

The router must set:

```text
selected_mode = LIGHT / STANDARD / HIGH_RISK
```

and produce `trigger_decision.json`.

## Workflow by mode

### LIGHT

Use for early-stage idea screening or comparing several possible topics.

```text
research-topic-intake-router
→ tiered-trigger-router
→ prior-art-topic-filter, quick mode
→ novelty-gate, quick mode
→ topic-brief-writer, compact mode
```

LIGHT output can be a compact recommendation rather than a full decision brief.

### STANDARD

Use for a serious candidate topic that may become a paper plan.

```text
research-topic-intake-router
→ tiered-trigger-router
→ literature-context-builder
→ prior-art-topic-filter
→ novelty-gate
→ feasibility-gate
→ collapse-test
→ topic-arbiter
→ topic-brief-writer
→ workflow-archivist
```

### HIGH_RISK

Use for dissertation/opening-report/submission/grant/expensive-experiment decisions.

```text
research-topic-intake-router
→ tiered-trigger-router
→ literature-context-builder
→ prior-art-topic-filter
→ novelty-gate
→ feasibility-gate
→ collapse-test
→ prior-art-auditor, if prior-art risk is central
→ methodology-auditor, if hypothesis/design/statistics are central
→ feasibility-auditor, if resources/timeline/experiments are central
→ targeted-conflict-gate
→ topic-arbiter
→ topic-brief-writer
→ workflow-archivist
```

## Divergent Ideation Mode

Divergent Ideation Mode is used when the user asks to brainstorm, expand thinking, generate different research topics, avoid repetitive topics, or explore alternative research directions.

It must run BEFORE the prior-art collision gate.

The mode must not directly produce a final topic. It first creates a broad topic pool across multiple independent research dimensions, then passes candidates into collision screening and narrowing.

Trigger phrases include:

- brainstorm
- 头脑风暴
- 扩展思维
- 题目太雷同
- 多生成几个方向
- 换一些研究角度
- 不要只围绕一个变量
- alternative topics
- divergent ideation
- topic pool

When triggered, the workflow must:

1. Identify the current crowded axis.
2. Identify unsafe novelty axes.
3. Generate topic candidates from at least 8 independent research dimensions.
4. Enforce lexical and conceptual diversity.
5. Run a light collision pre-screen.
6. Select 3–5 candidates for deeper evaluation.
7. Output a topic pool instead of a final single topic.

Output files:

```text
tasks/<task_name>/iterations/<iteration_id>/topic_pool.md
tasks/<task_name>/iterations/<iteration_id>/topic_pool.json
tasks/<task_name>/iterations/<iteration_id>/divergent_ideation_report.md
```

If there is no current `task_name`, use:

```text
tasks/divergent_topic_brainstorm/iterations/iteration_001/
```

## Eight-Lens Research Ideation Framework

For biomass-derived or model hard-carbon anode topics, brainstorm from these eight lenses:

1. Precursor chemistry
   - extractives
   - intrinsic heteroatoms
   - ash/mineral residues
   - carbon yield
   - industrial precursor impurity

2. Pyrolysis pathway
   - heating rate
   - low-temperature pre-carbonization
   - volatile release
   - dwell time
   - atmosphere
   - carbon yield evolution

3. Pore accessibility and closed pores
   - gas-accessible versus ion-accessible pores
   - open-pore penalty
   - closed-pore proxies
   - pore closure window
   - He density / CO2 adsorption / SAXS descriptors

4. Surface/interface/SEI
   - residual ash–SEI coupling
   - surface oxygen
   - first-cycle interphase
   - ex situ XPS after formation
   - irreversible capacity partition

5. Electrolyte and formation protocol
   - FEC masking effect
   - carbonate versus ether electrolyte
   - formation current
   - voltage window
   - protocol-dependent ICE ranking

6. Electrode engineering and practical relevance
   - mass loading
   - calendering
   - electrode density
   - binder system
   - full-cell sodium inventory loss
   - presodiation demand

7. Descriptor/statistical methodology
   - descriptor reliability
   - ash-corrected capacity
   - protocol-normalized benchmark
   - reporting standard
   - causality checklist
   - hidden protocol variables

8. Cross-system transferability
   - SIB versus LIB
   - SIB versus aqueous supercapacitor
   - same carbon, different design rules
   - descriptor sign reversal
   - gas-accessible versus ion-accessible descriptors across systems

For each lens, generate at least 5 candidate directions unless the user asks for fewer.

## Diversity Constraints

The brainstorming output must not collapse into repetitive wording.

Rules:

1. In a single topic pool, no more than 30% of candidates may use the same core phrase.
2. Avoid overusing the following phrases:
   - composition–ash
   - ICE-first
   - descriptor engineering
   - cellulose–lignin ladder
   - mineral perturbation
   - benchmark
   - decoupling
3. If more than 30% of topic titles contain the same keyword family, regenerate the topic pool.
4. Each candidate must be assigned a distinct primary mechanism axis:
   - precursor axis
   - pyrolysis axis
   - pore axis
   - interface axis
   - protocol axis
   - electrode-engineering axis
   - statistical/methodological axis
   - cross-system axis
5. Do not use cellulose:lignin ratio, Al2O3 mineral addition, natural biomass impurity removal, or broad biomass precursor screening as the main novelty axis unless the user explicitly asks to revisit a high-collision topic.
6. If a topic only differs by changing Ca to Si, Al, Fe, K, or Mg, mark it as low diversity and regenerate.

## Topic Pool Output Template

When Divergent Ideation Mode is triggered, generate:

```text
tasks/<task_name>/iterations/<iteration_id>/topic_pool.md
tasks/<task_name>/iterations/<iteration_id>/topic_pool.json
tasks/<task_name>/iterations/<iteration_id>/divergent_ideation_report.md
```

`topic_pool.md` must contain:

```text
# Divergent Topic Pool

## 1. Current Crowded Axis
- What the current topic is over-concentrated on.
- Which novelty axes are unsafe.
- Which phrases should be avoided.

## 2. Brainstorming Lenses
For each of the 8 lenses:
- Lens name
- 5 candidate directions
- For each candidate:
  - English working title
  - Chinese explanation
  - Core scientific question
  - Primary mechanism axis
  - Why it is different from the current Ca/Si ash timing topic
  - Potential collision risk
  - Feasibility score: 1–5
  - Novelty score: 1–5
  - Collision risk score: 1–5
  - Advisor-discussion value: 1–5
  - Pilot suitability: yes/no
  - Minimum experiment needed

## 3. Diversity Check
- Repeated keywords
- Repeated mechanism axes
- Candidates rejected for being too similar
- Regenerated candidates if needed

## 4. Top Candidate Shortlist
Select 3–5 topics for deeper evaluation.

Each shortlisted topic must include:
- safer working title
- strongest novelty space
- closest likely prior-art category
- minimum pilot matrix
- why it is not just another composition–ash–ICE topic
- recommended next gate:
  - light screen
  - full collision check
  - experimental narrowing
  - kill
```

`topic_pool.json` must save the same fields in structured form.

## Light Collision Pre-Screen

Before sending brainstormed topics to full evaluation, perform a quick collision pre-screen.

For each candidate, check whether it primarily depends on an already occupied axis:

- cellulose:lignin ratio
- pure cellulose/lignin model precursor
- Al2O3 mineral effect
- natural biomass impurity removal
- broad biomass precursor screening
- generic composition–microstructure–performance relationship
- generic high ICE hard carbon optimization
- generic acid washing purification

If yes, the candidate must be:

- rewritten around a narrower mechanism contrast; or
- demoted; or
- rejected.

Do not kill a candidate only because individual variables are known. Kill or demote it only if the proposed novelty is the known variable itself.

## Topic Family Deduplication

Group generated candidates into topic families:

1. Materials variable family
2. Pyrolysis mechanism family
3. Pore-accessibility family
4. Interface/SEI family
5. Electrolyte/protocol family
6. Electrode-engineering family
7. Statistical/methodological family
8. Cross-system transferability family

The final shortlist must contain candidates from at least 3 different families.

If all shortlisted candidates come from one family, repeat divergent ideation.

## Brainstorming Candidate Scoring

Score each candidate using:

```text
Total score =
0.30 * novelty_score
+ 0.25 * feasibility_score
+ 0.20 * advisor_discussion_value
+ 0.15 * mechanism_clarity_score
- 0.25 * collision_risk_score
```

Where:

- novelty_score: 1–5
- feasibility_score: 1–5
- advisor_discussion_value: 1–5
- mechanism_clarity_score: 1–5
- collision_risk_score: 1–5

Do not select a candidate with `collision_risk_score >= 4` unless it has a clearly defined pivot or narrowing strategy.

## Anti-AI-Wrapping Gate

Anti-AI-Wrapping Gate is required for every AI-for-Science candidate topic before it can enter a Top 10 shortlist, formal topic decision, advisor brief, or experimental plan.

Purpose: reject or rewrite topics where AI is only decorative wording rather than a necessary part of the scientific workflow.

For each AI-for-Science candidate, answer these eight questions:

1. If AI is removed, does the topic still have a clear materials-science question?
2. Can that materials-science question be experimentally validated?
3. Does AI solve a problem that traditional experiments or traditional analysis struggle to solve?
4. Is there a minimum experimental matrix, rather than only an existing dataset?
5. Is there an independent validation experiment or next-round experimental loop?
6. Do model inputs include physically meaningful descriptors?
7. Will the AI result change the next experimental choice or mechanism judgment?
8. If the AI model fails, can the topic fall back to an experimental paper or methodology paper?

Decision rules:

- If question 1 or 2 is `no`, directly mark the topic `KILL`.
- If question 3 is `no`, mark it as an `AI-wrapped low-value topic`.
- If question 4 or 5 is `no`, the topic cannot enter Top 10.
- If question 6 is `no`, rewrite the topic as a physics-informed descriptor topic.
- If question 7 is `no`, AI may only be auxiliary analysis and cannot be the core topic claim.
- If question 8 is `no`, mark it as `high-risk gimmick AI`.

After the eight-question gate, score surviving or rewritable candidates with a science-first score. Score each component from 1 to 5:

```text
Science-first score =
0.25 * material_question_strength
+ 0.20 * experimental_verifiability
+ 0.15 * mechanism_clarity
+ 0.15 * AI_necessity
+ 0.10 * validation_loop_strength
+ 0.10 * advisor_acceptance
+ 0.05 * publication_potential
```

Use this score to rank AI-for-Science candidates only after hard gate exclusions are applied. It must not rescue topics marked `KILL`, topics blocked from Top 10 by missing experiments or validation loops, or topics where AI is only decorative.

Science-first Top 10 eligibility rules:

- If `material_question_strength < 4`, the topic cannot enter Top 10.
- If `experimental_verifiability < 4`, the topic cannot enter Top 10.
- If `AI_necessity < 3`, the topic may only be treated as an ordinary experimental topic and must not be labeled as AI-for-Science.
- These thresholds are hard filters. A high total science-first score cannot override them.

Required output file when this gate is run:

```text
tasks/<task_name>/iterations/<iteration_id>/anti_ai_wrapping_report.md
```

If no task has been created, use:

```text
tasks/ai_for_science_topic_discovery/iterations/iteration_001/anti_ai_wrapping_report.md
```

For each candidate, `anti_ai_wrapping_report.md` must include:

- material science question
- why AI is necessary
- minimum experimental matrix
- validation loop
- physics descriptors
- fallback if AI fails
- gate answers for questions 1-8
- gate action: pass / rewrite / demote / top10_blocked / KILL
- AI-wrapping risk: low / medium / high
- science-first component scores
- science-first score
- science-first Top 10 eligibility: eligible / blocked
- final AI-for-Science label: AI-for-Science / ordinary experimental topic

## Project-Specific Unsafe Axes for Biomass Hard-Carbon SIB Topics

For the current hard-carbon topic family, treat the following as crowded or unsafe main novelty axes:

1. cellulose:lignin ratio as main novelty
2. pure cellulose/lignin model precursor as main novelty
3. Al2O3 addition as main mineral novelty
4. natural biomass impurity removal as main novelty
5. acid/base washing simply improving hard-carbon performance
6. broad biomass precursor screening
7. generic "high ICE by optimized carbonization temperature"
8. generic "composition–microstructure–pore–performance relationship"
9. generic "closed pores improve plateau capacity"
10. generic "BET reduction improves ICE"

These axes may be used as background, controls, or comparison baselines, but not as the central novelty claim.

## Decision protocol

Final decision must be one of:

```text
GO / REVISE / NARROW / PIVOT / KILL
```

Use `GO` only when the topic has:

1. a non-trivial novelty claim;
2. a clear scientific question;
3. a testable hypothesis;
4. a feasible minimum validation plan;
5. manageable prior-art risk.

## Escalation protocol

Escalate from LIGHT to STANDARD if:

- the user asks for a formal decision;
- direct or adjacent prior art appears non-trivial;
- novelty is conditional;
- feasibility or minimum validation needs to be judged;
- the output will be used for advisor discussion or paper planning.

Escalate from STANDARD to HIGH_RISK if:

- prior-art risk score ≥ 4;
- novelty decision = `fail` but continuation is being considered;
- feasibility label = `needs_key_resource` or `not_feasible`;
- collapse-test does not return `survives`;
- the decision affects dissertation direction, opening report, manuscript submission, grant/proposal, or expensive experiments;
- the user explicitly asks for multi-role conflict.

## Token-saving rules

1. Do not read all files by default.
2. Create a context manifest before extracting evidence.
3. Build a compact evidence pack.
4. Do not run all agents by default.
5. Use LIGHT for early ideation, STANDARD for formal topic validation, and HIGH_RISK only for consequential decisions.
6. Archive trigger decisions and final decisions in structured JSON.

## Output contract

Return a topic decision brief with these sections:

1. Selected mode and trigger reasons
2. Topic statement
3. Boundary and non-boundary
4. Novelty claim
5. Prior-art risk
6. Feasibility risk
7. Collapse-test result, if STANDARD or HIGH_RISK
8. Auditor findings, if HIGH_RISK
9. Multi-role conflict resolution, if HIGH_RISK
10. Minimum viable validation plan
11. Final decision
12. Next actions

## Forbidden behavior

Do not rewrite chapters, polish paragraphs, or generate manuscript patches. Those tasks belong to a separate manuscript-review skill.
