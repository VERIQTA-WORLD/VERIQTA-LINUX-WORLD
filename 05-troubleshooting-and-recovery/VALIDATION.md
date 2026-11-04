# Validation record

Recorded November 4, 2026. All ten guide pages are written. This record distinguishes executed exercises from Linux-only validation that is still pending. The collection is ready for content review, not certified across distributions or production environments.

## Checks completed

| Check | Method | Result and scope |
| --- | --- | --- |
| Guide structure | `python3 tools/check_command_content.py` | Enforces environment, evidence/interpretation, lab, recovery/verification, cleanup and references in all ten guides |
| Links and Markdown | Same checker and `git diff --check` | Case-exact local paths, linked heading anchors, balanced fences, escaped table pipes and changed-line whitespace |
| Shell syntax | Same checker | Parses Bash blocks without executing Linux diagnostics or privileged changes |
| Embedded Python syntax | Same checker | Parses the two disk-exercise Python heredocs without running them |
| Method exercise | `python3 tools/check_recovery_labs.py` | Published synthetic-evidence, competing-hypothesis and conclusion steps executed, including cleanup |
| Offline SSH exercise | Same portable runner | Isolated configuration resolved first to port 65022 and then 22; temporary file removed; optional authentication test excluded |
| Reachability exercise | Same portable runner | Observed ready response, connection failure after stopping the child, recovery with a new helper and cleanup |
| Acceptance exercise | Same portable runner | Confirmed successful HTTP with wrong content fails comparison; corrected content and five repeated samples pass; cleanup confirmed |
| HTTP helper | Same portable runner | Correct loopback response, bounded exit with an unfinished request and rejection of an excessive requested lifetime |
| Worker helper | Same portable runner | One-second, 1 MiB allocation completes; excessive memory/time requests are rejected |

The authoring host is macOS/Darwin with Python 3.9.6, Bash 3.2.57 and curl 8.7.1. The portable runner supplies confirmation replies separately to each interactive cleanup command and verifies that each exercise directory is removed. These runs are not Linux `/proc`, systemd, tmpfs, NSS or fstab validation. No privileged recovery command was executed.

The sandbox blocks loopback listeners by default. The portable HTTP checks were run with approved local execution outside that restriction; they use only 127.0.0.1, temporary files and bounded processes. A first sandboxed attempt could not start its listeners; the final successful run used the documented helper behavior. No external service or production configuration is involved.

## Run the checks yourself

From the repository root:

```bash
python3 tools/check_command_content.py
python3 tools/check_recovery_labs.py
python3 tools/check_cheat_sheets.py
git diff --check
```

The content checker does not execute commands. The portable recovery runner **does** execute selected unprivileged lab snippets, launches short-lived loopback servers and starts a one-second worker. Review it first; run it where local listener creation is allowed. It never mounts filesystems, uses sudo, edits host policy, connects to an SSH server or sends DNS queries. Optional packages and platform utilities still need checking on the target environment.

## Linux reproduction still required

| Guide or behavior | Environment and acceptance | Status |
| --- | --- | --- |
| systemd user-service failure/recovery | Disposable systemd VM with a working user manager, runtime unit, exit 1 evidence, corrected exit 0 and exact unit cleanup | Pending |
| Byte and inode exhaustion | Disposable VM, 8 MiB/128-inode tmpfs, both ENOSPC mechanisms, successful write after cleanup and successful unmount | Pending |
| Read-only mount failure/recovery | Disposable VM, separate 4 MiB tmpfs, observed ro write failure, rw recovery and unmount | Pending |
| CPU/memory investigation | Linux procps, `/proc` and optional sysstat; 20-second/16 MiB worker observed in the correct scope | Pending |
| DNS/NSS exercise | Linux with glibc getent; optional dig; capture actual invalid-name and localhost outcomes without resolver changes | Pending |
| Alternate fstab verification | Linux util-linux; absent placeholder source rejected, intended tmpfs entry accepted, no live mount performed | Pending |
| SSH server authentication/session | Authorized VM, independently verified host identity and known-good key; second session verified without changing server policy | Pending |
| Console boot observations | Snapshotted disposable VM; identify stages, kernel/root identities and required mounts; no induced boot failure | Pending |
| Distribution differences | Reproduce appropriate checks on one Debian/Ubuntu-family and one Fedora/RHEL-family system, recording actual versions and deviations | Pending |
| GitHub visual layout and independent reader review | Inspect rendered tables/code; reproduce scenarios without unstated setup | Pending |

Docker's daemon was unavailable, and Lima had no configured VM. No Linux VM was created or used during this authoring pass. Do not mark a scenario tested merely because its syntax check passed.

## Evidence to retain for each Linux run

Record reviewer/date, repository commit, distribution/release, kernel, Bash, Python and relevant utility versions. State privileges, namespace/container scope, optional packages and recovery access. Record exact steps, expected and actual observations, meaningful nonzero statuses, corrections and cleanup confirmation. Keep secrets and raw private evidence outside the public repository.

If a lab fails, preserve the relevant bounded output, stop dependent steps and investigate the difference. Do not remove the safety bound, substitute a real disk, disable security policy or force a reboot just to obtain the illustrated result. Update the guide and rerun the affected check after the cause is understood.

## Documentation review

Selected semantics were checked against upstream Linux/util-linux manuals, systemd, OpenSSH, BIND, RFC 2606, curl, Python and kernel tmpfs documentation linked within the guides. This is selective source review, not an exhaustive external-link availability test or independent operational review. Filesystem-specific repair recipes are deliberately not presented as universal commands.

The repository's existing custom personal-study license remains in effect. This content change does not alter reuse permissions or convert the project to an open-source license.

[Collection home](README.md) · [Content standard](../CONTENT-STANDARD.md)
