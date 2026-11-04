# CPU or memory usage is high

A high utilization number is not by itself an incident. Start with the affected request, throughput, queue or deadline. Decide whether resource use explains that impact, whether it is expected for the workload, and whether the metric represents the host, a container or one process.

## Environment and permissions

Examples assume Linux with procps-ng. Optional per-CPU/per-process interval tools come from sysstat. Restricted process details, kernel OOM records or cgroup paths can need authorization. Sampling is read-only, but aggressive tracing and large recursive scans can affect the workload.

The exercise requires Bash and Python 3 from the repository root in a disposable VM with spare CPU and at least 128 MiB of free memory headroom. It starts one worker for 20 seconds, touches 16 MiB and uses up to roughly one CPU. It does not induce OOM, disable swap, allocate without a bound or tune the host. Skip it on a shared or already distressed system.

## First checks

Record the user symptom, time window, usual workload and recent changes. Take interval samples instead of relying on a single screen:

```bash
date -Is
uptime
nproc
free -h
vmstat 1 5
ps -eo pid,ppid,user,%cpu,%mem,comm --sort=-%cpu
```

The first vmstat CPU/I/O report averages since boot; later reports describe the interval. `ps %cpu` is generally a lifetime average, not the same measurement as an interval CPU sample. `nproc` and some summary tools vary in how they reflect affinity or cgroup limits; record the actual execution boundary.

When sysstat is available:

```bash
mpstat -P ALL 1 5
pidstat -u -r 1 5
```

A single busy CPU can be hidden by a machine-wide average. Do not assume an application can use every CPU just because CPUs exist.

## Evidence and interpretation

| Evidence | Candidate explanation | Next discriminating check |
| --- | --- | --- |
| High application CPU and runnable queue | CPU-bound work, unexpected workload or inefficient code | Workload rate, per-thread activity and interval profiles |
| High load with many blocked tasks | I/O or another uninterruptible wait | I/O latency, device state and blocked-task context |
| High steal time in a guest | Hypervisor contention or scheduling limits | Infrastructure metrics and guest entitlement |
| Low free but substantial available memory | Reclaimable cache rather than immediate exhaustion | Available memory, pressure and application latency |
| Growing process RSS | Increasing live data, caching or a leak | Repeated samples against workload; allocator/application evidence |
| Sustained swap traffic and memory stalls | Active memory pressure | cgroup limits, working set, concurrent workload and OOM events |
| OOM-kill record | A memory limit or kernel allocation failure killed a process | Exact victim, cgroup and event time, not just host free memory |
| Host looks idle but container is throttled | Per-cgroup CPU/memory limits | The process's actual cgroup accounting and limits |

Useful additional observations, when supported:

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
journalctl -k -b --since '30 minutes ago' --no-pager
```

Read kernel records around the incident, looking for out-of-memory evidence without publishing unrelated sensitive logs. For a known PID, inspect `/proc/PID/status`, `/proc/PID/limits` and `/proc/PID/cgroup`. On cgroup v2, inspect memory.events, memory.max and cpu.stat in that process's **actual** cgroup. The host root directory is not automatically the correct container scope.

## Recovery decisions

If a change introduced excess work, consider a controlled rollback or rate reduction before increasing capacity. If one job is responsible, stop it through its manager after confirming identity, owner and impact. Record whether a restart is mitigation or a proven fix for a leak.

Do not drop filesystem caches, disable swap, change swappiness or kill the largest-looking PID without evidence and a recovery plan. Those actions can shift or worsen the symptom. An OOM-killed application may need data/queue integrity checks even after memory returns.

## Follow-along lab

### 1. Record a baseline and start bounded work

```bash
uptime
free -h
load_lab=$(mktemp -d)
python3 05-troubleshooting-and-recovery/labs/bounded_load.py \
  --seconds 20 --mib 16 --ready-file "$load_lab/pid" \
  > "$load_lab/result.log" 2>&1 &
load_pid=$!
for attempt in {1..50}; do
  test -s "$load_lab/pid" && break
  sleep 0.1
done
test -s "$load_lab/pid"
```

Stop if the readiness check fails and inspect result.log. This worker is intentionally bounded, not a full-system stress test.

### 2. Attribute the observed use

```bash
ps -p "$load_pid" -o pid,ppid,stat,etime,%cpu,%mem,comm
grep -E '^(Name|State|VmRSS|VmSize|Threads):' "/proc/$load_pid/status"
vmstat 1 5
```

The process should be a child of your shell and show CPU activity. Its RSS includes the interpreter and touched allocation, so do not expect exactly 16 MiB. Aggregate CPU may look small on a many-core host. This exercise does not establish memory pressure: available capacity should remain healthy.

If you take longer than 20 seconds, the worker may already have exited. An absent PID is expected then, not evidence the tools are broken. Do not increase the resource limits to force a dramatic graph.

## Recovery and verification

```bash
wait "$load_pid"
printf 'worker status: %s\n' "$?"
cat "$load_lab/result.log"
ps -p "$load_pid" -o pid,stat,comm
free -h
vmstat 1 5
```

Expect worker status 0 and a completion message. The final ps normally has no matching row and returns nonzero. The worker releases its memory on exit; exact host totals can still change because other work continues. Compare interval samples and confirm the user's operation separately in a real incident.

The supported lab conclusion is that this known child produced temporary CPU activity and held a bounded resident allocation. It does not prove how to identify every memory leak or reproduce an OOM event.

## Cleanup

After wait has collected the completed worker, remove its two files:

```bash
rm -i -- "$load_lab/pid" "$load_lab/result.log"
rmdir -- "$load_lab"
```

If you must abort before it finishes, identify it with `jobs -l` and `ps -p "$load_pid"`, terminate only that still-running child with `kill -TERM "$load_pid"`, then `wait "$load_pid"`. A terminated worker may return a signal-related nonzero status. Never signal an old numeric PID without rechecking it.

## References

- [vmstat](https://man7.org/linux/man-pages/man8/vmstat.8.html) and [process status](https://man7.org/linux/man-pages/man5/proc_pid_status.5.html).
- [Kernel pressure stall information](https://docs.kernel.org/accounting/psi.html) and [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html).
- [Performance investigation reference](../04-command-reference/performance/performance-investigation-cheat-sheet.md).

[Collection home](README.md) · [Recovery verification](verify-recovery-after-a-fix.md)
