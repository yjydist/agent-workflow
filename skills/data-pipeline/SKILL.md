---
name: data-pipeline
description: Use when the project ingests, transforms, validates, schedules, or exports data pipelines.
---

# Project Type Skill: Data Pipeline

## Type-specific Docs

```text
docs/type-specific/data-pipeline/
  sources.md
  schema.md
  transformations.md
  scheduling.md
  validation.md
  outputs.md
  observability.md
```

## Must Clarify

- 数据来源
- 输入 schema
- 清洗规则
- 转换逻辑
- 输出位置
- 调度方式
- 失败重试
- 数据质量校验

## Acceptance

数据项目必须有样例输入,期望输出,失败样例和校验方法.
