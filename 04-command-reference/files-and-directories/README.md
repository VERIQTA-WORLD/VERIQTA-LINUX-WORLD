# Files and directories

Locate yourself, inspect paths, manage files and find names. Start here before using relative paths in any other reference.

## Detailed references

1. [Navigate and inspect directories](navigation-commands.md)
2. [Create, copy, move and remove files](file-management-commands.md)
3. [Find files by name, type and metadata](file-search-commands.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Print the physical current directory, resolving symbolic links. | `pwd -P` | [Navigate and inspect directories](navigation-commands.md) |
| List ordinary and hidden entries with metadata and readable sizes. | `ls -lah` | [Navigate and inspect directories](navigation-commands.md) |
| Change this shell’s directory; quote paths containing spaces. | `cd -- PATH` | [Navigate and inspect directories](navigation-commands.md) |
| Create a directory and missing parents. | `mkdir -p -- PATH` | [Create, copy, move and remove files](file-management-commands.md) |
| Create an empty file or update an existing file’s timestamps. | `touch -- FILE` | [Create, copy, move and remove files](file-management-commands.md) |
| Copy; ask before replacing an existing destination. | `cp -i -- SOURCE DEST` | [Create, copy, move and remove files](file-management-commands.md) |
| Find regular files matching a case-sensitive shell pattern. | `find PATH -type f -name PATTERN` | [Find files by name, type and metadata](file-search-commands.md) |
| Find directories. | `find PATH -type d` | [Find files by name, type and metadata](file-search-commands.md) |
| Match names without case sensitivity; GNU extension. | `find PATH -iname PATTERN` | [Find files by name, type and metadata](file-search-commands.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
