---
description: Start a new project-spec workflow and initialize docs skeleton.
argument-hint: <project idea>
allowed-tools: Read, Write, Edit
---

# /project-spec:new

## Purpose

启动一个新软件项目的规格生成流程.该命令不写代码,只完成项目类型识别,docs 骨架创建,初始问题收集.

## User Input

用户可以只提供一句项目想法,例如:

```text
我想做一个面向软件工程学生的 AI 面试题库系统.
```

## Required Skills

- `skills/project-classification/SKILL.md`
- `skills/scope-control/SKILL.md`
- 对应的 `skills/<project-type>/SKILL.md`

## Procedure

1. 读取用户的项目想法.
2. 判断项目形态,可以多选:
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
3. 如果项目形态不明确,最多问 5 个澄清问题.
4. 创建 docs 目录骨架.
5. 初始化 `docs/README.md`,`docs/meta/project-context.md`,`docs/review/open-questions.md`.
6. 更新 `docs/README.md` 当前状态为 `classified`.
7. 给出下一步建议:运行 `/project-spec:interview`.

## Output Requirements

输出:

```text
项目类型判断:...
建议文档包:...
需要继续确认的问题:...
下一步:/project-spec:interview
```

如果可以写入文件,则写入:

```text
docs/README.md
docs/meta/project-context.md
docs/review/open-questions.md
```

## Rules

- 不要写代码.
- 不要生成完整设计文档.
- 不要默认项目是后端项目.
- 如果项目明显过大,先标记风险,不要直接否定.
