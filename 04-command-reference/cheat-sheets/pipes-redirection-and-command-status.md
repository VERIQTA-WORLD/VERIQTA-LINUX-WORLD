| Command | What you can do with it |
| --- | --- |
| `COMMAND > OUTPUT_FILE` | Write standard output to a file, replacing its contents. |
| `COMMAND >> OUTPUT_FILE` | Append standard output to a file. |
| `COMMAND 2> ERROR_FILE` | Write standard error to a file, replacing its contents. |
| `COMMAND > OUTPUT_FILE 2> ERROR_FILE` | Write standard output and error to separate files. |
| `COMMAND > OUTPUT_FILE 2>&1` | Write standard output and error to the same file. |
| `COMMAND_ONE \| COMMAND_TWO` | Send one command's standard output to another's input. |
| `COMMAND_ONE 2>&1 \| COMMAND_TWO` | Send both output streams from the first command into a pipe. |
| `COMMAND \| tee OUTPUT_FILE` | Display output and copy it to a file, replacing that file. |
| `COMMAND \| tee -a OUTPUT_FILE` | Display output and append it to a file. |
| `COMMAND < INPUT_FILE` | Read standard input from a file. |
| `COMMAND_ONE && COMMAND_TWO` | Run the second command only if the first succeeds. |
| `COMMAND_ONE \|\| COMMAND_TWO` | Run the second command only if the first fails. |
| `printf '%s\n' "$?"` | Print the preceding command's exit status. |
| `set -o pipefail` | Make a Bash pipeline report its rightmost failing component. |
| `set +o pipefail` | Restore Bash's default final-command pipeline status. |
| `printf '%s\n' "${PIPESTATUS[@]}"` | Print the preceding pipeline's individual exit statuses. |
| `COMMAND &` | Start a command in the background. |
| `wait` | Wait for the shell's outstanding child processes. |
| `true` | Return success. |
| `false` | Return failure. |
| `:` | Run Bash's no-operation builtin successfully. |
