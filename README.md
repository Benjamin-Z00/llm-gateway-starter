# LLM Gateway Starter

这是 CodeRun Agent Lab 的第一个免费自学项目包。

目标不是调用一个真实模型做聊天演示，而是完成一个面向生产系统的 LLM Gateway 雏形：统一入口、结构化输出、错误重试、流式响应、成本记录和测试覆盖。

## 适合谁

- 会一点 Python，想进入 AI Agent / LLM 应用开发方向
- 有后端、脚本、运维或测试开发基础
- 想用项目方式自学，而不是只看视频

## 你会做出什么

完成后你会得到一个 FastAPI 服务：

- `POST /v1/chat`：统一聊天调用入口
- `POST /v1/structured`：按 JSON Schema 返回结构化结果
- `POST /v1/chat/stream`：流式输出
- `GET /v1/usage`：查看调用次数、Token 和成本
- `GET /health`：健康检查

第一版默认使用本地 Fake Provider，不需要真实 API Key。你可以先把后端工程闭环跑通，再接 OpenAI、DeepSeek、Qwen 或其他模型。

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
pytest
uvicorn app.main:app --reload
```

打开接口文档：

```text
http://127.0.0.1:8000/docs
```

## 学习任务

按顺序完成 `tasks/` 里的任务：

1. `01-run-the-service.md`：跑通服务和测试
2. `02-chat-endpoint.md`：理解统一聊天入口
3. `03-structured-output.md`：完成结构化输出校验
4. `04-retry-and-fallback.md`：实现失败重试和降级
5. `05-streaming.md`：实现流式输出
6. `06-usage-cost.md`：记录 Token、延迟和成本
7. `07-portfolio-pack.md`：整理作品集说明

## 完成标准

- 所有测试通过
- 能用 `/docs` 手动调用 4 个核心接口
- 能解释为什么 Gateway 要独立存在
- 能说清楚结构化输出、重试、成本记录对 Agent 系统的价值
- 完成 `portfolio/PROJECT_README_TEMPLATE.md`

## 后续扩展

完成免费项目后，可以继续扩展：

- 接入真实模型 Provider
- 增加 Prompt 模板管理
- 增加多模型路由策略
- 增加 Redis / Postgres 持久化
- 增加 Agent Tool Runtime
