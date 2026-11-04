| Command | What you can do with it |
| --- | --- |
| `ps` | Show processes selected by ps defaults. |
| `ps -ef` | List processes with owners and parent IDs. |
| `ps aux` | List processes with resource and command details. |
| `ps -eo pid,ppid,user,stat,etime,comm` | List process IDs, parents, owners, states, elapsed times and names. |
| `ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu` | Sort processes by reported CPU usage. |
| `ps -eo pid,user,%cpu,%mem,comm --sort=-%mem` | Sort processes by reported memory usage. |
| `ps -p PID -o pid,ppid,user,stat,etime,args` | Inspect one process, including its arguments, which may contain secrets. |
| `ps -L -p PID` | List a process's threads. |
| `pgrep -a PROCESS_NAME` | Find processes by name and show their command lines. |
| `pgrep -a -u ACCOUNT PROCESS_NAME` | Find matching processes owned by an account. |
| `pstree -p` | Display the process tree with PIDs. |
| `pstree -p PID` | Display a process's descendant tree. |
| `top` | Monitor processes interactively with top. |
| `htop` | Monitor processes interactively with htop. |
| `btop` | Monitor resources with btop. |
| `pidof PROCESS_NAME` | Find PIDs for a program name. |
| `lsof -p PID` | List files opened by a process. |
| `lsof -- FILE` | Find processes that have a file open. |
| `sudo lsof +L1` | Find open files whose link count has dropped below one. |
| `sudo lsof -nP -iTCP -sTCP:LISTEN` | List listening TCP sockets and owning processes. |
| `fuser -v FILE` | Identify processes using a file. |
| `pmap -x PID` | Inspect a process's memory mappings. |
| `cat /proc/PID/status` | Read a process's status fields. |
| `cat /proc/PID/limits` | Read a process's resource limits. |
