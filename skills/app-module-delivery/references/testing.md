# Testing, repair, and acceptance

Define cases with the [Acceptance template](../templates/acceptance.md) before implementation. Link requirements, modules, targets, tasks, and evidence. Coverage percentages help find omissions but do not establish acceptance.

## Acceptance contract

Specify roles, initial data/dependencies, actions, expected observable results, environment, and evidence. Identify required and genuinely inapplicable cases before testing. Preserve existing independent QA and human gates.

Start with self-testing and self-review. Independent review requires authorization and capability. Distinguish author reports, independent source/screenshot review, independent operation, and human confirmation.

| Layer | Check | Evidence |
| --- | --- | --- |
| Unit | Computation, validation, invariants, transitions, boundaries, distinct errors | Observable results through a module contract; stand-ins may isolate dependencies |
| Integration | Calls, persistence, events, adapters, identity, error propagation | Actual contracts, data and side effects; identify real versus simulated dependencies |
| Business flow | Real GUI/CLI/device entry through receipt, persistence, later use | One correlated record/task identifier |
| Permission/data | Roles, resource/tenant isolation, constraints, transactions, idempotency, concurrency | Allowed success, denied access, and matching data results |
| Platform | Agreed OS/architecture, window, input, lifecycle, capability limits | Actual per-target scenarios; simulation and hardware labeled |
| Performance | Startup, response, throughput, resource use, long-running work | Environment, workload, budget, sampling, raw results |
| Recovery | Cancellation, timeout, disconnection, crash, write failure, conflict, outage | Intermediate facts, terminal state, integrity, recovery |
| Delivery | Configuration, build, installation, startup, migration, upgrade, applicable rollback | Operate the delivered candidate using its instructions |

Complete project-mandated checks and choose meaningful additional tests by impact. Do not add implementation-mirroring tests for trivial reversible visual changes. Preserve valuable behavior coverage during refactoring.

## Complete business flows

For example: create a record, persist it and return an identifier, query it elsewhere, authorize a state/history update, refresh or restart, and inspect the same result. Add actual external actions, devices, and sync where required.

Check the actual running version, roles, data prerequisites, feedback, persistence, and later use. API checks and real GUI/CLI operation are separate. Mocks establish their covered local behavior; sandboxes do not prove production services; screenshots do not establish persistence.

## Permissions and data

Test applicable unauthenticated, expired, insufficient-role, other-owner/tenant, revoked, and direct-interface access. Hidden controls only establish presentation behavior. Check authorization where the action executes.

Validate fields, relationships, uniqueness, duplicate submission, concurrent edits, illegal transitions, rollback or explicit partial success, file integrity, restart persistence, migration, import/export, and recovery as applicable. Use isolated accounts/data and clean up only owned records. Redact evidence appropriately.

## Platforms, UI/UX, and performance

Record OS/architecture, application/browser and build versions, window space, input, device or simulator. Reuse business meaning while operating each target's real entry. Include resizing, keyboards, system back, backgrounding, denied permissions, large text, language, focus, screen readers, and reduced motion where relevant.

Check visual quality and task usability separately: long content, hierarchy, density, wrapping, discoverability, and recovery. Verify actual screenshot viewport and scale. No overflow does not prove phone usability; emulation is not physical-device evidence.

Define performance thresholds, hardware/environment, data scale, concurrency/batch load, cold/warm state, sampling, and statistics first. Report percentiles only with suitable samples. Retain raw results. Check peak use, release, and long-term growth. Compare optimizations under comparable conditions.

## Recovery scenarios

| Failure | Inspect |
| --- | --- |
| Network/timeout | Preserved input and commits, known versus unknown outcome, lookup and idempotent retry |
| Crash/exit/restart | Committed data, task recovery, loss boundaries, terminal-state reconciliation |
| Cancellation | Request, actual cessation, completed portions, receipt, resource release |
| Write failure/full storage | Clear errors, transactions, original data integrity |
| External outage | Bounded waits, independent work, recovery, side-effect reconciliation |
| Concurrent edits | Conflict detection, understandable differences, agreed decisions |
| Partial success | Accurate details, remaining work, later use |

Trigger faults in authorized isolated conditions. Inspect intermediate and final states. A recovery control requires an actual working behavior.

## Results and evidence

Record case/requirement ID, source/uncommitted-change identifier, runtime/build, environment, actor/data, steps, expected/actual results, conclusion, evidence, executor/independence, time, and defect.

For commands, retain working directory, full argument vector, exit status, and key original output. For interaction, retain operation/results and necessary screenshots or video. For data, retain correlation identifiers.

| Outcome | Meaning |
| --- | --- |
| PASS | Actually executed and satisfied the contract |
| FAIL | Actually executed and contradicted the contract |
| NOT_RUN | Not executed |
| BLOCKED | A specific dependency prevented execution; include its release condition |
| INCONCLUSIVE | Execution occurred but result/evidence cannot support a conclusion |
| NOT_APPLICABLE | Genuinely irrelevant, with a reason |

Starting a command, timing out, skipping, or returning an exit code does not alone explain business completion. If the harness fails, identify whether business execution was reached. Preserve old failures and version-specific outcomes.

## Repair and regression

Defects include trigger, expected/actual behavior, impact, severity, version, evidence, ownership, and retest criteria. Prioritize broken core tasks, access violations, data loss, and serious runtime failures. Do not lower required standards autonomously.

Rerun the original failure after repair, then affected direct/indirect paths. Add useful regression coverage for recurring behavioral risks; compare visual changes under equivalent conditions. Broaden testing when changes or unresolved risks justify it, not through endless identical full-suite runs.

Deferral must follow the agreed acceptance policy or an explicit decision, with impact and follow-up. It does not turn required FAIL, NOT_RUN, or INCONCLUSIVE outcomes into passes.

## Final gate

For the integrated delivery candidate:

1. Required scenarios and target environments have actual passing evidence.
2. Release blockers are resolved and required independent/human gates have their own results.
3. Agreed build, installation, configuration, startup, migration, and rollback checks are complete.
4. Instructions, source, runtime, and artifacts match; changes have not invalidated evidence.
5. Remaining limits, untested areas, and permitted deferrals are explicit.

Otherwise, hand over current work and precise recovery conditions while final acceptance remains incomplete. Packaging success does not change that conclusion.
