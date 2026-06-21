from __future__ import annotations

from typing import Any


def build_problem_landscape(profile: dict[str, Any]) -> dict[str, Any]:
    counts = profile.get("keyword_counts", {})
    problems = []
    if counts.get("yield", 0) or counts.get("activation", 0):
        problems.append({
            "problem_id": "P-YIELD-PERFORMANCE",
            "problem": "High surface area or high capacity reports often ignore carbon yield, activation cost, and volumetric relevance.",
            "material_variables": ["activation severity", "carbonization temperature", "precursor composition", "ash removal"],
            "measurable_endpoints": ["carbon yield", "BET", "volumetric capacitance", "ICE"],
        })
    if counts.get("hard carbon", 0) or counts.get("sodium", 0):
        problems.append({
            "problem_id": "P-HARD-CARBON-PRECURSOR",
            "problem": "Biomass labels are weak descriptors; composition-normalized precursor variables may better explain hard-carbon ICE and plateau capacity.",
            "material_variables": ["cellulose/lignin ratio", "ash content", "washing", "carbonization temperature"],
            "measurable_endpoints": ["ICE", "reversible capacity", "plateau fraction", "d002", "ID/IG"],
        })
    if counts.get("pore", 0) or counts.get("supercapacitor", 0):
        problems.append({
            "problem_id": "P-ION-ACCESSIBILITY",
            "problem": "Gas-accessible surface area and electrochemically accessible pore volume can diverge across aqueous supercapacitor electrodes.",
            "material_variables": ["pore size distribution", "activation route", "mass loading", "electrode density"],
            "measurable_endpoints": ["specific capacitance", "rate retention", "thickness", "compacted density"],
        })
    return {"problems": problems, "notes": ["Science-first problem map generated from corpus keyword profile."]}


def generate_candidates(landscape: dict[str, Any]) -> dict[str, Any]:
    candidates = []
    for p in landscape.get("problems", []):
        if p["problem_id"] == "P-YIELD-PERFORMANCE":
            candidates.append({
                "candidate_id": "CAND-YIELD-NORM-SC",
                "title": "Yield-normalized design of biomass porous carbon for aqueous supercapacitors",
                "science_question": "Can activation benefits be evaluated by a yield-normalized, electrode-relevant metric rather than gravimetric capacitance alone?",
                "hypothesis": "Moderate activation that preserves yield and electrode density can outperform extreme activation under practical metrics.",
                "variables": p["material_variables"],
                "target_metrics": p["measurable_endpoints"],
                "ai_role": "optional: literature meta-analysis and candidate prioritization, not primary novelty",
            })
        elif p["problem_id"] == "P-HARD-CARBON-PRECURSOR":
            candidates.append({
                "candidate_id": "CAND-COMP-NORM-HC",
                "title": "Composition-normalized screening of biomass hard-carbon precursors",
                "science_question": "Do cellulose/lignin/ash descriptors explain SIB hard-carbon ICE better than biomass labels?",
                "hypothesis": "Composition-normalized descriptors reduce label noise and improve early-cycle performance interpretation.",
                "variables": p["material_variables"],
                "target_metrics": p["measurable_endpoints"],
                "ai_role": "useful: descriptor ranking and small-data modeling after frozen experimental protocol",
            })
        elif p["problem_id"] == "P-ION-ACCESSIBILITY":
            candidates.append({
                "candidate_id": "CAND-ACCESSIBLE-PORE-SC",
                "title": "Ion-accessible pore descriptors for aqueous supercapacitor biomass carbons",
                "science_question": "Which pore descriptors remain predictive under realistic mass loading and electrode thickness?",
                "hypothesis": "Ion-accessible pore volume and electrode engineering descriptors outperform BET alone for practical SC performance.",
                "variables": p["material_variables"],
                "target_metrics": p["measurable_endpoints"],
                "ai_role": "useful: multi-descriptor correlation and uncertainty-aware screening",
            })
    if not candidates:
        candidates.append({
            "candidate_id": "CAND-PILOT-REVIEW",
            "title": "Pilot corpus expansion before topic commitment",
            "science_question": "Is the current corpus sufficient to define a materials-science research gap?",
            "hypothesis": "The current corpus is too small or too sparse; expand and re-run the workflow.",
            "variables": [],
            "target_metrics": [],
            "ai_role": "not recommended until corpus improves",
        })
    return {"candidates": candidates}
