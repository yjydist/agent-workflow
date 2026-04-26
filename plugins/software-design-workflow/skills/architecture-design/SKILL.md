---
name: architecture-design
description: Use when designing system components, boundaries, deployment shape, and technical tradeoffs.
---

# Skill: Architecture Design

## Goal

为项目选择足够简单,可实现,可维护的架构.

## Output Template

```md
# Architecture

## Active Adapter Set

Kind: ...
Surfaces: ...
Runtimes: ...
Domains: ...
Concerns: ...

## System Context

## Modules

## Dependency Direction

## Runtime Flow

## Surface Boundaries

## Runtime Constraints

## Technology Choices

## Explicit Non-goals

## Risks
```

## Adapter Rules

- Kind adapters decide main boundaries: `application`, `service`, `library-sdk`, `tooling`, `agent-system`, and other kinds should not share the same default architecture.
- Surface adapters decide external contracts: `http-api`, `cli`, `web-ui`, `library-api`, `agent-tools`, and event/file surfaces each need explicit contract boundaries.
- Runtime adapters decide deployment and constraints: `browser`, `server`, `local-machine`, `cloud-platform`, `offline-first`, and other runtimes must be reflected in runtime flow.

## Rules

- 优先单体,模块化,清晰分层.
- 不为了简历亮点强行引入复杂架构.
- 架构必须能映射到 current target 和 implementation-plan.
