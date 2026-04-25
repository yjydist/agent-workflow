# Agent Workflow Marketplace

这是我的个人 Claude Code marketplace, 用来集中存放可复用的 commands, agents, skills 和 workflow plugins.

## Marketplace 结构

```text
agent-workflow/
  .claude-plugin/marketplace.json
  plugins/
    project-spec/
      .claude-plugin/plugin.json
      commands/
      agents/
      skills/
```

## 当前插件

| Plugin | Purpose | Commands |
| --- | --- | --- |
| `project-spec` | 把模糊项目想法整理成 reviewed docs 和 implementation plan | `/project:*` |

## 安装 marketplace

在 Claude Code 中添加本地 marketplace:

```text
/plugin marketplace add /absolute/path/to/agent-workflow
/plugin install project-spec@agent-workflow
/reload-plugins
```

安装后在目标项目运行:

```text
/project:new
/project:interview
/project:generate-docs
/project:review-docs
/project:freeze-v1
/project:plan-implementation
/project:ready-for-coding
```

## 验证

验证整个 marketplace:

```bash
python3 validate_marketplace.py
```

验证单个插件:

```bash
python3 plugins/project-spec/validate_plugin.py
```

## 新增插件约定

1. 在 `plugins/<plugin-name>/` 下创建插件.
2. 插件必须包含 `.claude-plugin/plugin.json`.
3. 插件资源放在 `commands/`, `agents/`, `skills/` 等标准目录.
4. 在 `.claude-plugin/marketplace.json` 的 `plugins` 数组追加条目.
5. 如果插件有自定义规则, 提供 `validate_plugin.py`.
