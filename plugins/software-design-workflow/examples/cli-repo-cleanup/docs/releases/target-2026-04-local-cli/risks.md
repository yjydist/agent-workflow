# Risks

## False positives

Simple heuristics may flag useful generated files. Mitigation: require explicit reasons and support ignore patterns in config.

## Path escape bugs

Symlinks or path normalization mistakes could traverse outside the repository root. Mitigation: canonicalize paths, skip escapes, and add dedicated fixtures.

## Scope expansion

Delete or auto-fix behavior could dilute safety guarantees. Mitigation: keep the target read-only and stop if work requests destructive actions.
