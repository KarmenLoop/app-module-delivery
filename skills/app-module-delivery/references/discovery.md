# Discovery: a 72-question candidate library

## Interview rules

Read existing materials and answers first. Summarize what is known and the current decision gap, then ask 4–6 useful questions with options, a recommendation, and tradeoffs. Respect smaller host question limits. Prioritize core value, expensive later changes, and immediate dependencies.

This library serves future application projects. It is not a 72-question prerequisite. Users decide business facts, scope, preferences, and commitments. The agent verifies source, configuration, interfaces, environments, and available tools, and recommends technical choices. Label reversible assumptions; do not infer consequential authorization from a default option.

After each round, record confirmed decisions, verified facts, provisional assumptions, and unresolved items. Resolve contradictions using their actual sources. Identify the affected flow, responsible party, and release condition for missing information; continue independent work.

## A. Goals, audience, and scope

1. Q01 Who uses the application, what problem matters most, and what does the current process cost?
2. Q02 Is this greenfield development, an extension, a module change, or a narrow repair? What behavior must remain?
3. Q03 What observable business outcomes define success?
4. Q04 What is required now, explicitly excluded, or deferred? What deadlines and resource constraints apply?
5. Q05 What industry, regions, languages, expertise, operating contexts, and accessibility needs matter?
6. Q06 Who decides business rules, design direction, and acceptance? Is independent QA or human acceptance already required?

## B. User tasks and scenarios

7. Q07 Describe the most important complete use: entry point, actions, and final outcome.
8. Q08 What are each role's frequent tasks, and which flow should work first?
9. Q09 What data, configuration, invitations, approvals, or devices must exist before starting?
10. Q10 Does work pass between modules, applications, people, or devices? What context must travel?
11. Q11 Which actions are costly, difficult to undo, affect other people, or fail inconspicuously?
12. Q12 What should people see on first use, during daily use, and when returning?

## C. Business rules and state

13. Q13 What calculations, validations, limits, time rules, or approvals apply, and what establishes them?
14. Q14 What states exist, and who may perform each transition under which conditions?
15. Q15 How should duplicate actions, duplicate records, concurrent edits, and batch operations behave?
16. Q16 Should partial failure roll back the batch or allow partial success? Which changes are atomic?
17. Q17 What happens to completed or committed work after cancellation, timeout, undo, or retry?
18. Q18 What receipts, history, audit, notifications, or fulfillment are required, and when is business completion reached?

## D. Data and files

19. Q19 What entities, fields, relationships, and files exist? Which are supplied and which are created?
20. Q20 Where does data originate, who owns it, what is authoritative, and who can change it?
21. Q21 Is data local, on an organization server, in the cloud, or mixed? What may leave a device?
22. Q22 What volume, size, format, search, ordering, relationships, and import/export requirements apply?
23. Q23 What retention, deletion, withdrawal, trash, backup, and recovery behavior is required?
24. Q24 How must existing data migrate? Must versions coexist, and may formats or historical meaning change?

## E. Identity, authorization, and organizations

25. Q25 Are accounts and sign-in necessary? How do personal and organizational use differ?
26. Q26 What roles, organizations, tenants, and workspaces exist, and who may do what to which resources?
27. Q27 How are resources created, owned, shared, transferred, or governed by inherited access?
28. Q28 What happens to running actions and local data after session expiry, membership changes, or revocation?
29. Q29 Which actions need confirmation, approval, or an audit record, and how is the actor established?
30. Q30 Which personal data, credentials, or sensitive content need special storage, display, export, and logging behavior?

## F. Modules and dependencies

31. Q31 What business capabilities are needed, and which already exist, are shared, or must be added?
32. Q32 What result does each module own, and which responsibilities belong elsewhere?
33. Q33 What data, commands, results, or events cross module interfaces?
34. Q34 Which modules require identity, configuration, network, storage, background processes, or external services?
35. Q35 Must capabilities be exposed to plugins, SDKs, other teams, or third parties? What compatibility is promised?
36. Q36 Should downstream work wait, reject, degrade, or take an alternative path when a dependency is unavailable?

## G. Targets and system capabilities

37. Q37 Which desktop, mobile, web, and CLI environments are supported, including OS versions, architectures, and devices?
38. Q38 Which tasks must work on each target, and which capabilities may be limited or unsupported?
39. Q39 Are files, camera, microphone, notifications, clipboard, connected devices, or other system capabilities required?
40. Q40 Are multiple windows, drag-and-drop, shortcuts, touch, external keyboards, or system sharing required?
41. Q41 Should tasks continue, stop, suspend, or recover after backgrounding, window closure, suspension, or process exit?
42. Q42 How can people continue after permission denial, unsupported hardware, or temporary capability loss?

## H. Offline use, synchronization, and continuity

43. Q43 Is offline use required? What remains executable, read-only, or queued?
44. Q44 Is synchronization needed, what is synchronized, who enables it, and where does it go?
45. Q45 How are concurrent edits detected, presented, and resolved?
46. Q46 How are disconnection, duplicate delivery, reordered messages, and partial synchronization reconciled?
47. Q47 What tasks, drafts, selections, and results follow people across devices, and what stays device-local?
48. Q48 How do people distinguish local persistence, remote synchronization, and business processing completion?

## I. Backends, services, and devices

49. Q49 What backends, storage, identity systems, device protocols, or external interfaces exist, and who supplies access details?
50. Q50 Should integration use stand-ins, a sandbox, or a live service? What authorization and test conditions exist?
51. Q51 What costs, quotas, concurrency limits, and network restrictions apply?
52. Q52 Can the original operation be queried after a timeout or unknown outcome to prevent repeated side effects?
53. Q53 Which external results are necessary for completion, and which can be retried or compensated later?
54. Q54 Who maintains integration changes, disabled services, and expired credentials, and how do users recover?

## J. UI/UX, navigation, and interaction

55. Q55 What is the primary workspace and action: finding, editing, approving, creating, or monitoring work?
56. Q56 Which mature products or references are useful, and which specific task behaviors fit or do not fit?
57. Q57 What brand, typography, color, icon, theme, density, and writing constraints apply?
58. Q58 What navigation, search, recents, filtering, panes, batch actions, and quick entry points are needed?
59. Q59 How should loading, saving, execution, completion, partial success, errors, emptiness, and denied access be explained?
60. Q60 What motion, keyboard, touch, screen-reader, text-scaling, and window-adaptation requirements apply?

## K. Performance, reliability, and observation

61. Q61 What typical and maximum data volumes, concurrency, batch sizes, and long-running scenarios matter?
62. Q62 What startup, response, throughput, memory, storage, or energy targets are acceptable?
63. Q63 Which interruptions, crashes, write failures, full-storage conditions, or dependency outages must recover, and what loss is permitted?
64. Q64 Where can users and maintainers observe tasks, status, error details, and diagnostics?
65. Q65 How long are histories, logs, and diagnostic records retained, and what must be redacted?
66. Q66 What compatibility or availability commitments exist, and how will actual workloads establish them?

## L. Engineering, acceptance, and handoff

67. Q67 What existing engineering, technology, and maintenance constraints are fixed, and where are project rules and environments?
68. Q68 What implementation, execution, device, external-test, and delivery actions are authorized, and what confirmation gates were requested?
69. Q69 Which normal, failure, permission, and recovery scenarios must actually pass, and how is test data prepared?
70. Q70 Which systems, devices, and environments provide acceptance evidence, and who supplies missing conditions?
71. Q71 Are source, installable packages, instructions, migration, deployment preparation, or actual publication required?
72. Q72 Who maintains and upgrades the result, and what handoff, rollback, remaining-work, and resumption records are needed?

## Convert answers into a plan

For consequential information, retain the item, conclusion, source, status, affected scope, responsible party, and resolution condition. Keep credentials in secure configuration rather than interview or progress records.

Define scenarios and the business model before deriving modules, data, permissions, and interfaces. Use the [Application plan](../templates/application-plan.md), mapping each requirement to implementation and acceptance. Explain inapplicability when a project has no UI, account, synchronization, or external service.
