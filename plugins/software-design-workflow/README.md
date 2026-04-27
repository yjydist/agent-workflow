# software-design-workflow

`software-design-workflow` is a Codex skill pack for turning vague software directions into a scoped design package with quality checks and handoff notes.

It does not implement the product by default. It prepares decisions, constraints, and plans that an implementation agent or developer can execute.

## Skills

| Skill | Use |
| --- | --- |
| `software-design-workflow` | End-to-end workflow from idea to design package. |
| `scope-control` | Current target selection, freeze, and change control. |
| `handoff-readiness` | Final review before implementation starts. |

## Repository Shape

```text
software-design-workflow/
  .codex-plugin/plugin.json
  skills/
  docs-template/
  adapters/index.md
  rubrics/
  scripts/
```

## Workflow

The compact sequence is:

```text
idea -> classified -> discovered -> modeled -> designed -> qualified -> scoped -> planned -> reviewed -> handoff-ready
```

Use the docs template when a durable package is needed. For lighter work, the main skill can produce the same sections inline.

## Validate

From the plugin directory:

```bash
python3 validate_plugin.py
```

From the repository root:

```bash
python3 plugins/software-design-workflow/validate_plugin.py
```

## Initialize Docs in a Project

```bash
plugins/software-design-workflow/scripts/install-to-project.sh /path/to/project
```

The generated handoff entry point is:

```text
docs/handoff/agent-entry.md
```
