# Scope Baseline

## Target

`target-2026-04-local-cli`

## In scope

- `repo-clean scan` prints candidate files with reasons.
- `repo-clean plan` writes a cleanup plan file.
- Config file supports ignore patterns and max file size.
- Exit codes distinguish success, findings, config error, and filesystem error.
- Logs include scanned roots and skipped paths.

## Out of scope

- Deleting files.
- Modifying repository contents.
- Remote repository integration.
- Watch mode.
- Interactive TUI.

## Frozen assumptions

- The CLI runs from a repository root or a provided path.
- The first target is read-only.
- Symlinks outside the root are skipped and reported.
