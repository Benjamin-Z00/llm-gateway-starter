# Day 1 自学指南

这份指南的目标是让你第一天就拿到一个可运行、可解释、可展示的小成果。

## 你今天要完成什么

今天不要急着接真实模型，也不要一开始就改复杂架构。先完成这 5 件事：

1. 在本地跑通测试。
2. 启动 FastAPI 服务。
3. 用 `/docs` 调通 `/v1/chat`。
4. 用 `/v1/structured` 看懂结构化输出。
5. 写下这个项目的 3 句作品集解释。

## 推荐时间安排

### 0-15 分钟：跑通环境

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

看到测试通过后，再启动服务：

```bash
uvicorn app.main:app --reload
```

打开：

```text
http://127.0.0.1:8000/docs
```

### 15-35 分钟：理解统一聊天入口

在 `/docs` 调用 `POST /v1/chat`：

```json
{
  "messages": [
    { "role": "user", "content": "解释 LLM Gateway 的作用" }
  ],
  "model": "fake-fast",
  "temperature": 0.2,
  "max_tokens": 512
}
```

你要观察返回里的这些字段：

- `content`
- `input_tokens`
- `output_tokens`
- `latency_ms`
- `cost_cny`

重点不是回复内容，而是 Gateway 把模型调用、统计和协议统一起来了。

### 35-60 分钟：理解结构化输出

调用 `POST /v1/structured`：

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

你要能解释：

- 为什么 Agent 工具调用不能只靠自然语言。
- 为什么需要 JSON Schema。
- 输出不合法时为什么要失败，而不是让下游系统继续处理。

### 60-90 分钟：整理作品集表达

用自己的话写下：

```text
我做了一个 LLM Gateway，用来统一管理业务系统对大模型的调用。
它集中处理结构化输出、重试、流式响应、Token 统计和成本记录。
这个模块可以作为 Agent、RAG、多模型路由等系统的底层入口。
```

然后复制 `portfolio/PROJECT_README_TEMPLATE.md`，开始补充你的项目说明。

## 今天不要做什么

- 不要一开始就接真实模型。
- 不要先加数据库。
- 不要先做前端页面。
- 不要把代码重构成复杂框架。

先跑通、理解、能讲清楚，再继续扩展。

