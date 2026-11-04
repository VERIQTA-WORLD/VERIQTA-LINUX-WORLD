# Capacity and performance reviews

Capacity review asks whether resources and architecture can meet the expected workload with sufficient headroom. Performance review asks whether the service meets its latency, throughput and error objectives. More capacity may help a constraint, but it does not automatically fix inefficient work, a bad dependency or a per-process limit.

## Environment and permissions

Linux observation examples use procps, util-linux and optional sysstat. Queries can expose process names, paths and workload details. Use a representative, authorized time window and understand whether measurements describe a host, container, cgroup, volume or application.

The exercise calculates a storage forecast from explicitly synthetic numbers using Python. It allocates no large data, benchmarks no disk and does not claim to predict a real system.

## Before you begin

Identify the service, owner, objectives, workload pattern, critical periods and planning horizon. Gather comparable history across quiet periods, peaks, deployments and growth events. Note missing samples, retention changes and changes in measurement scope.

Define reserve capacity for maintenance, recovery, replication/rebuild and bursts. A resource limit can exist beneath a healthy-looking aggregate: a full thin pool, inode cap, open-file limit, one hot CPU, constrained cgroup or saturated downstream dependency.

## Operating procedure

### 1. Measure the actual boundary

```bash
uptime
free -h
vmstat 1 5
df -hT DIRECTORY
df -i DIRECTORY
findmnt --target DIRECTORY
```

Replace DIRECTORY with the application's relevant path. For interval analysis where sysstat is installed:

```bash
mpstat -P ALL 1 5
iostat -xz 1 5
pidstat -u -r -d 1 5
```

Do not use the first since-boot vmstat/iostat row as the current interval. Correlate resource samples with user latency, error rates, throughput, queue length and workload shape. High CPU can be productive; low host CPU can coexist with a throttled container.

### 2. Identify the constraint and uncertainty

| Resource | Review at least | Common misinterpretation |
| --- | --- | --- |
| CPU | Per-core/thread activity, run queues, throttling and entitlement | Load average equals CPU percentage |
| Memory | Working set, available memory, pressure, paging and limits | Low free memory alone proves exhaustion |
| Storage | Bytes, inodes, pool capacity, latency and growth | Filesystem free bytes describe every lower layer |
| Network | Throughput, drops/retransmissions, connection rates and path limits | Link speed is achievable application throughput |
| Application | Queues, concurrency, dependencies and per-request cost | A faster host will fix a remote dependency |
| Recovery | Restore/rebuild duration and temporary working space | Steady-state headroom is enough for a failure |

Use [folder 5](../05-troubleshooting-and-recovery/cpu-or-memory-usage-is-high.md) for incident investigation. A capacity forecast should retain assumptions and error margins rather than presenting a straight-line extrapolation as certain.

### 3. Compare runway with action lead time

Choose consistent units and a growth estimate appropriate to the history. Calculate when the operational reserve would be breached, not only when usage reaches 100%. Include time for procurement, approval, rollout and verification. Check whether cleanup/retention changes merely postpone a persistent growth issue.

Decide whether the appropriate action is workload reduction, retention, tuning, a limit change, vertical scaling, horizontal scaling or architectural work. Assign an owner and a date before the reserve is expected to be consumed.

## Follow-along lab

Assume 100 GiB usable capacity, 70 GiB used, 20 GiB reserved headroom and growth of 2 GiB/day. Provisioning takes seven days:

```bash
capacity_lab=$(mktemp -d)
python3 - "$capacity_lab/review.txt" <<'PY'
from pathlib import Path
import sys
capacity_gib = 100
used_gib = 70
reserve_gib = 20
growth_gib_per_day = 2
lead_days = 7
operating_limit = capacity_gib - reserve_gib
days_to_reserve = (operating_limit - used_gib) / growth_gib_per_day
days_to_full = (capacity_gib - used_gib) / growth_gib_per_day
rows = [
    f'days to reserve: {days_to_reserve:.1f}',
    f'days to full: {days_to_full:.1f}',
    f'provisioning lead days: {lead_days}',
    'ACTION NEEDED: lead time exceeds reserve runway'
    if lead_days >= days_to_reserve else 'Planned lead time fits this model',
    'Assumptions: constant growth; no bursts, reclaim or measurement error',
]
Path(sys.argv[1]).write_text('\n'.join(rows) + '\n')
PY
cat "$capacity_lab/review.txt"
```

Expect five days to breach reserve and fifteen days to full. Seven-day provisioning is already too slow for the reserve target. The correct lesson is not “fifteen days remain, so no action is needed.”

As an extension, vary growth and reserve on your own exercise copy. Decide how zero growth, negative growth or already-breached reserve should be reported before changing the calculation. Those cases need explicit treatment in a real forecasting tool.

## Verification and rollback

Confirm input units, reserve definition, forecast calculation, lead time and uncertainty are recorded. The lab proves arithmetic on synthetic values, not real workload capacity.

After an actual capacity/tuning change, compare the same workload and user objectives, inspect the previously constrained boundary and confirm the bottleneck did not move somewhere worse. Use the reviewed reversal plan for incompatible tuning or limits. Disk/data expansion may not have a safe symmetric shrink operation; plan recovery rather than assuming every scaling action is reversible.

## Cleanup

```bash
rm -i -- "$capacity_lab/review.txt"
rmdir -- "$capacity_lab"
```

No workload, resource limit, device size or data-retention policy changed.

## References

- [vmstat](https://man7.org/linux/man-pages/man8/vmstat.8.html), [sysstat iostat](https://sysstat.github.io/man/iostat.1.html) and [kernel pressure accounting](https://docs.kernel.org/accounting/psi.html).
- [Performance reference](../04-command-reference/performance/performance-investigation-cheat-sheet.md).
- [Disk exhaustion investigation](../05-troubleshooting-and-recovery/disk-space-or-inodes-are-exhausted.md).

[Collection home](README.md)
