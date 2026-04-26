---
description: Discover users, goals, constraints, risks, and open questions.
argument-hint: [answers, notes, or focus area]
allowed-tools: Read, Write, Edit
---

# /sdw:discover

## Purpose

Discover enough user, scope, business, data, and constraint context to support design.

## Accepted Inputs

- Answers to discovery questions.
- Stakeholder notes.
- Constraints, non-goals, examples, edge cases, or acceptance signals.

## Procedure

1. Read classification and intake context.
2. Clarify goals, users, scenarios, constraints, risks, data, interfaces, and non-goals.
3. Keep questions focused and limited to decisions that affect design.
4. Record open questions and assumptions.
5. Update workflow state to `discovered` when design can proceed.

## Output Requirements

- Discovery summary.
- Confirmed scope signals.
- Open questions and assumptions.
- Next command: `/sdw:model`.

## Rules

- Do not fill critical business decisions silently.
- Do not write implementation code.
- Do not advance if key scope or actor questions remain blocking.
