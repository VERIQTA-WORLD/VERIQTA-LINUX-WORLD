```bash
nmcli general status
nmcli device status
nmcli device show INTERFACE
nmcli connection show
nmcli connection show --active
nmcli connection show CONNECTION_NAME
nmcli device wifi list
nmcli --ask device wifi connect SSID
sudo nmcli connection up CONNECTION_NAME
sudo nmcli connection down CONNECTION_NAME
sudo nmcli connection reload
nmtui
networkctl list
networkctl status INTERFACE
networkctl lldp
networkctl status
netplan get
sudo netplan generate
sudo netplan try
```
