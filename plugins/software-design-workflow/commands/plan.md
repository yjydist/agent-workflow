---
description: Create a delivery-neutral implementation plan from the frozen target.
argument-hint: [planning constraints]
allowed-tools: Read, Write, Edit
---

# /sdw:plan

## Purpose

Create a delivery-neutral implementation plan from the frozen target, without starting implementation.

## Accepted Inputs

- Frozen target notes.
- Sequencing constraints.
- Team, repository, testing, or delivery constraints.

## Procedure

1. Read the frozen target and design package.
2. Build a phased plan with goals, dependencies, allowed change areas, validation methods, and stop conditions.
3. Preserve scope lock from `/sdw:freeze-target`.
4. Update workflow state to `planned` when the plan is complete.
5. Prepare for `/sdw:review`.

## Output Requirements

- Plan summary.
- Phase list and validation approach.
- Risks or blockers.
- Next command: `/sdw:review`.

## Rules

- Do not write implementation code.
- Do not plan work outside the frozen target.
- Do not mark handoff-ready from this command.
