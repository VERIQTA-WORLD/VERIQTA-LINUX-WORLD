# RHEL and compatible distributions

The enterprise RPM ecosystem shares many concepts: RPM package metadata, DNF-family dependency management, systemd, NetworkManager and SELinux. Shared concepts do not make products interchangeable for every package, hardware driver, support contract or certification.

## Scope and environment

Reference tracks are **RHEL 9 and 10** and related enterprise distributions whose own documentation must be checked for their exact major release. Conventional mutable hosts are the target; image-based/bootc products need their product workflow.

Host observations require authorized access. Some policy, subscription and firewall queries require privileges and may reveal private system identifiers. The portable lab compares supplied identities only and creates no actual enterprise instance or subscription.

## What changes in practice

### Establish the exact product and coverage

| Product context | What to establish | What not to assume |
| --- | --- | --- |
| RHEL | Product, major/minor release, architecture, repositories and applicable support/entitlement | Every installed third-party package shares vendor coverage |
| Rocky Linux | Exact release, project support policy, upgrade and compatibility documentation | A RHEL vendor certification automatically transfers |
| AlmaLinux | Exact release, compatibility target, project support and package policies | All hardware/build details match every related image |
| CentOS Stream | Stream version, lifecycle and continuously delivered relationship to RHEL development | It is the old downstream CentOS Linux release model |

[CentOS describes Stream](https://www.centos.org/centos-stream/) as tracking just ahead of RHEL development, between Fedora and RHEL. Use the product's actual policy rather than a simplified diagram as a support guarantee. Consult [Rocky documentation](https://docs.rockylinux.org/) and [AlmaLinux documentation](https://wiki.almalinux.org/) for their own claims and procedures.

### Query packages and repositories

```bash
cat /etc/os-release
uname -m
rpm -q bash
dnf --version
dnf repolist
dnf info bash
```

Identify the installed DNF implementation; Fedora's DNF5 history does not prove the implementation on a particular RHEL-related image. Repositories and plugins may be managed by subscriptions, cloud providers or provisioning. Query effective repository state and the origin of candidate packages instead of assuming one filename fully describes it.

On an actual registered RHEL system, authorized subscription-manager queries may help explain content access. They do not apply identically to downstream products, and a status string alone may not establish contractual support or package coverage. Keep consumer IDs, organization details and credentials private.

A major-release upgrade is not a routine `dnf upgrade`. Check supported source/target paths, hardware/CPU requirements, removed features and migration tooling in the exact release documentation. Never mix repository major versions to imitate an upgrade.

### Inspect networking, firewall and mandatory policy

Conventional installations commonly use NetworkManager; identify actual connection ownership before editing profiles:

```bash
nmcli general status
nmcli connection show --active
ip -br address
ls -l /etc/resolv.conf
getenforce
sestatus
```

A tool being installed is not proof it owns all interfaces or enforcement decisions. On systems using firewalld, `sudo firewall-cmd --get-active-zones` and an exact zone inspection describe runtime policy; saved permanent policy is separate. Do not enable an unfamiliar firewall frontend over the existing rules.

RHEL documents SELinux enforcing as its normal installed default, but inspect the actual host and confined domain. A denial can involve labels, booleans, port types, ordinary access or application sandboxing. Disabling enforcement is not a substitute for investigating the specific access decision. See [SELinux/AppArmor comparison](apparmor-and-selinux-overview.md).

### Discover service and log behavior

`sshd.service` is common, but discover the installed unit and any sockets. Optional syslog files, journal retention and authentication integration depend on the image/packages. Backported security fixes mean upstream version numbers alone do not establish whether a distribution package is vulnerable; use its advisory and package-release information.

## Follow-along lab

Compare RHEL and a Rocky-like fixture without assuming identical product coverage:

```bash
enterprise_lab=$(mktemp -d)
printf '%s\n' 'ID=rhel' 'ID_LIKE=fedora' 'VERSION_ID="9.example"' > "$enterprise_lab/rhel"
printf '%s\n' 'ID=rocky' 'ID_LIKE="rhel centos fedora"' 'VERSION_ID="9.example"' > "$enterprise_lab/rocky"
python3 07-linux-distributions/labs/read_identity.py --file "$enterprise_lab/rhel"
python3 07-linux-distributions/labs/read_identity.py --file "$enterprise_lab/rocky"
printf '%s\n' \
  'Shared: Enterprise RPM-related family hint' \
  'Separate evidence needed: actual release, repository origin, hardware, application certification and coverage' \
  > "$enterprise_lab/review.txt"
cat "$enterprise_lab/review.txt"
```

Expect both hints to be Enterprise RPM-related while IDs remain rhel and rocky. The version strings are deliberately synthetic, not real point releases. The helper has not queried subscriptions, packages or policy.

## Verification and limits

A real comparison should record exact release/architecture, installed DNF implementation, package/repository versions, network owner, security enforcement, required service identity and product support evidence/date. Treat a missing tool/query or permission denial as an observation to explain, not permission to disable controls.

The fixture proves identity handling only. Installation, real repository access, major upgrades, certification and support coverage remain untested. Use [maintenance planning](../06-production-administration/patching-and-maintenance.md) before actual changes.

## Cleanup

```bash
rm -i -- "$enterprise_lab/rhel" "$enterprise_lab/rocky" "$enterprise_lab/review.txt"
rmdir -- "$enterprise_lab"
```

## References

- [RHEL lifecycle](https://access.redhat.com/support/policy/updates/errata) and [RHEL 10 DNF administration](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index).
- [RHEL 10 SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_selinux/index).
- [Rocky](https://docs.rockylinux.org/), [AlmaLinux](https://wiki.almalinux.org/) and [CentOS Stream](https://www.centos.org/centos-stream/).

[Collection home](README.md) · [Fedora comparison](fedora-administration-notes.md)
