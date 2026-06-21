from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from .scoring import decision_from_score


def build_decision_gate(candidates: dict[str, Any], reviews: dict[str, Any], mves: dict[str, Any]) -> dict[str, Any]:
    cand_map = {c["candidate_id"]: c for c in candidates.get("candidates", [])}
    decisions = []
    for r in reviews.get("reviews", []):
        decision = decision_from_score(r["weighted_score"], r.get("red_flags", []))
        decisions.append({
            "candidate_id": r["candidate_id"],
            "title": cand_map.get(r["candidate_id"], {}).get("title", ""),
            "decision": decision,
            "score": r["weighted_score"],
            "conditions": _conditions(decision, r),
        })
    return {"decisions": sorted(decisions, key=lambda x: x["score"], reverse=True)}


def _conditions(decision: str, review: dict[str, Any]) -> list[str]:
    if decision == "GO":
        return ["perform collision search", "freeze MVE protocol", "record negative results"]
    if decision == "CONDITIONAL GO":
        return ["complete collision search", "sharpen MVE endpoint", "downgrade AI claims unless validated"]
    return ["do not commit before corpus/problem reframing"]


def write_outputs(outdir: str | Path, profile: dict[str, Any], landscape: dict[str, Any], candidates: dict[str, Any], collision: dict[str, Any], reviews: dict[str, Any], mves: dict[str, Any], decisions: dict[str, Any]) -> None:
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(decisions["decisions"]).to_csv(out / "candidate_scoreboard.csv", index=False)
    rows = []
    for p in collision.get("collision_plans", []):
        for q in p["precise_queries"]:
            rows.append({"candidate_id": p["candidate_id"], "query_type": "precise", "query": q})
        for q in p["broad_queries"]:
            rows.append({"candidate_id": p["candidate_id"], "query_type": "broad", "query": q})
    pd.DataFrame(rows).to_csv(out / "collision_queries.csv", index=False)
    pd.DataFrame(mves.get("mve_designs", [])).to_csv(out / "mve_plan.csv", index=False)
    report = render_report(profile, decisions, reviews, mves)
    (out / "topic_selection_report.md").write_text(report, encoding="utf-8")


def render_report(profile: dict[str, Any], decisions: dict[str, Any], reviews: dict[str, Any], mves: dict[str, Any]) -> str:
    lines = []
    lines.append("# Research Topic Selection Report\n")
    lines.append("## Corpus summary\n")
    lines.append(f"- Records: {profile.get('n_records')}\n")
    lines.append(f"- Year range: {profile.get('year_min')}–{profile.get('year_max')}\n")
    lines.append("- Dense themes: " + ", ".join(profile.get("dense_themes", [])) + "\n")
    lines.append("\n## Decision summary\n")
    for d in decisions.get("decisions", []):
        lines.append(f"### {d['decision']} · {d['title']}\n")
        lines.append(f"- Candidate ID: `{d['candidate_id']}`\n")
        lines.append(f"- Score: {d['score']}\n")
        lines.append("- Conditions: " + "; ".join(d.get("conditions", [])) + "\n")
    lines.append("\n## Method note\n")
    lines.append("This report is a structured decision aid. It does not replace full-text prior-art search or advisor review.\n")
    return "\n".join(lines)
