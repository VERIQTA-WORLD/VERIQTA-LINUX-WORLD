| Command | What you can do with it |
| --- | --- |
| `help` | List Bash builtin help topics. |
| `help cd` | Read help for Bash directory changes. |
| `help test` | Read help for Bash conditional tests. |
| `man COMMAND` | Open the installed manual for a command. |
| `man 5 passwd` | Read the passwd file-format manual in section 5. |
| `man -k KEYWORD` | Search manual summaries by keyword. |
| `man -f COMMAND` | Show a command's one-line manual summary. |
| `apropos KEYWORD` | Search installed manual descriptions. |
| `whatis COMMAND` | Show a command's short description. |
| `info COMMAND` | Read GNU Info documentation for a command. |
| `COMMAND --help` | Open a tool's built-in help, when supported. |
| `COMMAND --version` | Display a tool's version, when supported. |
| `command -v COMMAND` | Locate the command selected by this shell. |
| `command -V COMMAND` | Describe how this shell resolves a command. |
| `type COMMAND` | Identify a command as a builtin, alias, function or executable. |
| `type -a COMMAND` | Show all resolutions of a command name. |
| `compgen -c` | List command names known to Bash. |
| `compgen -b` | List Bash builtin command names. |
| `compgen -A function` | List defined shell function names. |
| `compgen -A alias` | List defined shell alias names. |
| `whereis COMMAND` | Locate binary, source and manual paths. |
| `which COMMAND` | Find an executable through PATH. |
| `printf '%s\n' "$PATH"` | Display the executable search path. |
| `find /usr/bin /usr/sbin /bin /sbin -maxdepth 1 -type f -executable` | Find executable regular files in standard system command directories. |
