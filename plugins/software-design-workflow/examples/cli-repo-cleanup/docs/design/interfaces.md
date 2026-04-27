# Interfaces

## Commands

- `repo-clean scan`: inspect the repository and print findings with reasons.
- `repo-clean plan`: write a reviewable cleanup plan file without changing repository contents.

## Inputs

- Repository root or explicit path.
- Optional config file with ignore patterns and size limits.

## Output expectations

- Human-readable findings and exit codes.
- Reported skips for unsafe symlinks or out-of-root traversal attempts.
