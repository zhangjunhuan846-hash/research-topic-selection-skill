#!/usr/bin/env python3
"""Verify a research-topic-selection skill package.

Usage:
    python scripts/verify_skill_package.py .

This script checks structure, JSON validity, Python syntax, and common data-hygiene risks.
It is intentionally conservative: warnings do not always mean the package is broken.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "skills",
    ".agents/skills",
    ".agents/schemas",
    "scripts",
]

PRIVATE_DATA_PATTERNS = [
    "literature/raw/*",
    "literature/processed/*.csv",
    "literature/processed/*.jsonl",
    "tasks/*/iterations/*/*.md",
    "tasks/*/iterations/*/*.json",
    "*.xlsx",
    "*.pdf",
    "*.docx",
    "*.pptx",
]


def iter_files(root: Path, patterns: Iterable[str]) -> list[Path]:
    hits: list[Path] = []
    for pattern in patterns:
        hits.extend(p for p in root.glob(pattern) if p.is_file())
    return sorted(set(hits))


def check_required(root: Path) -> list[str]:
    messages: list[str] = []
    for rel in REQUIRED_PATHS:
        path = root / rel
        if not path.exists():
            messages.append(f"ERROR missing required path: {rel}")
    return messages


def check_json(root: Path) -> list[str]:
    messages: list[str] = []
    for path in sorted(root.rglob("*.json")):
        if any(part in {".git", ".venv", "venv", "env"} for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            messages.append(f"ERROR invalid JSON: {path.relative_to(root)} :: {exc}")
    return messages


def check_python_syntax(root: Path) -> list[str]:
    messages: list[str] = []
    for path in sorted((root / "scripts").glob("*.py")) if (root / "scripts").exists() else []:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            messages.append(f"ERROR syntax error: {path.relative_to(root)} :: {exc}")
    return messages


def check_private_data(root: Path) -> list[str]:
    messages: list[str] = []
    hits = iter_files(root, PRIVATE_DATA_PATTERNS)
    real_hits = [p for p in hits if p.name != ".gitkeep"]
    if real_hits:
        messages.append("WARNING possible private/runtime data inside skill package:")
        for path in real_hits[:40]:
            messages.append(f"  - {path.relative_to(root)}")
        if len(real_hits) > 40:
            messages.append(f"  ... {len(real_hits) - 40} more")
    return messages


def check_agent_isolation(root: Path) -> list[str]:
    messages: list[str] = []
    agents = root / "AGENTS.md"
    if not agents.exists():
        return messages
    text = agents.read_text(encoding="utf-8").lower()
    required_terms = ["state isolation", "historical", "fresh", "tasks/"]
    if not all(term in text for term in required_terms):
        messages.append(
            "WARNING AGENTS.md may lack an explicit state-isolation rule. "
            "Add the contents of AGENTS_APPEND_STATE_ISOLATION.md near the top."
        )
    return messages


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Package root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    messages: list[str] = []
    messages += check_required(root)
    messages += check_json(root)
    messages += check_python_syntax(root)
    messages += check_private_data(root)
    messages += check_agent_isolation(root)

    if messages:
        print("\n".join(messages))
    else:
        print("OK: package structure, JSON files, and script syntax look clean.")

    return 1 if any(m.startswith("ERROR") for m in messages) else 0


if __name__ == "__main__":
    sys.exit(main())
