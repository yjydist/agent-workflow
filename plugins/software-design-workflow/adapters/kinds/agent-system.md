# Agent System adapter

## Layer

Kind

## Applies when

Use when the software autonomously or semi-autonomously plans, uses tools, calls models, or acts on behalf of a user.

## Design focus

Define goals, autonomy level, tool boundaries, prompt and memory strategy, approval gates, evaluation, and safety constraints.

## Expected artifacts

Agent loop, tool contracts, memory model, prompt surfaces, safety boundaries, evaluation plan.

## Legacy migration

Legacy `ai-agent` maps to `agent-system + agent-tools + ai-safety`. Reuse prompts, tools, memory, planning, model-usage, safety-boundaries, and evaluation templates.
