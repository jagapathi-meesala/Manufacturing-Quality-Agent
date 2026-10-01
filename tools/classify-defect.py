from __future__ import annotations

from typing import Any, Mapping
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError


SEVERITY={"critical":4,"major":3,"minor":2,"observation":1}

class ClassifyDefectTool(ToolContract):
    metadata=ToolMetadata(name="classify-defect",description="Classify a manufacturing defect from measurable impact and recurrence evidence.",input_schema={"type":"object","required":["defect_type","severity","occurrences","safety_impact"],"properties":{}})
    def validate(self,inputs:Mapping[str,Any])->None:
        super().validate(inputs)
        if not isinstance(inputs.get("defect_type"),str) or not inputs["defect_type"].strip(): raise ToolValidationError("defect_type must be a non-empty string")
        if inputs.get("severity") not in SEVERITY: raise ToolValidationError("severity must be critical, major, minor, or observation")
        if isinstance(inputs.get("occurrences"),bool) or not isinstance(inputs.get("occurrences"),int) or inputs["occurrences"]<0: raise ToolValidationError("occurrences must be a non-negative integer")
        if not isinstance(inputs.get("safety_impact"),bool): raise ToolValidationError("safety_impact must be boolean")
    def execute(self,inputs:Mapping[str,Any])->ToolResult:
        severity=inputs["severity"]; occ=inputs["occurrences"]; safety=inputs["safety_impact"]
        if safety or severity=="critical": priority="immediate"
        elif severity=="major" or occ>=5: priority="high"
        elif severity=="minor" or occ>0: priority="medium"
        else: priority="low"
        return ToolResult(True,self.metadata.name,{"defect_type":inputs["defect_type"].strip(),"severity":severity,"severity_score":SEVERITY[severity],"occurrences":occ,"safety_impact":safety,"priority":priority,"recommended_action":"quarantine and human review" if priority=="immediate" else "contain, investigate root cause, and verify corrective action"})
