from __future__ import annotations
from statistics import mean, pstdev
from typing import Any, Mapping
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError
class CalculateSPCTool(ToolContract):
    metadata=ToolMetadata(name="calculate-spc",description="Calculate mean, sigma, control limits, and out-of-control observations using three-sigma limits.",input_schema={"type":"object","required":["measurements"],"properties":{"measurements":{"type":"array","items":{"type":"number"}}}})
    def validate(self,inputs:Mapping[str,Any])->None:
        super().validate(inputs); values=inputs.get("measurements")
        if not isinstance(values,list) or len(values)<2: raise ToolValidationError("at least two measurements are required")
        if any(isinstance(v,bool) or not isinstance(v,(int,float)) for v in values): raise ToolValidationError("measurements must be numeric")
        if any(v!=v or v in (float("inf"),float("-inf")) for v in values): raise ToolValidationError("measurements must be finite")
    def execute(self,inputs):
        values=[float(v) for v in inputs["measurements"]]; mu=mean(values); sigma=pstdev(values); ucl=mu+3*sigma; lcl=mu-3*sigma
        flags=[{"index":i,"value":v,"reason":"outside_3_sigma_limits"} for i,v in enumerate(values) if v<lcl or v>ucl]
        return ToolResult(True,self.metadata.name,{"mean":mu,"sigma":sigma,"ucl":ucl,"lcl":lcl,"out_of_control":flags,"out_of_control_count":len(flags),"method":"three-sigma individual-observation limits","note":"For production SPC, subgrouping and a validated control-chart method may be required."})
