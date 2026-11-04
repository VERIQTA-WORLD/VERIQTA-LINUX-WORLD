| Command | What you can do with it |
| --- | --- |
| `uptime` | Inspect uptime and load averages. |
| `nproc` | Count processing units available to the current process. |
| `nproc --all` | Count installed processing units. |
| `free -h` | Show memory and swap in readable units. |
| `free -m` | Show memory and swap in MiB. |
| `vmstat 1 5` | Take five virtual-memory and CPU samples at one-second intervals. |
| `vmstat -s` | Print cumulative virtual-memory statistics. |
| `mpstat -P ALL 1 5` | Sample CPU activity for every CPU. |
| `pidstat -u 1 5` | Sample per-process CPU activity. |
| `pidstat -r 1 5` | Sample per-process memory activity. |
| `sar -u 1 5` | Sample overall CPU activity with sar. |
| `sar -r 1 5` | Sample memory activity with sar. |
| `sar -W 1 5` | Sample swap-in and swap-out activity. |
| `cat /proc/meminfo` | Read kernel memory accounting fields. |
| `cat /proc/loadavg` | Read load averages and scheduling counts. |
| `cat /proc/pressure/cpu` | Read CPU-stall pressure metrics when supported. |
| `cat /proc/pressure/memory` | Read memory-stall pressure metrics when supported. |
| `cat /proc/pressure/io` | Read I/O-stall pressure metrics when supported. |
| `swapon --show` | List active swap areas. |
| `cat /proc/swaps` | Read kernel swap-area information. |
| `slabtop` | Monitor kernel slab-cache usage. |
| `vmstat -m` | Report slab statistics through vmstat. |
| `smem -tk` | Summarize proportional and other memory usage with totals. |
| `numactl --hardware` | Inspect NUMA nodes and capacity. |
| `numastat` | Inspect NUMA allocation statistics. |
