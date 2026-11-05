# Back up personal work and rehearse restoration

[Collection home](README.md) · Previous: [Peripherals](peripherals-printing-and-removable-media.md) · Next: [Developer workstation](developer-workstation.md)

## Environment and prerequisites

A useful personal backup lets you recover work after deletion, theft, hardware failure or a bad update. Synchronization can propagate deletion, and a snapshot on the same disk can disappear with that disk. Choose protection for the failures you actually need to survive.

The exercise needs Bash, Python 3 and an ordinary account. It uses three directories under a new temporary directory: source, retained copy and independent restore target. It never reads your real home data, deletes an original document or contacts cloud storage. The fixture demonstrates byte verification and recovery, **not** an independently protected backup location.

For your real backup workflow, use an authorized separate destination, enough capacity, application-consistent capture and a documented restore method. Protect encryption keys and recovery credentials independently. Keep sensitive files out of public reports.

## Understand the components

| Category | Decide what to preserve | Restoration concern |
| --- | --- | --- |
| Original work | Documents, photos, source files and other irreplaceable data | Include less-visible folders and unsynchronized work |
| Application data | Mail archives, local databases, browser profiles and project state | Follow the app's consistency/export guidance; copying an open database can be insufficient |
| Settings | Selected desktop/app preferences and input/accessibility requirements | Hardware-specific display/audio state may not transfer sensibly |
| Credentials | Password-manager recovery, encryption material and appropriate key backups | Use the application's protected backup process, not a public plaintext inventory |
| Software inventory | Package origins, application IDs and required versions | Reinstalling packages is different from restoring documents |
| Cache/build outputs | Re-creatable data | Exclude only after establishing that it is truly disposable |
| Ownership/metadata | Permissions, links, ACLs and other required attributes | Destination filesystem/tool capabilities determine what survives |

Define how much recent work you can afford to lose and how long restoration may take. A backup schedule without a restore test is an unverified assumption. Consider an offline or otherwise independently protected copy in addition to an online destination; the exact design depends on your risk and access requirements.

## Follow along

### 1. Rehearse a verified restore in isolation

The example writes a source document and manifest, copies it to a retained location, then restores into a different directory. It deliberately corrupts the **restored copy only**, detects that failure and restores it again. Your retained source and copy remain untouched during corruption.

<!-- workstation:exercise -->
```bash
backup_lab=$(mktemp -d) || exit 1
python3 - "$backup_lab" <<'PY'
import hashlib
import json
from pathlib import Path
import shutil
import sys
root = Path(sys.argv[1])
source, retained, restored = [root / name for name in ['source', 'retained', 'restored']]
for directory in [source, retained, restored]:
    directory.mkdir()
original = source / 'document.txt'
original.write_bytes(b'Original workstation practice document\n')
digest = hashlib.sha256(original.read_bytes()).hexdigest()
(root / 'manifest.json').write_text(json.dumps({'document.txt': digest}) + '\n')
shutil.copy2(original, retained / 'document.txt')
shutil.copy2(retained / 'document.txt', restored / 'document.txt')
assert hashlib.sha256((restored / 'document.txt').read_bytes()).hexdigest() == digest
print('PASS: independent restore target matches the recorded source digest')
(restored / 'document.txt').write_bytes(b'Corrupted restored copy only\n')
assert hashlib.sha256((restored / 'document.txt').read_bytes()).hexdigest() != digest
print('PASS: corruption of the restored copy is detected')
shutil.copy2(retained / 'document.txt', restored / 'document.txt')
assert (restored / 'document.txt').read_bytes() == original.read_bytes()
assert hashlib.sha256((retained / 'document.txt').read_bytes()).hexdigest() == digest
print('PASS: re-restoration recovers exact bytes; retained copy is unchanged')
PY
```

A manifest stored beside data is useful for detecting accidental mismatch. It is not independent proof against an attacker able to replace both. `copy2` attempts to preserve supported metadata; this fixture does not test ACLs, extended attributes, sparse files, hard links, encryption or application consistency.

### 2. Define your real selection

Make a private list of important folders and application-specific export/restore requirements. Include work outside standard Documents/Pictures folders, local repositories with unpushed commits, and accessibility settings needed to use a replacement machine. Do not treat a remote Git repository as a backup of untracked files or secrets that should never be committed.

Choose a maintained backup application supported by your distribution, such as its desktop backup tool or a documented dedicated backup program. Read retention, encryption, exclusion and restore instructions before the first job. Avoid a universal recursive copy of your entire live `/` tree; devices, virtual filesystems, mounts and active databases need different treatment.

### 3. Verify a real backup without overwriting current work

1. Complete a backup and inspect its reported status and selected content. Confirm the destination is the expected mounted device or remote account rather than an empty mountpoint on your root filesystem.
2. Restore a representative non-sensitive file to a **new empty directory**, not over the current original.
3. Open it in the intended application and compare content. Where appropriate, compare exact bytes against a known unchanged original. Test required metadata separately.
4. Confirm you can recover an earlier version or deleted file if your policy promises that capability.
5. Record elapsed time, required credentials and anything missing. Test recovery of encryption keys through the tool's supported route without exposing them.

An encrypted archive that you cannot unlock on a replacement machine does not meet the recovery goal. A cloud destination that silently stopped authenticating months ago does not provide the expected recent recovery point.

### 4. Migrate deliberately

On a replacement system, create the intended account and install supported applications from trusted sources. Restore personal data first into a separate staging location. Resolve ownership through supported tools and the actual account mapping; matching user names do not guarantee matching numeric IDs.

Import application data according to its version compatibility rules. Bring selected preferences across gradually. Do not overwrite the replacement system's entire `/etc`, graphics state or desktop database with another machine's copy. Verify work, accessibility, backups and key access on the replacement before retiring the original.

## Verify and recover

The fixture should print three `PASS` lines. Your real restore succeeds only when representative content and application behavior meet your needs at an independently protected destination and within your recovery objectives.

If a restore fails, keep the original and retained backup unchanged. Try a new restore directory, inspect the tool's exact error and check destination permissions/capacity, backup version and credentials. Do not prune history or reset repositories while investigating the only surviving copy.

| False confidence | Better evidence |
| --- | --- |
| “The backup icon is green” | Selected files restored and opened correctly |
| “Cloud sync is enabled” | Version/deletion recovery and independent account access tested |
| “I have a snapshot” | Required failure domains and restore procedure evaluated |
| “The copy has the right size” | Content and required metadata checked |

## Cleanup

Remove the disposable fixture only after verification:

<!-- workstation:cleanup -->
```bash
rm -i -- "$backup_lab/source/document.txt" "$backup_lab/retained/document.txt" "$backup_lab/restored/document.txt" "$backup_lab/manifest.json"
rmdir -- "$backup_lab/source" "$backup_lab/retained" "$backup_lab/restored"
rmdir -- "$backup_lab"
```

Do not delete real backups as lesson cleanup. Retention/pruning is a separate policy decision after you know what must remain recoverable. See [system backup operations](../06-system-administration/backup-and-restore-operations.md) for operational depth.

## Checkpoint

You can demonstrate an isolated restore, identify the failure domains your real backup survives, and explain why migration is more than copying settings onto a different machine.

## Sources

Use [GNOME backup help](https://help.gnome.org/gnome-help/backup-how.html), [Déjà Dup documentation](https://apps.gnome.org/DejaDup/), [Borg backup documentation](https://borgbackup.readthedocs.io/), [restic documentation](https://restic.readthedocs.io/), [Python shutil metadata limitations](https://docs.python.org/3/library/shutil.html) and [Python hashlib](https://docs.python.org/3/library/hashlib.html). Select a specific tool's current procedure rather than mixing repository formats or retention flags across tools.
