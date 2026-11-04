# Log management and rotation

Logs support diagnosis, security review and accountability. Manage them as data with owners, retention, access controls and capacity limits. Rotating files is only one part: the writer must continue writing to the intended destination, and retained records must remain usable.

## Environment and permissions

Linux systems may use journald, application files, syslog forwarding or several together. Discover the actual writer and owner. System log queries and rotation policy changes can require authorization. Logs, command arguments and captures can contain credentials or personal data; keep evidence private and share only reviewed redactions.

The lab needs logrotate but no root. It rotates one private temporary log using an isolated configuration and state file. It never reads `/etc/logrotate.conf`, rotates a host log or signals a real application. Runtime validation of this lab remains pending on Linux.

## Before you begin

Define required events, timestamps/time synchronization, sensitivity, expected volume, retention obligations and who may read/delete records. Identify local versus remote retention, forwarding queues and what happens when the collector is unavailable. Never invent a retention period without the service/data owner's policy.

Check the filesystem containing logs, inode headroom and whether files are held open after deletion. For incidents or legal holds, preserve the relevant records before changing rotation or retention.

## Operating procedure

### 1. Discover storage and delivery

```bash
journalctl --disk-usage
journalctl -b -n 20 -o short-iso --no-pager
df -hT /var/log
df -i /var/log
systemctl list-timers --all --no-pager
```

Check the actual application paths too. Journals can be volatile or persistent depending on effective configuration. Local records being visible does not prove central delivery succeeded. Test a uniquely identified, non-sensitive event through the intended collector path and confirm its timestamp, labels and arrival.

### 2. Review file rotation semantics

Inspect the owning application's reopen mechanism. Rename/create rotation leaves an existing file descriptor pointing to the old file until the writer reopens it. A supported signal/reload or built-in rotation can solve that. `copytruncate` can lose records during its copy/truncate race and is not a universal default.

Keep configuration, owner/group, new-file mode, compression timing, retention and state-file ownership explicit. A timer's cadence limits how often size criteria can be evaluated; a size threshold alone does not guarantee a strict maximum file size.

### 3. Preview before applying policy

For a reviewed host configuration, `logrotate --debug CONFIG_FILE` reports intended decisions without rotating logs or updating its state. Inspect included files and scripts: actual runs can execute postrotate commands with substantial privilege. Validate the exact configuration that the scheduled job uses.

Do not vacuum journals or force rotation merely to hide a capacity incident. Investigate growth, retention and open-file behavior using [capacity troubleshooting](../05-troubleshooting-and-recovery/disk-space-or-inodes-are-exhausted.md).

## Follow-along lab

### 1. Create one private log and isolated policy

```bash
log_lab=$(mktemp -d)
chmod 700 "$log_lab"
printf 'event one\nevent two\n' > "$log_lab/events.log"
chmod 600 "$log_lab/events.log"
printf '%s\n' \
  "\"$log_lab/events.log\" {" \
  '    size 1' \
  '    rotate 2' \
  '    missingok' \
  '    notifempty' \
  '    nocompress' \
  '    create 0600' \
  '}' \
  > "$log_lab/rotation.conf"
chmod 600 "$log_lab/rotation.conf"
cat "$log_lab/rotation.conf"
```

The path is quoted for logrotate, and the private parent directory avoids insecure shared-directory handling. No application keeps this sample file open, so a reopen action is not required for this limited exercise.

### 2. Preview and verify that preview changed nothing

```bash
logrotate --debug --state "$log_lab/state" "$log_lab/rotation.conf"
cat "$log_lab/events.log"
test ! -e "$log_lab/events.log.1"
printf 'preview left original intact: %s\n' "$?"
```

Expect both original events, no rotated file and status 0 from the test. If the tool is missing or rejects permissions/options, stop and record the difference; do not run the host's scheduled rotation configuration instead.

### 3. Apply only the isolated exercise policy

```bash
logrotate --force --state "$log_lab/state" "$log_lab/rotation.conf"
cat "$log_lab/events.log.1"
test ! -s "$log_lab/events.log"
printf 'new log starts empty: %s\n' "$?"
printf 'event three\n' >> "$log_lab/events.log"
cat "$log_lab/events.log"
```

Expect old events in events.log.1 and a newly created empty events.log before appending event three. `--force` is used only to make the private exercise deterministic. It is not a recommendation to force host-wide rotation.

## Verification and rollback

For the lab, confirm old records are readable and a new record reaches the new file. No long-running writer was tested. Real acceptance must also confirm the application's open descriptor/reopen behavior, collector delivery, intended new-file permissions, compression readability, scheduling and retention/capacity over time.

For a real policy failure, restore the known-good policy and writer destination through the application-supported process. Preserve both old and new records; blindly renaming/truncating files can overwrite evidence. Removing a rotation rule does not recover already deleted retained logs.

## Cleanup

After all steps succeed, remove exactly the four generated files:

```bash
rm -i -- "$log_lab/events.log" "$log_lab/events.log.1" \
  "$log_lab/rotation.conf" "$log_lab/state"
rmdir -- "$log_lab"
```

If interrupted before rotation, some files may not exist; inspect the temporary directory rather than substituting a broad deletion against a real log path.

## References

- [logrotate configuration and debug behavior](https://man7.org/linux/man-pages/man8/logrotate.8.html).
- [journald configuration](https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html) and [journal queries](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html).
- [Log investigation reference](../04-commands-and-cheat-sheets/processes-and-services/journalctl-reference.md).

[Collection home](README.md)
