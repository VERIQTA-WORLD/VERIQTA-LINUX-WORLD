# Tested distribution observations

Linux execution review: November 4, 2026. The Ubuntu, Debian and conventional Fedora guides were exercised against three separately booted aarch64 cloud VMs. Identity came from each guest's actual `/etc/os-release`; managers, tools and policy were queried independently.

## Named targets and observed state

| Target | Package implementation | Network and resolver observations | Mandatory policy observation |
| --- | --- | --- | --- |
| Ubuntu 24.04.5 LTS | Actual APT/dpkg package origin/version queries and simulations | systemd-networkd managed the configured interface; authorized Netplan inspection succeeded; resolv.conf selected the resolved stub | AppArmor module and loaded profiles, including enforcing profiles, reported by aa-status |
| Debian 13.7 trixie | Actual APT/dpkg package origin/version queries and simulations | This cloud image also used systemd-networkd and the resolved stub; that is an observation of this image, not a universal Debian default | AppArmor module and loaded profiles, including enforcing profiles, reported by aa-status |
| Fedora Linux 44 Cloud Edition | DNF5 5.4.1.0, RPM queries and declined/no-op proposals | NetworkManager managed the cloud interface; this image also used the resolved stub | SELinux targeted policy was enforcing; mode was not disabled or changed |

[Exact kernels, interpreter, systemd, util-linux, logrotate and OpenSSH versions](../04-command-reference/VALIDATION.md#named-linux-environments) identify the test boundaries. Lima 2.2.1/VZ provided the booted guests without host directory mounts. Package prerequisites were installed as VM preparation. These results do not describe a container or a desktop/Atomic image.

## What ran

- All nine supplied-data comparison exercises passed on each Linux target, including their expected output and temporary-directory cleanup.
- The identity reader passed its thirteen classification cases, eight invalid-input cases and no-shell-execution checks on each target. It also read each guest's real identity without inferring a manager or enforcement state.
- Package candidates/installed versions, applicable APT/DNF proposal behavior, actual network/resolver ownership, unit/log arrangement and available security-state interfaces were queried.
- Fedora's installed-bash proposal reported no work. A separate absent `ed` install proposal returned 1 with an explicit user-abort result and left ed uninstalled. A nonzero declined transaction is different from a repository/permission error.
- The shared host exercises reproduced systemd user failure/restart, GNU file restore, logrotate, tmpfs byte/inode exhaustion, read-only policy and alternate-fstab verification on all three products. Real trusted-key SSH sessions also passed; fixture access/trust state was restored afterward.

The Debian/Fedora networking observations reinforce why the guides tell you to discover actual ownership. Sharing a resolver implementation does not make their network profiles, repositories, release policy or support obligations interchangeable.

## Correction from real image permissions

The Ubuntu cloud image denied unprivileged `netplan get` because its generated YAML was private. The [Ubuntu guide](ubuntu-administration-notes.md) now uses authorized `sudo netplan get`, explains that boundary and retains the original file permissions. A visibility denial does not establish that networking is broken.

## Reproduce on your own named target

Read the [shared runner prerequisites](../04-command-reference/VALIDATION.md#reproduce-on-your-disposable-vm), then run from the repository root in an ordinary account on a disposable Ubuntu, Debian or conventional Fedora VM:

```bash
private_results=$(mktemp -d)
python3 tools/check_linux_exercises.py --confirm-disposable-vm \
  --report "$private_results/results.json"
```

Keep the raw report private and record the exact product/release/variant, architecture, image source, versions, privileges, observation time and cleanup. Never replace an unavailable observation with a guessed family default. The runner does not install a new manager, enable enforcement, edit resolver profiles or perform a release upgrade.

## Scope of comparison

The earlier official-source review supports the guides' documented concepts and dated release facts; it is not current commercial support verification. These VM runs add real observations for the three named cloud products, not certification for every related release or variant.

RHEL, Rocky/AlmaLinux, CentOS Stream, Fedora Atomic/bootc, openSUSE, Arch, Alpine and NixOS were not installed or runtime-validated in this pass. Related fixtures remain explicitly supplied-data exercises. No major upgrade, image deployment/rollback, network-manager transition, targeted mandatory-policy change or vendor entitlement test was performed.

The reader remains a bounded teaching parser for simple ID, ID_LIKE, VERSION_ID and VARIANT_ID values. It is not a full os-release parser or an automatic deployment-command selector. Passing its fixtures does not establish the truth of another image's identity or tool availability.

Content/syntax and local-link checks pass. External-link availability, GitHub visual rendering and independent reader reproduction are separate reviews. Use the [license](../LICENSE.md) for reuse terms; public availability does not remove its restrictions.

[Collection home](README.md) · [Content standard](../CONTENT-STANDARD.md)
