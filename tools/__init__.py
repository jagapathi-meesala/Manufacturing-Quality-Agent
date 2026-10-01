from importlib import import_module

_TOOL_MODULES = {
    "inspect-measurements": ("tools.inspect_measurements_impl", "InspectMeasurementsTool"),
    "calculate-spc": ("tools.calculate_spc_impl", "CalculateSPCTool"),
    "classify-defect": ("tools.classify_defect_impl", "ClassifyDefectTool"),
    "calculate-capability": ("tools.calculate_capability_impl", "CalculateCapabilityTool"),
    "generate-quality-report": ("tools.generate_quality_report_impl", "GenerateQualityReportTool"),
}

# The implementation modules use underscore names because Python module imports
# cannot address hyphenated filenames; OpenGAP still receives the canonical
# hyphenated tool filenames in agent.yaml.

def load_tool(name: str):
    module_name, class_name = _TOOL_MODULES[name]
    return getattr(import_module(module_name), class_name)

# Expose classes for the framework-independent core without vendor dependencies.
InspectMeasurementsTool = load_tool("inspect-measurements")
CalculateSPCTool = load_tool("calculate-spc")
ClassifyDefectTool = load_tool("classify-defect")
CalculateCapabilityTool = load_tool("calculate-capability")
GenerateQualityReportTool = load_tool("generate-quality-report")

__all__ = [
    "InspectMeasurementsTool", "CalculateSPCTool", "ClassifyDefectTool",
    "CalculateCapabilityTool", "GenerateQualityReportTool", "load_tool"
]
