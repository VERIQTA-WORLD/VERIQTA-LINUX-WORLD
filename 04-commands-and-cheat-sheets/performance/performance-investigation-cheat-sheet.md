# A first performance investigation

Begin with a measurable symptom: which request, how slow, since when, and compared with what baseline? Collect evidence before changing the workload or system settings.

## Environment and permissions

Linux with procps-ng and util-linux; optional sysstat for deeper sampling. These commands are observations; they do not create artificial load. Restrict shared evidence to non-sensitive data.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `date -Is` | Record sample time and offset (GNU date). |
| `uptime` | Observe load trend and uptime context. |
| `free -h` | Inspect available memory and swap accounting. |
| `vmstat 1 5` | Collect interval CPU, run queue and paging evidence. |
| `df -hT /` | Check capacity on the root filesystem; repeat for the application’s actual data path. |
| `df -i /` | Check inode exhaustion. |
| `ss -s` | Summarize connections. |
| `journalctl -b -p warning -n 50 --no-pager` | Inspect recent warnings, where available. |

## Follow along

```bash
date -Is
uptime
free -h
vmstat 1 5
df -hT /
df -i /
ss -s
```

Write a short observation record: symptom and time window; measured application latency/error rate; relevant host samples; one hypothesis; one additional observation that would disprove it. Repeat at the same workload after any separately planned change.

## Expected results and verification

A useful result is an evidence-supported next question, not a declaration that the server is healthy. High runnable queues with CPU busy suggest checking CPU consumers; blocked tasks and latency suggest I/O; paging plus stalls suggest memory pressure. These are hypotheses to test. No cleanup is needed.

## Common mistakes and next checks

One quiet sample cannot rule out an intermittent problem. Root filesystem capacity does not describe a separately mounted application volume. A restart can erase state and hide the cause. Compare before and after with equal time windows and workload; system averages can conceal one slow dependency.

## Authoritative references

- [Linux /proc reference](https://man7.org/linux/man-pages/man5/proc.5.html)
- [vmstat manual](https://man7.org/linux/man-pages/man8/vmstat.8.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
