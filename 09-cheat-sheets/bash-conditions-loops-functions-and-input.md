```bash
[[ -f FILE ]]
[[ -d DIRECTORY ]]
[[ -r FILE ]]
[[ -w FILE ]]
[[ -x FILE ]]
[[ -s FILE ]]
[[ -z "$VALUE" ]]
[[ -n "$VALUE" ]]
[[ "$LEFT" == "$RIGHT" ]]
[[ "$NUMBER" -gt 10 ]]
[[ "$VALUE" =~ ^[0-9]+$ ]]
if COMMAND; then COMMAND_ON_SUCCESS; else COMMAND_ON_FAILURE; fi
for item in ONE TWO THREE; do printf '%s\n' "$item"; done
while IFS= read -r line; do printf '%s\n' "$line"; done < FILE
while IFS= read -r -d '' path; do printf '%s\n' "$path"; done < <(find DIRECTORY -type f -print0)
case "$VALUE" in ONE) COMMAND_ONE ;; TWO) COMMAND_TWO ;; *) COMMAND_DEFAULT ;; esac
function_name() { printf '%s\n' "$1"; }
function_name 'VALUE'
read -r -p 'Value: ' VALUE
read -r -s -p 'Secret: ' SECRET
mapfile -t lines < FILE
getopts 'f:v' OPTION
bash -n SCRIPT.sh
bash SCRIPT.sh
shellcheck SCRIPT.sh
```
