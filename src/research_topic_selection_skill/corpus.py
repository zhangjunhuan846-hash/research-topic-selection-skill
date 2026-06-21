from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd

KEYWORDS = [
    "biomass", "hard carbon", "porous carbon", "supercapacitor", "sodium", "lithium",
    "activation", "carbonization", "pore", "BET", "d002", "Raman", "machine learning",
    "Bayesian", "optimization", "yield", "precursor", "lignin", "cellulose", "hemicellulose",
]


def profile_corpus(corpus_path: str | Path, constraints: dict[str, Any] | None = None) -> dict[str, Any]:
    df = pd.read_csv(corpus_path)
    constraints = constraints or {}
    text = (df.get("title", "").fillna("") + " " + df.get("abstract", "").fillna("")).str.lower()
    keyword_counts = {kw: int(text.str.contains(kw.lower(), regex=False).sum()) for kw in KEYWORDS}
    years = pd.to_numeric(df.get("year", pd.Series(dtype=float)), errors="coerce")
    missing = {col: int(df[col].isna().sum()) for col in df.columns}
    include = constraints.get("include_keywords", [])
    exclude = constraints.get("exclude_keywords_by_default", constraints.get("exclude_keywords", []))
    scope_hits = {kw: int(text.str.contains(str(kw).lower(), regex=False).sum()) for kw in include + exclude}
    return {
        "n_records": int(len(df)),
        "columns": list(df.columns),
        "year_min": None if years.dropna().empty else int(years.min()),
        "year_max": None if years.dropna().empty else int(years.max()),
        "missing_by_column": missing,
        "keyword_counts": keyword_counts,
        "scope_keyword_hits": scope_hits,
        "dense_themes": [k for k, v in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True) if v > 0][:8],
        "data_quality_notes": _quality_notes(df),
    }


def _quality_notes(df: pd.DataFrame) -> list[str]:
    notes = []
    for col in ["title", "abstract", "year"]:
        if col not in df.columns:
            notes.append(f"missing required/recommended column: {col}")
    if len(df) < 30:
        notes.append("small corpus; use as pilot only")
    return notes
