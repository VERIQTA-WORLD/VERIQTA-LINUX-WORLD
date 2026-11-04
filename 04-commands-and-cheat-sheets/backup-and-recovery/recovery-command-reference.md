# Verify a restore before replacing data

Recovery is the ability to restore usable data and service, not merely to create a backup file. Stage restored data separately, compare it, validate the application and plan cutover.

## Environment and permissions

GNU/Linux with Coreutils, tar and diffutils. The exercise restores one self-created file as a normal user. Real recovery needs authorization, a trusted backup, compatible application versions and a retained copy of current state.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `sha256sum FILE` | Compute content digest; compare against a trusted manifest. |
| `sha256sum -c MANIFEST` | Verify files against recorded digests; paths are relative to the current directory. |
| `tar -tzf ARCHIVE` | Inspect archive members before extraction. |
| `cmp -- EXPECTED RESTORED` | Compare file bytes; 0 identical, 1 different, higher status indicates trouble. |
| `diff -ru -- EXPECTED RESTORED` | Compare text trees recursively; contents may reveal secrets. |
| `stat -- FILE` | Inspect mode, owner, group and timestamps; bytes alone do not verify metadata. |

## Follow along

```bash
restore_lab=$(mktemp -d)
mkdir -- "$restore_lab/source" "$restore_lab/staged"
printf 'known good\n' > "$restore_lab/source/note"
( cd "$restore_lab/source" && sha256sum note > "$restore_lab/manifest" )
tar -czf "$restore_lab/backup.tar.gz" -C "$restore_lab/source" note
tar -tzf "$restore_lab/backup.tar.gz"
tar -xzf "$restore_lab/backup.tar.gz" -C "$restore_lab/staged"
( cd "$restore_lab/staged" && sha256sum -c "$restore_lab/manifest" )
diff -ru -- "$restore_lab/source" "$restore_lab/staged"
rm -i -- "$restore_lab/source/note" "$restore_lab/staged/note" "$restore_lab/manifest" "$restore_lab/backup.tar.gz"
rmdir -- "$restore_lab/source" "$restore_lab/staged" "$restore_lab"
```

## Expected results and verification

Digest verification prints `note: OK`; diff prints nothing and returns 0. This proves the exercise file matches its known-good copy. A real restore also needs ownership, access policy, application integrity and client-level checks.

## Common mistakes and next checks

A manifest stored beside a compromised backup is not independent proof of trust. Do not overwrite production data until staged validation and rollback are ready. Filesystem repair must follow filesystem-specific instructions with correct mount state and a recoverable image; do not run generic `fsck -y` against a mounted filesystem. Record recovery time and acceptable data loss for real services.

## Authoritative references

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [GNU Diffutils manual](https://www.gnu.org/software/diffutils/manual/diffutils.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
