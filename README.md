# Manufacturing Quality Agent

A framework-independent Python agent for manufacturing quality inspection, SPC screening, defect triage, process capability analysis, and traceable quality reporting.

## Architecture
`AgentCore` orchestrates tools through a dynamic `ToolRegistry`. Each tool implements the framework-neutral `ToolContract`; `PortableAdapter` exposes the same execution contract to external runtimes without importing vendor SDKs.

## Installation
Create a virtual environment and install `requirements.txt`. Copy `.env.example` to `.env` and set all runtime values explicitly; the application intentionally does not embed production configuration or credentials.

## Configuration
Required environment variables are `MQA_ENVIRONMENT`, `MQA_LOG_LEVEL`, `MQA_MAX_INPUT_RECORDS`, `MQA_MEASUREMENT_LIMIT`, and `MQA_DEFAULT_TARGET_CPK`. The current numerical tools do not require network credentials.

## Tools
- `inspect-measurements` — descriptive measurement statistics.
- `calculate-spc` — three-sigma screening limits.
- `classify-defect` — deterministic defect priority.
- `calculate-capability` — Cp/Cpk calculations.
- `generate-quality-report` — traceable report assembly.

## Skills
The skills directory documents quality inspection, SPC, defect triage, process capability, and quality reporting. Every skill declared in `agent.yaml` exists as a real file.

## Usage
```python
from core.agent_core import AgentCore
agent=AgentCore()
result=agent.execute("calculate-capability", {"measurements":[9.9,10.0,10.1,10.0],"lower_spec":9.5,"upper_spec":10.5})
print(result)
```

## Testing
Run `pytest -q` and `python verification/readiness_audit.py`. The tests cover tools, contracts, registry, adapters, security, documentation, and OpenGAP manifest structure.

## Portability
The core layer is framework-independent. Adapter contracts can be integrated with OpenAI SDK, CrewAI, Claude Code, or Lyzr runtimes, but this repository only claims the tested neutral adapter layer, not vendor-specific end-to-end execution.

## Limitations
The implementation does not access live plant systems, perform computer vision, diagnose physical root causes, authorize product release, or certify regulatory compliance. SPC and capability calculations must be interpreted using the site's approved methods, sampling plans, measurement-system controls, and engineering specifications.
