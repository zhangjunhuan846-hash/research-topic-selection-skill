from __future__ import annotations

from typing import Any


def design_mves(candidates: dict[str, Any], reviews: dict[str, Any]) -> dict[str, Any]:
    review_map = {r["candidate_id"]: r for r in reviews.get("reviews", [])}
    mves = []
    for c in candidates.get("candidates", []):
        cid = c["candidate_id"]
        mves.append({
            "candidate_id": cid,
            "minimum_viable_experiment": _mve_text(c),
            "controls": ["fixed carbonization protocol", "baseline precursor", "repeat cells or repeated electrodes"],
            "primary_endpoint": c.get("target_metrics", ["target property"])[0] if c.get("target_metrics") else "evidence quality",
            "secondary_endpoints": c.get("target_metrics", [])[1:4],
            "success_criteria": _success_criteria(c),
            "kill_criteria": _kill_criteria(c, review_map.get(cid, {})),
            "master_stage_fit": "yes" if review_map.get(cid, {}).get("weighted_score", 0) >= 60 else "weak",
        })
    return {"mve_designs": mves}


def _mve_text(c: dict[str, Any]) -> str:
    title = c.get("title", "").lower()
    if "composition" in title:
        return "Prepare 3-5 composition-controlled biomass-analog precursors under a frozen carbonization and half-cell protocol; compare ICE and plateau fraction."
    if "yield" in title:
        return "Prepare a small activation severity series and evaluate yield-normalized gravimetric and volumetric performance."
    if "pore" in title:
        return "Prepare a pore-structure series and test whether pore descriptors remain predictive under controlled mass loading and thickness."
    return "Expand corpus and define a concrete material variable before experiment."


def _success_criteria(c: dict[str, Any]) -> list[str]:
    return [
        "effect direction remains stable under frozen protocol",
        "primary endpoint difference exceeds measurement noise",
        "result can be interpreted by at least one measured descriptor",
    ]


def _kill_criteria(c: dict[str, Any], review: dict[str, Any]) -> list[str]:
    return [
        "no controllable variable can be isolated",
        "core measurement cannot be repeated reliably",
        "full collision search finds direct same-question same-protocol paper",
    ]
