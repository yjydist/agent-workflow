# Requirements

## Functional requirements

- Consumers can create an evaluator from a JSON file path.
- Consumers can evaluate a flag by key and optional attributes.
- Evaluation returns a typed result with value, reason, and fallback status.
- Invalid config fails with a structured error.
- Missing flag keys return the caller-provided fallback.

## Non-functional requirements

- Evaluation should not perform filesystem reads after initialization.
- Public API names should be stable within the target.
- Error messages should identify config location without leaking unrelated local paths.
