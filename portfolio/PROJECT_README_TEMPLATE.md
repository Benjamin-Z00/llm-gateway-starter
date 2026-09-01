# LLM Gateway 项目作品集说明

> 建议复制这个文件，改成你自己的项目 README。不要只保留模板文字，要补充你的运行结果、接口截图或测试输出。

## 项目背景

这个项目实现了一个 LLM Gateway，用于统一管理业务系统对大模型的调用。

业务系统直接调用模型 SDK 会带来这些问题：

- 模型供应商切换困难
- Token、延迟和成本难统计
- 结构化输出缺少统一校验
- 错误重试和降级逻辑散落在各业务模块
- 后续接入 Agent Tool Runtime 时缺少统一入口

## 核心功能

- 统一聊天接口：`POST /v1/chat`
- 结构化输出接口：`POST /v1/structured`
- 流式输出接口：`POST /v1/chat/stream`
- 使用统计接口：`GET /v1/usage`
- 健康检查：`GET /health`

## 技术栈

- Python 3.11+
- FastAPI
- Pydantic v2
- JSON Schema
- pytest

## 架构说明

```text
Client
  -> FastAPI Router
  -> LLMGateway Service
  -> Model Provider
  -> Usage Store
```

## 我完成的关键设计

1. 用 `ChatRequest` 和 `ChatResponse` 统一模型调用协议。
2. 用 JSON Schema 校验结构化输出，避免自然语言解析。
3. 在 Gateway 层集中处理重试、延迟和成本统计。
4. 用 Fake Provider 保证本地测试稳定可复现。

## 测试结果

```text
在这里贴 pytest 输出或截图说明
```

## 本地运行方式

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
pytest
uvicorn app.main:app --reload
```

接口文档：

```text
http://127.0.0.1:8000/docs
```

## 可展示接口

```bash
curl -X POST http://127.0.0.1:8000/v1/chat \
  -H "Content-Type: application/json" \
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}]}"
```

## 面试讲法

这个项目不是一个普通聊天 Demo，而是一个 Agent 系统的底层基础设施。它把模型调用从业务代码里抽离出来，统一处理结构化输出、重试、成本、延迟和流式响应。后续 Tool Runtime、RAG、Agent Loop 都可以复用这个 Gateway。

## 我遇到的问题和处理方式

可以补充：

- 环境问题：
- 接口调试问题：
- 结构化输出校验问题：
- 测试补充：
- 我如何定位和解决：

## 后续扩展

- 接入真实模型 API
- 增加多模型路由
- 增加 Prompt 模板管理
- 增加 Redis / Postgres 持久化
- 增加 Trace 和 Replay
