from __future__ import annotations

import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")


def load_schema(rel: str) -> dict:
    root = Path(__file__).resolve().parents[1]
    return json.loads((root / rel).read_text(encoding="utf-8"))


def test_trigger_decision_schema_accepts_minimal_valid_object():
    schema = load_schema(".agents/schemas/trigger_decision.schema.json")
    obj = {
        "selected_mode": "STANDARD",
        "trigger_reasons": ["Formal topic decision requested."],
        "modules_to_run": ["research-topic-intake-router"],
        "modules_to_skip": [],
        "escalation_allowed_later": True,
    }
    jsonschema.validate(obj, schema)


def test_topic_decision_schema_accepts_required_decision_labels():
    schema = load_schema(".agents/schemas/topic_decision.schema.json")
    for label in ["GO", "REVISE", "NARROW", "PIVOT", "KILL"]:
        obj = {
            "final_decision": label,
            "refined_topic": "Controlled biomass hard-carbon topic.",
            "research_question": "Does the controlled variable change ICE under frozen protocol?",
            "hypothesis": "The controlled variable changes ICE through a measurable structural descriptor.",
            "main_rationale": "The topic has a clear variable, comparator, and failure condition.",
            "next_actions": ["Run prior-art collision check."],
        }
        jsonschema.validate(obj, schema)


def test_trigger_schema_rejects_invalid_mode():
    schema = load_schema(".agents/schemas/trigger_decision.schema.json")
    obj = {
        "selected_mode": "CASUAL",
        "trigger_reasons": ["Invalid mode should fail."],
        "modules_to_run": [],
        "modules_to_skip": [],
        "escalation_allowed_later": True,
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(obj, schema)
