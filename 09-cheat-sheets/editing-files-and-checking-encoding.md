| Command | What you can do with it |
| --- | --- |
| `nano FILE` | Edit a file with Nano. |
| `nano -l FILE` | Edit with Nano and display line numbers. |
| `vim FILE` | Edit a file with Vim. |
| `vim -R FILE` | Open a file in Vim's read-only mode. |
| `vim -d FILE_ONE FILE_TWO` | Compare and edit two files using Vim's diff mode. |
| `vi FILE` | Edit a file with vi. |
| `view FILE` | Open a file using the vi-family read-only frontend. |
| `emacs -nw FILE` | Edit with Emacs inside the terminal. |
| `editor FILE` | Open a file using the configured editor command. |
| `sensible-editor FILE` | Open a file using Debian's sensible editor selection. |
| `file --mime-encoding -- FILE` | Identify the apparent text encoding. |
| `iconv -l` | List supported encoding conversions. |
| `iconv -f SOURCE_ENCODING -t UTF-8 FILE > CONVERTED_FILE` | Convert text to UTF-8 and write a separate output file. |
| `dos2unix -n INPUT_FILE OUTPUT_FILE` | Convert DOS line endings into a separate output file. |
| `unix2dos -n INPUT_FILE OUTPUT_FILE` | Convert Unix line endings into a separate output file. |
| `locale` | Display active locale settings. |
| `locale -a` | List installed locales. |
| `printf '%s\n' "$EDITOR" "$VISUAL"` | Show preferred editor environment variables. |
