from pathlib import Path

from research_topic_selection_skill.cli import run_workflow


def test_workflow_runs(tmp_path):
    root = Path(__file__).resolve().parents[1]
    decisions = run_workflow(
        corpus=str(root / "examples" / "input" / "demo_papers.csv"),
        constraints=str(root / "examples" / "input" / "constraints.yaml"),
        out=str(tmp_path / "out"),
    )
    assert decisions["decisions"]
    assert (tmp_path / "out" / "topic_selection_report.md").exists()
    assert (tmp_path / "out" / "state" / "03_candidate_topics.json").exists()


def test_decision_values(tmp_path):
    root = Path(__file__).resolve().parents[1]
    decisions = run_workflow(
        corpus=str(root / "examples" / "input" / "demo_papers.csv"),
        constraints=str(root / "examples" / "input" / "constraints.yaml"),
        out=str(tmp_path / "out2"),
    )
    values = {d["decision"] for d in decisions["decisions"]}
    assert values <= {"GO", "CONDITIONAL GO", "NO-GO"}


def test_scoreboard_created(tmp_path):
    root = Path(__file__).resolve().parents[1]
    run_workflow(
        corpus=str(root / "examples" / "input" / "demo_papers.csv"),
        constraints=str(root / "examples" / "input" / "constraints.yaml"),
        out=str(tmp_path / "out3"),
    )
    assert (tmp_path / "out3" / "candidate_scoreboard.csv").exists()
    assert (tmp_path / "out3" / "collision_queries.csv").exists()
    assert (tmp_path / "out3" / "mve_plan.csv").exists()
