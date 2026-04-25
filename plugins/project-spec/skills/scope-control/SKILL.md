---
name: scope-control
description: Use when trimming V1 scope, identifying out-of-scope work, and preventing feature creep.
---

# Skill: Scope Control

## Goal

把项目压缩成适合 V1 的最小闭环.

## Checklist

- V1 是否只有一个主要目标?
- 是否存在没有必要的高级技术?
- 是否存在多人协作,复杂权限,实时通知,支付,复杂部署等膨胀点?
- 是否能在 1-4 周内个人完成?
- 是否每个 V1 功能都有明确验收标准?

## Decision Categories

```md
## V1 Must Have

## V1 Explicitly Out of Scope

## V2 Candidates

## Removed for Now

## Rationale
```

## Student Project Defaults

默认不做:

- 微服务
- Kubernetes
- 复杂 RBAC
- 多租户
- 支付
- 实时协作
- 大规模高并发
- 复杂监控体系

除非用户明确表示项目目标就是练这些.
