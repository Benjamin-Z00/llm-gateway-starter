# 任务 05：流式输出

## 目标

理解聊天产品为什么需要 Streaming，以及后端如何转发流式结果。

## 练习

调用：

```text
POST /v1/chat/stream
```

请求体：

```json
{
  "messages": [
    { "role": "user", "content": "streaming makes product feel faster" }
  ]
}
```

## 验收标准

- 响应类型是 `text/event-stream`
- 可以看到多个 `data:` 片段
- 流结束后 `/v1/usage` 的调用统计增加

## 思考题

如果用户中途取消请求，后端应该如何停止模型调用并记录状态？
