from core.agent_core import AgentCore

def test_rejects_missing_measurements():
    r=AgentCore().execute("inspect-measurements",{})
    assert not r.ok and "validation_error" in r.error

def test_rejects_wrong_types():
    r=AgentCore().execute("inspect-measurements",{"measurements":[1,"2"]})
    assert not r.ok

def test_rejects_nonfinite():
    r=AgentCore().execute("inspect-measurements",{"measurements":[1,float("inf")]})
    assert not r.ok

def test_rejects_invalid_spec_limits():
    r=AgentCore().execute("calculate-capability",{"measurements":[1,2],"lower_spec":3,"upper_spec":2})
    assert not r.ok
