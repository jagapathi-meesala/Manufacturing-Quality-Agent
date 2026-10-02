from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_required_explainability_headings():
    text=(ROOT/"EXPLAINABILITY.md").read_text()
    assert text.count("## Inputs and Data Sources")==1
    assert text.count("## Decision and Reasoning")==1
    assert text.count("## Limits and Constraints")==1
    assert "## Inputs\n" not in text and "## Decision\n" not in text and "## Limits\n" not in text

def test_declared_skills_exist():
    for name in ["quality-inspection","statistical-process-control","defect-triage","process-capability","quality-reporting"]:
        assert (ROOT/"skills"/name/"SKILL.md").is_file()
