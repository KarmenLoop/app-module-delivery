# App Module Delivery

[![Verify](https://github.com/KarmenLoop/app-module-delivery/actions/workflows/verify.yml/badge.svg)](https://github.com/KarmenLoop/app-module-delivery/actions/workflows/verify.yml)
[![Release](https://img.shields.io/github/v/release/KarmenLoop/app-module-delivery)](https://github.com/KarmenLoop/app-module-delivery/releases)

An agent skill for planning, designing, building, integrating, and verifying complete applications and application modules.

Use it to create an application, add a capability to an existing product, or change a module without losing track of its callers, data, permissions, and recovery behavior.

**[Download](https://github.com/KarmenLoop/app-module-delivery/releases/tag/v1.0.1)** · **[Quickstart](docs/quickstart.md)** · **[Read the skill](skills/app-module-delivery/SKILL.md)** · **[Workflow](docs/workflow.md)** · **[Validation](skills/app-module-delivery/VALIDATION.md)**

![App Module Delivery workflow](docs/images/workflow.svg)

## What it covers

| Stage | Concrete output |
| --- | --- |
| Discovery | User tasks, business rules, data, access, dependencies, targets, and measurable success |
| Complete plan | Scope, scenarios, architecture, modules, contracts, UI/UX, implementation order, acceptance |
| Module design | Responsibility, public interface, data ownership, state, dependencies, lifecycle, platform adaptation |
| UI/UX | Industry/task research, navigation, workspace, interaction, feedback, motion, accessibility, recovery |
| Implementation | Evidence-based choices, selective reuse, ready-task decisions, business increments, actual operation |
| Integration | Host entry points, identity, storage, public contracts, lifecycle, correlated results |
| Acceptance | Unit, integration, business, permission/data, platform, performance, failure and recovery checks |
| Handoff | Matching source/artifacts, instructions, evidence, limitations, ownership, resumption |

The package includes a **72-question candidate library**, **six project templates**, **seven host setup routes**, and **12 behavioral evaluation scenarios**. Questions are selected by information gaps; users are not asked to answer the whole library.

## How it works

The agent first reuses existing answers and inspects technical facts. It asks consequential business questions with recommendations and delivers a complete application plan before implementation.

Once work is already authorized, it selects the next increment from satisfied dependencies, business value, and consequential uncertainty. It connects the actual entry point, business rules, authorization, persistence, and feedback, then operates and inspects the result. Failures lead to diagnosis and affected regression. An unavailable dependency blocks its branch rather than unrelated ready work.

Shared business meaning and data contracts support desktop, mobile, web business, and CLI targets. Each target uses appropriate interactions. Technology and deployment follow the actual project; no framework, model, account, or companion skill is mandatory.

## Start with your assignment

Download and extract the release, then use the [host setup guide](skills/app-module-delivery/references/platforms.md). The installable directory is skills/app-module-delivery in this repository.

For any agent that can read the directory:

~~~text
Read /absolute/path/app-module-delivery/SKILL.md.
Task: [application or module, current project, requested scope, target platforms].
Reuse the requirements and decisions already supplied.
Inspect technical facts yourself and ask only consequential decision gaps.
Deliver a complete application plan, then continue development, integration,
actual operation, repair, and acceptance already authorized.
Preserve existing ownership, unrelated edits, and required QA gates.
~~~

Examples:

- Create a local records application and verify creation, persistence, query, permissions, and restart.
- Add an import capability using an existing product's identity and storage contracts.
- Change a module with explicit compatibility, migration, and rollback conditions.
- Repair one interaction using only affected steps.
- Deliver a complete plan while preserving a planning-only scope.

These are usage scenarios, not claims of included application implementations.

## Six project-record templates

| Template | Use |
| --- | --- |
| [Application plan](skills/app-module-delivery/templates/application-plan.md) | Full scope, scenarios, decisions, architecture, delivery and acceptance |
| [Architecture](skills/app-module-delivery/templates/architecture.md) | Logical/runtime views, data/state, dependencies and targets |
| [Module](skills/app-module-delivery/templates/module-design.md) | Interface, implementation, lifecycle, dependencies and tests |
| [Interaction](skills/app-module-delivery/templates/interaction-contract.md) | Real action, states, feedback, accessibility and recovery |
| [Acceptance](skills/app-module-delivery/templates/acceptance.md) | Expected/actual results, evidence, defects and final conclusion |
| [Progress](skills/app-module-delivery/templates/progress.md) | Persistent facts, runtime ownership, next actions and resumption |

Fill templates with actual project facts. Empty fields do not establish progress. The license explicitly permits completed project records.

## Agent hosts

Setup instructions cover **Codex, Claude Code, Cursor, Qoder IDE/CLI, WorkBuddy, Koder, and Koder CLI**. The [platform guide](skills/app-module-delivery/references/platforms.md) identifies documented paths, native invocation, cloud differences, and file-reading fallbacks.

Koder-specific custom loading remains unverified. Do not substitute directories from unrelated similarly named products. Native discovery, explicit file loading, execution, previews, and end-to-end acceptance are separate evidence levels.

## Verification

Use Python 3.9 or later:

~~~sh
python -m pip install -r requirements-dev.txt
python -B scripts/check_repository.py
python -B skills/app-module-delivery/validation/test_verifier.py
python -B scripts/package_skill.py --output-dir dist
~~~

The package verifier is standard-library Python. Repository authoring checks additionally use PyYAML. CI runs package and tool checks on Linux, macOS, and Windows. A passing CI job does not prove native agent-client loading or application behavior.

The 14 verifier regressions exercise valid and damaged packages, including relocation, broken references, missing files, content drift, malformed manifests, and unsafe archives. Release checks compare file inventories, bytes, hashes, and ZIP CRC.

Read the [actual validation record](skills/app-module-delivery/VALIDATION.md), [verification guide](docs/verification.md), and [behavioral scenarios](skills/app-module-delivery/references/behavior-evals.md). Real agent trials, native host execution, and application/device/performance/recovery acceptance remain unverified for this edition.

## License and copyright

Copyright 2026 KarmenLoop. This repository uses the **[KarmenLoop Source-Available No-Modification License 1.1](LICENSE)**.

You may use and redistribute exact copies under its conditions. Modified, translated, or rebranded workflow distributions require prior written permission. Completed project records and independently created outputs are addressed explicitly.

This is **source-available**, not an OSI-approved open-source project. See [licensing details](docs/licensing.md). GitHub's public viewing and fork rights and third-party rights remain intact.
