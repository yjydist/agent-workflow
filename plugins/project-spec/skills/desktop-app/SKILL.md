---
name: desktop-app
description: Use when the project-spec is a desktop application with local state, packaging, permissions, or UI flows.
---

# Project Type Skill: Desktop App

## Type-specific Docs

```text
docs/type-specific/desktop-app/
  windows.md
  menus.md
  local-storage.md
  native-integration.md
  packaging.md
```

## Must Clarify

- 桌面框架:Electron / Tauri / native
- 窗口和页面
- 本地数据存储
- 文件系统访问
- 自动更新是否需要
- 打包目标平台

## Anti-overdesign

V1 通常不做自动更新,多平台深度适配,复杂原生集成.
