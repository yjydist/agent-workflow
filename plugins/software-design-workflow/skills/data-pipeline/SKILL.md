---
name: data-pipeline
description: Legacy compatibility guidance for data-pipeline. For new design work, prefer adapters for pipeline, batch-processing, and data-store guidance.
---

# Compatibility Skill: Data Pipeline

Legacy `data-pipeline` maps to adapter set `data-ml-system + background-jobs + file-format + observability`. Prefer adapter docs for new guidance:

```text
adapters/kinds/data-ml-system.md
adapters/surfaces/background-jobs.md
adapters/surfaces/file-format.md
adapters/concerns/observability.md
```

## Compatibility Assets

Existing reusable assets may still be read as transitional compatibility material:

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
