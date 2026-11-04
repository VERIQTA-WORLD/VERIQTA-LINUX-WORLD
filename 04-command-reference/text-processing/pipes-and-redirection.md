# Pipes, redirection and exit status

A pipe connects one program’s standard output to another’s standard input. Redirection sends streams to files. Standard error remains separate unless explicitly redirected.

## Environment and permissions

Bash on Linux; normal user. `pipefail` is a Bash option and should not be assumed in every `/bin/sh` implementation.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `COMMAND > FILE` | Replace FILE with stdout; creates or truncates it. |
| `COMMAND >> FILE` | Append stdout; creates FILE if needed. |
| `COMMAND 2> ERRORS` | Write standard error separately. |
| `COMMAND > FILE 2>&1` | Send stdout and stderr to the same file; order matters. |
| `A \| B` | Pipe stdout from A to B; stderr stays on the terminal. |
| `set -o pipefail` | Make a pipeline fail if any component fails; status is the rightmost failure. |
| `A && B` | Run B only if A succeeds. |
| `A \|\| B` | Run B only if A fails. |

## Follow along

```bash
pipe_lab=$(mktemp -d)
printf 'pear\napple\npear\n' > "$pipe_lab/items"
sort "$pipe_lab/items" | uniq -c > "$pipe_lab/counts"
cat -- "$pipe_lab/counts"
( set -o pipefail; false | cat; printf 'pipeline status: %s\n' "$?" )
rm -i -- "$pipe_lab/items" "$pipe_lab/counts"
rmdir -- "$pipe_lab"
```

## Expected results and verification

Counts show one apple and two pears (spacing varies). The subshell prints pipeline status 1. Parentheses keep the option change local to the exercise.

## Common mistakes and next checks

`2>&1 >file` differs from `>file 2>&1`: redirections apply left to right. A pipeline normally reports only its final command’s status. `sudo echo text > /root/file` does not elevate the shell redirection. Privileged file writes require a reviewed destination and a tool such as `sudo tee`; `tee` also overwrites by default.

## Authoritative references

- [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
