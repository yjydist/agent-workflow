---
name: fullstack-web
description: Legacy compatibility guidance for fullstack-web. For new design work, prefer adapters for application, web-ui, server, and persistence guidance.
---

# Compatibility Skill: Fullstack Web

Legacy `fullstack-web` maps to adapter set `application + web-ui + http-api + server`. Prefer adapter docs for new guidance:

```text
adapters/kinds/application.md
adapters/surfaces/web-ui.md
adapters/surfaces/http-api.md
adapters/runtimes/server.md
```

## Compatibility Assets

Existing reusable assets may still be read as transitional compatibility material:

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
