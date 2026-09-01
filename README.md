# LLM Gateway Starter

这是 CodeRun Agent Lab 的第一个免费自学项目包，也是你进入 AI Agent 工程方向的第一个可展示作品。

目标不是调用一个真实模型做聊天演示，而是完成一个面向生产系统的 LLM Gateway 雏形：统一入口、结构化输出、错误重试、流式响应、成本记录和测试覆盖。

你不需要老师带着讲，也不需要先准备真实模型 API Key。这个项目包的设计目标是：让你在本地先跑通一个稳定、可测试、可解释的 LLM 应用后端骨架。

## 适合谁

- 会一点 Python，想进入 AI Agent / LLM 应用开发方向
- 有后端、脚本、运维或测试开发基础
- 想用项目方式自学，而不是只看视频
- 想把“会调模型 API”升级成“能交付 AI 工程模块”

## 不适合谁

- 完全没有 Python、HTTP API 或命令行基础
- 只想看概念，不打算动手运行和修改代码
- 期望这个免费包直接包含完整商业级 Agent 平台

## 你会做出什么

完成后你会得到一个 FastAPI 服务：

- `POST /v1/chat`：统一聊天调用入口
- `POST /v1/structured`：按 JSON Schema 返回结构化结果
- `POST /v1/chat/stream`：流式输出
- `GET /v1/usage`：查看调用次数、Token 和成本
- `GET /health`：健康检查

第一版默认使用本地 Fake Provider，不需要真实 API Key。你可以先把后端工程闭环跑通，再接 OpenAI、DeepSeek、Qwen 或其他模型。

## 建议学习方式

如果你只有 60-90 分钟，先完成：

1. 跑通测试和服务
2. 打开 `/docs` 调用 `/v1/chat`
3. 调用 `/v1/structured` 看结构化输出
4. 查看 `/v1/usage` 理解调用统计
5. 写下你对 Gateway 价值的 3 句话

如果你有半天时间，按 `tasks/` 顺序完成 7 个任务，并填写作品集模板。

详细路线看：

- `docs/DAY1_GUIDE.md`：第一天怎么学
- `docs/SELF_CHECK.md`：完成后怎么自查
- `docs/TROUBLESHOOTING.md`：常见卡点
- `portfolio/PROJECT_README_TEMPLATE.md`：作品集说明模板

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

如果你使用 macOS / Linux，激活虚拟环境用：

```bash
source .venv/bin/activate
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

每个任务都建议留下一个“可证明结果”：接口返回、测试输出、代码改动或一段项目解释。这些材料会直接用于你的作品集。

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

## 你应该获得的能力

完成这个项目后，你不只是“跑了一个 Demo”，而是应该能回答这些问题：

- 一个企业 AI 应用为什么需要统一模型入口？
- 为什么 Agent 不能只依赖自然语言输出？
- 模型失败、超时、输出不合法时，后端应该怎么兜底？
- Token、延迟和成本为什么必须从第一天就记录？
- 如果未来要接 Tool Runtime、RAG 或多模型路由，这个 Gateway 应该放在哪一层？
