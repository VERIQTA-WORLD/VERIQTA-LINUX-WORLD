| Command | What you can do with it |
| --- | --- |
| `iostat -xz 1 5` | Sample extended disk I/O statistics, omitting idle devices. |
| `iostat -dxm 1 5` | Sample extended device statistics with transfer rates in MiB. |
| `pidstat -d 1 5` | Sample per-process I/O rates. |
| `sar -d 1 5` | Sample block-device activity with sar. |
| `sudo iotop -o` | Monitor tasks performing I/O. |
| `vmstat 1 5` | Compare block I/O, runnable tasks and CPU activity. |
| `cat /proc/diskstats` | Read raw kernel disk counters. |
| `cat /proc/sys/fs/file-nr` | Read allocated file-handle accounting and the limit. |
| `cat /proc/sys/fs/file-max` | Read the system-wide file-handle limit. |
| `ls /proc/PID/fd` | List a process's open file descriptors. |
| `lsof -p PID` | Inspect files held open by a process. |
| `ulimit -n` | Print the current shell's open-file limit. |
| `ulimit -a` | Print the current shell's resource limits. |
| `findmnt --target DIRECTORY` | Identify the filesystem containing a path. |
| `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS` | Map storage devices to filesystem types and mount points. |
