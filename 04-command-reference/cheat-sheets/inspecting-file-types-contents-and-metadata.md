| Command | What you can do with it |
| --- | --- |
| `file -- FILE` | Identify a file's type from its contents and metadata. |
| `file -i -- FILE` | Report a file's MIME type and encoding. |
| `stat -- FILE` | Inspect file metadata and timestamps. |
| `stat -c '%a %U %G %s %n' -- FILE` | Print numeric mode, owner, group, byte size and name. |
| `stat -f -- DIRECTORY` | Inspect the filesystem containing a directory. |
| `cat -- FILE` | Print a file's contents. |
| `cat -n -- FILE` | Print file contents with line numbers. |
| `less -- FILE` | Browse a file interactively. |
| `less +F -- LOG_FILE` | Follow appended log content in an interactive pager. |
| `more -- FILE` | Browse a file one screen at a time. |
| `head -n 20 -- FILE` | Print the first 20 lines. |
| `tail -n 20 -- FILE` | Print the last 20 lines. |
| `tail -F -- LOG_FILE` | Follow a log by name across rotation or replacement. |
| `wc -l -- FILE` | Count newline characters. |
| `wc -w -- FILE` | Count words. |
| `wc -c -- FILE` | Count bytes. |
| `wc -m -- FILE` | Count characters according to the current locale. |
| `od -An -tx1 -- FILE` | Display bytes in hexadecimal. |
| `hexdump -C -- FILE` | Display hexadecimal bytes alongside printable characters. |
| `xxd FILE` | Display a file as a hexadecimal dump. |
| `strings -- FILE` | Extract printable strings. |
| `strings -n 8 -- FILE` | Extract printable strings at least eight characters long. |
| `lsattr -- FILE` | Inspect filesystem attributes such as immutable and append-only. |
| `getfattr -d -- FILE` | Inspect user extended attributes. |
