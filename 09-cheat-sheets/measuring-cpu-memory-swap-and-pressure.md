```bash
uptime
nproc
nproc --all
free -h
free -m
vmstat 1 5
vmstat -s
mpstat -P ALL 1 5
pidstat -u 1 5
pidstat -r 1 5
sar -u 1 5
sar -r 1 5
sar -W 1 5
cat /proc/meminfo
cat /proc/loadavg
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
swapon --show
cat /proc/swaps
slabtop
vmstat -m
smem -tk
numactl --hardware
numastat
```
