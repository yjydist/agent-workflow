# Implementation Plan

## Phase 1: Project Bootstrap

### Goal

初始化项目结构,配置加载,数据库连接,统一响应,健康检查.

### Forbidden Changes

- 不实现用户模块.
- 不实现课程或任务模块.

### Acceptance

- `go run ./cmd/server` 可以启动.
- `GET /health` 返回 ok.

## Phase 2: Auth

### Goal

实现注册,登录,JWT 中间件.

### Acceptance

- 注册成功.
- 重复邮箱返回 409.
- 登录成功返回 token.
- 无 token 访问受保护接口返回 401.

## Phase 3: Course

实现课程 CRUD.

## Phase 4: Task

实现任务 CRUD 和筛选.
