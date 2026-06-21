#!/usr/bin/env python3
"""Conservative router for LIGHT / STANDARD / HIGH_RISK topic evaluation.

Recommended target path: `scripts/route_evaluation_mode.py`

Key policy:
- A user request may raise the evaluation mode.
- A user request must not lower the mode when consequences or risk are high.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

HIGH_CONSEQUENCES = {
    "thesis_chapter",
    "opening_report",
    "manuscript_submission",
    "grant_or_proposal",
    "expensive_experiment",
    "long_term_research_direction",
}
STANDARD_CONSEQUENCES = {"advisor_discussion", "group_meeting", "paper_plan"}

MODE_RANK = {"LIGHT": 0, "STANDARD": 1, "HIGH_RISK": 2}
RANK_MODE = {v: k for k, v in MODE_RANK.items()}

LIGHT_MODULES = [
    "research-topic-intake-router",
    "tiered-trigger-router",
    "prior-art-topic-filter:quick",
    "novelty-gate:quick",
    "topic-brief-writer:compact",
]

STANDARD_MODULES = [
    "research-topic-intake-router",
    "tiered-trigger-router",
    "literature-context-builder",
    "prior-art-topic-filter",
    "novelty-gate",
    "feasibility-gate",
    "collapse-test",
    "topic-arbiter",
    "topic-brief-writer",
    "workflow-archivist",
]

HIGH_MODULES = STANDARD_MODULES[:-3] + [
    "prior-art-auditor:if_needed",
    "methodology-auditor:if_needed",
    "feasibility-auditor:if_needed",
    "targeted-conflict-gate",
    "topic-arbiter",
    "topic-brief-writer",
    "workflow-archivist",
]


def _base_mode(intake: dict[str, Any], reasons: list[str]) -> str:
    risk = intake.get("risk_level", "low")
    consequences = set(intake.get("decision_consequence", []))
    target_output = str(intake.get("target_output", "")).lower()
    task_types = set(intake.get("task_type", []))

    if risk == "high" or consequences & HIGH_CONSEQUENCES:
        reasons.append("Decision consequence or risk level requires HIGH_RISK mode.")
        return "HIGH_RISK"

    formal_decision_requested = any(x in target_output for x in ["go", "revise", "narrow", "pivot", "kill"])
    if (
        risk == "medium"
        or consequences & STANDARD_CONSEQUENCES
        or "decision_brief" in task_types
        or formal_decision_requested
    ):
        reasons.append("Formal topic decision or advisor/paper-planning context requires STANDARD mode.")
        return "STANDARD"

    reasons.append("Early-stage or low-consequence screening detected.")
    return "LIGHT"


def route(intake: dict[str, Any]) -> dict[str, Any]:
    requested = intake.get("requested_mode")
    token_pref = intake.get("token_budget_preference", "balanced")
    risk = intake.get("risk_level", "low")

    reasons: list[str] = []
    non_reasons: list[str] = []

    base = _base_mode(intake, reasons)
    mode = base

    if requested in MODE_RANK:
        if MODE_RANK[requested] > MODE_RANK[base]:
            mode = requested
            reasons.append(f"User explicitly requested escalation to {requested} mode.")
        elif MODE_RANK[requested] == MODE_RANK[base]:
            reasons.append(f"User explicitly requested {requested} mode, matching the consequence-based route.")
        else:
            non_reasons.append(
                f"User requested {requested} mode, but consequence-based routing requires {base}; low-mode request cannot override high consequence."
            )

    if token_pref == "minimize" and mode != "LIGHT":
        non_reasons.append("Token preference is minimize; keep the selected mode tight and avoid unnecessary expansion.")

    if mode != "HIGH_RISK":
        non_reasons.append("No high-risk consequence was detected at intake; allow later escalation if gate scores require it.")

    modules = {"LIGHT": LIGHT_MODULES, "STANDARD": STANDARD_MODULES, "HIGH_RISK": HIGH_MODULES}[mode]
    all_modules = set(HIGH_MODULES)
    skipped = sorted(all_modules - set(modules))

    return {
        "selected_mode": mode,
        "initial_risk_level": risk,
        "trigger_reasons": reasons,
        "non_trigger_reasons": non_reasons,
        "modules_to_run": modules,
        "modules_to_skip": skipped,
        "auditors_to_consider": [
            "prior-art-auditor",
            "methodology-auditor",
            "feasibility-auditor",
        ] if mode == "HIGH_RISK" else [],
        "auditors_to_run": [],
        "escalation_allowed_later": mode != "HIGH_RISK",
        "escalation_watchpoints": [
            "prior_art_risk_score >= 4",
            "novelty_decision == fail",
            "feasibility_label in {needs_key_resource, not_feasible}",
            "collapse_test_report.survivability_label != survives",
            "user requests multi-role conflict review",
        ],
        "token_budget_note": "Use the lowest sufficient mode, but never let a low requested mode override high consequence.",
        "rationale": "Deterministic routing based on user request, risk level, decision consequence, and requested output.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Path to topic_intake.json")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Path to write trigger_decision.json")
    args = parser.parse_args()

    intake = json.loads(args.input.read_text(encoding="utf-8"))
    decision = route(intake)
    text = json.dumps(decision, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
