# AGENTS.md Addendum — State Isolation and Data Hygiene

Paste this section near the top of the root `AGENTS.md`, directly after the Mission section.

## State isolation rule

For every new research-topic selection request, start from a fresh context unless the user explicitly says one of the following:

- continue the exact previous task;
- compare with a previous iteration;
- reuse a named evidence pack;
- use task `<task_name>` as context;
- resume from a specific file path.

Default behavior for a new request:

1. Create or assume a fresh task directory.
2. Treat existing files under `tasks/`, `runs/`, `outputs/`, and `literature/processed/` as historical records, not active evidence.
3. Do not reuse old topic scores, old GO/KILL decisions, previous advisor briefs, or previous candidate pools as evidence for the new topic.
4. Reuse only reusable methodology files: `AGENTS.md`, `skills/`, `.agents/skills/`, `.agents/schemas/`, `scripts/`, `prompts/`, and approved files under `docs/domain_packs/`.
5. If a previous task appears relevant, mention it as an optional comparison source and ask for explicit permission before using it.

## Evidence-source hierarchy

Use this hierarchy when deciding what can influence a new topic decision:

1. User's current prompt and explicitly supplied files.
2. Current task intake file.
3. Approved domain pack, only if it matches the current field.
4. Fresh prior-art search or explicitly provided literature evidence.
5. Historical task outputs, only when explicitly requested.

Historical outputs must never silently override the current prompt.

## Domain-pack rule

Domain packs are reusable background constraints, not project memory. A domain pack may provide known collision patterns, methodological controls, or field-specific feasibility constraints, but it must not decide the final topic by itself.

## Private-data rule

Do not assume private databases, unpublished advisor discussions, or old workspaces are part of the active task unless the user explicitly attaches them or names them.

## Reset phrase

If the user says any of the following, ignore all historical task context and begin a clean evaluation:

- "重新开始"
- "不要参考之前的案例"
- "新课题"
- "clean run"
- "fresh task"
- "from scratch"

The output should then include: `context_status: fresh_run`.
