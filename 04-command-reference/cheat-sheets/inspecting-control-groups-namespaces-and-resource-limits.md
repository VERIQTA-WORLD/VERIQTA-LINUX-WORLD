| Command | What you can do with it |
| --- | --- |
| `cat /proc/self/cgroup` | Read the current process's cgroup membership. |
| `cat /proc/PID/cgroup` | Read another process's cgroup membership. |
| `systemd-cgls` | Display the systemd cgroup tree. |
| `systemd-cgtop` | Monitor cgroup resource usage. |
| `systemctl show UNIT -p MemoryCurrent -p MemoryMax -p CPUUsageNSec` | Inspect unit memory accounting, memory limit and CPU accounting. |
| `cat /sys/fs/cgroup/cgroup.controllers` | List controllers exposed by a cgroup v2 hierarchy. |
| `cat /sys/fs/cgroup/memory.current` | Read memory consumption for the referenced cgroup v2 root. |
| `cat /sys/fs/cgroup/memory.max` | Read its configured memory limit, if that file is exposed. |
| `cat /sys/fs/cgroup/cpu.stat` | Read its CPU accounting. |
| `cat /sys/fs/cgroup/pids.current` | Read its process count. |
| `lsns` | List visible Linux namespaces. |
| `lsns -p PID` | List namespaces associated with a process. |
| `readlink /proc/PID/ns/net` | Inspect a process's network-namespace identifier. |
| `sudo nsenter --target PID --net ip address` | Inspect addresses inside an authorized process's network namespace. |
| `unshare --user --map-root-user id` | Create a user namespace mapping your identity to namespace root. |
| `ulimit -a` | Show current shell resource limits. |
| `prlimit --pid PID` | Inspect a process's resource limits. |
| `cat /proc/PID/limits` | Read the kernel's resource-limit report for a process. |
| `systemd-run --user --scope -p MemoryMax=512M COMMAND` | Run a command in a user scope with a 512 MiB memory limit. |
