# Logs, monitoring and troubleshooting

Work through 15 follow-along labs, JUN-069–083. You will move from logging and journal investigation into resource monitoring, combine observations into health checks, then investigate controlled faults and prove recovery.

[All Junior labs](../README.md) · [Linux World Labs](../../README.md) · [Environment](../../LAB-ENVIRONMENT.md) · [Safety](../../LAB-SAFETY.md) · [Progress](../../PROGRESS-TRACKER.md)

## Prepare your environment

Use an ordinary account on a disposable Ubuntu Server 24.04 LTS reference VM, GNU Bash 5.x and the tools named by each lab. JUN-071–083 use Python 3.8+ from the standard library for bounded evidence analyzers and regression tests. Keep console access for host-level experiments. Complete the Bash prerequisites and read each lab’s own requirements before beginning.

JUN-069 and JUN-070 teach the logging foundations used throughout this category. Continue in order unless you can demonstrate the checkpoint for the prerequisite material. Earlier file, identity, process, storage and networking skills remain important; use the [Junior index](../README.md) to return to a specific foundation.

## Follow the sequence

| Lab | Open the guide | Checkpoint |
| --- | --- | --- |
| JUN-069 | [Linux Logging Fundamentals](69.%20JUN-069%20%E2%80%94%20Linux%20Logging%20Fundamentals.md) | Explain logging architecture, structured events and the limits of log evidence. |
| JUN-070 | [journalctl: Investigating Linux Logs with the systemd Journal](70.%20JUN-070%20%E2%80%94%20journalctl.md) | Query the journal with the relevant boot, unit, priority and time boundary. |
| JUN-071 | [Reading System Logs](71.%20JUN-071%20%E2%80%94%20Reading%20System%20Logs.md) | Correlate recorded events without inventing causation or mixing boots. |
| JUN-072 | [Basic CPU Monitoring](72.%20JUN-072%20%E2%80%94%20Basic%20CPU%20Monitoring.md) | Calculate comparable interval CPU use and preserve idle, wait and steal distinctions. |
| JUN-073 | [Memory Monitoring](73.%20JUN-073%20%E2%80%94%20Memory%20Monitoring.md) | Distinguish available memory, swap occupancy and task pressure. |
| JUN-074 | [Disk Monitoring](74.%20JUN-074%20%E2%80%94%20Disk%20Monitoring.md) | Identify the filesystem, ordinary-user block availability and inode limits. |
| JUN-075 | [Process Monitoring](75.%20JUN-075%20%E2%80%94%20Process%20Monitoring.md) | Compare the same process instance and retain exit/PID-reuse uncertainty. |
| JUN-076 | [Basic Network Monitoring](76.%20JUN-076%20%E2%80%94%20Basic%20Network%20Monitoring.md) | Calculate scoped interface rates without claiming application health. |
| JUN-077 | [Linux System Health Checks](77.%20JUN-077%20%E2%80%94%20Linux%20System%20Health%20Checks.md) | Combine fresh required checks while keeping failures and unknowns visible. |
| JUN-078 | [Basic Linux Troubleshooting](78.%20JUN-078%20%E2%80%94%20Basic%20Linux%20Troubleshooting.md) | Investigate a wrong-content fault and verify the same operation after repair. |
| JUN-079 | [Troubleshooting a Failed Service](79.%20JUN-079%20%E2%80%94%20Troubleshooting%20a%20Failed%20Service.md) | Separate config validation, manager state and application acceptance. |
| JUN-080 | [Troubleshooting Permission Problems](80.%20JUN-080%20%E2%80%94%20Troubleshooting%20Permission%20Problems.md) | Reproduce read/traverse denial and restore only the required access. |
| JUN-081 | [Troubleshooting Disk Space Problems](81.%20JUN-081%20%E2%80%94%20Troubleshooting%20Disk%20Space%20Problems.md) | Distinguish space, inode, quota and read-only constraints before cleanup. |
| JUN-082 | [Troubleshooting SSH Problems](82.%20JUN-082%20%E2%80%94%20Troubleshooting%20SSH%20Problems.md) | Locate the failed SSH boundary while preserving server identity verification. |
| JUN-083 | [Troubleshooting Network Connectivity](83.%20JUN-083%20%E2%80%94%20Troubleshooting%20Network%20Connectivity.md) | Distinguish TCP, HTTP and content acceptance with bounded local faults. |

## Learn in three stages

1. **Observe and explain, JUN-069–076.** Establish source, host, boot, identity, units and sample interval. A counter or log line is evidence within a boundary, not a complete diagnosis.
2. **Combine evidence, JUN-077–078.** Define the user operation, distinguish fresh failure from unknown or stale results, and choose checks that discriminate competing explanations.
3. **Investigate and recover, JUN-079–083.** Reproduce one controlled fault at a time, preserve the healthy baseline, repair the exact resource and repeat the original acceptance operation.

Your new tools have distinct jobs: timeline ordering, counter calculations, headroom checks, evidence summaries and troubleshooting records. They are deliberately limited learning tools. Do not use a fixture result as a claim that a real host is healthy.

## Follow along deliberately

Read each exercise before running it, including expected failures and cleanup. Create the unique workspace named in the lab, run one step at a time and compare actual observations with expected results. Preserve the raw evidence privately and write conclusions in your own words.

The new analyzer projects accept bounded JSON evidence, distinguish normal, attention and invalid-input outcomes, and include subprocess regression tests. The schema and interpretation are explained in each guide. Shared validation conventions let you concentrate on the new Linux concept rather than inventing a different error contract in every lab.

Actual Linux observations can differ from the supplied synthetic fixtures. Record absent tools, denied visibility and unsupported interfaces rather than substituting zero. The optional systemd user-service and tmpfs exercises require their stated Linux environment; portable fixture tests cannot establish those behaviors. The loopback test requires permission to create local listeners and never needs a public bind address.

## Build your evidence set

Keep your scripts, fixtures, regression output, environment details and engineering report for each lab. Your report should identify the failing operation, facts, alternative hypotheses, selected check, repair or revised interpretation, repeated acceptance results and cleanup or retained resources.

Do not publish raw authentication logs, keys, tokens, customer data or unreviewed process/network captures. Follow the repository’s [permissions](../../../LICENSE.md) when sharing adapted content.

## Verify the exercises from the repository

If you are reviewing the authored examples, inspect the runner first. It executes marked private-workspace exercises and analyzer tests, including bounded loopback children in JUN-083. It excludes live Linux observations, systemd changes, mounts, sudo and remote SSH connections.

```bash
python3 tools/check_junior_operations_labs.py --static-only
python3 tools/check_junior_operations_labs.py
```

Run these commands from the repository root. Use `--lab 71` through `--lab 83` for one new lab, or `--skip-loopback` when local listeners are prohibited; the output identifies that exclusion. A static pass proves structure, links and syntax, not Linux runtime behavior.

## Finish the category

You are ready to continue when you can explain the 15 checkpoints, independently reproduce the relevant exercises, reject malformed evidence, diagnose at least one controlled fault and show verified recovery and cleanup. Use the [progress guide](../../PROGRESS-TRACKER.md) to record demonstrated work, rather than treating page count as mastery.
