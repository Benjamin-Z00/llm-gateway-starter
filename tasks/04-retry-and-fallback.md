# 任务 04：失败重试和降级

## 目标

理解 LLM 输出不稳定时，后端需要如何兜底。

## 练习

调用 `POST /v1/structured`，输入：

```json
{
  "messages": [
    { "role": "user", "content": "return_invalid_json" }
  ],
  "schema": { "type": "object" },
  "max_retries": 1
}
```

## 验收标准

- 接口返回 `422`
- 错误信息包含重试失败原因
- 能解释为什么生产系统不能把模型原始输出直接交给下游服务

## 进阶

把 `FakeModelProvider` 改成第一次返回非法 JSON，第二次返回合法 JSON，并验证 `retries` 等于 `1`。
