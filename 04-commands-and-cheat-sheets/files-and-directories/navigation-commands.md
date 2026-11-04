# Navigate and inspect directories

A pathname identifies a location in the filesystem. Absolute paths begin at `/`; relative paths begin at your current directory. Navigation changes the shell’s working directory, which affects every later relative path.

## Environment and permissions

Bash on GNU/Linux; no administrator access. The examples create only a temporary directory owned by you.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `pwd -P` | Print the physical current directory, resolving symbolic links. |
| `ls -lah` | List ordinary and hidden entries with metadata and readable sizes. |
| `cd -- PATH` | Change this shell’s directory; quote paths containing spaces. |
| `cd ..` | Move to the parent directory. |
| `cd -` | Return to the previous working directory. |
| `realpath -- PATH` | Resolve a path; GNU utility, availability varies. |
| `stat -- PATH` | Inspect ownership, mode, size and timestamps. |

## Follow along

```bash
nav_lab=$(mktemp -d)
mkdir -p "$nav_lab/notes/week 1"
cd -- "$nav_lab/notes/week 1"
pwd -P
cd ..
ls -lah
cd -
pwd -P
cd /
rmdir -- "$nav_lab/notes/week 1" "$nav_lab/notes" "$nav_lab"
```

## Expected results and verification

The first and second `pwd` point to `notes/week 1`. The listing in between contains `week 1`. Successful `rmdir` prints nothing and removes only empty directories. The final working directory is `/`; use `cd` to return home.

## Common mistakes and next checks

`~` expands to your home directory when unquoted; `"~"` is a literal name. Linux names are case sensitive. `ls` hides dotfiles unless requested. A permission error can mean a missing search (`x`) permission on a parent directory. Use `ls -ld` on parents before assuming a file is missing.

## Authoritative references

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
