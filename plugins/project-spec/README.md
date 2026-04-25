# Project Spec Plugin

这是一个声明式 Claude Code plugin, 用于把模糊项目想法逐步整理成 coding agent 可以稳定执行的工程规格. 它不直接生成业务代码, 而是通过命令, agents, skills 和模板先产出可审查, 可冻结, 可分阶段实现的 docs.

适用项目类型包括:

- backend-api
- frontend-spa
- fullstack-web
- cli-tool
- desktop-app
- mobile-app
- library-sdk
- ai-agent
- rag-app
- data-pipeline

## 核心原则

1. 先分类, 再生成文档. 不要默认项目是后端, 前端或 AI 项目.
2. 文档是代码实现前的输入规格. 没有文档, 不写代码. 文档冲突, 不写代码. 范围未冻结, 不写代码.
3. 通用文档 + 类型专属文档. 所有项目都生成通用 docs, 根据项目类型追加 type-specific 文档.
4. 不确定内容标记 TODO. 不让 agent 擅自补关键业务决策.
5. V1 要冻结范围. 第一版只做最小闭环, 不中途乱加功能.
6. 每个 Phase 必须可测试. implementation-plan 是可执行任务序列.

## Claude Code plugin 使用方式

### 本地开发临时加载

在本仓库先验证结构:

```bash
python3 validate_plugin.py
```

然后用绝对路径启动 Claude Code:

```bash
claude --plugin-dir /absolute/path/to/project-spec
```

进入 Claude Code 后运行:

```text
/reload-plugins
```

### 持久安装

本插件由仓库根目录的 `agent-workflow` marketplace 分发. 在 Claude Code 中添加 marketplace 并安装插件:

```text
/plugin marketplace add /absolute/path/to/agent-workflow
/plugin install project-spec@agent-workflow
/reload-plugins
```

安装后在目标项目运行命令:

```text
/project:new
/project:interview
/project:generate-docs
/project:review-docs
/project:freeze-v1
/project:plan-implementation
/project:ready-for-coding
```

后续需求变更使用:

```text
/project:change
```

查看当前状态使用:

```text
/project:status
```

## Plugin 结构

```text
project-spec/
  .claude-plugin/plugin.json
  commands/              # Claude Code slash commands
  agents/                # 子 agent 角色说明
  skills/                # Claude Code skill 目录, 每个 skill 使用 SKILL.md
  docs-template/         # 复制或生成到目标项目 docs/ 的通用模板
  type-specific-templates/ # 项目类型专属模板
  examples/              # 示例项目文档
```

## 目标项目 docs 结构

```text
docs/
  README.md
  meta/
  product/
  requirements/
  design/
  type-specific/
  delivery/
  review/
```

## 工作流状态

```text
idea -> classified -> interviewed -> docs-generated -> docs-reviewed -> v1-frozen -> implementation-planned -> ready-for-coding
```

## 给 coding agent 的总规则

```text
实现代码前, 必须先阅读 docs/README.md 指定的必读文档.
只能实现 docs/product/scope.md 中 V1 明确包含的功能.
如果发现文档冲突, TODO, 遗漏或实现不可判定, 必须先停止并报告, 不得自行猜测.
每次只实现 docs/delivery/implementation-plan.md 中一个 Phase.
每个 Phase 完成后必须运行或给出可执行的验收命令.
```

## 手动备用方式

如果当前环境暂不支持 plugin 安装, 可以把 `docs-template/` 复制到目标项目的 `docs/`, 然后在对话中明确引用本仓库的 command, agent, skill 文件作为工作流依据. 推荐路径仍然是启用 plugin.
