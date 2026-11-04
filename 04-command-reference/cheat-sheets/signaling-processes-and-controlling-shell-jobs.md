| Command | What you can do with it |
| --- | --- |
| `jobs` | List jobs managed by the current shell. |
| `jobs -l` | List shell jobs with process IDs. |
| `COMMAND &` | Start a command in the background. |
| `printf '%s\n' "$!"` | Print the most recently started background process ID. |
| `fg %1` | Bring job one into the foreground. |
| `bg %1` | Resume job one in the background. |
| `disown %1` | Remove job one from the shell's job table. |
| `wait PID` | Wait for a child process and collect its exit status. |
| `kill -l` | List signal names and numbers. |
| `kill -0 PID` | Check process existence or signal permission without sending a signal. |
| `kill -TERM PID` | Request graceful termination of a process. |
| `kill -INT PID` | Send the interactive interrupt signal. |
| `kill -HUP PID` | Send SIGHUP, whose meaning depends on the application. |
| `kill -STOP PID` | Suspend a process with an uncatchable stop signal. |
| `kill -CONT PID` | Resume a stopped process. |
| `timeout 10s COMMAND` | Limit a command's runtime to ten seconds. |
| `timeout --signal=TERM --kill-after=5s 30s COMMAND` | Request termination at 30 seconds and force-kill five seconds later if needed. |
| `nohup COMMAND > OUTPUT_FILE 2>&1 &` | Run a command resistant to SIGHUP, writing output to a file. |
| `nice -n 10 COMMAND` | Start a command with lower CPU scheduling priority. |
| `renice -n 10 -p PID` | Lower an existing process's CPU scheduling priority. |
| `ionice -p PID` | Inspect a process's I/O scheduling class and priority. |
| `ionice -c 3 COMMAND` | Run a command using idle I/O scheduling. |
| `taskset -pc PID` | Inspect a process's CPU affinity. |
| `taskset -c 0 COMMAND` | Run a command restricted to CPU zero. |
