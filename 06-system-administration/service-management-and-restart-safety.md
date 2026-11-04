# Service management and restart safety

A service restart interrupts a process lifecycle and may affect connections, queues, locks and dependencies. Reloading configuration, restarting a unit and rebooting the host are different operations. Choose the action the application supports and verify user-visible behavior afterward.

## Environment and permissions

This runbook assumes Linux with systemd. Host service changes require authorized administration. A unit can be active without being ready; Type, socket activation, application readiness and dependency behavior all matter.

The lab uses a normal account's systemd **user manager** and one temporary runtime unit that runs sleep for at most 120 seconds per start. It never changes a host service, exposes a port or enables a unit at boot. It needs `/usr/bin/sleep`, Bash and a working user manager, and remains pending Linux execution validation.

## Before you begin

Identify the exact unit, owner, current state and intended user operation. Inspect configuration validation/reload support, dependency relationships, active work, redundancy and the maintenance window. Decide how to drain or checkpoint work using the application's supported mechanism. Keep the approved previous configuration and a recovery console.

Record a stop condition such as failed startup, unexpected errors, growing queue or exceeded interruption budget. Establish who decides to roll back rather than repeatedly restart.

## Operating procedure

### 1. Inspect the effective unit and current evidence

```bash
systemctl status UNIT --no-pager
systemctl cat UNIT
systemctl show UNIT -p ActiveState -p SubState -p CanReload -p MainPID -p Restart
systemctl list-dependencies UNIT
systemctl list-dependencies --reverse UNIT
journalctl -u UNIT --since '15 minutes ago' --no-pager
```

Replace UNIT with the discovered target. Definitions and logs can expose secrets. A dependency listing does not fully describe application clients or external traffic; consult the service architecture as well.

### 2. Validate before changing running state

Use the application's own configuration check. A valid unit file does not prove application configuration is valid. Unit-file changes require systemd daemon-reload; application reload is separate. `CanReload=yes` indicates a reload mechanism exists, not that it is safe for every change.

### 3. Choose and execute the approved action

| Action | Effect | Required follow-up |
| --- | --- | --- |
| daemon-reload | Manager rereads unit definitions | Apply any required application lifecycle action separately |
| reload | Uses the configured application reload mechanism | Check effective values and application behavior |
| restart | Stops then starts a unit | Expect interruption; verify startup, readiness and work handling |
| stop/start | Explicitly separates the stopped interval | Confirm dependencies and client handoff before both steps |
| enable/disable | Changes activation links | Does not by itself prove the present state or health |

Use a canary or one redundant member at a time when supported. Do not restart all instances just because a single check failed. If startup fails, use the [service troubleshooting guide](../05-troubleshooting-and-recovery/service-will-not-start.md) instead of increasing restart limits blindly.

## Follow-along lab

### 1. Establish an isolated unit

```bash
systemctl --user show-environment > /dev/null
test -n "$XDG_RUNTIME_DIR"
test -x /usr/bin/sleep
```

All checks must pass before continuing in the same shell:

```bash
safe_unit="linux-world-maintenance-$$.service"
mkdir -p "$XDG_RUNTIME_DIR/systemd/user"
safe_file="$XDG_RUNTIME_DIR/systemd/user/$safe_unit"
test ! -e "$safe_file" && test ! -L "$safe_file"
```

Stop if the target already exists. Create only the exercise definition:

```bash
printf '%s\n' \
  '[Unit]' \
  'Description=Linux World bounded service lifecycle exercise' \
  '[Service]' \
  'Type=simple' \
  'ExecStart=/usr/bin/sleep 120' \
  'Restart=no' \
  > "$safe_file"
systemctl --user daemon-reload
systemctl --user start "$safe_unit"
systemctl --user show "$safe_unit" -p ActiveState -p MainPID -p CanReload
before_pid=$(systemctl --user show "$safe_unit" -p MainPID --value)
```

Expect active state, a nonzero MainPID and CanReload=no. This unit provides no application reload operation. Complete observations before its 120-second process ends; if it has already exited, inspect that state rather than comparing stale PIDs.

### 2. Restart only the exercise unit

```bash
systemctl --user restart "$safe_unit"
after_pid=$(systemctl --user show "$safe_unit" -p MainPID --value)
printf 'before=%s after=%s\n' "$before_pid" "$after_pid"
systemctl --user is-active "$safe_unit"
```

Expect active state and normally a different nonzero PID. That establishes a process lifecycle transition, not application readiness. This teaching service has no network or data operation to validate.

## Verification and rollback

For the lab, inspect recent unit records and confirm no restart loop was configured:

```bash
systemctl --user show "$safe_unit" -p ActiveState -p SubState -p Restart -p NRestarts
journalctl --user -u "$safe_unit" -b -n 30 --no-pager
```

For a real service, repeat the original user request, validate data/queue handling and observe errors, latency and dependency health for the agreed window. If new configuration caused failure, restore the approved compatible version, validate it and apply its supported reload/restart workflow. Record the failed attempt as well as the recovered state.

## Cleanup

```bash
systemctl --user stop "$safe_unit"
rm -i -- "$safe_file"
systemctl --user daemon-reload
systemctl --user list-unit-files "$safe_unit" --no-pager
```

Expect no installed exercise unit. Leave a pre-existing runtime unit directory alone. Historical journal entries can remain. Do not disable or reset unrelated user/system services.

## References

- [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html) and [service lifecycle/readiness types](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html).
- [Recovery verification](../05-troubleshooting-and-recovery/verify-recovery-after-a-fix.md).

[Collection home](README.md)
