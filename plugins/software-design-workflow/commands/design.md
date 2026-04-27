---
description: Design the system shape, interfaces, data, security, and operational behavior.
argument-hint: [design focus or constraints]
allowed-tools: Read, Write, Edit
---

# /sdw:design

## Purpose

Produce the system design package for the modeled target, including boundaries, interfaces, data, security, and operations.

## Accepted Inputs

- Domain model notes.
- Architecture constraints.
- Interface, data, security, deployment, or integration requirements.

## Procedure

1. Read the current model and discovery context.
2. Define system boundaries, components, contracts, data responsibilities, errors, permissions, and operational concerns.
3. Record tradeoffs and decisions.
4. Keep design technology-aware when useful, but not implementation-bound unless required.
5. Update workflow state to `designed` when the package is coherent enough for quality checks.

## Output Requirements

- Design summary.
- Key decisions and tradeoffs.
- Open design risks.
- Next command: `/sdw:quality`.

## Rules

- Do not write implementation code.
- Do not expand scope beyond discovery without recording a change.
- Do not hide unresolved design conflicts.
