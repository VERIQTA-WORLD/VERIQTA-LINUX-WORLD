# Linux World Labs

**Learn Linux by doing it.**

Work through 83 Junior follow-along labs, from your first terminal session to evidence-based troubleshooting and verified recovery. Each numbered guide gives you a focused environment in which to understand a concept, perform an operation, inspect its effects and explain the result.

[Start JUN-001](Junior/01-Linux-Fundamentals-and-Command-Line/01.%20JUN-001%3A%20Linux%20Terminal%20Navigation.md) · [All 83 Junior labs](Junior/README.md) · [Environment](LAB-ENVIRONMENT.md) · [Safety](LAB-SAFETY.md) · [Progress](PROGRESS-TRACKER.md)

## Choose your route

| Lab range | Area | Open the material |
| --- | --- | --- |
| JUN-001–034 | Linux fundamentals and command line | [Numbered foundation guides](Junior/README.md#linux-fundamentals-and-command-line) |
| JUN-035–043 | Storage | [Numbered storage guides](Junior/README.md#storage) |
| JUN-044–057 | Networking | [Numbered networking guides](Junior/README.md#networking) |
| JUN-058–068 | Bash and automation | [Numbered scripting guides](Junior/README.md#bash-and-automation) |
| JUN-069–083 | Logs, monitoring and troubleshooting | [Category guide and all 15 labs](Junior/05-Logs-Monitoring-and-Troubleshooting/README.md) |

This index links the delivered lab files. Begin with Junior foundations or demonstrate the earlier checkpoints before selecting a later topic. For larger multi-host and architecture exercises, use the [project collection](../03-Projects/README.md), whose Junior, Mid-Level and Senior guides have their own prerequisites.

## Prepare before practicing

1. Read [environment setup](LAB-ENVIRONMENT.md) and confirm your VM, account, tools and recovery access.
2. Read [lab safety](LAB-SAFETY.md), including storage, access, process and network boundaries.
3. Open the selected lab and review its complete exercise, expected failures and cleanup before changing anything.
4. Keep a [progress and evidence record](PROGRESS-TRACKER.md); use actual results rather than copying expected output.

The introductory reference environment is Ubuntu Server 24.04 LTS. Each lab identifies its own requirements; do not assume a container, non-Linux shell or different distribution reproduces host boot, service, storage or policy behavior. JUN-071–083 also use Python 3.8+ standard-library tools for bounded supplied-data analysis and tests.

## Follow the learning cycle

**Understand → Practise → Verify → Introduce a scoped fault → Investigate → Recover → Explain.**

Your goal is to establish what the system did and why, not to collect a command history. Read command explanations, preserve meaningful nonzero statuses and compare the same acceptance operation before and after recovery. A process being active, a backup being created and a user operation succeeding are different claims.

Use the [lab standard](LAB-STANDARD.md) to understand the evidence expected from a complete exercise. Stop when prerequisites or target identity differ from the guide. Investigate that difference before adding privilege or broadening a change.

## Build useful evidence

Keep environment details, implementation decisions, actual observations, negative tests, recovery checks and cleanup records. Work with synthetic data and private lab resources. Review any shared material for secrets, personal data and repository permissions.

The new operations labs include a bounded supplied-data regression suite. Their Linux host observations, systemd user units and optional tmpfs mount exercise have separate runtime requirements; passing fixture tests does not establish those behaviors. Read the [category execution guidance](Junior/05-Logs-Monitoring-and-Troubleshooting/README.md#verify-the-exercises-from-the-repository) before running its repository checker.

## Continue learning

- [Start here](../00-start-here/README.md) for learning paths and shared preparation.
- [Foundation lessons](../01-Beginner-to-Advanced/README.md) for explanations in a 20-part sequence.
- [Command reference](../04-command-reference/README.md) for syntax, effects and compact lookup tables.
- [Troubleshooting and recovery](../05-troubleshooting-and-recovery/README.md) for symptom-driven investigation.
- [System administration](../06-system-administration/README.md) for controlled operational procedures.
- [Linux distributions](../07-linux-distributions/README.md) for environment and tooling differences.
- [Projects](../03-Projects/README.md) to combine demonstrated skills into larger systems.

Read the [license](../LICENSE.md) and [contribution guidance](../CONTRIBUTING.md) before sharing adaptations. Keep your claims tied to work you actually performed.
