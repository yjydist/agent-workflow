---
description: Create a phased implementation plan from frozen V1 docs.
argument-hint: [planning constraints]
allowed-tools: Read, Write, Edit
---

# /project:plan-implementation

## Purpose

把冻结后的文档转成 coding agent 可执行的分阶段开发计划.

## Agent

使用 `agents/implementation-planner.md`.

## Required Skills

- `skills/implementation-planning/SKILL.md`
- `skills/acceptance-design/SKILL.md`
- 对应项目类型 skill

## Required Reads

- `docs/README.md`
- `docs/product/scope.md`
- `docs/requirements/functional-requirements.md`
- `docs/design/architecture.md`
- `docs/design/data-design.md`
- `docs/design/interface-contracts.md`
- `docs/design/security-and-permissions.md`
- `docs/delivery/acceptance-criteria.md`

## Procedure

1. 只针对冻结后的 V1 规划实现.
2. 把实现拆成多个 Phase.
3. 每个 Phase 必须包含:
   - 目标
   - 输入文档
   - 允许修改的文件/目录
   - 禁止事项
   - 实现步骤
   - 验收命令或验收方法
4. 写入 `docs/delivery/implementation-plan.md`.
5. 更新 `docs/README.md` 当前状态为 `implementation-planned`, 并报告实现计划已完成.
6. 检查 `docs/delivery/implementation-plan.md`, 验收标准和必读文档是否完整, 但不要在同一次执行中更新为 `ready-for-coding`.
7. 如果所有准备项完整, 提醒用户审阅实现计划后再运行 readiness 流程或手动确认进入 `ready-for-coding`.

## Phase Template

```md
## Phase N:名称

### Goal

### Required Docs

### Allowed Changes

### Forbidden Changes

### Tasks

### Acceptance

### Notes for Coding Agent
```

## Rules

- 每个 Phase 尽量小.
- 每个 Phase 完成后项目应可运行,可测试,或者至少可静态验证.
- 不要把多个无关模块塞进同一个 Phase.
- 不要在实现计划中加入 V1 范围外功能.
