| Command | What you can do with it |
| --- | --- |
| `nmcli general status` | Inspect NetworkManager's overall state. |
| `nmcli device status` | Summarize devices managed by NetworkManager. |
| `nmcli device show INTERFACE` | Inspect properties of a network device. |
| `nmcli connection show` | List saved connection profiles. |
| `nmcli connection show --active` | List active connection profiles. |
| `nmcli connection show CONNECTION_NAME` | Inspect one connection profile. |
| `nmcli device wifi list` | Scan or list nearby Wi-Fi networks through NetworkManager. |
| `nmcli --ask device wifi connect SSID` | Connect to a Wi-Fi network with interactive credential prompting. |
| `sudo nmcli connection up CONNECTION_NAME` | Activate a saved connection, potentially changing connectivity. |
| `sudo nmcli connection down CONNECTION_NAME` | Deactivate a connection, potentially disconnecting remote access. |
| `sudo nmcli connection reload` | Reload saved NetworkManager connection files. |
| `nmtui` | Open NetworkManager's interactive terminal interface. |
| `networkctl list` | List links known to systemd-networkd. |
| `networkctl status INTERFACE` | Inspect one link's networkd state. |
| `networkctl lldp` | Inspect LLDP neighbors where available. |
| `networkctl status` | Inspect overall networkd state. |
| `netplan get` | Read merged Netplan configuration. |
| `sudo netplan generate` | Generate backend configuration from Netplan without directly applying it. |
| `sudo netplan try` | Temporarily apply Netplan settings with confirmation and rollback support. |
