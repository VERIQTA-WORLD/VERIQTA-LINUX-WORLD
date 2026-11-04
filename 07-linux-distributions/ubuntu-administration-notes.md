# Ubuntu administration notes

Ubuntu shares Debian-related packaging but has its own repositories, release/coverage policy, cloud images and defaults. Learn the management owner before changing configuration, particularly for networking and generated cloud settings.

## Scope and environment

The conventional Ubuntu Server reference track is **24.04 LTS**. This is a named study baseline, not a newest-release claim or evidence of VM execution. Desktop, cloud, minimal containers, WSL and Ubuntu Core can differ. Core's snap/image administration is outside this conventional APT host guide.

Host inspection needs an authorized Linux environment with the named tools; some security details require sudo. The portable lab uses only Bash, Python 3.8+ and temporary supplied metadata. Check [Ubuntu's current coverage information](https://ubuntu.com/about/release-cycle) for the exact release, package scope and entitlement when choosing a deployment.

## What changes in practice

### Packaging and updates

APT resolves dependency/repository operations; dpkg records installed packages. Inspect origins and candidate versions instead of treating every available package as equally maintained:

```bash
cat /etc/os-release
apt --version
apt-cache policy bash
dpkg-query -W bash
dpkg --print-architecture
```

An optional `apt-get -s install --only-upgrade bash` previews a transaction using current metadata. It installs nothing, and stale metadata or access differences can limit it. Do not mix Debian release repositories or another Ubuntu release merely to obtain a newer package. Follow the supported release-upgrade process separately from routine package maintenance.

### Networking and DNS

Netplan describes network configuration and renders to a backend such as systemd-networkd or NetworkManager. Server/desktop/image choices influence which backend owns an interface. Netplan's configuration and the backend's current state answer different questions. See [Ubuntu networking documentation](https://documentation.ubuntu.com/server/explanation/networking/configuring-networks/).

Useful selected checks, only where the tool is installed:

```bash
netplan get
networkctl status
nmcli device status
ls -l /etc/resolv.conf
resolvectl status
```

A missing/inactive manager is not automatically a failure if another component owns the connection. Cloud-init or image automation can generate networking. Editing generated files or changing renderers over SSH without console recovery can disconnect access. Inspect sources/owners and the real interface before planning a change.

### Services, access and security

A conventional host uses systemd, but a container/WSL arrangement may not provide a running manager. Discover SSH unit and socket names rather than assuming the same activation path everywhere:

```bash
systemctl list-unit-files 'ssh*' --no-pager
systemctl list-sockets --all --no-pager
```

AppArmor is installed/loaded by default on standard Ubuntu according to [Ubuntu's AppArmor guide](https://ubuntu.com/server/docs/how-to/security/apparmor/); actual profile enforcement must still be checked. `sudo aa-status` inspects policy state. The UFW frontend may be available, but installed does not mean active or complete network protection. Use the [security comparison](apparmor-and-selinux-overview.md) and inspect actual host/cloud policy.

## Follow-along lab

Create a conventional Ubuntu identity fixture and inspect only its identity hints:

```bash
ubuntu_lab=$(mktemp -d)
printf '%s\n' 'ID=ubuntu' 'ID_LIKE=debian' 'VERSION_ID="24.04"' 'VARIANT_ID=server' \
  > "$ubuntu_lab/os-release"
python3 07-linux-distributions/labs/read_identity.py --file "$ubuntu_lab/os-release"
printf '%s\n' \
  'Package implementation: not observed' \
  'Network owner and resolver: not observed' \
  'AppArmor profiles and enforcement: not observed' \
  'SSH unit/socket and coverage: not observed' \
  > "$ubuntu_lab/observations.txt"
cat "$ubuntu_lab/observations.txt"
```

Expect Debian-related, the supplied release/variant and not-observed tool/policy state. The variant is a supplied exercise value, not a claim that every real Ubuntu image includes VARIANT_ID=server. On a real authorized VM, use the read-only checks above and replace unknowns only with actual evidence.

## Verification and limits

Record identity separately from installed tool versions, active managers, repository origins, profile enforcement and support coverage. A successful apt query does not establish normal boot/service behavior inside a container. A valid Netplan configuration does not prove the remote client path works after activation.

Actual changes belong in the [configuration/rollback](../06-system-administration/configuration-changes-and-rollback.md) and [maintenance](../06-system-administration/patching-and-maintenance.md) workflows. No network, repository, security or service change is part of this lab.

## Cleanup

```bash
rm -i -- "$ubuntu_lab/os-release" "$ubuntu_lab/observations.txt"
rmdir -- "$ubuntu_lab"
```

## References

- [Ubuntu Server documentation](https://documentation.ubuntu.com/server/) and [release coverage](https://ubuntu.com/about/release-cycle).
- [Network configuration](https://documentation.ubuntu.com/server/explanation/networking/configuring-networks/) and [AppArmor](https://ubuntu.com/server/docs/how-to/security/apparmor/).
- [APT reference](../04-command-reference/packages/apt-reference.md).

[Collection home](README.md) · [Debian comparison](debian-administration-notes.md)
