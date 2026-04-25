---
name: cli-tool
description: Use when the project-spec is a command line tool with commands, config, input, output, and exit behavior.
---

# Project Type Skill: CLI Tool

## Type-specific Docs

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
