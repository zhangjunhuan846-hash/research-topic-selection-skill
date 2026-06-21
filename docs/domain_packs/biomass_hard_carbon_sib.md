# Domain Pack — Biomass-Derived Hard Carbon for Alkali-Ion Storage

Recommended target path: `docs/domain_packs/biomass_hard_carbon_sib.md`

## Scope

Use this domain pack only when evaluating topics related to biomass-derived carbon, hard carbon, sodium-ion batteries, lithium-ion batteries, potassium-ion batteries, aqueous supercapacitors, or cross-system carbon descriptor analysis.

This file is a reusable field constraint pack. It is not a historical task record and should not silently import conclusions from previous projects.

## Baseline collision patterns

Treat the following framings as high collision risk unless the user provides a clearly narrower mechanism, control protocol, or validation design:

1. Generic biomass precursor screening.
2. "Biomass X derived carbon for SIB/LIB/SC" without a mechanistic variable.
3. Heteroatom-doped biomass carbon with only capacity/rate comparison.
4. KOH/NaOH/ZnCl2 activation optimized only by surface area and capacitance.
5. Cellulose/lignin ratio studies without fixed carbonization, particle size, ash, and electrode protocol.
6. Mineral/ash addition studies without separating catalytic carbonization, templating, and residual inorganic effects.
7. AI/ML topic where the model only predicts literature performance without a testable experimental loop.
8. Cross-system comparison that mixes LIB, SIB, and aqueous SC metrics without non-mixing rules.

## Preferred novelty axes

A topic is stronger if it uses at least one of these axes:

1. Composition-normalized precursor design under frozen processing conditions.
2. Ash/mineral identity, removal, or timing as a controlled mechanistic variable.
3. Closed-pore versus open-pore distinction linked to ICE, plateau capacity, or SEI penalty.
4. Protocol-frozen comparison separating material effect from electrode/test effect.
5. Cross-system descriptor conflict: for example, BET can benefit aqueous SC but penalize SIB/LIB ICE.
6. Literature-data model followed by minimum viable experiment, not only retrospective prediction.
7. Mechanistic validation using Raman/XRD/BET/XPS/electrochemistry with pre-registered decision rules.
8. Negative-result value: proving that a popular descriptor is confounded or non-transferable.

## Minimum controls for experimental topic evaluation

For SIB/LIB hard carbon topics, require these controls before a GO decision:

- same carbonization temperature;
- same heating rate;
- same dwell time;
- same atmosphere and gas flow condition if available;
- same precursor particle-size treatment or clear particle-size reporting;
- same washing/ash-removal protocol or explicit washed/unwashed comparison;
- same electrode composition;
- comparable active-material loading;
- same electrolyte system;
- same voltage window;
- same formation/current-density protocol;
- at least duplicate cells for minimum viable validation.

If these cannot be controlled, downgrade from GO to REVISE or NARROW.

## Core descriptors

Prioritize these descriptors when building the evidence pack:

- carbonization temperature;
- BET surface area;
- total pore volume;
- micropore volume when available;
- pore-size distribution when available;
- d002 from XRD;
- Raman ID/IG, with caution because interpretation is system-dependent;
- XPS N/O and other heteroatoms;
- ash content and inorganic species;
- first-cycle ICE;
- reversible capacity;
- plateau capacity or plateau fraction for SIB hard carbon;
- rate capability and cycling retention;
- electrode loading and test current.

## Non-mixing rules

Do not directly merge the following without labeling or stratification:

1. Half-cell and full-cell performance.
2. Ether and carbonate electrolytes in SIB unless electrolyte is the variable.
3. Mass-normalized capacitance and areal/volumetric capacitance.
4. Three-electrode and two-electrode supercapacitor data.
5. Low-loading and high-loading electrodes.
6. Different current density units without conversion.
7. Different voltage windows.
8. Activated carbon-like high-surface-area materials and hard-carbon plateau-storage materials if the target mechanism differs.

## Strong decision pattern

A strong topic usually has this structure:

- one mechanistic variable;
- frozen synthesis and test protocol;
- explicit comparator;
- pre-defined primary endpoint;
- small but defensible MVE;
- collision check against the closest prior art;
- one clear failure mode.

## Weak decision pattern

Downgrade or kill the topic if it depends mainly on:

- more samples alone;
- a new biomass label alone;
- higher BET alone;
- ML model performance without experimental consequence;
- post-hoc SHAP interpretation without controlled validation;
- broad claims across LIB/SIB/SC without system-specific rules.
