from __future__ import annotations

from typing import Any


def build_collision_plan(candidates: dict[str, Any]) -> dict[str, Any]:
    plans = []
    for c in candidates.get("candidates", []):
        title = c["title"]
        variables = " ".join(c.get("variables", []))
        metrics = " ".join(c.get("target_metrics", []))
        base = f'"{title}" OR ({variables} {metrics})'
        precise = [
            f'{base} biomass carbon review',
            f'{base} hard carbon sodium ion battery',
            f'{base} supercapacitor electrode engineering',
            f'{base} precursor composition lignin cellulose',
            f'{base} carbon yield activation performance',
            f'{base} BET d002 ID/IG ICE capacity',
            f'{base} machine learning materials descriptor',
            f'{base} Bayesian optimization carbon materials',
            f'{base} mass loading electrode thickness density',
            f'{base} structure property relationship',
        ]
        broad = [
            "biomass derived carbon energy storage descriptor review",
            "hard carbon precursor composition sodium ion battery",
            "porous carbon aqueous supercapacitor practical metrics",
            "machine learning biomass carbon energy storage",
            "carbon material Bayesian optimization literature data",
        ]
        plans.append({
            "candidate_id": c["candidate_id"],
            "precise_queries": precise,
            "broad_queries": broad,
            "direct_collision_definition": "Same material family, same controllable variable, same target metric, and same validation logic.",
            "partial_collision_definition": "Same material family or metric, but different variable, dataset, protocol, or mechanism.",
            "adjacent_acceptable_definition": "Related work that motivates or bounds the topic but does not answer the central science question.",
        })
    return {"collision_plans": plans}
