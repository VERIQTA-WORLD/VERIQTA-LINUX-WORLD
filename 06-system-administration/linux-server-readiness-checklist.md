# Linux server readiness checklist

Readiness is an acceptance decision supported by evidence. A host that boots and answers SSH may still lack recoverable data, useful monitoring, intended access restrictions or an owner who can respond when it fails. Use this checklist when introducing a server or after a major rebuild.

## Environment and permissions

Inspection examples assume GNU/Linux, systemd and standard networking/storage utilities where named. Read-only information can still be sensitive. Journal, policy and device details may require authorized administrative access. The exercise only writes a private temporary record and can run without root.

Adapt the checklist to the service's role. A public frontend, database replica, build runner and single-user workstation have different acceptance criteria. Do not enable services or ports solely because another server has them.

## Before you begin

Identify the asset ID, environment, workload, owner, escalation route and intended lifecycle. Establish console/recovery access through the actual infrastructure control plane. Confirm the distribution/release is within the organization's support policy using that distribution's current lifecycle documentation.

Agree on a user-visible acceptance operation, required dependencies, data recovery objectives and monitoring coverage. A missing requirement belongs in the change record with an owner and decision, not an invented check mark.

## Operating procedure

### 1. Confirm identity, time and provenance

```bash
cat /etc/os-release
uname -r
hostnamectl
date -Is
timedatectl
systemd-detect-virt
```

Compare these with the asset inventory and build record. A timestamp without a correct time source weakens log correlation and can break certificate/authentication checks. Hostnames can be reused: corroborate infrastructure instance and storage identities through the authorized inventory.

### 2. Confirm access and management boundaries

Inspect approved identities, current groups, effective sudo policy and SSH configuration through the [access runbook](user-access-and-sudo-management.md). Test authorized access from its intended source and retain a verified recovery route. Check both intended access and a representative prohibited operation without triggering lockouts or broad scanning.

### 3. Confirm service, network and storage state

```bash
systemctl --failed --no-pager
systemctl list-unit-files --type=service --no-pager
ss -ltn
ip -br address
ip route show
findmnt
df -hT
df -i
```

Map listeners to approved services and exposure policy. Enablement is not current health. Verify required data mounts before allowing applications to write into directories that might merely be empty mount points. Readable free-space percentages are insufficient without workload-based headroom and inode checks.

### 4. Confirm ongoing operations

| Area | Evidence to retain | Acceptance question |
| --- | --- | --- |
| Patching | Supported repositories, baseline versions and update plan | Who owns updates and required restarts? |
| Backup | Restore result, recovery-point age and key access | Can an authorized operator restore usable data? |
| Logging | Recent events, retention, forwarding and access control | Can the incident window be investigated without exhausting storage? |
| Monitoring | User-path check, host/service signals and tested notification route | Will impact reach an accountable responder? |
| Capacity | Baseline and growth/load assumptions | Is there enough headroom to operate through the next review? |
| Configuration | Reviewed source and deployment/rollback method | Can another operator reproduce and undo the intended state? |

### 5. Make and record the acceptance decision

Perform the actual service operation from its intended client path. Compare data, errors and latency with the agreed acceptance criteria. Identify exceptions with an owner, expiry/review date and compensating controls. Decide ready, blocked, or conditionally accepted by the responsible owner.

## Follow-along lab

Create a record for a fictional lab host. The initial state deliberately contains unresolved evidence:

```bash
ready_lab=$(mktemp -d)
chmod 700 "$ready_lab"
printf '%s\n' \
  'Asset: linux-world-lab; environment: disposable learning VM' \
  'Owner: learner; acceptance: read exact expected health response' \
  'Console access: NOT YET VERIFIED' \
  'Restore evidence: NOT YET VERIFIED' \
  'Decision: BLOCKED pending recovery prerequisites' \
  > "$ready_lab/readiness.txt"
cat "$ready_lab/readiness.txt"
```

Do not replace unknowns with “passed” merely because the file was created. On your disposable Linux VM, run the read-only checks above and write their interpreted results into a separate evidence file. If no VM is available, keep those checks pending.

```bash
printf '%s\n' \
  'Evidence: this exercise produced a readiness record only' \
  'Console test: pending actual VM access' \
  'Restore test: pending a successful isolated restore' \
  'Next owner: learner; revisit before admitting any real workload' \
  > "$ready_lab/evidence.txt"
cat "$ready_lab/evidence.txt"
```

Explain why the honest decision is still blocked. As an extension, complete [backup practice](backup-and-restore-operations.md) and distinguish its static-file restore evidence from a real service's recovery requirements.

## Verification and rollback

Check that the record names the system, owner, acceptance operation, unresolved prerequisites and next action. For real readiness, independently reproduce recovery access and the user operation. Do not place real traffic or data on a system with unresolved critical recovery requirements.

Readiness inspection needs no system rollback because it changes no host settings. If onboarding exposed an error, correct it through the relevant reviewed runbook and rerun the affected acceptance checks. A previously accepted host can become unready after rebuilds, drift or expired credentials.

## Cleanup

```bash
rm -i -- "$ready_lab/readiness.txt" "$ready_lab/evidence.txt"
rmdir -- "$ready_lab"
```

Retain approved real operational evidence in the organization's protected system of record, not only on the host being assessed.

## References

- [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html) and [timedatectl](https://www.freedesktop.org/software/systemd/man/latest/timedatectl.html).
- [Recovery verification](../05-troubleshooting-and-recovery/verify-recovery-after-a-fix.md).
- [Capacity reviews](capacity-and-performance-reviews.md).

[Collection home](README.md)
