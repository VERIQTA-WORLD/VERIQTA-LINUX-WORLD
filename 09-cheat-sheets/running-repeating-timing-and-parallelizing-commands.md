| Command | What you can do with it |
| --- | --- |
| `time COMMAND` | Run a command and report shell timing statistics. |
| `/usr/bin/time -v COMMAND` | Run a command with detailed GNU time resource statistics. |
| `watch -n 2 COMMAND` | Repeat a command every two seconds. |
| `watch -d -n 2 COMMAND` | Repeat a command and highlight output changes. |
| `sleep 5` | Pause for five seconds. |
| `sleep 2m` | Pause for two minutes. |
| `timeout 30s COMMAND` | Limit a command to 30 seconds. |
| `flock -n LOCK_FILE COMMAND` | Run a command only if an advisory file lock is immediately available. |
| `xargs -r -a ARGUMENT_FILE COMMAND` | Build command arguments from a file without running on empty input. |
| `xargs -0 -r COMMAND < NULL_DELIMITED_FILE` | Read null-delimited arguments without splitting filenames at spaces. |
| `xargs -r -n 1 COMMAND < ARGUMENT_FILE` | Run a command once for each input argument. |
| `xargs -r -P 4 -n 1 COMMAND < ARGUMENT_FILE` | Run up to four commands concurrently, each with one input argument. |
| `parallel --dry-run COMMAND ::: ONE TWO THREE` | Preview GNU Parallel jobs without executing them. |
| `parallel -j 4 COMMAND ::: ONE TWO THREE` | Run one job per supplied value with up to four concurrent jobs. |
| `parallel --jobs 4 COMMAND :::: ARGUMENT_FILE` | Run jobs using arguments read from a file. |
| `printf '%s\n' ONE TWO THREE` | Print three values on separate lines. |
| `printf '%s\0' ONE TWO THREE` | Print three null-delimited values. |
| `printf '%q\n' 'VALUE WITH SPACES'` | Print a value quoted for reuse as shell input. |
| `env NAME=VALUE COMMAND` | Set an environment variable for one command. |
| `env -i PATH=/usr/bin:/bin COMMAND` | Run a command with a minimal explicit environment. |
| `stdbuf -oL COMMAND` | Request line-buffered standard output from a compatible command. |
