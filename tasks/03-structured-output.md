# 任务 03：结构化输出校验

## 目标

让模型输出变成后端系统可以信任的数据。

完成这个任务后，你要能理解：Agent 系统里很多“模型回答”最终都会变成工具参数、数据库字段或业务动作，因此必须校验。

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

## 可交付结果

写下你对结构化输出的理解：

```text
自然语言适合展示给人看，结构化输出适合交给系统处理。
Agent 要调用工具、创建工单、写入数据库或触发工作流时，必须先把模型输出变成可校验的数据结构。
```
