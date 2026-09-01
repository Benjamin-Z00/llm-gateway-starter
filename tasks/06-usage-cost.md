# 任务 06：Token、延迟和成本

## 目标

建立 LLM 应用的成本意识。

完成这个任务后，你应该能理解：AI 应用的成本不是上线后才看的指标，而是设计阶段就要进入后端链路。

## 你要阅读

- `app/services/tokenizer.py`
- `app/services/usage.py`
- `app/services/gateway.py`

## 练习

连续调用 `/v1/chat` 三次，然后查看：

```text
GET /v1/usage
```

## 验收标准

- `request_count` 增加
- `input_tokens` 和 `output_tokens` 增加
- `total_cost_cny` 有记录

## 可交付结果

在作品集里写清楚：

```text
我在 Gateway 层统一记录请求次数、输入 Token、输出 Token 和估算成本。
这样团队可以按模型、接口或业务场景分析 AI 调用成本，并为后续限流、套餐和报价提供依据。
```

## 进阶

把成本估算策略改成按模型区分，例如：

- `fake-fast`：输入 0.001 CNY / 1K tokens，输出 0.002 CNY / 1K tokens
- `fake-smart`：输入 0.004 CNY / 1K tokens，输出 0.012 CNY / 1K tokens
