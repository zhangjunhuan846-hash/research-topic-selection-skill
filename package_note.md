# Package note — clean v3

This clean package keeps the reusable research-topic-selection workflow and removes private runtime data.

Included:
- tiered LIGHT / STANDARD / HIGH_RISK routing;
- topic intake, prior-art filtering, novelty gate, feasibility gate, collapse test, arbiter, and brief writer skills;
- high-risk auditor and conflict-review roles;
- JSON schemas, prompts, scripts, tests, and generic examples;
- state-isolation and workspace hygiene policies.

Excluded from this clean package:
- historical task outputs under `tasks/`;
- private literature exports under `literature/raw/` and `literature/processed/`;
- user-specific databases, spreadsheets, PDFs, Word files, slide decks, and run artifacts.

For real projects, keep runtime data in a separate private workspace and reference it explicitly when needed.
