```bash
file -- FILE
file -i -- FILE
stat -- FILE
stat -c '%a %U %G %s %n' -- FILE
stat -f -- DIRECTORY
cat -- FILE
cat -n -- FILE
less -- FILE
less +F -- LOG_FILE
more -- FILE
head -n 20 -- FILE
tail -n 20 -- FILE
tail -F -- LOG_FILE
wc -l -- FILE
wc -w -- FILE
wc -c -- FILE
wc -m -- FILE
od -An -tx1 -- FILE
hexdump -C -- FILE
xxd FILE
strings -- FILE
strings -n 8 -- FILE
lsattr -- FILE
getfattr -d -- FILE
```
