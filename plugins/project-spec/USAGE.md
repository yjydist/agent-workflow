# Usage Guide

## 推荐方式: Claude Code plugin

### 1. 验证插件结构

在本仓库运行:

```bash
python3 validate_plugin.py
```

### 2. 本地开发临时加载

用绝对路径启动 Claude Code:

```bash
claude --plugin-dir /absolute/path/to/project-spec
```

进入 Claude Code 后运行:

```text
/reload-plugins
```

### 3. 持久安装

本插件由仓库根目录的 `agent-workflow` marketplace 分发. 在 Claude Code 中添加 marketplace 并安装插件:

```text
/plugin marketplace add /absolute/path/to/agent-workflow
/plugin install project-spec@agent-workflow
/reload-plugins
```

### 4. 验证命令可用

在目标项目中确认以下命令可用:

```text
/project:new
/project:interview
/project:generate-docs
/project:review-docs
/project:freeze-v1
/project:plan-implementation
/project:ready-for-coding
/project:change
/project:status
```

## 标准工作流

从目标项目运行:

```text
/project:new
/project:interview
/project:generate-docs
/project:review-docs
/project:freeze-v1
/project:plan-implementation
/project:ready-for-coding
```

状态流转:

```text
idea -> classified -> interviewed -> docs-generated -> docs-reviewed -> v1-frozen -> implementation-planned -> ready-for-coding
```

`/project:plan-implementation` 只负责生成实现计划并设置 `implementation-planned`. 用户审阅实现计划, 验收标准和必读文档后, 运行 `/project:ready-for-coding` 进入 `ready-for-coding`.

## 实现阶段提示

交给 coding agent 实现时, 使用这段约束:

```text
先阅读 docs/README.md 中的必读顺序.
只实现 docs/delivery/implementation-plan.md 的当前 Phase.
不要实现其他 Phase 或 V1 范围外功能.
如果发现文档冲突, TODO, 遗漏或实现不可判定, 停止并报告.
```

## 变更和状态

- 需求变更使用 `/project:change`.
- 查看状态使用 `/project:status`.
- 已冻结 V1 后, 默认把新增需求放入 V2, 除非用户明确替换或缩小其他 V1 内容.

## 手动备用方式

如果当前环境暂不支持 plugin 安装, 可以把 `docs-template/` 复制到目标项目的 `docs/`, 然后在对话中明确引用本仓库的 command, agent, skill 文件作为工作流依据. 这只是备用方式, 首选仍是 plugin.

## 推荐实践

- 每个项目先生成文档, 不要直接实现.
- 一次只实现一个 Phase.
- 所有变更都通过 `/project:change`.
- 项目越小, workflow 越有效.
