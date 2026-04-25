---
name: fullstack-web
description: Use when the project-spec combines frontend, backend, auth, persistence, and deployment concerns.
---

# Project Type Skill: Fullstack Web

## Type-specific Docs

```text
docs/type-specific/fullstack-web/
  frontend-pages.md
  backend-api.md
  database.md
  auth.md
  deployment.md
```

## Must Clarify

- 前后端是否分离
- 页面和 API 的映射关系
- SSR / SPA / MPA
- Auth 方案
- 数据提交和校验位置
- 部署方式

## Planning Advice

先实现后端核心 API 和数据,再实现前端页面;或者先做 mock UI,但必须保持 contract 一致.
