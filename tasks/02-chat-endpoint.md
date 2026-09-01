# 任务 02：理解统一聊天入口

## 目标

理解 LLM Gateway 为什么要提供统一入口，而不是业务代码直接调用不同模型 SDK。

完成这个任务后，你应该能解释：`/v1/chat` 不只是聊天接口，它是业务系统访问模型能力的统一入口。

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

## 可交付结果

在你的作品集里保留一段说明：

```text
我把模型调用封装在 Gateway 层，业务接口不直接依赖具体模型 SDK。
这样后续切换模型、统计成本、做失败重试和接入 Agent Tool Runtime 时，不需要在每个业务模块里重复改造。
```
