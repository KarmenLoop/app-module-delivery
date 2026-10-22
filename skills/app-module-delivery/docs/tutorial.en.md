# App Module Delivery: user guide

English | [简体中文](tutorial.zh-CN.md) · [Project](../README.md)

This guide matches **v1.0.2**.

## 1. Download and verify

From the release, download [`app-module-delivery-v1.0.2.zip`](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.0.2) and its checksum file or manifest. Compare the complete SHA-256 before extracting: use shasum -a 256 on macOS, sha256sum on Linux, or Get-FileHash -Algorithm SHA256 in PowerShell. Byte consistency relies on obtaining the expected hash from a trusted source.

## 2. Install and load

Extract the ZIP and keep the entire app-module-delivery folder under one skill directory supported by your host, for example ~/.agents/skills/app-module-delivery. Use a fresh destination; keep references, templates, VERSION, LICENSE, and MANIFEST.json together.

Refresh host discovery or open a new session, explicitly read the installed SKILL.md, and check the version above. The skill needs no separate model account; the host supplies its own model, tools, and permissions.

## 3. Configure and try one task

No API key or configuration file is consumed by the skill. Select the host, project path, target platforms, and authorized scope; the host must supply actual file, terminal, and browser capabilities.

Load SKILL.md and describe one existing module, the change needed, and how a user will know it works. Review the resulting plan and acceptance checks before relying on implementation work.

## 4. Develop a repeatable workflow

Follow one change through planning, integration, a real user operation, and recovery. Package verification checks files and references; it does not prove host decisions or application behavior.

Keep the version, actual command, exit code, resulting files, and unverified limits together. Use synthetic data for the first check.

## 5. Troubleshoot, update, and remove

If the host cannot find the skill, check its configured discovery root and SKILL.md readability. A checksum mismatch needs a fresh verified download; do not skip it.

Finish active writes and back up the skill and private task data separately. Extract updates into a new directory and verify before switching. For rollback, restore the older skill while retaining newer user records and evidence. Uninstall only its exact skill directory or discovery entry; separately registered schedules must be cancelled and confirmed in their host.

## 6. License

[KarmenLoop Source-Available No-Modification License 1.1](../LICENSE). This is concise user guidance; consult the original license for use and redistribution terms.
