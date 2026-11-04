# Inspect and manage APT packages

APT resolves packages and dependencies using configured repositories. Refreshing metadata is different from installing updates. Review the proposed transaction before allowing a change.

## Environment and permissions

Debian/Ubuntu family with APT. Read-only queries normally need no root. Repository refresh, installation and removal need root and can run package-maintainer scripts or restart services. Version and repository availability vary.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `apt search NAME` | Search repository metadata. |
| `apt show PACKAGE` | Describe an available package. |
| `apt-cache policy PACKAGE` | Show installed/candidate versions and repository priorities. |
| `dpkg-query -W PACKAGE` | Inspect the local package database. |
| `sudo apt update` | Refresh metadata; does not install upgrades. |
| `apt-get -s install PACKAGE` | Simulate an installation using current metadata; no package transaction. |
| `sudo apt install PACKAGE` | Install with dependencies after transaction review. |
| `sudo apt upgrade` | Upgrade without removing installed packages. |
| `sudo apt full-upgrade` | May remove installed packages to resolve dependencies. |
| `sudo apt remove PACKAGE` | Remove the package, usually retaining configuration; purge also removes package-managed configuration. |

## Follow along

```bash
cat /etc/os-release
apt --version
apt-cache policy bash
dpkg-query -W bash
apt-get -s install bash
```

## Expected results and verification

The OS identity should be Debian-family. Policy shows the installed and candidate bash versions; simulation shows a proposal or that the package is current. Stale metadata or absent repositories can prevent resolution. No package is changed and no cleanup is required.

## Common mistakes and next checks

Use `apt-get`/`apt-cache` rather than the interactive apt interface for scripts. A simulation is not a guarantee: repositories and system state can change. Do not delete package lock files to bypass an active transaction. `autoremove` may remove packages you still depend on; read the list. Reverting a package version does not necessarily reverse data migrations.

## Authoritative references

- [Debian apt manual](https://manpages.debian.org/bookworm/apt/apt.8.en.html)
- [apt-get manual](https://manpages.debian.org/bookworm/apt/apt-get.8.en.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
