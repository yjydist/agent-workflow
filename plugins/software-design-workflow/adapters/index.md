# Adapter Index

Adapters are short classification prompts used by the `software-design-workflow` skill. Pick only the adapters that change design decisions.

## Kinds

- `application`: user-facing product with workflows and UI or interaction state.
- `service`: long-running backend or API with operational behavior.
- `library-sdk`: reusable API consumed by other code.
- `tooling`: developer or operator tool with commands, files, or automation.
- `knowledge-system`: retrieval, documents, notes, search, or knowledge workflows.
- `agent-system`: model-driven loop, tools, memory, autonomy, or prompt contracts.
- `platform-infra`: shared infrastructure, deployment, provisioning, or governance layer.
- `data-ml-system`: data ingestion, transformation, training, evaluation, or analytics.
- `language-compiler`: parser, interpreter, compiler, linter, or code transformation.
- `embedded-system`: software constrained by device hardware or firmware lifecycle.
- `interactive-media`: game, simulation, creative tool, or highly interactive experience.

## Surfaces

- `web-ui`, `desktop-ui`, `mobile-ui`, `cli`, `tui`.
- `http-api`, `library-api`, `agent-tools`.
- `file-format`, `event-stream`, `ipc`, `background-jobs`.

## Runtimes

- `browser`, `server`, `local-machine`, `mobile-device`.
- `embedded-device`, `cloud-platform`, `offline-first`, `edge-runtime`.

## Domains

- `developer-tools`.
- `knowledge-management`.
- `education-learning`.

## Concerns

- `security-privacy`.
- `offline-sync`.
- `observability`.
- `compatibility`.
- `performance`.
- `ai-safety`.

## Use

Record the selected adapter set before design work starts. Revisit the set when the target changes enough to affect architecture, validation, or handoff.
