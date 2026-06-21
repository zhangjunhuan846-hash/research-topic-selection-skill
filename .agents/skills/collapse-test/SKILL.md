# collapse-test

## Purpose

Try to make the topic collapse before the user invests effort. A good topic should survive at least one strong skeptical reduction.

## Required collapse attacks

Run at least five:

1. `material-substitution attack`: Is the topic just changing the material?
2. `descriptor-renaming attack`: Is the descriptor just a renamed known variable?
3. `confounding attack`: Are synthesis, structure, and performance inseparable?
4. `review-paper attack`: Would a review paper already answer this?
5. `unfalsifiable attack`: Can the hypothesis clearly fail?
6. `scope-bloat attack`: Is the topic too broad to become one paper?
7. `data-quality attack`: Are the conclusions limited by inconsistent reporting?
8. `instrument-access attack`: Does the idea require unavailable measurements?

## Survivability labels

- `survives`: attacks do not invalidate the topic.
- `survives_if_narrowed`: topic works only after narrowing.
- `needs_pivot`: core framing collapses but adjacent framing may work.
- `collapses`: topic should be killed.

## Output

Produce `collapse_test_report.json`.
