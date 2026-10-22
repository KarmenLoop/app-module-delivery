# App Module Delivery · 应用与模块交付

[English](README.md) | 简体中文

改造应用时，接口、用户流程和验收很容易各说各话。这个技能把这些工作放回同一个交付流程，从现有工程和真正需要支持的平台开始。

[下载 v1.0.2](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.0.2) · [教程](docs/tutorial.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/app-module-delivery/issues)

## 用途与范围

适用于完整应用、扩展或局部模块改造。包内是工作流程、参考资料和项目记录模板，不是可直接启动的业务应用。

![应用与模块交付流程示意](docs/images/workflow-v1.0.2.svg)

*v1.0.2 的流程示意，非应用截图或运行验收。*

## 开始使用

解压 ZIP，将整个 app-module-delivery 文件夹放入宿主支持的一个技能目录，例如 ~/.agents/skills/app-module-delivery。使用新目录，保留 references、templates、VERSION、LICENSE 和 MANIFEST.json。

技能本身不读取 API 密钥或配置文件。明确宿主、项目路径、目标平台与授权范围；文件、终端、浏览器等实际能力由宿主提供。

## 第一次有用的任务

加载 SKILL.md，说明现有的一个模块、需要改变的行为，以及用户如何判断可用。先检查生成的计划和验收标准，再依据实际交件判断实现是否完成。

跟踪一次变更从计划、集成、真实用户操作到恢复的全过程。包验证只检查文件和引用，不能证明宿主决策或应用运行通过。

## 常见问题

**会安装哪套框架？** 不会安装框架。它使用项目已有技术栈和宿主实际具备的工具。

## 文档与许可证

[下载到实践的使用指南](docs/tutorial.zh-CN.md) · [LICENSE](LICENSE)

KarmenLoop Source-Available No-Modification License 1.1. 许可证条件以原文为准，再分发时保留包内法律文件。 [KarmenLoop](https://karmenloop.com).
