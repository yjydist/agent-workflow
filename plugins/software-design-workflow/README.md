# software-design-workflow

`software-design-workflow` is a declarative Claude Code plugin for software design. It turns vague project directions into a reviewed, scope-locked, handoff-ready design package. It does not write application code and does not treat the end of the workflow as coding permission.

## Command family

The plugin exposes `/sdw:*` commands:

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

## Workflow

Canonical state sequence:

```text
intake -> classified -> discovered -> modeled -> designed -> qualified -> planned -> reviewed -> handoff-ready
```

Scope is managed through the current target and `/sdw:freeze-target`:

- The current target is the active scope slice to plan and hand off.
- `/sdw:freeze-target` locks that target before `/sdw:plan`.
- After freeze-target, affected changes must go through `/sdw:change`.

The workflow ends at `handoff-ready`. Handoff means the design package is ready for a future implementation agent. It does not mean this plugin should start coding.

## Entry points in generated docs

- `docs/handoff/agent-entry.md` is the machine entry point for a future implementation agent.
- `docs/README.md` is a human navigation file only.

Future agents should not treat `docs/README.md` as the machine entry point.

## Adapter model

The workflow now classifies software through composable adapters instead of a single project-type label. Adapters are concise design prompts grouped by layer:

- `adapters/kinds/`: what the software primarily is, such as `application`, `service`, `library-sdk`, `tooling`, or `agent-system`.
- `adapters/surfaces/`: how users or systems interact, such as `web-ui`, `cli`, `http-api`, `library-api`, or `agent-tools`.
- `adapters/runtimes/`: where it executes, such as `browser`, `server`, `local-machine`, or `cloud-platform`.
- `adapters/domains/`: problem-domain prompts, such as `knowledge-management`, `education-learning`, or `developer-tools`.
- `adapters/concerns/`: cross-cutting concerns, such as `security-privacy`, `offline-sync`, `observability`, `compatibility`, `performance`, or `ai-safety`.

Use multiple adapters when a target crosses boundaries. The current target should name the active adapter set so downstream design, quality, plan, review, and handoff work can check the same assumptions.

### Compatibility mapping from legacy project types

Existing type-specific assets remain available and are reinterpreted through adapters rather than deleted. The `type-specific-templates/` tree is retained as a compatibility layer during migration, not as the primary modeling system:

| Legacy type | Adapter set | Migration note |
| --- | --- | --- |
| `backend-api` | `service + http-api + server` | Move endpoint contracts into `http-api`, persistence and service boundaries into `service`, and deployment/runtime details into `server`. |
| `frontend-spa` | `application + web-ui + browser` | Move pages, components, routing, API client, and client state into `web-ui` and browser runtime guidance. |
| `cli-tool` | `tooling + cli + local-machine` | Move command, flag, config, IO, and exit-code docs into the CLI surface and local-machine runtime model. |
| `ai-agent` | `agent-system + agent-tools + ai-safety` | Move tools into `agent-tools`, prompts, memory, and planning into `agent-system`, and safety or evaluation into `ai-safety`. |

## Claude Code plugin usage

### Validate the plugin

From `plugins/software-design-workflow/`:

```bash
python3 validate_plugin.py
```

### Local development load

Start Claude Code with the plugin directory:

```bash
claude --plugin-dir /absolute/path/to/software-design-workflow
```

Then reload plugins:

```text
/reload-plugins
```

### Marketplace install

This plugin is distributed by the `agent-workflow` marketplace:

```text
/plugin marketplace add /absolute/path/to/agent-workflow
/plugin install software-design-workflow@agent-workflow
/reload-plugins
```

## Typical command flow

```text
/sdw:start <project idea>
/sdw:classify
/sdw:discover
/sdw:model
/sdw:design
/sdw:quality
/sdw:target <current target>
/sdw:freeze-target
/sdw:plan
/sdw:review
/sdw:handoff
```

For a guided run, use:

```text
/sdw:full <project idea>
```

For changes, use:

```text
/sdw:change <change request>
```

For status, use:

```text
/sdw:status
```

## Core rules

1. Design before implementation.
2. This workflow never writes implementation code.
3. Keep scope explicit with current target.
4. Lock scope with `/sdw:freeze-target` before planning.
5. Review before handoff.
6. End at `handoff-ready`, where another agent or tool may consume the design package.
