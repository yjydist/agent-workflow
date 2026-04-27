# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库用途

本仓库是名为 `agent-workflow` 的个人 Claude Code marketplace. 它不是应用运行时, 而是用来分发可复用的 Claude Code plugins, slash commands, agents, skills, workflow docs 和 templates. 当前主要分发 `software-design-workflow`, 一个把模糊软件方向推进为可交接设计包的通用软件设计 workflow.

仓库根目录是 marketplace root. 单个 plugin 放在 `plugins/<plugin-name>/`, 并在各自目录中包含 `.claude-plugin/plugin.json`.

## 常用命令

在仓库根目录验证整个 marketplace:

```bash
python3 validate_marketplace.py
```

验证当前 `software-design-workflow` plugin:

```bash
python3 plugins/software-design-workflow/validate_plugin.py
```

在 `plugins/software-design-workflow/` 目录内开发时, 也可以从该目录运行 plugin validator:

```bash
python3 validate_plugin.py
```

本仓库没有 package-manager build step. Python validators 是结构测试的事实来源.

## Marketplace 结构

- `.claude-plugin/marketplace.json` 定义 marketplace metadata, 并列出可分发 plugins.
- `plugins/` 保存 plugin 目录. Plugin 目录名使用 kebab-case, 且必须匹配 plugin manifest 的 `name`.
- `plugins/software-design-workflow/` 是当前 plugin. 它提供 `/sdw:*` commands, 用于把模糊软件方向推进为 reviewed design docs, frozen current target 和 handoff-ready execution package.

新增 plugin 时:

1. 创建 `plugins/<plugin-name>/`.
2. 添加 `plugins/<plugin-name>/.claude-plugin/plugin.json`.
3. 在 `.claude-plugin/marketplace.json` 中追加 plugin, 且 `source` 必须严格为 `./plugins/<plugin-name>`.
4. 如果 plugin 有自定义结构或 workflow 规则, 添加 plugin-local `validate_plugin.py`.

Marketplace root 不能包含 `.claude-plugin/plugin.json`. 该文件只属于 plugin 目录.

## `software-design-workflow` 架构

`plugins/software-design-workflow/` 是声明式 Claude Code plugin. 主要部分如下:

- `commands/*.md`: `/sdw:*` slash commands 和 workflow gates.
- `agents/*.md`: 面向 requirements, architecture, data design, review, implementation planning 等工作的 subagent role definitions.
- `skills/*/SKILL.md`: reusable skills, 包括通用 design skills 和 legacy project-type compatibility skills.
- `docs-template/`: 复制或生成到目标项目的通用 docs skeleton.
- `type-specific-templates/`: legacy compatibility templates, 保留用于迁移旧项目类型, 不是 primary modeling path.
- `workflow.md` 和 `USAGE.md`: workflow overview 和 plugin usage guidance.

Canonical workflow state sequence:

```text
intake -> classified -> discovered -> modeled -> designed -> qualified -> planned -> reviewed -> handoff-ready
```

重要 workflow 约束:

- 不要在 design workflow 中写 implementation code.
- 不要跳过 `/sdw:review` 直接 handoff.
- 不要跳过 `/sdw:freeze-target` 直接 plan.
- `/sdw:plan` 可以设置 `planned`, 但同一次 command 不得推进到 `handoff-ready`.
- `/sdw:handoff` 是 execution-layer handoff gate, 不是 coding command.
- current target freeze 后的需求变更必须走 `/sdw:change`.

## 必须保持的验证规则

Validators 会强制检查这些仓库约定, 修改时必须保持:

- Marketplace plugin entries 必须直接指向 `plugins/` 下的目录, source 形式为 `./plugins/<name>`.
- Plugin manifests 必须匹配目录名和 marketplace name.
- `/sdw:*` command files 必须有 YAML frontmatter, 且包含 `description`, `argument-hint`, `allowed-tools`.
- Plugin commands 和 agents 不得允许 unrestricted `Bash`.
- Agent frontmatter 必须包含 `name`, `description`, `tools`, `model`, `color`.
- 每个 skill directory 必须包含 `SKILL.md`, 且其中 `name` 匹配目录名.
- Legacy project-type compatibility assets 必须保持与 validator expectations 同步, 直到迁移层被显式移除.
- `software-design-workflow` 的 handoff, freeze-target, change, plan gate text 会被刻意验证. 修改这些 command docs 时, 要当作 workflow change, 不要当作 copy edit.
- 文本文件不得包含全角标点或本地绝对路径泄漏.

## Legacy compatibility project types

当前 plugin 保留这些 legacy project-type compatibility assets:

```text
backend-api
frontend-spa
fullstack-web
cli-tool
desktop-app
mobile-app
library-sdk
ai-agent
rag-app
data-pipeline
```

新增或重命名 legacy project-type compatibility asset 时, 必须同步更新对应 skill, type-specific template directory 和 validator expectations. Primary modeling path 应优先使用 adapters.
