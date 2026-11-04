# A service will not start

A service manager reports what happened while starting or supervising a process. The process may fail because of configuration, identity, missing paths, dependencies, a busy port, a resource limit or an application error. Read the exit evidence before restarting repeatedly.

## Environment and permissions

Host examples assume Linux booted with systemd. System service changes need authorization; logs may require sudo. Containers and non-systemd hosts need their own supervisor's equivalents.

The lab uses a systemd **user manager**, Bash and `/usr/bin/false` plus `/usr/bin/true`. It writes one uniquely named runtime user unit. It does not touch a production service or enable anything at boot. A desktop/login session often has a user manager; minimal containers and some sudo shells do not. Stop if `systemctl --user show-environment` fails.

## First checks

Replace UNIT with the exact discovered name:

```bash
systemctl status UNIT --no-pager
systemctl show UNIT -p LoadState -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus
systemctl cat UNIT
journalctl -u UNIT -b -n 100 --no-pager
```

A nonzero `systemctl status` is expected for a failed or inactive unit. Record it rather than treating it as a broken diagnostic. Read timestamps: a historical failure in the journal is not necessarily the state after your latest change.

## Evidence and interpretation

| Evidence | Candidate explanation | Check that distinguishes it |
| --- | --- | --- |
| Unit not found | Wrong name, missing package or unloaded user/system scope | Installed unit files and intended service manager |
| Bad-setting or parse error | Invalid unit configuration | Unit definition and `systemd-analyze verify` |
| Executable cannot be invoked | Wrong path, permissions, binary/interpreter problem | Actual ExecStart path, `namei -l`, file type and installed package |
| Application exits nonzero | Application rejected configuration or encountered runtime error | Application-specific log and supported configuration validation |
| Address already in use | Another process occupies the requested endpoint | `ss -ltnp` for the exact port, when permitted |
| Permission denied | Identity, directory traversal, ACL, sandbox or mandatory-access policy | Unit User/Group, path permissions, sandbox settings and security logs |
| Dependency failed | Required unit or mount was unavailable | Dependency state and its own failure evidence |
| Start request repeated too quickly | Repeated starts crossed a manager limit | Original failure before the rate-limit message |
| Active but client operation fails | Process exists but readiness or dependency is broken | Real request plus application/dependency checks |

An exit code such as 203/EXEC has a systemd meaning. Use the installed `systemd.exec` manual rather than assuming all nonzero codes come from the application.

## Recovery decisions

Validate application configuration using the application's documented check mode when available. A systemd unit syntax check and an application configuration check test different inputs. Confirm the service's working directory, environment and runtime identity; a command working in your interactive shell does not reproduce those conditions.

Change only the confirmed cause. Unit-file changes need `daemon-reload`; application configuration reload/restart is separate. `reset-failed` clears failure state and rate-limit counters but does not repair the underlying fault. Do not raise restart limits until the reason for the failures is understood.

Before touching an important service, record dependencies, customer impact, current configuration, rollback and a real acceptance request.

## Follow-along lab

### 1. Check prerequisites and create a runtime unit

```bash
systemctl --user show-environment > /dev/null
test -n "$XDG_RUNTIME_DIR"
test -x /usr/bin/false
test -x /usr/bin/true
```

All checks must succeed. Use a normal login session rather than a root shell. Continue only in the same shell:

```bash
lab_unit="linux-world-recovery-$$.service"
mkdir -p "$XDG_RUNTIME_DIR/systemd/user"
lab_unit_file="$XDG_RUNTIME_DIR/systemd/user/$lab_unit"
test ! -e "$lab_unit_file" && test ! -L "$lab_unit_file"
```

If the final check fails, stop rather than overwrite an existing file. Create only this exercise unit:

```bash
printf '%s\n' \
  '[Unit]' \
  'Description=Linux World controlled recovery exercise' \
  '[Service]' \
  'Type=oneshot' \
  'ExecStart=/usr/bin/false' \
  'RemainAfterExit=yes' \
  > "$lab_unit_file"
systemctl --user daemon-reload
systemctl --user start "$lab_unit"
printf 'start status: %s\n' "$?"
```

The start should fail because `/usr/bin/false` exits 1. That is intentional. No background crash loop is configured.

### 2. Explain the failure using records

```bash
systemctl --user show "$lab_unit" -p ActiveState -p SubState -p Result -p ExecMainStatus
journalctl --user -u "$lab_unit" -b -n 30 --no-pager
cat "$lab_unit_file"
```

Expect failed/failed, an exit-code result and ExecMainStatus=1. Journal access and content depend on local retention. The file proves the exercise explicitly asks a program to fail. Restarting unchanged cannot make that command succeed.

### 3. Correct only the exercise command

```bash
printf '%s\n' \
  '[Unit]' \
  'Description=Linux World controlled recovery exercise' \
  '[Service]' \
  'Type=oneshot' \
  'ExecStart=/usr/bin/true' \
  'RemainAfterExit=yes' \
  > "$lab_unit_file"
systemctl --user daemon-reload
systemctl --user reset-failed "$lab_unit"
systemctl --user start "$lab_unit"
```

## Recovery and verification

```bash
systemctl --user show "$lab_unit" -p ActiveState -p SubState -p Result -p ExecMainStatus
systemctl --user is-active "$lab_unit"
```

Expect active/exited, success and exit status 0. `RemainAfterExit=yes` deliberately keeps the successful oneshot active after it exits. This is not a network application, so a real client request is not applicable. For a real service, add an approved readiness and user-operation test: active state alone is insufficient.

## Cleanup

Stop the lab unit, clear only its recorded failure state, remove its exact file and reload the user manager:

```bash
systemctl --user stop "$lab_unit"
systemctl --user reset-failed "$lab_unit"
rm -i -- "$lab_unit_file"
systemctl --user daemon-reload
systemctl --user list-unit-files "$lab_unit" --no-pager
```

The final listing should contain no installed lab unit. The runtime user-unit directory can remain; do not remove a directory containing other units. Historical journal entries remain as evidence. Do not reset all host failures to hide this one exercise.

## References

- [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html), [unit definitions](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html) and [execution status](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html).
- [Service command reference](../04-command-reference/processes-and-services/systemctl-reference.md).

[Collection home](README.md) · [Recovery verification](verify-recovery-after-a-fix.md)
