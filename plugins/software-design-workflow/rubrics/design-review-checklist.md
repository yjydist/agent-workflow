# Design Review Checklist

Use this checklist before declaring a package handoff-ready.

## Scope

- Current target is explicit and frozen.
- Included, excluded, and deferred work are clear.
- Requirements map to acceptance checks.
- The plan does not include out-of-scope work.

## Design

- Adapter classification matches architecture decisions.
- Interfaces, state, and data ownership use consistent vocabulary.
- Error handling, permissions, and operational behavior are addressed.
- Risks have mitigations, validation, or stop conditions.

## Handoff

- `docs/handoff/agent-entry.md` exists when durable docs are used.
- Required reading order is clear.
- Allowed next actions and stop conditions are explicit.
- No blocking open question remains hidden.
