# Linux server decommissioning

Decommissioning removes a system's responsibilities and access without losing required data or leaving an unmanaged dependency. Shutdown is one reversible checkpoint; destruction, credential revocation and media disposition can cross different recovery boundaries. Treat each boundary as a separate decision.

## Environment and permissions

Real retirement needs the authorized asset/service/data owners and the relevant infrastructure, identity, backup and security operators. Cloud instances, physical hosts, attached storage, snapshots, images and external services have different lifecycles. Do not infer the target from hostname alone.

The exercise evaluates a mock asset record in a temporary directory. It never drains a real service, changes identity, stops a host, deletes an instance or erases storage. The procedure deliberately omits a universal destructive command because correct deletion/sanitization depends on ownership, media and platform.

## Before you begin

Record immutable asset identifiers, environment, attached volumes, IP/DNS names, certificates, secrets, backup scope, scheduled work, monitoring and all known consumers. Reconcile the inventory with actual usage and the service architecture. An apparently idle server can still host a rarely used recovery, licensing, routing or scheduled function.

Identify retention requirements, legal/preservation holds and data ownership through the responsible organization. Required holds block incompatible deletion. Agree on the replacement service, observation period, recovery boundary and who can authorize each irreversible step.

## Operating procedure

### 1. Discover and confirm dependencies

Authorized read-only Linux checks may include:

```bash
hostnamectl
systemctl list-unit-files --type=service --no-pager
systemctl list-timers --all --no-pager
ss -ltn
findmnt
lsblk -f
```

Correlate with infrastructure inventory, traffic, jobs, application owners and external service records. These snapshots cannot prove there are no consumers. Record meaningful usage over an appropriate workload cycle.

### 2. Transfer responsibility before removing the source

Move application traffic, scheduled jobs, replication/backup duties and monitoring ownership through supported procedures. Verify replacement capacity, data authority, access and the real user operation. Prevent duplicate job execution or two independent writable authorities during migration.

Make an accepted, independently recoverable backup where required and **test the restore**. Preserve configuration and recovery keys under approved control. A successful final backup job alone is not enough.

### 3. Quarantine through a reversible checkpoint

With authorization, stop accepting new work, drain supported in-flight work and stop the intended workload. Use the platform's approved shutdown or isolation mechanism while retaining the documented ability to reverse it. Observe the agreed interval and check for missing consumers, failed jobs, unexpected alerts and recovery obligations.

Do not revoke the only credentials needed to recover or read required archives before their replacement path is verified. Conversely, do not leave unused interactive access active indefinitely: sequence identity work with the checkpoint and recovery requirements.

### 4. Cross irreversible boundaries only after acceptance

After required sign-offs, holds and recovery tests pass, remove platform resources through the approved process. Handle attached/detached volumes, snapshots, machine images, external backups, DNS, certificates, secrets, monitoring, inventory and billing explicitly. Deleting a VM does not necessarily delete its disks or backups.

Select and verify media sanitization/disposition using current organizational policy, platform capabilities and media type. File deletion or repeated writes with a generic command do not automatically sanitize SSDs, snapshots, replicated storage or cloud media. Preserve the required evidence/certificate without retaining sensitive data unnecessarily.

### 5. Close the lifecycle record

Record what was retired, what remains under retention, who owns those remnants, when they expire, the evidence of dependency transfer and disposition, and the final status. Make remaining recovery obligations discoverable to another operator.

## Follow-along lab

### 1. Model a blocked retirement

```bash
retire_lab=$(mktemp -d)
printf '%s\n' \
  '{"asset":"lab-vm-001","owner_approved":true,"replacement_verified":true,"restore_verified":false,"hold":false}' \
  > "$retire_lab/asset.json"
python3 - "$retire_lab/asset.json" <<'PY'
import json
from pathlib import Path
import sys
asset = json.loads(Path(sys.argv[1]).read_text())
blockers = []
for key in ('owner_approved', 'replacement_verified', 'restore_verified'):
    if asset.get(key) is not True:
        blockers.append(key)
if asset.get('hold') is not False:
    blockers.append('hold not cleared')
print('BLOCKED: ' + ', '.join(blockers) if blockers else 'READY FOR REVIEW: ' + asset['asset'])
PY
```

Expect `BLOCKED: restore_verified`. The script performs no retirement action. A true value is an assertion in this simulation, not evidence that a real restore occurred.

### 2. Add supplied exercise evidence and request review

For the synthetic case only, assume a separately reviewed restore succeeded:

```bash
printf '%s\n' \
  '{"asset":"lab-vm-001","owner_approved":true,"replacement_verified":true,"restore_verified":true,"hold":false}' \
  > "$retire_lab/asset.json"
python3 - "$retire_lab/asset.json" <<'PY'
import json
from pathlib import Path
import sys
asset = json.loads(Path(sys.argv[1]).read_text())
checks = ('owner_approved', 'replacement_verified', 'restore_verified')
ready = all(asset.get(key) is True for key in checks) and asset.get('hold') is False
print('READY FOR REVIEW: ' + asset['asset'] if ready else 'BLOCKED')
PY
```

Expect `READY FOR REVIEW: lab-vm-001`, not an automatic deletion. In real work, evidence and human/platform authorization still govern the irreversible boundary. As an extension, set hold to true on your exercise copy and explain why other successful gates cannot override it.

## Verification and rollback

Before destruction, verify the replacement operation, work/data handoff, absence of required consumers over the agreed interval and ability to restore from the quarantine checkpoint. If a dependency was missed, stop retirement and use the planned reversible path while reconciling any new writes or duplicate work.

After destruction or sanitization, rollback may no longer exist. Verify through the platform inventory that intended resources are gone, retained resources remain controlled, access is revoked at its source and the replacement service still works. Keep owners and expiry for retained backups/holds; do not describe the system as completely gone while unmanaged remnants remain.

## Cleanup

```bash
rm -i -- "$retire_lab/asset.json"
rmdir -- "$retire_lab"
```

Only mock data is removed. No production retirement, shutdown or sanitization command is part of this exercise.

## References

- [NIST SP 800-88 Rev. 2, media sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final): use with applicable policy, platform guidance and authorized specialists.
- [Backup/restore requirements](backup-and-restore-operations.md), [access lifecycle](user-access-and-sudo-management.md) and [service handoff](service-management-and-restart-safety.md).
- [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html).

[Collection home](README.md)
