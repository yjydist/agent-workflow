---
name: project-classification
description: Use when classifying a new project idea into canonical workflow project types.
---

# Skill: Project Classification

## Goal

根据用户想法识别软件项目类型,并选择合适的文档模板.

## Supported Types

- `backend-api`
- `frontend-spa`
- `fullstack-web`
- `cli-tool`
- `desktop-app`
- `mobile-app`
- `library-sdk`
- `ai-agent`
- `rag-app`
- `data-pipeline`

## Classification Questions

1. 用户如何使用这个软件?浏览器,命令行,桌面,手机,代码调用,聊天界面?
2. 是否需要后端服务?
3. 是否需要持久化数据?
4. 是否需要调用 LLM 或 embedding?
5. 是否主要提供 API / UI / 命令 / SDK / 自动化流程?
6. 是否有外部系统集成?

## Output Template

```md
## Project Type

Primary: ...
Secondary: ...

## Reasoning

## Required Type-specific Docs

## Recommended Skills

## Open Questions
```
