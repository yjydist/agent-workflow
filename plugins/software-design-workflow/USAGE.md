# Usage Guide

This guide explains how to use the `software-design-workflow` Codex plugin.

## Use the Skills

Start with `software-design-workflow` when the user has a vague idea, an incomplete product direction, or a design package that needs structure.

Use `scope-control` when the next decision is about what belongs in the current target, what is out of scope, or whether a change invalidates a frozen plan.

Use `handoff-readiness` before implementation starts, especially when another agent or developer will consume the design package.

## Standard Flow

```text
idea
classified
discovered
modeled
designed
qualified
scoped
planned
reviewed
handoff-ready
```

The flow is intentionally skill-driven. There is no command namespace and no compatibility command layer.

## Durable Docs

When the output should live in the target project, initialize the docs template:

```bash
plugins/software-design-workflow/scripts/install-to-project.sh /path/to/project
```

Then fill the generated docs under:

```text
docs/project/
docs/analysis/
docs/design/
docs/quality/
docs/releases/current-target/
docs/handoff/
```

The machine-oriented entry point is:

```text
docs/handoff/agent-entry.md
```

## Safety Rules

- Do not treat handoff as permission to start implementation.
- Freeze the current target before writing a detailed implementation plan.
- Route scope-changing requests through change control.
- Mark stale plans or handoff notes when a frozen target changes.
- Stop and ask for clarification when required decisions are missing.
