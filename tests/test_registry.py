import pytest
from adapters.registry import ToolRegistry
from tools import InspectMeasurementsTool

def test_registry_register_and_discover():
    reg=ToolRegistry(); reg.register(InspectMeasurementsTool())
    assert reg.discover()==["inspect-measurements"]

def test_registry_rejects_duplicate():
    reg=ToolRegistry(); reg.register(InspectMeasurementsTool())
    with pytest.raises(ValueError): reg.register(InspectMeasurementsTool())
