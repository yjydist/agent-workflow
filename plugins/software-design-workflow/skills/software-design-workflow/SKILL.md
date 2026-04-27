---
name: software-design-workflow
description: Use when turning a vague software idea into a scoped design package with requirements, architecture, quality checks, implementation plan, and handoff notes.
---

# Software Design Workflow

This is the primary Codex skill for the plugin. Use it to guide software work from ambiguous idea to handoff-ready design package. It is not a coding skill. It prepares the materials that an implementation agent or developer can execute.

## Operating Rules

- Start by understanding the user's goal, audience, constraints, and success criteria.
- Keep the first target small enough to implement and validate independently.
- Do not write application code as part of this workflow unless the user explicitly leaves design mode and asks for implementation.
- Treat handoff as a reviewable package, not as implicit permission to start coding.
- Prefer existing project conventions over new process artifacts.

## Workflow

1. Capture the raw idea in the user's words.
2. Classify the software with adapters:
   - Kind: `application`, `service`, `library-sdk`, `tooling`, `knowledge-system`, `agent-system`, `platform-infra`, `data-ml-system`, `language-compiler`, `embedded-system`, or `interactive-media`.
   - Surface: `web-ui`, `desktop-ui`, `mobile-ui`, `cli`, `tui`, `http-api`, `library-api`, `agent-tools`, `file-format`, `event-stream`, `ipc`, or `background-jobs`.
   - Runtime: `browser`, `server`, `local-machine`, `mobile-device`, `embedded-device`, `cloud-platform`, `offline-first`, or `edge-runtime`.
   - Concern: `security-privacy`, `offline-sync`, `observability`, `compatibility`, `performance`, or `ai-safety`.
3. Discover users, goals, non-goals, workflows, data, integrations, risks, and constraints.
4. Model the domain vocabulary, entities, state changes, invariants, and edge cases.
5. Design boundaries, components, interfaces, data ownership, runtime behavior, errors, permissions, and observability.
6. Define quality attributes, acceptance checks, validation strategy, and risks.
7. Select the current target and freeze it before planning.
8. Write a phased implementation plan for the frozen target.
9. Review the package for contradictions, missing decisions, scope drift, stale assumptions, and handoff blockers.

## Output Shape

Use the repository docs template when a durable package is useful:

```text
docs/project/
docs/analysis/
docs/design/
docs/quality/
docs/releases/current-target/
docs/handoff/
```

For lighter work, produce the same sections inline:

```md
## Goal
## Classification
## Users and Workflows
## Domain Model
## Design
## Quality and Validation
## Current Target
## Implementation Plan
## Handoff Notes
```

## Quality Bar

- Requirements are testable.
- Non-goals are explicit.
- Interfaces and state transitions are named.
- Risks have concrete mitigations or stop conditions.
- The current target has clear included, excluded, and deferred work.
- The implementation plan can be followed without inventing missing scope.
