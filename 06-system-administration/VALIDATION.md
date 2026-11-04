# Tested administration exercises

Linux execution review: November 4, 2026. Published exercises ran on separately booted Ubuntu 24.04.5 LTS, Debian 13.7 and Fedora Linux 44 Cloud Edition aarch64 VMs. See the [exact environment versions](../04-command-reference/VALIDATION.md#named-linux-environments). These are bounded teaching runs, not production change approval or service certification.

## Execution results

| Exercise | Verified result on the named targets |
| --- | --- |
| Readiness record | The fictional record retained unresolved prerequisites and a blocked decision. Real guest identity, time, root/mount, network and manager observations were collected separately; the fictional assertions were not changed to invented passes. |
| Access draft | The private draft was never installed. Actual visudo parsed it successfully on all three systems; full effective-role/session authorization is a separate question. |
| Maintenance plan | The plan remained a private record. Actual APT candidate/simulation and DNF5 query/proposal behavior was inspected without accepting an exercise transaction. |
| Service restart | The bounded runtime user unit was active, had CanReload=no and changed between distinct nonzero MainPIDs on restart. Restart remained no and NRestarts showed no automatic loop. Stop, exact file removal and daemon-reload completed. |
| Isolated logrotate | Debug left the original data intact and no rotated file. Force against only the private policy/state file retained the old two events, created an empty new log and accepted event three. Exact four-file cleanup passed. |
| Backup/restore | The frozen sample matched initially, mismatched after controlled corruption and matched after restore. Comparison statuses were 0/1/0 and cleanup passed with GNU/Linux utilities. |
| Alert sequence | Synthetic two-failure transition occurred at sample 4 and two-success recovery at sample 6. No real notification was sent. |
| Capacity model | Supplied capacity/reserve/growth values produced five days to reserve, fifteen to full and the lead-time warning. This is calculation evidence, not live workload forecasting. |
| Configuration promotion/rollback | Invalid candidate was rejected, valid file promoted and exact previous bytes restored; original data remained protected. |
| Retirement gates | The mock asset remained blocked without restore evidence and reached review state after supplied assertions. No real infrastructure was retired. |
| Demo validator | Valid input and nine malformed/schema-invalid cases produced the required outcomes. |

All eight existing portable sequences were rerun on each Linux target; the restart, logrotate and visudo cases add actual Linux/tool execution. Required packages were provisioned in the disposable VMs before review, not accepted by the exercise's proposal commands.

## Correction to cleanup guidance

On systemd 255, 257 and 259, listing a pattern with no installed unit files returned status 1 after successful cleanup. The [service runbook](service-management-and-restart-safety.md#cleanup) now records that status and explains the empty result. File absence, stopped state and correct manager scope remain the meaningful cleanup evidence.

## Reproduce the bounded exercises

Use an ordinary account with a functioning user manager, the required tools and authorized noninteractive sudo in an explicitly disposable VM. Read the runner and its mount/unit effects before execution.

```bash
private_results=$(mktemp -d)
python3 tools/check_linux_exercises.py --confirm-disposable-vm \
  --report "$private_results/results.json"
```

Run from the repository root. [Shared preparation](../04-command-reference/VALIDATION.md#reproduce-on-your-disposable-vm) explains dependencies and boundaries. The runner does not install sudo policy, rotate host logs, accept updates, configure real alert delivery or retire assets. Its raw 0600 report contains private observation evidence and must be reviewed before sharing.

## Operational limits

The file-based restore does not establish application/database consistency, metadata completeness for every filesystem, protected-key access, actual RTO/RPO or approved cutover. The mock alert/capacity/retirement exercises do not establish real notification delivery, representative workload history or disposition of actual assets.

No fleet rollout, application-specific activation rollback, production admission, real decommissioning or external communication was performed. Policy parsing is not effective authorization. A bounded user sleep service has no customer readiness operation. Those limits remain explicit when you adapt the guides to real systems.

Content contracts, shell/embedded Python syntax and local navigation also pass. The earlier macOS runs remain historical portable evidence; the results above name the actual Linux environments used for this review.

[Collection home](README.md) · [Content standard](../CONTENT-STANDARD.md)
