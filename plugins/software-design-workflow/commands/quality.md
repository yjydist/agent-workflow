---
description: Define quality attributes, risks, acceptance criteria, and validation approach.
argument-hint: [quality focus or constraints]
allowed-tools: Read, Write, Edit
---

# /sdw:quality

## Purpose

Define quality attributes, acceptance criteria, risk checks, and validation approach for the design.

## Accepted Inputs

- Design notes.
- Performance, security, reliability, usability, maintainability, or compliance expectations.
- Acceptance examples or test expectations.

## Procedure

1. Read current design docs.
2. Identify quality attributes and measurable acceptance criteria.
3. Record validation methods, review risks, and blocking quality gaps.
4. Update workflow state to `qualified` when the design has enough quality definition for target locking.
5. Recommend `/sdw:target` for current target selection.

## Output Requirements

- Quality criteria.
- Acceptance and validation notes.
- Blocking risks.
- Next command: `/sdw:target`.

## Rules

- Do not write implementation code.
- Do not mark vague quality goals as accepted without validation signals.
- Do not proceed if acceptance is impossible to judge.
