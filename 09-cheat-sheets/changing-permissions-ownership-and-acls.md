| Command | What you can do with it |
| --- | --- |
| `umask` | Display the current creation-permission mask. |
| `umask 027` | Set the mask to remove group write and all other-user permissions. |
| `ls -ld -- PATH` | Inspect a path's mode, owner and group. |
| `stat -c '%a %A %U %G %n' -- PATH` | Print numeric mode, symbolic mode, owner, group and name. |
| `chmod 600 -- FILE` | Allow only the owner to read and write a file. |
| `chmod 640 -- FILE` | Allow owner read/write and group read. |
| `chmod 644 -- FILE` | Allow owner read/write and everyone else read. |
| `chmod 700 -- DIRECTORY` | Allow only the owner to access a directory. |
| `chmod 750 -- DIRECTORY` | Give the owner full directory access and the group list/traverse access. |
| `chmod 755 -- DIRECTORY` | Give the owner full directory access and everyone else list/traverse access. |
| `chmod u+x -- SCRIPT.sh` | Add owner execute permission to a script. |
| `chmod go-rwx -- FILE` | Remove group and other-user permissions. |
| `chmod g+s -- DIRECTORY` | Set directory setgid so new entries inherit its group where supported. |
| `chmod +t -- DIRECTORY` | Set a directory's sticky bit to restrict entry removal. |
| `sudo chown ACCOUNT:GROUP PATH` | Change a path's owner and group. |
| `chgrp GROUP PATH` | Change group ownership where authorized. |
| `getfacl -- PATH` | Inspect a path's access control list. |
| `getfacl -R -- DIRECTORY` | Inspect access control lists recursively. |
| `setfacl -m u:ACCOUNT:r-- FILE` | Grant a named account read access through an ACL. |
| `setfacl -m g:GROUP:rx DIRECTORY` | Grant a group read/traverse access to a directory through an ACL. |
| `setfacl -m d:g:GROUP:rx DIRECTORY` | Set an inheritable default directory ACL for a group. |
| `setfacl -x u:ACCOUNT FILE` | Remove a named account's ACL entry. |
| `getfattr -d -- PATH` | Inspect user extended attributes. |
| `getcap -- FILE` | Inspect executable file capabilities. |
| `capsh --print` | Display the process capability environment. |
