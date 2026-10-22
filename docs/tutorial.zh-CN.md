# App Module Delivery · 应用与模块交付: 使用指南

[English](tutorial.en.md) | 简体中文 · [项目首页](../README.zh-CN.md)

本指南对应 **v1.0.2**.

## 1. 下载与校验

从发行页下载 [`app-module-delivery-v1.0.2.zip`](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.0.2)，同时保留校验文件或 manifest。比较完整 SHA-256 后再解压：macOS 使用 shasum -a 256，Linux 使用 sha256sum，PowerShell 使用 Get-FileHash -Algorithm SHA256。校验只能证明字节一致，预期哈希本身也需要可信来源。

## 2. 安装与加载

解压 ZIP，将整个 app-module-delivery 文件夹放入宿主支持的一个技能目录，例如 ~/.agents/skills/app-module-delivery。使用新目录，保留 references、templates、VERSION、LICENSE 和 MANIFEST.json。

刷新宿主发现或开启新会话，明确读取已安装的 SKILL.md，并核对上面版本。不需要为技能另开模型账号；宿主使用自己的模型、工具与权限。

## 3. 配置与第一项任务

技能本身不读取 API 密钥或配置文件。明确宿主、项目路径、目标平台与授权范围；文件、终端、浏览器等实际能力由宿主提供。

加载 SKILL.md，说明现有的一个模块、需要改变的行为，以及用户如何判断可用。先检查生成的计划和验收标准，再依据实际交件判断实现是否完成。

## 4. 进一步实践

跟踪一次变更从计划、集成、真实用户操作到恢复的全过程。包验证只检查文件和引用，不能证明宿主决策或应用运行通过。

保留当前版本、真实命令、退出码、结果与未验证限制。使用合成数据做首次检查。

## 5. 排错、升级与移除

宿主找不到技能时，先检查配置的技能根目录和 SKILL.md 可读性。哈希不一致时停止使用该包并重新核对下载；不要跳过错误。

升级前完成当前写入，分别备份技能与私人任务数据。将新版本解压到新目录，核对后再切换；回退时恢复旧技能，保留较新的用户数据与证据。卸载只移除对应技能目录或发现入口；如曾另行注册调度，应在真实宿主中取消并确认。

## 6. 许可证

[KarmenLoop Source-Available No-Modification License 1.1](../LICENSE). 此处提供简明用户指南；具体使用和再分发条件以许可证原文为准。
