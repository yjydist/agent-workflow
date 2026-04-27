# AGENTS.md

This repository is a local Codex marketplace named `agent-workflow`.

It is not an application runtime. It distributes reusable Codex plugins, primarily `software-design-workflow`, a compact skill pack for turning vague software directions into scoped design and handoff packages.

## Common Commands

Validate the whole marketplace from the repository root:

```bash
python3 validate_marketplace.py
```

Validate the plugin:

```bash
python3 plugins/software-design-workflow/validate_plugin.py
```

The repository has no package-manager build step. Python validators are the structural tests.

## Marketplace Structure

- `.agents/plugins/marketplace.json` defines Codex marketplace metadata and plugin ordering.
- `plugins/` contains plugin directories.
- Each plugin directory must contain `.codex-plugin/plugin.json`.
- `plugins/software-design-workflow/` exposes Codex skills through `skills/`.

## Plugin Rules

New plugins should follow this shape:

1. Create `plugins/<plugin-name>/`.
2. Add `plugins/<plugin-name>/.codex-plugin/plugin.json`.
3. Add a marketplace entry to `.agents/plugins/marketplace.json`.
4. Use `source.source: "local"` and `source.path: "./plugins/<plugin-name>"`.
5. Add a plugin-local validator when the plugin has custom structure.

Do not add old marketplace manifests, command surfaces, or subagent directories. They are intentionally absent.

## Software Design Workflow

The current plugin is skill-driven:

- `software-design-workflow`: end-to-end design package workflow.
- `scope-control`: current target selection, freeze, and change control.
- `handoff-readiness`: final consistency and execution-readiness review.

The workflow can produce docs under:

```text
docs/project/
docs/analysis/
docs/design/
docs/quality/
docs/releases/current-target/
docs/handoff/
```

The handoff entry point is `docs/handoff/agent-entry.md`.

## Validation Rules

Keep validators aligned with the simplified Codex structure:

- Root marketplace entries point directly to `./plugins/<name>`.
- Plugin manifests use `.codex-plugin/plugin.json`.
- Required skills have `SKILL.md` files with matching `name` frontmatter.
- Removed marketplace compatibility directories stay absent.
- Text files must not contain local absolute path leaks or fullwidth punctuation.
