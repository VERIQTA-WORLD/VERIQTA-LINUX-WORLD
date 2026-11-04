# Inspect and control systemd services

`systemctl` communicates with systemd. A unit describes a managed resource. A service’s current activity and its boot enablement are independent states.

## Environment and permissions

A Linux VM booted with systemd. Minimal containers, chroots and some WSL installations may not provide a running system manager. Inspection is usually unprivileged; system service changes need authorization.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `systemctl --failed` | List units currently marked failed. |
| `systemctl list-unit-files --type=service` | List installed service unit files and enablement. |
| `systemctl status UNIT --no-pager` | Show recent status; a nonzero exit may mean inactive or failed. |
| `systemctl cat UNIT` | Show unit definition and drop-ins; may expose configuration details. |
| `systemctl is-active UNIT` | Query current activity. |
| `systemctl is-enabled UNIT` | Query boot enablement; static units can still be activated by dependencies. |
| `sudo systemctl start UNIT` | Start now; does not enable at boot. |
| `sudo systemctl enable UNIT` | Configure boot/dependency activation; does not start now. |
| `sudo systemctl restart UNIT` | Stop then start, interrupting service. |
| `sudo systemctl daemon-reload` | Reload unit definitions; does not reload application configuration. |

## Follow along

Read-only walkthrough; discover names rather than guessing a production unit:

```bash
systemctl --version
systemctl --failed --no-pager
systemctl list-unit-files --type=service --no-pager
systemctl show systemd-journald.service -p LoadState -p ActiveState -p SubState
systemctl status systemd-journald.service --no-pager
```

## Expected results and verification

On a typical systemd VM the journal service is loaded and active. Actual state is host-specific. An empty failed-unit list is useful but does not establish application health. Nothing was changed, so no cleanup is needed.

## Common mistakes and next checks

SSH may be named `ssh.service` or `sshd.service`. `reload` requires application support; `daemon-reload` serves a different purpose. Before a restart, validate configuration, inspect dependencies, define rollback and check console access. Verify both unit state and a real client request after changes.

## Authoritative references

- [systemctl manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
