---
description: Review generated docs for consistency, gaps, overreach, and V1 readiness.
argument-hint: [review focus]
allowed-tools: Read, Write, Edit
---

# /project:review-docs

## Purpose

对已生成的 docs 做一致性,完整性,可实现性审查.

## Agent

使用 `agents/review.md`.

## Required Skills

- `skills/scope-control/SKILL.md`
- `skills/requirement-writing/SKILL.md`
- `skills/interface-contract-design/SKILL.md`
- `skills/data-design/SKILL.md`
- `skills/security-design/SKILL.md`
- `skills/acceptance-design/SKILL.md`

## Procedure

1. 阅读 `docs/README.md` 中列出的必读文档.
2. 检查文档之间是否一致.
3. 检查是否有 TODO,冲突,遗漏,不可验收项.
4. 检查是否存在过度设计.
5. 将结果写入:
   - `docs/review/review-notes.md`
   - `docs/review/risk-list.md`
   - `docs/review/open-questions.md`
6. 不直接写代码.
7. 如果建议修改正式文档,必须说明影响范围.

## Review Checklist

- Scope:V1 是否明确?是否有偷偷膨胀的功能?
- Requirements:每个功能是否有规则,输入,输出,失败情况?
- Domain:实体关系是否支持需求?
- Data:数据结构是否支持查询和状态变化?
- Interface:接口/命令/组件/API 是否覆盖功能?
- Security:用户是否可能访问不该访问的数据?
- Errors:失败路径是否明确?
- Acceptance:每个 V1 功能是否可测试?
- Complexity:是否适合个人学生项目?

## Output Format

```md
# Review Notes

## Blocking Issues

必须先解决,否则不能进入实现.

## Non-blocking Issues

可以后续处理.

## Over-design Candidates

建议砍掉或放到 V2 的内容.

## Suggested Changes

每条建议必须包含:原因,影响文件,建议改法.
```
