```bash
tmux
tmux new -s SESSION
tmux ls
tmux attach -t SESSION
tmux new-window -t SESSION
tmux list-windows -t SESSION
tmux list-panes -t SESSION
tmux capture-pane -p -t SESSION
tmux detach-client
screen -ls
screen -S SESSION
screen -r SESSION
screen /dev/ttyUSB0 115200
picocom -b 115200 /dev/ttyUSB0
minicom -D /dev/ttyUSB0 -b 115200
stty -F /dev/ttyUSB0 -a
```
