---
name: desktop-app
description: Legacy compatibility guidance for desktop-app. For new design work, prefer adapters for application, desktop-ui, and desktop-runtime guidance.
---

# Compatibility Skill: Desktop App

Legacy `desktop-app` maps to adapter set `application + desktop-ui + local-machine + ipc`. Prefer adapter docs for new guidance:

```text
adapters/kinds/application.md
adapters/surfaces/desktop-ui.md
adapters/runtimes/local-machine.md
adapters/surfaces/ipc.md
```

## Compatibility Assets

Existing reusable assets may still be read as transitional compatibility material:

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
