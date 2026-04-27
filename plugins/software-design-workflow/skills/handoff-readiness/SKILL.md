---
name: handoff-readiness
description: Use when reviewing whether a design package is ready for another implementation agent or developer to execute safely.
---

# Handoff Readiness

Use this skill near the end of design work, before implementation starts. The goal is to find missing decisions, stale assumptions, and scope leaks while changes are still cheap.

## Required Inputs

- Project goal and non-goals.
- Classification or adapter set.
- Current target and scope freeze status.
- Requirements and acceptance criteria.
- Architecture, interface, data, and runtime notes.
- Quality and validation strategy.
- Implementation plan.
- Known risks and open questions.

## Review Checklist

### Scope

- The current target is frozen or explicitly ready to freeze.
- Included, excluded, and deferred work are clear.
- The implementation plan does not include out-of-scope features.
- Open questions do not block the next implementation step.

### Consistency

- Requirements match the design.
- Interfaces match the implementation plan.
- Data and state models use the same vocabulary throughout.
- Quality checks map to acceptance criteria.
- Risks are reflected in the plan or stop conditions.

### Executability

- A new agent can identify where to start.
- The plan is sequenced by dependency.
- Each phase has a validation command, manual check, or review gate.
- Allowed and forbidden changes are explicit.
- Handoff notes say when to stop and ask for clarification.

## Output

Return one of these statuses:

- `ready`: Implementation can start from the handoff notes.
- `ready-with-risks`: Implementation can start, but named risks need active monitoring.
- `blocked`: Missing or contradictory design decisions must be resolved first.

Use this report shape:

```markdown
## Handoff Status

## Blocking Issues

## Risks to Monitor

## Required Reading Order

## Allowed Next Actions

## Stop Conditions
```
