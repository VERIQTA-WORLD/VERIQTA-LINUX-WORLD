# Senior Linux portfolio projects

Design connected Linux systems, test their failure boundaries and defend your operating decisions with evidence. These ten projects connect architecture, high availability, Kubernetes, identity, observability, recovery, security, automation, performance and incident response.

[All projects](../README.md) · [Mid-Level projects](../02.%20Mid-Level/README.md) · [Project workflow](../project-workflow.md)

## Before you begin

You should be able to administer a Linux host, troubleshoot a multi-host service, use SSH and sudo deliberately, inspect logs and resource pressure, and restore data from a verified backup. Read each project’s prerequisites for additional knowledge, VM counts, memory, storage, networking and tools. The infrastructure architecture capstone combines skills from the preceding projects.

Use dedicated disposable VMs with console access, isolated lab networks and a reset route. A collection of VMs on one physical host still shares that host’s failure domain. Never transfer failure-injection or teardown commands to an existing production environment.

## Choose a project

| Project | Focus | Evidence to demonstrate |
| --- | --- | --- |
| [Enterprise High-Availability Linux Infrastructure](01.%20Portfolio%20Project%2001%3A%20Enterprise%20High-Availability%20Linux%20Infrastructure.md) | High-Availability Linux Infrastructure | Measure request failures and recovery during backend and load-balancer faults; identify shared failure domains. |
| [Production Kubernetes Infrastructure on Linux](02.%20Portfolio%20Project%2002%3A%20Production%20Kubernetes%20Infrastructure%20on%20Linux.md) | Production Kubernetes Infrastructure on Linux | Verify workload access, authorization, networking and storage; distinguish workload recovery from control-plane availability. |
| [Enterprise Linux Identity & Access Platform](03.%20Portfolio%20Project%2003%3A%20Enterprise%20Linux%20Identity%20%26%20Access%20Platform.md) | Linux Identity & Access Platform | Test allowed and denied operations, identity lifecycle and revocation while preserving recovery access. |
| [Linux Observability Platform](04.%20Portfolio%20Project%2004%3A%20Linux%20Observability%20Platform.md) | Linux Observability Platform | Connect a workload symptom to metrics and logs, exercise an alert and verify signal recovery. |
| [Enterprise Linux Disaster Recovery Architecture](05.%20Portfolio%20Project%2005%3A%20Enterprise%20Linux%20Disaster%20Recovery%20Architecture.md) | Linux Disaster Recovery Architecture | Restore application and database state, measure recovery time and account for data loss and dependencies. |
| [Zero-Trust Linux Infrastructure](06.%20Portfolio%20Project%2006%3A%20Zero-Trust%20Linux%20Infrastructure.md) | Zero-Trust Linux Infrastructure | Test segmentation, identity, policy and revocation from both permitted and denied paths. |
| [Enterprise Linux Automation Platform](07.%20Portfolio%20Project%2007%3A%20Enterprise%20Linux%20Automation%20Platform.md) | Linux Automation Platform | Validate configuration, constrain rollout scope, explain drift and verify convergence and rollback. |
| [Linux Performance Engineering Platform](08.%20Portfolio%20Project%2008%3A%20Linux%20Performance%20Engineering%20Platform.md) | Linux Performance Engineering Platform | Compare repeatable baselines and experiments; support bottleneck conclusions with correlated measurements. |
| [Production Linux Incident Simulation](09.%20Portfolio%20Project%2009%3A%20Production%20Linux%20Incident%20Simulation.md) | Production Linux Incident Simulation | Keep a timed decision log, diagnose controlled faults and verify sustained service recovery. |
| [Enterprise Linux Infrastructure Architecture](10.%20Portfolio%20Capstone%20Project%2010%3A%20Enterprise%20Linux%20Infrastructure%20Architecture.md) | Linux Infrastructure Architecture | Integrate application, data, access, observability, automation and recovery decisions into a defensible architecture. |

## Work with explicit gates

Use the [shared project workflow](../project-workflow.md) to check prerequisites, implement in verified stages, test normal and denied operations, recover from one controlled fault at a time and verify cleanup. Each guide’s opening navigation links to its own detailed procedures.

Before failure injection, preserve a healthy baseline and define an impact limit and recovery trigger. Restore healthy state between experiments. Record topology, versions, assumptions, measurements and observed limits; a lab result does not establish production availability or professional seniority.

## Finish with reproducible evidence

Keep sanitized architecture notes, implementation decisions, passing and failing acceptance results, an incident timeline, recovery measurements and final cleanup or retained-state records. Review working-tree changes before publishing; do not include private keys, tokens, kubeconfig credentials, backup passwords or real customer data.

[All projects](../README.md) · [System administration](../../06-system-administration/README.md) · [Troubleshooting](../../05-troubleshooting-and-recovery/README.md)
