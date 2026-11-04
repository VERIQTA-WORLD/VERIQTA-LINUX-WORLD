# Read systemd journal evidence

`journalctl` queries structured event records. Filtering by boot, time and unit reduces noise while preserving context around a failure.

## Environment and permissions

Linux with systemd-journald. Access to system records depends on root or journal-related group permissions. Volatile journals may disappear at reboot; missing records do not prove no event occurred.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `journalctl -b --no-pager -n 50` | Read the last 50 records for the current boot. |
| `journalctl --list-boots` | Show boots retained in this journal. |
| `journalctl -b -1 --no-pager` | Inspect the previous retained boot. |
| `journalctl -u UNIT --since "1 hour ago"` | Filter one unit by time. |
| `journalctl -p warning -b` | Show warning and more severe events this boot. |
| `journalctl -k -b` | Show kernel records this boot. |
| `journalctl -f` | Follow new records; Ctrl-C stops the viewer. |
| `journalctl --disk-usage` | Report journal storage usage. |

## Follow along

```bash
journalctl --list-boots --no-pager
journalctl -b -n 20 -o short-iso --no-pager
journalctl -u systemd-journald.service -b -n 20 --no-pager
journalctl --disk-usage
```

## Expected results and verification

Records include timestamps and sources; content depends on the machine. Permission warnings or “No entries” require checking access, retention and unit name. These queries do not change retention and need no cleanup.

## Common mistakes and next checks

Keep a time window around the symptom rather than selecting only error lines. Check timezone and boot identity when correlating hosts. Redact tokens, IPs and user data before sharing. Vacuum options delete historical evidence; collect needed records before changing retention.

## Authoritative references

- [journalctl manual](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
