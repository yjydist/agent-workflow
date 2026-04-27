> Legacy compatibility asset. For new design work, prefer adapters first, see `adapters/`.

# AI Agent Safety Boundaries

## Tool Policy

- 默认禁止任意 shell 和未列明的系统命令.
- 删除文件, 批量改写, 迁移数据, 修改权限等破坏性操作必须用户确认.
- 外部写操作必须用户确认, 包括发送消息, 创建 issue, 修改远端资源, 写入第三方系统.
- Agent 不得自行扩大工具权限, 不得绕过用户确认, 不得静默降级安全检查.

## Filesystem Boundaries

- Allowed paths: TODO
- Read-only paths: TODO
- Writeable paths: TODO
- Denied paths: TODO

## Secrets And Credentials

- secrets, credentials, tokens, cookies, private keys 不得写入日志, docs, prompts 或示例输出.
- 如果任务需要 secret, 只引用 secret 名称或环境变量名, 不记录具体值.
- 如果发现 secret 泄露, 停止并报告用户.

## Confirmation Required

| Action | Confirmation Required | Notes |
| --- | --- | --- |
| Run shell command | yes | 默认禁止任意 shell |
| Delete file or directory | yes | 包括批量删除 |
| Write external service | yes | 包括 GitHub, Slack, email, SaaS API |
| Modify local workflow docs | no | 仅限 workflow 允许的 docs |
| Modify source code | yes | 仅在 execution layer receives handoff-ready package 后 |

## Failure Handling

- 工具失败时不得用破坏性操作绕过问题.
- 权限不足时停止并请求用户确认或提供替代路径.
- 不确定行为是否安全时默认停止.
