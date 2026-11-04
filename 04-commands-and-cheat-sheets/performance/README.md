# Performance

Measure the workload symptom, sample over time and form a testable hypothesis before tuning.

## Detailed references

1. [Read CPU and memory pressure](cpu-and-memory-commands.md)
2. [Observe disk I/O and latency](disk-io-commands.md)
3. [A first performance investigation](performance-investigation-cheat-sheet.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Show load averages over 1, 5 and 15 minutes. | `uptime` | [Read CPU and memory pressure](cpu-and-memory-commands.md) |
| Show processing units available to the current process, subject to tool/version behavior. | `nproc` | [Read CPU and memory pressure](cpu-and-memory-commands.md) |
| Show memory accounting; focus on available rather than only free. | `free -h` | [Read CPU and memory pressure](cpu-and-memory-commands.md) |
| Show extended device statistics; suppress inactive devices. | `iostat -xz 1 5` | [Observe disk I/O and latency](disk-io-commands.md) |
| Sample per-task I/O accounting where permitted. | `pidstat -d 1 5` | [Observe disk I/O and latency](disk-io-commands.md) |
| Compare blocked tasks, block I/O and CPU wait. | `vmstat 1 5` | [Observe disk I/O and latency](disk-io-commands.md) |
| Record sample time and offset (GNU date). | `date -Is` | [A first performance investigation](performance-investigation-cheat-sheet.md) |
| Observe load trend and uptime context. | `uptime` | [A first performance investigation](performance-investigation-cheat-sheet.md) |
| Inspect available memory and swap accounting. | `free -h` | [A first performance investigation](performance-investigation-cheat-sheet.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
