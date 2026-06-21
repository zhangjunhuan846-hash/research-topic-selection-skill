from __future__ import annotations

from typing import Any

DEFAULT_WEIGHTS = {
    "scientific_problem_strength": 0.18,
    "novelty_potential": 0.14,
    "collision_risk_inverse": 0.12,
    "experimental_feasibility": 0.14,
    "data_availability": 0.10,
    "mve_clarity": 0.12,
    "publication_potential": 0.10,
    "phd_continuity": 0.07,
    "ai_necessity": 0.03,
}


def critique_candidates(candidates: dict[str, Any], collision_plan: dict[str, Any]) -> dict[str, Any]:
    reviews = []
    for c in candidates.get("candidates", []):
        title = c.get("title", "").lower()
        scores = {
            "scientific_problem_strength": 85,
            "novelty_potential": 72,
            "collision_risk_inverse": 62,
            "experimental_feasibility": 76,
            "data_availability": 70,
            "mve_clarity": 68,
            "publication_potential": 72,
            "phd_continuity": 75,
            "ai_necessity": 55,
        }
        red_flags = []
        if "pilot" in title:
            scores.update({"scientific_problem_strength": 45, "mve_clarity": 35, "publication_potential": 30})
            red_flags.append("insufficient_corpus")
        if "composition" in title or "precursor" in title:
            scores.update({"scientific_problem_strength": 88, "mve_clarity": 82, "phd_continuity": 86})
        if "yield" in title:
            scores.update({"experimental_feasibility": 82, "publication_potential": 76})
        if "pore" in title:
            scores.update({"data_availability": 62, "experimental_feasibility": 70})
        total = sum(scores[k] * DEFAULT_WEIGHTS[k] for k in DEFAULT_WEIGHTS)
        reviews.append({
            "candidate_id": c["candidate_id"],
            "scores": scores,
            "weighted_score": round(float(total), 1),
            "red_flags": red_flags,
            "critic_notes": _notes(c, scores, red_flags),
        })
    return {"reviews": reviews}


def _notes(c: dict[str, Any], scores: dict[str, int], red_flags: list[str]) -> list[str]:
    notes = []
    if scores["ai_necessity"] < 60:
        notes.append("AI should be framed as secondary support rather than the main novelty.")
    if scores["collision_risk_inverse"] < 70:
        notes.append("Run full collision search before claiming novelty.")
    if red_flags:
        notes.append("Red flags require resolution before upgrade.")
    return notes


def decision_from_score(score: float, red_flags: list[str]) -> str:
    if "insufficient_corpus" in red_flags:
        return "NO-GO"
    if score >= 78:
        return "GO"
    if score >= 60:
        return "CONDITIONAL GO"
    return "NO-GO"
