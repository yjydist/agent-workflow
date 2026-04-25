---
name: interface-contract-design
description: Use when defining APIs, CLI commands, SDK methods, UI contracts, events, or agent tools.
---

# Skill: Interface Contract Design

## Goal

定义系统内部或外部交互契约.

## Contract Types

- HTTP API
- UI routes and components
- CLI commands and flags
- SDK public API
- Agent tools schema
- Event/message schema
- File format

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
