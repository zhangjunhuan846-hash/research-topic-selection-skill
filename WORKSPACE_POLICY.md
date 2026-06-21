# Workspace Policy — Keep the Skill Clean

Recommended target path: `WORKSPACE_POLICY.md`

## Purpose

This repository should contain reusable topic-selection logic, not the user's private research history. Real runs, literature databases, advisor notes, and generated task outputs should live in a separate workspace.

## Recommended split

Use two locations:

```text
research-topic-selection-skill/      # reusable public or semi-public skill
research-topic-selection-workspace/  # private runs, data, outputs
```

## Keep inside the skill repository

```text
AGENTS.md
README.md
skills/
.agents/skills/
.agents/schemas/
.agents/prompts/
scripts/
examples/
docs/domain_packs/
tests/
requirements.txt
.gitignore
```

## Keep outside the skill repository

```text
tasks/*
literature/raw/*
literature/processed/*
runs/*
outputs/*
private advisor notes
full-text PDFs
Scopus/Web of Science exports
Zotero exports
unpublished datasets
```

## Why this matters

If historical task outputs remain inside the reusable skill folder, Codex or another agent may treat old decisions as active evidence. This causes context contamination, especially when old examples contain strong labels such as GO, KILL, recommended topic, advisor brief, or final roadmap.

## Clean-run checklist

Before using the skill on a new topic:

1. Confirm whether the user wants a fresh run or a continuation.
2. If fresh, do not read old `tasks/` outputs.
3. Use only the current prompt, current files, schemas, scripts, and relevant domain packs.
4. Write new outputs into a new task directory.
5. Record a `context_manifest.json` stating which sources were used.

## GitHub rule

Do not commit real literature databases, full-text PDFs, Excel sheets, or task outputs unless the repository is private and the user intentionally wants an archive repository rather than a clean reusable skill.
