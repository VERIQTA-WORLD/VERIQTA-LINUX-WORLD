# Configuration changes and rollback

A configuration change has several states: edited source, validated candidate, installed file, application-effective settings and verified user behavior. Moving a file does not automatically make the application use it. Keep these boundaries explicit and define the previous compatible state before making the change.

## Environment and permissions

Real host configuration changes need authorization and the application's actual owner/deployment system. Generated files should be changed at their source of truth. Preserve secrets, ownership, mode, ACLs, labels and relevant links using the environment's approved tooling.

The lab uses Bash, Python 3.8+ and a small JSON-schema validator from the repository root. It changes only private temporary files, runs no real service and needs no sudo. The demonstration validator does not validate Nginx, SSH or another application's configuration.

## Before you begin

Record the exact intended behavior, current version/values, affected clients, dependencies and change window. Identify validation commands, activation semantics and what survives restart/reboot. Decide the verification request and rollback trigger before editing.

Check whether old software/configuration remains compatible with any new data, schema or key state. Rollback needs more than a saved text file if the application changes persistent state during activation.

## Operating procedure

### 1. Stage a candidate separately

Review the source diff, restrict changes to the intended scope and keep secret-bearing values out of public diffs. Validate syntax plus application-specific semantics as the relevant runtime identity where supported. An administrator's successful check may miss an application's access restrictions.

### 2. Preserve and install deliberately

Capture the known-good version and required metadata. Use the environment's managed deployment method. For a simple regular-file replacement on one filesystem, a staged rename can provide atomic visibility of that file; it does not make several files or application state one transaction, and it does not by itself guarantee crash durability.

Do not casually replace symlinks, mount targets or files owned by a configuration manager. Confirm the path before installation, then verify the installed content and access metadata.

### 3. Activate with the supported mechanism

Determine whether the application reads the file dynamically, needs reload or requires restart. Unit-file changes may require systemd daemon-reload separately. Validate the new effective state and user behavior, not just the saved file. Use canaries or one instance at a time when the architecture supports it.

### 4. Roll back at the defined boundary

If acceptance fails, stop rollout and restore the reviewed compatible state using the supported method. Revalidate, reactivate and recheck the user path. Preserve failed-candidate evidence for diagnosis without retaining exposed secrets unnecessarily.

## Follow-along lab

### 1. Save a known-good sample and reject an invalid candidate

```bash
config_lab=$(mktemp -d)
chmod 700 "$config_lab"
printf '{"port":8000,"message":"before"}\n' > "$config_lab/active.json"
chmod 600 "$config_lab/active.json"
cp -p "$config_lab/active.json" "$config_lab/previous.json"
printf '{"port":"wrong-type","message":"after"}\n' > "$config_lab/candidate.json"
python3 06-production-administration/labs/check_demo_config.py "$config_lab/candidate.json"
printf 'invalid candidate status: %s\n' "$?"
cmp -- "$config_lab/previous.json" "$config_lab/active.json"
printf 'active still matches previous: %s\n' "$?"
```

Expect validator status 2 and comparison status 0. The candidate is valid JSON syntax but violates this demonstration's port type rule. No invalid candidate was installed.

### 2. Validate and promote a corrected candidate

```bash
printf '{"port":9000,"message":"after"}\n' > "$config_lab/candidate.json"
python3 06-production-administration/labs/check_demo_config.py "$config_lab/candidate.json"
```

Stop unless validation succeeds. Stage a regular file in the same directory, give it the intended mode and replace only the sample active file:

```bash
cp "$config_lab/candidate.json" "$config_lab/next.json"
chmod 600 "$config_lab/next.json"
mv "$config_lab/next.json" "$config_lab/active.json"
python3 06-production-administration/labs/check_demo_config.py "$config_lab/active.json"
cat "$config_lab/active.json"
```

Expect the accepted candidate values, port 9000 and message after. No application is running, so this proves file promotion and validation only. A real activation would need its own acceptance check.

### 3. Rehearse a controlled rollback

Assume an application-level test rejected the changed behavior. Validate the previous sample, stage its metadata-preserving copy and replace the active file:

```bash
python3 06-production-administration/labs/check_demo_config.py "$config_lab/previous.json"
cp -p "$config_lab/previous.json" "$config_lab/rollback.json"
mv "$config_lab/rollback.json" "$config_lab/active.json"
cmp -- "$config_lab/previous.json" "$config_lab/active.json"
printf 'rollback byte comparison: %s\n' "$?"
cat "$config_lab/active.json"
```

## Verification and rollback

Expect rollback comparison status 0 and original values, port 8000 and message before. The original backup remains intact. The exercise has demonstrated rejecting a bad candidate, promoting a good one and restoring known-good bytes.

For a real service, also verify metadata, effective loaded values, client requests, data compatibility, errors and stability. Restoring bytes without reactivation may leave the new behavior running. If rollback is incompatible with changed data, escalate to the predetermined recovery strategy rather than forcing old binaries/configuration onto it.

## Cleanup

```bash
rm -i -- "$config_lab/active.json" "$config_lab/previous.json" "$config_lab/candidate.json"
rmdir -- "$config_lab"
```

The staging files were consumed by their renames. If interrupted, inspect this temporary directory for the exact next.json or rollback.json before cleanup; never translate these paths into a live configuration directory.

## References

- [Python JSON parsing](https://docs.python.org/3/library/json.html): parsing is distinct from application schema validation.
- [Linux rename semantics](https://man7.org/linux/man-pages/man2/rename.2.html) and [systemd manager actions](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html).
- [Service activation safety](service-management-and-restart-safety.md) and [recovery verification](../05-troubleshooting-and-recovery/verify-recovery-after-a-fix.md).

[Collection home](README.md)
