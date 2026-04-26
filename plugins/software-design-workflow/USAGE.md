# Usage Guide

This guide explains how to use the `software-design-workflow` Claude Code plugin.

## Install or load

### Validate structure

From `plugins/software-design-workflow/`:

```bash
python3 validate_plugin.py
```

### Local development load

```bash
claude --plugin-dir /absolute/path/to/software-design-workflow
```

Inside Claude Code:

```text
/reload-plugins
```

### Marketplace install

```text
/plugin marketplace add /absolute/path/to/agent-workflow
/plugin install software-design-workflow@agent-workflow
/reload-plugins
```

## Available commands

```text
/sdw:full
/sdw:start
/sdw:classify
/sdw:discover
/sdw:model
/sdw:design
/sdw:quality
/sdw:target
/sdw:freeze-target
/sdw:plan
/sdw:review
/sdw:handoff
/sdw:change
/sdw:status
```

## Standard workflow

Run commands from the target project:

```text
/sdw:start "Build a lightweight issue triage tool for a small engineering team"
/sdw:classify
/sdw:discover
/sdw:model
/sdw:design
/sdw:quality
/sdw:target "Team-local issue triage workflow with manual import and basic reporting"
/sdw:freeze-target
/sdw:plan
/sdw:review
/sdw:handoff
```

State sequence:

```text
intake -> classified -> discovered -> modeled -> designed -> qualified -> planned -> reviewed -> handoff-ready
```

`/sdw:target` defines the current target. `/sdw:freeze-target` locks the current target before planning. After freeze-target, use `/sdw:change` for any change that affects locked scope.

## Handoff output

The workflow end state is `handoff-ready`. Handoff means the package is ready for a future implementation agent to read. It is not an instruction for this plugin to start coding.

Generated docs should distinguish these entry points:

- `docs/handoff/agent-entry.md` is the machine entry point.
- `docs/README.md` is a human navigation file only.

A future implementation agent should start from `docs/handoff/agent-entry.md`, then follow the frozen target, plan, validation notes, and stop conditions.

## Change and status commands

Use change control when requirements or scope move:

```text
/sdw:change "Replace email login with SSO-only authentication"
```

Check the current state:

```text
/sdw:status
```

## Safety rules

- This workflow never writes implementation code.
- Do not skip `/sdw:freeze-target` before `/sdw:plan`.
- Do not skip `/sdw:review` before `/sdw:handoff`.
- Do not preserve `handoff-ready` after a change invalidates the handoff package.
- Do not treat `docs/README.md` as the machine entry point.
- `handoff-ready` means another agent or tool may consume the design package. This plugin itself does not transition into coding.
