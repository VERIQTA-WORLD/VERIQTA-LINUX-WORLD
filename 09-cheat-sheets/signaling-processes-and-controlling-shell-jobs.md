```bash
jobs
jobs -l
COMMAND &
printf '%s\n' "$!"
fg %1
bg %1
disown %1
wait PID
kill -l
kill -0 PID
kill -TERM PID
kill -INT PID
kill -HUP PID
kill -STOP PID
kill -CONT PID
timeout 10s COMMAND
timeout --signal=TERM --kill-after=5s 30s COMMAND
nohup COMMAND > OUTPUT_FILE 2>&1 &
nice -n 10 COMMAND
renice -n 10 -p PID
ionice -p PID
ionice -c 3 COMMAND
taskset -pc PID
taskset -c 0 COMMAND
```
