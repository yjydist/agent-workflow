# Software design workflow anti-patterns

Avoid these patterns when using or maintaining `software-design-workflow`.

## Workflow anti-patterns

- Skipping discovery and modeling, then treating architecture guesses as requirements.
- Advancing to `handoff-ready` while blocking open questions remain.
- Treating `planned` as permission to start coding without review and handoff checks.
- Hiding scope changes in implementation notes instead of using `/sdw:change`.

## Documentation anti-patterns

- Duplicating conflicting requirements across project, target, and handoff docs.
- Leaving template placeholders that look like real decisions.
- Making `agent-entry.md` a summary only, instead of a safe entry point with required reading order.
- Recording decisions without rationale, tradeoffs, or validation implications.

## Tooling anti-patterns

- Allowing unrestricted `Bash` in command or agent tool declarations.
- Making validators depend on network access, timestamps, or generated examples.
- Validating prose style instead of stable structure and required workflow gates.
