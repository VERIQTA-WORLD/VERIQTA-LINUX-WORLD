# Text processing

Select lines, transform text, summarize fields and connect command streams. Preview edits before replacing source files.

## Detailed references

1. [Search text with grep](grep-reference.md)
2. [Transform text with sed](sed-reference.md)
3. [Select fields and summarize with awk](awk-reference.md)
4. [Pipes, redirection and exit status](pipes-and-redirection.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Print line numbers and lines containing literal text. | `grep -nF -- TEXT FILE` | [Search text with grep](grep-reference.md) |
| Use extended regular expressions. | `grep -nE -- PATTERN FILE` | [Search text with grep](grep-reference.md) |
| Ignore letter case. | `grep -i -- PATTERN FILE` | [Search text with grep](grep-reference.md) |
| Print only lines 1 through 5. | `sed -n '1,5p' FILE` | [Transform text with sed](sed-reference.md) |
| Replace the first match on each line in output. | `sed 's/old/new/' FILE` | [Transform text with sed](sed-reference.md) |
| Replace every match on each line in output. | `sed 's/old/new/g' FILE` | [Transform text with sed](sed-reference.md) |
| Print the first whitespace-separated field. | `awk '{print $1}' FILE` | [Select fields and summarize with awk](awk-reference.md) |
| Print account names and numeric UIDs from the local account file. | `awk -F: '{print $1, $3}' /etc/passwd` | [Select fields and summarize with awk](awk-reference.md) |
| Skip a header record. | `awk 'NR > 1 {print}' FILE` | [Select fields and summarize with awk](awk-reference.md) |
| Replace FILE with stdout; creates or truncates it. | `COMMAND > FILE` | [Pipes, redirection and exit status](pipes-and-redirection.md) |
| Append stdout; creates FILE if needed. | `COMMAND >> FILE` | [Pipes, redirection and exit status](pipes-and-redirection.md) |
| Write standard error separately. | `COMMAND 2> ERRORS` | [Pipes, redirection and exit status](pipes-and-redirection.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
