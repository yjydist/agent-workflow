# Requirements

## Functional requirements

- `repo-clean scan` must list cleanup candidates with a reason for each finding.
- `repo-clean plan` must write a reviewable plan file without modifying repository files.
- The CLI must support ignore patterns and a maximum file size setting.
- Unsafe traversal outside the repository root must be skipped and reported.

## Non-functional requirements

- Every filesystem action in this target must preserve dry-run semantics.
- Exit codes must distinguish clean runs, findings, config errors, and filesystem errors.
- Output should remain stable enough for golden fixture tests.
