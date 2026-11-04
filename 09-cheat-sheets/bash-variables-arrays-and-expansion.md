```bash
NAME='VALUE'
export NAME='VALUE'
printf '%s\n' "$NAME"
printenv NAME
declare -p NAME
unset NAME
readonly NAME='VALUE'
printf '%s\n' "${NAME:-DEFAULT}"
printf '%s\n' "${NAME:=DEFAULT}"
printf '%s\n' "${NAME:?NAME is required}"
printf '%s\n' "${#NAME}"
printf '%s\n' "${NAME#PREFIX}"
printf '%s\n' "${NAME%SUFFIX}"
printf '%s\n' "${NAME/OLD/NEW}"
printf '%s\n' "${NAME//OLD/NEW}"
printf '%s\n' "${NAME^^}"
printf '%s\n' "${NAME,,}"
items=('ONE' 'TWO' 'THREE')
printf '%s\n' "${items[@]}"
printf '%s\n' "${!items[@]}"
printf '%s\n' "${#items[@]}"
declare -A values=([KEY]='VALUE')
printf '%s\n' "${values[KEY]}"
value=$(COMMAND)
printf '%s\n' "$((1 + 2))"
```
