# Adapter system

The adapter system helps projects describe their real shape without forcing them into a single fixed project-type label. Instead of picking one category and stretching it to fit, projects combine adapters across multiple layers to capture what the software is, how it is used, where it runs, which domain language matters, and which cross-cutting concerns must guide the design.

## Adapter layers

The adapter system is organized into five layers:

- kinds
- surfaces
- runtimes
- domains
- concerns

Projects usually use combinations of adapters across these layers. For example, one project might combine a service kind, an HTTP API surface, a cloud platform runtime, a developer tools domain, and strong observability concerns. Another project may use a library SDK kind, a CLI surface, a local machine runtime, and compatibility concerns. The goal is to describe the project as a composition of traits, not to force it under one fixed label.

## Layer indexes

Use the layer indexes below to browse available adapters:

- [Kinds](./kinds/index.md)
- [Surfaces](./surfaces/index.md)
- [Runtimes](./runtimes/index.md)
- [Domains](./domains/index.md)
- [Concerns](./concerns/index.md)
