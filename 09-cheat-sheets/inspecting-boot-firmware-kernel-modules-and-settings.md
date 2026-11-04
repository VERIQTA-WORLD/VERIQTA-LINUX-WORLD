```bash
cat /proc/cmdline
cat /proc/version
lsmod
modinfo MODULE
modprobe --show-depends MODULE
modprobe --dry-run --verbose MODULE
sysctl -a
sysctl kernel.hostname
sysctl vm.swappiness
sysctl net.ipv4.ip_forward
sysctl fs.file-max
bootctl status
bootctl list
sudo efibootmgr -v
systemd-analyze time
systemd-analyze critical-chain
journalctl -b -k --no-pager
journalctl -b -1 -k --no-pager
ls -lh /boot
ls -l /sys/class
```
