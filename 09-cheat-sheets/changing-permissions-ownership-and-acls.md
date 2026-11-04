```bash
umask
umask 027
ls -ld -- PATH
stat -c '%a %A %U %G %n' -- PATH
chmod 600 -- FILE
chmod 640 -- FILE
chmod 644 -- FILE
chmod 700 -- DIRECTORY
chmod 750 -- DIRECTORY
chmod 755 -- DIRECTORY
chmod u+x -- SCRIPT.sh
chmod go-rwx -- FILE
chmod g+s -- DIRECTORY
chmod +t -- DIRECTORY
sudo chown ACCOUNT:GROUP PATH
chgrp GROUP PATH
getfacl -- PATH
getfacl -R -- DIRECTORY
setfacl -m u:ACCOUNT:r-- FILE
setfacl -m g:GROUP:rx DIRECTORY
setfacl -m d:g:GROUP:rx DIRECTORY
setfacl -x u:ACCOUNT FILE
getfattr -d -- PATH
getcap -- FILE
capsh --print
```
