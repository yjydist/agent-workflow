---
name: ai-agent
description: Use when the project-spec is an AI agent and needs prompts, tools, memory, safety, or evaluation docs.
---

# Project Type Skill: AI Agent

## Type-specific Docs

```text
docs/type-specific/ai-agent/
  model-usage.md
  prompts.md
  tools.md
  memory.md
  planning.md
  safety-boundaries.md
  evaluation.md
```

## Must Clarify

- Agent 目标
- 模型供应商和模型
- 系统提示词边界
- 可用工具
- 工具输入输出 schema
- 是否有记忆
- 是否允许写文件,执行命令,调用外部 API
- 失败和重试策略
- 评估用例

## Safety Defaults

- 默认不自动执行危险命令.
- 默认不删除文件.
- 默认需要用户确认外部写操作.
