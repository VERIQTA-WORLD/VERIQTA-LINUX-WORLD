| Command | What you can do with it |
| --- | --- |
| `sort -- FILE` | Sort lines lexically using the current locale. |
| `sort -n -- FILE` | Sort lines numerically. |
| `sort -h -- FILE` | Sort human-readable numbers such as 1K and 2M. |
| `sort -r -- FILE` | Reverse the sort order. |
| `sort -u -- FILE` | Sort lines and remove duplicates. |
| `sort -t: -k3,3n /etc/passwd` | Sort passwd records numerically by UID. |
| `LC_ALL=C sort -- FILE` | Sort with deterministic byte-based collation. |
| `sort -- FILE \| uniq` | Sort lines and collapse adjacent duplicates. |
| `sort -- FILE \| uniq -c` | Count occurrences of each sorted line. |
| `sort -- FILE \| uniq -d` | Print only lines that occur more than once. |
| `cut -d: -f1 /etc/passwd` | Extract account names from colon-separated records. |
| `cut -f1,3 FILE.tsv` | Extract the first and third tab-separated fields. |
| `cut -c1-20 -- FILE` | Extract the first 20 character positions. |
| `paste FILE_ONE FILE_TWO` | Combine corresponding lines with tab separators. |
| `paste -sd, FILE` | Combine all lines into one comma-separated line. |
| `join SORTED_FILE_ONE SORTED_FILE_TWO` | Join two pre-sorted files on their default first field. |
| `comm SORTED_FILE_ONE SORTED_FILE_TWO` | Compare sorted files in three columns. |
| `comm -12 SORTED_FILE_ONE SORTED_FILE_TWO` | Print lines present in both sorted files. |
| `tr '[:lower:]' '[:upper:]' < FILE` | Convert lowercase characters to uppercase. |
| `tr -d '\r' < FILE` | Remove carriage-return characters. |
| `tr -s '[:space:]' < FILE` | Collapse repeated whitespace characters. |
| `expand -t 4 FILE` | Replace tabs with spaces at four-column tab stops. |
| `unexpand -t 4 FILE` | Convert eligible spaces to tabs at four-column tab stops. |
| `fold -s -w 80 FILE` | Wrap lines at spaces to a width of 80 columns. |
| `fmt -w 80 FILE` | Reflow paragraphs to a width of 80 columns. |
| `nl -ba FILE` | Number every line, including blank lines. |
| `split -l 1000 -- FILE CHUNK_PREFIX` | Split a file into chunks of 1,000 lines. |
| `csplit FILE '/PATTERN/' '{*}'` | Split a file at each occurrence of a pattern. |
| `shuf -n 10 FILE` | Select ten random input lines. |
| `seq 1 10` | Generate integers from one through ten. |
