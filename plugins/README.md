# Plugins

该目录保存 `agent-workflow` 个人 marketplace 中的所有 Claude Code plugins.

## 当前插件

| Plugin | Description |
| --- | --- |
| `software-design-workflow` | Adapter-first software design workflow, 提供 `/sdw:*` commands, agents, skills 和 docs templates. |

## 命名约定

- 插件目录使用 kebab-case.
- 插件目录名必须和 `.claude-plugin/plugin.json` 的 `name` 一致.
- 每个插件尽量自带 `README.md` 和 `validate_plugin.py`.
- 新增插件后, 必须更新根目录 `.claude-plugin/marketplace.json`.
