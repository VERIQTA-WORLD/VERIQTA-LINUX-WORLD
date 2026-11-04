| Command | What you can do with it |
| --- | --- |
| `compgen -c \| LC_ALL=C sort -u` | List command names known to Bash without duplicates. |
| `compgen -b \| LC_ALL=C sort -u` | List Bash builtin names without duplicates. |
| `compgen -A alias \| LC_ALL=C sort -u` | List shell alias names without duplicates. |
| `compgen -A function \| LC_ALL=C sort -u` | List shell function names without duplicates. |
| `printf '%s\n' "$PATH" \| tr ':' '\n'` | Print each PATH entry on its own line. |
| `find /usr/bin /usr/sbin /bin /sbin -maxdepth 1 -type f -executable -printf '%f\n' \| LC_ALL=C sort -u` | List executable regular-file names in standard system command directories. |
| `find /usr/local/bin /usr/local/sbin -maxdepth 1 -type f -executable -printf '%f\n' \| LC_ALL=C sort -u` | List executable regular-file names in local administration command directories. |
| `man -k .` | Search the installed manual index for all matching entries. |
| `apropos .` | List indexed manual descriptions through apropos. |
| `ls /usr/share/doc` | List installed package documentation directories. |
| `ls /usr/share/man/man1` | List section-one command manuals. |
| `ls /usr/share/man/man8` | List section-eight administration manuals. |
| `type -a COMMAND` | Inspect all shell resolutions of a command. |
| `command -V COMMAND` | Inspect the selected resolution of a command. |
| `man COMMAND` | Open a command's installed manual. |
| `COMMAND --help` | Read a command's built-in help where supported. |
