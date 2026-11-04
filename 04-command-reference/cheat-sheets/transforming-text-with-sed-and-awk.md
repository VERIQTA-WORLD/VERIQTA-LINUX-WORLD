| Command | What you can do with it |
| --- | --- |
| `sed -n '1,20p' FILE` | Print only the first 20 lines. |
| `sed -n '/START/,/END/p' FILE` | Print lines between matching start and end patterns. |
| `sed 's/OLD/NEW/' FILE` | Replace the first match on each line in output. |
| `sed 's/OLD/NEW/g' FILE` | Replace every match on each line in output. |
| `sed -E 's/[[:space:]]+/ /g' FILE` | Collapse runs of whitespace to one space in output. |
| `sed '/^#/d' FILE` | Omit lines beginning with a hash character. |
| `sed '/^[[:space:]]*$/d' FILE` | Omit blank or whitespace-only lines. |
| `sed '$d' FILE` | Omit the last line. |
| `sed '1d' FILE` | Omit the first line. |
| `sed -n 's/^KEY=//p' FILE` | Print values from lines beginning with KEY=. |
| `sed 's/OLD/NEW/g' FILE > NEW_FILE` | Write transformed text to a separate file, replacing that destination. |
| `awk '{print $1}' FILE` | Print the first whitespace-separated field. |
| `awk '{print $NF}' FILE` | Print the final field. |
| `awk -F: '{print $1, $3}' /etc/passwd` | Print account names and numeric UIDs from the local passwd file. |
| `awk 'NR > 1 {print}' FILE` | Skip the first record. |
| `awk 'NF {print}' FILE` | Print records that contain fields. |
| `awk '$2 > 100 {print $1, $2}' FILE` | Print the first two fields when the second exceeds 100. |
| `awk '{sum += $2} END {print sum}' FILE` | Sum the second field across records. |
| `awk '{count[$1]++} END {for (key in count) print key, count[key]}' FILE` | Count occurrences of each first-field value. |
| `awk '!seen[$0]++' FILE` | Print each distinct line once while retaining its first occurrence. |
| `awk 'END {print NR}' FILE` | Print the total record count. |
| `awk -v value="$VALUE" '$1 == value {print}' FILE` | Pass a shell value to awk and select matching first fields. |
