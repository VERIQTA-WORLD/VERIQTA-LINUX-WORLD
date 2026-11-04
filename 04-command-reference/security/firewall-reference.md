# Inspect firewall policy and plan changes

A host firewall filters traffic. An allowed port still needs an application listener and a valid route; a working local request does not prove the same access is permitted remotely.

## Environment and permissions

Linux with the host’s existing firewall frontend. Ubuntu commonly uses UFW; Fedora/RHEL commonly use firewalld, but inspect the actual host. Do not activate a different frontend over existing policy. Queries often require sudo.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `sudo ufw status verbose` | UFW: inspect status and rules. |
| `sudo ufw status numbered` | UFW: inspect rule numbering; numbers change after deletion. |
| `sudo firewall-cmd --state` | firewalld: check daemon state. |
| `sudo firewall-cmd --get-active-zones` | firewalld: map active interfaces/sources to zones. |
| `sudo firewall-cmd --zone=ZONE --list-all` | firewalld: inspect one runtime zone. |
| `sudo firewall-cmd --permanent --zone=ZONE --list-all` | firewalld: inspect saved policy separately. |
| `sudo nft list ruleset` | Read underlying nftables policy when applicable; do not edit manager-owned tables directly. |

## Follow along

Choose the frontend already configured; these are alternative inspection paths.

```bash
# UFW host:
sudo ufw status verbose
# firewalld host:
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
```

For firewalld, use the actual zone name from the last command with `--zone=ZONE --list-all`. Also inspect its permanent policy separately. No change sequence is intended in this walkthrough.

## Expected results and verification

UFW may report inactive. firewalld may report not running, or active zones with interface/source assignments. Neither proves another filtering layer is absent. Inspection does not require rollback or cleanup.

## Common mistakes and next checks

Before changes, identify SSH’s actual port, source restrictions, IPv4/IPv6 paths and cloud firewall policy; preserve console recovery and test a second session. Firewalld runtime changes and permanent changes differ; a reload can discard runtime-only rules. `ufw enable`, policy flushes and broad deny rules can disconnect you. This reference deliberately requires a host-specific change plan rather than an unconditional enable/reset recipe.

## Authoritative references

- [Ubuntu firewall documentation](https://documentation.ubuntu.com/server/how-to/security/firewalls/)
- [firewall-cmd manual](https://firewalld.org/documentation/man-pages/firewall-cmd.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
