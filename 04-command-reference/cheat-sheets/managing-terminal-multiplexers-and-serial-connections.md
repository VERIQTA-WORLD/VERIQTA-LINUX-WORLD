| Command | What you can do with it |
| --- | --- |
| `tmux` | Start or attach to tmux using its default behavior. |
| `tmux new -s SESSION` | Create a named tmux session. |
| `tmux ls` | List tmux sessions. |
| `tmux attach -t SESSION` | Attach to a named tmux session. |
| `tmux new-window -t SESSION` | Create another window in a session. |
| `tmux list-windows -t SESSION` | List a session's windows. |
| `tmux list-panes -t SESSION` | List panes in a session's default target window. |
| `tmux capture-pane -p -t SESSION` | Print the contents of a tmux pane. |
| `tmux detach-client` | Detach the current tmux client. |
| `screen -ls` | List screen sessions. |
| `screen -S SESSION` | Create a named screen session. |
| `screen -r SESSION` | Resume a detached screen session. |
| `screen /dev/ttyUSB0 115200` | Open a serial terminal at 115200 baud using screen. |
| `picocom -b 115200 /dev/ttyUSB0` | Open a serial terminal with picocom. |
| `minicom -D /dev/ttyUSB0 -b 115200` | Open a serial terminal with minicom. |
| `stty -F /dev/ttyUSB0 -a` | Inspect a serial device's terminal settings. |
