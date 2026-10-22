# App Module Delivery

English | [简体中文](README.zh-CN.md)

A planning and delivery skill for changing an application without losing track of its interfaces, user flows, and acceptance checks. Start with the existing project and the platforms it actually needs.

[Download v1.0.2](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.0.2) · [Guide](docs/tutorial.en.md) · [Issues](https://github.com/KarmenLoop/app-module-delivery/issues)

## What it does

Use it for a complete application, an extension, or a module change. The package contains workflow instructions, references, and project-record templates; it is not an application runtime.

![App Module Delivery workflow illustration](docs/images/workflow-v1.0.2.svg)

*Workflow illustration for v1.0.2; not an application screenshot or runtime acceptance.*

## Start here

Extract the ZIP and keep the entire app-module-delivery folder under one skill directory supported by your host, for example ~/.agents/skills/app-module-delivery. Use a fresh destination; keep references, templates, VERSION, LICENSE, and MANIFEST.json together.

No API key or configuration file is consumed by the skill. Select the host, project path, target platforms, and authorized scope; the host must supply actual file, terminal, and browser capabilities.

## A first useful task

Load SKILL.md and describe one existing module, the change needed, and how a user will know it works. Review the resulting plan and acceptance checks before relying on implementation work.

Follow one change through planning, integration, a real user operation, and recovery. Package verification checks files and references; it does not prove host decisions or application behavior.

## Questions

**Which framework does it install?** None. It works with the project’s chosen stack and the host’s available tools.

## Documentation and license

[Download, setup, practice, and updates](docs/tutorial.en.md) · [LICENSE](LICENSE)

KarmenLoop Source-Available No-Modification License 1.1. The original license terms govern use and redistribution; retain the included legal files. [KarmenLoop](https://karmenloop.com).
