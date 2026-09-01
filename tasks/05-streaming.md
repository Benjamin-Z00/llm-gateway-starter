# 任务 05：流式输出

## 目标

理解聊天产品为什么需要 Streaming，以及后端如何转发流式结果。

完成这个任务后，你应该知道：Streaming 不是炫技，而是改善用户等待体验和长文本生成体验的关键能力。

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

## 可交付结果

写下你对流式响应的理解：

```text
流式响应让用户不必等完整结果生成完才看到反馈。
Gateway 负责把模型输出逐段转发给客户端，同时在结束后记录用量和成本。
```

## 思考题

如果用户中途取消请求，后端应该如何停止模型调用并记录状态？
