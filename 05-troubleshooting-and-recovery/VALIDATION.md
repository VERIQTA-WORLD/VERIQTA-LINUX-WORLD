# Tested recovery exercises

Linux execution review: November 4, 2026. The bounded guide exercises were reproduced on Ubuntu 24.04.5 LTS, Debian 13.7 and Fedora Linux 44 Cloud Edition, each a separately booted aarch64 VM. Exact kernels and utility versions appear in the [environment matrix](../04-command-reference/VALIDATION.md#named-linux-environments).

## Observed Linux results

| Exercise | Actual result and recovery evidence |
| --- | --- |
| Troubleshooting method | Supplied evidence, competing hypotheses and conclusion steps passed on all targets; temporary evidence was removed. |
| Reachability | The loopback helper returned the expected response, connection failed after its exact child stopped, a new helper restored the response and cleanup passed. |
| SSH | Offline configuration resolved first to 65022, then the exercise's approved port 22. A separate real port-22 key-authenticated session returned the expected account/host on each VM using independently provisioned host trust. Temporary fixture credentials/agent were removed and original access/trust files restored. |
| Failed user service | `/usr/bin/false` produced failed state and ExecMainStatus=1. Replacing only the exercise command with true produced active/exited, success and status 0. The exact runtime file was removed. |
| Byte exhaustion | The verified 8 MiB/128-inode tmpfs produced kernel ENOSPC during bounded writes while inodes remained available; only the exercise payload was removed. |
| Inode exhaustion | The same bounded mount produced ENOSPC after its inode limit was reached by empty files. Removing only the generated inode files restored a successful write/read; unmount and directory cleanup passed. |
| CPU/memory | The 20-second child touched 16 MiB, appeared in its actual `/proc`/process observations and completed with status 0. Its final process query had no matching row; files were removed. No OOM was induced. |
| DNS/NSS | The `.invalid` lookup returned nonzero (glibc getent status 2); localhost returned loopback data and status 0. Dig's actual DNS response was retained separately. No resolver setting changed. |
| Read-only mount | A separate 4 MiB tmpfs accepted the initial write, rejected append with EROFS/nonzero status after ro remount, then accepted the expected second line after rw remount. Unmount and cleanup passed. |
| Alternate fstab | Missing placeholder UUID produced verification status 1; the corrected alternate tmpfs entry produced 0. No entry was mounted and real fstab/boot settings were unchanged. |
| Recovery acceptance | HTTP success with wrong content failed the comparison; corrected content and five repeated samples passed. Exact-child and temporary-file cleanup passed. |

The helper checks also verified bounded exit with an unfinished HTTP request, rejection of excessive lifetime/memory requests and a one-second/1 MiB worker. Those checks ran on all three Linux targets as well as in the earlier portable review.

## Correction from actual execution

After runtime-unit cleanup, `systemctl --user list-unit-files PATTERN` returned 1 when no unit files matched on systemd 255, 257 and 259. The [failed-service guide](service-will-not-start.md#cleanup) now prints and explains that expected empty-result status. A nonzero diagnostic result must be interpreted in context, not confused with a failed repair.

## Reproduce and keep evidence

Use the prerequisites and stop conditions in each guide. The shared Linux runner requires an explicitly disposable VM, ordinary account, working user manager and authorized sudo. It performs the bounded mount exercises; it is not a production-host checker.

```bash
private_results=$(mktemp -d)
python3 tools/check_linux_exercises.py --confirm-disposable-vm \
  --report "$private_results/results.json"
```

Run from the repository root. Read [runner preparation and scope](../04-command-reference/VALIDATION.md#reproduce-on-your-disposable-vm) first. The default automation reproduces the offline SSH exercise; the authenticated session additionally requires independently verified host identity and a known-good key as described in the SSH guide. Never weaken host-key checking to turn an unavailable fixture into a pass.

The runner retains actual stdout/stderr and intermediate statuses in a private 0600 report. Record repository revision, target identity, versions, privilege/scope, expected/actual outcomes and cleanup. Review redactions before sharing any evidence.

## What these exercises establish

The tests reproduce the documented bounded mechanisms and cleanup on the three named environments. Fedora retained SELinux enforcing. They do not reproduce a corrupt production filesystem, a real unbootable machine, OOM, every NSS/SSH policy, remote routing failure or an application-specific data recovery.

Normal running-guest boot/root/mount observations were collected, but no induced boot failure, rescue-shell repair, firmware/bootloader alteration or console-driven rollback was performed. Alternate-file verification is not a successful reboot test. GitHub rendering and independent reader review remain separate checks.

The original portable checks used macOS; those results are not substituted for the Linux observations above. No system resolver, host firewall policy, mandatory enforcement or production service was changed by an exercise.

[Collection home](README.md) · [Content standard](../CONTENT-STANDARD.md)
