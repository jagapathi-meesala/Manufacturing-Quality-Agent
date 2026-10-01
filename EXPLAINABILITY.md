# Explainability

## Inputs and Data Sources
The agent accepts structured inputs supplied directly to its tools, including manufacturing measurements, specification limits, and defect observations. Data sources are external to the core agent; the implementation only uses data explicitly provided in the request and does not silently fetch production records.

### Input Requirements
Measurement tools require finite numeric values, while defect triage requires a defect type, severity, occurrence count, and safety-impact flag. Capability analysis additionally requires ordered lower and upper specification limits, and reporting requires a title and supplied findings.

### Failure Handling
Invalid types, missing required fields, non-finite values, invalid limits, and unsafe request shapes are rejected with structured validation errors. The agent does not substitute defaults for missing production data because doing so would weaken traceability.

## Decision and Reasoning
The decision process is rule-based for numerical tools: the inspection tool calculates descriptive statistics, SPC uses mean ± three population standard deviations as a screening rule, and capability analysis uses Cp and Cpk formulas from the supplied limits. Defect triage escalates safety-impacting or critical defects immediately and otherwise uses severity and recurrence rules to assign a priority.

### Rules Applied
For capability, Cp = (USL - LSL) / (6σ), Cpu = (USL - mean) / (3σ), Cpl = (mean - LSL) / (3σ), and Cpk = min(Cpu, Cpl). For SPC screening, observations outside mean ± 3σ are flagged, while reporting preserves supplied findings without inventing causes or measurements.

### Expected Outputs
Every tool returns a structured result containing success state, tool name, output data, and an error field when execution fails. Numerical outputs retain the inputs and method context needed for a reviewer to understand what was calculated.

### Worked Example
Given measurements and specification limits, the capability tool computes mean, sigma, Cp, Cpu, Cpl, and Cpk from those supplied values. Given a defect marked safety-impacting, the triage tool returns immediate priority and recommends containment plus human review.

## Limits and Constraints
The agent's calculations are analytical aids and do not by themselves establish product conformity, process validation, regulatory compliance, or release authorization. SPC screening uses a simple individual-observation three-sigma rule and may not match a plant's approved subgrouped control-chart methodology.

### Constraints
The agent does not infer root causes, does not access hidden production systems, and does not replace qualified engineering judgment. Capability metrics can be misleading when sampling assumptions, distributional behavior, measurement-system error, or specification context are inappropriate.
