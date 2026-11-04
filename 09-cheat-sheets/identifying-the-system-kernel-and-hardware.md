```bash
uname -a
uname -r
uname -m
cat /etc/os-release
hostname
hostnamectl
uptime
uptime -s
arch
getconf LONG_BIT
lscpu
lscpu -e
lsmem
lsblk
lspci -nnk
lsusb
lsusb -t
sudo dmidecode -t system
sudo dmidecode -t memory
sudo lshw -short
sudo hwinfo --short
sensors
inxi -F
udevadm info --query=all --name=/dev/DEVICE
systemd-detect-virt
```
