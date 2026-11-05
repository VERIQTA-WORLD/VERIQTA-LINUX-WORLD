# Linux filesystem and path reference

[Reference library](README.md) · [Glossary](linux-glossary.md) · [Configuration reference](linux-configuration-file-reference.md)

## Scope and environment

Use this page to answer “What belongs at this path, who manages it, and what happens if it disappears?” A pathname is a location inside a process's mount namespace. It is not proof of a particular disk, filesystem type, persistence policy or owner.

The reference covers common Linux conventions, including GNU/systemd distributions and desktop applications that follow XDG conventions. Containers, embedded systems, image-based hosts and other distributions can arrange paths differently. Inspect your system before applying a convention.

The exercise uses Bash, Python 3 and an ordinary account. It builds a small model in a new temporary directory; you do not edit `/etc`, `/usr`, `/var` or your real application settings. Optional Linux observations need the installed `findmnt`, `stat` and `readlink` utilities.

## Reference

### Top-level paths

| Path | Common purpose | Ownership, lifetime and interpretation |
| --- | --- | --- |
| `/` | Root of the visible directory tree | Can span many mounted filesystems; it is different from the root user's home |
| `/boot` | Kernel, initramfs and boot-loader assets on many systems | Boot layout varies; changing files here can prevent startup |
| `/efi` or `/boot/efi` | A mount location for an EFI System Partition | Neither location nor a separate mounted partition is universal |
| `/etc` | Host-specific configuration | Package files, administrator changes and generated content can coexist; identify the consumer before editing |
| `/usr` | Operating-system and installed software resources | Often package/image managed; it can be read-only on some systems |
| `/usr/local` | Locally installed software outside ordinary distribution package ownership | Local policy may use packages here too; do not assume everything is disposable |
| `/opt` | Add-on application trees | Vendor/application layout varies |
| `/var` | Variable persistent system data | Includes valuable state as well as logs and caches; never treat the whole tree as expendable |
| `/run` | Runtime data since boot on many modern systems | Commonly tmpfs; applications recreate required runtime objects |
| `/tmp` | Temporary working files | Cleanup policy varies; never rely on indefinite retention or assume immediate deletion at reboot |
| `/var/tmp` | Temporary data conventionally retained longer than `/tmp` | Local cleanup and storage policy still apply |
| `/home` | Homes for ordinary users on many installations | Can be a separate, remote or encrypted filesystem; not every account has a home here |
| `/root` | Conventional home directory of the root account | Not the filesystem root; permission restrictions are intentional |
| `/srv` | Data served by a system under local policy | Applications and distributions may instead use other state locations |
| `/mnt` | Conventional temporary administrator mount location | A directory under it is not proof that a mount is active |
| `/media` or `/run/media` | Removable-media mounts in some environments | Desktop/session manager policy determines the actual path |
| `/dev` | Device nodes and related interfaces | Device names can change; device nodes are not ordinary data files |
| `/proc` | Process and kernel interfaces through procfs | Much content is generated on read; some files are writable control interfaces |
| `/sys` | Device, driver and kernel object interfaces through sysfs | Writing can change live kernel/device behavior; permissions and semantics matter |

On many systems, `/bin`, `/sbin` and `/lib` are symbolic links into `/usr`. Other installations preserve separate directories. Software should not infer a system's health from one preferred layout. `readlink /bin` can reveal a link; a nonzero result can simply mean `/bin` is an ordinary directory. The [hierarchy manual](https://man7.org/linux/man-pages/man7/hier.7.html) describes conventions, including historical ones; it is not an inventory of your host.

### Paths you will inspect frequently

| Path or pattern | What you may find | What you should distinguish |
| --- | --- | --- |
| `/etc/os-release` | Operating-system identity, sometimes a symlink | Identifies user space; the running kernel is a separate observation |
| `/usr/lib/os-release` | Vendor OS identity fallback | Follow the interface's documented fallback order rather than merging both files arbitrarily |
| `/etc/fstab` | Administrator-defined mount configuration | Configuration is different from the current mount table |
| `/etc/hosts` | Static host-name mappings | Name-service policy determines whether and when an application consults it |
| `/etc/resolv.conf` | Resolver configuration or a manager-owned link | It may point at a local stub; it need not list upstream DNS servers |
| `/etc/passwd` | Account metadata | Not the password-hash database; local files are not the only possible account source |
| `/etc/shadow` | Restricted authentication metadata | Do not read, copy or publish it for a reference exercise |
| `/etc/ssh` | OpenSSH system configuration and server keys | Private host keys are secrets; a client config and a server config have different consumers |
| `/etc/systemd/system` | Administrator units and overrides | Inspect effective unit paths and drop-ins; editing vendor files risks replacement |
| `/usr/lib/systemd/system` | Packaged units on many distributions | Some systems expose these through a different path or symlink |
| `/var/lib` | Persistent application state | Databases, package state and service data may be essential for recovery |
| `/var/cache` | Re-creatable cached data by convention | An application's documented cleanup procedure still matters |
| `/var/log` | Logs and logging storage | Not every service writes a text file here; see the [log reference](linux-log-location-reference.md) |
| `/var/spool` | Queued work, mail or scheduled jobs | Pending work is state; deleting it can lose tasks |
| `/run/user/UID` | Common per-user runtime directory | Use the actual `XDG_RUNTIME_DIR`; do not manufacture this path from a guessed UID |
| `/run/lock` | Runtime locking objects on some systems | Lock semantics belong to the application; deletion is not a general repair |
| `/proc/PID/fd` | File descriptors held by a process | Visibility depends on permissions, process lifetime and namespace |
| `/proc/PID/mountinfo` | Mount information as seen by that process | Your shell and a containerized service can see different mounts |
| `/proc/self` | The process accessing this path | `cat` inspecting `/proc/self` observes `cat`, not necessarily your shell |
| `/sys/fs/cgroup` | cgroup hierarchy when mounted there | Version, controllers and delegated permissions determine available interfaces |
| `/dev/null` | Sink on write, end-of-file on read | Redirection here discards output; it does not make a failed command successful |
| `/dev/zero` | A source of zero bytes | An unbounded copy can consume storage or memory |
| `/dev/disk/by-*` | Device links based on discovered identifiers | Inspect the target and uniqueness; no naming scheme replaces checking the intended device |

A mounted filesystem can hide files that already exist underneath its mountpoint. An empty-looking directory can also mean a mount failed, a different namespace is in use, or permissions hide information. Do not “repair” it by deleting or repopulating paths before identifying the mount and the application's expectations.

### User configuration, data, state and cache

The [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/latest/) distinguishes these purposes for applications that implement it. An application may use older paths or its own rules instead.

| Variable | Default when unset or empty | Intended role |
| --- | --- | --- |
| `XDG_CONFIG_HOME` | `$HOME/.config` | User-specific configuration |
| `XDG_DATA_HOME` | `$HOME/.local/share` | User-specific data files |
| `XDG_STATE_HOME` | `$HOME/.local/state` | Persistent state such as history or application state |
| `XDG_CACHE_HOME` | `$HOME/.cache` | Non-essential data that can be re-created |
| `XDG_RUNTIME_DIR` | No universal fallback specified | Private runtime objects with an account/session-related lifetime |

These variables must contain absolute paths under the specification. Runtime directories have ownership, permission and lifetime requirements; a shared directory such as `/tmp` is not an equivalent replacement. `XDG_CONFIG_DIRS` and `XDG_DATA_DIRS` describe search locations, not an instruction to overwrite every matching file.

A backup policy should distinguish irreplaceable data from re-creatable cache, while still following application consistency requirements. A directory name alone does not prove that deleting its contents is safe. See [backups and restoration](../06-system-administration/backup-and-restore-operations.md) for operational practice.

### Inspect paths before acting

These are independent read-only Linux observations, not a script to modify the system:

| Command | Question answered | Limit |
| --- | --- | --- |
| `pwd -P` | What is this shell's physical working directory? | A process may later change its directory or namespace |
| `ls -ld -- /path` | What metadata can I see for this directory entry? | Replace `/path` with a known existing path; an error can be an access issue |
| `stat -- /path` | What metadata does this implementation report? | GNU and BSD option sets differ; a symlink can require explicit dereference options |
| `readlink -- /bin` | Is this path a symbolic link, and what is its stored target? | A relative target is interpreted from the link's parent directory |
| `findmnt --target /` | Which mount contains the specified path? | Does not establish application-level data integrity |
| `df -h /` | What filesystem capacity does this view report? | Capacity and inode exhaustion are different problems |
| `df -i /` | What inode accounting is available? | Filesystems differ; not every filesystem has a fixed inode pool |
| `getent passwd ACCOUNT` | What account information does configured name service return? | Replace `ACCOUNT`; avoid dumping account inventories into public notes |

## Follow along

Model four kinds of application files without touching real application directories. You will remove only the model's cache, then prove that configuration, user data and persistent state remain intact.

<!-- reference:exercise -->
```bash
paths_lab=$(mktemp -d) || exit 1
python3 - "$paths_lab" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
files = {
    'config/settings.txt': b'theme=dark\n',
    'data/document.txt': b'My original document\n',
    'state/history.txt': b'opened document.txt\n',
    'cache/thumbnail.txt': b're-creatable preview\n',
}
for name, content in files.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
(root / 'cache/thumbnail.txt').unlink()
assert not (root / 'cache/thumbnail.txt').exists()
for name, content in files.items():
    if not name.startswith('cache/'):
        assert (root / name).read_bytes() == content
print('PASS: selected cache removed; configuration, data and state preserved')
(root / 'cache/thumbnail.txt').write_bytes(files['cache/thumbnail.txt'])
assert (root / 'cache/thumbnail.txt').read_bytes() == files['cache/thumbnail.txt']
print('PASS: model cache re-created from known example content')
PY
```

This model encodes a deliberately simple cleanup rule. A real application's cache may be locked, shared, expensive to rebuild or actively used. Follow its documented cleanup procedure rather than translating this example into a recursive deletion of your home directory.

## Verify your result

Expect two `PASS` lines. Identify which model file is an original document and which is a preview. Explain why losing `state/history.txt` is different from losing `cache/thumbnail.txt`, even though both files were created by the application.

On Linux, optionally run `findmnt --target /` and inspect `/bin` with `ls -ld -- /bin`. Record the actual filesystem and whether `/bin` is a link. Neither result has to match a screenshot or another distribution. These observations do not prove bootability, backup completeness or that every path follows a hierarchy specification.

## Cleanup

<!-- reference:cleanup -->
```bash
rm -i -- "$paths_lab/config/settings.txt" "$paths_lab/data/document.txt" "$paths_lab/state/history.txt" "$paths_lab/cache/thumbnail.txt"
rmdir -- "$paths_lab/config" "$paths_lab/data" "$paths_lab/state" "$paths_lab/cache"
rmdir -- "$paths_lab"
```

## Sources

Use [hier(7)](https://man7.org/linux/man-pages/man7/hier.7.html), [path_resolution(7)](https://man7.org/linux/man-pages/man7/path_resolution.7.html), [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html), [sysfs(5)](https://man7.org/linux/man-pages/man5/sysfs.5.html), [mount_namespaces(7)](https://man7.org/linux/man-pages/man7/mount_namespaces.7.html) and your installed utility manuals for observed behavior. The [Filesystem Hierarchy Standard 3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) is a historical standard reference. [UAPI.9](https://uapi-group.org/specifications/specs/linux_file_system_hierarchy/) is a modern hierarchy design reference whose page identifies its own maturity; it is not a requirement implemented by every distribution. For per-user application paths, use the [XDG specification](https://specifications.freedesktop.org/basedir/latest/).
