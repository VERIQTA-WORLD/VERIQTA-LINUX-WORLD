# Use SSH and inspect connection settings

SSH encrypts remote sessions and authenticates the server as well as the user. A server host key and your user authentication key serve different purposes.

## Environment and permissions

OpenSSH client on Linux; remote examples require a lab host and authorized account. `lab.example.invalid` is a placeholder and must be replaced. The local walkthrough does not connect or generate keys.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `ssh USER@HOST` | Connect after verifying the expected host identity. |
| `ssh -p PORT USER@HOST` | Use a nondefault TCP port. |
| `ssh -i KEY USER@HOST` | Offer a specified private identity file. |
| `ssh -G HOST` | Print evaluated client configuration without opening a remote session. |
| `ssh -v USER@HOST` | Emit diagnostic connection details; redact before sharing. |
| `ssh-keygen -lf PUBLIC_KEY_FILE` | Print a key fingerprint. |
| `sftp USER@HOST` | Open an encrypted file-transfer session. |
| `ssh -N -L 127.0.0.1:8080:127.0.0.1:80 USER@HOST` | Forward a local loopback port to port 80 as seen by the remote host; changes local access paths. |

## Follow along

```bash
ssh -V
ssh -G lab.example.invalid | head -n 20
```

For an authorized lab host, the connection syntax is `ssh learner@YOUR_LAB_HOST`. Obtain its host-key fingerprint through a trusted independent channel before accepting the first connection. Exit a remote shell with `exit`.

## Expected results and verification

`ssh -V` prints a version (usually to stderr). `ssh -G` shows effective settings such as hostname, user and port; a configured Match exec rule could run a local command during configuration evaluation, so inspect unfamiliar SSH configuration first. No remote session or cleanup is expected in the local walkthrough.

## Common mistakes and next checks

Never share private keys. A changed host-key warning needs investigation, not `StrictHostKeyChecking=no`. User configuration normally belongs in `~/.ssh/config` with restricted access. Server unit names and logging differ by distribution; use systemctl discovery rather than assuming a name.

## Authoritative references

- [OpenSSH manuals](https://www.openssh.org/manual.html)
- [ssh client manual](https://man.openbsd.org/ssh.1)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
