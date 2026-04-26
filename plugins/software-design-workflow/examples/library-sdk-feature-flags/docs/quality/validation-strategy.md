# Validation Strategy

## Primary checks

- Verify the public API works for boolean, string, and number flags.
- Confirm invalid config surfaces structured initialization errors.
- Confirm compatibility fixtures remain accepted across target iterations.

## Evidence expectations

Implementation work should include API tests, JSON fixture tests, and a small performance check showing repeated evaluation is in-memory only.
