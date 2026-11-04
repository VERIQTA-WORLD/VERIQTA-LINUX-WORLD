| Command | What you can do with it |
| --- | --- |
| `find DIRECTORY -name '*.log'` | Find paths whose names match a case-sensitive log pattern. |
| `find DIRECTORY -iname '*.conf'` | Find names matching a configuration-file pattern without case sensitivity. |
| `find DIRECTORY -type f` | Find regular files. |
| `find DIRECTORY -type d` | Find directories. |
| `find DIRECTORY -type l` | Find symbolic links. |
| `find DIRECTORY -maxdepth 2 -type f` | Find regular files no more than two levels below the starting path. |
| `find DIRECTORY -type f -size +100M` | Find regular files larger than 100 MiB. |
| `find DIRECTORY -type f -empty` | Find empty regular files. |
| `find DIRECTORY -type d -empty` | Find empty directories. |
| `find DIRECTORY -type f -mtime -1` | Find files modified within the last 24 hours. |
| `find DIRECTORY -type f -mtime +7` | Find files whose rounded-down age in days is greater than seven. |
| `find DIRECTORY -type f -mmin -30` | Find files modified within the last 30 minutes. |
| `find DIRECTORY -type f -newer REFERENCE_FILE` | Find files newer than a reference file. |
| `find DIRECTORY -user ACCOUNT` | Find paths owned by an account. |
| `find DIRECTORY -group GROUP` | Find paths belonging to a group. |
| `find DIRECTORY -perm -4000` | Find paths with the set-user-ID bit set. |
| `find DIRECTORY -perm -2000` | Find paths with the set-group-ID bit set. |
| `find DIRECTORY -perm -0002` | Find paths writable by others. |
| `find DIRECTORY -xdev -type f` | Find files without crossing filesystem boundaries. |
| `find DIRECTORY -type f -name '*.log' -exec wc -l -- {} +` | Count lines in matching log files while handling spaces in names. |
| `find DIRECTORY -type f -print0 \| xargs -0 -r file --` | Identify file types using null-delimited filenames. |
| `find DIRECTORY -path '*/.git' -prune -o -type f -print` | List files while excluding .git directory trees. |
| `locate -- PATTERN` | Search an existing filename database. |
| `locate -i -- PATTERN` | Search a filename database without case sensitivity. |
| `fd PATTERN DIRECTORY` | Search with the optional fd tool using its default filtering rules. |
