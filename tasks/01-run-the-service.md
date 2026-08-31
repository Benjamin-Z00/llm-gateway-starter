# 任务 01：跑通服务和测试

## 目标

确认项目能在本地运行，并理解项目结构。

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

## 思考题

为什么这个项目先使用 Fake Provider，而不是一开始就接真实模型？
