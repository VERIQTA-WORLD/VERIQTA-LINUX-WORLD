```bash
time COMMAND
/usr/bin/time -v COMMAND
watch -n 2 COMMAND
watch -d -n 2 COMMAND
sleep 5
sleep 2m
timeout 30s COMMAND
flock -n LOCK_FILE COMMAND
xargs -r -a ARGUMENT_FILE COMMAND
xargs -0 -r COMMAND < NULL_DELIMITED_FILE
xargs -r -n 1 COMMAND < ARGUMENT_FILE
xargs -r -P 4 -n 1 COMMAND < ARGUMENT_FILE
parallel --dry-run COMMAND ::: ONE TWO THREE
parallel -j 4 COMMAND ::: ONE TWO THREE
parallel --jobs 4 COMMAND :::: ARGUMENT_FILE
printf '%s\n' ONE TWO THREE
printf '%s\0' ONE TWO THREE
printf '%q\n' 'VALUE WITH SPACES'
env NAME=VALUE COMMAND
env -i PATH=/usr/bin:/bin COMMAND
stdbuf -oL COMMAND
```
