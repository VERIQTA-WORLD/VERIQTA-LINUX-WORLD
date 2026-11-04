```bash
ps
ps -ef
ps aux
ps -eo pid,ppid,user,stat,etime,comm
ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu
ps -eo pid,user,%cpu,%mem,comm --sort=-%mem
ps -p PID -o pid,ppid,user,stat,etime,args
ps -L -p PID
pgrep -a PROCESS_NAME
pgrep -a -u ACCOUNT PROCESS_NAME
pstree -p
pstree -p PID
top
htop
btop
pidof PROCESS_NAME
lsof -p PID
lsof -- FILE
sudo lsof +L1
sudo lsof -nP -iTCP -sTCP:LISTEN
fuser -v FILE
pmap -x PID
cat /proc/PID/status
cat /proc/PID/limits
```
