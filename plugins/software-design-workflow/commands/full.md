---
description: Run the complete software design workflow from intake through handoff-ready.
argument-hint: <project idea or design brief>
allowed-tools: Read, Write, Edit
---

# /sdw:full

## Purpose

Run the full software design workflow without skipping gates. This command may orchestrate the same work as `/sdw:start`, `/sdw:classify`, `/sdw:discover`, `/sdw:model`, `/sdw:design`, `/sdw:quality`, `/sdw:target`, `/sdw:freeze-target`, `/sdw:plan`, `/sdw:review`, and `/sdw:handoff`, but it must stop whenever user input or a blocking decision is required.

## Accepted Inputs

- A project idea.
- A design brief.
- Existing notes that describe goals, users, constraints, or desired outcomes.

## Procedure

1. Initialize or locate the design package under `docs/`.
2. Move through the canonical sequence: `intake -> classified -> discovered -> modeled -> designed -> qualified -> planned -> reviewed -> handoff-ready`.
3. Establish the current target before planning.
4. Run `/sdw:freeze-target` semantics before producing a plan.
5. Stop before implementation. The terminal state is `handoff-ready`, not coding.
6. Ensure `docs/handoff/agent-entry.md` exists as the machine entry point and `docs/README.md` remains a human navigation file only.

## Output Requirements

- Current state.
- Current target.
- Files created or updated.
- Blocking questions, if any.
- Next command, if not yet `handoff-ready`.

## Rules

- Do not write implementation code.
- Do not skip review or handoff validation.
- Do not claim `handoff-ready` while open blockers remain.
