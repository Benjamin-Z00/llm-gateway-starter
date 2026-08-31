# 任务 06：Token、延迟和成本

## 目标

建立 LLM 应用的成本意识。

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

## 进阶

把成本估算策略改成按模型区分，例如：

- `fake-fast`：输入 0.001 CNY / 1K tokens，输出 0.002 CNY / 1K tokens
- `fake-smart`：输入 0.004 CNY / 1K tokens，输出 0.012 CNY / 1K tokens
