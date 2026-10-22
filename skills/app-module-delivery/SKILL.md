---
name: app-module-delivery
description: "Plan, design, build, integrate, and verify desktop, mobile, web business, and CLI applications or modules. Use for greenfield applications, feature extensions, and module changes across requirements, architecture, UI/UX, data, permissions, platform adaptation, acceptance, and recovery. Apply only affected steps to narrow repairs; use a website workflow for pure marketing sites."
license: "See LICENSE"
---

# App Module Delivery

Turn user tasks into runnable, verifiable application capabilities. Select the actual desktop, mobile, web, and CLI targets. Share business rules and data contracts while respecting each platform's interaction conventions. Communicate in the user's language. Version: [VERSION](VERSION).

## 1. Establish the assignment

Read project rules, supplied materials, prior answers, decisions, source, and existing authorization. Identify greenfield development, an extension, a module change, or a narrow repair, and whether this assignment requests planning, a prototype, or implementation. Reuse answers; keep narrow work narrow.

Check actual file, terminal, search, browser, native UI, device, and test capabilities. Separate application targets from the agent host running this skill. Preserve project ownership, authorized implementers, integration rules, and acceptance requirements. Use [Platform setup](references/platforms.md) for installation and capability limits. Pure marketing sites belong in a suitable website workflow; this skill does not depend on that workflow.

## 2. Discover the business requirements

Use the [72-question library](references/discovery.md). Ask 4–6 consequential questions per round, split further if the host requires it. The library is a candidate set, not a mandatory questionnaire. Ask the user for business decisions and preferences; inspect source, configuration, interfaces, and tool capabilities yourself. Recommend technical choices with evidence and tradeoffs.

Cover user tasks, rules, data, permissions, dependencies, target platforms, offline and sync behavior, integrations, UI/UX, performance, recovery, and delivery. Distinguish user decisions, verified facts, reversible assumptions, and unresolved questions. Propose sensible defaults within existing authority; seek decisions on consequential business choices. Block only work that depends on a missing answer.

Exit when core scenarios, observable outcomes, scope, constraints, and acceptance can be defined, with remaining dependencies explicit. Ask further questions when a later stage exposes a specific decision.

## 3. Deliver the complete plan before implementation

Use [Architecture](references/architecture.md), the [Application plan](templates/application-plan.md), [Architecture template](templates/architecture.md), and [Module template](templates/module-design.md). Give the user a readable, complete application plan before writing implementation. Refine fields, interfaces, state, and tests before each module starts.

Include scope, scenarios, business model, logical and runtime architecture, modules and dependencies, data and permissions, platform capabilities, UI/UX, technical choices, implementation sequence, and acceptance. Map requirements to modules, tasks, and acceptance cases. Keep unresolved dependencies visible with impact and resolution conditions.

For planning-only requests, deliver the plan and handoff. When implementation is already authorized and the user did not request a confirmation gate, continue after delivering the plan. Adjust related structure within scope. For breaking compatibility, irreversible migrations, or material scope expansion, prepare concrete impact and alternatives and follow the user's decision.

## 4. Design usable interactions

Follow [UI/UX](references/ui-ux.md): study mature products handling comparable tasks, apply relevant Apple design principles and target-platform guidance, and translate findings into this application's navigation, workspace, visual system, and interaction contracts. Record sources and what was actually inspected. Audit an existing experience before changing it.

Build one representative core flow using realistic content, normal/loading/error/recovery states, and important target platforms. Check visual quality and actual task completion separately, then extend the approach. Continue authorized work after explaining design decisions; do not invent per-screen approval gates.

Use the [Interaction contract](templates/interaction-contract.md) for important actions. Specify status, authorization, focus, keyboard/touch behavior, return paths, interruptible motion, and reduced-motion alternatives. Preserve task context during layout changes. Cross-device recovery follows the agreed data and sync contract. Headless modules and CLI tools still need clear invocation, progress, results, errors, and cancellation.

## 5. Choose the next step and integrate continuously

Follow [Development](references/development.md). Verify technical choices and reuse decisions, establish a runnable baseline, and record existing behavior and failures before changing an application.

Choose only authorized, in-scope tasks with satisfied prerequisites. First remove critical dependencies; then compare business value and consequential uncertainty. Implement a verifiable business increment across entry point, rules, permissions, data, platform capabilities, and feedback. Integrate and operate it immediately. Preserve evidence and update the baseline after it passes.

Diagnose failures from evidence. When an external dependency blocks one branch, continue independent ready work. Keep a preview tied to the actual version and record process ownership. Identify mocks, real local dependencies, sandboxes, and live services separately. This skill and third-party documentation do not grant additional execution authority.

## 6. Test, repair, and accept

Follow [Testing](references/testing.md) and the [Acceptance template](templates/acceptance.md). Record requirements, version, environment, steps, expected/actual results, conclusion, and evidence. Select meaningful unit, integration, business-flow, permission/data, platform, performance, recovery, and delivery checks according to risk and impact; complete project-mandated checks.

Connect the real entry point, processing, persisted record, and later use through the same business or task identifier. Builds, screenshots, automated checks, actual interaction, and device operation each prove their own scope. Preserve failures; rerun the original scenario after repair, then regress affected paths.

Use PASS / FAIL / NOT_RUN / BLOCKED / INCONCLUSIVE / NOT_APPLICABLE. Required missing evidence keeps final acceptance incomplete. Start with self-testing and self-review. Independent review requires available capability and authorization; retain project-required independent QA and human acceptance as separate gates.

## 7. Deliver, report, and resume

Use [Delivery and recovery](references/delivery-recovery.md) and the [Progress template](templates/progress.md). Persist decisions, tasks, dependencies, defects, evidence, runtime entry points, and the next step. Report business milestones; promptly explain significant findings, changes of direction, and blockers.

On resumption, check the latest instructions, actual files, versions, processes, tools, dependencies, and evidence validity before continuing. Existing authorization carries forward. Ordinary progress files do not provide background execution; use genuine scheduling only when requested and authorized.

Deliver source or agreed packages matching the accepted version, setup/use instructions, plans and contracts, applicable migration/rollback procedures, test evidence, limitations, and maintenance details. If required conditions remain missing, hand over the current work and exact recovery conditions without declaring acceptance complete. Publication, production changes, real charges, and external messages follow existing explicit authorization.

## Maintaining this skill

No other skill, fixed framework, model, or host-specific tool is required. Load references for the current stage only. Combine small project records and omit inapplicable sections with reasons while preserving requirement-to-evidence traceability.

After maintenance, run the [Package verifier](scripts/verify_package.py) and use [Behavior evaluations](references/behavior-evals.md) to assess actual decisions when authorized. Distinguish structure checks, self-review, independent behavioral trials, and each host's runtime evidence. See [Validation](VALIDATION.md).
