# Read CPU and memory pressure

Performance diagnosis needs time-series context and workload impact. CPU utilization, runnable tasks, available memory and paging describe different parts of the system.

## Environment and permissions

Linux with procps-ng. `pidstat` is commonly in sysstat and is optional here. Read-only samples need no root; process visibility can be restricted.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `uptime` | Show load averages over 1, 5 and 15 minutes. |
| `nproc` | Show processing units available to the current process, subject to tool/version behavior. |
| `free -h` | Show memory accounting; focus on available rather than only free. |
| `vmstat 1 5` | Take five reports; first includes since-boot CPU/I/O averages. |
| `ps -eo pid,comm,%cpu,%mem --sort=-%cpu` | Sort lifetime CPU averages; not an instantaneous interval measurement. |
| `pidstat -u -r 1 5` | Sample per-task CPU and memory over intervals, if installed. |
| `cat /proc/pressure/memory` | Show memory-stall pressure if supported by the kernel. |

## Follow along

```bash
uptime
nproc
free -h
vmstat 1 5
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 11
```

## Expected results and verification

Ignore the first vmstat CPU/I/O row when assessing the current interval. Later rows show run queue (`r`), blocked tasks (`b`), swap traffic (`si`/`so`) and CPU categories. Values vary; the exercise is observation only and needs no cleanup.

## Common mistakes and next checks

Load includes runnable and uninterruptible tasks; it is not CPU percentage. Low free memory can be normal filesystem caching. Sustained paging plus pressure and latency is stronger evidence than swap allocation alone. Containers may show host-level totals in some tools: check cgroup limits before interpreting capacity. Do not drop caches or disable swap as a diagnostic shortcut.

## Authoritative references

- [vmstat manual](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- [free manual](https://man7.org/linux/man-pages/man1/free.1.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
