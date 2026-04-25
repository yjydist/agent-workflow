---
name: rag-app
description: Use when the project-spec uses retrieval augmented generation, ingestion, chunking, retrieval, or answer quality checks.
---

# Project Type Skill: RAG App

## Type-specific Docs

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
