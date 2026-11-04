# Understand modes, ownership and access

Linux checks ownership and mode bits, with possible additional ACL and security-policy checks. For files, read means reading bytes, write means changing bytes, and execute means running a program. On directories, read lists names, execute traverses, and write allows directory-entry changes when traversal is also allowed.

## Environment and permissions

GNU/Linux; modify only your own temporary file. `chown` generally requires root to change owner; changing group is limited to groups you belong to. ACL tools may need an extra package.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `ls -ld -- PATH` | Inspect the object itself, including a directory’s mode. |
| `stat -c "%a %U %G" -- PATH` | Print octal mode, owner and group (GNU syntax). |
| `chmod u=rw,go= -- FILE` | Give only the owner read and write access. |
| `chmod 640 -- FILE` | Owner read/write, group read, others no access. |
| `chmod 750 -- DIR` | Owner full access; group list/traverse; others none. |
| `chown OWNER:GROUP PATH` | Change ownership subject to privilege checks. |
| `umask` | Show the permission mask applied when creating new objects. |
| `getfacl -- PATH` | Inspect ACLs, if installed. |

## Follow along

```bash
perm_lab=$(mktemp -d)
printf 'private note\n' > "$perm_lab/note"
chmod 600 -- "$perm_lab/note"
stat -c '%a %U %G' -- "$perm_lab/note"
chmod u+x -- "$perm_lab/note"
stat -c '%a' -- "$perm_lab/note"
chmod u-x -- "$perm_lab/note"
rm -i -- "$perm_lab/note"
rmdir -- "$perm_lab"
```

## Expected results and verification

First mode is 600; after adding owner execute it is 700. Execute permission does not turn arbitrary text into a valid program. Cleanup removes the exercise file and empty directory.

## Common mistakes and next checks

Access to a file also depends on every parent directory. Deletion is principally governed by the containing directory, including sticky-bit rules. `chmod -R 777` destroys useful access boundaries. ACL masks, SELinux or AppArmor may explain denial even when mode bits seem sufficient. `umask` removes requested permissions; ordinary file creation normally starts without execute bits.

## Authoritative references

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [ACL manual](https://man7.org/linux/man-pages/man5/acl.5.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
