| Command | What you can do with it |
| --- | --- |
| `ssh -V` | Display the OpenSSH client version. |
| `ssh ACCOUNT@HOST` | Connect to an authorized remote account after verifying host identity. |
| `ssh -p PORT ACCOUNT@HOST` | Connect using a custom SSH port. |
| `ssh -i PRIVATE_KEY ACCOUNT@HOST` | Offer a selected private identity key. |
| `ssh -o IdentitiesOnly=yes -i PRIVATE_KEY ACCOUNT@HOST` | Limit offered identities to configured identity files. |
| `ssh -v ACCOUNT@HOST` | Print verbose connection diagnostics, which may reveal sensitive details. |
| `ssh -G HOST` | Print effective SSH client configuration. |
| `ssh -J JUMP_ACCOUNT@JUMP_HOST ACCOUNT@HOST` | Connect through an SSH jump host. |
| `ssh -t ACCOUNT@HOST COMMAND` | Allocate a remote terminal for a command. |
| `ssh ACCOUNT@HOST 'hostname; uptime'` | Run hostname and uptime on an authorized remote host. |
| `ssh -N -L 127.0.0.1:8080:127.0.0.1:80 ACCOUNT@HOST` | Forward local loopback port 8080 to port 80 as seen by the remote host. |
| `ssh -N -D 127.0.0.1:1080 ACCOUNT@HOST` | Create a loopback SOCKS proxy through an SSH connection. |
| `ssh-keygen -t ed25519 -f NEW_PRIVATE_KEY` | Create a new Ed25519 keypair at a chosen path. |
| `ssh-keygen -lf PUBLIC_KEY` | Display a public key's fingerprint. |
| `ssh-keygen -F HOST` | Search known_hosts entries for a host. |
| `ssh-add -l` | List identities currently held by the SSH agent. |
| `ssh-add PRIVATE_KEY` | Add a private identity to the SSH agent. |
| `ssh-copy-id -i PUBLIC_KEY ACCOUNT@HOST` | Install a public key on an authorized remote account. |
| `scp FILE ACCOUNT@HOST:REMOTE_DIRECTORY/` | Copy a file to a remote directory. |
| `scp -P PORT FILE ACCOUNT@HOST:REMOTE_DIRECTORY/` | Copy a file using a custom SSH port. |
| `scp ACCOUNT@HOST:REMOTE_FILE LOCAL_DIRECTORY/` | Copy a remote file to a local directory. |
| `sftp ACCOUNT@HOST` | Open an interactive SFTP session. |
| `sftp -P PORT ACCOUNT@HOST` | Open SFTP using a custom SSH port. |
| `sudo sshd -t` | Check SSH server configuration syntax. |
| `sudo sshd -T` | Print effective SSH server configuration. |
