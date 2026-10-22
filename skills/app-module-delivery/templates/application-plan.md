# Application plan template

Copy into the project and replace bracketed fields. Empty fields are not verified facts. Keep unresolved decisions visible; remove inapplicable sections only with reasons. Small projects may combine tables.

## 1. Goal and boundaries

- Project, date, responsible owner: [fill]
- Assignment: [greenfield / extension / module change / narrow repair]
- Mode: [discussion/plan / prototype / implementation]
- Users, problem, current process, observable success: [fill]
- Required scope, exclusions, permitted deferrals, resource constraints: [fill]
- Targets, OS/architecture/device range: [fill]
- Existing implementation/integration ownership, independent/human gates, authorization: [fill]

## 2. Decisions and materials

| ID | Conclusion | Decision/fact/assumption/unresolved | Source/date | Impact and resolution |
| --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] |

## 3. Scenarios and requirements

| Requirement | Role and goal | Entry and steps | Observable result | Required/priority | Acceptance ID |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

Include first-use, everyday, consequential, collaborative, and failure paths as applicable.

## 4. Business model

- Entities, relationships, ownership, authoritative data: [fill]
- Rules, calculations, invariants, allowed transitions: [fill]
- Concurrency, duplicates, atomicity/partial success, side effects: [fill]
- Cancellation, undo, timeout, unknown outcomes, recovery: [fill]
- Identity, roles, resource/tenant access, revocation: [fill]

## 5. Architecture and modules

Use the [Architecture template](architecture.md) for logical/runtime views, flows, dependencies, and target capabilities. Refine substantial modules with the [Module template](module-design.md).

| Module | Responsibility and limits | Public capabilities | Data ownership | Dependencies | Reuse/add/change | Requirements/acceptance |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

## 6. UI/UX and platforms

- Research sources, actual inspection, adopted principles: [fill]
- Navigation, workspace, primary task, return relationships: [fill]
- Visual system, component states, representative flow: [fill]
- Interaction contracts, recovery, motion, accessibility: [fill]
- Shared meaning, target-specific operation, limits, alternatives: [fill]

## 7. Technical and runtime plan

| Choice/reuse | Verified needs/constraints | Recommendation/evidence | Alternatives/tradeoffs | Version/license/dependencies | Experiment |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

Runtime, storage, configuration, services, offline/sync, maintenance, and cost: [fill]. Distinguish experiments, sandboxes, and live services.

## 8. Implementation and acceptance

| Increment/task | Requirements/modules | Ready prerequisites | Change scope | Result/completion | Actual checks | Sequence rationale |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

Use the [Acceptance template](acceptance.md) for applicable test levels. Separate self-review and independent/human gates. Define performance environment, workload, budget, and measurement.

## 9. Compatibility, delivery, resumption

- Baseline, preserved/changed behavior, existing failures: [fill]
- Migration, coexistence, cutover, rollback prerequisites: [fill]
- Source/packages, configuration, startup, use, maintenance: [fill]
- Blockers, untested areas, owners, resolution conditions: [fill]
- Existing authority, necessary decisions, next action: [fill]

Exit when every required item has an implementation and acceptance path, unresolved items are visible, and users can understand the proposed route. Follow existing authorization after presenting the plan. Template completion is not runtime acceptance.
