# Implementation Plan

## Milestones

1. Define CLI parser, config schema, and exit codes.
2. Implement repository root detection and safe path traversal.
3. Implement scan rules and finding model.
4. Implement plan file rendering.
5. Add tests for ignored paths, symlink escapes, large files, and golden command output.

## Validation

- Command tests for `scan` and `plan`.
- Fixture repositories for normal files, generated files, ignored files, and unsafe symlinks.
- Diff check showing no fixture mutation after command runs.

## Handoff note

This plan is intentionally read-only. Any destructive cleanup command requires a later target and change review.
