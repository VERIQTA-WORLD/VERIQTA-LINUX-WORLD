```bash
iostat -xz 1 5
iostat -dxm 1 5
pidstat -d 1 5
sar -d 1 5
sudo iotop -o
vmstat 1 5
cat /proc/diskstats
cat /proc/sys/fs/file-nr
cat /proc/sys/fs/file-max
ls /proc/PID/fd
lsof -p PID
ulimit -n
ulimit -a
findmnt --target DIRECTORY
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
```
