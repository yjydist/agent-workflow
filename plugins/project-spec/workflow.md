# Workflow Overview

本 workflow 由 `project-spec` Claude Code plugin 提供, 负责把项目从模糊想法推进到可执行规格. 首选方式是在目标项目启用 plugin, 然后运行 `/project-spec:*` 命令.

## 状态机

```text
idea
  -> classified
  -> interviewed
  -> docs-generated
  -> docs-reviewed
  -> v1-frozen
  -> implementation-planned
  -> ready-for-coding
```

## 阶段说明

### 1. idea

用户只有一个粗略项目想法.

目标: 不要直接设计, 不要直接写代码, 先确认项目类型和目标.

### 2. classified

已经识别项目类型, 例如: backend-api, cli-tool, rag-app.

目标: 选择对应的 type-specific 文档模板和 skill.

### 3. interviewed

通过多轮访谈收集足够信息.

目标: 补齐项目目标, 用户, 场景, 范围, 实体, 接口, 数据, 质量要求, 验收方式.

### 4. docs-generated

已生成初版 docs.

目标: 文档完整, 但允许存在 TODO 和 open questions.

### 5. docs-reviewed

review agent 已审查文档一致性.

目标: 找出冲突, 过度设计, 遗漏, 不适合 V1 的内容.

### 6. v1-frozen

V1 范围已冻结.

目标: 明确 V1 必做, 不做, V2 候选. coding agent 后续不得随意加功能.

### 7. implementation-planned

已生成分 Phase 实现计划.

目标: 每个 Phase 有目标, 允许修改文件, 禁止事项, 验收命令.

### 8. ready-for-coding

可以交给 coding agent 分阶段实现.

目标: `/project-spec:ready-for-coding` 已确认 `docs/delivery/implementation-plan.md`, 验收标准, review blocking issues, blocking open questions 和 `docs/README.md` 必读顺序均已完整.

## 关键约束

- 不允许跳过 `/project-spec:review-docs` 直接冻结.
- 不允许跳过 `/project-spec:freeze-v1` 直接实现.
- `/project-spec:plan-implementation` 只设置并报告 `implementation-planned`, 可以报告 readiness 缺口, 但不得在同一次执行中更新为 `ready-for-coding`.
- `/project-spec:ready-for-coding` 是唯一负责从 `implementation-planned` 推进到 `ready-for-coding` 的命令.
- 所有 TODO 必须在实现前解决, 或者明确标记为 V2 不处理.
- 每次需求变更必须通过 `/project-spec:change` 写入 `docs/meta/change-log.md` 和 `docs/meta/decisions.md`.
