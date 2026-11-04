# Create and restore a tar archive

`tar` stores files and metadata in an archive; compression reduces archive size. An archive becomes useful as a backup only when its contents, storage and restore procedure are verified.

## Environment and permissions

GNU tar on Linux; normal user with a disposable tree. `-z` uses gzip. Keep the archive outside the source tree and restore into an empty directory.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `tar -czf ARCHIVE -C DIRECTORY NAME` | Create a gzip-compressed archive from NAME relative to DIRECTORY. |
| `tar -tzf ARCHIVE` | List members without extracting. |
| `tar -xzf ARCHIVE -C DIRECTORY` | Extract into an existing directory; may overwrite matching files. |
| `tar -tvzf ARCHIVE` | Inspect member names and stored metadata. |
| `sha256sum ARCHIVE` | Compute a digest for transfer/corruption checks; not authenticity without a trusted expected digest. |

## Follow along

```bash
tar_lab=$(mktemp -d)
mkdir -- "$tar_lab/source" "$tar_lab/restore"
printf 'backup practice\n' > "$tar_lab/source/note"
tar -czf "$tar_lab/notes.tar.gz" -C "$tar_lab/source" note
tar -tzf "$tar_lab/notes.tar.gz"
tar -xzf "$tar_lab/notes.tar.gz" -C "$tar_lab/restore"
cmp -- "$tar_lab/source/note" "$tar_lab/restore/note"
rm -i -- "$tar_lab/source/note" "$tar_lab/restore/note" "$tar_lab/notes.tar.gz"
rmdir -- "$tar_lab/source" "$tar_lab/restore" "$tar_lab"
```

## Expected results and verification

Listing shows `note`, and cmp returns 0 with no output. That verifies this file’s restored bytes; it does not prove every attribute of a real backup was preserved. Cleanup removes both practice copies and archive.

## Common mistakes and next checks

Never extract an untrusted archive as root. Inspect names and symlinks and use an isolated destination; path validation alone is not a full defense. Live databases require application-consistent backups. ACLs, xattrs and SELinux labels require deliberate tar options, compatible filesystems and restore checks. gzip is compression, not encryption.

## Authoritative references

- [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
