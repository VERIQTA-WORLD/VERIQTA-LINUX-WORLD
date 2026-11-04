# Observe disk I/O and latency

Disk capacity and disk performance are separate questions. I/O diagnosis compares throughput, queueing and latency during a specific application symptom.

## Environment and permissions

Linux. `iostat` and `pidstat` are supplied by sysstat on many distributions; `iotop` may be a separate package and need elevated permissions. Samples below do not write test traffic.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `iostat -xz 1 5` | Show extended device statistics; suppress inactive devices. |
| `pidstat -d 1 5` | Sample per-task I/O accounting where permitted. |
| `vmstat 1 5` | Compare blocked tasks, block I/O and CPU wait. |
| `lsblk -o NAME,TYPE,SIZE,MOUNTPOINTS` | Relate reported devices to storage topology. |
| `cat /proc/pressure/io` | Inspect I/O stall pressure where supported. |
| `sudo iotop -o` | Interactive view of tasks doing I/O; implementation/permissions vary, q exits. |

## Follow along

```bash
command -v iostat
lsblk -o NAME,TYPE,SIZE,MOUNTPOINTS
iostat -xz 1 5
vmstat 1 5
```

## Expected results and verification

If iostat is absent, use your package reference to inspect sysstat before installing it on a disposable VM. The first iostat report is since boot; interpret subsequent intervals. `await` includes queueing and service time, while throughput reports transfer rate. No cleanup is required.

## Common mistakes and next checks

`%util` near 100 is not a universal saturation test for parallel devices or RAID. `%iowait` is CPU accounting, not per-request disk latency. Mapped devices can report the same work at multiple layers. Do not run `dd` writes, destructive benchmarks or cache changes on a live volume to “test speed”. Correlate samples with application latency and storage-layer metrics.

## Authoritative references

- [sysstat iostat manual](https://sysstat.github.io/man/iostat.1.html)
- [sysstat pidstat manual](https://sysstat.github.io/man/pidstat.1.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
