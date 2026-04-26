---
name: cli-tool
description: Legacy compatibility guidance for cli-tool. For new design work, prefer adapters for application, cli, and local-tool guidance.
---

# Compatibility Skill: CLI Tool

Legacy `cli-tool` maps to adapter set `tooling + cli + local-machine`. Prefer adapter docs for new guidance:

```text
adapters/kinds/tooling.md
adapters/surfaces/cli.md
adapters/runtimes/local-machine.md
```

## Legacy compatibility docs

Existing legacy reusable assets may still be read during migration from:

```text
docs/type-specific/cli-tool/
  commands.md
  flags.md
  config.md
  input-output.md
  exit-codes.md
```

## Must Clarify

- 命令列表
- 参数和 flag
- 配置文件路径和格式
- stdin/stdout/stderr 规则
- exit code
- 文件读写边界
- dry-run / confirm 行为

## Contract Example

```text
mytool add <name> --tag <tag> --json
```

必须定义:输入,输出,错误,exit code.
