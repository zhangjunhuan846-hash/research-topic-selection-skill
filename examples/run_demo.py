from pathlib import Path
from research_topic_selection_skill.cli import run_workflow

ROOT = Path(__file__).resolve().parents[1]
run_workflow(
    corpus=str(ROOT / "examples" / "input" / "demo_papers.csv"),
    constraints=str(ROOT / "examples" / "input" / "constraints.yaml"),
    out=str(ROOT / "outputs" / "demo_topic_selection"),
)
print("Demo complete. See outputs/demo_topic_selection/topic_selection_report.md")
