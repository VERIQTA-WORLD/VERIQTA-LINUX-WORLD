# User access and sudo management

Access management connects an identity to a justified capability for a defined period. Treat account creation, SSH keys, group membership, sudo policy and offboarding as one lifecycle. A working login is not evidence that privileges are appropriately limited.

## Environment and permissions

Linux account lookups may use local files, LDAP, Active Directory or other identity services. The authoritative owner matters. Querying identity is usually unprivileged; protected password state and policy administration need authorization. Debian/Ubuntu often use the sudo group, while RPM-family systems often use wheel; neither group name alone defines effective policy.

The mandatory lab creates only a temporary policy **draft**. It never installs it in `/etc/sudoers` or `/etc/sudoers.d`. Optional validation needs visudo and a target Linux environment; syntax validation does not prove authorization is safe.

## Before you begin

Record the requester, identity owner, task, target systems, required duration, approval and revocation date. Separate human and service identities. Determine which capabilities the task actually needs; do not default to a root shell or an unrestricted administrative group.

For SSH/sudo changes, keep a verified recovery console and an existing administrative session. Identify the source of truth so a manual local edit is not immediately overwritten by automation.

## Operating procedure

### 1. Inspect current identity and effective access

```bash
id ACCOUNT
getent passwd ACCOUNT
getent group GROUP
sudo -l
```

Replace ACCOUNT and GROUP with approved identities. `sudo -l` describes the caller's policy; querying another user's privileges requires additional authorization. A group listing may omit users whose primary group is that group. Accounts can also have rights through identity-service rules or included sudo policy.

### 2. Design the smallest useful grant

Define exact commands, target identity, hosts and permitted arguments. Root-run editors, shells, package managers, interpreters and commands that can write arbitrary privileged files can defeat an apparently narrow allowlist. Wildcards and user-controlled paths require careful threat review. A command wrapper is not automatically safe either: its code, ownership, writable dependencies and arguments matter.

Do not use `NOPASSWD: ALL` to fix an automation failure. Where noninteractive access is required, design a narrowly scoped machine identity or controlled privileged service and protect its credentials.

### 3. Apply only an authorized plan

Local account/group operations change real access and require a target-specific plan. Use [account commands](../04-command-reference/users-and-permissions/user-and-group-commands.md) for syntax after verifying identity ownership. New group membership generally affects new login sessions; existing processes keep their groups.

Use visudo for sudoers edits and validate the **whole policy**, including includes. Match ownership/mode requirements to the installed sudo version and distribution. Test a second session before closing your recovery session. For SSH, follow the [SSH recovery guide](../05-troubleshooting-and-recovery/ssh-login-is-failing.md) for host identity and configuration checks.

### 4. Review and revoke deliberately

At review or departure, remove grants at their authoritative source, remove obsolete keys/tokens, invalidate affected sessions/credentials through the supported system, and reassign data and scheduled work. Password locking alone does not disable every SSH key, token or existing process. Deleting a home directory is a separate data-retention decision.

## Follow-along lab

Create a private draft granting the current user only a demonstration id command. It is never loaded as real policy:

```bash
access_lab=$(mktemp -d)
chmod 700 "$access_lab"
lab_account=$(id -un)
printf '%s ALL=(root) /usr/bin/id\n' "$lab_account" > "$access_lab/sudoers-draft"
chmod 600 "$access_lab/sudoers-draft"
cat "$access_lab/sudoers-draft"
```

Record the proposed permission and limits:

```bash
printf '%s\n' \
  'Purpose: syntax exercise only; draft not installed' \
  'Grant: run /usr/bin/id as root on matched hosts' \
  'Does not grant: an unrestricted shell or arbitrary file editing' \
  'Unverified: actual command path, full policy interaction, target-host authorization' \
  > "$access_lab/review.txt"
cat "$access_lab/review.txt"
```

On a Linux lab machine with visudo available, inspect the draft without installing it:

```bash
visudo -c -f "$access_lab/sudoers-draft"
```

Expect a parsed-OK result if syntax is valid and local validation permits it. If visudo is absent or reports ownership/mode/parser differences, record the environment and stop that optional validation. Do not copy the file into a live policy directory or add sudo just to force the illustrated result.

The example allows id's arguments because none were restricted in the draft. Command argument matching and other policy entries need separate review before a real grant. Treat this as parsing practice, not a production role recommendation.

## Verification and rollback

For this exercise, confirm the draft and review notes exist only beneath the unique temporary directory. Your effective privileges should be unchanged. A syntax pass does not establish least privilege or user-session behavior.

For a real grant, validate full policy, then test the intended operation and a representative prohibited operation from a new authorized session. Document authentication prompts, target identity and expiration. If validation or the second session fails, use retained recovery access to restore the known-good policy and recheck it before closing the change.

## Cleanup

```bash
rm -i -- "$access_lab/sudoers-draft" "$access_lab/review.txt"
rmdir -- "$access_lab"
```

No account, group, key or sudo rule was changed by the draft exercise.

## References

- [sudoers policy](https://www.sudo.ws/docs/man/sudoers.man/) and [visudo validation](https://www.sudo.ws/docs/man/visudo.man/).
- [getent](https://man7.org/linux/man-pages/man1/getent.1.html) and [sudo reference](../04-command-reference/users-and-permissions/sudo-reference.md).

[Collection home](README.md)
