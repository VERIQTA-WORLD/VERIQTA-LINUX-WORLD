```bash
findmnt -t nfs,nfs4,cifs
nfsstat -m
nfsstat -c
showmount -e SERVER
rpcinfo -p SERVER
sudo exportfs -v
smbclient -L SERVER -U ACCOUNT
smbclient //SERVER/SHARE -U ACCOUNT
smbstatus
sudo testparm -s
sudo mount -t nfs SERVER:/EXPORT MOUNTPOINT
sudo mount -t cifs //SERVER/SHARE MOUNTPOINT -o credentials=CREDENTIALS_FILE
sftp ACCOUNT@HOST
rsync -avni SOURCE_DIRECTORY/ ACCOUNT@HOST:DESTINATION_DIRECTORY/
```
