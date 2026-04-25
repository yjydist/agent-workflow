# Acceptance Criteria

## Project-level Acceptance

- 服务可以本地启动.
- 所有 V1 API 都有 curl 示例.
- 用户不能访问其他用户的数据.
- 所有参数错误都有明确响应.

## Health Check

```bash
curl http://localhost:8080/health
```

Expected:

```json
{"code":0,"message":"ok","data":{"status":"ok"}}
```
