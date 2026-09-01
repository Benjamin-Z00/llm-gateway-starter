# 常见问题

## `python` 命令找不到

先确认本机已经安装 Python 3.11 或更高版本。

Windows 可以尝试：

```bash
py -3.11 --version
```

如果 `python` 不可用，但 `py` 可用，可以把命令替换成：

```bash
py -3.11 -m venv .venv
```

## Windows 无法激活虚拟环境

PowerShell 可能会拦截脚本执行。可以尝试：

```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

然后重新执行：

```bash
.venv\Scripts\activate
```

## `pip install -e ".[dev]"` 失败

先升级基础安装工具：

```bash
python -m pip install --upgrade pip setuptools wheel
```

然后重新安装：

```bash
pip install -e ".[dev]"
```

## `pytest` 找不到

说明开发依赖没有装好。重新执行：

```bash
pip install -e ".[dev]"
```

再运行：

```bash
pytest
```

## 端口 8000 被占用

换一个端口启动：

```bash
uvicorn app.main:app --reload --port 8001
```

然后打开：

```text
http://127.0.0.1:8001/docs
```

## `/v1/structured` 返回 422

这通常不是环境问题，而是结构化输出没有通过校验。

你可以检查：

- 请求体里的 `schema` 是否是合法 JSON Schema。
- `required` 字段是否真的出现在模型返回结果里。
- 字段类型是否匹配，例如要求 `string` 却返回了数字。
- 是否故意输入了 `return_invalid_json` 触发失败场景。

## `/v1/usage` 没有变化

先调用一次 `/v1/chat` 或 `/v1/structured`，再查看 `/v1/usage`。

注意：项目当前使用内存统计，服务重启后统计会清空。这是 starter 项目的设计选择，后续可以扩展为 Redis 或 Postgres。

## 为什么不用真实模型 API

这个免费包优先训练后端工程闭环：

- 统一协议
- 结构化输出
- 重试与失败处理
- 流式响应
- 成本统计
- 测试覆盖

真实模型 Provider 是下一步扩展，不是第一天的必要条件。

