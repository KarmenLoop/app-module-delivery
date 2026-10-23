# App Module Delivery v1.1.0 宿主教程

[English](tutorial.en.md) · [中文](tutorial.zh-CN.md)

1. 下载并解压当前技能 ZIP，使用 Python 3.11+，按许可证保持文件完整。仓库内入口为 `skills/app-module-delivery/scripts/host.py`；ZIP 内为 `app-module-delivery/scripts/host.py`。
2. 在应用工作区创建 `.app-delivery-checks.json`，登记所有者批准的命令。每项必须包含精确 `argv` 数组，可选 `cwd`、`timeout_seconds`（1–60）、`expected_exit` 和工作区内 `artifacts`、`inputs` 路径。将变化后需要使结果失效的源码或配置列入 `inputs`；只有这些登记的输入与产物参与后续变化核对。应使用真正验证应用、生成实际产物的命令，不能以 echo 代替功能。
3. 替换路径后，为两个宿主安装工作区配置：

```sh
python /path/to/host.py --root /private/app-acceptance --workspace /path/to/application --install-host codex install
python /path/to/host.py --root /private/app-acceptance --workspace /path/to/application --install-host cursor install
```

4. 重载宿主并批准特定服务，确认能发现 `app_init`、`app_run_check`、`app_status`、`app_export`。用 `app_init` 设置项目 ID、目标，并将需求 ID、标题映射到已登记的 `check_id`。
5. 读取当前版本后，用项目、检查 ID、`expected_revision` 调用 `app_run_check`。检查真实退出码、日志、产物哈希与需求结果。失败后修复应用，再使用新版本号执行同一批准检查；适配器自身不会修复应用。
6. `app_status` 会重新核对产物。变化或缺失会显示 `STALE`；命令配置改变需要重新审核并建立新计划。用 `app_export` 导出当前验收记录。

无需模型也能调用：`python /path/to/host.py --root /private/app-acceptance --workspace /path/to/application call app_status --input request.json`，输入 JSON 包含 `project_id`。

宿主运行中退出时，等待原检查的有限超时窗口，再读取 `app_status`。独立的受控 runner 会保存终态收条，重连后只对账一次，不重复执行。若 runner 或电脑本身在写收条前被终止，状态保持运行中/未知并阻止重复运行，需人工检查原运行目录，不能按通过处理。每份日志有 8 MiB 轮询限制。

这是本地验收台账与登记命令执行器，不会生成设备证据、调度计划或额外执行授权。已在 macOS 完成真实子进程与 Codex 读取验收；Cursor 工具发现已通过，模型回合和 Windows/Linux 原生使用仍待验证。
