# Linux networking reference

[Reference library](README.md) · [Glossary](linux-glossary.md) · [Troubleshooting collection](../05-troubleshooting-and-recovery/README.md)

## Scope and environment

Use this page to connect network concepts to observations. You will distinguish interface state, addressing, routes, name resolution, listening sockets, transport, encryption and application responses. Success at one layer does not prove success at every other layer.

The command reference assumes Linux with iproute2 and, where named, glibc or systemd-resolved. Containers and network namespaces can expose a different network view from the host. Commands are read-only observations unless stated otherwise. Substitute your own authorized destination for a placeholder; do not scan other people's systems.

The follow-along exercise needs Bash and Python 3. It uses offline address calculations in a temporary directory. It sends no packets, changes no routes and needs no elevated privileges. Optional Linux observations use `ip`, `ss` and `getent`.

## Reference

### Work through the layers

| Layer or concept | Meaning | Useful question or observation |
| --- | --- | --- |
| Network namespace | A process's network devices, routes, sockets and related state | Are you inspecting the same namespace as the application? |
| Interface | A network attachment such as a physical NIC, bridge, loopback or virtual link | `ip -brief link`; an administrative “up” flag alone does not prove a usable path |
| Link state | Whether the device has the relevant lower-layer connectivity/state | Carrier and operational state depend on interface type |
| MTU | Maximum packet size supported at a relevant link layer | A working small exchange does not prove larger packets or path-MTU discovery work |
| MAC address | Link-layer identifier on applicable networks | Not a routable internet address or universal permanent identity |
| IPv4/IPv6 address | Network-layer address assigned/used in a context | `ip -brief address`; one interface can have several addresses |
| Prefix length | Number of leading bits defining an address block | `/24` and `/64` describe different address-family sizes; they are not host counts by themselves |
| Loopback | Local network communication within a namespace | IPv4 commonly uses `127.0.0.0/8`; IPv6 uses `::1` for loopback |
| Neighbor discovery | Mapping/locating peers on a local link | IPv4 ARP and IPv6 Neighbor Discovery are related functions, not identical protocols |
| Route | Rule-selected path for a destination | `ip route get ADDRESS` asks for a lookup; it does not send an application request |
| Default route | A least-specific route used when no more-specific applicable route wins | A default route is unnecessary for a purely loopback destination |
| Gateway/next hop | Next router or forwarding endpoint | The destination is not necessarily directly connected |
| Policy routing | Route selection using rules and tables beyond a simple destination-only view | A single main-table listing may not explain application traffic |
| DNS | Distributed naming system with different record types | A successful DNS answer does not prove a TCP connection |
| NSS | Configured name-service selection used by consumers such as glibc | `getent ahosts NAME` can include sources other than DNS |
| Resolver cache/stub | A local intermediary for name queries | `/etc/resolv.conf` may identify the stub rather than the actual upstream servers |
| Socket | An endpoint used by a process for communication | Its address family and namespace matter |
| Listening socket | Endpoint awaiting incoming connection requests for a connection-oriented protocol | `ss -lnt` shows TCP listeners in your view; it does not prove remote reachability |
| Bind address | Address selected for a local socket | Loopback binding differs from listening on all suitable local interfaces |
| Port | Transport endpoint identifier associated with a protocol | TCP port 53 and UDP port 53 are distinct endpoints |
| TCP | Reliable ordered byte-stream transport | A completed handshake does not validate application content or TLS identity |
| UDP | Datagram transport | No TCP-style connection handshake; a silent probe does not prove success |
| Firewall/filter policy | Rules that permit, reject, drop or otherwise process traffic | Local and remote policy, forwarding and cloud controls can all matter |
| NAT | Address/port translation | Translation does not inherently provide application authentication or encryption |
| TLS | Encrypted transport with negotiated cryptographic properties | Certificate trust, name matching and time are separate checks from IP reachability |
| HTTP status | Application-protocol response category | A response can be an error; inspect the endpoint's documented expected status/body |
| Proxy | Intermediary handling traffic for a client or server | Environment, client settings and routing can change the actual destination |
| Timeout | A deadline expired before the expected operation completed | Locate whether the delay was in resolution, connect, TLS or application response |

### Read addresses without guessing

| Address/block | Intended interpretation | Boundary |
| --- | --- | --- |
| `127.0.0.1` | Common IPv4 loopback address | Refers to the current network namespace's local stack |
| `::1` | IPv6 loopback address | A service listening only on IPv4 may not answer here |
| `0.0.0.0` in a server bind | Wildcard IPv4 bind | Not a destination to give remote clients; the effective exposure still depends on policy |
| `::` in a server bind | IPv6 wildcard bind | Whether it also accepts IPv4 depends on socket options and system behavior |
| `10.0.0.0/8` | RFC 1918 private IPv4 space | Not globally unique; overlapping networks can cause routing problems |
| `172.16.0.0/12` | RFC 1918 private IPv4 space | Not every `172.*` address is private |
| `192.168.0.0/16` | RFC 1918 private IPv4 space | “Private” does not mean authenticated or encrypted |
| `169.254.0.0/16` | IPv4 link-local space | Has special local-link behavior; do not substitute it for a routed network design |
| `fe80::/10` | IPv6 link-local space | An interface/zone identifier can be required when using a link-local destination |
| `fc00::/7` | IPv6 unique-local address space | Address assignment and routing design still matter; not equivalent to public reachability |
| `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` | IPv4 documentation blocks | Used for examples here; do not send exercise traffic to them |
| `2001:db8::/32` | An IPv6 documentation prefix | Used for examples, not an address assignment for your real service |
| `224.0.0.0/4`, `ff00::/8` | IPv4/IPv6 multicast spaces | Group delivery has its own scope and protocol rules |

Special-purpose addresses have more detailed rules than this table. Consult the [IANA IPv4 registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) and [IPv6 registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml) for authoritative classifications. Python's `is_private` describes its library's non-global/special-address classification, which can change between versions; it is not simply a test for the three RFC 1918 blocks. The exercise below tests explicit prefix membership instead.

### Choose a command for a question

These fragments are independent observations. Replace uppercase placeholders deliberately; do not paste them as if they were actual hostnames or addresses.

| Command | What you can learn | What it does not prove |
| --- | --- | --- |
| `ip -brief address` | Current interface/address summary | Correct remote routing or application health |
| `ip route show` | Routes in the default queried IPv4 table | Every policy-routing table or IPv6 route |
| `ip -6 route show` | Queried IPv6 routes | Equivalent IPv4 reachability |
| `ip rule show` | Policy-routing rule selection | Complete explanation without the referenced route tables |
| `ip route get ADDRESS` | Kernel route lookup for supplied context | That the next hop or application responds |
| `ip neigh show` | Visible neighbor entries and states | Complete network inventory or end-to-end health |
| `getent ahosts NAME` | Address resolution through configured host database facilities | A DNS-only result or availability of the returned services |
| `resolvectl status` | systemd-resolved links, servers and policy when available | Behavior of an application using its own DNS implementation |
| `dig NAME TYPE` | DNS response from the selected resolver, if DNS tools are installed | The same result as NSS or an application's cache |
| `ss -lnt` | Numeric TCP listeners | A listener's HTTP correctness or accessibility from another host |
| `ss -lnu` | Numeric UDP socket information | Successful delivery to each socket |
| `ss -lntp` | TCP listeners plus process details where permitted | Visibility of every other account's process without permission |
| `ping -c 3 ADDRESS` | ICMP echo observations where supported and allowed | TCP/UDP service availability; ICMP can be filtered independently |
| `curl --connect-timeout 3 --max-time 10 URL` | A bounded application request | Correctness unless you also check expected status/content and relevant TLS behavior |

Network tools can generate traffic or disclose internal topology. Use only authorized targets, a bounded timeout and the minimum evidence needed. Avoid using an internet site as a mandatory exercise dependency: access policy, outages, proxies and geography differ around the world.

### Interpret failures by evidence

| Observation | Next question | Tempting but unsupported conclusion |
| --- | --- | --- |
| A name fails but a known address works | Which resolver path, search domain, record family and cache did the application use? | “The entire network is down” |
| No relevant listener appears | Correct namespace, protocol, bind address and service instance? | “The firewall is definitely blocking it” |
| TCP connects but application response is wrong | Correct endpoint, host header, backend and expected content? | “The service is healthy because the port is open” |
| One address family works | Which IPv4/IPv6 listeners and routes exist? | “The hostname always works” |
| A request times out | Which stage reached its deadline, and what did each side observe? | “Timeout proves a dropped firewall packet” |
| A TLS certificate check fails | Correct host name, trust chain, validity time and intermediary? | “Disable verification permanently” |
| A ping fails but HTTPS succeeds | Are ICMP and HTTPS governed by different policies? | “HTTPS success is impossible without ping” |

## Follow along

Calculate membership in explicit documentation prefixes. You will also see why a host address with `/24` can be normalized to a network only when you request that behavior.

<!-- reference:exercise -->
```bash
network_lab=$(mktemp -d) || exit 1
python3 - "$network_lab" <<'PY'
import ipaddress
import json
from pathlib import Path
import sys
root = Path(sys.argv[1])
v4 = ipaddress.ip_network('192.0.2.0/24')
v6 = ipaddress.ip_network('2001:db8::/32')
assert ipaddress.ip_address('192.0.2.10') in v4
assert ipaddress.ip_address('192.0.3.10') not in v4
assert ipaddress.ip_address('2001:db8::10') in v6
assert not v4.overlaps(ipaddress.ip_network('198.51.100.0/24'))
try:
    ipaddress.ip_network('192.0.2.10/24')
except ValueError:
    print('PASS: strict network parsing rejects host bits in a network declaration')
else:
    raise AssertionError('strict parsing unexpectedly accepted host bits')
normalized = ipaddress.ip_network('192.0.2.10/24', strict=False)
assert normalized == v4
result = {'ipv4_network': str(v4), 'ipv4_addresses': v4.num_addresses,
          'ipv6_network': str(v6), 'normalization_requested': str(normalized)}
(root / 'address-check.json').write_text(json.dumps(result, indent=2) + '\n')
assert json.loads((root / 'address-check.json').read_text()) == result
print('PASS: prefix membership, non-overlap and explicit normalization verified offline')
PY
cat "$network_lab/address-check.json"
```

The IPv4 block contains 256 addresses. That is its address count, not a promise of 256 usable host assignments under every subnet/protocol convention. The example deliberately avoids enumerating the enormous IPv6 block.

## Verify your result

Expect two `PASS` lines and JSON showing `192.0.2.0/24`, `256` and `2001:db8::/32`. Explain the difference between a host address, a network declaration and a route.

On Linux, optionally try `ip route get 127.0.0.1`, `getent ahosts localhost` and `ss -lnt`. The route query is a lookup; it does not establish a connection. `localhost` answers depend on local name-service configuration. Your listener list is specific to the current namespace and time. None of these observations prove public internet reachability.

## Cleanup

<!-- reference:cleanup -->
```bash
rm -i -- "$network_lab/address-check.json"
rmdir -- "$network_lab"
```

## Sources

Consult [network_namespaces(7)](https://man7.org/linux/man-pages/man7/network_namespaces.7.html), [ip(7)](https://man7.org/linux/man-pages/man7/ip.7.html), [ipv6(7)](https://man7.org/linux/man-pages/man7/ipv6.7.html), [ip-route(8)](https://man7.org/linux/man-pages/man8/ip-route.8.html), [ss(8)](https://man7.org/linux/man-pages/man8/ss.8.html), [getent(1)](https://man7.org/linux/man-pages/man1/getent.1.html), [curl manual](https://curl.se/docs/manpage.html) and [Python ipaddress documentation](https://docs.python.org/3/library/ipaddress.html). Address references include [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918), [RFC 3927](https://www.rfc-editor.org/rfc/rfc3927), [RFC 4193](https://www.rfc-editor.org/rfc/rfc4193), [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737) and [RFC 3849](https://www.rfc-editor.org/rfc/rfc3849). Read updates and the IANA registries for classifications beyond the examples here.
