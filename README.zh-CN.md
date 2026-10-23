# App Module Delivery

[English](README.md) · [中文](README.zh-CN.md) · **v1.1.0**

规划应用、登记验收命令，并将真实结果与需求对应保存。技能现在包含可用于 Codex、Cursor 的 Python CLI/MCP 适配器。

![应用交付流程示意](docs/images/workflow-v1.1.0.svg)

适配器只执行工作区所有者预先登记的精确命令，保存真实退出码、日志和产物哈希。产物变化会使之前的通过结果失效。宿主连接关闭后，原检查仍可完成；重连读取同一份收条，不会自动重复运行。

下载 [v1.1.0 ZIP](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.1.0)，使用 Python 3.11+，按[中文宿主教程](docs/tutorial.zh-CN.md)安装。仓库中的可安装技能位于 `skills/app-module-delivery`，技能 ZIP 中直接位于根目录。

适配器不提供模型、GUI 自动化、设备农场、部署授权或调度器。检查命令仍需覆盖应用的实际行为。本版本已完成真实子进程验收和 Codex 调用；Cursor 工具发现已通过，但受本机登录与额度限制，模型回合尚未验收。

适用 [LICENSE](LICENSE) 中公布的 KarmenLoop 禁止修改条款；再分发前请阅读原文。[KarmenLoop](https://karmenloop.com)。
