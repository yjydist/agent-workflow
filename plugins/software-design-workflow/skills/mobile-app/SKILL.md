---
name: mobile-app
description: Legacy compatibility guidance for mobile-app. For new design work, prefer adapters for application, mobile-ui, and mobile-runtime guidance.
---

# Compatibility Skill: Mobile App

Legacy `mobile-app` maps to adapter set `application + mobile-ui + mobile-device + offline-sync`. Prefer adapter docs for new guidance:

```text
adapters/kinds/application.md
adapters/surfaces/mobile-ui.md
adapters/runtimes/mobile-device.md
adapters/concerns/offline-sync.md
```

## Compatibility Assets

Existing reusable assets may still be read as transitional compatibility material:

```text
docs/type-specific/mobile-app/
  screens.md
  navigation.md
  local-storage.md
  permissions.md
  api-client.md
```

## Must Clarify

- iOS / Android / cross-platform
- 页面和导航
- 本地权限
- 离线能力
- 后端 API
- 推送通知是否需要

## Anti-overdesign

V1 默认不做复杂推送,深度原生能力,多端适配细节.
