from core.agent_core import AgentCore

def test_spc_flags_outlier():
    r=AgentCore().execute("calculate-spc",{"measurements":[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,40]})
    assert r.ok and r.output["out_of_control_count"]==1

def test_defect_triage_safety_is_immediate():
    r=AgentCore().execute("classify-defect",{"defect_type":"fracture","severity":"major","occurrences":1,"safety_impact":True})
    assert r.ok and r.output["priority"]=="immediate"

def test_capability_values_exist():
    r=AgentCore().execute("calculate-capability",{"measurements":[9.8,10.0,10.2,10.0],"lower_spec":9.0,"upper_spec":11.0})
    assert r.ok and r.output["cp"]>0 and r.output["cpk"]>0

def test_report_preserves_findings():
    r=AgentCore().execute("generate-quality-report",{"title":"Shift A","findings":["Dimension stable"]})
    assert r.ok and r.output["findings"]==["Dimension stable"]
