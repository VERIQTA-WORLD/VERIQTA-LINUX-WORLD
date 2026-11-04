| Command | What you can do with it |
| --- | --- |
| `history` | List the current shell's command history. |
| `history 20` | Show the latest 20 history entries. |
| `fc -l -10` | List the latest ten history entries with fc. |
| `alias` | List defined aliases. |
| `alias ll='ls -lah'` | Define an alias for detailed file listings. |
| `unalias ll` | Remove an alias. |
| `set -o` | List shell option settings. |
| `shopt` | List Bash shopt settings. |
| `shopt -s nullglob` | Expand unmatched filename patterns to no words. |
| `shopt -u nullglob` | Restore unmatched patterns as literal text. |
| `set -o noclobber` | Prevent ordinary redirection from replacing existing regular files. |
| `set +o noclobber` | Allow ordinary redirection to replace existing files. |
| `set -o vi` | Use vi-style command-line editing. |
| `set -o emacs` | Use Emacs-style command-line editing. |
| `bind -P` | List Readline function bindings. |
| `hash -l` | List cached command locations. |
| `hash -r` | Clear cached command locations. |
| `printf '%s\n' "$SHELL" "$BASH_VERSION"` | Print the login-shell setting and current Bash version. |
| `stty -a` | Display terminal line settings. |
| `tty` | Print the current terminal device path. |
| `tput cols` | Print terminal width. |
| `tput lines` | Print terminal height. |
| `clear` | Clear the terminal display. |
| `reset` | Reset terminal state. |
| `script SESSION.log` | Record a terminal session into a log file. |
