from adapters.portable_adapter import PortableAdapter
from core.agent_core import AgentCore

def test_portable_adapter_translates_result():
    out=PortableAdapter(AgentCore()).invoke("inspect-measurements",{"measurements":[2,4]})
    assert out["ok"] is True and out["tool"]=="inspect-measurements"
