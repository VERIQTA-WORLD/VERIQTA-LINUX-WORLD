# Backup and recovery

Create a practice copy, inspect what it contains and demonstrate a verified restore into a separate destination.

## Detailed references

1. [Create and restore a tar archive](tar-reference.md)
2. [Preview, copy and verify with rsync](rsync-reference.md)
3. [Verify a restore before replacing data](recovery-command-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Create a gzip-compressed archive from NAME relative to DIRECTORY. | `tar -czf ARCHIVE -C DIRECTORY NAME` | [Create and restore a tar archive](tar-reference.md) |
| List members without extracting. | `tar -tzf ARCHIVE` | [Create and restore a tar archive](tar-reference.md) |
| Extract into an existing directory; may overwrite matching files. | `tar -xzf ARCHIVE -C DIRECTORY` | [Create and restore a tar archive](tar-reference.md) |
| Copy contents of SOURCE into DEST; may replace existing destination files. | `rsync -av SOURCE/ DEST/` | [Preview, copy and verify with rsync](rsync-reference.md) |
| Dry run with verbose itemized proposed changes. | `rsync -avni SOURCE/ DEST/` | [Preview, copy and verify with rsync](rsync-reference.md) |
| Copy the SOURCE directory itself beneath DEST. | `rsync -av SOURCE DEST/` | [Preview, copy and verify with rsync](rsync-reference.md) |
| Compute content digest; compare against a trusted manifest. | `sha256sum FILE` | [Verify a restore before replacing data](recovery-command-reference.md) |
| Verify files against recorded digests; paths are relative to the current directory. | `sha256sum -c MANIFEST` | [Verify a restore before replacing data](recovery-command-reference.md) |
| Inspect archive members before extraction. | `tar -tzf ARCHIVE` | [Verify a restore before replacing data](recovery-command-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
