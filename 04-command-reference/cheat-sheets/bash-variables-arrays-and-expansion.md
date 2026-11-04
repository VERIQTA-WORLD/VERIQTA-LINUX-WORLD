| Command | What you can do with it |
| --- | --- |
| `NAME='VALUE'` | Assign a shell variable. |
| `export NAME='VALUE'` | Assign and export a variable to child processes. |
| `printf '%s\n' "$NAME"` | Print a variable without word splitting. |
| `printenv NAME` | Print an exported environment variable. |
| `declare -p NAME` | Inspect a variable's declaration and attributes. |
| `unset NAME` | Remove a variable. |
| `readonly NAME='VALUE'` | Assign a value and prevent later reassignment. |
| `printf '%s\n' "${NAME:-DEFAULT}"` | Use a fallback when a variable is unset or empty. |
| `printf '%s\n' "${NAME:=DEFAULT}"` | Assign a fallback when a variable is unset or empty. |
| `printf '%s\n' "${NAME:?NAME is required}"` | Fail expansion with a message when a variable is unset or empty. |
| `printf '%s\n' "${#NAME}"` | Print a variable's character length. |
| `printf '%s\n' "${NAME#PREFIX}"` | Remove a matching shortest prefix. |
| `printf '%s\n' "${NAME%SUFFIX}"` | Remove a matching shortest suffix. |
| `printf '%s\n' "${NAME/OLD/NEW}"` | Replace the first matching substring. |
| `printf '%s\n' "${NAME//OLD/NEW}"` | Replace every matching substring. |
| `printf '%s\n' "${NAME^^}"` | Convert a value to uppercase in Bash 4 or later. |
| `printf '%s\n' "${NAME,,}"` | Convert a value to lowercase in Bash 4 or later. |
| `items=('ONE' 'TWO' 'THREE')` | Create an indexed array. |
| `printf '%s\n' "${items[@]}"` | Print each array element separately. |
| `printf '%s\n' "${!items[@]}"` | Print an array's populated indexes. |
| `printf '%s\n' "${#items[@]}"` | Print the number of array elements. |
| `declare -A values=([KEY]='VALUE')` | Create an associative array in Bash 4 or later. |
| `printf '%s\n' "${values[KEY]}"` | Read an associative-array entry. |
| `value=$(COMMAND)` | Capture a command's standard output in a variable. |
| `printf '%s\n' "$((1 + 2))"` | Evaluate integer arithmetic. |
