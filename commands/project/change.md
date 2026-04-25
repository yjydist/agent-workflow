---
description: Process a requested project change through scope and decision records.
argument-hint: <change request>
allowed-tools: Read, Write, Edit
---

# /project:change

## Purpose

处理项目中途需求变更,避免随意改需求导致实现失控.

## User Input

用户提出变更,例如:

```text
我想给任务系统加一个标签功能.
```

## Procedure

### Impact analysis

1. 判断变更类型:
   - 新增功能
   - 修改功能
   - 删除功能
   - 技术栈变更
   - 数据结构变更
   - 接口契约变更
2. 判断是否影响 V1 范围.
3. 如果影响 V1, 要求明确取舍: 替换哪个功能, 或者放到 V2.
4. 写入 `docs/meta/change-log.md`.
5. 如果是重要决策, 写入 `docs/meta/decisions.md`.
6. 列出 impacted docs 和 impacted implementation phases.
7. 等待用户确认 recommendation.

### Apply change

8. 用户确认后, 更新所有 impacted docs.
9. 至少检查并按需更新 `docs/product/scope.md`, `docs/requirements/functional-requirements.md`, `docs/requirements/business-rules.md`, `docs/design/interface-contracts.md`, `docs/design/data-design.md`, `docs/delivery/implementation-plan.md`, `docs/delivery/acceptance-criteria.md`.
10. 如果 V1 已冻结且用户确认变更进入 V1, 在 `docs/meta/decisions.md` 追加 superseding decision.
11. 不直接改代码.

## Output Format

```md
# Change Impact Analysis

## Proposed Change

## Impacted Docs

## Impacted Implementation Phases

## Recommendation

- Accept into V1 / Move to V2 / Reject for now

## Required User Decision
```

## Rules

- 已冻结 V1 后,默认把新需求放到 V2.
- 只有当用户明确愿意替换或缩小其他 V1 功能时,才允许进入 V1.
- 所有变更必须先更新文档,再改代码.
