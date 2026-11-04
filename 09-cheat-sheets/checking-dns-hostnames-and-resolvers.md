```bash
getent hosts HOSTNAME
getent ahosts HOSTNAME
getent ahostsv4 HOSTNAME
getent ahostsv6 HOSTNAME
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
dig example.com SOA
dig -x 192.0.2.1
dig @DNS_SERVER example.com A
dig +short example.com A
dig +tcp example.com A
dig +dnssec example.com A
dig +time=2 +tries=1 example.com A
host example.com
host -t MX example.com
nslookup example.com
resolvectl status
resolvectl query example.com
resolvectl dns
resolvectl domain
```
