# Inspect listening and connected sockets

A socket is a communication endpoint. `ss` helps answer whether an application is listening, where it is bound, and whether connections exist.

## Environment and permissions

Linux with iproute2. Ordinary users can inspect many socket details; process attribution for other users often needs root. No listener or firewall is created by this walkthrough.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `ss -ltn` | List listening TCP sockets using numeric addresses and ports. |
| `ss -lun` | List bound UDP sockets; UDP does not have TCP’s handshake states. |
| `ss -tn state established` | List established TCP connections. |
| `ss -ltnp` | Include process details where permitted. |
| `ss -ltn 'sport = :22'` | Filter listeners by local port 22. |
| `ss -s` | Summarize socket counts. |

## Follow along

```bash
ss -ltn
ss -lun
ss -tn state established
ss -ltn 'sport = :22'
ss -s
```

## Expected results and verification

Rows show local/peer endpoints and queue fields. Empty output beneath the header for port 22 means no matching TCP listener in this namespace at that moment. `127.0.0.1` is loopback; `0.0.0.0` is an IPv4 wildcard bind. No cleanup is required.

## Common mistakes and next checks

A listener does not prove remote access: firewall, routing and application policy still matter. An IPv6 wildcard may or may not also accept IPv4, depending on socket settings. Missing `users:` fields can be a permissions issue. Queue interpretation differs between listening and established sockets.

## Authoritative references

- [ss manual](https://man7.org/linux/man-pages/man8/ss.8.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
