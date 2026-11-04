# SSH login is failing

SSH has several stages: resolve a destination, establish TCP, verify the server's identity, authenticate your account and create a session. Identify the stage that fails before changing keys, permissions or server policy.

## Environment and permissions

Use an OpenSSH client and an authorized Linux lab host. Server-side checks require an existing administrative session or console; keep it open while investigating. The configuration exercise works offline as a normal user. Its optional connection test requires a known-good SSH account, approved port and verified host-key fingerprint.

Debian/Ubuntu commonly use `ssh.service`; Fedora/RHEL commonly use `sshd.service`. Socket activation and custom names are possible. Discover the installed unit instead of assuming one. Local, directory-service and certificate-based accounts can have different authentication requirements.

## First checks

Record the exact command, destination, username, port, time and error. Never publish passwords, private keys, tokens or unredacted authentication logs.

```bash
ssh -V
ssh -G HOST
ssh -v -o ConnectTimeout=5 ACCOUNT@HOST
```

`ssh -G` prints the effective client configuration without opening an SSH session. A configured `Match exec` rule can still execute a local command during evaluation, so do not evaluate untrusted configuration blindly. Verbose connection diagnostics can reveal internal addresses and file paths.

Inspect only one controlled attempt initially. Repeated failures can trigger rate limits or account-protection policies. Do not add obsolete cryptography or disable host-key checking to make an error disappear.

## Evidence and interpretation

| Observed stage/error | What is established | What to inspect next |
| --- | --- | --- |
| Could not resolve hostname | Name lookup failed before SSH authentication | Effective hostname, spelling, resolver and search domains |
| Connection refused | The selected TCP path received a rejection | Approved port, listener and active rejection policy |
| Connection timed out | No usable connection before the deadline | Routes, filtering, address family, host state and load |
| Host identification changed | Stored and offered host identities differ | Rebuild/change records and independently verified fingerprint |
| Permission denied | Transport reached authentication, but no offered method succeeded | Correct account, offered key, allowed methods and server decision |
| Too many authentication failures | The server rejected too many attempts in one session | Identities offered by the client; consider a specific authorized key |
| Authenticated, then session closes | Authentication may have succeeded | Shell, account expiry, PAM, home access and forced commands |

`Permission denied (publickey)` does not prove the server lacks your public key. It can also reflect a different username, wrong identity, policy, ownership, account restrictions or a certificate validity problem.

## Server-side evidence

From the retained session or console, discover and inspect the actual unit:

```bash
systemctl list-unit-files 'ssh*' --no-pager
ss -ltn
sudo sshd -t
```

`sshd -t` checks syntax and required key sanity; success does not test every account's authorization. If the executable is outside PATH, use its verified installed path. For a known systemd unit, query `journalctl -u UNIT --since '15 minutes ago' --no-pager`. On some hosts, `/var/log/auth.log` or `/var/log/secure` holds additional evidence.

Inspect effective server policy, accounting for `Match` blocks:

```bash
sudo sshd -T -C user=ACCOUNT,host=CLIENT_HOST,addr=CLIENT_IP
getent passwd ACCOUNT
id ACCOUNT
namei -l /home/ACCOUNT/.ssh/authorized_keys
```

Replace every placeholder first, including the actual account home path. `sshd -T` output can contain sensitive configuration. Some versions accept additional connection criteria such as local address/port. Directory-service policy and PAM may add restrictions outside sshd_config.

## Recovery decisions

Correct the confirmed mismatch. If the client offers the wrong key, use its approved identity and `IdentitiesOnly=yes` rather than changing the server to allow everything. If a key path has incorrect permissions, compare intended ownership and access along the entire path before a targeted correction. Do not use recursive chmod/chown against a home directory.

For server configuration changes: save the previous file, validate the proposed configuration, retain console/session recovery and follow the service's supported reload procedure. A syntax check alone does not guarantee a new login will work. Open a **second** verified session before closing the first. A host-key change must be independently verified before updating only the affected known_hosts entry.

## Follow-along lab

### 1. Create an isolated client configuration

The approved endpoint in this exercise is loopback port 22. This is an exercise assumption, not a universal SSH default. Do not change the real server. The first configuration deliberately selects port 65022.

```bash
ssh_lab=$(mktemp -d)
chmod 700 "$ssh_lab"
printf '%s\n' \
  'Host linux-world-lab' \
  '  HostName 127.0.0.1' \
  '  Port 65022' \
  "  User $(id -un)" \
  > "$ssh_lab/client.conf"
chmod 600 "$ssh_lab/client.conf"
ssh -F "$ssh_lab/client.conf" -G linux-world-lab | grep -E '^(hostname|port|user) '
```

Expected effective values: hostname 127.0.0.1, port 65022 and your account name. This proves the client would choose the wrong exercise port. It does not require any connection attempt.

### 2. Correct the confirmed mismatch

```bash
printf '%s\n' \
  'Host linux-world-lab' \
  '  HostName 127.0.0.1' \
  '  Port 22' \
  "  User $(id -un)" \
  > "$ssh_lab/client.conf"
ssh -F "$ssh_lab/client.conf" -G linux-world-lab | grep -E '^(hostname|port|user) '
```

Now the effective port should be 22. Neither your normal SSH configuration nor the server changed.

## Recovery and verification

The offline lab establishes only that the configuration matches the supplied endpoint. If this is your authorized SSH lab VM, its actual service uses port 22, its host fingerprint is already verified and this account has a known-working key, test once:

```bash
ssh -F "$ssh_lab/client.conf" -o BatchMode=yes -o ConnectTimeout=3 \
  linux-world-lab 'id -un; hostname'
```

Expect the authorized remote identity and hostname with status 0. BatchMode disables interactive password/passphrase prompting, so failure can mean the key was unavailable rather than bad server policy. If no such lab server exists, skip this optional test and record authentication/session validation as pending.

## Cleanup

```bash
rm -i -- "$ssh_lab/client.conf"
rmdir -- "$ssh_lab"
```

No keys, accounts, host trust entries or server policy were changed. Write a note distinguishing client configuration evidence from successful remote authentication.

## References

- [OpenSSH client](https://man.openbsd.org/ssh), [server](https://man.openbsd.org/sshd) and [server configuration](https://man.openbsd.org/sshd_config).
- [SSH command reference](../04-command-reference/networking/ssh-reference.md).
- [Server reachability](server-is-unreachable.md) for failures before authentication.

[Collection home](README.md) · [Troubleshooting method](linux-troubleshooting-method.md)
