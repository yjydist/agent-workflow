# Software Design Docs Template

This compact template stores the minimum durable docs needed to hand software design work to an implementation agent or developer.

## Directory Model

- `project/`: durable intent, boundaries, and project context.
- `analysis/`: classification, workflows, and domain model.
- `design/`: architecture, interfaces, and data ownership.
- `quality/`: quality attributes and validation strategy.
- `releases/current-target/`: frozen target scope, requirements, plan, risks, review notes, and change log.
- `handoff/`: execution entry point and brief.

## Start Points

Humans should start at `project/vision.md` and `releases/current-target/scope-baseline.md`.

Implementation agents should start at `handoff/agent-entry.md`, then follow the required reading order listed there.
