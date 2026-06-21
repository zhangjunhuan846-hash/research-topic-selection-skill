# feasibility-auditor

## Purpose

Audit whether the topic can realistically be executed under current resources, data access, instruments, collaboration, and time constraints. This is stricter than `feasibility-gate` and is used only in HIGH_RISK mode.

## When to use

Use when:

- feasibility label is `needs_key_resource` or `not_feasible`;
- the topic requires expensive or unavailable characterization;
- the topic requires long-cycle experiments;
- the available dataset may be too small or too noisy;
- the user is deciding whether to invest major time or lab resources.

## Audit questions

1. What exact resource is rate-limiting?
2. Can the topic be narrowed into a minimum viable validation?
3. Which measurements are essential versus optional?
4. What timeline is realistic?
5. What lower-cost substitute experiment or analysis exists?
6. What result would justify stopping early?

## Output

Return:

- resource_bottlenecks
- essential_vs_optional_requirements
- minimum_viable_execution_plan
- early_stop_rules
- feasibility_downgrade_or_rescue_path
- recommended_decision_effect
