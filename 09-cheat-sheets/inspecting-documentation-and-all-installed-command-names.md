```bash
compgen -c | LC_ALL=C sort -u
compgen -b | LC_ALL=C sort -u
compgen -A alias | LC_ALL=C sort -u
compgen -A function | LC_ALL=C sort -u
printf '%s\n' "$PATH" | tr ':' '\n'
find /usr/bin /usr/sbin /bin /sbin -maxdepth 1 -type f -executable -printf '%f\n' | LC_ALL=C sort -u
find /usr/local/bin /usr/local/sbin -maxdepth 1 -type f -executable -printf '%f\n' | LC_ALL=C sort -u
man -k .
apropos .
ls /usr/share/doc
ls /usr/share/man/man1
ls /usr/share/man/man8
type -a COMMAND
command -V COMMAND
man COMMAND
COMMAND --help
```
