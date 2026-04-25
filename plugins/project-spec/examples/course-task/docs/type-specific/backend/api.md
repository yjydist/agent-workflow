# Backend API

## Response Format

```json
{
  "code": 0,
  "message": "ok",
  "data": {}
}
```

## Auth

### POST /api/v1/auth/register

Request:

```json
{
  "email": "test@example.com",
  "password": "12345678"
}
```

Response:

```json
{
  "id": 1,
  "email": "test@example.com"
}
```

### POST /api/v1/auth/login

Response:

```json
{
  "token": "jwt-token"
}
```

## Tasks

### POST /api/v1/tasks

Requires: `Authorization: Bearer <token>`

Request:

```json
{
  "course_id": 1,
  "title": "完成数据库作业",
  "description": "第 3 章习题",
  "due_time": "2026-05-01T23:59:59+08:00"
}
```
