# Inspect and manage DNF packages

DNF resolves RPM packages and dependencies from enabled repositories. The `dnf` command may select DNF4 or DNF5, so determine the installed implementation before using advanced options.

## Environment and permissions

Fedora/RHEL-family Linux with DNF. Queries need no root in many environments but can refresh metadata/cache and use the network. Transactions need root and may restart services.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `dnf --version` | Identify installed implementation and version. |
| `dnf repolist` | List enabled repositories. |
| `dnf info PACKAGE` | Describe package metadata. |
| `dnf search NAME` | Search package names and descriptions. |
| `rpm -q PACKAGE` | Query installed RPM state without contacting repositories. |
| `dnf --assumeno install PACKAGE` | Resolve a proposed install and decline confirmation; may refresh cache. |
| `sudo dnf install PACKAGE` | Install package and required dependencies. |
| `sudo dnf upgrade` | Resolve system updates; review before confirming. |
| `sudo dnf remove PACKAGE` | Remove a package and possibly dependent packages. |

## Follow along

```bash
cat /etc/os-release
dnf --version
rpm -q bash
dnf info bash
dnf --assumeno install bash
```

## Expected results and verification

RPM reports the installed bash version. DNF either proposes a transaction and declines it or reports no work. A declined proposal can have a nonzero status; inspect the text. No package transaction is accepted. Cache refresh may have occurred; no package cleanup is required.

## Common mistakes and next checks

DNF4 plugins and history commands are not automatically interchangeable with DNF5. Use `dnf help` on your host. `--allowerasing` can remove packages and must not be added merely to suppress dependency failures. Transaction history is useful evidence but an undo cannot guarantee data or configuration rollback. Do not mix manual RPM dependency overrides into routine maintenance.

## Authoritative references

- [DNF command reference](https://dnf.readthedocs.io/en/latest/command_ref.html)
- [DNF5 install manual](https://dnf5.readthedocs.io/en/latest/commands/install.8.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
