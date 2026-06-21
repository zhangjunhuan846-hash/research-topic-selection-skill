from __future__ import annotations

import argparse
from pathlib import Path

from .candidates import build_problem_landscape, generate_candidates
from .collision import build_collision_plan
from .corpus import profile_corpus
from .mve import design_mves
from .report import build_decision_gate, write_outputs
from .scoring import critique_candidates
from .utils import ensure_dir, read_yaml, write_json


def run_workflow(corpus: str, constraints: str | None, out: str) -> dict:
    outdir = ensure_dir(out)
    state = ensure_dir(outdir / "state")
    constraints_data = read_yaml(constraints) if constraints else {}

    profile = profile_corpus(corpus, constraints_data)
    write_json(state / "01_corpus_profile.json", profile)

    landscape = build_problem_landscape(profile)
    write_json(state / "02_problem_landscape.json", landscape)

    candidates = generate_candidates(landscape)
    write_json(state / "03_candidate_topics.json", candidates)

    collision = build_collision_plan(candidates)
    write_json(state / "04_collision_plan.json", collision)

    reviews = critique_candidates(candidates, collision)
    write_json(state / "05_critic_review.json", reviews)

    mves = design_mves(candidates, reviews)
    write_json(state / "06_mve_designs.json", mves)

    decisions = build_decision_gate(candidates, reviews, mves)
    write_json(state / "07_decision_gate.json", decisions)

    memory = {
        "recommended_next_actions": [
            "Run full collision search for GO and CONDITIONAL GO candidates.",
            "Freeze MVE variables before generating experimental plan.",
            "Archive NO-GO reasons to avoid repeating discarded topics.",
        ],
        "top_candidate": decisions["decisions"][0] if decisions.get("decisions") else None,
    }
    write_json(state / "08_roadmap_memory.json", memory)
    write_outputs(outdir, profile, landscape, candidates, collision, reviews, mves, decisions)
    return decisions


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Research topic selection skill v3")
    sub = parser.add_subparsers(dest="cmd")
    run = sub.add_parser("run")
    run.add_argument("--corpus", required=True)
    run.add_argument("--constraints", default=None)
    run.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    if args.cmd == "run":
        result = run_workflow(args.corpus, args.constraints, args.out)
        print("Topic selection complete")
        for d in result.get("decisions", []):
            print(f"{d['decision']}: {d['candidate_id']} ({d['score']})")
    else:
        parser.print_help()
