# Agent Workflow Marketplace

这是我的个人 Claude Code marketplace, 用来集中存放可复用的 commands, agents, skills 和 workflow plugins.

## Marketplace 结构

```text
agent-workflow/
  .claude-plugin/marketplace.json
  plugins/
    software-design-workflow/
      .claude-plugin/plugin.json
      commands/
      agents/
      skills/
```

## 当前插件

| Plugin | Purpose | Commands |
| --- | --- | --- |
| `software-design-workflow` | 把模糊方向整理成 handoff-ready software design package | `/sdw:*` |

## 安装 marketplace

在 Claude Code 中添加本地 marketplace:

```text
/plugin marketplace add /absolute/path/to/agent-workflow
/plugin install software-design-workflow@agent-workflow
/reload-plugins
```

安装后在目标项目运行:

```text
/sdw:start "your vague software idea"
/sdw:classify
/sdw:discover
/sdw:model
/sdw:design
/sdw:quality
/sdw:target "current target slice"
/sdw:freeze-target
/sdw:plan
/sdw:review
/sdw:handoff
```

## 验证

验证整个 marketplace:

```bash
python3 validate_marketplace.py
```

验证单个插件:

```bash
python3 plugins/software-design-workflow/validate_plugin.py
```

## 新增插件约定

1. 在 `plugins/<plugin-name>/` 下创建插件.
2. 插件必须包含 `.claude-plugin/plugin.json`.
3. 插件资源放在 `commands/`, `agents/`, `skills/` 等标准目录.
4. 在 `.claude-plugin/marketplace.json` 的 `plugins` 数组追加条目.
5. 如果插件有自定义规则, 提供 `validate_plugin.py`.
