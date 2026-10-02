---
name: statistical-process-control
description: Evaluate manufacturing measurements using three-sigma statistical process control screening.
---

# Statistical Process Control

## Purpose
Evaluate individual measurements against three-sigma limits.

## Inputs
At least two numeric observations.

## Processing
Calculate process mean and population sigma, then flag observations outside mean ± 3 sigma.

## Outputs
Control limits and flagged observations.

## Limitations
This is a screening calculation, not a replacement for a validated plant SPC plan.

## Expected Behavior
The skill validates inputs before calculation, returns structured results, and reports failures rather than fabricating values.
