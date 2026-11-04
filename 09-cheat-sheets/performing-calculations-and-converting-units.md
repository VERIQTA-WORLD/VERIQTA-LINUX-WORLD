```bash
expr 2 + 3
printf '%s\n' "$((2 + 3))"
printf '%s\n' "$((2 ** 8))"
printf '%s\n' "$((16#ff))"
printf '%x\n' 255
printf '%o\n' 255
printf '%.2f\n' 3.14159
printf 'scale=4; 22/7\n' | bc -l
printf 'sqrt(2)\n' | bc -l
printf '2 3 + p\n' | dc
awk 'BEGIN {print 2 + 3}'
awk 'BEGIN {printf "%.2f\n", 22/7}'
numfmt --to=iec 1048576
numfmt --from=iec 1M
numfmt --to=si 1000000
seq 0 2 20
factor 360
units '10 miles' kilometers
```
