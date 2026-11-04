```bash
find DIRECTORY -name '*.log'
find DIRECTORY -iname '*.conf'
find DIRECTORY -type f
find DIRECTORY -type d
find DIRECTORY -type l
find DIRECTORY -maxdepth 2 -type f
find DIRECTORY -type f -size +100M
find DIRECTORY -type f -empty
find DIRECTORY -type d -empty
find DIRECTORY -type f -mtime -1
find DIRECTORY -type f -mtime +7
find DIRECTORY -type f -mmin -30
find DIRECTORY -type f -newer REFERENCE_FILE
find DIRECTORY -user ACCOUNT
find DIRECTORY -group GROUP
find DIRECTORY -perm -4000
find DIRECTORY -perm -2000
find DIRECTORY -perm -0002
find DIRECTORY -xdev -type f
find DIRECTORY -type f -name '*.log' -exec wc -l -- {} +
find DIRECTORY -type f -print0 | xargs -0 -r file --
find DIRECTORY -path '*/.git' -prune -o -type f -print
locate -- PATTERN
locate -i -- PATTERN
fd PATTERN DIRECTORY
```
