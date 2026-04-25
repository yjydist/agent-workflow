---
name: docs-maintenance
description: Use when maintaining generated workflow docs, resolving TODOs, and keeping state consistent.
---

# Skill: Docs Maintenance

## Goal

保持 docs 在项目迭代中一致,可读,可追踪.

## Rules

- 重要设计选择写入 `docs/meta/decisions.md`.
- 需求变更写入 `docs/meta/change-log.md`.
- 未解决问题写入 `docs/review/open-questions.md`.
- 风险写入 `docs/review/risk-list.md`.
- `docs/README.md` 负责维护阅读顺序和项目状态.

## Decision Record Template

```md
## Dxxx: Decision Title

Date:
Status: accepted / rejected / superseded

### Context

### Decision

### Consequences
```
