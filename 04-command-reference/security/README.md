# Security

Inspect effective access and active filtering policy. Design host-specific changes with a recovery path.

## Detailed references

1. [Inspect account and access evidence](access-audit-commands.md)
2. [Inspect firewall policy and plan changes](firewall-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Show your effective identity and groups. | `id` | [Inspect account and access evidence](access-audit-commands.md) |
| Enumerate accounts exposed by configured identity sources; enumeration may be incomplete. | `getent passwd` | [Inspect account and access evidence](access-audit-commands.md) |
| Inspect one common Debian-family administrator group. | `getent group sudo` | [Inspect account and access evidence](access-audit-commands.md) |
| UFW: inspect status and rules. | `sudo ufw status verbose` | [Inspect firewall policy and plan changes](firewall-reference.md) |
| UFW: inspect rule numbering; numbers change after deletion. | `sudo ufw status numbered` | [Inspect firewall policy and plan changes](firewall-reference.md) |
| firewalld: check daemon state. | `sudo firewall-cmd --state` | [Inspect firewall policy and plan changes](firewall-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
