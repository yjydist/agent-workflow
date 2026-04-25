---
name: backend-api
description: Use when the project-spec exposes backend APIs, auth, persistence, deployment, or service contracts.
---

# Project Type Skill: Backend API

## Type-specific Docs

```text
docs/type-specific/backend-api/
  api.md
  database.md
  auth.md
  deployment.md
```

## Must Clarify

- API style: REST / RPC / GraphQL
- Auth: JWT / session / none
- Database: SQL / NoSQL / file
- Error response format
- Pagination and filtering
- Resource ownership rules

## Suggested Architecture

```text
router -> handler/controller -> service -> repository -> database
```

## Anti-overdesign

默认不使用微服务,消息队列,分布式事务,Kubernetes.
