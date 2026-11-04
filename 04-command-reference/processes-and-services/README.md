# Processes and services

Distinguish individual processes from managed services and read the evidence they leave.

## Detailed references

1. [Observe processes and send signals](process-management-commands.md)
2. [Inspect and control systemd services](systemctl-reference.md)
3. [Read systemd journal evidence](journalctl-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Snapshot process IDs, parents, owners, state and command names. | `ps -eo pid,ppid,user,stat,comm` | [Observe processes and send signals](process-management-commands.md) |
| Find matching process names for one owner; inspect results before acting. | `pgrep -a -u USER PATTERN` | [Observe processes and send signals](process-management-commands.md) |
| Inspect a specific PID; args may expose secrets. | `ps -p PID -o pid,ppid,stat,etime,args` | [Observe processes and send signals](process-management-commands.md) |
| List units currently marked failed. | `systemctl --failed` | [Inspect and control systemd services](systemctl-reference.md) |
| List installed service unit files and enablement. | `systemctl list-unit-files --type=service` | [Inspect and control systemd services](systemctl-reference.md) |
| Show recent status; a nonzero exit may mean inactive or failed. | `systemctl status UNIT --no-pager` | [Inspect and control systemd services](systemctl-reference.md) |
| Read the last 50 records for the current boot. | `journalctl -b --no-pager -n 50` | [Read systemd journal evidence](journalctl-reference.md) |
| Show boots retained in this journal. | `journalctl --list-boots` | [Read systemd journal evidence](journalctl-reference.md) |
| Inspect the previous retained boot. | `journalctl -b -1 --no-pager` | [Read systemd journal evidence](journalctl-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
