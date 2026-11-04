# DNS resolution is failing

Applications usually ask the operating system to resolve names. That lookup can consult local files, DNS, caches or directory services. A DNS query tool and an application can therefore return different results without either command being defective.

## Environment and permissions

Linux examples use glibc `getent`, BIND `dig` and optional systemd-resolved. Debian/Ubuntu commonly package dig in dnsutils; Fedora/RHEL commonly use bind-utils. Read-only queries normally need no root but contact configured resolvers. Query only non-sensitive test names unless you have approval to disclose an internal name to that resolver.

The lab uses a reserved `.invalid` name and localhost, plus a temporary application-setting file. It does not edit `/etc/hosts`, `/etc/resolv.conf`, network profiles or DNS records. External DNS results require a functioning configured resolver; the localhost comparison should work through normal system name services.

## First checks

Record the exact name, requested record type, client location, time, expected answer and whether the issue affects short names, fully qualified names or both. Check the configured resolver path before choosing a replacement server.

```bash
getent ahosts HOSTNAME
dig +time=2 +tries=1 HOSTNAME A
dig +time=2 +tries=1 HOSTNAME AAAA
cat /etc/nsswitch.conf
ls -l /etc/resolv.conf
cat /etc/resolv.conf
```

Substitute a verified hostname. Inspect hosts: in nsswitch.conf where applicable. resolv.conf can be a generated file or symlink to a local stub resolver; a loopback nameserver entry can be intentional.

If systemd-resolved actually owns resolution on this machine:

```bash
resolvectl status
resolvectl query HOSTNAME
```

Per-link DNS domains and VPN policy may explain why an internal name works only on one interface. Do not infer that all queries use one global server.

## Evidence and interpretation

| Result | Meaning and limits | Next check |
| --- | --- | --- |
| NXDOMAIN | The responding DNS path reports that name does not exist | Exact name, suffix, authoritative data and negative-cache timing |
| NOERROR with no requested answer | Response succeeded but no matching data may be present | Record type, aliases and answer/authority sections |
| SERVFAIL | The resolver could not complete the query | Resolver logs, upstream reachability, DNSSEC and authoritative health |
| REFUSED | The server declines this query | Client source and resolver policy |
| Timeout | No usable response before the deadline | Resolver address, local service, route and UDP/TCP filtering |
| getent succeeds, dig differs | Application name services may use a source other than DNS | hosts file, NSS order, caches, split DNS and exact query |
| dig succeeds, application fails | Different lookup path, cache, family or application configuration | Actual application hostname and resolver behavior |
| Address is valid but connection fails | Resolution may be working while the service path fails | Routing, listener, TLS and application checks |

Dig's exit status alone does not prove a record exists: inspect the DNS status and answer. The TTL describes caching behavior; waiting for it does not correct an erroneous authoritative record. Check whether you are reading a cached answer before concluding a change failed.

## Recovery decisions

Correct a misspelled application name at its configuration source. Correct DNS data at its authorized owner. If a network manager owns resolver settings, change the appropriate managed configuration rather than replacing a generated file. Preserve the previous settings and test the same internal and external names after any resolver change.

A public DNS server may not know private zones and may disclose queried names. Flushing a cache can change timing but cannot repair wrong data or a broken route. When SERVFAIL involves DNSSEC, do not disable validation as an unexplained permanent workaround.

## Follow-along lab

### 1. Reproduce an invalid application hostname

```bash
dns_lab=$(mktemp -d)
printf 'linux-world.invalid\n' > "$dns_lab/hostname"
lab_hostname=$(cat "$dns_lab/hostname")
getent ahosts "$lab_hostname"
printf 'lookup status: %s\n' "$?"
```

Expect no usable address and a nonzero lookup status on a normally configured system. `.invalid` is reserved for names intended to be invalid. A timeout or unusual answer needs interpretation rather than assuming NXDOMAIN was received.

If dig is installed, compare its DNS view:

```bash
dig +time=2 +tries=1 linux-world.invalid A
```

A working recursive resolver normally returns NXDOMAIN. If the resolver is unavailable, this may time out instead. Those are different failure modes. This exercise does not require changing the resolver to force a particular response.

### 2. Compare with a known local name

```bash
getent ahosts localhost
```

Expect loopback address data, commonly 127.0.0.1 and/or ::1. The exact rows can repeat for socket types. Localhost frequently comes from local name services rather than a public DNS record. If this fails, inspect the local naming setup and stop before claiming the proposed application fix is valid.

### 3. Correct only the exercise configuration

```bash
printf 'localhost\n' > "$dns_lab/hostname"
lab_hostname=$(cat "$dns_lab/hostname")
getent ahosts "$lab_hostname"
printf 'lookup status: %s\n' "$?"
```

## Recovery and verification

Expect loopback data and status 0 after the exercise setting changes. This establishes that the application setting names a resolvable local host. It does **not** prove any application is listening there. Pair resolution with [reachability checks](server-is-unreachable.md) and an actual request before declaring service recovery.

For a real DNS change, compare the intended record, the affected client's system lookup and the application result. Account for positive and negative caching, VPN domains and both address families. Preserve the before/after names, responder, DNS status and observation times.

## Cleanup

```bash
rm -i -- "$dns_lab/hostname"
rmdir -- "$dns_lab"
```

No system resolver setting or DNS record changed. Record whether your external query returned NXDOMAIN, timed out or produced another response.

## References

- [BIND dig documentation](https://bind9.readthedocs.io/en/latest/manpages.html#dig-dns-lookup-utility).
- [getent](https://man7.org/linux/man-pages/man1/getent.1.html) and [resolver configuration](https://man7.org/linux/man-pages/man5/resolv.conf.5.html).
- [RFC 2606 reserved names](https://www.rfc-editor.org/rfc/rfc2606.html).
- [DNS command reference](../04-commands-and-cheat-sheets/networking/dns-troubleshooting-commands.md).

[Collection home](README.md) · [Troubleshooting method](linux-troubleshooting-method.md)
