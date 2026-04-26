---
description: Freeze the current target as the scope lock for planning and handoff.
argument-hint: [freeze notes]
allowed-tools: Read, Write, Edit
---

# /sdw:freeze-target

## Purpose

Freeze the current target as the scope lock for planning, review, and handoff.

## Accepted Inputs

- Confirmation that the current target is correct.
- Freeze notes.
- Explicit adjustments to include, exclude, or defer before locking.

## Procedure

1. Read the current target and all known blockers.
2. Confirm included, excluded, and deferred scope.
3. Resolve or explicitly defer non-blocking open questions.
4. Record the frozen target and scope-lock decision.
5. Keep workflow state ready for `/sdw:plan`; the canonical state advances to `planned` only after planning is complete.

## Output Requirements

- Frozen target summary.
- Scope-lock decision.
- Remaining non-blocking questions.
- Next command: `/sdw:plan`.

## Rules

- Do not freeze an undefined current target.
- Do not write implementation code.
- After freeze-target, changes must go through `/sdw:change`.
