# Tooling adapter

## Layer

Kind

## Applies when

Use when the software helps users or developers perform tasks through commands, generators, automation, or local workflows.

## Design focus

Define tasks automated, command model, configuration, inputs and outputs, exit behavior, integration points, and safe defaults.

## Expected artifacts

Command map, config model, IO behavior, exit codes, install or distribution notes.

## Legacy migration

Legacy `cli-tool` maps to `tooling + cli + local-machine`. Reuse commands, flags, config, input-output, and exit-codes templates as CLI surface details.
