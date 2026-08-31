# 任务 03：结构化输出校验

## 目标

让模型输出变成后端系统可以信任的数据。

## 背景

Agent 系统不能依赖自然语言解析。订单、工单、用户画像、工具参数都需要结构化输出，并且必须校验。

## 练习

调用 `POST /v1/structured`，要求模型抽取用户画像：

```json
{
  "messages": [
    { "role": "user", "content": "extract_profile" }
  ],
  "schema": {
    "type": "object",
    "required": ["name", "role", "goal"],
    "properties": {
      "name": { "type": "string" },
      "role": { "type": "string" },
      "goal": { "type": "string" }
    }
  }
}
```

## 验收标准

- 能返回合法 JSON
- 缺字段或类型不匹配时会失败
- 能解释 JSON Schema 在 Function Calling 里的作用
