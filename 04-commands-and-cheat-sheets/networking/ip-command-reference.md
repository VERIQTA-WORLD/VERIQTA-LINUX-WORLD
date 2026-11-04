# Inspect interfaces, addresses and routes

`ip` exposes the kernel’s network view. Link state, IP addressing and routing are different layers; an interface can be up without a usable route to a destination.

## Environment and permissions

Linux with iproute2 (`ip`). Read-only queries are normally unprivileged and show only the current network namespace. This page does not change addresses or routes.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `ip -br link` | Summarize interfaces and link state. |
| `ip -br address` | Show interface addresses including prefixes. |
| `ip route show` | Show IPv4 routing entries. |
| `ip -6 route show` | Show IPv6 routing entries. |
| `ip route get ADDRESS` | Ask how the kernel would route to a numeric destination; sends no probe. |
| `ip neigh show` | Show neighbor cache; absence does not by itself prove failure. |
| `ip -s link` | Show per-interface traffic and error counters. |

## Follow along

```bash
ip -br link
ip -br address
ip route show
ip -6 route show
ip route get 192.0.2.1
```

## Expected results and verification

Every normal Linux namespace has loopback (`lo`); other interfaces and routes vary. The final command either prints route/interface/source selection or an unreachable error. `192.0.2.1` is a documentation address and no connection is attempted. No cleanup is needed.

## Common mistakes and next checks

`UP` administrative state differs from carrier state. Route selection does not test DNS or application reachability. `ip address add`, `ip route del` and link changes can immediately disconnect SSH; persistent settings belong to the host’s network manager. Do not copy another host’s interface name.

## Authoritative references

- [ip manual](https://man7.org/linux/man-pages/man8/ip.8.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
