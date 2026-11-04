```bash
ss -s
ss -ltn
ss -lun
ss -ltnp
ss -tn state established
ss -ltn 'sport = :22'
ss -tn 'dst 192.0.2.1'
ss -x
sudo lsof -nP -i
ping -c 4 HOST
ping -6 -c 4 HOST
tracepath HOST
traceroute HOST
traceroute -T -p 443 HOST
mtr --report --report-cycles 10 HOST
nc -vz -w 3 HOST PORT
curl --connect-timeout 5 --max-time 15 -I https://example.com
ethtool INTERFACE
ethtool -S INTERFACE
ip -s link show dev INTERFACE
```
