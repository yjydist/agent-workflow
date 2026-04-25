# Functional Requirements

## Auth

### Register

- 用户可以使用邮箱和密码注册.
- 邮箱必须唯一.
- 密码长度至少 8 位.
- 注册成功返回用户 ID 和邮箱.
- 重复邮箱返回 409.

### Login

- 用户使用邮箱和密码登录.
- 登录成功返回 JWT token.
- 密码错误返回 401.

## Course

### Create Course

- 登录用户可以创建课程.
- 课程名必填,长度 1-100.
- 课程归属于当前用户.

## Task

### Create Task

- 登录用户可以在自己的课程下创建任务.
- title 必填,长度 1-100.
- due_time 可为空;如果存在,不能早于当前时间.
- 默认状态为 pending.
