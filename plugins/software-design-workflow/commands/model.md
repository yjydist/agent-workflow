---
description: Model the domain, key concepts, lifecycles, and system vocabulary.
argument-hint: [domain notes or decisions]
allowed-tools: Read, Write, Edit
---

# /sdw:model

## Purpose

Model the domain language, entities, lifecycles, invariants, and important state transitions.

## Accepted Inputs

- Discovery notes.
- Domain examples.
- Entity lists, workflows, states, or business rules.

## Procedure

1. Read intake, classification, and discovery context.
2. Identify domain concepts, relationships, ownership, lifecycle states, and invariants.
3. Separate confirmed facts from assumptions.
4. Record modeling decisions and unresolved questions.
5. Update workflow state to `modeled` when the model can support system design.

## Output Requirements

- Domain model summary.
- Key entities and relationships.
- Lifecycle or state notes.
- Next command: `/sdw:design`.

## Rules

- Do not pick implementation storage technology unless the design requires it.
- Do not write implementation code.
- Do not advance if the domain model contradicts discovered scope.
