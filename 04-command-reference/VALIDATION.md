# Tested environments and reproduction

Linux execution review: November 4, 2026. The detailed walkthroughs were reproduced in separately booted aarch64 Linux VMs. This record identifies the tested scope; it does not certify every command-table entry, optional argument or production workload.

## Named Linux environments

| Environment | Kernel | Bash / Python | systemd / util-linux | logrotate / OpenSSH |
| --- | --- | --- | --- | --- |
| Ubuntu 24.04.5 LTS cloud image | 6.8.0-142-generic | 5.2.21 / 3.12.3 | 255 / 2.39.3 | 3.21.0 / 9.6p1 |
| Debian 13.7 trixie genericcloud | 6.12.111+deb13-cloud-arm64 | 5.2.37 / 3.13.5 | 257 / 2.41.5 | 3.22.0 / 10.0p2 |
| Fedora Linux 44 Cloud Edition | 6.19.10-300.fc44.aarch64 | 5.3.9 / 3.14.3 | 259 / 2.41.3 | 3.22.0 / 10.2p1 |

The VMs used Lima 2.2.1 with Apple's VZ virtualization and no host filesystem mounts. Ubuntu/Fedora had 2 GiB RAM; Debian had 1.5 GiB; each had two virtual CPUs. Required utilities were installed as VM preparation, separately from the exercises. Fedora retained SELinux enforcing; Ubuntu and Debian reported loaded AppArmor profiles, including enforcing profiles. No mandatory policy was disabled.

The official image inputs were Ubuntu's `noble/release-20260926/ubuntu-24.04-server-cloudimg-arm64.img`, Debian's `trixie/20261001-2618/debian-13-genericcloud-arm64-20261001-2618.qcow2` and Fedora's `44/Cloud/aarch64/images/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2`. Lima verified the configured image digests before boot. These identify the test inputs, not a recommendation to use a particular point image indefinitely.

## Execution results

| Scope | Observed result |
| --- | --- |
| Nine file/text/archive/rsync walkthroughs | Passed on all three targets, including expected comparisons, meaningful nonzero outcomes and temporary-directory cleanup. |
| Additional checksum/restore and GNU permission exercise | Manifest printed `note: OK`; restored bytes matched; mode transitions were 600 → 700 → 600; generated paths were removed. |
| Process lifecycle | The known sleep child terminated, wait reported 143 and the subsequent process query had no matching row. No name-based kill was used. |
| Host inspection | Actual systemd/journal, users/groups/sudo, procps/sysstat, iproute2, mounts, capacity and DNS/NSS commands ran on the targets. A returned empty result is not treated as a tool failure. |
| APT | Ubuntu and Debian package identity/candidate queries and simulation ran without accepting an exercise transaction. |
| DNF5 | Fedora reported DNF5 5.4.1.0; installed-bash queries/proposals ran. A separate absent-package `ed` proposal returned 1 with “Operation aborted by the user”; RPM still reported it uninstalled. |
| Firewall alternatives | UFW reported inactive on the Debian-family VMs. Fedora firewalld reported not running, including status 252; no firewall was activated or policy changed to force a running result. |
| LVM | Queries ran on all targets. An additional Ubuntu fixture supplied a 16 MiB file-backed loop PV, private VG and 8 MiB LV; published queries showed the populated layers. The LV/VG/PV were removed and the exact loop detached. No real disk was formatted. |
| Authorized SSH | A real port-22 key-authenticated session ran on each VM. Expected host identity was provisioned from the VM's public host key through the trusted control path, not accepted blindly from a scan. Temporary key/agent setup was removed and the guest's original authorized_keys/known_hosts bytes restored. |

Each VM exercised 29 applicable detailed references: the APT and DNF guides are alternatives. Together the targets cover all 30 detailed references. This is not execution of all 1,518 cheat-sheet examples.

## Reproduce on your disposable VM

Use an ordinary account, a working systemd user manager and authorized noninteractive sudo in a dedicated disposable Ubuntu, Debian or conventional Fedora VM. Install the required utilities before running: Python 3, Bash, rsync, curl, procps, sysstat, iproute2, the distribution's dig package, logrotate, sudo/visudo, LVM reporting tools and the firewall frontend you will inspect. Read the runner first.

From the repository root:

```bash
python3 tools/check_command_content.py
python3 tools/check_cheat_sheets.py
private_results=$(mktemp -d)
python3 tools/check_linux_exercises.py --confirm-disposable-vm \
  --report "$private_results/results.json"
```

The Linux runner executes published private-file exercises, bounded tmpfs mounts, runtime user units and host observations. It checks intermediate statuses as well as final output so successful cleanup cannot hide an earlier failed command. It refuses root, non-Linux hosts and a missing VM/user-manager prerequisite. The raw report is created with mode 0600; keep it private because account, network and policy output can contain sensitive information.

The runner does not install packages, accept a transaction, reboot, change the resolver/firewall policy, provision LVM storage or add SSH keys. Its default LVM queries can validly return an empty layout. The separate populated-LVM and authenticated-SSH checks require their stated, pre-established lab fixtures; do not infer those results from the automated run alone.

## Boundaries and further review

The earlier macOS runs remain portable evidence; the named VM runs above establish the listed GNU/Linux behavior. They do not establish every release, architecture, container/image variant, remote network path, real data restore, major upgrade or production authorization. APT/DNF may refresh metadata caches during queries.

Syntax, local links, content contracts and cheat-sheet table structure also pass. External URLs, GitHub visual rendering, independent reader reproduction and legal review of the custom license are separate activities. Consult the [recovery](../05-troubleshooting-and-recovery/VALIDATION.md), [administration](../06-system-administration/VALIDATION.md) and [distribution](../07-linux-distributions/VALIDATION.md) records for their specific Linux results.

[Collection home](README.md) · [Command index](command-index.md)
