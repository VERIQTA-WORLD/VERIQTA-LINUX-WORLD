```bash
udevadm --version
udevadm info --query=all --name=/dev/DEVICE
udevadm info --attribute-walk --name=/dev/DEVICE
udevadm monitor --kernel --udev
lspci -vv
lspci -nnk
lsusb -v
lsusb -t
ls -l /dev/serial/by-id
rfkill list
bluetoothctl show
bluetoothctl devices
upower -e
upower -d
acpi -V
sensors
powerprofilesctl list
powerprofilesctl get
```
