# A filesystem is read-only

A write can fail because the filesystem or mount is read-only even when the file's mode allows writing. The read-only state may be intentional, imposed by a container or snapshot, or a protective response to filesystem/storage errors. The correct response depends on which of those is true.

## Environment and permissions

Diagnostic examples assume Linux with util-linux and systemd journal access where available. Use the application's actual path and execution context. A host mount and a container's view can have different read-only policy. Access to kernel records may require sudo.

The lab requires a disposable Linux VM, sudo and tmpfs support. It remounts only a unique, separately created 4 MiB tmpfs. It does not use a block device, simulate corruption or change fstab. Do not remount an existing root or data filesystem to imitate the lab.

## First checks

Capture the exact error and failing operation. “Permission denied,” “No space left on device” and “Read-only file system” are different evidence. Do not start by changing permissions.

```bash
findmnt --target DIRECTORY
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS --target DIRECTORY
ls -ld -- DIRECTORY
```

Replace DIRECTORY with the failing path or its containing directory. Inspect whether `ro` is present on the relevant mount and whether a submount changes the policy. In a container, inspect that container's mount namespace and configured read-only mounts; host-level rw alone does not rule out a restricted view.

Read bounded records around the first failure:

```bash
journalctl -k -b --since '30 minutes ago' --no-pager
lsblk -f
```

Look for filesystem error reports, I/O failures, device disappearance and remount events. The absence of a log line is not proof the storage is healthy: access, retention and external storage telemetry may limit the available evidence.

## Evidence and interpretation

| Observation | Candidate explanation | Next discriminating check |
| --- | --- | --- |
| Mount intentionally configured ro | Deployment, image or snapshot policy | Approved configuration and intended writable data paths |
| Only one bind/submount is ro | More specific mount policy | Exact target and mount namespace |
| Kernel reports filesystem errors then remounts | Integrity protection, possibly triggered by lower-layer faults | Preserve records; inspect storage health and filesystem-specific recovery requirements |
| Multiple devices show I/O errors | Storage path, controller, media or infrastructure issue | Infrastructure/storage owner and redundant-path health |
| Mount is rw but access denied | Mode, ACL, identity, mandatory policy or application sandbox | Exact errno and access path, not a blind remount |
| Root filesystem is immutable by design | Appliance or image-based administration model | Supported writable overlay or vendor maintenance workflow |

Read-only does not itself establish corruption. Conversely, forcing rw after an integrity error does not establish that writing is safe.

## Recovery decisions

For a confirmed intentional policy mismatch, correct the owning configuration or application write path with rollback. For unexpected error-driven read-only state, reduce further writes, preserve evidence and involve the storage/data owner. Verify backups and whether an image or snapshot is needed before any repair.

Filesystem check/repair must follow that filesystem's documented mount-state requirements. Ext-family repair generally requires an unmounted filesystem; XFS and Btrfs have different tools and constraints. Do not run generic `fsck -y`, `xfs_repair -L` or Btrfs repair options as interchangeable fixes. Root filesystem work often needs a rescue environment. A read-only mount can still involve filesystem recovery behavior, so it is not universal forensic write protection.

Do not repair a filesystem through one host while another host or storage client can still write it. A failing device may need data recovery or replacement before filesystem-level recovery.

## Follow-along lab

### 1. Create and verify a separate tmpfs

```bash
readonly_lab=$(mktemp -d)
mkdir "$readonly_lab/fs"
sudo mount -t tmpfs -o size=4m,nosuid,nodev tmpfs "$readonly_lab/fs"
findmnt --mountpoint "$readonly_lab/fs"
```

Confirm the exact temporary path, tmpfs type and bound before continuing. Change ownership only of this mount root:

```bash
sudo chown "$(id -u):$(id -g)" "$readonly_lab/fs"
printf 'initial\n' > "$readonly_lab/fs/note"
cat "$readonly_lab/fs/note"
```

Expect a successful write and `initial`. If it fails now, investigate setup instead of proceeding.

### 2. Introduce read-only policy on this mount only

```bash
sudo mount -o remount,ro "$readonly_lab/fs"
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS --mountpoint "$readonly_lab/fs"
printf 'second line\n' >> "$readonly_lab/fs/note"
printf 'write status: %s\n' "$?"
cat "$readonly_lab/fs/note"
```

Expect `ro`, a failed append, a nonzero write status and unchanged content. The exact error wording depends on locale. Ownership did not change, and adding file write permission would not solve this mount policy.

Here the cause is known: you deliberately remounted a healthy, disposable tmpfs. That justifies remounting this **lab** rw; the same justification is absent after unexplained disk errors.

## Recovery and verification

```bash
sudo mount -o remount,rw "$readonly_lab/fs"
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS --mountpoint "$readonly_lab/fs"
printf 'write restored\n' >> "$readonly_lab/fs/note"
cat "$readonly_lab/fs/note"
```

Expect `rw` and two lines: `initial` and `write restored`. In a real incident, require evidence that the underlying cause is resolved, the intended policy permits writes, application state is consistent and kernel/storage errors do not recur over a meaningful observation period.

## Cleanup

Remove only the exercise file, unmount the separate tmpfs and then remove its directories:

```bash
rm -i -- "$readonly_lab/fs/note"
sudo umount "$readonly_lab/fs"
findmnt --mountpoint "$readonly_lab/fs"
```

Expect no exact mount after successful unmount. If unmount fails, stop and inspect its users; do not force it or remove its directory. Once unmounted:

```bash
rmdir -- "$readonly_lab/fs" "$readonly_lab"
```

Unmounting tmpfs discards its remaining contents. No block-device metadata was modified by this exercise.

## References

- [mount](https://man7.org/linux/man-pages/man8/mount.8.html) and [kernel tmpfs documentation](https://docs.kernel.org/filesystems/tmpfs.html).
- [e2fsck requirements](https://man7.org/linux/man-pages/man8/e2fsck.8.html) and [XFS repair](https://man7.org/linux/man-pages/man8/xfs_repair.8.html): consult the installed version and filesystem owner before repair.
- [Capacity investigation](disk-space-or-inodes-are-exhausted.md) for a different write-failure class.

[Collection home](README.md) · [Recovery verification](verify-recovery-after-a-fix.md)
