from __future__ import annotations
from typing import Any, Mapping
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError
class GenerateQualityReportTool(ToolContract):
    metadata=ToolMetadata(name="generate-quality-report",description="Assemble structured findings into a traceable quality report without inventing missing measurements.",input_schema={"type":"object","required":["title","findings"],"properties":{}})
    def validate(self,inputs:Mapping[str,Any])->None:
        super().validate(inputs)
        if not isinstance(inputs.get("title"),str) or not inputs["title"].strip(): raise ToolValidationError("title must be non-empty")
        if not isinstance(inputs.get("findings"),list) or any(not isinstance(x,str) or not x.strip() for x in inputs["findings"]): raise ToolValidationError("findings must be a list of non-empty strings")
    def execute(self,inputs):
        return ToolResult(True,self.metadata.name,{"title":inputs["title"].strip(),"findings":[x.strip() for x in inputs["findings"]],"status":"generated","traceability":"Only supplied findings are included; no unsupported measurements or causes are inferred."})
