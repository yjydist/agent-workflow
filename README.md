# Agent Workflow Marketplace

Personal Codex marketplace for reusable workflow plugins.

## Structure

```text
agent-workflow/
  .agents/plugins/marketplace.json
  plugins/
    software-design-workflow/
      .codex-plugin/plugin.json
      skills/
      docs-template/
      scripts/
```

## Plugin

| Plugin | Purpose | Surface |
| --- | --- | --- |
| `software-design-workflow` | Turn vague software ideas into scoped design and handoff packages. | Codex skills |

## Install Shape

Codex marketplace metadata lives at:

```text
.agents/plugins/marketplace.json
```

The marketplace entry points to:

```text
./plugins/software-design-workflow
```

The plugin manifest lives at:

```text
plugins/software-design-workflow/.codex-plugin/plugin.json
```

## Validate

Validate the marketplace:

```bash
python3 validate_marketplace.py
```

Validate the plugin:

```bash
python3 plugins/software-design-workflow/validate_plugin.py
```

## Add a Plugin

1. Create `plugins/<plugin-name>/`.
2. Add `.codex-plugin/plugin.json`.
3. Add skills or other Codex plugin resources.
4. Add an entry to `.agents/plugins/marketplace.json`.
5. Add a plugin validator if the plugin has custom rules.
