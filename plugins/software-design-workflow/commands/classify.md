---
description: Classify the software design using adapter-first project dimensions.
argument-hint: [project idea or existing notes]
allowed-tools: Read, Write, Edit
---

# /sdw:classify

## Purpose

Classify the software design by selecting adapters that describe what must be designed before deeper discovery. Classification is adapter-first, not a single project type or one fixed design track.

## Accepted Inputs

- Existing intake notes.
- A project idea with suspected kind, surface, runtime, domain, or concern adapters.
- User answers about users, platforms, integration surfaces, operating constraints, data, safety, or delivery context.

## Procedure

1. Read current intake context from `docs/` when available.
2. Select the required adapter set across these dimensions:
   - Kind adapters: primary software shape, such as application, service, library, automation, data workflow, or AI-enabled system.
   - Surface adapters: user or integration surfaces, such as CLI, API, SDK, web UI, desktop UI, mobile UI, file interface, event interface, or agent tool interface.
   - Runtime adapters: execution and deployment environments, such as local process, server, browser, mobile device, desktop app, scheduled job, serverless function, container, or managed platform.
   - Domain adapters: business or product domain concepts that drive vocabulary, invariants, workflows, and data rules.
   - Concern adapters: cross-cutting design needs, such as security, privacy, reliability, observability, accessibility, compliance, performance, migration, evaluation, or operability.
3. Record confidence, uncertainties, and missing evidence for each selected adapter.
4. Add optional legacy compatibility labels only when useful for migration, marketplace search, or backward-compatible reporting. Do not let legacy labels replace adapter selection.
5. Update workflow state to `classified` only when the required adapter dimensions are sufficiently covered for discovery.
6. Prepare adapter-specific discovery questions for `/sdw:discover`.

## Output Requirements

- Selected kind adapters with confidence.
- Selected surface adapters with confidence.
- Selected runtime adapters with confidence.
- Selected domain adapters with confidence.
- Selected concern adapters with confidence.
- Optional legacy compatibility labels, if any, with rationale.
- Implications, risks, ambiguities, and next discovery questions.
- Next command: `/sdw:discover`.

## Rules

- Do not collapse classification into one canonical project type.
- Do not assume every project is a web app, backend API, AI system, or single runtime.
- Do not write implementation code.
- If any required adapter dimension is blocked, ask targeted questions instead of advancing state.
