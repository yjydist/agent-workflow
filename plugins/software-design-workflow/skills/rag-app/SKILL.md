---
name: rag-app
description: Legacy compatibility guidance for rag-app. For new design work, prefer adapters for agent, retrieval, and knowledge-base guidance.
---

# Compatibility Skill: RAG App

Legacy `rag-app` maps to adapter set `knowledge-system + agent-system + knowledge-management + ai-safety`. Prefer adapter docs for new guidance:

```text
adapters/kinds/knowledge-system.md
adapters/kinds/agent-system.md
adapters/domains/knowledge-management.md
adapters/concerns/ai-safety.md
```

## Compatibility Assets

Existing reusable assets may still be read as transitional compatibility material:

```text
docs/type-specific/rag-app/
  documents.md
  ingestion.md
  chunking.md
  embedding.md
  retrieval.md
  generation.md
  evaluation.md
```

## Must Clarify

- 文档来源
- 文档格式
- 解析方式
- chunk 策略
- embedding 模型
- 向量库
- 检索策略
- 引用和答案格式
- 评估问题集

## Anti-overdesign

V1 可以先做单用户,本地文档,小规模向量库,不做复杂权限和在线协作.
