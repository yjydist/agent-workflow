---
name: implementation-planning
description: Use when converting frozen V1 docs into phased implementation tasks and acceptance checks.
---

# Skill: Implementation Planning

## Goal

把设计文档拆成 coding agent 可以稳定执行的任务.

## Phase Template

```md
## Phase N:Name

### Goal

### Required Docs

### Allowed Changes

### Forbidden Changes

### Tasks

### Acceptance

### Notes for Coding Agent
```

## Rules

- 每个 Phase 只做一个主题.
- Phase 顺序应该从基础设施到核心功能,再到测试和文档.
- 每个 Phase 都必须能验证.
- 明确禁止 coding agent 做 V1 外功能.
