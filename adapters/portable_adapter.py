from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Mapping
from core.agent_core import AgentCore

class AgentAdapter(ABC):
    """Framework-neutral adapter contract. Vendor SDKs are intentionally not imported."""
    @abstractmethod
    def invoke(self, tool_name:str, inputs:Mapping[str,Any])->dict[str,Any]: ...

class PortableAdapter(AgentAdapter):
    def __init__(self, agent:AgentCore): self.agent=agent
    def invoke(self, tool_name:str, inputs:Mapping[str,Any])->dict[str,Any]:
        result=self.agent.execute(tool_name,inputs)
        return {"ok":result.ok,"tool":result.tool,"output":dict(result.output),"error":result.error}
