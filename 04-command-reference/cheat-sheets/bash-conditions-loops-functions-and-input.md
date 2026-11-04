| Command | What you can do with it |
| --- | --- |
| `[[ -f FILE ]]` | Test whether a path is a regular file. |
| `[[ -d DIRECTORY ]]` | Test whether a path is a directory. |
| `[[ -r FILE ]]` | Test whether a file is readable. |
| `[[ -w FILE ]]` | Test whether a file is writable. |
| `[[ -x FILE ]]` | Test whether a file is executable. |
| `[[ -s FILE ]]` | Test whether a file has nonzero size. |
| `[[ -z "$VALUE" ]]` | Test whether a value is empty. |
| `[[ -n "$VALUE" ]]` | Test whether a value is nonempty. |
| `[[ "$LEFT" == "$RIGHT" ]]` | Compare two strings for equality. |
| `[[ "$NUMBER" -gt 10 ]]` | Compare an integer with ten. |
| `[[ "$VALUE" =~ ^[0-9]+$ ]]` | Test whether a value contains only ASCII digits. |
| `if COMMAND; then COMMAND_ON_SUCCESS; else COMMAND_ON_FAILURE; fi` | Choose a command according to another command's exit status. |
| `for item in ONE TWO THREE; do printf '%s\n' "$item"; done` | Loop over three values and print each one. |
| `while IFS= read -r line; do printf '%s\n' "$line"; done < FILE` | Read and print lines without interpreting backslashes. |
| `while IFS= read -r -d '' path; do printf '%s\n' "$path"; done < <(find DIRECTORY -type f -print0)` | Iterate safely over null-delimited filenames. |
| `case "$VALUE" in ONE) COMMAND_ONE ;; TWO) COMMAND_TWO ;; *) COMMAND_DEFAULT ;; esac` | Choose an action based on a value. |
| `function_name() { printf '%s\n' "$1"; }` | Define a shell function that prints its first argument. |
| `function_name 'VALUE'` | Call a function with one argument. |
| `read -r -p 'Value: ' VALUE` | Prompt for a value and read it literally. |
| `read -r -s -p 'Secret: ' SECRET` | Read a secret without echoing typed characters. |
| `mapfile -t lines < FILE` | Load file lines into an array in Bash 4 or later. |
| `getopts 'f:v' OPTION` | Parse short command-line options inside a script. |
| `bash -n SCRIPT.sh` | Check Bash script syntax without execution. |
| `bash SCRIPT.sh` | Run a script in Bash. |
| `shellcheck SCRIPT.sh` | Check a shell script with ShellCheck. |
