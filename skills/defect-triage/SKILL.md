---
name: defect-triage
description: Prioritize reported manufacturing defects using deterministic severity and safety rules.
---

# Defect Triage

## Purpose
Prioritize reported manufacturing defects.

## Inputs
Defect type, severity, occurrence count, safety impact.

## Processing
Apply deterministic priority rules with safety/critical cases escalated immediately.

## Outputs
Priority and recommended containment/review action.

## Limitations
Does not diagnose root cause or authorize disposition.

## Expected Behavior
The skill validates inputs before calculation, returns structured results, and reports failures rather than fabricating values.
