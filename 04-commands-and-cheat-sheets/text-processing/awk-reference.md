# Select fields and summarize with awk

`awk` processes records (usually lines), splits them into fields, and runs actions. It is useful for structured plain text and small summaries.

## Environment and permissions

POSIX-style awk on Linux; normal user. GNU awk (`gawk`) and `mawk` differ in extensions, so this page uses common features.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `awk '{print $1}' FILE` | Print the first whitespace-separated field. |
| `awk -F: '{print $1, $3}' /etc/passwd` | Print account names and numeric UIDs from the local account file. |
| `awk 'NR > 1 {print}' FILE` | Skip a header record. |
| `awk '$2 > 10 {print $1}' FILE` | Print names whose second field exceeds 10. |
| `awk '{s += $2} END {print s}' FILE` | Sum the second field across records. |

## Follow along

```bash
awk_lab=$(mktemp -d)
printf 'web 12\napi 8\nweb 5\n' > "$awk_lab/usage"
awk '$2 > 10 {print $1}' "$awk_lab/usage"
awk '{total[$1] += $2} END {for (name in total) print name, total[name]}' "$awk_lab/usage" | sort
rm -i -- "$awk_lab/usage"
rmdir -- "$awk_lab"
```

## Expected results and verification

The filter prints `web`. Sorted totals are `api 8` and `web 17`. The `END` block runs after all records; associative-array iteration order is otherwise unspecified.

## Common mistakes and next checks

Single quotes protect `$1` and `$2` from shell expansion. Default splitting treats runs of whitespace as one separator. `-F,` is not a full CSV parser: quoted commas and embedded newlines require a CSV-aware tool. Do not parse unstable human-readable output for critical automation.

## Authoritative references

- [GNU awk manual](https://www.gnu.org/software/gawk/manual/gawk.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
