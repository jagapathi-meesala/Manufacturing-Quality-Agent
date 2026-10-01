from pathlib import Path
import json, yaml
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]

def test_manifest_matches_open_gap_static_schema():
    manifest=yaml.safe_load((ROOT/"agent.yaml").read_text())
    schema=json.loads((ROOT/"verification/opengap_manifest_schema.json").read_text())
    errors=list(Draft202012Validator(schema).iter_errors(manifest))
    assert not errors, [e.message for e in errors]
    assert manifest["spec_version"]=="0.1.0"
    assert all((ROOT/"skills"/f"{s}.md").exists() for s in manifest["skills"])
    assert all((ROOT/"tools"/f"{t}.py").exists() for t in manifest["tools"])
