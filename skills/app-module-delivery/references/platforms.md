# Setup across seven agent hosts

Official documentation was checked on October 22, 2026. Documented installation is not proof that this package has loaded or executed in a particular client. Preserve the complete directory and relative resources.

## Native entry points

Install one authoritative copy per host. The expected shape is skills-root/app-module-delivery/SKILL.md, without an extra nested directory.

| Host | Installation and invocation | Evidence boundary |
| --- | --- | --- |
| Codex | User ~/.agents/skills/app-module-delivery/ or project .agents/skills/app-module-delivery/; invoke $app-module-delivery | Current official directories checked; older ~/.codex/skills behavior depends on the actual host. Native execution of this English edition is untested |
| Claude Code | User ~/.claude/skills/app-module-delivery/ or project .claude/skills/app-module-delivery/; invoke /app-module-delivery | Local documentation checked; package loading untested |
| Cursor | User ~/.cursor/skills/app-module-delivery/ or project .cursor/skills/app-module-delivery/; also reads .agents/skills/ and ~/.agents/skills/; invoke /app-module-delivery or select it with @ | Official documentation checked; package loading untested |
| Qoder IDE/CLI | User ~/.qoder/skills/app-module-delivery/ or project .qoder/skills/app-module-delivery/; invoke /app-module-delivery | Both documentation routes checked; actual client loading and execution untested |
| WorkBuddy | Skills section, Add Skill, Upload Skill; choose a local package, then confirm installed and enabled | Upload route documented; this ZIP has not been imported. Follow the target client's accepted formats |
| Koder | Verify the current product's custom-skill import/loading and file-reading capabilities; use the explicit-file prompt below when native support is unverified | Desktop native import untested; no invented dedicated directory |
| Koder CLI | Establish product identity/version and actual custom loading; use the file-reading prompt in a capable project session | Limited inspection of a local CLI 0.3.0 installation established bundled resource reading, not user-defined loading. This package was not executed there |

agents/openai.yaml provides optional Codex UI metadata. The portable frontmatter contains ordinary name/description/license fields; no fixed model, tool, or permission settings are required.

Qoder IDE documentation describes project-level precedence, whereas CLI documentation describes user-level precedence. Avoid conflicting duplicate copies and inspect the actual loaded path. IDE documentation uses restart/list discovery; CLI documentation provides /skills reload, subject to target-version verification.

Koder and Koder CLI here mean the user's KARMEN/KODER products. Do not substitute unrelated products named Koder, Kode, Qoder, or QoderWork. The limited local inspection concerned package metadata and bundled ecosystem reading; it proves neither universal support nor universal absence of custom-skill loading.

## Explicit file-reading fallback

In any agent that can read the project files, replace the path and send:

~~~text
Read /absolute/path/app-module-delivery/SKILL.md.
Load the references and templates needed for this assignment, preserving relative paths.
Task: [application/module, greenfield/extension/change, targets, existing materials].
Reuse answers already supplied. Inspect technical facts yourself.
Deliver a complete application plan, then continue implementation, integration,
actual operation, and acceptance already authorized.
Check project rules, current files, actual tools, and existing authorization first.
~~~

This is an explicit workflow invocation, not native automatic discovery. Use it in a Koder workspace or Koder CLI session with genuine access to the directory. Follow supported directory authorization rather than inventing flags.

If local files are inaccessible, provide the complete directory through supported project attachments or sources. A text-only agent can plan from supplied references but cannot claim file edits, execution, or previews it cannot perform.

## Cloud, remote, and missing capabilities

Local directories do not automatically appear in cloud or remote sessions. Install or import into the actual environment and check relative-resource access. Cloud localhost identifies that environment; previews need supported forwarding.

Claude Code distinguishes local, Cowork, and cloud loading. Cursor documents personal cloud sync for ~/.cursor/skills/; other local directories do not automatically follow it. Administrative policy may restrict access.

| Missing capability | Continue | Keep unverified |
| --- | --- | --- |
| Network/search | Local facts, existing engineering, supported planning | New sources, versions, licenses, real connectivity |
| File writes/terminal | Requirements, design, executable handoff | Changes, execution, actual tests |
| Browser/native UI | Source and available command/interface checks | Interaction, visual quality, system operation |
| Target OS/device | Available environments | Missing target's installation and behavior |
| External service/access | Independent real flows and useful local stand-ins | Actual external end-to-end results |
| Scheduling | Exact waiting conditions and resumption records | Automatic wakeups and unattended continuation |

Stand-ins and alternatives do not remove required acceptance. Only dependent branches are blocked.

## Per-host acceptance

Record product/version, OS/architecture, skill version/hash, installation source, invocation, and actual read path. Verify discovery or explicit loading and one conditional reference; reuse supplied answers and produce a plan; perform isolated file changes and real commands; complete a correlated business result; operate available GUI/CLI/devices; resume against actual versions and processes.

Report documented support, installation, loading, execution, preview/interaction, and full-flow acceptance separately. See [Validation](../VALIDATION.md).

## Official sources

- [Codex Skills](https://learn.chatgpt.com/docs/customization/overview#skills)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Cursor Skills](https://cursor.com/help/customization/skills)
- [Qoder IDE](https://docs.qoder.com/extensions/skills)
- [Qoder CLI](https://docs.qoder.com/cli/Skills)
- [WorkBuddy Skills](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
