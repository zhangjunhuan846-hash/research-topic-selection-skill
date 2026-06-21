# Architecture

`research-topic-selection-skill-v3` uses a JSON-first pipeline. The main design goal is not to maximize generated text, but to make topic decisions auditable.

## State files

Each agent writes one state file. Later agents should consume only the state files they need.

## Decision philosophy

The workflow is intentionally conservative. It should downgrade topics that are merely AI-wrapped or that cannot define a minimum viable experiment.
