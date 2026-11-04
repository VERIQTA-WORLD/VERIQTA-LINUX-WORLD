# Observe processes and send signals

A process is a running program with a process ID (PID). Signals request actions; SIGTERM asks for termination and allows handling, while SIGKILL cannot be caught for cleanup.

## Environment and permissions

Linux with procps-ng and Bash. You may normally signal processes you own; other identities need appropriate privilege. The exercise starts and stops only its own `sleep` process.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `ps -eo pid,ppid,user,stat,comm` | Snapshot process IDs, parents, owners, state and command names. |
| `pgrep -a -u USER PATTERN` | Find matching process names for one owner; inspect results before acting. |
| `ps -p PID -o pid,ppid,stat,etime,args` | Inspect a specific PID; args may expose secrets. |
| `top` | Interactive process view; q exits. |
| `kill -TERM PID` | Request graceful termination; successful delivery is not proof of exit. |
| `kill -KILL PID` | Force termination; can lose in-memory state and skip cleanup. |
| `jobs -l` | List jobs belonging to this shell. |
| `wait PID` | Wait for this shell’s child and collect its exit status. |

## Follow along

```bash
sleep 120 &
practice_pid=$!
ps -p "$practice_pid" -o pid,ppid,stat,comm
kill -TERM "$practice_pid"
wait "$practice_pid"
printf 'child exit: %s\n' "$?"
ps -p "$practice_pid" -o pid,stat,comm
```

## Expected results and verification

The first snapshot shows sleep. Bash normally reports exit 143 for termination by SIGTERM. The final `ps` should show only the header and return nonzero because the child is gone. The process is the only exercise resource.

## Common mistakes and next checks

PIDs can be reused; recheck identity immediately before signalling. `kill -0` checks existence/permission, not application health. A zombie has already exited and needs its parent to reap it. Stop managed services through their service manager; direct kills may trigger automatic restarts.

## Authoritative references

- [procps-ng project](https://gitlab.com/procps-ng/procps)
- [Linux signal manual](https://man7.org/linux/man-pages/man7/signal.7.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
