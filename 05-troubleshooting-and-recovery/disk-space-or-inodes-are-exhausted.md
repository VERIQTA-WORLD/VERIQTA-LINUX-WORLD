# Disk space or inodes are exhausted

A write needs both storage capacity and filesystem metadata. “No space left on device” can mean exhausted data space, exhausted inodes, a full thin pool or another allocation limit. “Disk quota exceeded” is a different limit. First identify the filesystem that actually contains the failing path.

## Environment and permissions

Diagnostics assume GNU/Linux with Coreutils, util-linux and optional lsof/quota/LVM tools. Some paths and process details require sudo. Traversing a large tree can create meaningful I/O load; narrow the scope.

The lab requires a **disposable Linux VM**, sudo and tmpfs support. It creates a separate 8 MiB tmpfs with a limit of 128 inodes. It does not fill an existing disk, format a device or change fstab. It consumes at most the bounded filesystem data plus metadata; do not run it on a memory-constrained or shared production host. Run each step separately and preserve the shell variables until cleanup.

## First checks

Replace DIRECTORY with the failing application's actual data or log directory:

```bash
findmnt --target DIRECTORY
df -hT DIRECTORY
df -i DIRECTORY
du -xhd1 -- DIRECTORY
```

`findmnt` identifies source, type and mount. `df` reports the containing filesystem; `du` totals visible allocated files under the chosen path. `-x` avoids descending into other filesystems. Unreadable files make a du total incomplete.

For a known large directory, inspect one level before drilling down. Do not run a recursive scan of every mounted network filesystem as a first response.

## Evidence and interpretation

| Evidence | Candidate explanation | Next check |
| --- | --- | --- |
| Bytes nearly exhausted, inodes available | Large files or retained data | Scoped usage, retention owner and growth rate |
| Inodes exhausted, bytes available | Many small/empty files | File counts and application-created spool/cache directories |
| df high, du much lower | Deleted-open files, hidden mount contents, snapshots, reservations or access limits | Process open files and filesystem-specific accounting |
| Quota exceeded | User, group or project quota | Appropriate quota report and application identity |
| Filesystem appears free but thin pool is full | Lower-layer data/metadata exhausted | LVM thin-pool data and metadata percentages |
| Only a container fails | Writable-layer, mount, quota or cgroup/storage limit | Container mount and storage driver, not only host root df |
| Read-only filesystem | A write policy or integrity response rather than ordinary capacity | [Read-only investigation](filesystem-is-read-only.md) |

Where available and authorized:

```bash
sudo lsof +L1
quota -s
sudo lvs -a -o lv_name,vg_name,data_percent,metadata_percent
```

`lsof +L1` helps find open, unlinked files; it may reveal sensitive paths. Deleting a pathname does not release blocks while a process holds the file open. LVM reports are relevant only on an LVM host. A snapshot or storage pool needs its own capacity accounting.

## Recovery decisions

Identify who owns the data and which retention or backup policy applies. Prefer application-supported log rotation, retention or a reviewed capacity increase. A targeted service action can release a deleted-open log, but first assess interruption and why rotation failed. Do not truncate database files, remove arbitrary application directories or delete evidence to recover a few bytes.

Restoring free space is a mitigation. Verify that the original writer can complete its operation and that data consistency remains acceptable. Then prevent recurrence with capacity/retention monitoring. Freeing bytes does not help inode exhaustion unless file entries are actually released.

## Follow-along lab

### 1. Create a bounded temporary filesystem

```bash
space_lab=$(mktemp -d)
mkdir "$space_lab/fs"
sudo mount -t tmpfs -o size=8m,nr_inodes=128,nosuid,nodev tmpfs "$space_lab/fs"
findmnt --mountpoint "$space_lab/fs"
```

Stop unless the exact path is mounted as tmpfs with the intended bounds. Give your lab user ownership of **only the mounted root** so writes do not need sudo:

```bash
sudo chown "$(id -u):$(id -g)" "$space_lab/fs"
df -hT "$space_lab/fs"
df -i "$space_lab/fs"
```

### 2. Exhaust bytes without exhausting the host filesystem

The writer attempts at most 16 MiB, twice the mount's data limit. It accepts only ENOSPC as the intended failure and leaves the partial file for inspection:

```bash
python3 - "$space_lab/fs/payload" <<'PY'
import errno
import sys
try:
    with open(sys.argv[1], 'wb', buffering=0) as stream:
        for _ in range(16):
            stream.write(b'x' * (1024 * 1024))
except OSError as error:
    if error.errno != errno.ENOSPC:
        raise
    print('Observed ENOSPC while writing payload')
else:
    raise SystemExit('Expected the bounded filesystem to fill; inspect the mount')
PY
df -hT "$space_lab/fs"
df -i "$space_lab/fs"
```

Expect ENOSPC, bytes near capacity and inodes still available. If the mount does not match the setup, stop: do not increase the writer limit to force a failure.

Remove only the known lab payload after inspecting its temporary path:

```bash
rm -i -- "$space_lab/fs/payload"
df -hT "$space_lab/fs"
```

### 3. Exhaust inodes while using little data space

```bash
python3 - "$space_lab/fs" <<'PY'
import errno
from pathlib import Path
import sys
root = Path(sys.argv[1])
for number in range(256):
    try:
        (root / f'inode-{number}').touch(exist_ok=False)
    except OSError as error:
        if error.errno != errno.ENOSPC:
            raise
        print(f'Observed ENOSPC after {number} empty files')
        break
else:
    raise SystemExit('Expected the inode limit to be reached; inspect the mount')
PY
df -hT "$space_lab/fs"
df -i "$space_lab/fs"
```

Expect inodes at or near their limit while data space remains. The exact file count depends on filesystem metadata. Empty files are enough to demonstrate that bytes alone are not the whole capacity model.

## Recovery and verification

The following removes only generated inode-* regular files from this unique exercise mount. Inspect the printed temporary path first. This targeted deletion is appropriate because the files are known disposable exercise data; it is not a production cleanup recipe.

```bash
printf '%s\n' "$space_lab/fs"
for lab_file in "$space_lab/fs"/inode-*; do
  test -f "$lab_file" && rm -- "$lab_file"
done
printf 'write recovered\n' > "$space_lab/fs/check"
cat "$space_lab/fs/check"
df -hT "$space_lab/fs"
df -i "$space_lab/fs"
```

Expect the write/read check to succeed and both capacity classes to have headroom. In a real application, also validate its affected transaction, queue and data integrity after the allocation failure.

## Cleanup

```bash
rm -i -- "$space_lab/fs/check"
sudo umount "$space_lab/fs"
findmnt --mountpoint "$space_lab/fs"
```

After successful unmount, findmnt should show no exact mount and return nonzero. Stop if unmount fails; do not force it or remove its directory while it is mounted. Once unmounted:

```bash
rmdir -- "$space_lab/fs" "$space_lab"
```

Unmounting tmpfs discards anything remaining in it. If interrupted, inspect `findmnt` and the retained variable/path to identify and unmount only your lab mount.

## References

- [Kernel tmpfs documentation](https://docs.kernel.org/filesystems/tmpfs.html).
- [df and file utilities](https://www.gnu.org/software/coreutils/manual/coreutils.html), [lsof](https://man7.org/linux/man-pages/man8/lsof.8.html) and [LVM reporting](https://man7.org/linux/man-pages/man8/lvs.8.html).
- [Disk and filesystem commands](../04-commands-and-cheat-sheets/storage/disk-and-filesystem-commands.md).

[Collection home](README.md) · [Recovery verification](verify-recovery-after-a-fix.md)
