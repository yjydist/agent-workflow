# Software design review checklist

Use this checklist during `/sdw:review` and before `/sdw:handoff`.

## Consistency

- Project vision, scope, current target, and requirements describe the same product boundary.
- Analysis docs do not contradict design docs.
- Quality requirements are testable and linked to current target risks.
- Deferred work is listed outside the frozen current target.

## Completeness

- Required long-lived docs exist under `docs/project`, `docs/analysis`, `docs/design`, and `docs/quality`.
- Required current-target docs exist under `docs/releases/current-target` or the concrete target directory.
- Required handoff docs exist under `docs/handoff`.
- `docs/handoff/agent-entry.md` includes required reading order, non-overridable decisions, and allowed next actions.

## Safety

- No implementation code is started by the design workflow itself.
- Agent instructions do not grant unrestricted shell access.
- Security, privacy, data retention, and operational failure modes are explicit where relevant.
