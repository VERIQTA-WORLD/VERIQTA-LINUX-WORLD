```bash
sudo nft list ruleset
sudo nft list tables
sudo nft list table inet TABLE_NAME
sudo nft list chain inet TABLE_NAME CHAIN_NAME
sudo nft -a list ruleset
sudo nft -c -f RULES_FILE
sudo ufw status verbose
sudo ufw status numbered
sudo ufw show raw
sudo ufw app list
sudo ufw app info APP_NAME
sudo ufw --dry-run allow from SOURCE_IP to any port PORT proto tcp
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --get-zones
sudo firewall-cmd --zone=ZONE --list-all
sudo firewall-cmd --permanent --zone=ZONE --list-all
sudo firewall-cmd --zone=ZONE --list-services
sudo firewall-cmd --zone=ZONE --list-ports
sudo firewall-cmd --info-service=SERVICE
sudo iptables -S
sudo iptables -L -n -v
sudo iptables -t nat -L -n -v
sudo ip6tables -S
```
