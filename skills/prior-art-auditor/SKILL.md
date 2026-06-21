# prior-art-auditor

## Purpose

Provide a high-risk audit of whether the candidate topic is already covered by existing literature. This is stricter than `prior-art-topic-filter` and is used only in HIGH_RISK mode.

## When to use

Use when:

- prior-art risk score is 4 or 5;
- direct competitors exist;
- the proposed novelty may be only a wording change;
- a review, benchmark, or database paper may already answer the question;
- the decision affects thesis, opening report, submission, grant/proposal, or major experiments.

## Audit questions

1. What is the closest existing paper or review logic?
2. Does the proposed topic ask a genuinely different scientific question?
3. Which novelty claim would fail under reviewer scrutiny?
4. Which narrowed claim remains defensible?
5. What exact prior-art search or reading is still required before proceeding?

## Output

Return:

- direct_overlap_assessment
- strongest_prior_art_threat
- unsafe_novelty_claims
- defensible_safe_space
- required_literature_checks
- recommended_decision_effect
