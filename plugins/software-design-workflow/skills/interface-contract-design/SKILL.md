---
name: interface-contract-design
description: Use when defining APIs, CLI commands, SDK methods, UI contracts, events, or agent tools.
---

# Skill: Interface Contract Design

## Goal

定义系统内部或外部交互契约.

## Adapter Surface Contract Types

Use the active surface adapters to decide which contracts are required:

- `http-api`: HTTP endpoints, request and response schemas, status codes, auth, pagination, idempotency.
- `web-ui`, `desktop-ui`, `mobile-ui`, `tui`: routes, screens, components, interaction states, accessibility, input and output behavior.
- `cli`: commands, flags, config, stdin, stdout, stderr, exit codes.
- `library-api`: public functions, classes, modules, types, examples, versioning.
- `agent-tools`: tool schema, permissions, side effects, confirmation gates, retries.
- `event-stream`: event and message schema, delivery semantics, ordering, retention.
- `file-format`: file schema, examples, validation, compatibility.
- `ipc`: channels, message schemas, lifecycle, permissions, timeout behavior.
- `background-jobs`: job triggers, payloads, retries, progress, cancellation.

## Generic Contract Template

```md
## Contract Name

### Purpose

### Caller / User

### Input

### Output

### Error Cases

### Permission / Preconditions

### Examples
```

## Rules

- 所有契约必须有输入和输出.
- 所有契约必须有错误情况.
- 契约变化必须记录到 change-log.
