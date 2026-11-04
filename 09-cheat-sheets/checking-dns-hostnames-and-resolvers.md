| Command | What you can do with it |
| --- | --- |
| `getent hosts HOSTNAME` | Resolve a hostname through configured name services. |
| `getent ahosts HOSTNAME` | Resolve host addresses through the system's address lookup interface. |
| `getent ahostsv4 HOSTNAME` | Resolve IPv4 addresses through configured name services. |
| `getent ahostsv6 HOSTNAME` | Resolve IPv6 addresses through configured name services. |
| `dig example.com A` | Query DNS A records. |
| `dig example.com AAAA` | Query DNS AAAA records. |
| `dig example.com MX` | Query DNS mail-exchanger records. |
| `dig example.com NS` | Query DNS authoritative name-server records. |
| `dig example.com TXT` | Query DNS text records. |
| `dig example.com SOA` | Query DNS start-of-authority data. |
| `dig -x 192.0.2.1` | Perform a reverse DNS lookup. |
| `dig @DNS_SERVER example.com A` | Query a selected DNS server. |
| `dig +short example.com A` | Print a compact A-record answer. |
| `dig +tcp example.com A` | Query DNS over TCP. |
| `dig +dnssec example.com A` | Request DNSSEC-related response data without proving validation. |
| `dig +time=2 +tries=1 example.com A` | Bound DNS query timeout and retry count. |
| `host example.com` | Resolve a name using the host utility. |
| `host -t MX example.com` | Query mail exchangers with host. |
| `nslookup example.com` | Query a name with nslookup. |
| `resolvectl status` | Inspect systemd-resolved per-link resolver state. |
| `resolvectl query example.com` | Resolve a name through systemd-resolved. |
| `resolvectl dns` | Inspect configured per-link DNS servers. |
| `resolvectl domain` | Inspect per-link DNS search and routing domains. |
