| Command | What you can do with it |
| --- | --- |
| `rsync -avni SOURCE_DIRECTORY/ DESTINATION_DIRECTORY/` | Preview an archive-mode synchronization with itemized changes. |
| `rsync -av SOURCE_DIRECTORY/ DESTINATION_DIRECTORY/` | Copy a directory's contents while preserving supported archive attributes. |
| `rsync -acni SOURCE_DIRECTORY/ DESTINATION_DIRECTORY/` | Compare source and destination using checksums without making changes. |
| `rsync -av --exclude='PATTERN' SOURCE_DIRECTORY/ DESTINATION_DIRECTORY/` | Copy a directory's contents while excluding matching names. |
| `rsync -av --progress SOURCE_DIRECTORY/ DESTINATION_DIRECTORY/` | Copy a directory's contents and show transfer progress. |
| `rsync -av -e ssh SOURCE_DIRECTORY/ ACCOUNT@HOST:DESTINATION_DIRECTORY/` | Copy a directory's contents to an authorized host over SSH. |
| `rsync -av -e 'ssh -p PORT' SOURCE_DIRECTORY/ ACCOUNT@HOST:DESTINATION_DIRECTORY/` | Copy over SSH using a custom port. |
| `rsync -av --backup --backup-dir=BACKUP_DIRECTORY SOURCE_DIRECTORY/ DESTINATION_DIRECTORY/` | Retain replaced destination files in a backup directory during synchronization. |
| `sha256sum -c MANIFEST` | Verify files against a digest manifest. |
| `cmp -- ORIGINAL_FILE RESTORED_FILE` | Compare an original file with a restored file byte for byte. |
| `diff -ru -- ORIGINAL_DIRECTORY RESTORED_DIRECTORY` | Compare original and restored directory trees. |
| `getfacl -R -- DIRECTORY > ACL_BACKUP_FILE` | Save a recursive ACL listing to a file. |
| `getfattr -R -d -- DIRECTORY > XATTR_BACKUP_FILE` | Save recursive user extended attributes to a file. |
| `restic snapshots` | List snapshots in the configured restic repository. |
| `restic check` | Check restic repository consistency. |
| `restic ls SNAPSHOT_ID` | List paths within a restic snapshot. |
| `restic backup DIRECTORY` | Back up a directory to the configured restic repository. |
| `restic restore SNAPSHOT_ID --target EMPTY_RESTORE_DIRECTORY` | Restore a restic snapshot into a separate destination. |
| `borg list REPOSITORY` | List archives in a Borg 1.x repository. |
| `borg info REPOSITORY` | Inspect a Borg 1.x repository. |
| `borg list REPOSITORY::ARCHIVE` | List members of a Borg 1.x archive. |
| `rclone listremotes` | List configured rclone remotes. |
| `rclone lsd REMOTE:` | List directories on an rclone remote. |
| `rclone copy --dry-run SOURCE_DIRECTORY REMOTE:DESTINATION` | Preview a copy to a remote without transferring files. |
