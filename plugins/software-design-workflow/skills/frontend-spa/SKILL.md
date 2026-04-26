---
name: frontend-spa
description: Legacy compatibility guidance for frontend-spa. For new design work, prefer adapters for application, web-ui, and browser guidance.
---

# Compatibility Skill: Frontend SPA

Legacy `frontend-spa` maps to adapter set `application + web-ui + browser`. Prefer adapter docs for new guidance:

```text
adapters/kinds/application.md
adapters/surfaces/web-ui.md
adapters/runtimes/browser.md
```

## Legacy compatibility docs

Existing legacy reusable assets may still be read during migration from:

```text
docs/type-specific/frontend-spa/
  pages.md
  components.md
  routing.md
  state-management.md
  api-client.md
  ui-interactions.md
```

## Must Clarify

- 页面列表
- 用户路径
- 组件层级
- 状态来源:local state / global store / server state
- 表单校验
- loading / empty / error states
- API contract

## Anti-overdesign

不要一开始设计复杂 design system,除非项目目标就是 UI 组件库.
