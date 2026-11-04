| Command | What you can do with it |
| --- | --- |
| `ss -s` | Summarize socket counts. |
| `ss -ltn` | List listening TCP endpoints numerically. |
| `ss -lun` | List bound UDP endpoints numerically. |
| `ss -ltnp` | Include permitted process attribution for TCP listeners. |
| `ss -tn state established` | List established TCP connections. |
| `ss -ltn 'sport = :22'` | Find TCP listeners bound to local port 22. |
| `ss -tn 'dst 192.0.2.1'` | Filter TCP sockets by destination address. |
| `ss -x` | List Unix-domain sockets. |
| `sudo lsof -nP -i` | Inspect network sockets and their owning processes. |
| `ping -c 4 HOST` | Send four IPv4 or default-family ICMP probes. |
| `ping -6 -c 4 HOST` | Send four IPv6 ICMP probes. |
| `tracepath HOST` | Trace path and path-MTU information where supported. |
| `traceroute HOST` | Trace hops toward a host. |
| `traceroute -T -p 443 HOST` | Trace hops using TCP probes to port 443. |
| `mtr --report --report-cycles 10 HOST` | Collect a ten-cycle route and packet-loss report. |
| `nc -vz -w 3 HOST PORT` | Attempt a TCP connection to one port with a three-second timeout. |
| `curl --connect-timeout 5 --max-time 15 -I https://example.com` | Fetch HTTPS response headers with bounded connection and total time. |
| `ethtool INTERFACE` | Inspect Ethernet link settings. |
| `ethtool -S INTERFACE` | Inspect device-specific interface counters. |
| `ip -s link show dev INTERFACE` | Read traffic and error counters for one interface. |
