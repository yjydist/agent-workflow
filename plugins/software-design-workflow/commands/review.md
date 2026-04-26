---
description: Review the design package for consistency, gaps, and handoff blockers.
argument-hint: [review focus]
allowed-tools: Read, Write, Edit
---

# /sdw:review

## Purpose

Review the full design package and plan for consistency, completeness, scope control, and handoff blockers.

## Accepted Inputs

- Review focus.
- Known risks.
- A request to re-check the package after updates.

## Procedure

1. Read the design package, frozen target, and plan.
2. Check consistency across intake, classification, discovery, model, design, quality, target, and plan.
3. Identify missing decisions, contradictions, overreach, and handoff blockers.
4. If blockers remain, report them, keep the workflow state at `planned`, and recommend the earliest command needed to fix them before rerunning `/sdw:review`.
5. Update workflow state to `reviewed` only when blocking issues are resolved.
6. Prepare `/sdw:handoff` recommendations only after the package is truly review-clean.

## Output Requirements

- Review result.
- Blocking issues, if any, with the earliest recommended fix command.
- Non-blocking concerns.
- Next command: `/sdw:handoff` only when blockers are resolved, otherwise the earliest command needed to fix blockers.

## Rules

- Do not write implementation code.
- Do not rubber-stamp inconsistent docs.
- Do not mark the package `reviewed` while blockers remain, even if owners or follow-up commands are already clear.
- Do not advance to handoff-ready from this command.
