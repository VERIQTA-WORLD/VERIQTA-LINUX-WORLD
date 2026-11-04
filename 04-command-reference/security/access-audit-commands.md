# Inspect account and access evidence

Access review asks who can log in, who has administrative power, which sessions are active and what evidence exists. A command snapshot is an input to that review, not a complete security audit.

## Environment and permissions

Linux with NSS tools and optional sudo/systemd. Read access varies; never publish raw account, journal, sudo-policy or public-key inventories without review. This walkthrough changes no policy.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `id` | Show your effective identity and groups. |
| `getent passwd` | Enumerate accounts exposed by configured identity sources; enumeration may be incomplete. |
| `getent group sudo` | Inspect one common Debian-family administrator group. |
| `getent group wheel` | Inspect one common RPM-family administrator group. |
| `sudo -l` | Inspect effective sudo policy; group membership alone is not proof. |
| `who` | Inspect recorded login sessions; records may be absent. |
| `last -n 10` | Read recent wtmp records if the utility and database exist. |
| `journalctl -u ssh -u sshd --since today` | Look for SSH service events under common names; discover the actual unit on your host. |

## Follow along

```bash
id
getent passwd "$(id -un)"
who
sudo -l
```

## Expected results and verification

Compare your resolved account and groups with the permissions reported by sudo. A denial or an empty session list is valid evidence with limitations. No account, key or policy changes occur; no cleanup is needed.

## Common mistakes and next checks

A login shell field does not prove remote access is possible. Sudo rules can come from includes or identity services. `last` records and logs can be rotated, missing or tampered with. Do not lock accounts, remove authorized keys or rewrite sudoers based on a name alone. Verify ownership and a recovery route first.

## Authoritative references

- [getent manual](https://man7.org/linux/man-pages/man1/getent.1.html)
- [sudoers manual](https://www.sudo.ws/docs/man/sudoers.man/)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
