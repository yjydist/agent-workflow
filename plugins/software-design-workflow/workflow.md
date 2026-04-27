# Software Design Workflow

`software-design-workflow` is a Claude Code plugin for turning vague software directions into a reviewed, scope-locked, handoff-ready design package. It does not implement the product. It prepares the design artifacts that a future implementation agent can consume safely.

## Command family

Commands use the `/sdw:*` namespace:

```text
/sdw:full
/sdw:start
/sdw:classify
/sdw:discover
/sdw:model
/sdw:design
/sdw:quality
/sdw:target
/sdw:freeze-target
/sdw:plan
/sdw:review
/sdw:handoff
/sdw:change
/sdw:status
```

## Canonical sequence

```text
intake
  -> classified
  -> discovered
  -> modeled
  -> designed
  -> qualified
  -> planned
  -> reviewed
  -> handoff-ready
```

`/sdw:target` and `/sdw:freeze-target` are scope-locking operations around the canonical sequence. They happen after the design is qualified and before planning. They do not add separate canonical state names.

## Scope-locking concepts

### Current target

The current target is the explicit scope slice that planning and handoff will describe. It records:

- Included capabilities.
- Excluded capabilities.
- Deferred ideas.
- Assumptions.
- Acceptance boundaries.

The current target can be revised with `/sdw:target` before it is frozen. It must stay consistent with discovery, model, design, and quality docs.

### freeze-target

`/sdw:freeze-target` locks the current target for planning, review, and handoff. After freeze-target, new scope cannot be silently added. Any change that affects the frozen target must go through `/sdw:change`, and downstream plan, review, or handoff artifacts may need to be invalidated and regenerated.

## Stage details

### 1. intake

The project idea has been captured without assuming architecture or implementation. The goal is to preserve raw direction and prepare classification.

Typical command: `/sdw:start`.

### 2. classified

The adapter set, user group, and broad design track are known well enough to guide discovery. Classification should select at least one kind adapter and then add surface, runtime, domain, and concern adapters as needed.

Typical command: `/sdw:classify`.

Recommended classification shape:

```text
kind: application | service | library-sdk | tooling | knowledge-system | agent-system | platform-infra | data-ml-system | language-compiler | embedded-system | interactive-media
surfaces: web-ui | desktop-ui | mobile-ui | cli | tui | http-api | library-api | agent-tools | file-format | event-stream | ipc | background-jobs
runtimes: browser | server | local-machine | mobile-device | embedded-device | cloud-platform | offline-first | edge-runtime
domains: knowledge-management | education-learning | developer-tools
concerns: security-privacy | offline-sync | observability | compatibility | performance | ai-safety
```

Legacy project types are compatibility labels only. Map common labels as follows:

- `backend-api` -> `service + http-api + server`.
- `frontend-spa` -> `application + web-ui + browser`.
- `cli-tool` -> `tooling + cli + local-machine`.
- `ai-agent` -> `agent-system + agent-tools + ai-safety`.

### 3. discovered

The workflow has collected goals, users, scenarios, constraints, non-goals, data needs, integrations, and important risks.

Typical command: `/sdw:discover`.

### 4. modeled

Domain concepts, relationships, lifecycle states, invariants, and vocabulary are explicit enough to support system design.

Typical command: `/sdw:model`.

### 5. designed

System boundaries, components, interfaces, data responsibilities, security, error handling, and operational behavior are described.

Typical command: `/sdw:design`.

### 6. qualified

Quality attributes, acceptance criteria, risk checks, and validation approach are defined enough to judge whether the design is acceptable.

Typical command: `/sdw:quality`.

Before planning, choose and lock scope:

```text
/sdw:target
/sdw:freeze-target
```

### 7. planned

A phased, delivery-neutral plan exists for the frozen target. The plan describes sequencing, dependencies, validation, stop conditions, and areas future implementation may change. It does not start implementation.

Typical command: `/sdw:plan`.

### 8. reviewed

The design package and plan have been checked for consistency, missing decisions, overreach, stale assumptions, and handoff blockers.

Typical command: `/sdw:review`.

### 9. handoff-ready

The package is ready to hand off to a future implementation agent. `docs/handoff/agent-entry.md` is the machine entry point. `docs/README.md` is a human navigation file only.

Typical command: `/sdw:handoff`.

## Handoff rule

The workflow ends at handoff-ready. It must not write implementation code, start coding phases, or treat handoff as implicit permission to implement. A future implementation agent should start from `docs/handoff/agent-entry.md` and obey the frozen target and plan.

## Change control

Use `/sdw:change` for any request that changes goals, scope, domain model, design decisions, quality criteria, current target, frozen target, plan, review outcome, or handoff instructions. If the change affects frozen scope, rerun the earliest impacted command and do not preserve `handoff-ready` unless the handoff package remains accurate.
