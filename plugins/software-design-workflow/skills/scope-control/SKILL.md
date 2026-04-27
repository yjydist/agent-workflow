---
name: scope-control
description: Use when selecting the current target, freezing scope, processing scope changes, or preventing feature creep.
---

# Scope Control

## Goal

Keep the active target small, explicit, and stable enough to plan and hand off. This skill can be used inside the main software design workflow or independently when a project is drifting.

## Current Target Checklist

- Does the target have one primary outcome?
- Can the target be implemented and validated independently?
- Are included capabilities, excluded capabilities, and deferred ideas all explicit?
- Does every included capability have acceptance criteria?
- Are expensive additions justified by the target itself?
- Are assumptions and dependencies named?

## Scope Record

Use this structure:

```markdown
## Current Target

## Included

## Explicitly Out of Scope

## Deferred

## Assumptions

## Acceptance Boundaries

## Change Control
```

## Default Trims

Cut these unless they are central to the target:

- Microservices.
- Kubernetes.
- Complex role-based access control.
- Multi-tenant administration.
- Payments.
- Real-time collaboration.
- Large-scale concurrency.
- Complex observability stacks.
- Heavy customization systems.

## Freeze Rules

- Freeze scope before writing the implementation plan.
- After freeze, do not silently add requirements.
- If a requested change affects frozen scope, mark the current plan, review, or handoff notes stale.
- Re-run the earliest impacted design step before declaring the package handoff-ready again.

## Change Triage

```markdown
## Change Request

## Affected Docs

## Scope Impact

## Decision

## V1 Must Have

## V1 Explicitly Out of Scope

## V2 Candidates

## Removed for Now

## Rationale
```
