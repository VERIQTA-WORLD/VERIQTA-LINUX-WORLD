# Inspect mounts and understand mount syntax

Mounting makes a filesystem visible at a directory. Existing contents beneath that mount point become hidden until unmounted. Mount options influence access and behavior.

## Environment and permissions

Linux with util-linux. Inspection is unprivileged. Mounting normally requires root or an explicit policy. The walkthrough does not mount or edit `/etc/fstab`.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `findmnt --target /` | Find the filesystem containing the root path. |
| `findmnt --mountpoint /` | Match an exact mount point. |
| `findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS` | List mount sources and options. |
| `findmnt --fstab` | Read configured fstab entries; does not mount them. |
| `mount -t TYPE -o OPTIONS DEVICE DIRECTORY` | Administrative syntax: attach a filesystem to a directory. |
| `umount DIRECTORY` | Administrative syntax: detach a filesystem; may fail while busy. |
| `mountpoint DIRECTORY` | Check whether a directory is itself a mount point. |

## Follow along

```bash
findmnt --target /
findmnt --mountpoint /
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
findmnt --fstab
mountpoint /
```

## Expected results and verification

Root should be a mount point. `findmnt --fstab` may show no entries in a container; that is not the same as having no active mounts. No state changed and no cleanup is needed.

## Common mistakes and next checks

Identify a device by stable identity and verify contents before mounting. `mount -a` can activate many fstab entries and should not be a casual test. Read-only mounting is not a substitute for forensic write protection: some filesystems may replay journals. A busy unmount needs identifying users of the mount; forced or lazy unmount can complicate recovery. fstab changes need validation and console recovery before reboot.

## Authoritative references

- [mount manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- [findmnt manual](https://man7.org/linux/man-pages/man8/findmnt.8.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
