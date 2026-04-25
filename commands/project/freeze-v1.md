---
description: Freeze V1 scope and record what is in, out, and deferred.
argument-hint: [scope decisions]
allowed-tools: Read, Write, Edit
---

# /project:freeze-v1

## Purpose

冻结 V1 范围,防止实现阶段范围膨胀.

## Required Reads

- `docs/product/scope.md`
- `docs/review/review-notes.md`
- `docs/review/open-questions.md`
- `docs/meta/decisions.md`

## Procedure

1. 确认所有 blocking open questions 已解决或移出 V1.
2. 将 V1 必做功能写入 `docs/product/scope.md`.
3. 将 V1 明确不做功能写入 `docs/product/scope.md`.
4. 将 V2 候选写入 `docs/product/scope.md`.
5. 在 `docs/meta/decisions.md` 记录冻结决策.
6. 更新 `docs/README.md` 当前项目状态.

## Frozen Scope Template

```md
# Scope

## V1 Must Have

- ...

## V1 Explicitly Out of Scope

- ...

## V2 Candidates

- ...

## Scope Lock Rule

实现 V1 期间不得新增 Must Have 功能.
任何新想法必须先写入 V2 Candidates 或通过 /project:change 走变更流程.
```

## Rules

- open questions 未处理完,不允许冻结.
- 不能把"以后可能做"的内容写入 V1.
- V1 应该是 1-4 周内个人可完成的小闭环.
