# 任务 01：跑通服务和测试

## 目标

确认项目能在本地运行，并理解项目结构。

完成这个任务后，你应该得到一个明确结果：测试通过、服务启动、接口文档可以打开。

## 操作

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
pytest
uvicorn app.main:app --reload
```

## 验收标准

- `pytest` 全部通过
- 浏览器打开 `http://127.0.0.1:8000/docs`
- 能调用 `GET /health` 并得到 `{"status":"ok"}`

## 记录你的结果

把下面内容补充完整：

```text
Python 版本：
测试结果：
服务地址：
我看到的接口数量：
```

## 思考题

为什么这个项目先使用 Fake Provider，而不是一开始就接真实模型？

参考回答方向：

- 本地测试更稳定，不依赖外部 API。
- 自学第一步先理解 Gateway 结构，而不是被 API Key、额度和网络问题卡住。
- Fake Provider 可以稳定模拟成功、失败、结构化输出和流式响应。
