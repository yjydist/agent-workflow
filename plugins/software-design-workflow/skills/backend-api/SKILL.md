---
name: backend-api
description: Legacy compatibility guidance for backend-api. For new design work, prefer adapters for service, http-api, and server guidance.
---

# Compatibility Skill: Backend API

Legacy `backend-api` maps to adapter set `service + http-api + server`. Prefer adapter docs for new guidance:

```text
adapters/kinds/service.md
adapters/surfaces/http-api.md
adapters/runtimes/server.md
```

## Legacy compatibility docs

Existing legacy reusable assets may still be read during migration from:

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
