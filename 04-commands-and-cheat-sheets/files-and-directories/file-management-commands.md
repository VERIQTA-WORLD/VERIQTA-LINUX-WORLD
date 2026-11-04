# Create, copy, move and remove files

File commands change directory entries or file contents. Copy creates another file; move renames or relocates an entry; deletion removes a name and is not a recycle-bin operation.

## Environment and permissions

GNU Coreutils on Linux; normal user in a disposable directory. Do not use these examples against your home directory or application data.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `mkdir -p -- PATH` | Create a directory and missing parents. |
| `touch -- FILE` | Create an empty file or update an existing file’s timestamps. |
| `cp -i -- SOURCE DEST` | Copy; ask before replacing an existing destination. |
| `cp -a -- SOURCE DEST` | Copy a tree preserving attributes where permissions allow. |
| `mv -i -- SOURCE DEST` | Move or rename; ask before replacement. |
| `ln -s -- TARGET LINK` | Create a symbolic link; relative targets are resolved from the link’s parent. |
| `rm -i -- FILE` | Remove a file with confirmation; no automatic undo. |
| `rmdir -- DIR` | Remove an empty directory. |

## Follow along

```bash
file_lab=$(mktemp -d)
mkdir -- "$file_lab/source"
printf 'first note\n' > "$file_lab/source/note.txt"
cp -i -- "$file_lab/source/note.txt" "$file_lab/copy.txt"
cmp -- "$file_lab/source/note.txt" "$file_lab/copy.txt"
mv -i -- "$file_lab/copy.txt" "$file_lab/renamed.txt"
ls -l -- "$file_lab"
rm -i -- "$file_lab/renamed.txt" "$file_lab/source/note.txt"
rmdir -- "$file_lab/source" "$file_lab"
```

## Expected results and verification

`cmp` returns 0 with no output for identical bytes. `renamed.txt` appears after the move. Answer yes to the two removal prompts only after checking their temporary paths. `rmdir` confirms no files remain by succeeding.

## Common mistakes and next checks

`>` truncates an existing file before the writing program runs. `cp -a` is not a consistent backup of a live database. `rm -r` traverses a tree; avoid it until the target has been independently checked. `--` ends option parsing for filenames beginning with `-`.

## Authoritative references

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
