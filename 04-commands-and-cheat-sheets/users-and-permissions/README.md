# Users and permissions

Resolve identities, understand access checks and inspect administrative authorization.

## Detailed references

1. [Inspect users and groups](user-and-group-commands.md)
2. [Understand modes, ownership and access](permissions-and-ownership.md)
3. [Use sudo deliberately](sudo-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Print the effective account name. | `whoami` | [Inspect users and groups](user-and-group-commands.md) |
| Show current UID, primary group and supplementary groups. | `id` | [Inspect users and groups](user-and-group-commands.md) |
| Inspect a named identity. | `id ACCOUNT` | [Inspect users and groups](user-and-group-commands.md) |
| Inspect the object itself, including a directory’s mode. | `ls -ld -- PATH` | [Understand modes, ownership and access](permissions-and-ownership.md) |
| Print octal mode, owner and group (GNU syntax). | `stat -c "%a %U %G" -- PATH` | [Understand modes, ownership and access](permissions-and-ownership.md) |
| Give only the owner read and write access. | `chmod u=rw,go= -- FILE` | [Understand modes, ownership and access](permissions-and-ownership.md) |
| List permissions granted to your identity; may authenticate. | `sudo -l` | [Use sudo deliberately](sudo-reference.md) |
| Validate or refresh cached credentials without running a target command. | `sudo -v` | [Use sudo deliberately](sudo-reference.md) |
| Invalidate cached credentials for the applicable session. | `sudo -k` | [Use sudo deliberately](sudo-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
