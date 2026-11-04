| Command | What you can do with it |
| --- | --- |
| `sudo nft list ruleset` | Inspect the active nftables ruleset. |
| `sudo nft list tables` | List nftables tables. |
| `sudo nft list table inet TABLE_NAME` | Inspect one nftables table. |
| `sudo nft list chain inet TABLE_NAME CHAIN_NAME` | Inspect one nftables chain. |
| `sudo nft -a list ruleset` | Show nftables rule handles. |
| `sudo nft -c -f RULES_FILE` | Check an nftables rules file without applying it. |
| `sudo ufw status verbose` | Inspect UFW status and policy details. |
| `sudo ufw status numbered` | List UFW rules with their current numbers. |
| `sudo ufw show raw` | Inspect raw rules visible through UFW. |
| `sudo ufw app list` | List UFW application profiles. |
| `sudo ufw app info APP_NAME` | Inspect one UFW application profile. |
| `sudo ufw --dry-run allow from SOURCE_IP to any port PORT proto tcp` | Preview a source-restricted TCP allow rule without applying it. |
| `sudo firewall-cmd --state` | Check whether firewalld is running. |
| `sudo firewall-cmd --get-active-zones` | Map active firewalld zones to interfaces or sources. |
| `sudo firewall-cmd --get-default-zone` | Read the default firewalld zone. |
| `sudo firewall-cmd --get-zones` | List available firewalld zones. |
| `sudo firewall-cmd --zone=ZONE --list-all` | Inspect a zone's runtime policy. |
| `sudo firewall-cmd --permanent --zone=ZONE --list-all` | Inspect a zone's saved permanent policy. |
| `sudo firewall-cmd --zone=ZONE --list-services` | List allowed services in a runtime zone. |
| `sudo firewall-cmd --zone=ZONE --list-ports` | List explicitly allowed ports in a runtime zone. |
| `sudo firewall-cmd --info-service=SERVICE` | Inspect a firewalld service definition. |
| `sudo iptables -S` | Display IPv4 filter-table rules as rule syntax. |
| `sudo iptables -L -n -v` | Inspect IPv4 filter-table counters and rules numerically. |
| `sudo iptables -t nat -L -n -v` | Inspect IPv4 NAT-table counters and rules. |
| `sudo ip6tables -S` | Display IPv6 filter-table rules as rule syntax. |
