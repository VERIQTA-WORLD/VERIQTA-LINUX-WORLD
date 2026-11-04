# Fedora administration notes

Fedora offers rapidly evolving Linux technology through several products and deployment models. A conventional mutable installation, an Atomic desktop and a bootc-based image need different host-update decisions even when their operating-system identity is related.

## Scope and environment

The package-manager reference is the **DNF5 generation introduced with Fedora 41**, as documented in the [accepted Fedora change](https://fedoraproject.org/wiki/Changes/SwitchToDnf5). Fedora 41 is historical context, not a recommendation to install it now. Choose an actually supported release from the official lifecycle/release information at the time of installation.

The November 4, 2026 review verified the DNF5 transition and available upstream package/documentation sources, not a running Fedora VM. The portable exercise compares supplied variants using Bash and Python. Real policy/network queries require appropriate access and the relevant installed components.

## What changes in practice

### Identify the host-update model first

| Product/model | What to inspect | Administration implication |
| --- | --- | --- |
| Conventional mutable Fedora | Variant, DNF implementation and repositories | Host package operations use the supported DNF workflow |
| Fedora Atomic desktop | Actual deployment tooling and current deployment | Host image/deployment updates differ from ordinary mutable-host transactions |
| bootc-based system | Image origin, bootc deployment state and product guidance | Image build/update lifecycle governs the host |
| Fedora container | Image contents, runtime and host boundary | It does not reproduce normal host boot or full security policy |

Where those tools actually exist, `rpm-ostree status` or `bootc status` can help inspect deployment state. Their absence alone does not tell you which alternate image-management workflow applies. Installing an extra manager is not a safe way to infer or convert the model.

### Check DNF rather than assuming the binary's implementation

```bash
cat /etc/os-release
dnf --version
rpm -q bash
dnf repolist
dnf info bash
```

These queries can contact repositories or update caches. DNF4 plugins, option spelling, automatic-update units and history behavior do not all map unchanged to DNF5. Use the installed help and [DNF5 documentation](https://dnf5.readthedocs.io/en/latest/). For a conventional lab host, `dnf --assumeno upgrade bash` proposes and declines a transaction; a nonzero result after declining can be expected.

Do not apply this package-proposal step as a host-upgrade recipe on an Atomic or image-managed product. A package command within a development container can act on that container rather than the host.

### Treat release upgrades as planned maintenance

Fedora's lifecycle expects regular release transitions. Verify supported upgrade paths and release notes, spare storage and recovery access for the exact source/target. Rawhide/development branches are different study targets from a supported released product. The [official lifecycle page](https://docs.fedoraproject.org/en-US/releases/lifecycle/) is the current decision source; exact support dates are deliberately not duplicated here.

A single package version cannot establish whether an operating system is supported or whether all installed software receives updates. Third-party repositories and proprietary drivers can affect the transition independently.

### Observe security and networking

Conventional Fedora commonly uses NetworkManager, SELinux and firewalld. Inspect actual manager, domain and zone state instead of treating the default as a measurement:

```bash
nmcli device status
nmcli connection show --active
getenforce
sestatus
systemctl --failed --no-pager
```

A rootless container or user service can add distinct namespaces, labels, cgroup limits and access boundaries. Do not “fix” a mismatch by disabling SELinux or broadly granting root. Use the evidence-led [security guide](apparmor-and-selinux-overview.md).

## Follow-along lab

Create two supplied Fedora records with different variant fields:

```bash
fedora_lab=$(mktemp -d)
printf '%s\n' 'ID=fedora' 'VERSION_ID="example"' 'VARIANT_ID=workstation' > "$fedora_lab/mutable"
printf '%s\n' 'ID=fedora' 'VERSION_ID="example"' 'VARIANT_ID=silverblue' > "$fedora_lab/atomic"
python3 07-linux-distributions/labs/read_identity.py --file "$fedora_lab/mutable"
python3 07-linux-distributions/labs/read_identity.py --file "$fedora_lab/atomic"
printf '%s\n' \
  'Both identity hints are Fedora/RPM-related' \
  'Variant values differ; actual deployment tooling still needs observation' \
  'No package transaction is authorized by the family hint' \
  > "$fedora_lab/review.txt"
cat "$fedora_lab/review.txt"
```

Expect the same family hint and preserved workstation/silverblue variant values. These are teaching fixtures, not proof of any particular real image's fields or current product naming. The helper intentionally selects no host-update command.

## Verification and limits

On a real system, verify exact release, supported lifecycle, variant, update/deployment manager, repository/image origin and security/network state. Explain which commands target the host versus a container or deployment image.

No Fedora image was installed, no manager transition performed and no major upgrade exercised. Syntax and fixture checks do not establish Linux behavior or current support. See the [validation record](VALIDATION.md).

## Cleanup

```bash
rm -i -- "$fedora_lab/mutable" "$fedora_lab/atomic" "$fedora_lab/review.txt"
rmdir -- "$fedora_lab"
```

## References

- [Fedora DNF5 transition](https://fedoraproject.org/wiki/Changes/SwitchToDnf5) and [DNF5 packages](https://packages.fedoraproject.org/pkgs/dnf5/dnf5/).
- [Fedora lifecycle](https://docs.fedoraproject.org/en-US/releases/lifecycle/) and [Atomic desktops](https://fedoraproject.org/atomic-desktops/).
- [DNF5 documentation](https://dnf5.readthedocs.io/en/latest/) and [bootc documentation](https://bootc-dev.github.io/bootc/).

[Collection home](README.md) · [RHEL-family comparison](rhel-and-compatible-distributions.md)
