| Command | What you can do with it |
| --- | --- |
| `cat /proc/cmdline` | Read the current kernel command line. |
| `cat /proc/version` | Read the kernel version and build string. |
| `lsmod` | List loaded kernel modules. |
| `modinfo MODULE` | Inspect a kernel module's metadata. |
| `modprobe --show-depends MODULE` | Show module dependencies without loading them. |
| `modprobe --dry-run --verbose MODULE` | Preview module-loading actions without loading the module. |
| `sysctl -a` | List readable kernel tunables. |
| `sysctl kernel.hostname` | Read the kernel hostname setting. |
| `sysctl vm.swappiness` | Read the swap aggressiveness setting. |
| `sysctl net.ipv4.ip_forward` | Read the IPv4 forwarding setting. |
| `sysctl fs.file-max` | Read the system-wide file-handle limit. |
| `bootctl status` | Inspect systemd-boot and EFI boot status. |
| `bootctl list` | List boot entries recognized by bootctl. |
| `sudo efibootmgr -v` | Read EFI boot variables and entry details. |
| `systemd-analyze time` | Inspect boot timing. |
| `systemd-analyze critical-chain` | Inspect timing along the boot critical chain. |
| `journalctl -b -k --no-pager` | Read current-boot kernel journal records. |
| `journalctl -b -1 -k --no-pager` | Read previous-boot kernel journal records. |
| `ls -lh /boot` | List boot files with readable sizes. |
| `ls -l /sys/class` | List device-class interfaces exposed by sysfs. |
