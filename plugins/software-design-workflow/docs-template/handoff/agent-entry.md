# Agent entry

## Current target

- Target id: TODO
- Target docs path template: `docs/releases/<target-id>/`
- Resolved target docs path: `docs/releases/TODO/`
- Current workflow state: TODO

## Handoff consumer

| Consumer type | Purpose | Expected output |
| --- | --- | --- |
| Human reviewer | TODO | TODO |
| Planning agent | TODO | TODO |
| Implementation agent | TODO | TODO |
| QA or validation agent | TODO | TODO |

## Required Reading Order

1. `docs/project/vision.md`
2. `docs/project/scope.md`
3. `docs/project/project-context.md`
4. `<resolved-target-docs-path>/scope-baseline.md`
5. `<resolved-target-docs-path>/requirements.md`
6. `<resolved-target-docs-path>/risks.md`
7. `<resolved-target-docs-path>/review-notes.md`
8. Relevant `docs/analysis/`, `docs/design/`, and `docs/quality/` files for the assigned task.

## Long-lived docs vs target docs

| Doc class | Location | Change policy |
| --- | --- | --- |
| Long-lived project docs | `docs/project/`, `docs/analysis/`, `docs/design/`, `docs/quality/` | Update only when durable project understanding or decisions change. |
| Target docs | `<resolved-target-docs-path>/` | Update when target scope, plan, risks, questions, or review status changes. |
| Handoff docs | `docs/handoff/` | Update before transferring work to another human or agent. |

## Non-overridable decisions

- TODO: Decision that downstream consumers must not change without explicit scope or design review.

## Open questions and blockers

| ID | Question or blocker | Source doc | Owner | Required before |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |

## Allowed next actions by consumer type

| Consumer type | Allowed next actions | Not allowed |
| --- | --- | --- |
| Human reviewer | TODO: Review docs, answer questions, approve or request changes. | TODO |
| Planning agent | TODO: Refine plans and tasks within approved scope. | TODO |
| Implementation agent | TODO: Implement only tasks already approved for the current target. | TODO |
| QA or validation agent | TODO: Run checks, document evidence, report gaps. | TODO |

## Handoff notes

- TODO: Current context, cautions, and next recommended action.
