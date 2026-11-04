# Distribution differences quick reference

Use these tables to choose the next observation, not to skip it. Family, product, variant, release, image and administrator choices all influence the right procedure. Installed tools and a package suffix alone cannot establish the management owner or support contract.

## Scope and environment

Source review date: November 4, 2026. Tables describe common conventional models; they are not exhaustive default inventories or release compatibility certifications. Detailed reference tracks and limits are listed in the [collection home](README.md).

Actual inspection requires the corresponding Linux environment. Portable practice uses supplied identity records only and needs Bash plus Python 3.8+. No commands in this exercise install packages, switch managers or change policy.

## What changes in practice

### Common models to verify

| Product/family | Package/deployment starting point | Init/service starting point on a full system | Important exception or observation |
| --- | --- | --- | --- |
| Conventional Ubuntu | APT/dpkg | systemd | Netplan/backend ownership, Core/containers and profile enforcement differ |
| Conventional Debian | APT/dpkg | systemd on normal installations | NetworkManager/networkd/ifupdown depends on installation/configuration |
| Conventional Fedora | DNF implementation plus RPM | systemd | DNF5 generation; Atomic/image products need another host workflow |
| RHEL/Rocky/AlmaLinux conventional hosts | DNF implementation plus RPM | systemd | Exact product, repository access, certification and release policy remain distinct |
| Conventional openSUSE | Zypper/libzypp plus RPM | systemd | Leap, Tumbleweed and transactional products have different release/update models |
| Arch | pacman | systemd | Coherent rolling updates; do not construct arbitrary partial upgrades |
| Alpine | apk | Commonly OpenRC | musl/BusyBox options and binary compatibility differ from common GNU/glibc systems |
| NixOS | Declarative configuration and Nix generations | systemd | Generated configuration/activation, not arbitrary manual replacement of managed files |

### Translate operational intent

| Task | Common difference | Verify before acting |
| --- | --- | --- |
| Find a service | SSH commonly uses ssh on Debian/Ubuntu and sshd on RPM hosts | Actual installed unit, aliases and socket activation |
| Find an application package | Names and package splits differ | Repository search and file/capability provider |
| Configure networking | Netplan, NetworkManager, networkd, ifupdown or another source | Owner of the exact interface and generated configuration |
| Inspect name resolution | Local files, stub resolvers, VPN/split DNS and manager integration vary | NSS order, resolv.conf ownership and actual resolver behavior |
| Investigate denied access | Unix/ACL rules plus mandatory policy and sandboxing | Exact identity, domain/profile, object, operation and event |
| Read authentication logs | Journals, optional syslog files and forwarding vary | Installed logging stack, retention and permissions |
| Install security updates | Repository coverage, backports and frontend behavior differ | Distribution advisory, package release, origin and transaction scope |
| Plan a reboot/upgrade | Kernel, initramfs, bootloader and release tooling vary | Supported procedure for exact source/target and working console recovery |
| Run a downloaded binary | CPU architecture/level, loader, libc and libraries matter | Supported build/runtime matrix, not only “Linux” in its filename |
| Use a snapshot as rollback | Filesystem/deployment rollback may omit data or external effects | Application consistency, retained writes and supported recovery boundary |

### A read-only discovery sequence

Start with identity and scope on an authorized Linux host:

```bash
cat /etc/os-release
uname -r
uname -m
ps -p 1 -o comm=
command -v apt dnf zypper pacman apk rpm-ostree bootc
```

Some names will be missing, so command -v may return nonzero. Presence does not prove that a tool owns the host. Continue with that product's installed help, effective repositories/deployment state, manager ownership and policy queries using the detailed guide.

Write down “not observed,” “not installed,” “inactive,” “permission denied” and “not applicable” distinctly. They are not interchangeable diagnoses.

## Follow-along lab

Create two supplied conventional identity records and a comparison checklist:

```bash
compare_lab=$(mktemp -d)
printf '%s\n' 'ID=ubuntu' 'VERSION_ID="24.04"' 'ID_LIKE=debian' > "$compare_lab/first"
printf '%s\n' 'ID=fedora' 'VERSION_ID="example"' 'VARIANT_ID=server' > "$compare_lab/second"
python3 07-linux-distributions/labs/read_identity.py --file "$compare_lab/first"
python3 07-linux-distributions/labs/read_identity.py --file "$compare_lab/second"
printf '%s\n' \
  'Known from fixtures: IDs, supplied versions/variant and family hints' \
  'Unknown: actual package implementation and repository/image origins' \
  'Unknown: network/resolver owner, service units and enforcement state' \
  'Next step: observe each real disposable VM before translating a change' \
  > "$compare_lab/checklist.txt"
cat "$compare_lab/checklist.txt"
```

Expect different family hints with tool/policy state still not observed. The Fedora example version is synthetic. The checklist preserves the boundary between metadata and measured behavior.

## Verification and limits

A useful real comparison has equivalent tasks on both systems, exact versions, current official sources, observed outputs and explanations of differences. Reproduce at least one package query, service discovery, network-owner check and security-state observation on each intended VM. Do not claim tested equivalence based on these fixture files.

Tables are intentionally concise. Use [family](understanding-linux-distribution-families.md), [package](package-manager-comparison.md) and [security](apparmor-and-selinux-overview.md) explanations for context, then the relevant administration/recovery runbook for an actual change.

## Cleanup

```bash
rm -i -- "$compare_lab/first" "$compare_lab/second" "$compare_lab/checklist.txt"
rmdir -- "$compare_lab"
```

## References

- [OS identity fields](https://www.freedesktop.org/software/systemd/man/latest/os-release.html).
- [Alpine model](https://alpinelinux.org/about/), [NixOS manual](https://nixos.org/manual/nixos/stable/) and [openSUSE documentation](https://doc.opensuse.org/).
- [Debian networking alternatives](https://www.debian.org/doc/manuals/debian-reference/ch05) and [Fedora DNF5 transition](https://fedoraproject.org/wiki/Changes/SwitchToDnf5).

[Collection home](README.md) · [Validation record](VALIDATION.md)
