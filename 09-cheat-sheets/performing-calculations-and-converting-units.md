| Command | What you can do with it |
| --- | --- |
| `expr 2 + 3` | Add two integers with expr. |
| `printf '%s\n' "$((2 + 3))"` | Evaluate integer addition in the shell. |
| `printf '%s\n' "$((2 ** 8))"` | Evaluate integer exponentiation in Bash. |
| `printf '%s\n' "$((16#ff))"` | Interpret a hexadecimal integer. |
| `printf '%x\n' 255` | Format an integer as hexadecimal. |
| `printf '%o\n' 255` | Format an integer as octal. |
| `printf '%.2f\n' 3.14159` | Print a number with two decimal places. |
| `printf 'scale=4; 22/7\n' \| bc -l` | Calculate a division result to four decimal places. |
| `printf 'sqrt(2)\n' \| bc -l` | Calculate a square root using bc's math library. |
| `printf '2 3 + p\n' \| dc` | Calculate addition using dc's stack-based notation. |
| `awk 'BEGIN {print 2 + 3}'` | Calculate a value using awk. |
| `awk 'BEGIN {printf "%.2f\n", 22/7}'` | Format an awk calculation to two decimal places. |
| `numfmt --to=iec 1048576` | Format a byte count using IEC suffixes. |
| `numfmt --from=iec 1M` | Convert an IEC-suffixed quantity to a number. |
| `numfmt --to=si 1000000` | Format a number using SI suffixes. |
| `seq 0 2 20` | Generate even integers from zero through twenty. |
| `factor 360` | Factor an integer into prime factors. |
| `units '10 miles' kilometers` | Convert miles into kilometers with the units utility. |
