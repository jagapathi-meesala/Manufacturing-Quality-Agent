from __future__ import annotations
from statistics import mean, median, pstdev
from typing import Any, Mapping
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError
class InspectMeasurementsTool(ToolContract):
    metadata=ToolMetadata(name="inspect-measurements",description="Validate numeric manufacturing measurements and summarize their distribution.",input_schema={"type":"object","required":["measurements"],"properties":{"measurements":{"type":"array","items":{"type":"number"}}}})
    def validate(self,inputs:Mapping[str,Any])->None:
        super().validate(inputs); values=inputs.get("measurements")
        if not isinstance(values,list) or not values: raise ToolValidationError("measurements must be a non-empty list")
        if any(isinstance(v,bool) or not isinstance(v,(int,float)) for v in values): raise ToolValidationError("measurements must contain only finite numeric values")
        if any(v!=v or v in (float("inf"),float("-inf")) for v in values): raise ToolValidationError("measurements must contain only finite numeric values")
        if len(values)>10000: raise ToolValidationError("measurement list exceeds safety limit of 10000 records")
    def execute(self,inputs):
        values=[float(v) for v in inputs["measurements"]]; ordered=sorted(values)
        return ToolResult(True,self.metadata.name,{"count":len(values),"mean":mean(values),"median":median(values),"stddev_population":pstdev(values),"minimum":ordered[0],"maximum":ordered[-1],"range":ordered[-1]-ordered[0]})
