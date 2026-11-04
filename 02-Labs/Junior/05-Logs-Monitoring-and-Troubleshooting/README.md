# Logs, monitoring and troubleshooting

Begin with Linux logging fundamentals, then investigate the systemd journal. You will learn to inspect recorded events, preserve their context and distinguish evidence from an unsupported explanation.

[All Junior labs](../README.md) · [Linux World Labs](../../README.md) · [Environment](../../LAB-ENVIRONMENT.md) · [Safety](../../LAB-SAFETY.md) · [Progress](../../PROGRESS-TRACKER.md)

## Follow the sequence

| Lab | Guide | Checkpoint |
| --- | --- | --- |
| JUN-069 | [Linux Logging Fundamentals](69.%20JUN-069%20%E2%80%94%20Linux%20Logging%20Fundamentals.md) | Explain logging architecture, structured events and the limits of log evidence. |
| JUN-070 | [journalctl: Investigating Linux Logs with the systemd Journal](70.%20JUN-070%20%E2%80%94%20journalctl.md) | Query the journal with the relevant boot, unit, priority and time boundary. |

## Prepare and follow along

Read each lab's prerequisites, environment, privileges, workspace and cleanup instructions before running commands. Use an ordinary account on the stated Linux environment and keep recovery access available. Return to the [Junior index](../README.md) when you need to revisit Bash, process, storage or networking foundations.

Work one step at a time. Compare actual output with expected observations, record meaningful exit statuses and distinguish supplied synthetic fixtures from observations of your machine. A log entry supports a recorded event; it does not automatically establish its cause.

## Keep evidence and verify your work

Retain your implementation, regression results, environment details and engineering report privately. Separate facts, hypotheses and remaining uncertainty. Review raw logs and generated reports for credentials or personal data before sharing permitted material.

Complete the guide's acceptance checks and verify cleanup or deliberate retention. Use the [progress guide](../../PROGRESS-TRACKER.md) to record what you can independently demonstrate.
