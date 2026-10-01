from core.agent_core import AgentCore

def test_agent_discovers_all_tools():
    assert AgentCore().tools()==["calculate-capability","calculate-spc","classify-defect","generate-quality-report","inspect-measurements"]

def test_agent_executes_valid_tool():
    r=AgentCore().execute("inspect-measurements",{"measurements":[1,2,3]})
    assert r.ok and r.output["mean"]==2.0

def test_unknown_tool_is_structured_error():
    r=AgentCore().execute("missing-tool",{})
    assert not r.ok and "tool_not_found" in r.error
