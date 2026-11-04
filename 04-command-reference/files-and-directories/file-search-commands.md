# Find files by name, type and metadata

`find` walks directory trees and evaluates tests. It searches names and metadata; use `grep` to search file contents. Narrowing the starting directory reduces noise and cost.

## Environment and permissions

GNU Findutils on Linux; normal user. The exercise creates two files. Administrative searches may expose paths you should not publish.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `find PATH -type f -name PATTERN` | Find regular files matching a case-sensitive shell pattern. |
| `find PATH -type d` | Find directories. |
| `find PATH -iname PATTERN` | Match names without case sensitivity; GNU extension. |
| `find PATH -type f -size +100M` | Find regular files larger than 100 units of 1 MiB. |
| `find PATH -type f -mtime +7` | Match files with rounded-down age in days greater than 7. |
| `find PATH -type f -exec COMMAND {} +` | Pass found paths as arguments in batches; handles spaces. |

## Follow along

```bash
search_lab=$(mktemp -d)
printf 'hello\n' > "$search_lab/notes one.txt"
printf 'other\n' > "$search_lab/notes.log"
find "$search_lab" -type f -name '*.txt' -print
find "$search_lab" -type f -name '*.txt' -exec wc -l -- {} +
rm -i -- "$search_lab/notes one.txt" "$search_lab/notes.log"
rmdir -- "$search_lab"
```

## Expected results and verification

Only `notes one.txt` matches `*.txt`; its line count is 1. The quoted pattern reaches `find` unchanged. Remove both temporary files after checking the prompts.

## Common mistakes and next checks

Do not pipe newline-separated names into plain `xargs`; use `-exec … {} +` or `-print0` with `xargs -0`. `-delete` is a destructive action, not a filter. Preview matches first and understand traversal behavior. An unreadable directory can produce errors alongside valid matches; inspect the exit status.

## Authoritative references

- [GNU Findutils manual](https://www.gnu.org/software/findutils/manual/html_mono/find.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
