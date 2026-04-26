# Scope Baseline

## Target

`target-2026-04-sdk-core`

## In scope

- Public evaluator API for boolean, string, and number flags.
- Local JSON provider with schema validation.
- Typed result object with value, reason, and fallback indicator.
- Deterministic fallback behavior for missing or invalid flags.
- Compatibility fixtures for the JSON file format.

## Out of scope

- Hosted flag service.
- Remote polling or streaming updates.
- Web dashboard.
- User targeting rules beyond simple attributes.
- Multi-language SDKs.

## Frozen assumptions

- The first SDK target is single-language.
- Evaluation is synchronous.
- The JSON format must remain backward compatible within this target.
