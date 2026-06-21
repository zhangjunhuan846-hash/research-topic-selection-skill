# novelty-gate

## Purpose

Determine whether the candidate topic has a defensible novelty claim.

## Novelty types

Classify novelty as one or more:

- `new_problem_definition`
- `new_descriptor_framework`
- `new_cross-system_comparison`
- `new_dataset_or_benchmark`
- `new_experimental_control`
- `new_mechanistic_test`
- `new_theory_or_model`
- `new_application_boundary`

## Novelty quality levels

- `weak`: mostly wording or material substitution.
- `moderate`: useful boundary or descriptor refinement.
- `strong`: changes the scientific question or testable mechanism.
- `very_strong`: creates a new benchmark, mechanism, or decision framework.

## Red flags

Reject or downgrade novelty if:

- novelty depends only on a rare biomass precursor;
- novelty depends only on adding another dataset column;
- novelty has no falsifiable hypothesis;
- novelty is only a review-style narrative without testable discrimination;
- novelty ignores confounding processing variables.

## Output

Produce `novelty_gate_report.json` with:

- novelty_statement_one_sentence
- novelty_type
- novelty_quality
- novelty_rationale
- weakest_link
- required_evidence_to_defend
- novelty_decision: `pass`, `conditional_pass`, or `fail`
