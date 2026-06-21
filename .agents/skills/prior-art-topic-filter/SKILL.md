# prior-art-topic-filter

## Purpose

Attack the candidate topic using existing literature. The goal is to determine whether the proposed topic is already done, trivially incremental, or still defensible.

## Checks

1. Direct duplication: has the exact question already been answered?
2. Conceptual duplication: has the same logic been applied under different wording?
3. System substitution: is the topic only changing LIB/SIB/SC, electrolyte, precursor, or descriptor label?
4. Dataset duplication: is the proposed meta-analysis already present in a review, benchmark, or database paper?
5. Method duplication: is the proposed workflow already standard?
6. Claim inflation: does the topic claim general rules from narrow evidence?

## Required output fields

- direct_prior_art
- adjacent_prior_art
- novelty_threats
- safe_space
- unsafe_claims
- recommended_boundary
- prior_art_risk_score: 0 to 5

## Decision guidance

- risk 0–1: weak prior-art threat;
- risk 2–3: manageable with boundary correction;
- risk 4: likely needs narrowing or pivot;
- risk 5: likely kill unless user can provide decisive new data.

## Output

Produce `prior_art_report.json`.
