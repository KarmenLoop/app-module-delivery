# App Module Delivery

[English](README.md) · [中文](README.zh-CN.md) · **v1.1.0**

Plan an application, register its acceptance checks, and keep the actual results with the requirements they verify. The skill now includes a Python CLI/MCP adapter for Codex and Cursor.

![Application delivery workflow](docs/images/workflow-v1.1.0.svg)

The adapter runs exact commands registered by the workspace owner. It stores real exit codes, logs, and artifact hashes; changed evidence invalidates an earlier pass. A check can finish after its host connection closes, and the next connection recovers that same receipt without rerunning it.

Download the versioned ZIP from [Releases](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.1.0). Python 3.11+ is required. Follow the [host tutorial](docs/tutorial.en.md). The installable skill is under `skills/app-module-delivery` in this repository and at the root of the skill ZIP.

The adapter does not supply an agent model, GUI automation, device farm, deployment permission, or scheduler. It verifies registered checks; those checks must still cover the application's real behavior. This release completed a live Codex read and actual subprocess acceptance. Cursor tool discovery passed; a Cursor model turn remains unverified because of local authentication and usage limits.

[License](LICENSE): KarmenLoop's published no-modification terms apply. Review those terms before redistribution. [KarmenLoop](https://karmenloop.com).
