# Validation and reproduction record

Recorded November 4, 2026. All ten production-administration runbooks are written. The completed checks below establish content structure and bounded teaching behavior, not authorization or certification for a real production change.

## Completed checks

| Check | Evidence | Scope and limits |
| --- | --- | --- |
| Runbook contract | `python3 tools/check_command_content.py` | Requires environment, preflight, operating procedure, lab, verification/rollback, cleanup and references in each runbook |
| Navigation and Markdown | Same checker and `git diff --check` | Case-exact local paths, linked anchors, balanced fences, table-code pipes and whitespace |
| Bash/embedded Python syntax | Same checker | Parses documented command blocks and Python heredocs without running host-administration steps |
| Readiness record | `python3 tools/check_administration_labs.py` | Records unresolved prerequisites and a blocked decision; does not inspect/admit a real Linux host |
| Access draft | Same portable runner | Creates a private policy draft and review record; does not install policy or run optional visudo |
| Maintenance plan | Same portable runner | Creates scope/recovery/result notes; package-manager proposals are not executed |
| Static backup/restore | Same portable runner | Byte equality before corruption, mismatch after corruption, equality after restore and cleanup |
| Alert sequence | Same portable runner | Synthetic two-failure transition at sample 4 and two-success recovery at sample 6; no actual notification |
| Capacity forecast | Same portable runner | Synthetic reserve runway of five days, full-capacity runway of fifteen days and lead-time warning |
| Configuration promotion/rollback | Same portable runner | Rejects wrong-typed candidate, preserves original, promotes valid file and restores exact previous bytes |
| Retirement gates | Same portable runner | Blocks missing restore assertion and reaches review state after supplied mock evidence; no infrastructure action |
| Demo validator | Same portable runner | Accepts valid input and rejects nine malformed/schema-invalid cases, including boolean/out-of-range port, missing/extra keys and empty message |

Eight published portable lab sequences were executed on macOS/Darwin with Python 3.9.6 and Bash 3.2.57. The runner supplies isolated yes responses to temporary-file cleanup prompts and checks that each lab directory is removed. Success on platform tar/cmp/cp is not a GNU/Linux metadata-preservation or application-consistency certification.

No host policy was installed, no package transaction was accepted, no real service restarted, no host log rotated, no external notification sent and no server/storage resource retired by these checks. The synthetic exercises explicitly preserve that boundary.

## Reproduce the checks

From the repository root:

```bash
python3 tools/check_command_content.py
python3 tools/check_administration_labs.py
python3 tools/check_cheat_sheets.py
git diff --check
```

The content checker does not execute listed administration commands. The administration runner **does execute** selected file-based exercises and the demo validator using temporary directories. It excludes the systemd/logrotate labs, optional visudo and package proposals. Review the runner before executing it.

## Linux and operational validation still required

| Scenario | Required evidence | Status |
| --- | --- | --- |
| Host readiness | Actual Linux identity/time, access, mounts, listeners, restore and user-path evidence under approved ownership | Pending |
| Sudo draft parser and effective policy | Installed visudo version, isolated-file syntax result, full-policy review and authorized session tests if applying real policy | Pending |
| Package proposals | Actual APT or DNF implementation, repositories, candidate scope, simulated/declined result and interpretation | Pending |
| systemd user restart | Working user manager, bounded runtime unit, current state/PIDs, restart observation and exact unit cleanup | Pending |
| Isolated logrotate | Version, private directory, no-change debug result, rotation/new-file evidence, metadata and cleanup | Pending |
| GNU/Linux file exercises | Reproduce portable operations on selected Linux releases; record tool/metadata differences | Pending |
| Real backup objectives | Application consistency, protected key access, metadata, isolated restore, measured recovery time/data loss and approved cutover | Pending |
| Actual alert route | Approved rule tests, missing-data behavior, notification delivery, acknowledgement/escalation and recovery route | Pending |
| Capacity review | Comparable real workload history, correct resource boundary, reserve and provisioning assumptions, post-change outcome | Pending |
| Configuration activation | Application-specific validation, metadata, loaded-state/user checks and compatible rollback after activation | Pending |
| Actual retirement | Asset identities, dependency transfer, holds, restore evidence, approvals, reversible checkpoint and platform/media disposition verification | Pending |
| GitHub rendering and independent reader review | Visual inspection and reproduction without unstated setup | Pending |

No Linux VM was used for this authoring pass. Record exact distribution/release, kernel, shell/tool versions, privileges, scope, repository commit, reviewer/date, expected/actual observations and cleanup when completing any pending item. A parser passing cannot substitute for real authorization, application readiness or data recovery.

## Source and publication review

Selected semantics were reviewed against upstream sudo/visudo, logrotate, Debian APT, DNF5, Prometheus, Linux rename, Python JSON and NIST media-sanitization documentation linked in the runbooks. systemd documentation is linked and was consulted in earlier repository work; one fresh systemctl fetch timed out. This is selective source review, not exhaustive external-link or production review.

The existing custom personal-study license is unchanged. Public availability does not change its reuse restrictions; this installment does not introduce an open-source license.

[Collection home](README.md) · [Content standard](../CONTENT-STANDARD.md)
