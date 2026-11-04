```bash
sort -- FILE
sort -n -- FILE
sort -h -- FILE
sort -r -- FILE
sort -u -- FILE
sort -t: -k3,3n /etc/passwd
LC_ALL=C sort -- FILE
sort -- FILE | uniq
sort -- FILE | uniq -c
sort -- FILE | uniq -d
cut -d: -f1 /etc/passwd
cut -f1,3 FILE.tsv
cut -c1-20 -- FILE
paste FILE_ONE FILE_TWO
paste -sd, FILE
join SORTED_FILE_ONE SORTED_FILE_TWO
comm SORTED_FILE_ONE SORTED_FILE_TWO
comm -12 SORTED_FILE_ONE SORTED_FILE_TWO
tr '[:lower:]' '[:upper:]' < FILE
tr -d '\r' < FILE
tr -s '[:space:]' < FILE
expand -t 4 FILE
unexpand -t 4 FILE
fold -s -w 80 FILE
fmt -w 80 FILE
nl -ba FILE
split -l 1000 -- FILE CHUNK_PREFIX
csplit FILE '/PATTERN/' '{*}'
shuf -n 10 FILE
seq 1 10
```
