# Research Topic Selection Skill v3

面向“研究型论文选题”的低 token、多阶段、可证伪工作流。v3 的核心变化是加入 **tiered triggering / 分级触发机制**：先用轻量流程做初筛，只有在证据风险、投入成本或决策后果足够高时，才升级到标准评估或高风险多角色对抗评审。

本包只处理研究型论文选题，不执行 manuscript review、章节改写、patch writing 或语言润色。

## 这个 skill 解决什么问题

它用于判断一个研究型论文选题是否值得继续推进，核心问题包括：

1. 这个题目是否只是换材料、换体系、换说法？
2. 已有文献是否已经做过类似工作？
3. 科学问题是否足够清晰，而不是“材料堆砌”或“数据堆砌”？
4. 是否存在可检验假设、最小可行验证方案和明确失败标准？
5. 选题是否能被压缩成一篇有发表潜力的论文，而不是无限扩张成综述或项目申请书？
6. 应该使用轻量模式、标准模式，还是高风险对抗评审？

## 分级触发总览

```text
LIGHT / 轻量模式
用于：早期想法、多个候选题初筛、局部范围判断
特点：不启动多角色对抗；只做低成本硬过滤和简短判断

STANDARD / 标准模式
用于：准备向导师汇报、准备投入系统文献或小规模数据分析
特点：完整跑 prior-art、novelty、feasibility、collapse-test 和 topic-arbiter

HIGH_RISK / 高风险模式
用于：博士论文方向、开题、投稿策略、基金/课题设计、昂贵实验决策
特点：在标准模式基础上，追加专业 auditor，并触发 Advocate / Skeptic / Arbiter 对抗裁决
```

## 主工作流

```text
research-topic-intake-router
→ tiered-trigger-router
→ literature-context-builder, as required by mode
→ prior-art-topic-filter
→ novelty-gate
→ feasibility-gate, STANDARD/HIGH_RISK
→ collapse-test, STANDARD/HIGH_RISK
→ prior-art-auditor, HIGH_RISK optional
→ methodology-auditor, HIGH_RISK optional
→ feasibility-auditor, HIGH_RISK optional
→ targeted-conflict-gate, HIGH_RISK
→ topic-arbiter
→ topic-brief-writer
→ workflow-archivist
```

## 三档模式的默认执行范围

| 模式 | 典型用途 | 默认模块 | 是否多角色对抗 |
|---|---|---|---|
| `LIGHT` | 早期想法、候选题粗筛、判断是否值得继续查 | intake、tiered route、prior-art quick scan、novelty quick gate、brief | 否 |
| `STANDARD` | 正式判断单个选题是否值得推进 | intake、context、prior-art、novelty、feasibility、collapse-test、arbiter、brief、archive | 默认否 |
| `HIGH_RISK` | 开题/投稿/基金/大规模实验前决策 | STANDARD 全部模块 + auditors + conflict gate | 是 |

## 升级规则

从 `LIGHT` 升级到 `STANDARD`，如果出现任一情况：

- 选题要提交导师或用于组会汇报；
- 用户要求输出 GO / REVISE / NARROW / PIVOT / KILL；
- 需要判断 feasibility、数据量、实验设计或最小验证方案；
- 出现直接 prior art、强相似工作或明显 scope bloat；
- novelty 只能给出 conditional pass。

从 `STANDARD` 升级到 `HIGH_RISK`，如果出现任一情况：

- prior-art risk score ≥ 4；
- novelty decision = `fail`，但用户仍考虑推进；
- feasibility label = `needs_key_resource` 或 `not_feasible`；
- collapse-test 返回 `survives_if_narrowed`、`needs_pivot` 或 `collapses`；
- 该决策会影响博士课题方向、开题、投稿、基金或昂贵实验投入；
- 用户明确要求多角色冲突评审。

## 输出结果

最终输出不是一篇初稿，而是一个 research-topic decision brief：

```text
GO / REVISE / NARROW / PIVOT / KILL
```

并附带：

- 题目一句话版本；
- novelty claim；
- prior-art risk；
- feasibility risk；
- collapse-test 结果；
- 分级触发理由；
- 最小可行验证方案；
- 下一步执行清单。

## 与 v2 的区别

v2 已经把 manuscript review 从主线中剥离。v3 进一步加入了 **分级触发机制**：

- 轻量问题不再默认跑完整链路；
- 标准问题保留完整选题判断；
- 高风险问题才启动 auditor 和 Advocate / Skeptic / Arbiter；
- 每次升级或不升级都必须给出 `trigger_decision.json` 记录，避免随意开 agent 浪费 token。

## 目录结构

```text
.
├── AGENTS.md
├── README.md
├── package_note.md
├── .agents/
│   ├── skills/
│   ├── schemas/
│   ├── prompts/
│   └── subagents/
├── skills/                       # mirrored skills for compatibility
├── scripts/
├── examples/
└── tasks/
```

## Codex 使用示例

```text
Use $research-topic-selection-skill to validate this research topic:
"Composition-normalized screening of biomass hard-carbon precursors for sodium-ion battery first-cycle ICE."

Inputs:
- candidate topic: ...
- field boundary: biomass-derived hard carbon / sodium-ion batteries
- available data: Scopus abstracts, cleaned descriptor table, limited experimental validation
- target output: GO / REVISE / NARROW / PIVOT / KILL decision brief

Use tiered triggering. Start with the lowest sufficient mode and escalate only if the trigger rules require it.
Run only the topic-selection workflow. Do not perform manuscript review.
```

## How to run divergent ideation

Use this mode when generated topics are too repetitive, too concentrated on one variable path, or need a broader research-direction pool before formal GO / REVISE / NARROW / PIVOT / KILL evaluation.

Example prompt:

```text
Use $research-topic-selection-skill in Divergent Ideation Mode. My current topics are too repetitive. Generate a broad topic pool across 8 research lenses, avoid crowded hard-carbon axes, run light collision pre-screen, and output topic_pool.md, topic_pool.json, and divergent_ideation_report.md.
```

If using Codex CLI:

```text
codex exec -C . "Use the research-topic-selection-skill in Divergent Ideation Mode. Generate a diverse topic pool for biomass/model hard-carbon SIB research, avoiding cellulose:lignin ratio, Al2O3 addition, natural biomass impurity removal, and broad precursor screening as main novelty axes. Output topic_pool.md, topic_pool.json, and divergent_ideation_report.md."
```

Divergent Ideation Mode follows this order:

```text
topic intake
→ identify crowded axes and unsafe novelty axes
→ generate candidates across 8 independent lenses
→ enforce diversity constraints
→ light collision pre-screen
→ topic family deduplication
→ shortlist 3–5 candidates for deeper evaluation
```

It must output a topic pool, not a final single topic. Formal topic decisions still use the existing GO / REVISE / NARROW / PIVOT / KILL workflow after collision screening and narrowing.
