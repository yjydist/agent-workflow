# Workflow Redesign Examples

These examples demonstrate the redesigned software-design-workflow model. Each example starts from a vague idea, captures a multi-dimensional classification, keeps long-lived docs outside the target slice, stores target-specific docs under `docs/releases/<target-id>/`, and provides a handoff entry file for downstream implementation work.

## Example directories

- `ai-agent-research-assistant/`: Shows an AI agent workflow example that turns a research assistant idea into a bounded target with agent-specific design and handoff materials.
- `library-sdk-feature-flags/`: Shows a library or SDK workflow example focused on public API design, compatibility expectations, and a narrow SDK target.
- `cli-repo-cleanup/`: Shows a CLI workflow example focused on local repository scanning, safety constraints, and a read-only planning target.

## Shared elements in every example

Each example includes:

- a vague idea input that represents the starting point
- a multi-dimensional classification section
- long-lived docs described as stable documentation for the project
- target docs under `docs/releases/<target-id>/`
- a handoff entry file at `docs/handoff/agent-entry.md`
