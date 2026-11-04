# Linux distributions

![Linux distributions](../assets/images/07-linux-distributions-cover.svg)

Learn what Linux distributions share, what they change, and how to adapt administration work without relying on a name alone. A useful comparison starts with the exact release, product variant, installation image, architecture and management model.

## Choose your path

| Learning goal | Guide | Practice |
| --- | --- | --- |
| Understand families and release models | [Distribution families](understanding-linux-distribution-families.md) | Read supplied identity records without executing them |
| Choose for a workload and learning goal | [Choosing a distribution](choosing-a-linux-distribution.md) | Reject an option that fails a required constraint |
| Work with Ubuntu | [Ubuntu administration](ubuntu-administration-notes.md) | Separate release identity from observed package/network/security state |
| Work with Debian | [Debian administration](debian-administration-notes.md) | Compare Debian identity with an Ubuntu derivative |
| Work in the enterprise RPM ecosystem | [RHEL and compatible distributions](rhel-and-compatible-distributions.md) | Compare product identity and compatibility assumptions |
| Work with Fedora | [Fedora administration](fedora-administration-notes.md) | Distinguish conventional and Atomic product variants |
| Translate package tasks | [Package-manager comparison](package-manager-comparison.md) | Map intent before choosing commands |
| Understand mandatory access control | [AppArmor and SELinux](apparmor-and-selinux-overview.md) | Combine ordinary permissions and a separate policy decision |
| Keep a compact reference | [Distribution differences](distribution-differences-quick-reference.md) | Build a comparison checklist with unknowns left visible |

Read the family guide first, then choose a distribution guide and use the package/security comparisons alongside it. These pages connect the [command references](../04-command-reference/README.md), [troubleshooting guides](../05-troubleshooting-and-recovery/README.md) and [administration runbooks](../06-system-administration/README.md).

## Baselines and claims

Source review date: **November 4, 2026**. The detailed examples discuss Ubuntu 24.04 LTS, Debian 13, RHEL 9/10 and Fedora's DNF5 generation introduced with Fedora 41. These are reference tracks, not a list of the newest or currently supported releases. In particular, an introduction release such as Fedora 41 is historical context, not a recommendation to install an unsupported image.

Check the linked release/support documentation when selecting an actual image. A product lifecycle, architecture, package repository and purchased support entitlement can each have different coverage. Do not infer that every package receives the same support merely because the release is supported.

openSUSE, Arch, Alpine and NixOS receive comparison coverage, not full installation/upgrade manuals. Image-based variants such as Ubuntu Core, Fedora Atomic desktops and bootc-based systems need their own workflows. The conventional apt/dnf examples do not automatically apply to them.

## Follow along safely

Use a disposable Linux VM for actual host observations. Containers are useful for package/userland study but do not establish a distribution's normal boot, kernel, service manager, device policy or full-host security behavior. A container can identify one distribution while running the host's kernel.

Portable exercises use Bash, Python 3.8+ and temporary files from the repository root. Each page has setup, expected observations, limitations and cleanup. The supplied identity reader handles four simple identity fields; it never sources a shell file, probes installed tools or changes a host. A family hint is a research starting point, not authority to run family-specific changes.

Read command blocks as selected checks. Uppercase tokens such as PACKAGE, UNIT and INTERFACE need verified replacements. Commands that inspect identities, logs or configuration can still expose sensitive details. Optional administrator queries are identified; the mandatory portable exercises need no root, network access or installation.

## Check the actual system

For every real comparison, record distribution ID/release/variant, kernel and architecture, package-manager implementation, repository origins, service manager, networking owner, resolver, active security policy and support source/date. Keep “not observed” separate from “absent” or “disabled.”

[Validation record](VALIDATION.md) identifies reproduced exercises and actual package, manager and policy observations on Ubuntu 24.04, Debian 13 and Fedora 44 VMs. It also states the boundaries for other products, image variants, upgrades and policy changes.

[LINUX-WORLD](../README.md) · [Content standard](../CONTENT-STANDARD.md)
