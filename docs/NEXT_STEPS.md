# 完成免费包后的下一步

当你完成 LLM Gateway Starter 后，可以按这个顺序继续升级。

## 第 1 步：接入真实模型

新增一个真实 Provider，例如：

- OpenAI
- DeepSeek
- Qwen
- Claude

不要改业务路由，只替换 Provider 实现。这样可以验证 Gateway 抽象是否成立。

你要完成：

- API Key 从环境变量读取。
- 超时控制。
- 错误码转换。
- 真实 Token 用量统计。

## 第 2 步：增加多模型路由

让 Gateway 根据任务类型选择模型：

- 简单问答走低成本模型。
- 复杂推理走高质量模型。
- 结构化抽取优先选择稳定输出模型。
- 失败时自动降级到备用模型。

你要完成：

- 模型配置表。
- 路由策略函数。
- fallback 规则。
- 成本对比记录。

## 第 3 步：增加 Prompt 模板管理

不要把 Prompt 散落在业务代码里。可以新增：

- 模板名称
- 模板版本
- 输入变量
- 输出 Schema
- 示例用例

你要完成：

- Prompt 模板加载。
- 变量渲染。
- 版本记录。
- 测试用例。

## 第 4 步：接入 Agent Tool Runtime

Gateway 负责模型调用，Tool Runtime 负责执行工具。

一个基础 Agent 链路可以是：

```text
User Request
  -> Gateway
  -> Structured Tool Call
  -> Tool Runtime
  -> Tool Result
  -> Gateway
  -> Final Answer
```

你要完成：

- 工具注册。
- 工具参数 Schema。
- 工具执行结果。
- 工具失败处理。
- 执行日志。

## 第 5 步：做成可展示项目

最后整理为一个完整作品：

- 项目背景
- 架构图
- 接口文档
- 测试结果
- 成本统计截图
- Agent 执行链路截图
- 下一步商业化场景

这时它就不再是一个练习项目，而是一个可以用于求职、转型、面试和客户沟通的 AI 工程作品。
