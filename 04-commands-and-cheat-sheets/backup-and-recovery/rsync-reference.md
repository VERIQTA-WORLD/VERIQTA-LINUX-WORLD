# Preview, copy and verify with rsync

`rsync` synchronizes file trees locally or over a transport such as SSH. Its source-path trailing slash changes whether you copy a directory itself or its contents.

## Environment and permissions

Linux with rsync installed; normal user for the temporary local exercise. Remote use needs rsync on both ends and authorized SSH access. Archive mode cannot preserve privileged ownership as an ordinary user.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `rsync -av SOURCE/ DEST/` | Copy contents of SOURCE into DEST; may replace existing destination files. |
| `rsync -avni SOURCE/ DEST/` | Dry run with verbose itemized proposed changes. |
| `rsync -av SOURCE DEST/` | Copy the SOURCE directory itself beneath DEST. |
| `rsync -acni SOURCE/ DEST/` | Checksum-based dry-run comparison; reads file data and can be expensive. |
| `rsync -av -e ssh SOURCE/ USER@HOST:DEST/` | Copy over SSH; host and destination must be verified. |
| `rsync -avni --delete SOURCE/ DEST/` | Preview removal of destination-only entries; omit -n only with an explicit deletion plan. |

## Follow along

```bash
sync_lab=$(mktemp -d)
mkdir -- "$sync_lab/source" "$sync_lab/backup"
printf 'copy me\n' > "$sync_lab/source/note"
rsync -avni "$sync_lab/source/" "$sync_lab/backup/"
rsync -av "$sync_lab/source/" "$sync_lab/backup/"
cmp -- "$sync_lab/source/note" "$sync_lab/backup/note"
rsync -acni "$sync_lab/source/" "$sync_lab/backup/"
rm -i -- "$sync_lab/source/note" "$sync_lab/backup/note"
rmdir -- "$sync_lab/source" "$sync_lab/backup" "$sync_lab"
```

## Expected results and verification

First dry run proposes note. Actual copy creates it; cmp succeeds. The final checksum dry run should contain no file-change entries. Summary text may still appear. Cleanup removes the two disposable copies.

## Common mistakes and next checks

`--delete` removes data from the receiver; reversed source/destination can be disastrous. A mirror can propagate corruption or deletion and is not versioned backup. Archive mode `-a` does not include ACLs (`-A`), xattrs (`-X`) or hard-link preservation (`-H`). Test required metadata and application consistency separately.

## Authoritative references

- [rsync manual](https://download.samba.org/pub/rsync/rsync.1)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
