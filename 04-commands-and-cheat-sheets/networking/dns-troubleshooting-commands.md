# Check name resolution

Applications typically use the system name-service configuration; `dig` sends DNS queries. Comparing both paths helps distinguish DNS data from local hosts-file, cache or resolver behavior.

## Environment and permissions

Linux with glibc `getent`; `dig` is commonly provided by `dnsutils` on Debian/Ubuntu or `bind-utils` on RPM systems. `resolvectl` applies only where systemd-resolved is used. Network queries contact configured resolvers.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `getent ahosts example.com` | Resolve through configured name services as many applications do. |
| `dig example.com A` | Query IPv4 DNS data; inspect status and sections. |
| `dig example.com AAAA` | Query IPv6 DNS data. |
| `dig example.com MX` | Inspect mail-exchanger records. |
| `dig +time=2 +tries=1 example.com A` | Bound the time spent waiting for a DNS response. |
| `resolvectl status` | Inspect systemd-resolved per-link DNS state when available. |
| `cat /etc/resolv.conf` | Read resolver configuration; this may be a managed symlink. |

## Follow along

```bash
getent ahosts example.com
dig +time=2 +tries=1 example.com A
cat /etc/resolv.conf
```

## Expected results and verification

Answers and addresses vary. In dig, `status: NOERROR` is a successful DNS response but may have zero answers for the requested type. `NXDOMAIN` means the queried name does not exist; timeout means no reply was received in time. No cleanup is needed.

## Common mistakes and next checks

Dig exit status alone does not establish that a record exists. `SERVFAIL` is not the same as NXDOMAIN. Search suffixes and split DNS may make short names behave differently. Do not replace managed resolv.conf or send internal names to public DNS servers without understanding privacy and routing.

## Authoritative references

- [BIND dig manual](https://bind9.readthedocs.io/en/latest/manpages.html#dig-dns-lookup-utility)
- [getent manual](https://man7.org/linux/man-pages/man1/getent.1.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
