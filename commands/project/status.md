---
description: Report current workflow state, docs completeness, risks, and next action.
argument-hint: [status focus]
allowed-tools: Read, Write, Edit
---

# /project:status

## Purpose

读取当前 docs,汇总项目状态.

## Required Reads

- `docs/README.md`
- `docs/product/scope.md`
- `docs/review/open-questions.md`
- `docs/review/risk-list.md`
- `docs/delivery/implementation-plan.md`

## Output Format

```md
# Project Status

## Current Stage

## Project Type

## V1 Scope Summary

## Blocking Open Questions

## Main Risks

## Next Recommended Command
```

## Rules

- 不生成新需求.
- 不修改文档,除非用户明确要求.
- 如果状态信息缺失,指出缺失文件或字段.
