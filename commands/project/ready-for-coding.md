---
description: Validate readiness gates and mark a frozen project ready for coding.
argument-hint: [readiness notes]
allowed-tools: Read, Write, Edit
---

# /project:ready-for-coding

## Purpose

在实现计划生成后做最终 readiness validation. 该命令不生成代码, 只验证项目是否可以交给 coding agent 分 Phase 实现.

## Required Reads

- `docs/README.md`
- `docs/product/scope.md`
- `docs/review/review-notes.md`
- `docs/review/open-questions.md`
- `docs/delivery/implementation-plan.md`
- `docs/delivery/acceptance-criteria.md`

## Preconditions

- `docs/README.md` 当前状态必须是 `implementation-planned`.
- `docs/README.md` 的 V1 status 必须是 `frozen`.
- `docs/delivery/implementation-plan.md` 必须存在并包含可执行 Phase.
- `docs/delivery/acceptance-criteria.md` 必须覆盖 V1 must-have 功能.
- `docs/review/review-notes.md` 的 `Blocking Issues` 必须为空, 或所有条目都标记为 resolved.
- `docs/review/open-questions.md` 中 `Blocking V1? yes` 的问题必须全部 resolved, 或明确移出 V1.
- 用户确认已经审阅 implementation plan 和 acceptance criteria.

## Procedure

1. 检查所有 Preconditions.
2. 如果任何条件不满足, 停止, 只报告缺口和下一步修复建议.
3. 如果全部满足, 更新 `docs/README.md` 当前状态为 `ready-for-coding`.
4. 输出 coding agent 应读取的文档和第一个 Phase.

## Output Format

```md
# Ready For Coding Check

## Result

ready / blocked

## Blocking Gaps

## Required Reading For Coding Agent

## First Phase
```

## Rules

- 不生成业务代码.
- 不修改 scope, requirements, design 或 implementation plan 内容.
- 只允许在 readiness 通过时更新 `docs/README.md` 的 Current stage.
- 如果用户没有确认, 不得进入 `ready-for-coding`.
