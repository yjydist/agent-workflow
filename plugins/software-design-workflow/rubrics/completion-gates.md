# Software design workflow completion gates

Use these gates to decide whether a design package can move to the next canonical stage.

## Stage gates

- `intake`: A project idea exists and the docs package has been initialized.
- `classified`: Project kind, surfaces, runtime, concerns, and domain adapters have been selected or intentionally deferred.
- `discovered`: Users, goals, constraints, risks, assumptions, and open questions are captured.
- `modeled`: Domain concepts, workflows, states, information model, and shared vocabulary are coherent.
- `designed`: Architecture, components, interfaces, data, UX, and runtime decisions are documented.
- `qualified`: Quality attributes, security, privacy, operability, validation, and acceptance criteria are explicit.
- `planned`: The current target has implementation phases, task breakdown, risks, and validation steps.
- `reviewed`: Cross-doc review notes are resolved or marked as accepted non-blockers.
- `handoff-ready`: `docs/handoff/agent-entry.md` is current and gives the next agent a safe required reading order.

## Handoff gate

The package is handoff-ready only when no blocking open question remains for the current target, non-overridable decisions are listed, and allowed next actions are clear.
