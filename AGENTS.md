# Framework-Agnostic Agent Instructions

The core entry point is `core.agent_core.AgentCore`. Tools implement `contracts.tool_contract.ToolContract` and are discovered through `adapters.registry.ToolRegistry`.

Framework adapters must translate external framework calls into the same `AgentCore.execute(tool_name, inputs)` contract. No vendor SDK is required by the core implementation.
