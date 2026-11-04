```bash
cat /proc/self/cgroup
cat /proc/PID/cgroup
systemd-cgls
systemd-cgtop
systemctl show UNIT -p MemoryCurrent -p MemoryMax -p CPUUsageNSec
cat /sys/fs/cgroup/cgroup.controllers
cat /sys/fs/cgroup/memory.current
cat /sys/fs/cgroup/memory.max
cat /sys/fs/cgroup/cpu.stat
cat /sys/fs/cgroup/pids.current
lsns
lsns -p PID
readlink /proc/PID/ns/net
sudo nsenter --target PID --net ip address
unshare --user --map-root-user id
ulimit -a
prlimit --pid PID
cat /proc/PID/limits
systemd-run --user --scope -p MemoryMax=512M COMMAND
```
