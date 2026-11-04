| Command | What you can do with it |
| --- | --- |
| `findmnt -t nfs,nfs4,cifs` | List active NFS and CIFS mounts. |
| `nfsstat -m` | Inspect NFS mount parameters. |
| `nfsstat -c` | Inspect NFS client statistics. |
| `showmount -e SERVER` | Query exports advertised by an authorized NFS server. |
| `rpcinfo -p SERVER` | Query an authorized server's RPC services. |
| `sudo exportfs -v` | List configured active NFS exports. |
| `smbclient -L SERVER -U ACCOUNT` | List SMB shares using an authorized account. |
| `smbclient //SERVER/SHARE -U ACCOUNT` | Open an interactive SMB share session. |
| `smbstatus` | Inspect Samba sessions and locks. |
| `sudo testparm -s` | Validate and print Samba configuration. |
| `sudo mount -t nfs SERVER:/EXPORT MOUNTPOINT` | Mount an authorized NFS export, hiding existing mount-point contents. |
| `sudo mount -t cifs //SERVER/SHARE MOUNTPOINT -o credentials=CREDENTIALS_FILE` | Mount an authorized SMB share using a protected credentials file. |
| `sftp ACCOUNT@HOST` | Open an authorized SFTP session. |
| `rsync -avni SOURCE_DIRECTORY/ ACCOUNT@HOST:DESTINATION_DIRECTORY/` | Preview synchronization to a remote directory without transferring files. |
