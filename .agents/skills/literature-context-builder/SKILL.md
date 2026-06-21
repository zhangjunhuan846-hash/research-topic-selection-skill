# literature-context-builder

## Purpose

Build a compact evidence context for topic validation without consuming full-text token budgets unnecessarily.

## Core tasks

1. Define the literature boundary.
2. Separate core prior art from adjacent prior art.
3. Identify review papers, benchmark papers, and direct competitors.
4. Record the search/query provenance if available.
5. Compress evidence into an evidence pack.

## Evidence tiers

- `Tier 0`: title/abstract-level evidence only.
- `Tier 1`: selected full-text evidence from key papers.
- `Tier 2`: manually extracted quantitative dataset or experimental data.

## Required distinctions

Always distinguish:

- direct prior art vs adjacent prior art;
- evidence from abstracts vs full text;
- claims supported by data vs claims inferred by the agent;
- topic novelty vs wording novelty.

## Output

Produce:

- `context_manifest.json`
- `evidence_pack.json`

following `.agents/schemas/context_manifest.schema.json` and `.agents/schemas/evidence_pack.schema.json`.
