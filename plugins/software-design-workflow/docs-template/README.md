# Software design docs template

This directory is a human navigation map for generated project design docs. It is not the machine-oriented execution contract.

## Directory model

- `project/`: long-lived project intent, boundaries, context, and shared language.
- `analysis/`: discovery outputs that explain the problem space, domain, workflows, states, and information model.
- `design/`: solution decisions for architecture, components, interfaces, data, UX, and runtime.
- `quality/`: quality attributes, validation, security, privacy, observability, and operability expectations.
- `releases/`: target-scoped docs for the active delivery target and future targets.
- `handoff/`: agent and human handoff entry points for continuing the work safely.

## Where humans should start

1. Read `project/vision.md`, `project/scope.md`, and `project/project-context.md` for durable intent, boundaries, and project context.
2. Read the active target docs under `releases/current-target/` or the concrete target directory that replaced it.
3. Use `analysis/` and `design/` when a decision needs context.
4. Use `quality/` before approving implementation or release readiness.

## Where agents should start

Agents should start at `docs/handoff/agent-entry.md` after this template is copied into a project docs directory. That file defines required reading order, non-overridable decisions, and allowed next actions.

## Active target docs

The template uses `releases/current-target/` as a placeholder. For real work, replace `current-target` with a concrete target id such as `v1`, `mvp`, `release-2026-04`, or `milestone-1`.
