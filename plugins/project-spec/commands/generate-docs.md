---
description: Generate project specification docs from interview notes and selected project type.
argument-hint: [project type or notes]
allowed-tools: Read, Write, Edit
---

# /project-spec:generate-docs

## Purpose

根据访谈结果生成项目文档初版.

## Agents

- `agents/requirements.md`
- `agents/domain-model.md`
- `agents/architecture.md`
- `agents/interface-contract.md`
- `agents/data-design.md`
- `agents/quality.md`

## Required Skills

- `skills/requirement-writing/SKILL.md`
- `skills/domain-modeling/SKILL.md`
- `skills/architecture-design/SKILL.md`
- `skills/interface-contract-design/SKILL.md`
- `skills/data-design/SKILL.md`
- `skills/error-handling-design/SKILL.md`
- `skills/security-design/SKILL.md`
- `skills/test-design/SKILL.md`
- `skills/acceptance-design/SKILL.md`
- 对应项目类型 skill

## Procedure

1. 阅读 `docs/meta/project-context.md` 和访谈记录.
2. 根据 `docs-template/` 生成或更新 docs.
3. 根据项目类型生成 `docs/type-specific/<project-type>/` 文档.
4. 所有不确定内容写为 `TODO`,并同步到 `docs/review/open-questions.md`.
5. 更新 `docs/README.md` 当前状态为 `docs-generated`.
6. 不生成代码.

## Required Output Files

通用文档:

```text
docs/README.md
docs/meta/project-context.md
docs/meta/decisions.md
docs/meta/change-log.md
docs/product/overview.md
docs/product/scope.md
docs/product/users-and-scenarios.md
docs/requirements/functional-requirements.md
docs/requirements/non-functional-requirements.md
docs/requirements/business-rules.md
docs/design/domain-model.md
docs/design/architecture.md
docs/design/data-design.md
docs/design/interface-contracts.md
docs/design/error-handling.md
docs/design/security-and-permissions.md
docs/delivery/test-plan.md
docs/delivery/acceptance-criteria.md
docs/review/open-questions.md
```

类型专属文档按项目类型生成.

## Rules

- 不允许擅自添加用户没有确认的核心功能.
- 可以补充合理的默认实现,但必须标注为 `Assumption`.
- V1 范围必须小于用户的全部想象范围.
- 文档优先清晰,可执行,不追求形式复杂.
