from __future__ import annotations
from typing import Iterable
from contracts.tool_contract import ToolContract

class ToolRegistry:
    def __init__(self, tools:Iterable[ToolContract]=()): self._tools={}
    def register(self,tool:ToolContract)->None:
        name=tool.metadata.name
        if not name or name in self._tools: raise ValueError(f"Tool name unavailable: {name}")
        self._tools[name]=tool
    def discover(self)->list[str]: return sorted(self._tools)
    def get(self,name:str)->ToolContract:
        try:return self._tools[name]
        except KeyError as exc: raise KeyError(f"Unknown tool: {name}") from exc
