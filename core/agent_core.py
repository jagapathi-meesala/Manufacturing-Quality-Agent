from __future__ import annotations
from typing import Any, Mapping
from adapters.registry import ToolRegistry
from contracts.tool_contract import ToolResult
from tools import CalculateCapabilityTool, CalculateSPCTool, ClassifyDefectTool, GenerateQualityReportTool, InspectMeasurementsTool

class AgentCore:
    """Domain orchestration independent of AI/vendor frameworks."""
    def __init__(self, registry:ToolRegistry|None=None):
        self.registry=registry or self._default_registry()
    @staticmethod
    def _default_registry()->ToolRegistry:
        registry=ToolRegistry()
        for tool in [InspectMeasurementsTool(),CalculateSPCTool(),ClassifyDefectTool(),CalculateCapabilityTool(),GenerateQualityReportTool()]: registry.register(tool)
        return registry
    def execute(self,tool_name:str,inputs:Mapping[str,Any])->ToolResult:
        if not isinstance(tool_name,str) or not tool_name.strip(): return ToolResult(False,"unknown",error="validation_error: tool_name must be non-empty")
        try:return self.registry.get(tool_name).run(inputs)
        except KeyError as exc:return ToolResult(False,tool_name,error=f"tool_not_found: {exc}")
    def tools(self)->list[str]: return self.registry.discover()
