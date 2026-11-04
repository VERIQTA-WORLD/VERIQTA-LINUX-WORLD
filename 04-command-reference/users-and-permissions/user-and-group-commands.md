# Inspect users and groups

An account maps a name to a user ID (UID); groups collect identities for access decisions. The local files are only one identity source: directory services can also supply accounts.

## Environment and permissions

Linux with `id`, `getent` and shadow-utils. Queries usually need no elevation. Creating or changing accounts requires root and affects access; the exercise is read-only.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `whoami` | Print the effective account name. |
| `id` | Show current UID, primary group and supplementary groups. |
| `id ACCOUNT` | Inspect a named identity. |
| `getent passwd ACCOUNT` | Resolve through configured name services, not only /etc/passwd. |
| `getent group GROUP` | Resolve a group; listed members may omit users whose primary group is this group. |
| `who` | Show login sessions recorded in utmp; may be empty in containers. |
| `sudo useradd -m ACCOUNT` | Administrative syntax: create an account and home directory. |
| `sudo usermod -aG GROUP ACCOUNT` | Administrative syntax: append group membership; omitting -a replaces supplementary groups. |

## Follow along

```bash
whoami
id
getent passwd "$(id -un)"
id -nG
getent group "$(id -gn)"
```

## Expected results and verification

The account name from `whoami` normally matches `id -un`. A passwd record has seven colon-separated fields: name, password marker, UID, GID, comment, home, shell. The password marker is not the password. No cleanup is required.

## Common mistakes and next checks

New group memberships usually require a new login session; existing processes retain their groups. Debian/Ubuntu may provide the friendlier `adduser` frontend, while `useradd` defaults vary. `userdel -r` removes home data and is not a harmless account toggle. Plan account lifecycle changes in an isolated VM with recovery access.

## Authoritative references

- [shadow-utils useradd manual](https://man7.org/linux/man-pages/man8/useradd.8.html)
- [getent manual](https://man7.org/linux/man-pages/man1/getent.1.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
