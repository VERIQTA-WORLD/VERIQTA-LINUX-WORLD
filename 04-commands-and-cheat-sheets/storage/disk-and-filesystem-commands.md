# Inspect disks, filesystems and capacity

A block device provides storage; a filesystem organizes files; a mount attaches a filesystem to a path. Free space reported for a filesystem is different from the apparent size of one directory tree.

## Environment and permissions

Linux with util-linux and GNU Coreutils. Queries below are read-only; `du` can be expensive on large trees and may lack access to some directories.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS` | Show storage topology with explicit columns; older releases may need MOUNTPOINT singular. |
| `df -hT /` | Report mounted filesystem type, capacity and usage for /. |
| `df -i /` | Report inode usage; free bytes do not guarantee free inodes. |
| `du -sh -- PATH` | Sum allocated file space beneath a path. |
| `du -xhd1 -- PATH` | Show one directory level without crossing filesystem boundaries (GNU syntax). |
| `findmnt --target PATH` | Identify the filesystem that contains a path. |
| `sudo blkid` | Probe block-device filesystem identities; elevated read-only inspection. |

## Follow along

```bash
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
findmnt --target /
df -hT /
df -i /
storage_lab=$(mktemp -d)
printf 'sample\n' > "$storage_lab/note"
du -sh -- "$storage_lab"
rm -i -- "$storage_lab/note"
rmdir -- "$storage_lab"
```

## Expected results and verification

`df` measures the filesystem containing `/`; `du` measures only the exercise tree. Tiny files still occupy allocation units, so a seven-byte file can consume several KiB. Storage layout and totals vary. The temporary file is removed after verification.

## Common mistakes and next checks

Deleted files held open by processes can explain df/du differences; so can snapshots, reserved blocks, hidden mount contents and permissions. Do not “fix” this by formatting or removing partitions. `mkfs`, `wipefs` and partition writes can destroy data and require a separate verified recovery plan.

## Authoritative references

- [lsblk manual](https://man7.org/linux/man-pages/man8/lsblk.8.html)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
