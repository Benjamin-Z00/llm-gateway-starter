# 任务 02：理解统一聊天入口

## 目标

理解 LLM Gateway 为什么要提供统一入口，而不是业务代码直接调用不同模型 SDK。

## 你要阅读

- `app/main.py`
- `app/models.py`
- `app/services/gateway.py`
- `app/providers/fake.py`

## 练习

调用 `POST /v1/chat`：

```json
{
  "messages": [
    { "role": "system", "content": "你是一个简洁的技术助手" },
    { "role": "user", "content": "解释什么是 LLM Gateway" }
  ],
  "model": "fake-fast",
  "temperature": 0.2,
  "max_tokens": 512
}
```

## 验收标准

- 能说清楚 `ChatRequest` 和 `ChatResponse` 的字段含义
- 能解释 Gateway 统一记录 Token、延迟和成本的好处
- 能新增一个测试，验证空 `messages` 会被拒绝
