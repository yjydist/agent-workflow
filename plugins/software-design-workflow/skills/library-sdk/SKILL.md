---
name: library-sdk
description: Legacy compatibility guidance for library-sdk. For new design work, prefer adapters for library, public-api, and package-distribution guidance.
---

# Compatibility Skill: Library / SDK

Legacy `library-sdk` maps to adapter set `library-sdk + library-api + compatibility`. Prefer adapter docs for new guidance:

```text
adapters/kinds/library-sdk.md
adapters/surfaces/library-api.md
adapters/concerns/compatibility.md
```

## Compatibility Assets

Existing reusable assets may still be read as transitional compatibility material:

```text
docs/type-specific/library-sdk/
  public-api.md
  types.md
  examples.md
  compatibility.md
  versioning.md
```

## Must Clarify

- 目标使用者
- Public API
- 类型和错误
- 兼容性策略
- 示例代码
- 版本策略

## Acceptance

SDK 项目的验收重点是 examples 能运行,API 清晰,错误可理解,README 完整.
