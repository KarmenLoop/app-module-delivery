# Delivery, milestone reporting, and resumption

Fit the project's existing structure. Small projects may combine short tables. A new project can keep its plan, architecture/modules, contracts, acceptance, progress, and evidence under docs/app-delivery/. Maintain one authoritative record of each fact.

## Persistent facts

Use the [Progress template](../templates/progress.md) for:

- Goal, scope, sourced decisions, verified facts, assumptions, unresolved questions.
- Source/uncommitted changes, runtime/build versions, evidence validity.
- Requirements, modules, tasks, acceptance, dependencies, completion criteria, ownership.
- Defects, failed attempts, cause hypotheses, repairs, regressions, release conditions.
- Actual commands, exit status, entry points, test identifiers, evidence locations.
- Preview resource ownership, process/session identity, startup, safe shutdown.
- Existing authority, consequential boundaries, next action, and rationale.

Keep credentials in secure configuration. Record variable names and acquisition/setup methods, not secret values. A progress label is not evidence of a currently running process or device.

## Reporting

Report business milestones and significant discoveries, direction changes, and blockers. Explain what now works, how verified, where it can be inspected, what remains, and why the next step matters. Expand the detailed ledger when requested.

Distinguish designed, implemented, integrated, actually operated, and finally accepted. Dispatch, ACTIVE labels, file counts, test counts, and author reports do not automatically establish business completion.

## Resume a session or execution environment

1. Read the latest instructions and recorded scope/authority; do not re-request ordinary already-authorized work.
2. Inspect actual files, versions, uncommitted work, and other contributors' changes. Determine affected contracts and evidence.
3. Recheck tools, environments, target devices, dependencies, previews, and resource ownership; stale process IDs do not establish ownership.
4. Determine whether the last operation took effect, especially writes, charges, sends, and remote tasks. Reconcile unknown outcomes first.
5. Mark invalidated evidence and unresolved conditions, choose a ready next task, and update the record.

Moving a project between devices requires version, configuration, data, and authority checks. Copying a skill does not transfer credentials or execution authority. Application tasks recover through their actual application contracts.

## Waiting and scheduling

Record the awaited condition, reason, observable source, release condition, and next action. Block dependent branches only. Timing follows urgency, available feedback, and capabilities rather than a universal interval.

When future work is requested and genuine scheduling is available and authorized, use it with the user's notification preferences. Notify meaningful changes, completion, failure, or required action. Without scheduling, retain a recovery point and state the actual limitation.

## Final handoff

Deliver according to scope:

- Source, directory index, and agreed installation/release artifacts matching acceptance.
- Application plan, module/interface/data/access/platform documentation, design rationale.
- Environment versions, dependencies, configuration examples, startup/shutdown, actual entry points.
- Safe test-account access, isolated fixtures, applicable cleanup.
- Maintenance, backup, migration, upgrade, cutover, and supported rollback prerequisites.
- Acceptance, commands, interaction/data evidence, defects and regression records.
- Untested targets, external dependencies, limitations, and maintenance ownership.

Use concrete natural English for repository descriptions, README files, and commits unless instructed otherwise. Product content follows the required user language. Avoid unsupported capability and production-readiness claims.

Follow the instructions in an isolated directory or agreed environment to establish setup, startup, and a core operation. Build, installation, runtime, and publication remain separate facts. Existing explicit authorization governs publication or production changes; prepare reviewable artifacts before asking for any missing final authority.

## Version and package consistency

Create inventories/checksums when useful. Exclude credentials, sessions, runtime databases, dependencies, and unrelated private material. Read archive members and compare bytes and CRC. Revalidate affected checks after artifact changes.

Code rollback and data rollback have different prerequisites. An older installer alone does not prove reversibility. If required acceptance remains incomplete, deliver current work with its exact limits and recovery conditions.
