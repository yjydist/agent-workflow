---
description: Start a software design workflow and initialize the design package.
argument-hint: <project idea>
allowed-tools: Read, Write, Edit
---

# /sdw:start

## Purpose

Start a software design workflow from a vague idea and create the minimum design package structure needed for intake.

## Accepted Inputs

- A short project idea.
- A product direction.
- A problem statement.
- A partial brief copied from another tool.

## Procedure

1. Capture the raw intake without over-designing.
2. Create or update initial `docs/` design package files.
3. Record workflow state as `intake`.
4. Identify obvious missing context and prepare for `/sdw:classify`.
5. Keep `docs/README.md` as a human navigation file only.

## Output Requirements

- Intake summary.
- Initial assumptions.
- Open questions.
- Next command: `/sdw:classify`.

## Rules

- Do not write implementation code.
- Do not classify by default if the input is ambiguous.
- Do not create a handoff package at this stage.
