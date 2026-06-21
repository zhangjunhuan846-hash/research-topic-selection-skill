# README Supplement — GitHub/Codex Usage Notes

Recommended target path: `README_GITHUB_SUPPLEMENT.md`

## Clean installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run a basic package check:

```bash
python scripts/verify_skill_package.py .
```

Run tests:

```bash
pytest -q
```

## Recommended Codex prompt

```text
Use this repository as a research-topic-selection skill.
Start a fresh run unless I explicitly ask you to continue a previous task.
Do not use historical task outputs as evidence.
Use AGENTS.md, skills, schemas, scripts, and relevant domain packs only.
Evaluate the topic with the lowest sufficient mode, but do not let a low requested mode override high-consequence decisions.
```

## Data policy

This repository should not include private literature exports, old task outputs, unpublished datasets, or full-text PDFs. Put those files in a private workspace and reference them explicitly when needed.

## Minimal useful file additions

If the existing folder is already present, the most important additional files are:

1. `.gitignore`
2. `requirements.txt`
3. `AGENTS_APPEND_STATE_ISOLATION.md`
4. `WORKSPACE_POLICY.md`
5. `docs/domain_packs/biomass_hard_carbon_sib.md`
6. `scripts/verify_skill_package.py`
7. `tests/test_route_evaluation_mode.py`
8. `tests/test_schema_validation.py`

## Important maintenance rule

When a test fails, do not immediately change the test to pass. First decide whether the skill logic or schema should be corrected. Tests are intended to catch silent context contamination and unsafe mode downgrading.
