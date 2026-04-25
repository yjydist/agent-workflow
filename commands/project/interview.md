---
description: Interview the user to clarify scope, users, data, interfaces, risks, and acceptance.
argument-hint: [project context or answers]
allowed-tools: Read, Write, Edit
---

# /project:interview

## Purpose

通过多轮访谈补齐项目规格所需信息.

## Agent

使用 `agents/project-interviewer.md`.

## Required Skills

- `skills/requirement-writing/SKILL.md`
- `skills/domain-modeling/SKILL.md`
- `skills/interface-contract-design/SKILL.md`
- `skills/data-design/SKILL.md`
- `skills/acceptance-design/SKILL.md`
- `skills/scope-control/SKILL.md`

## Procedure

1. 阅读已有 docs,尤其是:
   - `docs/meta/project-context.md`
   - `docs/product/scope.md`,如果存在
   - `docs/review/open-questions.md`,如果存在
2. 判断当前缺失信息.
3. 每轮最多问 6 个问题.
4. 优先询问会影响以下内容的问题:
   - 项目范围
   - 用户角色
   - 核心场景
   - 数据实体
   - 接口/交互契约
   - 权限和安全
   - 验收方式
5. 用户回答后,更新 open questions 状态.
6. 当信息足够生成初版文档时,建议运行 `/project:generate-docs`.

## Question Priority

优先级从高到低:

1. V1 做什么,不做什么.
2. 用户是谁,以及核心使用路径.
3. 核心实体有哪些.
4. 外部交互方式是什么:HTTP API,页面,CLI 命令,SDK API,Agent tools 等.
5. 数据如何保存.
6. 错误如何处理.
7. 如何验收项目完成.
8. 技术栈约束.

## Rules

- 不要一次问超过 6 个问题.
- 不要问审美偏好,除非项目是 UI 密集型.
- 用户回答模糊时继续追问.
- 如果用户提出过大功能,建议放到 V2.
- 不确定内容写入 TODO,不要自行决定.
