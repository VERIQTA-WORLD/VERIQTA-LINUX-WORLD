# Patching and maintenance

Patching is a controlled transition between supported states. It includes repository trust, dependency changes, service interruptions, kernel/userspace compatibility, reboot decisions and acceptance after the work. A package manager reporting success is not enough to close the change.

## Environment and permissions

Examples distinguish Debian/Ubuntu APT from Fedora/RHEL-family DNF. Identify release, enabled repositories and installed implementation before selecting commands. Read-only queries and simulations often work without root; metadata refresh and accepted transactions change state and can run package scripts or restart services.

The mandatory exercise writes a maintenance plan. Optional package proposals run on a disposable Linux VM and accept **no** transaction. DNF may still contact repositories and update user metadata caches. No real patch or reboot was performed during authoring.

## Before you begin

Identify the supported target, advisories or business reason, workload owner, window and expected interruption. Check available storage/inodes, package-manager consistency, repository configuration and recovery access. Confirm backups or restore points are appropriate to the application; a VM snapshot is not automatically application-consistent or independent of its storage.

Plan the recovery of package versions **and data/configuration**. A package downgrade or DNF history operation may not undo a database migration, removed dependency or changed persistent format. Keep required older artifacts or a tested image rebuild path where policy allows.

## Operating procedure

### 1. Capture the baseline

```bash
cat /etc/os-release
uname -r
df -hT /
df -i /
systemctl --failed --no-pager
```

Check the actual package/cache, boot and application filesystems if separately mounted. Record relevant service versions, health checks, dependency/cluster state and current running kernel. A host that is already degraded needs an explicit decision before routine maintenance proceeds.

### 2. Inspect proposals using the correct family

Debian/Ubuntu inspection using current metadata:

```bash
apt-cache policy bash
apt-get -s install --only-upgrade bash
dpkg --audit
```

Simulation does not install packages and may be limited by stale metadata or unprivileged visibility. In a real approved change, `sudo apt update` refreshes repository metadata before a new proposal is reviewed. `apt full-upgrade` can remove packages and has different effects from an ordinary upgrade.

DNF-family inspection:

```bash
dnf --version
dnf repolist
rpm -q bash
dnf --assumeno upgrade bash
```

Read proposed additions, removals, replacements, repository origins and versions. An intentionally declined DNF transaction may return nonzero. Do not add `--allowerasing`, skip-broken options or signature bypasses merely to make a proposal complete.

### 3. Apply in a bounded sequence

For actual approved work, update a representative canary first, drain work or preserve redundancy through the service's supported procedure, accept only the reviewed transaction and retain its logs. Package changes may restart services without a separate explicit systemctl command. Avoid simultaneous maintenance of quorum members or redundant paths unless the architecture explicitly tolerates it.

Do not delete package lock files to bypass an active transaction. Investigate the owning process and supported recovery workflow. Keep a clear abort decision if the result diverges from the approved scope.

### 4. Decide on restarts and reboot

Use distribution/application guidance and installed tooling to identify processes or the kernel needing restart. A marker such as `/var/run/reboot-required` is distribution-specific, not universal. A successful package install does not replace a running kernel. Schedule an authorized reboot only with console access, expected boot/mount state, workload handoff and a defined return-to-service test.

## Follow-along lab

Create a plan before querying a package manager:

```bash
patch_lab=$(mktemp -d)
printf '%s\n' \
  'Target: disposable lab VM; package example: bash' \
  'Scope: inspect proposal only; no install or reboot' \
  'Prechecks: OS/repositories, baseline health, capacity, console and restore path' \
  'Stop: unexpected removals, untrusted origin or missing recovery evidence' \
  'Acceptance for a real change: intended versions plus original user operation' \
  'Rollback: tested prior image/data state, not assumed package undo' \
  > "$patch_lab/plan.txt"
cat "$patch_lab/plan.txt"
```

On your disposable Linux VM, choose **one** family above and inspect its proposal. Do not execute the other family's commands or accept an installation. If no suitable VM is available, record that package validation is pending:

```bash
printf '%s\n' \
  'Proposal evidence: pending target Linux VM and actual repository state' \
  'Transaction accepted: no' \
  'Reboot performed: no' \
  > "$patch_lab/result.txt"
cat "$patch_lab/result.txt"
```

After an actual optional proposal review, replace that note with versions, repository origins, proposed changes and the decline/simulation outcome. Keep private repository URLs or credentials out of public notes.

## Verification and rollback

The exercise proves only that a plan/result record was prepared; it does not establish patch readiness. For a real change, verify installed and running versions where applicable, intended services, required mounts, application operations, errors, queues and resource headroom. Recheck after an authorized reboot when one is required.

If the change fails acceptance, stop rollout and use the tested recovery plan. Determine whether restoring old application binaries against newer data is compatible before attempting it. Record any temporary holds, reduced redundancy or deferred updates with an owner and follow-up date.

## Cleanup

```bash
rm -i -- "$patch_lab/plan.txt" "$patch_lab/result.txt"
rmdir -- "$patch_lab"
```

The mandatory lab changed no installed package, repository policy or boot setting. Optional metadata queries may leave ordinary package-manager cache state.

## References

- [APT transaction simulation](https://manpages.debian.org/bookworm/apt/apt-get.8.en.html).
- [DNF command reference](https://dnf.readthedocs.io/en/latest/command_ref.html) and [DNF5 upgrades](https://dnf5.readthedocs.io/en/latest/commands/upgrade.8.html).
- [Boot investigation](../05-troubleshooting-and-recovery/server-will-not-boot.md) and [service safety](service-management-and-restart-safety.md).

[Collection home](README.md)
