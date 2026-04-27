---
name: project-classification
description: Use when classifying a new software idea into adapter kinds, surfaces, runtimes, domains, and concerns.
---

# Skill: Project Classification

## Goal

根据用户想法选择 adapter set,并保留必要的 legacy project type compatibility label.

## Adapter Layers

- Kind: `application`, `service`, `library-sdk`, `tooling`, `knowledge-system`, `agent-system`, `platform-infra`, `data-ml-system`, `language-compiler`, `embedded-system`, `interactive-media`.
- Surface: `web-ui`, `desktop-ui`, `mobile-ui`, `cli`, `tui`, `http-api`, `library-api`, `agent-tools`, `file-format`, `event-stream`, `ipc`, `background-jobs`.
- Runtime: `browser`, `server`, `local-machine`, `mobile-device`, `embedded-device`, `cloud-platform`, `offline-first`, `edge-runtime`.
- Domain: `knowledge-management`, `education-learning`, `developer-tools`.
- Concern: `security-privacy`, `offline-sync`, `observability`, `compatibility`, `performance`, `ai-safety`.

## Legacy Compatibility Mapping

- `backend-api` -> `service + http-api + server`.
- `frontend-spa` -> `application + web-ui + browser`.
- `cli-tool` -> `tooling + cli + local-machine`.
- `ai-agent` -> `agent-system + agent-tools + ai-safety`.

## Classification Questions

1. 用户使用入口是什么?浏览器,命令行,桌面,手机,代码调用,HTTP API,agent tool,文件,事件?
2. 软件本质是什么?application,service,library-sdk,tooling,knowledge-system,agent-system,platform-infra,data-ml-system?
3. 代码运行在哪里?browser,server,local-machine,mobile-device,embedded-device,cloud-platform,edge-runtime,offline-first?
4. 是否需要持久化数据,同步,后台任务,事件流,或外部系统集成?
5. 是否调用 LLM,embedding,agent tools,或需要 ai-safety?
6. 是否有 domain adapter 或 concern adapter 必须影响当前 target?

## Output Template

```md
## Adapter Set

Kind: ...
Surfaces: ...
Runtimes: ...
Domains: ...
Concerns: ...

## Legacy Compatibility Label

Primary: ...
Secondary: ...

## Reasoning

## Required Adapter Docs

## Type-specific Assets To Reuse

## Recommended Skills

## Open Questions
```
