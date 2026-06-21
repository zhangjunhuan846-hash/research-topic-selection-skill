# feasibility-gate

## Purpose

Determine whether the user can realistically execute the topic with available data, experiments, models, or time.

## Checks

1. Data availability
2. Experimental controllability
3. Required characterization
4. Statistical power or sample size
5. Confounder control
6. Time and cost realism
7. Target journal realism
8. Minimum publishable unit

## Feasibility labels

- `ready`: can proceed now.
- `limited_but_workable`: can proceed with narrowed scope.
- `needs_key_resource`: blocked until a missing dataset/instrument/collaboration exists.
- `not_feasible`: cannot be executed under current constraints.

## Minimum viable validation

Always propose a minimal validation plan:

- minimum dataset or sample count;
- primary endpoint;
- secondary endpoints;
- necessary controls;
- failure criterion;
- decision threshold.

## Output

Produce `feasibility_report.json`.
