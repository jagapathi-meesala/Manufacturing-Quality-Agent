from __future__ import annotations
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FILES=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
REQUIRED_DIRS=["adapters","config","contracts","core","skills","tools","tests","verification"]
HEADINGS=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]

def audit():
    errors=[]
    for f in REQUIRED_FILES:
        if not (ROOT/f).is_file(): errors.append(f"missing file: {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT/d).is_dir(): errors.append(f"missing directory: {d}")
    p=ROOT/"EXPLAINABILITY.md"
    if p.exists():
        text=p.read_text(encoding="utf-8")
        for h in HEADINGS:
            if text.count(h)!=1: errors.append(f"heading count invalid: {h}")
            if h in text:
                section=text.split(h,1)[1].split("\n## ",1)[0]
                sentences=[s for s in re.split(r"(?<=[.!?])\s+",section.strip()) if s]
                if len(sentences)<2: errors.append(f"section has fewer than two sentences: {h}")
        for h in ["## Inputs","## Decision","## Limits"]:
            if any(line.strip() == h for line in text.splitlines()): errors.append(f"conflicting exact heading: {h}")
    return not errors,errors

if __name__=="__main__":
    ok,errors=audit()
    if ok: print("READINESS AUDIT: PASS")
    else:
        print("READINESS AUDIT: FAIL")
        for e in errors: print("-",e)
        raise SystemExit(1)
