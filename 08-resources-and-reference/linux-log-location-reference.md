# Find and interpret Linux logs

[Reference library](README.md) · [Configuration reference](linux-configuration-file-reference.md) · [Log operations](../06-system-administration/log-management-and-rotation.md)

## Scope and environment

Use this page when you need to find evidence for an event without assuming that every distribution writes the same files. Start with the producing component, then identify its logging destination, access controls, timestamps and retention.

The reference covers common systemd-journal and file-based arrangements. A container, appliance, remote logging platform or application can use another design. The exercise needs Bash, Python 3 and `gzip`, with an ordinary account. You create and read synthetic events in a temporary directory. You do not alter journal retention, rotate system logs or collect another user's activity.

## Reference

### Follow the evidence from source to storage

A log has several distinct properties:

| Property | Question to ask | Why the answer matters |
| --- | --- | --- |
| Producer | Which process, kernel subsystem or application emitted it? | A reverse proxy and its backend can report different parts of the same request |
| Destination | Journal, text file, standard output, socket or remote collector? | An absent local text file does not prove no event was recorded |
| Scope | Which host, boot, unit, container, account or namespace? | A correct query in the wrong scope can return misleading silence |
| Access | Can your account read this source? | Partial results and permission notices are evidence limitations |
| Time | UTC, local time, monotonic time, application time or receipt time? | Clock changes, time zones and ingestion delay can alter apparent order |
| Retention | Rotation, size limits, boot-only storage or remote policy? | An event can have expired even if logging works now |
| Integrity | Is it original evidence, an export or a transformed copy? | Compression, filtering and redaction should preserve a traceable original where required |
| Meaning | Is this a symptom, an action, a consequence or a confirmed cause? | A nearby warning is not automatically the cause of an outage |

Logs complement service state, metrics, traces and direct application checks. A healthy-looking log message does not prove the current service is ready. Avoid posting raw logs publicly: URLs, account names, tokens, customer data and private network details can appear in ordinary messages.

### Journald and kernel evidence

| Source or query | What it can show | Important boundary |
| --- | --- | --- |
| `journalctl --list-boots` | Boots retained in the journal visible to your account | Missing older boots can reflect storage/retention or access, not absence of reboot |
| `journalctl -b -n 20 --no-pager` | Last visible entries from the current boot | Last 20 messages are a sample, not a complete incident timeline |
| `journalctl -b -u UNIT --no-pager` | Current-boot entries associated with a named unit | Substitute an actual unit; application output can go elsewhere |
| `journalctl -b -k --no-pager` | Current-boot kernel messages available through the journal | Access and collection policy vary |
| `journalctl --since TIME --until TIME --utc --no-pager` | Time-window query rendered in UTC | Replace the placeholders and check the accepted time syntax; timestamp conversion does not repair a wrong clock |
| `journalctl --disk-usage` | Space used by journal files visible to the query | Not the complete disk usage of every logging destination |
| `dmesg` | Current kernel ring-buffer view when permitted | Ring buffers are finite and access may be restricted; this is not a persistent boot history |
| `/run/log/journal` | Volatile journal storage when used | Often lost at reboot; do not assume it is a text-file tree |
| `/var/log/journal` | Persistent journal storage when configured | Directory existence alone does not establish complete retention or successful collection |

`Storage=auto`, `persistent`, `volatile` and `none` have distinct journald semantics. Distribution presets, directory setup and forwarding settings also matter. Read the installed [journald configuration manual](https://man7.org/linux/man-pages/man5/journald.conf.5.html) rather than assuming persistent logs are always enabled. Journal files use a binary format; read them with journal-aware tools, not a text editor.

For a service, `systemctl show UNIT -p StandardOutput -p StandardError` helps identify systemd's configured output routing. It does not prove that the application actually writes useful events there. A process may separately open a file or send events to another collector.

### File locations you may encounter

These are candidates to inspect, not files you must create or expect on every distribution.

| Candidate | Common producer or purpose | Alternatives and cautions |
| --- | --- | --- |
| `/var/log/syslog` | General syslog-style messages on some Debian/Ubuntu installations | Requires a configured file-logging service; minimal/cloud systems can rely on the journal |
| `/var/log/messages` | General messages on some other distributions | Not a universal replacement for the journal or every application log |
| `/var/log/auth.log` | Authentication-related syslog messages on some systems | Often absent without the relevant syslog configuration; sensitive account/network information |
| `/var/log/secure` | Authentication-related messages on some RPM-family setups | Distribution version and syslog policy determine use |
| `/var/log/kern.log` | Kernel messages routed to a file by configured logging | The journal/kernel ring buffer can be the actual source instead |
| `/var/log/audit/audit.log` | Linux Audit events when auditd is configured | Structured records can span multiple entries; permissions and rotation are significant |
| `/var/log/dpkg.log` | dpkg package operations | Rotated archives may hold older entries; not every APT decision is in this file |
| `/var/log/apt/history.log` | APT transaction history when recorded | Local logs do not prove repository trust or successful application behavior after an upgrade |
| `/var/log/apt/term.log` | APT-associated terminal output | Can contain more detail than transaction summaries; access and rotation vary |
| `/var/log/dnf*` | DNF-related logging on applicable versions | DNF generations and configuration change filenames; inspect the installed implementation |
| `/var/log/nginx/*`, `/var/log/apache2/*`, `/var/log/httpd/*` | Common web-server log directories | Virtual hosts, containers and custom configurations can route each access/error stream differently |
| `/var/log/wtmp`, `/var/log/btmp` | Login/accounting records on systems that maintain them | Binary accounting data; use the appropriate installed reader, not `cat` |
| `/var/log/lastlog` or alternative accounting stores | Last-login information where supported | Newer implementations can use other databases; absence is not proof that no account logged in |
| User application data/state directories | User-scoped application logs or history | Consult the application; do not assume every app uses `~/.local/state` |
| Container runtime or orchestrator logs | Captured standard output/error and runtime events | Logging driver, rotation, pod/container identity and previous instances matter |
| Remote collector | Centrally retained or transformed events | Local access does not imply collector access; ingestion gaps and field normalization need separate checks |

Use package documentation and the application's configuration to locate the actual path. Reading every file under `/var/log` with elevated privileges is neither necessary nor a good learning exercise. Request only the access appropriate to the question.

### Query and preserve deliberately

1. Identify one event or symptom and a narrow time range. Record the time zone.
2. Confirm the service, instance, boot and account context.
3. Query a bounded sample. Check stderr for access or parsing problems rather than suppressing it.
4. Distinguish “source does not exist,” “source is unreadable,” “query failed” and “query returned no matching events.”
5. Preserve originals according to your organization's policy before redacting or transforming copies. A checksum detects later byte changes; it does not establish who originally produced the content.
6. Correlate independent observations before assigning a cause. Use request IDs when the application provides them, and understand how they propagate.

For compressed text archives, `gzip -cd FILE.gz` writes decompressed bytes to standard output without replacing the archive. `gzip -t FILE.gz` checks compressed-stream integrity, not the truth or completeness of the events. A collector accepting a message does not guarantee durable retention forever.

## Follow along

Create two explicitly synthetic UTC events, preserve an archive and verify that decompression returns exactly the same bytes. You will also test a filter with no matching event, while keeping that result separate from a missing source.

<!-- reference:exercise -->
```bash
logs_lab=$(mktemp -d) || exit 1
printf '%s\n' \
  '2026-01-01T12:00:00Z demo event=start request=example-1' \
  '2026-01-01T12:00:01Z demo event=ready request=example-1' > "$logs_lab/events.log"
gzip -c "$logs_lab/events.log" > "$logs_lab/events.log.gz"
gzip -t "$logs_lab/events.log.gz"
gzip -cd "$logs_lab/events.log.gz" > "$logs_lab/restored.log"
cmp -- "$logs_lab/events.log" "$logs_lab/restored.log"
echo 'PASS: archived events restore byte for byte'
python3 - "$logs_lab" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
lines = (root / 'restored.log').read_text().splitlines()
assert len(lines) == 2
assert all('request=example-1' in line for line in lines)
matches = [line for line in lines if 'event=failed' in line]
assert matches == []
assert not (root / 'missing.log').exists()
print('PASS: readable source has no failed event; a missing source is a different condition')
PY
```

## Verify your result

Expect two `PASS` lines. Both original events and the compressed archive should still exist. The empty filter means only that these two synthetic lines contain no `event=failed` value. It does not establish that a real service was healthy, that no event was dropped, or that the timestamps reflect a real clock.

On a Linux system using journald, you can separately try `journalctl --list-boots` and `journalctl --disk-usage` without changing retention. Note permission warnings honestly. Do not run vacuum or deletion commands to complete this page.

## Cleanup

<!-- reference:cleanup -->
```bash
rm -i -- "$logs_lab/events.log" "$logs_lab/events.log.gz" "$logs_lab/restored.log"
rmdir -- "$logs_lab"
```

## Sources

Use [journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html), [journald.conf](https://man7.org/linux/man-pages/man5/journald.conf.5.html), [systemd.exec output routing](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html), [rsyslog documentation](https://www.rsyslog.com/doc/), [Linux Audit documentation](https://github.com/linux-audit/audit-documentation), [dpkg manual](https://manpages.debian.org/dpkg/dpkg.1.en.html), [DNF5 logging configuration](https://dnf5.readthedocs.io/en/latest/dnf5.conf.5.html), [GNU gzip manual](https://www.gnu.org/software/gzip/manual/gzip.html) and [Docker logging documentation](https://docs.docker.com/engine/logging/). The directory candidates above describe common arrangements; the actual package and configuration determine your destinations.
