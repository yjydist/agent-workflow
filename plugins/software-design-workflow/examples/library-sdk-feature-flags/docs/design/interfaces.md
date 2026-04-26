# Interfaces

## Public API

- Create an evaluator from a local JSON file.
- Evaluate a flag by key with optional attributes and fallback.

## Result contract

- Typed value.
- Reason describing match, missing flag, or invalid config fallback.
- Boolean indicator for whether fallback was used.

## Configuration contract

- JSON file contains flag definitions and simple targeting attributes.
- Invalid config fails during initialization, not on every evaluation call.
