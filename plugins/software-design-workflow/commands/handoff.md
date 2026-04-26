---
description: Validate handoff readiness and prepare the agent entry point.
argument-hint: [handoff notes]
allowed-tools: Read, Write, Edit
---

# /sdw:handoff

## Purpose

Validate handoff readiness and prepare the machine-readable entry point for a future implementation agent.

## Accepted Inputs

- Handoff notes.
- Confirmation that review blockers are resolved.
- Constraints for the future receiving agent.

## Procedure

1. Read the reviewed design package and plan.
2. Verify there are no blocking open questions, unresolved review blockers, or scope-lock conflicts.
3. Create or update `docs/handoff/agent-entry.md` as the machine entry point.
4. Ensure `docs/README.md` is a human navigation file only and points humans to the relevant docs.
5. Update workflow state to `handoff-ready` when all gates pass.

## Output Requirements

- Handoff readiness result.
- `docs/handoff/agent-entry.md` status.
- Remaining concerns, if any.
- Terminal state: `handoff-ready`.

## Rules

- Do not write implementation code.
- Do not mark `handoff-ready` if blockers remain.
- The workflow ends at handoff, not coding.
