from __future__ import annotations

import importlib.util
from pathlib import Path


def load_router():
    root = Path(__file__).resolve().parents[1]
    path = root / "scripts" / "route_evaluation_mode.py"
    spec = importlib.util.spec_from_file_location("route_evaluation_mode", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_light_request_cannot_override_thesis_consequence():
    router = load_router()
    decision = router.route(
        {
            "requested_mode": "LIGHT",
            "risk_level": "low",
            "decision_consequence": ["thesis_chapter"],
            "task_type": ["topic_screening"],
            "target_output": "quick impression",
        }
    )
    assert decision["selected_mode"] == "HIGH_RISK"


def test_high_request_can_escalate_low_consequence_task():
    router = load_router()
    decision = router.route(
        {
            "requested_mode": "HIGH_RISK",
            "risk_level": "low",
            "decision_consequence": [],
            "task_type": ["topic_screening"],
            "target_output": "quick impression",
        }
    )
    assert decision["selected_mode"] == "HIGH_RISK"


def test_formal_go_kill_output_routes_to_standard():
    router = load_router()
    decision = router.route(
        {
            "risk_level": "low",
            "decision_consequence": [],
            "task_type": ["decision_brief"],
            "target_output": "GO / REVISE / NARROW / PIVOT / KILL decision",
        }
    )
    assert decision["selected_mode"] == "STANDARD"
