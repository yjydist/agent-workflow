# Example: CLI Repo Cleanup Tool

This lightweight example shows a tooling workflow with a local command surface and a narrow current target.

## Vague idea input

> I want a small CLI that finds stale generated files and safe cleanup candidates in a repository.

## Classification

- Kind: `tooling`
- Surface: `cli`
- Runtime: `local-machine`
- Domain: `developer-tools`
- Concerns: `security-privacy`, `observability`, `compatibility`

## Long-lived docs

Stable docs live under `docs/project/`, `docs/analysis/`, `docs/design/`, and `docs/quality/`. They define repository safety rules, command UX, filesystem boundaries, dry-run behavior, logs, and compatibility expectations.

## Current target docs

The current target is stored under:

```text
docs/releases/target-2026-04-local-cli/
```

This target covers `repo-clean scan` and `repo-clean plan` with no destructive delete command.

## Handoff entry point

The execution-layer agent starts from:

```text
docs/handoff/agent-entry.md
```

The handoff keeps implementation bounded to read-only scanning and plan output.
