# App Module Delivery

Version 1.0.1. An English public edition of the application-development workflow designed with KarmenLoop.

Use it for complete applications, extensions, and module changes across selected desktop, mobile, web business, and CLI targets. Pure marketing websites belong in a website workflow.

## Use

Read [SKILL.md](SKILL.md), or install the complete directory using [Platform setup](references/platforms.md). The main file loads stage-specific references as needed.

~~~text
Read /absolute/path/app-module-delivery/SKILL.md.
Task: [application or module, current project, actual targets, requested scope].
Reuse existing answers and inspect technical facts yourself.
Deliver a complete plan, then continue already-authorized implementation,
integration, actual operation, repair, and acceptance.
Follow project ownership, tool permissions, and existing acceptance rules.
~~~

No mandatory framework, model, external account, or other skill is required. Communicate in the user's language.

## Resources

| Resource | Purpose |
| --- | --- |
| [Discovery](references/discovery.md) | 72 candidate questions and interview rules |
| [Architecture](references/architecture.md) | Modules, interfaces, dependencies, data, state, targets |
| [UI/UX](references/ui-ux.md) | Task research, workspaces, navigation, interaction, recovery |
| [Development](references/development.md) | Technical choices, reuse, sequence, integration, previews |
| [Testing](references/testing.md) | Observable results, defects, regression, final acceptance |
| [Delivery/recovery](references/delivery-recovery.md) | Handoff, milestones, persistent progress, resumption |
| [Platforms](references/platforms.md) | Seven host setup routes and honest capability limits |
| [Evaluations](references/behavior-evals.md) | Scenarios for actual agent-behavior evaluation |
| [Application plan](templates/application-plan.md) | Starting point for the six project-record templates |
| [Validation](VALIDATION.md) | Actual checks, evidence boundaries, untested areas |

## Verify

The verifier and its tests use Python 3.9 or later and the standard library:

~~~sh
python3 scripts/verify_package.py
python3 -B validation/test_verifier.py
python3 scripts/verify_package.py --archive /absolute/path/to/release.zip
~~~

The verifier reads files; its regression suite mutates isolated temporary copies. Checks cover resources, relative references, question inventory, Markdown fences, manifest, archive bytes, and CRC. They do not establish client loading, agent decisions, or application runtime.

## License

Copyright 2026 KarmenLoop. This is source-available under the [No-Modification License](LICENSE), not an OSI open-source license. Use and exact-copy redistribution are permitted under its conditions; modified workflow distributions require written permission. Project records completed from the supplied templates have an explicit permission in the license.
