---
description: Set or revise the current target scope for the design package.
argument-hint: <target description>
allowed-tools: Read, Write, Edit
---

# /sdw:target

## Purpose

Set or revise the current target, meaning the explicit scope slice that planning and handoff will describe.

## Accepted Inputs

- A desired target scope.
- A release slice.
- A narrowed or expanded scope request.
- Notes about what should be included, excluded, or deferred.

## Procedure

1. Read qualified design context and existing target notes.
2. Confirm whether the target is still unfrozen. If the target has already been frozen and the requested update would change scope, stop and direct the user to `/sdw:change` instead of revising it here.
3. Define or refine the current target with included scope, excluded scope, deferred ideas, assumptions, and acceptance boundaries.
4. Check that the current target is coherent with discovery, model, design, and quality docs.
5. Record any required tradeoffs or changes.
6. Keep state at `qualified` until `/sdw:freeze-target` locks the scope.

## Output Requirements

- Current target.
- In scope, out of scope, and deferred items.
- Target risks or conflicts.
- Next command: `/sdw:freeze-target`.

## Rules

- The current target is not frozen until `/sdw:freeze-target` runs.
- Once a target has been frozen, any scope-impacting revision must go through `/sdw:change`, not `/sdw:target`.
- Do not write implementation code.
- Do not use target selection to bypass unresolved blockers.
