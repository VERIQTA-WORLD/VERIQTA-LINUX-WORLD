| Command | What you can do with it |
| --- | --- |
| `grep -- PATTERN FILE` | Print lines matching a regular expression. |
| `grep -n -- PATTERN FILE` | Include line numbers with matching lines. |
| `grep -nF -- 'LITERAL TEXT' FILE` | Search for literal text rather than a regular expression. |
| `grep -ni -- PATTERN FILE` | Search without case sensitivity and include line numbers. |
| `grep -nE -- 'PATTERN_ONE\|PATTERN_TWO' FILE` | Match either of two extended regular expressions. |
| `grep -v -- PATTERN FILE` | Print nonmatching lines. |
| `grep -c -- PATTERN FILE` | Count matching lines. |
| `grep -l -- PATTERN FILE_ONE FILE_TWO` | List input files that contain a match. |
| `grep -L -- PATTERN FILE_ONE FILE_TWO` | List input files without a match. |
| `grep -w -- WORD FILE` | Match complete words. |
| `grep -x -- LINE FILE` | Match complete lines. |
| `grep -A 3 -B 3 -- PATTERN FILE` | Include three lines of context before and after each match. |
| `grep -rIn -- PATTERN DIRECTORY` | Search recursively with line numbers while skipping binary files. |
| `grep -rIl -- PATTERN DIRECTORY` | List matching text-file names recursively. |
| `grep -q -- PATTERN FILE` | Test whether any match exists using the exit status. |
| `rg PATTERN DIRECTORY` | Search recursively with ripgrep and its default ignore rules. |
| `rg -n -i PATTERN DIRECTORY` | Search with ripgrep without case sensitivity and include line numbers. |
| `rg -F 'LITERAL TEXT' DIRECTORY` | Search for literal text with ripgrep. |
| `rg -g '*.conf' PATTERN DIRECTORY` | Restrict a ripgrep search to configuration filenames. |
| `rg --files DIRECTORY` | List files visible to ripgrep's traversal rules. |
| `rg -l PATTERN DIRECTORY` | List matching filenames with ripgrep. |
| `rg -v PATTERN FILE` | Print lines that do not match with ripgrep. |
| `zgrep -n -- PATTERN FILE.gz` | Search compressed gzip text with line numbers. |
