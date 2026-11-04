| Command | What you can do with it |
| --- | --- |
| `ip -br link` | Summarize network interface link states. |
| `ip -br address` | Summarize interface addresses and prefixes. |
| `ip -4 address show` | List IPv4 addresses. |
| `ip -6 address show` | List IPv6 addresses. |
| `ip -s link` | Read interface traffic and error counters. |
| `ip -d link show` | Inspect detailed link properties. |
| `ip route show` | List routes in the main IPv4 routing table. |
| `ip -6 route show` | List routes in the main IPv6 routing table. |
| `ip route show table all` | List routes across all tables. |
| `ip rule show` | Inspect policy-routing rules. |
| `ip route get 192.0.2.1` | Ask the kernel which route it would use without sending a probe. |
| `ip neigh show` | Inspect the neighbor cache. |
| `ip maddress show` | Inspect multicast link addresses. |
| `ip tunnel show` | List configured IP tunnels. |
| `ip netns list` | List named network namespaces. |
| `ip monitor` | Monitor network-state notifications. |
| `bridge link show` | Inspect bridge port state. |
| `bridge vlan show` | Inspect bridge VLAN configuration. |
| `bridge fdb show` | Inspect the bridge forwarding database. |
| `cat /etc/resolv.conf` | Read resolver configuration, which may be managed. |
| `cat /etc/hosts` | Read local static hostname mappings. |
| `hostname -I` | Print non-loopback addresses through hostname's interface lookup. |
