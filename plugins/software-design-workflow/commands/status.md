---
description: Report current software design workflow state and next action.
argument-hint: [status focus]
allowed-tools: Read
---

# /sdw:status

## Purpose

Report the current software design workflow state, current target, freeze-target status, blockers, and next action.

## Accepted Inputs

- A request for workflow status.
- A focus area such as blockers, target, handoff, or next command.

## Procedure

1. Read available workflow docs and state indicators.
2. Report the highest justified state in the sequence: `intake -> classified -> discovered -> modeled -> designed -> qualified -> planned -> reviewed -> handoff-ready`.
3. Report current target and whether `/sdw:freeze-target` has locked it.
4. Identify blockers, stale docs, and the next command.
5. Do not modify files unless the user explicitly asks for a status repair in a separate command.

## Output Requirements

- Current state.
- Current target.
- Freeze-target status.
- Blockers.
- Next command.

## Rules

- Do not write implementation code.
- Do not overstate state if evidence is missing.
- Do not treat `docs/README.md` as the machine entry point; use `docs/handoff/agent-entry.md` for handoff.
