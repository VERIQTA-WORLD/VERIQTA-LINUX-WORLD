# Search text with grep

`grep` selects lines matching a pattern. Use fixed-string matching for literal text and regular expressions when you need a pattern language.

## Environment and permissions

GNU grep on Linux; no administrator access. Exit status is 0 for a match, 1 for no match, and 2 for an error.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `grep -nF -- TEXT FILE` | Print line numbers and lines containing literal text. |
| `grep -nE -- PATTERN FILE` | Use extended regular expressions. |
| `grep -i -- PATTERN FILE` | Ignore letter case. |
| `grep -v -- PATTERN FILE` | Select nonmatching lines. |
| `grep -rIl -- TEXT DIR` | Recursively list matching text-file names, skipping binary files. |
| `grep -c -- PATTERN FILE` | Count matching lines, not every individual occurrence. |

## Follow along

```bash
grep_lab=$(mktemp -d)
printf 'INFO ready\nERROR disk\nERROR network\n' > "$grep_lab/app.log"
grep -nF -- 'ERROR' "$grep_lab/app.log"
grep -c -- '^ERROR' "$grep_lab/app.log"
grep -F -- 'MISSING' "$grep_lab/app.log"
printf 'previous status: %s\n' "$?"
rm -i -- "$grep_lab/app.log"
rmdir -- "$grep_lab"
```

## Expected results and verification

Numbered matches are `2:ERROR disk` and `3:ERROR network`; count is 2. The absent literal prints nothing and returns 1. The following `printf` displays that status.

## Common mistakes and next checks

Quote patterns to prevent shell expansion. `.` matches any character in regular expressions; use `-F` for a literal dot. Recursive scans of `/` are slow and noisy. A no-match exit status is expected evidence, not necessarily a broken command.

## Authoritative references

- [GNU grep manual](https://www.gnu.org/software/grep/manual/grep.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
