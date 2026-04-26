# Example: AI Agent Research Assistant

This lightweight example shows how a vague idea becomes a handoff-ready design package without asking the design workflow to write implementation code.

## Vague idea input

> I want an agent that can help me research technical topics, keep notes, and prepare a short brief with sources.

## Classification

- Kind: `agent-system`
- Surfaces: `agent-tools`, `file-format`
- Runtimes: `local-machine`, optional `cloud-platform`
- Domain: `knowledge-management`
- Concerns: `ai-safety`, `observability`, `security-privacy`

## Long-lived docs

The project keeps stable docs under `docs/project/`, `docs/analysis/`, `docs/design/`, and `docs/quality/`. These describe the product intent, agent boundaries, tool contracts, memory model, source handling, safety rules, and validation strategy across targets.

## Current target docs

The active scope slice is stored under:

```text
docs/releases/target-2026-04-research-mvp/
```

This target covers one local research loop: accept a topic, search approved sources through tools, summarize notes, cite sources, and write a brief.

## Handoff entry point

A future implementation agent starts from:

```text
docs/handoff/agent-entry.md
```

That file points to the current target docs, stop conditions, validation commands, and execution-layer handoff notes.
