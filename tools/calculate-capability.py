from __future__ import annotations

from statistics import mean, pstdev
from typing import Any, Mapping
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError

class CalculateCapabilityTool(ToolContract):
    metadata=ToolMetadata(name="calculate-capability",description="Calculate Cp and Cpk from measurements and specification limits.",input_schema={"type":"object","required":["measurements","lower_spec","upper_spec"],"properties":{}})
    def validate(self,inputs:Mapping[str,Any])->None:
        super().validate(inputs); values=inputs.get("measurements")
        if not isinstance(values,list) or len(values)<2: raise ToolValidationError("at least two measurements are required")
        if any(isinstance(v,bool) or not isinstance(v,(int,float)) for v in values): raise ToolValidationError("measurements must be numeric")
        lo,hi=inputs.get("lower_spec"),inputs.get("upper_spec")
        if isinstance(lo,bool) or isinstance(hi,bool) or not isinstance(lo,(int,float)) or not isinstance(hi,(int,float)) or lo>=hi: raise ToolValidationError("lower_spec and upper_spec must be numeric and lower_spec < upper_spec")
        if pstdev([float(v) for v in values])==0: raise ToolValidationError("capability is undefined when process sigma is zero")
    def execute(self,inputs:Mapping[str,Any])->ToolResult:
        x=[float(v) for v in inputs["measurements"]]; mu=mean(x); s=pstdev(x); lo=float(inputs["lower_spec"]); hi=float(inputs["upper_spec"])
        cp=(hi-lo)/(6*s); cpu=(hi-mu)/(3*s); cpl=(mu-lo)/(3*s); cpk=min(cpu,cpl)
        return ToolResult(True,self.metadata.name,{"mean":mu,"sigma":s,"cp":cp,"cpu":cpu,"cpl":cpl,"cpk":cpk,"specification":{"lower":lo,"upper":hi},"interpretation":"Cpk reflects centering as well as spread; acceptance criteria must come from the applicable quality specification."})
