# Software Design Workflow

This workflow turns vague software directions into a reviewed, scope-locked, handoff-ready design package.

## Sequence

```text
idea -> classified -> discovered -> modeled -> designed -> qualified -> scoped -> planned -> reviewed -> handoff-ready
```

## Stages

### idea

Capture the raw direction, user intent, desired outcome, constraints, and unknowns without assuming architecture.

### classified

Pick the relevant adapter set from `adapters/index.md`. At minimum, identify the software kind and user or integration surface.

### discovered

Collect users, goals, non-goals, workflows, data needs, integrations, risks, and constraints.

### modeled

Define domain concepts, relationships, lifecycle states, invariants, and vocabulary.

### designed

Describe system boundaries, components, interfaces, data responsibilities, runtime behavior, permissions, errors, and observability.

### qualified

Define quality attributes, acceptance checks, validation strategy, risks, and stop conditions.

### scoped

Select and freeze the current target. Included work, excluded work, deferred work, assumptions, and acceptance boundaries must be explicit.

### planned

Write a phased implementation plan for the frozen target. The plan should describe sequencing, dependencies, validation, allowed changes, forbidden changes, and stop conditions.

### reviewed

Check the design package for contradictions, missing decisions, stale assumptions, scope drift, and handoff blockers.

### handoff-ready

The package is ready for another implementation agent or developer to consume. `docs/handoff/agent-entry.md` is the machine-oriented entry point.

## Change Control

After scope freeze, any request that changes goals, requirements, design decisions, quality criteria, current target, plan, review status, or handoff instructions must invalidate the affected downstream sections until they are updated.
