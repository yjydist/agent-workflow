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

1. 判断变更类型:
   - 新增功能
   - 修改功能
   - 删除功能
   - 技术栈变更
   - 数据结构变更
   - 接口契约变更
2. 判断是否影响 V1 范围.
3. 如果影响 V1,要求明确取舍:替换哪个功能,或者放到 V2.
4. 写入 `docs/meta/change-log.md`.
5. 如果是重要决策,写入 `docs/meta/decisions.md`.
6. 列出需要修改的文档.
7. 不直接改代码.

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
