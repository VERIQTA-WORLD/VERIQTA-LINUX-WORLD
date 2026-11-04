```bash
sed -n '1,20p' FILE
sed -n '/START/,/END/p' FILE
sed 's/OLD/NEW/' FILE
sed 's/OLD/NEW/g' FILE
sed -E 's/[[:space:]]+/ /g' FILE
sed '/^#/d' FILE
sed '/^[[:space:]]*$/d' FILE
sed '$d' FILE
sed '1d' FILE
sed -n 's/^KEY=//p' FILE
sed 's/OLD/NEW/g' FILE > NEW_FILE
awk '{print $1}' FILE
awk '{print $NF}' FILE
awk -F: '{print $1, $3}' /etc/passwd
awk 'NR > 1 {print}' FILE
awk 'NF {print}' FILE
awk '$2 > 100 {print $1, $2}' FILE
awk '{sum += $2} END {print sum}' FILE
awk '{count[$1]++} END {for (key in count) print key, count[key]}' FILE
awk '!seen[$0]++' FILE
awk 'END {print NR}' FILE
awk -v value="$VALUE" '$1 == value {print}' FILE
```
