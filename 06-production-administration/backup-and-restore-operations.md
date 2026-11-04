# Backup and restore operations

A backup is useful when an authorized operator can restore the right data, in a compatible environment, within agreed limits. A successful copy or job status does not establish recoverability. Design and regularly rehearse the restore, including credentials, keys, configuration and application consistency.

## Environment and permissions

The sample uses Bash, tar, cmp and Python 3.8+ on a temporary static file tree, without root. It does not back up a live database or preserve every ACL, extended attribute, ownership mapping or security label. Production backup tools and retention mechanisms require service-specific procedures and approved access to sensitive data.

The example archive is created from known local files and restored only into a new empty directory. Never extract an untrusted archive as root or directly over live data.

## Before you begin

Agree with the data owner on:

| Requirement | Operational question |
| --- | --- |
| Recovery point objective (RPO) | How much committed data loss is acceptable? |
| Recovery time objective (RTO) | How long may the defined service outcome remain unavailable? |
| Consistency | Which application/database mechanism makes a recoverable point? |
| Scope | Are data, configuration, identities, keys and dependencies included? |
| Retention and separation | Which failures or malicious actions can affect both live and backup copies? |
| Access and encryption | Who can restore, and can they obtain required keys independently of the failed host? |
| Evidence | When was usable data last restored and checked? |

A snapshot on the same failing storage is not independent protection. A mirror can propagate deletion or corruption. Encryption without recoverable key access can make an intact backup unusable.

## Operating procedure

### 1. Create a consistent recovery point

Use application-supported backups, snapshots coordinated with the application, or an approved quiescing workflow. Record the point's time and workload state. Copying live database files with tar or rsync alone does not establish transactional consistency.

### 2. Track creation and retention

Record job identity, protected scope, completion, warnings, size trend, destination, key/reference metadata and recovery-point age. Separate “job completed” from “the newest usable recovery point meets RPO.” Alert on stale, partial, inaccessible or unexpectedly small/large backups as appropriate.

Apply retention only after checking holds and recovery requirements. Test that deletion or compromise of a production account cannot silently remove every required recovery copy.

### 3. Restore in isolation

Select a trusted recovery point, provision compatible software and identities, retrieve keys through the authorized path, and restore into an isolated target. Verify file metadata and application/database integrity using the application's supported checks. Prevent a restored clone from sending real messages, taking production jobs or reusing an active identity unintentionally.

### 4. Plan cutover and reconciliation

Identify the lost-data interval, replay/reconciliation requirements, client endpoint change, write authority and rollback limits. Two writable copies can diverge. Data owners must decide what is authoritative before reopening writes.

## Follow-along lab

### 1. Create and archive frozen sample data

```bash
backup_lab=$(mktemp -d)
mkdir "$backup_lab/source" "$backup_lab/restored"
printf 'record one\nrecord two\n' > "$backup_lab/source/records.txt"
restore_start=$SECONDS
tar -czf "$backup_lab/sample.tar.gz" -C "$backup_lab/source" records.txt
tar -tzf "$backup_lab/sample.tar.gz"
tar -xzf "$backup_lab/sample.tar.gz" -C "$backup_lab/restored"
cmp -- "$backup_lab/source/records.txt" "$backup_lab/restored/records.txt"
printf 'initial byte comparison: %s\n' "$?"
```

Expect one member and comparison status 0. Source data remains frozen throughout this exercise.

### 2. Demonstrate that a present file can still be wrong

```bash
printf 'damaged copy\n' > "$backup_lab/restored/records.txt"
cmp -- "$backup_lab/source/records.txt" "$backup_lab/restored/records.txt"
printf 'damaged byte comparison: %s\n' "$?"
```

Expect status 1 for different bytes. Existence and nonzero size are insufficient. A comparison status above 1 indicates a comparison error and needs investigation.

### 3. Restore and check content again

The archive is trusted exercise data. Re-extraction replaces only its known sample file in the disposable destination:

```bash
tar -xzf "$backup_lab/sample.tar.gz" -C "$backup_lab/restored"
cmp -- "$backup_lab/source/records.txt" "$backup_lab/restored/records.txt"
printf 'recovered byte comparison: %s\n' "$?"
cat "$backup_lab/restored/records.txt"
printf 'exercise elapsed seconds: %s\n' "$((SECONDS - restore_start))"
```

Expect status 0 and both original records. Elapsed time includes your interaction and demonstrates recording a duration; it is not a production RTO measurement. The lab has no changing source workload, so it does not measure real RPO.

## Verification and rollback

The lab establishes byte equality for one static file after a known corruption. Real verification must include correct recovery-point selection, metadata/access, keys, application consistency, dependencies, actual user operations and measured time/data loss against RTO/RPO. Keep evidence and an independent reviewer where appropriate.

Before production cutover, preserve the current state and define how to abandon the staged restore safely. After accepting new writes, reverting to an older copy may discard those writes: a “rollback” then requires reconciliation, not simply swapping directories back.

## Cleanup

```bash
rm -i -- "$backup_lab/source/records.txt" "$backup_lab/restored/records.txt" \
  "$backup_lab/sample.tar.gz"
rmdir -- "$backup_lab/source" "$backup_lab/restored" "$backup_lab"
```

Production backup expiry and deletion are separate authorized lifecycle tasks; this cleanup applies only to the temporary exercise.

## References

- [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).
- [rsync preservation and synchronization semantics](https://download.samba.org/pub/rsync/rsync.1).
- [Restore verification reference](../04-commands-and-cheat-sheets/backup-and-recovery/recovery-command-reference.md) and [service recovery acceptance](../05-troubleshooting-and-recovery/verify-recovery-after-a-fix.md).

[Collection home](README.md)
