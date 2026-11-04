# Networking

Inspect links, routes, sockets, name resolution and secure remote access in that order when investigating reachability.

## Detailed references

1. [Inspect interfaces, addresses and routes](ip-command-reference.md)
2. [Inspect listening and connected sockets](ss-command-reference.md)
3. [Check name resolution](dns-troubleshooting-commands.md)
4. [Use SSH and inspect connection settings](ssh-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Summarize interfaces and link state. | `ip -br link` | [Inspect interfaces, addresses and routes](ip-command-reference.md) |
| Show interface addresses including prefixes. | `ip -br address` | [Inspect interfaces, addresses and routes](ip-command-reference.md) |
| Show IPv4 routing entries. | `ip route show` | [Inspect interfaces, addresses and routes](ip-command-reference.md) |
| List listening TCP sockets using numeric addresses and ports. | `ss -ltn` | [Inspect listening and connected sockets](ss-command-reference.md) |
| List bound UDP sockets; UDP does not have TCP’s handshake states. | `ss -lun` | [Inspect listening and connected sockets](ss-command-reference.md) |
| List established TCP connections. | `ss -tn state established` | [Inspect listening and connected sockets](ss-command-reference.md) |
| Resolve through configured name services as many applications do. | `getent ahosts example.com` | [Check name resolution](dns-troubleshooting-commands.md) |
| Query IPv4 DNS data; inspect status and sections. | `dig example.com A` | [Check name resolution](dns-troubleshooting-commands.md) |
| Query IPv6 DNS data. | `dig example.com AAAA` | [Check name resolution](dns-troubleshooting-commands.md) |
| Connect after verifying the expected host identity. | `ssh USER@HOST` | [Use SSH and inspect connection settings](ssh-reference.md) |
| Use a nondefault TCP port. | `ssh -p PORT USER@HOST` | [Use SSH and inspect connection settings](ssh-reference.md) |
| Offer a specified private identity file. | `ssh -i KEY USER@HOST` | [Use SSH and inspect connection settings](ssh-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
