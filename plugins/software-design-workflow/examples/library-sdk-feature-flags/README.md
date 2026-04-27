# Example: Feature Flag SDK

This lightweight example shows a reusable library or SDK workflow with public API and compatibility concerns.

## Vague idea input

> I want a tiny SDK that lets services evaluate feature flags from a local JSON file before we add a hosted service.

## Classification

- Kind: `library-sdk`
- Surface: `library-api`, `file-format`
- Runtime: `server`, `local-machine`
- Domain: `developer-tools`
- Concerns: `compatibility`, `performance`, `observability`

## Long-lived docs

Stable docs live under `docs/project/`, `docs/analysis/`, `docs/design/`, and `docs/quality/`. They define SDK consumers, public API shape, flag evaluation rules, config format, versioning policy, error behavior, and compatibility promises.

## Current target docs

The current target is stored under:

```text
docs/releases/target-2026-04-sdk-core/
```

This target covers a synchronous evaluator, local JSON provider, typed result object, and compatibility tests.

## Handoff entry point

The execution-layer agent starts from:

```text
docs/handoff/agent-entry.md
```

The handoff emphasizes public API stability and avoids hosted-service scope.
