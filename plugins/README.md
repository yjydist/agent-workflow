# Plugins

This directory contains local Codex plugins published by the `agent-workflow` marketplace.

| Plugin | Description |
| --- | --- |
| `software-design-workflow` | Compact skill pack for software design, scope control, and handoff readiness. |

## Conventions

- Plugin directory names must match `.codex-plugin/plugin.json` `name`.
- Marketplace entries live in `.agents/plugins/marketplace.json`.
- Local plugin entries use `source.source: "local"` and `source.path: "./plugins/<plugin-name>"`.
- Keep plugin surfaces small. Prefer a focused skill over command, agent, example, or compatibility layers.
