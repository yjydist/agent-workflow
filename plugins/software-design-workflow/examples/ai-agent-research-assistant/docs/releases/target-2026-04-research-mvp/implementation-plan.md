# Implementation Plan

## Milestones

1. Define agent prompt, tool registry, and refusal rules.
2. Implement topic intake and clarification loop.
3. Implement source collection and note capture.
4. Implement brief generation with citation checks.
5. Add validation fixtures for successful, ambiguous, and unsafe research requests.

## Validation

- Unit tests for citation enforcement and refusal paths.
- Integration fixture for one approved research topic.
- Manual run that produces a brief with source links and uncertainty notes.

## Handoff note

This plan is for an execution-layer agent. The design workflow stops after producing and reviewing this package.
