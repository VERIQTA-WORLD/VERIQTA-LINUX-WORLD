# A server will not boot

A startup failure can occur before firmware finds a boot device, before the kernel starts, while the initial RAM filesystem locates root, or after systemd begins starting mounts and services. “The server does not boot” is too broad to select a safe repair.

## Environment and permissions

Use a disposable Linux VM for practice. A real investigation needs authorized hypervisor/cloud/physical console access, boot media compatible with the installation, storage identities and encryption recovery material where applicable. Keep recovery secrets private. The guide assumes systemd for the userspace stage, but firmware, bootloaders and initramfs tooling vary widely.

The mandatory lab only validates an **alternate temporary fstab file**. It does not change the machine's real fstab, bootloader, firmware variables, initramfs or partitions, and does not require a reboot or sudo. Console observations are an optional extension on a snapshotted disposable VM. This lab demonstrates one startup dependency mechanism, not an actual unbootable machine.

## First checks: identify the last successful stage

Capture the console message and its preceding context, the last known successful boot, recent kernel/storage/firmware changes, and whether the disk layout or instance attachments changed. Do not reboot repeatedly just to see if a storage error disappears.

| Last visible stage | What it suggests | Useful next evidence |
| --- | --- | --- |
| Firmware cannot find a boot device | Attachment, boot order, disk or firmware mode | Console boot settings and infrastructure attachment state |
| Bootloader prompt or rescue message | Boot entry, bootloader files or access to their filesystem | Exact error and installed BIOS/UEFI layout |
| Kernel panic before root is mounted | Kernel, driver, root selection, initramfs or hardware | Full panic, selected kernel and root command line |
| Initramfs waits for root/encryption/device | Missing device, UUID, driver, key or storage path | Available devices versus expected identity |
| Emergency mode after root is found | Required mount, filesystem check or dependency failure | Failed units, boot journal, fstab and actual devices |
| Normal console login but remote access fails | Startup may have succeeded; network/service did not | Reachability and SSH guides rather than reinstalling bootloader |

A boot screen stopping at one line does not prove the named component caused the failure. Capture preceding errors and compare with the expected stage.

## Evidence and interpretation

If an emergency/recovery shell is available, first determine whether it belongs to the installed system or a separate rescue image. Its `/` and `/etc/fstab` may not belong to the failed installation.

On the installed system's usable emergency shell, these are read-only starting points:

```bash
cat /proc/cmdline
lsblk -f
findmnt
systemctl --failed --no-pager
journalctl -b -p warning --no-pager
cat /etc/fstab
```

Commands and journals may be absent in initramfs. In a rescue image, inspect identified target storage with the appropriate vendor procedure. Do not assume that mounting it at a guessed path or entering a chroot makes all repair tools safe. Some operations need the correct mounted filesystems, device mappings, firmware mode and initramfs environment.

| Specific evidence | Hypothesis to test | What would weaken it |
| --- | --- | --- |
| Required fstab UUID is absent | Missing or renamed/reattached filesystem prevents a required mount | UUID is present and its actual mount failure has another cause |
| Previous kernel boots, new kernel fails | Kernel/initramfs/module regression or entry-specific configuration | Both entries fail identically before kernel selection matters |
| Root command line identifies an old device | Stale root selection | Correct identity is selected and readable but filesystem fails |
| Disk reports repeated I/O errors | Storage-path or media failure | Independent storage evidence shows another layer caused the missing device |
| Failed optional network mount blocks boot | Dependency/timeout policy does not match intended availability | The mount is actually required for data integrity or service correctness |

The absence of a device could mean wrong attachment, not a deleted filesystem. Do not create a replacement partition or format a device to satisfy a missing UUID.

## Recovery decisions

- **Recent kernel update:** selecting a known-good installed kernel for one boot may restore access. Confirm module compatibility and record which entry succeeded before changing persistent defaults.
- **Confirmed fstab mistake:** preserve the original, establish the intended device/mount and correct only the verified entry. `nofail` changes dependency semantics; do not apply it to a required data volume just to get a login screen.
- **Initramfs/bootloader problem:** follow the exact distribution and firmware-mode procedure. Debian-family update-initramfs and RPM-family dracut are not universal substitutes. Blind `grub-install` can target the wrong disk or boot mode.
- **Storage errors or corruption:** preserve evidence and recovery options; coordinate filesystem-specific checking with the data/storage owner. Repair tools may write metadata and discard unrecoverable data.

Before a planned reboot after recovery, validate the relevant configuration, verify console access and ensure someone can select a recovery path. A config parser succeeding is a prerequisite, not proof the next boot will succeed.

## Follow-along lab

### 1. Create an alternate fstab with a missing source

```bash
boot_lab=$(mktemp -d)
mkdir "$boot_lab/mount"
printf '%s %s %s %s %s %s\n' \
  'UUID=11111111-1111-1111-1111-111111111111' \
  "$boot_lab/mount" ext4 defaults 0 2 \
  > "$boot_lab/fstab"
cat "$boot_lab/fstab"
findmnt --verify --verbose --tab-file "$boot_lab/fstab"
printf 'verification status: %s\n' "$?"
```

The example assumes that placeholder UUID is absent. Inspect output rather than assuming it is unique on your host. Expect source-availability errors and nonzero verification status when it is absent. findmnt may also emit environment/version-specific warnings. It reads this alternate file; it does not mount its entries or edit `/etc/fstab`.

If your findmnt does not support these flags, stop and inspect its installed help. Do not substitute `mount -a`, which acts on live mount configuration.

### 2. Correct the exercise's intended mount definition

In this exercise, the intended filesystem is a small disposable tmpfs, not the missing ext4 device. Replace only the alternate file:

```bash
printf '%s %s %s %s %s %s\n' \
  tmpfs "$boot_lab/mount" tmpfs size=4m,nosuid,nodev 0 0 \
  > "$boot_lab/fstab"
findmnt --verify --verbose --tab-file "$boot_lab/fstab"
printf 'verification status: %s\n' "$?"
```

Expect no missing-UUID error and status 0 on the intended util-linux baseline. If another warning/error appears, read it and record the actual result. This is a correction to supplied exercise intent, not permission to replace a real missing data filesystem with empty temporary storage.

## Recovery and verification

The lab verifies alternate-file consistency only. Confirm the temporary path was never mounted:

```bash
findmnt --mountpoint "$boot_lab/mount"
```

Expect no exact mount and nonzero status. For a real boot recovery, acceptance includes reaching the intended target, expected root/data mounts, unlocked required volumes, working services, remote access and the original user operation. Inspect current-boot errors and verify that required data is present before starting applications that might write into an empty mount-point directory.

Optional disposable-VM extension: snapshot a known-good VM, open its console and observe one normal boot. Record the firmware/bootloader/kernel/userspace transition, selected kernel, root identity and required mounts. No induced boot failure is needed to learn where to gather evidence. If any later exercise changes boot settings, define snapshot restoration **before** making that change.

## Cleanup

No filesystem should be mounted at the lab path. Remove the alternate file and empty directories:

```bash
rm -i -- "$boot_lab/fstab"
rmdir -- "$boot_lab/mount" "$boot_lab"
```

Do not remove actual boot files, snapshots or recovery media as part of this exercise. Reconcile any emergency changes separately with the system owner.

## References

- [findmnt verification](https://man7.org/linux/man-pages/man8/findmnt.8.html) and [fstab format](https://man7.org/linux/man-pages/man5/fstab.5.html).
- [systemd boot sequence](https://www.freedesktop.org/software/systemd/man/latest/bootup.html) and [fstab generator](https://www.freedesktop.org/software/systemd/man/latest/systemd-fstab-generator.html).
- [dracut](https://man7.org/linux/man-pages/man8/dracut.8.html): relevant only where this tool is installed and used.
- [Read-only filesystem investigation](filesystem-is-read-only.md).

[Collection home](README.md) · [Recovery verification](verify-recovery-after-a-fix.md)
