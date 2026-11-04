# Use sudo deliberately

`sudo` runs an authorized command as another user, usually root. Authorization comes from policy; knowing your login password does not automatically grant administrative permission.

## Environment and permissions

Linux with sudo configured. Querying policy may prompt for your password and is logged. Do not paste credentials or policy output into public reports.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `sudo -l` | List permissions granted to your identity; may authenticate. |
| `sudo -v` | Validate or refresh cached credentials without running a target command. |
| `sudo -k` | Invalidate cached credentials for the applicable session. |
| `sudo -u ACCOUNT COMMAND` | Run one authorized command as another account. |
| `sudoedit /path/to/file` | Edit via sudo policy using an unprivileged editor; the resulting file change is privileged. |
| `sudo visudo` | Edit sudo policy with syntax checking; a bad policy can break administrative access. |

## Follow along

```bash
id -u
sudo -l
sudo -u root id -u
sudo -k
```

## Expected results and verification

Your normal numeric UID is usually nonzero. If policy permits the target command, the root query prints 0. A policy denial is a valid outcome: use the lab’s authorized administrator rather than bypassing policy. `sudo -k` clears the relevant cache. No files change.

## Common mistakes and next checks

A root shell broadens the scope of accidental changes. `sudo` does not fix missing files or incorrect syntax. Shell expansions and redirection happen before sudo runs. Never grant broad `NOPASSWD: ALL` just to complete a lesson. Validate policy with `visudo -c` and retain a recovery session when changing it.

## Authoritative references

- [sudo manual](https://www.sudo.ws/docs/man/sudo.man/)
- [sudoers manual](https://www.sudo.ws/docs/man/sudoers.man/)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
