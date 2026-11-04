| Command | What you can do with it |
| --- | --- |
| `uname -a` | Print kernel and machine identification. |
| `uname -r` | Print the running kernel release. |
| `uname -m` | Print machine architecture. |
| `cat /etc/os-release` | Read distribution identification. |
| `hostname` | Print the system hostname. |
| `hostnamectl` | Inspect hostname and system identity through systemd. |
| `uptime` | Print uptime and load averages. |
| `uptime -s` | Print system start time. |
| `arch` | Print architecture using arch. |
| `getconf LONG_BIT` | Print the system's long-integer bit width. |
| `lscpu` | Summarize CPU architecture and topology. |
| `lscpu -e` | Display CPUs in an extended table. |
| `lsmem` | Summarize memory block layout. |
| `lsblk` | List block devices. |
| `lspci -nnk` | List PCI devices with IDs and kernel drivers. |
| `lsusb` | List USB devices. |
| `lsusb -t` | Display USB topology. |
| `sudo dmidecode -t system` | Read firmware-provided system information. |
| `sudo dmidecode -t memory` | Read firmware-provided memory information. |
| `sudo lshw -short` | Summarize detected hardware. |
| `sudo hwinfo --short` | Summarize hardware through hwinfo. |
| `sensors` | Read available hardware sensors. |
| `inxi -F` | Print a system summary using inxi. |
| `udevadm info --query=all --name=/dev/DEVICE` | Inspect udev properties for a device. |
| `systemd-detect-virt` | Identify the virtualization environment, if detected. |
