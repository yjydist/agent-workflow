---
description: Process a design change request after target selection or target freeze.
argument-hint: <change request>
allowed-tools: Read, Write, Edit
---

# /sdw:change

## Purpose

Process a change request without silently breaking the current target, frozen target, plan, or handoff package.

## Accepted Inputs

- A new requirement.
- A scope change.
- A correction to prior discovery, model, design, quality, target, plan, or handoff docs.

## Procedure

1. Identify current workflow state and whether `/sdw:freeze-target` has locked scope.
2. Classify the change as clarification, scope addition, scope removal, target replacement, or post-handoff revision.
3. Update decisions and change history.
4. If the frozen target is affected, invalidate downstream plan, review, and handoff state as needed.
5. Recommend the earliest command that must be rerun.

## Output Requirements

- Change classification.
- Impacted docs and states.
- Required rerun point.
- Next command.

## Rules

- Do not write implementation code.
- Do not silently include new scope after freeze-target.
- Do not preserve `handoff-ready` if the handoff package is no longer accurate.
