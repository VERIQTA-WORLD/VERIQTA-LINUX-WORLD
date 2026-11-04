| Command | What you can do with it |
| --- | --- |
| `udevadm --version` | Print the udev tools version. |
| `udevadm info --query=all --name=/dev/DEVICE` | Inspect properties associated with a device. |
| `udevadm info --attribute-walk --name=/dev/DEVICE` | Walk udev device and parent attributes. |
| `udevadm monitor --kernel --udev` | Monitor kernel and udev device events. |
| `lspci -vv` | Inspect detailed PCI device information. |
| `lspci -nnk` | Inspect PCI IDs and associated drivers. |
| `lsusb -v` | Inspect detailed USB descriptors. |
| `lsusb -t` | Inspect USB device topology. |
| `ls -l /dev/serial/by-id` | List stable serial-device identifiers. |
| `rfkill list` | Inspect wireless radio block status. |
| `bluetoothctl show` | Inspect the Bluetooth controller. |
| `bluetoothctl devices` | List known Bluetooth devices. |
| `upower -e` | List devices recognized by UPower. |
| `upower -d` | Dump UPower device information. |
| `acpi -V` | Inspect available ACPI battery, thermal and power data. |
| `sensors` | Read available hardware sensor values. |
| `powerprofilesctl list` | List power profiles. |
| `powerprofilesctl get` | Print the active power profile. |
